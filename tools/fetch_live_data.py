#!/usr/bin/env python3
"""Universe of Finance — Live Layer feed fetcher (Tier 1: ledger-verified chains).

Runs in GitHub Actions (no CORS constraints there), fetches transaction throughput
from genuinely open, keyless chain APIs, and writes data/live/chains.json which the
static site reads as its API.

Design rules (from the Live Layer build brief):
- stdlib only (urllib) — no pip install step needed on the runner.
- Every feed payload carries: value, unit, source_url, retrieved_at, period_covered, method.
- Graceful degradation: if a feed is unreachable, KEEP the last committed value and mark it
  stale (never blank, never fake). The previous chains.json is read for this purpose.
- Each feed is isolated in try/except so one dead endpoint never breaks the others.
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "live" / "chains.json"
UA = "UniverseOfFinance-LiveLayer/1.0 (+https://github.com/quackstra/universe-of-finance)"
TIMEOUT = 15


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _get(url: str, data: bytes | None = None, headers: dict | None = None):
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("User-Agent", UA)
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8"))


def _rpc(url: str, method: str, params: list):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    return _get(url, data=body)


# ── Tier 1 feeds ─────────────────────────────────────────────────────────────

def feed_bitcoin() -> dict:
    """mempool.space — confirmed TPS from the span of recent blocks."""
    url = "https://mempool.space/api/v1/blocks"
    blocks = _get(url)  # newest-first list, each with tx_count + timestamp
    recent = blocks[:10]
    # tx confirmed across the closed interval between newest and oldest block header times
    newest_ts = recent[0]["timestamp"]
    oldest_ts = recent[-1]["timestamp"]
    span = max(newest_ts - oldest_ts, 1)
    # count txns in all but the newest block (those confirmed within the span)
    txs = sum(b["tx_count"] for b in recent[1:])
    return {
        "label": "Bitcoin",
        "tps": round(txs / span, 3),
        "unit": "tps",
        "method": "ledger",
        "source_url": url,
        "period_covered": f"last {len(recent)} blocks (~{round(span/60)} min)",
        "extra": {"block_height": recent[0].get("height")},
    }


def feed_ethereum() -> dict:
    """Public RPC — TPS from the latest block's tx count over its block time."""
    url = "https://ethereum-rpc.publicnode.com"
    latest = _rpc(url, "eth_getBlockByNumber", ["latest", False])["result"]
    num = int(latest["number"], 16)
    parent = _rpc(url, "eth_getBlockByNumber", [hex(num - 1), False])["result"]
    span = max(int(latest["timestamp"], 16) - int(parent["timestamp"], 16), 1)
    txs = len(latest["transactions"])
    return {
        "label": "Ethereum",
        "tps": round(txs / span, 3),
        "unit": "tps",
        "method": "ledger",
        "source_url": url,
        "period_covered": f"block {num} ({span}s)",
        "extra": {"block_height": num},
    }


def feed_solana() -> dict:
    """Public RPC getRecentPerformanceSamples — includes vote txns (flagged)."""
    url = "https://api.mainnet-beta.solana.com"
    samples = _rpc(url, "getRecentPerformanceSamples", [1])["result"]
    s = samples[0]
    period = max(s["samplePeriodSecs"], 1)
    total_tps = round(s["numTransactions"] / period, 1)
    non_vote = s.get("numNonVoteTransactions")
    out = {
        "label": "Solana",
        "tps": total_tps,
        "unit": "tps",
        "method": "ledger",
        "source_url": url,
        "period_covered": f"{period}s performance sample",
        "note": "includes consensus vote txns",
    }
    if non_vote is not None:
        out["non_vote_tps"] = round(non_vote / period, 1)
    return out


def feed_radix() -> dict:
    """Radix Babylon Gateway — TPS from the span of the recent transaction stream."""
    url = "https://mainnet.radixdlt.com/stream/transactions"
    body = json.dumps({"limit_per_page": 100, "order": "desc"}).encode()
    resp = _get(url, data=body)
    items = resp.get("items", [])
    stamped = [i["confirmed_at"] for i in items if i.get("confirmed_at")]
    if len(stamped) < 2:
        raise ValueError("insufficient timestamped transactions")
    to_dt = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
    newest, oldest = to_dt(stamped[0]), to_dt(stamped[-1])
    span = max((newest - oldest).total_seconds(), 1)
    return {
        "label": "Radix",
        "tps": round(len(stamped) / span, 3),
        "unit": "tps",
        "method": "ledger",
        "source_url": "https://mainnet.radixdlt.com",
        "period_covered": f"last {len(stamped)} txns (~{round(span)}s)",
        "extra": {"state_version": items[0].get("state_version")},
    }


def feed_xrpl() -> dict:
    """XRPL public cluster — TPS from the latest validated ledger's tx count."""
    url = "https://xrplcluster.com"
    body = json.dumps({
        "method": "ledger",
        "params": [{"ledger_index": "validated", "transactions": True, "expand": False}],
    }).encode()
    resp = _get(url, data=body)
    ledger = resp["result"]["ledger"]
    txs = len(ledger.get("transactions", []))
    # XRPL closes a ledger roughly every 3-4s
    return {
        "label": "XRP Ledger",
        "tps": round(txs / 4.0, 3),
        "unit": "tps",
        "method": "ledger",
        "source_url": url,
        "period_covered": f"ledger {ledger.get('ledger_index')} (~4s close)",
        "extra": {"ledger_index": ledger.get("ledger_index")},
    }


FEEDS = {
    "bitcoin": feed_bitcoin,
    "ethereum": feed_ethereum,
    "solana": feed_solana,
    "radix": feed_radix,
    "xrpl": feed_xrpl,
}


def main() -> int:
    prev = {}
    if OUT.exists():
        try:
            prev = json.loads(OUT.read_text()).get("feeds", {})
        except Exception:
            prev = {}

    feeds = {}
    ok = 0
    for key, fn in FEEDS.items():
        try:
            payload = fn()
            payload["retrieved_at"] = now_iso()
            payload["status"] = "ok"
            feeds[key] = payload
            ok += 1
            print(f"[ok]   {key}: {payload['tps']} tps")
        except Exception as e:  # keep last-good value, mark stale
            print(f"[fail] {key}: {e}", file=sys.stderr)
            if key in prev:
                stale = dict(prev[key])
                stale["status"] = "stale"
                stale["last_error"] = str(e)[:200]
                stale["last_attempt"] = now_iso()
                feeds[key] = stale
            else:
                feeds[key] = {
                    "label": key.title(),
                    "status": "unreachable",
                    "last_error": str(e)[:200],
                    "last_attempt": now_iso(),
                }

    out = {
        "generated_at": now_iso(),
        "tier": 1,
        "description": "Ledger-verified real-time transaction throughput from open, keyless chain APIs.",
        "feeds": feeds,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {OUT} — {ok}/{len(FEEDS)} feeds ok")
    # Non-fatal even if some feeds fail; only fail hard if ALL fail and no prior data.
    return 0 if (ok > 0 or prev) else 1


if __name__ == "__main__":
    sys.exit(main())

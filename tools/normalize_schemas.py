#!/usr/bin/env python3
"""Universe of Finance — Schema Normalizer (Run 3)

Reads all 24 category data.json files and normalizes them to the target schema.
"""

import json
import os
from pathlib import Path

ANALYSIS_ROOT = Path("/home/quackstra/universe-of-finance/analysis")

# Map: (sector_dir, slug) -> sector display name
SECTOR_MAP = {
    "payments": "Payments",
    "traditional-finance": "Traditional Finance",
    "digital-assets": "Digital Assets",
    "banking": "Banking",
    "gaming": "Gaming",
    "government": "Government",
    "emerging": "Emerging",
}

# Overlap rules
OVERLAP_RULES: dict[str, dict] = {
    "consumer-cards": {"overlaps_with": ["digital-wallets"], "overlap_type": "partial", "overlap_note": "Card-rail transactions processed via digital wallets (Apple Pay, Google Pay)"},
    "digital-wallets": {"overlaps_with": ["consumer-cards", "bank-transfers"], "overlap_type": "partial", "overlap_note": "Card-rail overlay (~40B txns via Apple Pay etc.) + UPI counted in bank-transfers"},
    "bank-transfers": {"overlaps_with": ["digital-wallets"], "overlap_type": "partial", "overlap_note": "UPI (172B txns) also counted under digital wallets"},
    "ecommerce": {"overlaps_with": ["consumer-cards", "digital-wallets", "bank-transfers"], "overlap_type": "partial", "overlap_note": "~95% of e-commerce transactions settle on card, wallet, or bank transfer rails"},
    "p2p-transfers": {"overlaps_with": ["digital-wallets"], "overlap_type": "partial", "overlap_note": "Minor overlap — some P2P flows through digital wallet platforms"},
    "remittances": {"overlaps_with": ["bank-transfers", "p2p-transfers"], "overlap_type": "partial", "overlap_note": "Minor overlap — some remittances flow through bank transfer and P2P rails"},
    "defi": {"overlaps_with": ["blockchain-l1-l2"], "overlap_type": "full_subset", "overlap_note": "All DeFi transactions are on-chain L1/L2 transactions"},
    "stablecoins": {"overlaps_with": ["blockchain-l1-l2"], "overlap_type": "full_subset", "overlap_note": "All stablecoin transfers are on-chain L1/L2 transactions"},
    "gaming-microtx": {"overlaps_with": ["consumer-cards"], "overlap_type": "partial", "overlap_note": "65-75% of microtransactions settle on card rails"},
    "gaming-sales": {"overlaps_with": ["consumer-cards"], "overlap_type": "partial", "overlap_note": "70-80% of digital game sales settle on card rails"},
    "government-payments": {"overlaps_with": ["bank-transfers"], "overlap_type": "partial", "overlap_note": "~60% of government payments flow via ACH/bank transfer rails"},
    "iot-m2m": {"overlaps_with": ["consumer-cards", "bank-transfers"], "overlap_type": "partial", "overlap_note": "~75% of IoT payments settle on existing card or bank transfer rails"},
    "rwa-tokenisation": {"overlaps_with": ["blockchain-l1-l2"], "overlap_type": "full_subset", "overlap_note": "All RWA token transactions are on-chain L1/L2 transactions"},
    "ai-agents": {"overlaps_with": ["blockchain-l1-l2"], "overlap_type": "full_subset", "overlap_note": "AI agent payments (x402, AP2) settle on-chain"},
}

# Reference values for fallback
REF = {
    "consumer-cards": {"avg_tps": 24501, "peak_tps": 61250, "annual_vol": 772730000000, "annual_val": 51920000000000},
    "digital-wallets": {"avg_tps": 19660, "peak_tps": 45000, "annual_vol": 620000000000, "annual_val": 15600000000000},
    "bank-transfers": {"avg_tps": 15338, "peak_tps": 27500, "annual_vol": 484000000000},
    "etd": {"avg_tps": 9500, "peak_tps": 57000, "annual_vol": 205340000000},
    "equity-markets": {"avg_tps": 3500, "peak_tps": 80000, "annual_vol": 61500000000, "annual_val": 106500000000000},
    "cex": {"avg_tps": 3100, "peak_tps": 15000, "annual_val": 77300000000000},
    "ecommerce": {"avg_tps": 1800, "annual_vol": 57500000000, "annual_val": 6330000000000},
    "blockchain-l1-l2": {"avg_tps": 900, "peak_tps": 5000, "annual_vol": 27000000000},
    "government-payments": {"avg_tps": 793, "peak_tps": 7500, "annual_vol": 25000000000},
    "iot-m2m": {"avg_tps": 634, "peak_tps": 2500, "annual_vol": 20000000000},
    "stablecoins": {"avg_tps": 520, "peak_tps": 2000, "annual_val": 27600000000000},
    "gaming-microtx": {"avg_tps": 389, "peak_tps": 778, "annual_vol": 12280000000, "annual_val": 114000000000},
    "commodities": {"avg_tps": 330, "annual_vol": 10400000000},
    "p2p-transfers": {"avg_tps": 270, "peak_tps": 600, "annual_vol": 8500000000, "annual_val": 2800000000000},
    "gaming-sales": {"avg_tps": 92, "peak_tps": 275, "annual_vol": 2890000000, "annual_val": 60200000000},
    "remittances": {"avg_tps": 57, "peak_tps": 100, "annual_vol": 1800000000, "annual_val": 905000000000},
    "securities-settlement": {"avg_tps": 45, "annual_vol": 1400000000, "annual_val": 3700000000000000000},
    "forex": {"avg_tps": 35, "annual_vol": 750000000, "annual_val": 2500000000000000},
    "interbank-rtgs": {"avg_tps": 13.4, "peak_tps": 35, "annual_vol": 423000000, "annual_val": 2150000000000000},
    "fixed-income": {"avg_tps": 7, "annual_vol": 220000000, "annual_val": 145000000000000},
    "rwa-tokenisation": {"avg_tps": 2.4, "peak_tps": 15, "annual_vol": 75000000, "annual_val": 24000000000},
    "otc-derivatives": {"avg_tps": 0.6, "annual_vol": 15000000, "annual_val": 665000000000000},
    "ai-agents": {"avg_tps": 0.66, "peak_tps": 8.5, "annual_val": 600000000},
    "defi": {"annual_val": 4160000000000},
}


CONFIDENCE_MAP = {"green": "high", "yellow": "medium", "red": "low"}

def normalize_confidence(c: str) -> str:
    return CONFIDENCE_MAP.get(c, c) if isinstance(c, str) else "medium"

def make_metric(value, source="", url="", confidence="medium", note=None) -> dict:
    m = {"value": value, "source": source, "url": url, "confidence": normalize_confidence(confidence)}
    if note:
        m["note"] = note
    return m


def extract_current(data: dict, slug: str) -> dict:
    """Extract current metrics from various schema formats into normalized form."""
    ref = REF.get(slug, {})
    current = {}

    # Try to find values from the existing data
    fields = ["avg_tps", "peak_tps", "daily_volume", "annual_volume", "annual_value_usd"]

    # Already normalized format (consumer-cards, digital-wallets, p2p, remittances, stablecoins, etc.)
    if "current" in data and isinstance(data["current"], dict):
        src = data["current"]
        for f in fields:
            # Prefer adjusted_avg_tps over raw avg_tps (e.g. CEX wash-trade adjusted)
            if f == "avg_tps" and "adjusted_avg_tps" in src and isinstance(src["adjusted_avg_tps"], dict):
                # CEX: use wash-trade adjusted TPS
                adj = src["adjusted_avg_tps"]
                current[f] = make_metric(
                    adj.get("value"),
                    adj.get("source", ""),
                    adj.get("url", ""),
                    adj.get("confidence", "low"),
                    note=adj.get("note"),
                )
            elif f in src and isinstance(src[f], dict):
                current[f] = src[f]

    # bank-transfers capsule format
    if "capsules" in data:
        caps = data["capsules"]
        if "current_tps" in caps:
            ct = caps["current_tps"]
            if "average_tps" in ct and "avg_tps" not in current:
                current["avg_tps"] = make_metric(
                    ct["average_tps"],
                    ct.get("notes", ""),
                    ct.get("sources", [""])[0] if ct.get("sources") else "",
                    ct.get("confidence", "medium"),
                )
            if "peak_tps_estimate" in ct and "peak_tps" not in current:
                current["peak_tps"] = make_metric(
                    ct["peak_tps_estimate"],
                    ct.get("notes", ""),
                    "",
                    ct.get("confidence", "low"),
                )
        if "annual_volume" in caps:
            av = caps["annual_volume"]
            if isinstance(av, dict):
                vol_key = None
                for k in ["total_transactions_millions", "total_transactions_billions"]:
                    if k in av:
                        vol_key = k
                        break
                if vol_key and "annual_volume" not in current:
                    raw = av[vol_key]
                    multiplier = 1_000_000 if "millions" in vol_key else 1_000_000_000
                    current["annual_volume"] = make_metric(
                        int(raw * multiplier),
                        av.get("notes", ""),
                        av.get("sources", [""])[0] if av.get("sources") else "",
                        av.get("confidence", "medium"),
                    )
        if "annual_value" in caps:
            val = caps["annual_value"]
            if isinstance(val, dict):
                for k in ["total_usd_trillions", "total_usd_quadrillions"]:
                    if k in val and "annual_value_usd" not in current:
                        raw = val[k]
                        mult = 1_000_000_000_000 if "trillions" in k else 1_000_000_000_000_000
                        current["annual_value_usd"] = make_metric(
                            int(raw * mult),
                            val.get("notes", ""),
                            val.get("sources", [""])[0] if val.get("sources") else "",
                            val.get("confidence", "medium"),
                        )

    # Flat format (ecommerce, equity-markets, etd, forex, fixed-income, commodities, otc-derivatives)
    if "current_tps" in data and isinstance(data["current_tps"], dict):
        ct = data["current_tps"]
        if "average_tps" in ct and "avg_tps" not in current:
            current["avg_tps"] = make_metric(
                ct["average_tps"],
                ct.get("source", ct.get("methodology", "")),
                ct.get("source_url", ""),
                ct.get("confidence", "medium"),
            )
        if "peak_tps" in ct and "peak_tps" not in current:
            current["peak_tps"] = make_metric(
                ct["peak_tps"],
                ct.get("source", ""),
                ct.get("source_url", ""),
                ct.get("confidence", "low"),
            )

    if "tps" in data and isinstance(data["tps"], dict):
        t = data["tps"]
        for key_src, key_dst in [
            ("average_tps_2024", "avg_tps"),
            ("average_tps_2024_est", "avg_tps"),
            ("average_tps_cash_bonds_2024", "avg_tps"),
            ("average_tps_incl_fx_derivs", "avg_tps"),
            ("average_tps_incl_repo_2024", "avg_tps"),
            ("peak_tps_estimate_2024", "peak_tps"),
            ("peak_tps_estimate", "peak_tps"),
        ]:
            if key_src in t and key_dst not in current:
                current[key_dst] = make_metric(
                    t[key_src],
                    t.get("methodology", ""),
                    "",
                    t.get(f"confidence_{'average' if 'avg' in key_dst else 'peak'}", "medium"),
                )

    # annual_volume from flat formats
    if "annual_volume" in data and isinstance(data["annual_volume"], dict) and "annual_volume" not in current:
        av = data["annual_volume"]
        for vol_key in ["transactions_billions", "total_2024_est"]:
            if vol_key in av:
                current["annual_volume"] = make_metric(
                    int(av[vol_key] * 1_000_000_000),
                    av.get("source", av.get("source_primary", "")),
                    av.get("source_url", ""),
                    av.get("confidence", "medium"),
                )
                break
        # FX: estimated trades in millions
        if "annual_volume" not in current and "timeseries_daily_turnover_usd_trillions" in av:
            pass  # handle via tps block

    if "annual_volume_2024" in data and isinstance(data["annual_volume_2024"], dict) and "annual_volume" not in current:
        av = data["annual_volume_2024"]
        if "total_trades_billions" in av:
            current["annual_volume"] = make_metric(
                int(av["total_trades_billions"] * 1_000_000_000),
                av.get("derivation", ""),
                av.get("sources", [""])[0] if av.get("sources") else "",
                av.get("confidence", "medium"),
            )

    # annual_value from flat formats
    if "annual_value" in data and isinstance(data["annual_value"], dict) and "annual_value_usd" not in current:
        val = data["annual_value"]
        for vk in ["total_usd_trillions", "gmv_trillions_usd", "value_2024_est"]:
            if vk in val:
                current["annual_value_usd"] = make_metric(
                    int(val[vk] * 1_000_000_000_000),
                    val.get("source", ""),
                    val.get("source_url", val.get("source", "")),
                    val.get("confidence", "medium"),
                )
                break

    if "annual_value_2024" in data and isinstance(data["annual_value_2024"], dict) and "annual_value_usd" not in current:
        val = data["annual_value_2024"]
        if "total_usd_trillions" in val:
            current["annual_value_usd"] = make_metric(
                int(val["total_usd_trillions"] * 1_000_000_000_000),
                val.get("notes", ""),
                val.get("source", ""),
                val.get("confidence", "medium"),
            )

    # ETD annual volume
    if slug == "etd" and "annual_volume" in data and "timeseries" in data["annual_volume"]:
        ts = data["annual_volume"]["timeseries"]
        if "2024" in ts:
            current["annual_volume"] = make_metric(
                int(ts["2024"]["total"] * 1_000_000_000),
                data["annual_volume"].get("source_primary", "FIA"),
                ts["2024"].get("source", ""),
                "high",
            )

    # FX: derive annual volume from tps block
    if slug == "forex" and "tps" in data:
        t = data["tps"]
        if "annual_trade_count_est" in t:
            current.setdefault("annual_volume", make_metric(
                t["annual_trade_count_est"],
                t.get("methodology", ""),
                "",
                t.get("confidence_average", "low"),
            ))

    # OTC derivatives: trade count
    if slug == "otc-derivatives" and "annual_trade_count" in data:
        tc = data["annual_trade_count"]
        val = tc.get("global_total_excl_fx_derivs_2024") or tc.get("global_total_incl_fx_derivs_2024")
        if val and "annual_volume" not in current:
            current["annual_volume"] = make_metric(
                int(val * 1_000_000),
                tc.get("note", ""),
                tc.get("source", ""),
                tc.get("confidence", "low"),
            )

    # OTC derivatives: annual value from notional
    if slug == "otc-derivatives" and "annual_value_usd" not in current:
        if "annual_notional_value" in data:
            anv = data["annual_notional_value"]
            if "annual_estimate_usd_trillions" in anv:
                current["annual_value_usd"] = make_metric(
                    int(anv["annual_estimate_usd_trillions"] * 1_000_000_000_000),
                    anv.get("annual_estimate_note", ""),
                    anv.get("source", ""),
                    anv.get("confidence", "medium"),
                    note="Notional turnover (interest rate + FX only)",
                )

    # Fixed income: derive annual value from daily ADV
    if slug == "fixed-income" and "annual_value_usd" not in current:
        val_data = data.get("annual_value", {})
        if "global_outstanding_2024_usd_trillions" in val_data:
            current["annual_value_usd"] = make_metric(
                int(val_data["global_outstanding_2024_usd_trillions"] * 1_000_000_000_000),
                "Global bond market outstanding value",
                val_data.get("sources", [""])[0] if val_data.get("sources") else "",
                val_data.get("confidence", "medium"),
                note="Outstanding value, not annual turnover",
            )

    # Fixed income: annual volume from global estimates
    if slug == "fixed-income" and "annual_volume" not in current:
        av = data.get("annual_volume", {})
        cash = av.get("global_cash_bond_estimate_2024", {}).get("annual_trades_millions", 0)
        repo = av.get("global_repo_estimate_2024", {}).get("annual_trades_millions", 0)
        if cash or repo:
            total = int((cash + repo) * 1_000_000)
            current["annual_volume"] = make_metric(total, "Estimated cash bonds + repo trades", "", "low")

    # Commodities annual volume: 10.4B contracts (from tps methodology)
    if slug == "commodities" and "annual_volume" not in current:
        av = data.get("annual_volume", {})
        if "total_2024_est" in av:
            current["annual_volume"] = make_metric(
                int(av["total_2024_est"] * 1_000_000_000),
                av.get("source_primary", ""),
                "",
                av.get("confidence", "medium"),
            )

    # DeFi: use combined DEX volume as annual_value_usd
    if slug == "defi" and "annual_value_usd" not in current:
        src = data.get("current", {})
        if "combined_dex_volume_usd" in src:
            v = src["combined_dex_volume_usd"]
            current["annual_value_usd"] = make_metric(
                v["value"], v.get("source", ""), v.get("url", ""), v.get("confidence", "medium"),
            )

    # CEX: annual combined volume as annual_value_usd
    if slug == "cex" and "annual_value_usd" not in current:
        src = data.get("current", {})
        if "annual_combined_volume_usd" in src:
            v = src["annual_combined_volume_usd"]
            current["annual_value_usd"] = make_metric(
                v["value"], v.get("source", ""), v.get("url", ""), v.get("confidence", "medium"),
            )
        if "est_annual_trade_count" in src and "annual_volume" not in current:
            v = src["est_annual_trade_count"]
            current["annual_volume"] = make_metric(
                v["value"], v.get("source", ""), v.get("url", ""), v.get("confidence", "low"),
            )

    # Ecommerce annual volume
    if slug == "ecommerce" and "annual_volume" not in current:
        av = data.get("annual_volume", {})
        if "transactions_billions" in av:
            current["annual_volume"] = make_metric(
                int(av["transactions_billions"] * 1_000_000_000),
                av.get("source", ""),
                "",
                av.get("confidence", "medium"),
            )

    # Ecommerce annual value
    if slug == "ecommerce" and "annual_value_usd" not in current:
        av = data.get("annual_value", {})
        if "gmv_trillions_usd" in av:
            current["annual_value_usd"] = make_metric(
                int(av["gmv_trillions_usd"] * 1_000_000_000_000),
                av.get("source", ""),
                av.get("source_url", ""),
                av.get("confidence", "medium"),
            )

    # Ecommerce avg_tps / peak_tps from current_tps
    if slug == "ecommerce" and "current_tps" in data:
        ct = data["current_tps"]
        if "average_tps" in ct and "avg_tps" not in current:
            current["avg_tps"] = make_metric(
                ct["average_tps"], ct.get("methodology", ""), ct.get("source_url", ""), ct.get("confidence", "medium"),
            )
        if "peak_tps" in ct and "peak_tps" not in current:
            current["peak_tps"] = make_metric(
                ct["peak_tps"], ct.get("peak_event", ""), "", ct.get("confidence", "low"),
            )

    # Blockchain L1/L2 daily_volume
    if slug == "blockchain-l1-l2" and "current" in data:
        src = data["current"]
        if "daily_volume" in src and isinstance(src["daily_volume"], dict) and "daily_volume" not in current:
            current["daily_volume"] = src["daily_volume"]

    # Fill from reference values where missing
    metric_to_ref = {
        "avg_tps": "avg_tps",
        "peak_tps": "peak_tps",
        "annual_volume": "annual_vol",
        "annual_value_usd": "annual_val",
    }
    for metric, ref_key in metric_to_ref.items():
        if metric not in current and ref_key in ref:
            current[metric] = make_metric(ref[ref_key], "Reference value", "", "medium")

    # Derive daily_volume if missing
    if "daily_volume" not in current and "annual_volume" in current:
        av = current["annual_volume"]["value"]
        if av is not None:
            current["daily_volume"] = make_metric(
                int(av / 365),
                "Derived: annual_volume / 365",
                "",
                current["annual_volume"]["confidence"],
            )

    # Ensure all 5 fields exist and normalize confidence values
    for f in fields:
        if f not in current:
            current[f] = make_metric(None, "", "", "low")
        elif isinstance(current[f], dict) and "confidence" in current[f]:
            current[f]["confidence"] = normalize_confidence(current[f]["confidence"])

    return current


def extract_historic(data: dict, slug: str) -> list:
    """Extract historic data into normalized array format."""
    result = []

    # Already an array
    if "historic" in data and isinstance(data["historic"], list):
        for entry in data["historic"]:
            row = {"year": entry.get("year")}
            row["annual_volume"] = entry.get("annual_volume", entry.get("est_annual_txns"))
            row["avg_tps"] = entry.get("avg_tps", entry.get("est_avg_tps"))
            row["source"] = entry.get("source", "")
            row["confidence"] = entry.get("confidence", "medium")
            result.append(row)
        return result

    # Capsule format with timeseries dicts
    if "capsules" in data and "historic_timeseries" in data["capsules"]:
        ts = data["capsules"]["historic_timeseries"]
        # Interbank-rtgs: merge fedwire + t2 + chaps
        if slug == "interbank-rtgs":
            years = set()
            for series in [ts.get("fedwire_volume_millions", {}), ts.get("t2_target2_volume_millions", {}), ts.get("chaps_volume_millions", {})]:
                years.update(series.keys())
            for y in sorted(years):
                total = 0
                for series in [ts.get("fedwire_volume_millions", {}), ts.get("t2_target2_volume_millions", {}), ts.get("chaps_volume_millions", {})]:
                    if y in series:
                        total += series[y]
                result.append({
                    "year": int(y),
                    "annual_volume": int(total * 1_000_000),
                    "avg_tps": round(total * 1_000_000 / 31_536_000, 1),
                    "source": "Fedwire + T2 + CHAPS",
                    "confidence": "medium",
                })
            return result

        # Securities-settlement
        if slug == "securities-settlement":
            ts_euroclear = ts.get("euroclear_transactions_millions", {})
            for y, val in sorted(ts_euroclear.items()):
                result.append({
                    "year": int(y),
                    "annual_volume": int(val * 1_000_000),
                    "avg_tps": round(val * 1_000_000 / 31_536_000, 1),
                    "source": "Euroclear",
                    "confidence": "medium",
                })
            return result

    # Bank-transfers capsule format
    if "capsules" in data and "historic_timeseries" in data.get("capsules", {}):
        ts = data["capsules"]["historic_timeseries"]
        if slug == "bank-transfers":
            rtp = ts.get("global_rtp_volume_billions", {})
            for y, val in sorted(rtp.items()):
                result.append({
                    "year": int(y),
                    "annual_volume": int(val * 1_000_000_000),
                    "avg_tps": round(val * 1_000_000_000 / 31_536_000),
                    "source": "ACI Worldwide Global RTP",
                    "confidence": "medium",
                })
            return result

    # Flat historic_timeseries (ecommerce, equity-markets, etc.)
    if "historic_timeseries" in data and isinstance(data["historic_timeseries"], dict):
        ht = data["historic_timeseries"]
        if "data" in ht and isinstance(ht["data"], list):
            for entry in ht["data"]:
                result.append({
                    "year": entry.get("year"),
                    "annual_volume": entry.get("est_transactions_billions", entry.get("est_trades_billions")),
                    "avg_tps": entry.get("est_avg_tps"),
                    "source": ht.get("source", ""),
                    "confidence": ht.get("confidence", "medium"),
                })
                # Convert billions to raw count
                if result[-1]["annual_volume"] is not None:
                    result[-1]["annual_volume"] = int(result[-1]["annual_volume"] * 1_000_000_000)
            return result
        # Dict-based timeseries (equity value)
        if "metric" in ht and ht["metric"] == "total_value_traded_usd_trillions":
            for entry in ht.get("data", []):
                result.append({
                    "year": entry.get("year"),
                    "annual_volume": int(entry.get("est_trades_billions", 0) * 1_000_000_000) if entry.get("est_trades_billions") else None,
                    "avg_tps": None,
                    "source": ht.get("source", ""),
                    "confidence": ht.get("confidence", "medium"),
                })
            return result

    # ETD timeseries
    if slug == "etd" and "annual_volume" in data and "timeseries" in data["annual_volume"]:
        ts = data["annual_volume"]["timeseries"]
        for y, entry in sorted(ts.items()):
            result.append({
                "year": int(y),
                "annual_volume": int(entry["total"] * 1_000_000_000),
                "avg_tps": round(entry["total"] * 1_000_000_000 / 31_536_000),
                "source": entry.get("source", "FIA"),
                "confidence": entry.get("confidence", "medium").replace("green", "high").replace("yellow", "medium").replace("red", "low"),
            })
        return result

    # FX timeseries (daily turnover, not trade count)
    if slug == "forex":
        ts = data.get("annual_volume", {}).get("timeseries_daily_turnover_usd_trillions", {})
        for y, entry in sorted(ts.items()):
            result.append({
                "year": int(y),
                "annual_volume": None,
                "avg_tps": None,
                "source": entry.get("source", "BIS"),
                "confidence": entry.get("confidence", "medium").replace("green", "high"),
            })
        return result

    # Fixed income
    if slug == "fixed-income" and "historic" in data and isinstance(data["historic"], dict):
        h = data["historic"]
        outstanding = h.get("global_outstanding_trillions", {})
        for y, val in sorted(outstanding.items()):
            result.append({
                "year": int(y),
                "annual_volume": None,
                "avg_tps": None,
                "source": h.get("source", "SIFMA"),
                "confidence": "medium",
            })
        return result

    # Commodities
    if slug == "commodities" and "historic" in data and isinstance(data["historic"], dict):
        h = data["historic"]
        etd = h.get("global_commodity_etd_est_billions", {})
        for y, val in sorted(etd.items()):
            result.append({
                "year": int(y),
                "annual_volume": int(val * 1_000_000_000),
                "avg_tps": round(val * 1_000_000_000 / 31_536_000),
                "source": "FIA estimate",
                "confidence": "medium",
            })
        return result

    # OTC derivatives
    if slug == "otc-derivatives":
        ts = data.get("notional_outstanding", {}).get("timeseries_year_end", {})
        for y, entry in sorted(ts.items()):
            result.append({
                "year": int(y),
                "annual_volume": None,
                "avg_tps": None,
                "source": "BIS",
                "confidence": entry.get("confidence", "medium").replace("green", "high"),
            })
        return result

    # IoT: device counts as historic proxy
    if slug == "iot-m2m" and "historic" in data and isinstance(data["historic"], list):
        for entry in data["historic"]:
            result.append({
                "year": entry.get("year"),
                "annual_volume": None,
                "avg_tps": None,
                "source": entry.get("source", ""),
                "confidence": entry.get("confidence", "medium"),
            })
        return result

    return result


def extract_projections(data: dict, slug: str) -> dict:
    """Extract projections into normalized format."""
    result = {"baseline": [], "high_growth": [], "conservative": []}
    proj = data.get("projections", {})
    if not proj:
        if "capsules" in data and "projections" in data["capsules"]:
            proj = data["capsules"]["projections"]

    for scenario in ["baseline", "high_growth", "conservative"]:
        sc_data = proj.get(scenario, {})

        # Already a list of dicts with year/tps/annual_volume
        if isinstance(sc_data, list):
            for entry in sc_data:
                row = {
                    "year": entry.get("year"),
                    "tps": entry.get("tps", entry.get("avg_tps", entry.get("est_avg_tps"))),
                    "annual_volume": entry.get("annual_volume", entry.get("est_annual_txns")),
                }
                result[scenario].append(row)
            continue

        # Dict with year keys (bank-transfers, interbank-rtgs, securities-settlement format)
        if isinstance(sc_data, dict):
            # Has milestones array (equity-markets)
            if "milestones" in sc_data:
                for entry in sc_data["milestones"]:
                    result[scenario].append({
                        "year": entry.get("year"),
                        "tps": round(entry.get("trades_billions", 0) * 1_000_000_000 / 31_536_000) if entry.get("trades_billions") else None,
                        "annual_volume": int(entry.get("trades_billions", 0) * 1_000_000_000) if entry.get("trades_billions") else None,
                    })
                continue

            # Has data array (ecommerce)
            if "data" in sc_data and isinstance(sc_data["data"], list):
                for entry in sc_data["data"]:
                    result[scenario].append({
                        "year": entry.get("year"),
                        "tps": entry.get("est_avg_tps"),
                        "annual_volume": int(entry.get("gmv_trillions", 0) / 0.00011) if entry.get("gmv_trillions") else None,
                    })
                continue

            # Has volume milestones (ETD)
            if "volume_2030_bn" in sc_data or "volume_2035_bn" in sc_data:
                for yr_key, tps_key in [("volume_2030_bn", "tps_2030"), ("volume_2035_bn", "tps_2035")]:
                    if yr_key in sc_data:
                        year = int(yr_key.split("_")[1])
                        result[scenario].append({
                            "year": year,
                            "tps": sc_data.get(tps_key, round(sc_data[yr_key] * 1_000_000_000 / 31_536_000)),
                            "annual_volume": int(sc_data[yr_key] * 1_000_000_000),
                        })
                continue

            # FX projection format
            if "daily_turnover_2030_usd_trillions" in sc_data:
                for yr in [2030, 2035]:
                    key = f"daily_turnover_{yr}_usd_trillions"
                    tps_key = f"tps_{yr}"
                    if key in sc_data:
                        result[scenario].append({
                            "year": yr,
                            "tps": sc_data.get(tps_key),
                            "annual_volume": None,
                        })
                continue

            # Fixed income
            if "daily_trades_2030" in sc_data or "daily_trades_2035" in sc_data:
                for yr in [2030, 2035]:
                    key = f"daily_trades_{yr}"
                    tps_key = f"tps_cash_{yr}"
                    if key in sc_data:
                        result[scenario].append({
                            "year": yr,
                            "tps": sc_data.get(tps_key, round(sc_data[key] / 86400, 1)),
                            "annual_volume": int(sc_data[key] * 252),
                        })
                continue

            # OTC derivatives
            if "annual_trades_2030_m" in sc_data:
                for yr in [2030, 2035]:
                    key = f"annual_trades_{yr}_m"
                    tps_key = f"tps_{yr}"
                    if key in sc_data:
                        result[scenario].append({
                            "year": yr,
                            "tps": sc_data.get(tps_key, round(sc_data[key] * 1_000_000 / 31_536_000, 2)),
                            "annual_volume": int(sc_data[key] * 1_000_000),
                        })
                continue

            # Year-keyed dict (bank-transfers, interbank-rtgs, securities-settlement)
            for k, v in sorted(sc_data.items()):
                if k.isdigit() and isinstance(v, dict):
                    yr = int(k)
                    tps_val = v.get("avg_tps", v.get("avg_tps_calendar"))
                    vol_key = None
                    for vk in ["total_billions", "total_millions"]:
                        if vk in v:
                            vol_key = vk
                            break
                    vol = None
                    if vol_key:
                        mult = 1_000_000_000 if "billions" in vol_key else 1_000_000
                        vol = int(v[vol_key] * mult)
                    result[scenario].append({"year": yr, "tps": tps_val, "annual_volume": vol})

    return result


def extract_sources(data: dict) -> list:
    """Extract sources into normalized format."""
    sources = data.get("sources", [])

    # Capsule format: sources may be nested inside capsules sub-dicts
    if not sources:
        seen_urls = set()
        all_sources = []
        # Collect from all sub-dicts that have 'sources' arrays
        def _collect(obj):
            if isinstance(obj, dict):
                if "sources" in obj and isinstance(obj["sources"], list):
                    for s in obj["sources"]:
                        if isinstance(s, str):
                            if s not in seen_urls:
                                seen_urls.add(s)
                                all_sources.append({"url": s, "citation": s.split("/")[-1]})
                        elif isinstance(s, dict):
                            url = s.get("url", "")
                            if url not in seen_urls:
                                seen_urls.add(url)
                                all_sources.append(s)
                for src_key in ["source", "source_url"]:
                    if src_key in obj and isinstance(obj[src_key], str) and obj[src_key].startswith("http"):
                        url = obj[src_key]
                        if url not in seen_urls:
                            seen_urls.add(url)
                            citation = obj.get("source", obj.get("citation", url.split("/")[-1]))
                            if citation.startswith("http"):
                                citation = url.split("/")[-1]
                            all_sources.append({"url": url, "citation": citation})
                for v in obj.values():
                    _collect(v)
            elif isinstance(obj, list):
                for item in obj:
                    _collect(item)
        _collect(data)
        sources = all_sources

    result = []
    for i, s in enumerate(sources):
        result.append({
            "id": s.get("id", i + 1),
            "citation": s.get("citation", s.get("title", "")),
            "url": s.get("url", ""),
            "accessed": s.get("accessed", "2026-03-26"),
        })
    return result


def normalize_file(filepath: Path) -> dict:
    slug = filepath.parent.name
    sector_dir = filepath.parent.parent.name
    sector = SECTOR_MAP.get(sector_dir, sector_dir)

    with open(filepath) as f:
        data = json.load(f)

    category = data.get("category", slug.replace("-", " ").title())

    normalized = {
        "category": category,
        "slug": slug,
        "sector": sector,
        "last_updated": "2026-03-26",
        "current": extract_current(data, slug),
        "historic": extract_historic(data, slug),
        "projections": extract_projections(data, slug),
        "overlap": OVERLAP_RULES.get(slug, {"overlaps_with": [], "overlap_type": "none", "overlap_note": ""}),
        "sources": extract_sources(data),
    }

    return normalized


def main():
    categories = []
    for sector_dir in sorted(ANALYSIS_ROOT.iterdir()):
        if not sector_dir.is_dir():
            continue
        for cat_dir in sorted(sector_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            data_file = cat_dir / "data.json"
            if data_file.exists():
                categories.append(data_file)

    print(f"Found {len(categories)} data.json files")

    for filepath in categories:
        slug = filepath.parent.name
        try:
            normalized = normalize_file(filepath)
            with open(filepath, "w") as f:
                json.dump(normalized, f, indent=2)
            # Quick validation
            avg_tps = normalized["current"]["avg_tps"]["value"]
            annual_vol = normalized["current"]["annual_volume"]["value"]
            annual_val = normalized["current"]["annual_value_usd"]["value"]
            print(f"  {slug:25s}  avg_tps={str(avg_tps):>12}  annual_vol={str(annual_vol):>18}  annual_val={str(annual_val):>22}  sources={len(normalized['sources']):>2}  historic={len(normalized['historic']):>2}  overlap={normalized['overlap']['overlap_type']}")
        except Exception as e:
            print(f"  ERROR {slug}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()

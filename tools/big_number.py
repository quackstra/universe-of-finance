#!/usr/bin/env python3
"""Universe of Finance — Big Number Calculator

Reads all 24 normalized data.json files and computes de-duplicated global financial TPS.
"""

import argparse
import json
import sys
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).resolve().parent.parent / "analysis"

# Overlap deduction rules for de-duplication
# Format: slug -> (deduction_type, params)
# "exclude": entire category excluded from TPS sum
# "pct": reduce annual_volume by X%
# "flat_vol": subtract flat number from annual_volume
DEDUCTIONS = {
    "digital-wallets": {
        "type": "flat_vol",
        "deductions": [
            {"amount": 172_000_000_000, "reason": "UPI counted in bank-transfers"},
            {"amount": 40_000_000_000, "reason": "Card-rail overlay (Apple Pay etc.)"},
        ],
    },
    "ecommerce": {"type": "pct", "pct": 95, "reason": "~95% settles on card/wallet/bank rails"},
    "defi": {"type": "exclude", "reason": "Full subset of L1/L2 blockchain transactions"},
    "stablecoins": {"type": "exclude", "reason": "Full subset of L1/L2 blockchain transactions"},
    "government-payments": {"type": "pct", "pct": 60, "reason": "~60% flows via ACH/bank transfers"},
    "gaming-microtx": {"type": "exclude_tps", "reason": "Commerce layer; settles on card rails (65-75%)"},
    "gaming-sales": {"type": "exclude_tps", "reason": "Commerce layer; settles on card rails (70-80%)"},
    "iot-m2m": {"type": "pct", "pct": 75, "reason": "~75% settles on existing card/bank rails"},
    "rwa-tokenisation": {"type": "exclude", "reason": "Full subset of L1/L2 blockchain transactions"},
    "ai-agents": {"type": "exclude", "reason": "Full subset of L1/L2 blockchain transactions"},
}

SECONDS_PER_YEAR = 31_536_000


def load_all_categories() -> list[dict]:
    """Load all normalized data.json files."""
    categories = []
    for sector_dir in sorted(ANALYSIS_ROOT.iterdir()):
        if not sector_dir.is_dir():
            continue
        for cat_dir in sorted(sector_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            data_file = cat_dir / "data.json"
            if data_file.exists():
                with open(data_file) as f:
                    categories.append(json.load(f))
    return categories


def get_val(cat: dict, field: str):
    """Get a numeric value from the current metrics."""
    v = cat.get("current", {}).get(field, {}).get("value")
    return v if v is not None else 0


def compute_raw(categories: list[dict]) -> dict:
    """Compute raw sums without deduplication."""
    by_sector = {}
    total_tps = 0
    total_vol = 0
    total_val = 0

    for cat in categories:
        slug = cat["slug"]
        sector = cat["sector"]
        avg_tps = get_val(cat, "avg_tps")
        annual_vol = get_val(cat, "annual_volume")
        annual_val = get_val(cat, "annual_value_usd")

        if sector not in by_sector:
            by_sector[sector] = {"categories": [], "total_tps": 0, "total_vol": 0, "total_val": 0}

        by_sector[sector]["categories"].append({
            "slug": slug,
            "category": cat["category"],
            "avg_tps": avg_tps,
            "annual_volume": annual_vol,
            "annual_value_usd": annual_val,
        })
        by_sector[sector]["total_tps"] += avg_tps
        by_sector[sector]["total_vol"] += annual_vol
        by_sector[sector]["total_val"] += annual_val
        total_tps += avg_tps
        total_vol += annual_vol
        total_val += annual_val

    return {
        "by_sector": by_sector,
        "total_tps": total_tps,
        "total_volume": total_vol,
        "total_value_usd": total_val,
    }


def compute_deduped(categories: list[dict]) -> dict:
    """Compute de-duplicated sums with overlap deductions."""
    by_sector = {}
    total_tps = 0
    total_vol = 0
    total_val = 0
    deduction_log = []

    for cat in categories:
        slug = cat["slug"]
        sector = cat["sector"]
        avg_tps = get_val(cat, "avg_tps")
        annual_vol = get_val(cat, "annual_volume")
        annual_val = get_val(cat, "annual_value_usd")

        deduction = DEDUCTIONS.get(slug)
        effective_tps = avg_tps
        effective_vol = annual_vol
        deducted = False

        if deduction:
            dtype = deduction["type"]
            if dtype == "exclude":
                effective_tps = 0
                effective_vol = 0
                deducted = True
                deduction_log.append(f"  {slug:25s}  EXCLUDED  ({deduction['reason']})")
            elif dtype == "exclude_tps":
                effective_tps = 0
                effective_vol = 0
                deducted = True
                deduction_log.append(f"  {slug:25s}  EXCLUDED from TPS  ({deduction['reason']})")
            elif dtype == "pct":
                pct = deduction["pct"]
                removed_tps = avg_tps * pct / 100
                removed_vol = annual_vol * pct / 100
                effective_tps = avg_tps - removed_tps
                effective_vol = annual_vol - removed_vol
                deducted = True
                deduction_log.append(f"  {slug:25s}  -{pct}%  TPS: {avg_tps:>10.1f} -> {effective_tps:>10.1f}  ({deduction['reason']})")
            elif dtype == "flat_vol":
                total_removed = 0
                for d in deduction["deductions"]:
                    total_removed += d["amount"]
                effective_vol = max(0, annual_vol - total_removed)
                effective_tps = effective_vol / SECONDS_PER_YEAR if effective_vol > 0 else 0
                deducted = True
                deduction_log.append(f"  {slug:25s}  -{total_removed/1e9:.0f}B txns  TPS: {avg_tps:>10.1f} -> {effective_tps:>10.1f}")

        if sector not in by_sector:
            by_sector[sector] = {"categories": [], "total_tps": 0, "total_vol": 0, "total_val": 0}

        by_sector[sector]["categories"].append({
            "slug": slug,
            "category": cat["category"],
            "raw_tps": avg_tps,
            "effective_tps": effective_tps,
            "raw_volume": annual_vol,
            "effective_volume": effective_vol,
            "annual_value_usd": annual_val,
            "deducted": deducted,
        })
        by_sector[sector]["total_tps"] += effective_tps
        by_sector[sector]["total_vol"] += effective_vol
        by_sector[sector]["total_val"] += annual_val
        total_tps += effective_tps
        total_vol += effective_vol
        total_val += annual_val

    return {
        "by_sector": by_sector,
        "total_tps": total_tps,
        "total_volume": total_vol,
        "total_value_usd": total_val,
        "deduction_log": deduction_log,
    }


def fmt_num(n, suffix="") -> str:
    """Format large numbers with human-readable suffixes."""
    if n is None or n == 0:
        return "—"
    abs_n = abs(n)
    if abs_n >= 1e15:
        return f"${n/1e15:,.1f}Q{suffix}"
    if abs_n >= 1e12:
        return f"${n/1e12:,.1f}T{suffix}"
    if abs_n >= 1e9:
        return f"{n/1e9:,.1f}B{suffix}"
    if abs_n >= 1e6:
        return f"{n/1e6:,.1f}M{suffix}"
    return f"{n:,.0f}{suffix}"


def fmt_tps(n) -> str:
    if n is None or n == 0:
        return "—"
    if n >= 1000:
        return f"{n:,.0f}"
    return f"{n:,.1f}"


def print_table(result: dict, title: str, deduped: bool = False):
    """Print a clean sector breakdown table."""
    print(f"\n{'=' * 90}")
    print(f"  {title}")
    print(f"{'=' * 90}")

    sector_order = ["Payments", "Traditional Finance", "Digital Assets", "Banking", "Gaming", "Government", "Emerging"]

    for sector in sector_order:
        if sector not in result["by_sector"]:
            continue
        sdata = result["by_sector"][sector]
        print(f"\n  {sector}")
        print(f"  {'-' * 86}")
        print(f"  {'Category':30s} {'Avg TPS':>12s} {'Annual Txns':>16s} {'Annual Value':>18s} {'Status':>8s}")
        print(f"  {'-' * 86}")

        for c in sorted(sdata["categories"], key=lambda x: -(x.get("effective_tps", x.get("avg_tps", 0)) or 0)):
            if deduped:
                tps = c["effective_tps"]
                status = "DEDUP" if c.get("deducted") else ""
                vol = c["effective_volume"]
            else:
                tps = c["avg_tps"]
                status = ""
                vol = c["annual_volume"]
            val = c["annual_value_usd"]

            print(f"  {c['slug']:30s} {fmt_tps(tps):>12s} {fmt_num(vol):>16s} {fmt_num(val):>18s} {status:>8s}")

        print(f"  {'Sector Total':30s} {fmt_tps(sdata['total_tps']):>12s} {fmt_num(sdata['total_vol']):>16s} {fmt_num(sdata['total_val']):>18s}")

    print(f"\n  {'=' * 86}")
    print(f"  {'GLOBAL TOTAL':30s} {fmt_tps(result['total_tps']):>12s} {fmt_num(result['total_volume']):>16s} {fmt_num(result['total_value_usd']):>18s}")
    print(f"  {'=' * 86}")

    if deduped and "deduction_log" in result:
        print(f"\n  Deduction details:")
        for line in result["deduction_log"]:
            print(line)


def run_sensitivity(categories: list[dict]):
    """Show how key parameters affect the total."""
    base = compute_deduped(categories)
    base_tps = base["total_tps"]

    print(f"\n{'=' * 70}")
    print(f"  Sensitivity Analysis")
    print(f"{'=' * 70}")
    print(f"\n  Baseline de-duplicated TPS: {fmt_tps(base_tps)}")
    print()

    tests = [
        ("E-commerce overlap 90% (vs 95%)", "ecommerce", {"type": "pct", "pct": 90, "reason": "test"}),
        ("E-commerce overlap 100%", "ecommerce", {"type": "exclude", "reason": "test"}),
        ("Digital wallets -100B (vs -212B)", "digital-wallets", {"type": "flat_vol", "deductions": [{"amount": 100_000_000_000, "reason": "test"}]}),
        ("Government -40% (vs -60%)", "government-payments", {"type": "pct", "pct": 40, "reason": "test"}),
        ("IoT -50% (vs -75%)", "iot-m2m", {"type": "pct", "pct": 50, "reason": "test"}),
        ("Include gaming in TPS", "gaming-microtx", None),
        ("Include DeFi (not subset)", "defi", None),
    ]

    print(f"  {'Scenario':45s} {'TPS':>12s} {'Delta':>12s} {'% Change':>10s}")
    print(f"  {'-' * 79}")

    for label, slug, override in tests:
        saved = DEDUCTIONS.get(slug)
        if override is None:
            if slug in DEDUCTIONS:
                del DEDUCTIONS[slug]
        else:
            DEDUCTIONS[slug] = override

        test_result = compute_deduped(categories)
        delta = test_result["total_tps"] - base_tps
        pct = (delta / base_tps * 100) if base_tps else 0
        print(f"  {label:45s} {fmt_tps(test_result['total_tps']):>12s} {'+' if delta >= 0 else ''}{fmt_tps(delta):>11s} {pct:>+9.1f}%")

        # Restore
        if saved is not None:
            DEDUCTIONS[slug] = saved
        elif override is not None and slug not in DEDUCTIONS:
            pass  # was deleted, stays deleted — but we need to restore
        if override is None and saved is not None:
            DEDUCTIONS[slug] = saved


def main():
    parser = argparse.ArgumentParser(description="Universe of Finance — Big Number Calculator")
    parser.add_argument("--raw", action="store_true", help="Raw sum without deduplication")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--sensitivity", action="store_true", help="Sensitivity analysis")
    args = parser.parse_args()

    categories = load_all_categories()

    if not categories:
        print("ERROR: No data.json files found", file=sys.stderr)
        sys.exit(1)

    if args.json:
        raw = compute_raw(categories)
        deduped = compute_deduped(categories)
        output = {
            "raw": {
                "total_tps": raw["total_tps"],
                "total_annual_transactions": raw["total_volume"],
                "total_annual_value_usd": raw["total_value_usd"],
            },
            "deduped": {
                "total_tps": deduped["total_tps"],
                "total_annual_transactions": deduped["total_volume"],
                "total_annual_value_usd": deduped["total_value_usd"],
                "deductions_applied": len(deduped["deduction_log"]),
            },
            "categories_loaded": len(categories),
        }
        print(json.dumps(output, indent=2))
        return

    if args.raw:
        result = compute_raw(categories)
        print_table(result, "RAW TOTALS (no deduplication)")
    elif args.sensitivity:
        run_sensitivity(categories)
    else:
        result = compute_deduped(categories)
        print_table(result, "DE-DUPLICATED GLOBAL FINANCIAL TPS", deduped=True)

        # Also show raw for comparison
        raw = compute_raw(categories)
        print(f"\n  Raw total (no dedup): {fmt_tps(raw['total_tps'])} TPS")
        print(f"  Deduction impact:     {fmt_tps(raw['total_tps'] - result['total_tps'])} TPS removed ({(raw['total_tps'] - result['total_tps']) / raw['total_tps'] * 100:.1f}%)")


if __name__ == "__main__":
    main()

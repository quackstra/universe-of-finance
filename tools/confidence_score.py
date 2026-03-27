#!/usr/bin/env python3
"""
Confidence Scoring Model for Universe of Finance data.json files.

Reads all 24 data.json files, scores each on a 0-100 rubric across four
dimensions, writes scores back into each data.json, and generates
analysis/CONFIDENCE_SCORECARD.md.

Rubric:
  - Source quality   (0-30): Primary/regulatory=25-30, industry=15-24, extrapolations=5-14, pure estimates=0-4
  - Data recency     (0-20): <1yr=16-20, 1-2yr=10-15, 2-3yr=5-9, >3yr=0-4
  - Triangulation    (0-25): 3+ methods=20-25, 2 methods=10-19, 1 method=0-9
  - Coverage         (0-25): >90%=20-25, 50-90%=10-19, <50%=0-9

Usage:
    python3 tools/confidence_score.py            # run from repo root
    python3 tools/confidence_score.py --dry-run   # preview without writing
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from datetime import date

# ---------------------------------------------------------------------------
# Confidence scores per category (hand-scored based on source analysis)
# ---------------------------------------------------------------------------

SCORES: dict[str, dict] = {
    # ── Banking ──────────────────────────────────────────────────────────
    "interbank-rtgs": {
        "source_quality": 26,   # Fedwire, ECB, BoE, BoJ — primary central bank data
        "data_recency": 18,     # 2024 data available
        "triangulation": 20,    # 3+ independent RTGS systems cross-checked
        "coverage": 18,         # Major systems covered; some emerging markets missing
        "notes": "Strong primary sources from central banks. Missing some smaller RTGS systems (MEPS+, SAMOS).",
    },
    "securities-settlement": {
        "source_quality": 24,   # DTCC, Euroclear, CSD data — primary
        "data_recency": 16,     # 2024 data for major CSDs
        "triangulation": 18,    # Multiple CSDs cross-checked
        "coverage": 16,         # Major markets covered; APAC CSDs partially estimated
        "notes": "Good CSD-level data for US/EU. Asia-Pacific settlement volumes partially estimated.",
    },

    # ── Digital Assets ───────────────────────────────────────────────────
    "blockchain-l1-l2": {
        "source_quality": 22,   # On-chain data is verifiable; some L2 estimation
        "data_recency": 19,     # Real-time blockchain data
        "triangulation": 20,    # Multiple block explorers + analytics platforms
        "coverage": 15,         # Major L1s covered; long tail of L2s estimated
        "notes": "On-chain data is transparent and verifiable. L2 rollup transaction counts are harder to aggregate.",
    },
    "cex": {
        "source_quality": 12,   # Self-reported exchange data; wash trading concerns
        "data_recency": 18,     # Real-time data available
        "triangulation": 12,    # CoinGecko vs CoinMarketCap vs Kaiko, but all use exchange-reported data
        "coverage": 14,         # Top 20 exchanges covered; hundreds of smaller ones estimated
        "notes": "Wash trading inflates volumes at some exchanges. No regulatory audit of transaction counts.",
    },
    "defi": {
        "source_quality": 18,   # On-chain verifiable but complex to aggregate
        "data_recency": 19,     # Real-time blockchain data
        "triangulation": 15,    # DeFi Llama, Dune Analytics, The Block
        "coverage": 10,         # EVM chains well covered; non-EVM DeFi estimated
        "notes": "On-chain data is verifiable but DeFi 'transaction' definition varies. MEV and arbitrage inflate counts.",
    },
    "stablecoins": {
        "source_quality": 20,   # On-chain transfer data + issuer attestations
        "data_recency": 19,     # Real-time
        "triangulation": 18,    # Multiple analytics platforms + issuer reports
        "coverage": 18,         # USDT, USDC, DAI cover >90% of market
        "notes": "Good coverage of major stablecoins. Transfer count vs. meaningful payment distinction is blurry.",
    },

    # ── Emerging ─────────────────────────────────────────────────────────
    "ai-agents": {
        "source_quality": 8,    # Mostly projections and estimates; very early market
        "data_recency": 16,     # 2025 data but market barely exists
        "triangulation": 5,     # Single method — top-down estimation
        "coverage": 5,          # Market is too nascent to have meaningful coverage
        "notes": "Pre-market category. Most data is projections, not measurements. Very low base makes any estimate unreliable.",
    },
    "iot-m2m": {
        "source_quality": 16,   # Mix of primary (NPCI FASTag, IEA) and industry reports
        "data_recency": 17,     # 2024-2025 data for major segments
        "triangulation": 20,    # 6 segments triangulated independently; 3+ methods for toll/vending
        "coverage": 14,         # Toll/vending well covered; industrial IoT opaque
        "notes": "Triangulated across 6 segments. Toll collection (NPCI, E-ZPass) has hard data. Industrial IoT and connected vehicle segments are estimates.",
    },
    "rwa-tokenisation": {
        "source_quality": 14,   # On-chain data + industry reports (rwa.xyz, Boston Consulting)
        "data_recency": 18,     # Current on-chain data
        "triangulation": 12,    # rwa.xyz + Dune Analytics, but limited methods
        "coverage": 12,         # Public chain RWAs covered; private/permissioned unknown
        "notes": "Public blockchain RWA data is verifiable. Private tokenisation platforms not captured.",
    },

    # ── Gaming ───────────────────────────────────────────────────────────
    "gaming-microtx": {
        "source_quality": 10,   # Industry reports; publishers don't disclose txn counts
        "data_recency": 16,     # 2024-2025 market reports
        "triangulation": 8,     # Primarily top-down from revenue / avg spend
        "coverage": 10,         # Mobile gaming estimated; PC/console better known
        "notes": "Publishers report revenue, not transaction counts. Derived from revenue / average transaction size.",
    },
    "gaming-sales": {
        "source_quality": 14,   # Steam, Epic, console store partial disclosures
        "data_recency": 16,     # 2024 data from major platforms
        "triangulation": 12,    # Cross-check Steam vs console vs mobile store data
        "coverage": 14,         # Major platforms covered; smaller stores estimated
        "notes": "Steam Replay and platform reports give reasonable data. Indie/smaller platform sales estimated.",
    },

    # ── Government ───────────────────────────────────────────────────────
    "government-payments": {
        "source_quality": 16,   # Some government statistical agencies; mostly industry reports
        "data_recency": 14,     # Mix of 2023-2024 data
        "triangulation": 10,    # Limited methods — mostly top-down
        "coverage": 10,         # OECD countries better; developing world estimated
        "notes": "Tax payment counts are published by some revenue authorities but aggregation is difficult. Social benefit disbursements better documented.",
    },

    # ── Payments ─────────────────────────────────────────────────────────
    "bank-transfers": {
        "source_quality": 24,   # BIS CPMI statistics; national payment system data
        "data_recency": 16,     # 2023-2024 BIS data (1-2 year lag)
        "triangulation": 20,    # BIS + national central bank + payment network data
        "coverage": 18,         # CPMI reporting countries cover >80% of volume
        "notes": "BIS CPMI statistics are authoritative. Some lag in data. Non-CPMI countries estimated.",
    },
    "consumer-cards": {
        "source_quality": 28,   # Nilson Report, Visa/MC 10-K filings — primary
        "data_recency": 19,     # 2024 annual data available
        "triangulation": 22,    # Nilson + network filings + BIS + Fed Payments Study
        "coverage": 22,         # Visa/MC/UnionPay/Amex cover >95% of market
        "notes": "Best-documented payment category. Nilson Report is the gold standard. Network filings provide cross-checks.",
    },
    "digital-wallets": {
        "source_quality": 18,   # Mix of operator reports (Alipay, WeChat) and industry estimates
        "data_recency": 17,     # 2024 data for major wallets
        "triangulation": 16,    # Multiple sources but definition inconsistency
        "coverage": 16,         # Alipay/WeChat/PayPal well documented; smaller wallets estimated
        "notes": "Alipay and WeChat Pay dominate but detailed transaction counts are corporate-confidential. Good proxy data from PBOC.",
    },
    "ecommerce": {
        "source_quality": 18,   # Industry reports (eMarketer, Euromonitor) + some platform data
        "data_recency": 17,     # 2024 estimates available
        "triangulation": 16,    # Multiple research firms + platform disclosures
        "coverage": 16,         # Major markets well covered; transaction count (vs value) is the weak point
        "notes": "E-commerce GMV is well documented. Transaction count is derived from GMV / average order value, adding uncertainty.",
    },
    "p2p-transfers": {
        "source_quality": 20,   # Venmo, Zelle, UPI disclose volumes; PBOC data
        "data_recency": 17,     # 2024 data for major platforms
        "triangulation": 16,    # Platform reports + BIS data
        "coverage": 16,         # UPI, Venmo, Zelle, Pix well documented; informal P2P unknown
        "notes": "UPI (India) and Pix (Brazil) have excellent public data. US platforms (Venmo, Zelle) disclose quarterly. Informal cash P2P not captured.",
    },
    "remittances": {
        "source_quality": 20,   # World Bank Remittance Prices Worldwide; KNOMAD
        "data_recency": 14,     # World Bank data typically 1-2 year lag
        "triangulation": 12,    # World Bank + IFAD + bilateral corridor data
        "coverage": 12,         # Formal remittances tracked; informal (hawala, crypto) estimated
        "notes": "World Bank is authoritative for formal remittances. Informal channels (estimated 30-50% of total) are untracked.",
    },

    # ── Traditional Finance ──────────────────────────────────────────────
    "commodities": {
        "source_quality": 22,   # Exchange-reported data (CME, ICE, LME)
        "data_recency": 18,     # 2024 exchange annual reports
        "triangulation": 18,    # Multiple exchanges + FIA data
        "coverage": 16,         # Exchange-traded well covered; OTC physical commodities estimated
        "notes": "Exchange-traded commodity derivatives well documented via FIA. Physical commodity spot transactions are opaque.",
    },
    "equity-markets": {
        "source_quality": 26,   # Exchange-reported data; WFE statistics
        "data_recency": 18,     # 2024 data from major exchanges
        "triangulation": 22,    # WFE + individual exchange data + dark pool estimates
        "coverage": 20,         # Listed exchanges well covered; dark pools and ATS estimated
        "notes": "World Federation of Exchanges data is comprehensive for lit markets. Dark pool / ATS volume adds ~15-20% estimated.",
    },
    "etd": {
        "source_quality": 27,   # FIA annual volume survey — industry gold standard
        "data_recency": 19,     # 2024 FIA data
        "triangulation": 20,    # FIA + individual exchange reports + BIS
        "coverage": 22,         # FIA covers virtually all major exchanges
        "notes": "FIA annual survey is the most authoritative source for ETD volumes. Excellent coverage of listed derivatives.",
    },
    "fixed-income": {
        "source_quality": 18,   # SIFMA, ICMA; some exchange data
        "data_recency": 16,     # 2023-2024 data
        "triangulation": 14,    # SIFMA + BIS + TRACE (US only)
        "coverage": 12,         # US (TRACE) well covered; EU/Asia bond markets less transparent
        "notes": "Bond trading is predominantly OTC, making transaction counts difficult. US TRACE data is good; global coverage is patchy.",
    },
    "forex": {
        "source_quality": 22,   # BIS Triennial Survey — authoritative but infrequent
        "data_recency": 10,     # BIS survey every 3 years (last: April 2022, next: 2025)
        "triangulation": 12,    # BIS + CLS + platform data (limited)
        "coverage": 14,         # BIS survey covers reported dealers; retail FX and crypto FX pairs estimated
        "notes": "BIS Triennial Survey is definitive but only every 3 years. Daily value well-known; transaction count is derived and low-confidence.",
    },
    "otc-derivatives": {
        "source_quality": 22,   # BIS semiannual OTC derivatives statistics
        "data_recency": 16,     # H1 2024 BIS data
        "triangulation": 14,    # BIS + ISDA surveys + trade repository data
        "coverage": 16,         # Notional outstanding well known; transaction count very difficult
        "notes": "BIS data on notional outstanding is authoritative. Transaction count is extremely low-confidence — OTC trades are large, bespoke, and infrequent.",
    },
}


def load_all_data_json(analysis_dir: Path) -> list[tuple[Path, dict]]:
    """Walk analysis/ and return all (path, parsed-json) pairs."""
    results = []
    for root, _dirs, files in os.walk(analysis_dir):
        if "data.json" in files:
            p = Path(root) / "data.json"
            with open(p) as f:
                results.append((p, json.load(f)))
    results.sort(key=lambda x: x[0])
    return results


def compute_total(scores: dict) -> int:
    return (
        scores["source_quality"]
        + scores["data_recency"]
        + scores["triangulation"]
        + scores["coverage"]
    )


def confidence_band(score: int) -> str:
    if score >= 80:
        return "High"
    elif score >= 60:
        return "Medium-High"
    elif score >= 40:
        return "Medium"
    elif score >= 20:
        return "Low-Medium"
    else:
        return "Low"


def confidence_emoji(score: int) -> str:
    if score >= 70:
        return ":green_circle:"
    elif score >= 45:
        return ":yellow_circle:"
    else:
        return ":red_circle:"


def write_scorecard(
    analysis_dir: Path, all_data: list[tuple[Path, dict]], dry_run: bool = False
) -> str:
    """Generate the CONFIDENCE_SCORECARD.md content and optionally write it."""
    today = date.today().isoformat()

    rows: list[dict] = []
    for path, data in all_data:
        slug = data.get("slug", "unknown")
        scores = SCORES.get(slug)
        if not scores:
            continue
        total = compute_total(scores)
        rows.append(
            {
                "category": data.get("category", slug),
                "sector": data.get("sector", "?"),
                "slug": slug,
                "source_quality": scores["source_quality"],
                "data_recency": scores["data_recency"],
                "triangulation": scores["triangulation"],
                "coverage": scores["coverage"],
                "total": total,
                "band": confidence_band(total),
                "emoji": confidence_emoji(total),
                "notes": scores["notes"],
            }
        )

    rows.sort(key=lambda r: -r["total"])

    lines = [
        "# Universe of Finance — Confidence Scorecard",
        "",
        f"> Generated: {today}",
        "> Scoring rubric: Source Quality (0-30) + Data Recency (0-20) + Triangulation (0-25) + Coverage (0-25) = Total (0-100)",
        "",
        "## Summary",
        "",
        f"- **Categories scored:** {len(rows)}",
        f"- **Median score:** {sorted(r['total'] for r in rows)[len(rows)//2]}",
        f"- **Highest:** {rows[0]['category']} ({rows[0]['total']})",
        f"- **Lowest:** {rows[-1]['category']} ({rows[-1]['total']})",
        "",
        "## Scorecard",
        "",
        "| # | Category | Sector | Source (30) | Recency (20) | Triang (25) | Coverage (25) | **Total** | Band |",
        "|---|----------|--------|-------------|-------------|-------------|---------------|-----------|------|",
    ]

    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | {r['category']} | {r['sector']} "
            f"| {r['source_quality']} | {r['data_recency']} "
            f"| {r['triangulation']} | {r['coverage']} "
            f"| **{r['total']}** | {r['emoji']} {r['band']} |"
        )

    lines.extend(
        [
            "",
            "## Scoring Rubric Detail",
            "",
            "### Source Quality (0-30)",
            "| Range | Meaning |",
            "|-------|---------|",
            "| 25-30 | Primary / regulatory data (central bank reports, exchange filings, government statistics) |",
            "| 15-24 | Industry reports from credible bodies (FIA, Nilson, BIS, IEA) |",
            "| 5-14  | Extrapolations from partial data or market research firms |",
            "| 0-4   | Pure estimates with no verifiable source |",
            "",
            "### Data Recency (0-20)",
            "| Range | Meaning |",
            "|-------|---------|",
            "| 16-20 | Data from within the last 12 months |",
            "| 10-15 | Data 1-2 years old |",
            "| 5-9   | Data 2-3 years old |",
            "| 0-4   | Data older than 3 years |",
            "",
            "### Triangulation (0-25)",
            "| Range | Meaning |",
            "|-------|---------|",
            "| 20-25 | 3+ independent methods/sources agree within 20% |",
            "| 10-19 | 2 independent methods/sources |",
            "| 0-9   | Single method or source |",
            "",
            "### Coverage (0-25)",
            "| Range | Meaning |",
            "|-------|---------|",
            "| 20-25 | >90% of the known market captured |",
            "| 10-19 | 50-90% of the market captured |",
            "| 0-9   | <50% of the market captured |",
            "",
            "## Per-Category Notes",
            "",
        ]
    )

    for r in rows:
        lines.append(f"**{r['category']}** ({r['total']}, {r['band']}): {r['notes']}")
        lines.append("")

    content = "\n".join(lines)

    scorecard_path = analysis_dir / "CONFIDENCE_SCORECARD.md"
    if not dry_run:
        with open(scorecard_path, "w") as f:
            f.write(content)
        print(f"Wrote {scorecard_path}")

    return content


def update_data_json_files(
    all_data: list[tuple[Path, dict]], dry_run: bool = False
) -> int:
    """Add confidence field to each data.json. Returns count of files updated."""
    updated = 0
    for path, data in all_data:
        slug = data.get("slug", "unknown")
        scores = SCORES.get(slug)
        if not scores:
            print(f"  SKIP {slug} — no confidence scores defined")
            continue

        total = compute_total(scores)
        confidence_block = {
            "score": total,
            "source_quality": scores["source_quality"],
            "data_recency": scores["data_recency"],
            "triangulation": scores["triangulation"],
            "coverage": scores["coverage"],
            "notes": scores["notes"],
        }

        data["confidence"] = confidence_block

        if not dry_run:
            with open(path, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"  Updated {path}")
        else:
            print(f"  Would update {path} — score {total}")

        updated += 1

    return updated


def print_table(all_data: list[tuple[Path, dict]]) -> None:
    """Print a summary table to stdout."""
    rows = []
    for _path, data in all_data:
        slug = data.get("slug", "unknown")
        scores = SCORES.get(slug)
        if not scores:
            continue
        total = compute_total(scores)
        rows.append((total, data.get("category", slug), data.get("sector", "?")))

    rows.sort(key=lambda r: -r[0])

    print()
    print(f"{'Score':>5}  {'Category':<45}  {'Sector':<20}  Band")
    print(f"{'─'*5}  {'─'*45}  {'─'*20}  {'─'*15}")
    for total, cat, sector in rows:
        band = confidence_band(total)
        print(f"{total:>5}  {cat:<45}  {sector:<20}  {band}")
    print()


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    # Find the analysis directory relative to this script or CWD
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    analysis_dir = repo_root / "analysis"

    if not analysis_dir.is_dir():
        # Try CWD
        analysis_dir = Path.cwd() / "analysis"

    if not analysis_dir.is_dir():
        print(f"ERROR: Cannot find analysis/ directory (tried {analysis_dir})")
        sys.exit(1)

    print(f"Scanning {analysis_dir} for data.json files...")
    all_data = load_all_data_json(analysis_dir)
    print(f"Found {len(all_data)} data.json files.")

    if dry_run:
        print("\n--- DRY RUN (no files will be modified) ---\n")

    # Update data.json files with confidence scores
    print("\nUpdating data.json files with confidence scores...")
    count = update_data_json_files(all_data, dry_run=dry_run)
    print(f"\n{count} files {'would be ' if dry_run else ''}updated.")

    # Re-read after update (or use in-memory data for dry run)
    if not dry_run:
        all_data = load_all_data_json(analysis_dir)

    # Write scorecard
    print("\nGenerating CONFIDENCE_SCORECARD.md...")
    write_scorecard(analysis_dir, all_data, dry_run=dry_run)

    # Print summary table
    print_table(all_data)


if __name__ == "__main__":
    main()

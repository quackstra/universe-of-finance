#!/usr/bin/env python3
"""
Universe of Finance — Visualization Suite (Run 3)
Generates 4 key charts from research capsule data.
"""

import json
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = BASE_DIR / "analysis"
CHARTS_DIR = ANALYSIS_DIR / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

DPI = 150
FIGSIZE = (14, 8)

# ---------------------------------------------------------------------------
# Fallback reference data
# ---------------------------------------------------------------------------
FALLBACK_DATA = {
    "consumer-cards": {"avg_tps": 24501, "peak_tps": 61250, "annual_vol": 772730000000, "annual_val": 51920000000000, "sector": "Payments"},
    "digital-wallets": {"avg_tps": 19660, "peak_tps": 45000, "annual_vol": 620000000000, "annual_val": 15600000000000, "sector": "Payments"},
    "bank-transfers": {"avg_tps": 15338, "peak_tps": 27500, "annual_vol": 484000000000, "annual_val": 2471000000000000, "sector": "Payments"},
    "etd": {"avg_tps": 9500, "peak_tps": 57000, "annual_vol": 205340000000, "annual_val": None, "sector": "Traditional Finance"},
    "equity-markets": {"avg_tps": 3500, "peak_tps": 80000, "annual_vol": 61500000000, "annual_val": 106500000000000, "sector": "Traditional Finance"},
    "cex": {"avg_tps": 3100, "peak_tps": 15000, "annual_vol": None, "annual_val": 77300000000000, "sector": "Digital Assets"},
    "ecommerce": {"avg_tps": 1800, "peak_tps": None, "annual_vol": 57500000000, "annual_val": 6330000000000, "sector": "Payments"},
    "blockchain-l1-l2": {"avg_tps": 900, "peak_tps": 5000, "annual_vol": 27000000000, "annual_val": None, "sector": "Digital Assets"},
    "government-payments": {"avg_tps": 793, "peak_tps": 7500, "annual_vol": 25000000000, "annual_val": 27500000000000, "sector": "Government"},
    "iot-m2m": {"avg_tps": 634, "peak_tps": 2500, "annual_vol": 20000000000, "annual_val": None, "sector": "Emerging"},
    "stablecoins": {"avg_tps": 520, "peak_tps": 2000, "annual_vol": None, "annual_val": 27600000000000, "sector": "Digital Assets"},
    "gaming-microtx": {"avg_tps": 389, "peak_tps": 778, "annual_vol": 12280000000, "annual_val": 114000000000, "sector": "Gaming"},
    "commodities": {"avg_tps": 330, "peak_tps": None, "annual_vol": 10400000000, "annual_val": None, "sector": "Traditional Finance"},
    "p2p-transfers": {"avg_tps": 270, "peak_tps": 600, "annual_vol": 8500000000, "annual_val": 2800000000000, "sector": "Payments"},
    "gaming-sales": {"avg_tps": 92, "peak_tps": 275, "annual_vol": 2890000000, "annual_val": 60200000000, "sector": "Gaming"},
    "remittances": {"avg_tps": 57, "peak_tps": 100, "annual_vol": 1800000000, "annual_val": 905000000000, "sector": "Payments"},
    "securities-settlement": {"avg_tps": 45, "peak_tps": None, "annual_vol": 1400000000, "annual_val": 3700000000000000000, "sector": "Banking"},
    "forex": {"avg_tps": 35, "peak_tps": None, "annual_vol": 750000000, "annual_val": 2500000000000000, "sector": "Traditional Finance"},
    "fixed-income": {"avg_tps": 7, "peak_tps": None, "annual_vol": 220000000, "annual_val": 145000000000000, "sector": "Traditional Finance"},
    "interbank-rtgs": {"avg_tps": 13.4, "peak_tps": 35, "annual_vol": 423000000, "annual_val": 2150000000000000, "sector": "Banking"},
    "rwa-tokenisation": {"avg_tps": 2.4, "peak_tps": 15, "annual_vol": 75000000, "annual_val": 24000000000, "sector": "Emerging"},
    "otc-derivatives": {"avg_tps": 0.6, "peak_tps": None, "annual_vol": 15000000, "annual_val": 665000000000000, "sector": "Traditional Finance"},
    "ai-agents": {"avg_tps": 0.66, "peak_tps": 8.5, "annual_vol": None, "annual_val": 600000000, "sector": "Emerging"},
    "defi": {"avg_tps": None, "peak_tps": None, "annual_vol": None, "annual_val": 4160000000000, "sector": "Digital Assets"},
}

SECTOR_COLORS = {
    "Payments": "#2563eb",
    "Traditional Finance": "#7c3aed",
    "Digital Assets": "#f59e0b",
    "Banking": "#059669",
    "Government": "#dc2626",
    "Gaming": "#ec4899",
    "Emerging": "#06b6d4",
}

DISPLAY_NAMES = {
    "consumer-cards": "Consumer Cards",
    "digital-wallets": "Digital Wallets",
    "bank-transfers": "Bank Transfers",
    "etd": "Exchange-Traded Deriv.",
    "equity-markets": "Equity Markets",
    "cex": "Centralised Exchanges",
    "ecommerce": "E-Commerce",
    "blockchain-l1-l2": "Blockchain L1/L2",
    "government-payments": "Gov. Payments",
    "iot-m2m": "IoT / M2M",
    "stablecoins": "Stablecoins",
    "gaming-microtx": "Gaming Micro-TX",
    "commodities": "Commodities",
    "p2p-transfers": "P2P Transfers",
    "gaming-sales": "Gaming Sales",
    "remittances": "Remittances",
    "securities-settlement": "Securities Settl.",
    "forex": "Forex",
    "fixed-income": "Fixed Income",
    "interbank-rtgs": "Interbank RTGS",
    "rwa-tokenisation": "RWA Tokenisation",
    "otc-derivatives": "OTC Derivatives",
    "ai-agents": "AI Agents",
    "defi": "DeFi",
}

# ---------------------------------------------------------------------------
# Data extraction helpers
# ---------------------------------------------------------------------------

def _dig(obj: dict, *paths):
    """Try multiple dot-separated key paths; return first non-None hit."""
    for path in paths:
        val = obj
        try:
            for key in path.split("."):
                val = val[key]
            if val is not None:
                return val
        except (KeyError, TypeError, IndexError):
            continue
    return None


def _load_capsule(slug: str) -> dict:
    """Load data.json for a capsule, falling back to hardcoded values."""
    # Find the data.json across sector subdirectories
    for sector_dir in ANALYSIS_DIR.iterdir():
        if not sector_dir.is_dir() or sector_dir.name == "charts":
            continue
        candidate = sector_dir / slug / "data.json"
        if candidate.exists():
            try:
                raw = json.loads(candidate.read_text())
                return _extract(slug, raw)
            except (json.JSONDecodeError, Exception) as exc:
                print(f"  Warning: could not parse {candidate}: {exc}")
                break
    # Fallback
    fb = FALLBACK_DATA.get(slug, {})
    return fb.copy()


def _extract(slug: str, raw: dict) -> dict:
    """Normalise varying data.json schemas into a flat dict."""
    fb = FALLBACK_DATA.get(slug, {})
    sector = (
        raw.get("sector")
        or fb.get("sector", "Unknown")
    )

    avg_tps = _dig(
        raw,
        "current.avg_tps.value",
        "capsules.current_tps.average_tps",
    )
    peak_tps = _dig(
        raw,
        "current.peak_tps.value",
        "capsules.current_tps.peak_tps_estimate",
    )
    annual_vol = _dig(
        raw,
        "current.annual_volume.value",
        "capsules.annual_volume.total_transactions_billions",
    )
    # If the capsule stores volume in billions, convert
    if annual_vol is not None and annual_vol < 100000:
        annual_vol = annual_vol * 1_000_000_000

    annual_val = _dig(
        raw,
        "current.annual_value_usd.value",
        "capsules.annual_value.total_usd_trillions",
    )
    # If stored in trillions, convert to USD
    if annual_val is not None and annual_val < 1_000_000_000:
        annual_val = annual_val * 1_000_000_000_000

    return {
        "avg_tps": avg_tps if avg_tps is not None else fb.get("avg_tps"),
        "peak_tps": peak_tps if peak_tps is not None else fb.get("peak_tps"),
        "annual_vol": annual_vol if annual_vol is not None else fb.get("annual_vol"),
        "annual_val": annual_val if annual_val is not None else fb.get("annual_val"),
        "sector": sector,
        "_raw": raw,
    }


def load_all() -> dict[str, dict]:
    """Load all 24 categories."""
    data = {}
    for slug in FALLBACK_DATA:
        data[slug] = _load_capsule(slug)
    return data


# ---------------------------------------------------------------------------
# Chart 1: TPS by Category (log-scale bar chart)
# ---------------------------------------------------------------------------

def chart_tps_by_category(data: dict[str, dict]) -> None:
    print("  Chart 1: TPS by Category ...")
    # Filter to categories that have TPS data
    items = [(slug, d) for slug, d in data.items() if d.get("avg_tps")]
    items.sort(key=lambda x: x[1]["avg_tps"], reverse=True)

    slugs = [s for s, _ in items]
    tps_vals = [d["avg_tps"] for _, d in items]
    colors = [SECTOR_COLORS.get(d["sector"], "#888888") for _, d in items]
    labels = [DISPLAY_NAMES.get(s, s) for s in slugs]

    fig, ax = plt.subplots(figsize=(16, 8))
    bars = ax.bar(range(len(labels)), tps_vals, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_yscale("log")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=55, ha="right", fontsize=9)
    ax.set_ylabel("Average TPS (log scale)", fontsize=12)
    ax.set_title("Global Transaction Throughput by Category (2024)", fontsize=14, fontweight="bold")

    # Value labels on bars
    for bar, val in zip(bars, tps_vals):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val * 1.15,
            f"{val:,.0f}" if val >= 1 else f"{val:.2f}",
            ha="center", va="bottom", fontsize=7, rotation=0,
        )

    # Legend for sectors
    from matplotlib.patches import Patch
    legend_handles = [
        Patch(facecolor=c, label=s) for s, c in SECTOR_COLORS.items()
    ]
    ax.legend(handles=legend_handles, loc="upper right", fontsize=9, framealpha=0.9)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}" if x >= 1 else f"{x:.1f}"))
    ax.set_xlim(-0.6, len(labels) - 0.4)
    fig.tight_layout()
    out = CHARTS_DIR / "tps_by_category.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"    -> {out}")


# ---------------------------------------------------------------------------
# Chart 2: Value vs Count Scatter (log-log)
# ---------------------------------------------------------------------------

def chart_value_vs_count(data: dict[str, dict]) -> None:
    print("  Chart 2: Value vs Count Scatter ...")
    fig, ax = plt.subplots(figsize=FIGSIZE)

    for slug, d in data.items():
        vol = d.get("annual_vol")
        val = d.get("annual_val")
        if vol is None or val is None:
            continue
        color = SECTOR_COLORS.get(d["sector"], "#888888")
        ax.scatter(vol, val, s=100, color=color, edgecolors="white", linewidth=0.5, zorder=3)
        label = DISPLAY_NAMES.get(slug, slug)
        ax.annotate(
            label, (vol, val),
            textcoords="offset points", xytext=(6, 6),
            fontsize=7.5, color="#333333",
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Annual Transaction Count", fontsize=12)
    ax.set_ylabel("Annual Value (USD)", fontsize=12)
    ax.set_title("Transaction Count vs Value by Category (2024)", fontsize=14, fontweight="bold")

    # Format axes
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(
        lambda x, _: _human_number(x)
    ))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(
        lambda x, _: f"${_human_number(x)}"
    ))

    from matplotlib.patches import Patch
    legend_handles = [Patch(facecolor=c, label=s) for s, c in SECTOR_COLORS.items()]
    ax.legend(handles=legend_handles, loc="lower right", fontsize=9, framealpha=0.9)
    ax.grid(True, which="both", ls="--", alpha=0.3)

    fig.tight_layout()
    out = CHARTS_DIR / "value_vs_count.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"    -> {out}")


def _human_number(n: float) -> str:
    """Format large numbers for axis labels."""
    abs_n = abs(n)
    if abs_n >= 1e18:
        return f"{n/1e18:.0f}E"
    if abs_n >= 1e15:
        return f"{n/1e15:.0f}Q"
    if abs_n >= 1e12:
        return f"{n/1e12:.0f}T"
    if abs_n >= 1e9:
        return f"{n/1e9:.0f}B"
    if abs_n >= 1e6:
        return f"{n/1e6:.0f}M"
    if abs_n >= 1e3:
        return f"{n/1e3:.0f}K"
    return f"{n:.0f}"


# ---------------------------------------------------------------------------
# Chart 3: De-Duplication Waterfall
# ---------------------------------------------------------------------------

def chart_dedup_waterfall(data: dict[str, dict]) -> None:
    print("  Chart 3: De-Duplication Waterfall ...")

    # Waterfall steps (values from the overlap matrix analysis)
    steps = [
        ("Raw Sum\n~82K TPS", 82000, None),
        ("UPI overlap\n(cards/wallets)", None, -3500),
        ("Card-rail\nwallets", None, -2800),
        ("E-commerce\noverlay", None, -1600),
        ("DeFi/stablecoin\nsubsets", None, -400),
        ("Other\noverlaps", None, -3100),
        ("De-Duplicated\n~70.6K TPS", 70600, None),
    ]

    labels = [s[0] for s in steps]
    n = len(steps)

    # Calculate bar positions
    bottoms = []
    heights = []
    colors = []
    running = 0

    for i, (label, absolute, delta) in enumerate(steps):
        if absolute is not None and delta is None:
            # Absolute bar (first or last)
            bottoms.append(0)
            heights.append(absolute)
            colors.append("#2563eb" if i == 0 else "#059669")
            running = absolute
        else:
            # Delta bar (hangs from running total)
            new_running = running + delta
            bottoms.append(new_running)
            heights.append(abs(delta))
            colors.append("#ef4444")
            running = new_running

    fig, ax = plt.subplots(figsize=FIGSIZE)

    bars = ax.bar(range(n), heights, bottom=bottoms, color=colors,
                  edgecolor="white", linewidth=1.5, width=0.6)

    # Connector lines between bars
    for i in range(n - 1):
        top = bottoms[i] + heights[i]
        if steps[i][1] is None:  # delta bar — connect from bottom of current bar
            top = bottoms[i]
        ax.plot(
            [i + 0.3, i + 0.7], [bottoms[i] + heights[i] if steps[i][1] is not None else bottoms[i]] * 2,
            color="#999999", linewidth=1, ls="--", zorder=1,
        )

    # Value labels
    for i, bar in enumerate(bars):
        y_center = bottoms[i] + heights[i] / 2
        if steps[i][2] is not None:
            txt = f"-{abs(steps[i][2]):,}"
        else:
            txt = f"{steps[i][1]:,}"
        ax.text(
            bar.get_x() + bar.get_width() / 2, y_center,
            txt, ha="center", va="center", fontsize=10,
            fontweight="bold", color="white",
        )

    ax.set_xticks(range(n))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("TPS", fontsize=12)
    ax.set_title(
        "Global TPS: Raw Sum to De-Duplicated Total",
        fontsize=14, fontweight="bold",
    )
    ax.set_ylim(0, 90000)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1000:.0f}K"))

    fig.tight_layout()
    out = CHARTS_DIR / "dedup_waterfall.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"    -> {out}")


# ---------------------------------------------------------------------------
# Chart 4: Consumer Cards Historic Timeseries (2010-2024)
# ---------------------------------------------------------------------------

def chart_consumer_cards_history(data: dict[str, dict]) -> None:
    print("  Chart 4: Consumer Cards Historic Timeseries ...")

    # Try to read from data.json
    raw = data.get("consumer-cards", {}).get("_raw", {})
    historic = raw.get("historic", [])

    if historic:
        years = [h["year"] for h in historic]
        volumes_b = [h["annual_volume"] / 1e9 for h in historic]
        tps_vals = [h["avg_tps"] for h in historic]
    else:
        # Hardcoded fallback
        years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
        volumes_b = [227, 260, 300, 346, 398, 380, 467, 625, 687, 773]
        tps_vals = [7197, 8243, 9512, 10971, 12620, 12049, 14805, 19812, 21788, 24501]

    fig, ax1 = plt.subplots(figsize=FIGSIZE)

    # Volume bars
    bar_color = "#2563eb"
    ax1.bar(years, volumes_b, color=bar_color, alpha=0.35, width=0.7, label="Annual Volume (B txns)")
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Annual Transaction Volume (Billions)", fontsize=12, color=bar_color)
    ax1.tick_params(axis="y", labelcolor=bar_color)
    ax1.set_ylim(0, max(volumes_b) * 1.2)

    # TPS line
    ax2 = ax1.twinx()
    line_color = "#dc2626"
    ax2.plot(years, tps_vals, color=line_color, linewidth=2.5, marker="o",
             markersize=6, label="Average TPS", zorder=5)
    ax2.set_ylabel("Average TPS", fontsize=12, color=line_color)
    ax2.tick_params(axis="y", labelcolor=line_color)
    ax2.set_ylim(0, max(tps_vals) * 1.2)

    # Highlight COVID dip
    if 2020 in years:
        idx = years.index(2020)
        ax1.annotate(
            "COVID-19\ndip",
            xy=(2020, volumes_b[idx]),
            xytext=(2020.6, volumes_b[idx] + 80),
            fontsize=10, color="#666666",
            arrowprops=dict(arrowstyle="->", color="#999999", lw=1.5),
            ha="left",
        )
        # Highlight bar
        ax1.bar([2020], [volumes_b[idx]], color="#ef4444", alpha=0.5, width=0.7)

    ax1.set_title(
        "Consumer Card Payments: Volume & TPS Growth (2015-2024)",
        fontsize=14, fontweight="bold",
    )

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=10, framealpha=0.9)

    ax1.set_xticks(years)
    ax1.set_xticklabels([str(y) for y in years], rotation=45, ha="right")

    fig.tight_layout()
    out = CHARTS_DIR / "consumer_cards_history.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"    -> {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # Use a clean style
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except OSError:
        try:
            plt.style.use("seaborn-whitegrid")
        except OSError:
            plt.style.use("ggplot")

    # Global font tweaks
    plt.rcParams.update({
        "font.family": "sans-serif",
        "axes.titlesize": 14,
        "axes.labelsize": 12,
    })

    print("Universe of Finance — Chart Generator")
    print(f"Output: {CHARTS_DIR}\n")

    print("Loading capsule data ...")
    data = load_all()
    loaded = sum(1 for d in data.values() if d.get("avg_tps") is not None)
    print(f"  {loaded}/{len(data)} categories have TPS data\n")

    chart_tps_by_category(data)
    chart_value_vs_count(data)
    chart_dedup_waterfall(data)
    chart_consumer_cards_history(data)

    print("\nDone. All charts saved to:")
    for f in sorted(CHARTS_DIR.glob("*.png")):
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()

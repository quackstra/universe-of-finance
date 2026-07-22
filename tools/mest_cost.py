#!/usr/bin/env python3
"""Universe of Finance — Cost of MEST by Sector + the blockchain disruption threshold.

Two questions, one model:

  1. What does a single MEST cost, and why does a securities MEST cost ~1000x more
     than a gaming MEST? (Answer: it's the *type* of state transition — settlement
     finality, netting, custody, and regulatory reporting are expensive; an internal
     ledger write is nearly free.)

  2. How efficient must a blockchain be to disrupt the transfer/ownership machinery
     of each sector? A chain replaces an m-MEST incumbent cascade with a small
     residual of on-chain state transitions. It undercuts the incumbent when

         residual x chain_cost_per_state_transition  <  m x cost_per_MEST

     so the REQUIRED chain cost per state transition (the disruption threshold) is

         b* = (m x cost_per_MEST) / residual

     A high b* means the chain can be wildly inefficient and still win; a low b*
     means only the most efficient chains (Solana-class) can compete on cost.

Run:  python3 tools/mest_cost.py         # prints both tables + renders the chart
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
CHARTS_DIR = BASE_DIR / "analysis" / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)
DPI = 150

# ---------------------------------------------------------------------------
# (1) Cost per MEST by TYPE — the taxonomy from analysis/MEST.md.
#     Cost is what it takes to process ONE bilateral state transition of that
#     kind (build + operate + reconcile), in USD. Ranges, order-of-magnitude.
# ---------------------------------------------------------------------------
MEST_TYPE_COST = {
    # type                     (low,     high,    why it costs what it costs)
    "Ledger credit/debit": (0.0001, 0.001, "internal DB write; no external finality"),
    "Authorization": (0.001, 0.01, "a contingent hold; cheap to place, cheap to void"),
    "Fee/commission": (0.005, 0.05, "calculate + allocate + book on both sides"),
    "Revenue recognition": (0.01, 0.10, "recognition + the tax/audit counterparty"),
    "Payment leg": (0.01, 0.05, "interbank value movement across two ledgers"),
    "Clearing event": (0.02, 0.20, "match, validate, novate; CCP operations"),
    "Audit trail/recon": (0.02, 0.50, "labour-heavy reconciliation + dispute ops"),
    "Netting entry": (0.05, 0.50, "multilateral position compression; CCP/CLS"),
    "Custody movement": (0.10, 1.00, "CSD/omnibus transfer; asset-servicing overhead"),
    "Risk/margin adj.": (0.10, 2.00, "bilateral margin call + collateral movement"),
    "Settlement leg": (0.10, 2.00, "irrevocable finality (RTGS/DvP) — the expensive one"),
    "Regulatory report": (0.10, 5.00, "reportable-event capture + filing infrastructure"),
}

# ---------------------------------------------------------------------------
# (2) Cost per MEST by SECTOR + the incumbent multiplier + the DLT residual.
#     cost_mid = representative $/MEST (mid of the MEST Advantage §2.1 ranges,
#     extended). mult = incumbent MESTs/txn (MEST Advantage §3.1). residual =
#     on-chain state transitions after atomic condensation.
# ---------------------------------------------------------------------------
# moat = the NON-cost barrier (0-100): legal finality + netting benefit + liquidity
# + regulatory acceptance + network effects. High moat = un-disrupted even when cost
# headroom is huge, because the barrier isn't price. This is the §5 "why" axis.
SECTORS = [
    # name,               group,       mult, cost_mid, residual, moat, dominant MEST types
    ("Gaming microtx", "Gaming", 4, 0.002, 2, 10, "internal ledger writes"),
    ("Digital wallets", "Payments", 5, 0.005, 2, 20, "ledger + payment leg"),
    ("Bill payments", "Payments", 4, 0.008, 2, 25, "payment leg + recon"),
    ("Bank transfers", "Payments", 5, 0.025, 2, 35, "clearing + interbank settle"),
    ("Consumer cards", "Payments", 7, 0.008, 2, 45, "auth + clearing + interchange + settle"),
    ("Cross-border wire", "Payments", 7, 3.50, 2, 55, "correspondent hops + reg report"),
    ("Forex", "TradFi", 8, 2.00, 2, 70, "CLS/PvP legs + nostro recon"),
    ("Fixed income", "TradFi", 8, 2.00, 2, 72, "bilateral confirm + custody + repo"),
    ("Equity markets", "TradFi", 10, 0.15, 2, 75, "clearing + netting + custody + settle"),
    ("ETD (derivatives)", "TradFi", 10, 0.30, 3, 80, "CCP novation + margin + settle"),
    ("Securities settle", "Banking", 9, 1.00, 2, 85, "custody + DvP finality + recon"),
    ("OTC derivatives", "TradFi", 10, 5.00, 3, 88, "ISDA + bilateral margin + recon"),
]

GROUP_COLOR = {
    "Payments": "#2563eb",   # blue
    "TradFi": "#7c3aed",     # purple
    "Banking": "#0d9488",    # teal
    "Gaming": "#db2777",     # pink
}

# What real chains cost to process ONE state transition today (USD, typical).
CHAIN_REFS = [
    ("Solana-class", 0.0005, "#16a34a"),      # sub-cent, high throughput
    ("L2 rollups", 0.01, "#ca8a04"),          # Base/Arbitrum/Optimism typical
    ("Ethereum L1", 3.00, "#dc2626"),         # congested base layer
]


def threshold(mult: float, cost_mid: float, residual: int) -> float:
    """Required chain $/state-transition to undercut the incumbent (b*)."""
    return mult * cost_mid / residual


def print_tables() -> None:
    print("\n=== Cost per MEST by TYPE (why securities > gaming) ===")
    print(f"{'MEST type':22} {'$/MEST (low–high)':>20}   basis")
    for t, (lo, hi, why) in MEST_TYPE_COST.items():
        print(f"{t:22} {f'${lo:.4f}–${hi:.2f}':>20}   {why}")

    print("\n=== Disruption threshold by SECTOR ===")
    print(f"{'Sector':20} {'mult':>4} {'$/MEST':>8} {'resid':>5} {'friction/txn':>12} {'b* ($/state-tx)':>16}")
    rows = []
    for name, group, mult, cost, resid, moat, _types in SECTORS:
        friction = mult * cost
        b = threshold(mult, cost, resid)
        rows.append((name, group, mult, cost, resid, friction, b, moat))
        print(f"{name:20} {mult:>4} {cost:>8.4f} {resid:>5} {friction:>12.3f} {b:>16.4f}")
    print(
        "\nReading: a chain can cost UP TO b* per state transition and still undercut\n"
        "the incumbent. Higher b* = easier to disrupt. Compare b* to chain costs:\n"
        + "  " + " · ".join(f"{n} ~${c:g}" for n, c, _ in CHAIN_REFS)
    )
    return rows


def render_chart(rows) -> Path:
    rows = sorted(rows, key=lambda r: r[6])  # by threshold ascending
    names = [r[0] for r in rows]
    thresholds = [r[6] for r in rows]
    colors = [GROUP_COLOR[r[1]] for r in rows]
    y = range(len(names))

    fig, ax = plt.subplots(figsize=(14, 8.4))
    ax.set_xscale("log")
    floor = 1e-4
    ax.barh(
        list(y),
        thresholds,
        left=floor,
        color=colors,
        height=0.62,
        zorder=3,
    )
    for i, (name, thr) in enumerate(zip(names, thresholds)):
        ax.text(thr * 1.15, i, f"${thr:,.3f}", va="center", ha="left",
                fontsize=9, color="#334155", zorder=5)

    # Headroom above the top bar so reference-line labels sit in a clear band.
    ax.set_ylim(-0.7, len(names) - 0.5 + 1.15)

    # Reference lines: what real chains cost per state transition today.
    for label, cost, color in CHAIN_REFS:
        ax.axvline(cost, color=color, linestyle="--", linewidth=1.6, zorder=2, alpha=0.9)
        ax.text(
            cost, len(names) - 0.5 + 0.98, f"{label}\n~${cost:g}", color=color,
            fontsize=9, va="top", ha="center", zorder=6, fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.5),
        )

    ax.set_yticks(list(y))
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlim(floor, 60)
    ax.set_xlabel(
        "Required blockchain cost per state transition to undercut the incumbent  "
        "(log scale, USD) — bar end = the ceiling the chain must beat",
        fontsize=10,
    )
    ax.grid(axis="x", color="#e2e8f0", linewidth=0.8, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    fig.suptitle(
        "How efficient must a blockchain be to disrupt each sector's MEST?",
        fontsize=15, fontweight="bold", x=0.5, y=0.985,
    )
    fig.text(
        0.5, 0.935,
        "Longer bar = more room = easier to disrupt on cost (a sector is cost-disruptable "
        "once a chain sits LEFT of its bar end).\nThe surprise: the most expensive MESTs "
        "(OTC, FX, securities) are the EASIEST to beat on cost — the cheap consumer/gaming "
        "MESTs are the hardest.",
        ha="center", va="top", fontsize=9.5, color="#475569",
    )

    # Legends: sector groups (fixed order) + reference lines already labelled inline.
    from matplotlib.patches import Patch
    handles = [Patch(facecolor=c, label=g) for g, c in GROUP_COLOR.items()]
    ax.legend(handles=handles, title="Sector group", loc="lower right",
              frameon=False, fontsize=9, title_fontsize=9)

    fig.tight_layout(rect=[0, 0, 1, 0.9])
    out = CHARTS_DIR / "mest_disruption_threshold.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return out


def render_scatter(rows) -> Path:
    """Why the cost-easy sectors stay un-disrupted: cost headroom vs. the moat.

    x = disruption threshold b* (cost headroom, log). y = the non-cost moat.
    The payoff: high-value sectors sit top-RIGHT (huge cost headroom, high moat) —
    un-disrupted by institutions, not price. The disruption sweet spot is bottom-
    RIGHT (high headroom, low moat), exactly where stablecoins are winning.
    """
    fig, ax = plt.subplots(figsize=(13, 8.4))
    ax.set_xscale("log")
    x_lo, x_hi, y_hi = 2e-3, 40, 100
    moat_split = 50

    # Quadrant shading + labels (drawn first, behind points).
    ax.axhspan(moat_split, y_hi, xmin=0.5, xmax=1.0, color="#fca5a5", alpha=0.12, zorder=0)
    ax.axhspan(0, moat_split, xmin=0.5, xmax=1.0, color="#86efac", alpha=0.16, zorder=0)
    ax.axhspan(0, moat_split, xmin=0.0, xmax=0.5, color="#fcd34d", alpha=0.12, zorder=0)
    ax.axhline(moat_split, color="#94a3b8", linestyle=":", linewidth=1.2, zorder=1)

    # Chain-cost feasibility boundaries (can a chain even afford this sector?).
    for label, cost, color in CHAIN_REFS[1:]:  # L2, L1
        ax.axvline(cost, color=color, linestyle="--", linewidth=1.4, alpha=0.8, zorder=1)
        ax.text(cost, 2, f"{label}\n~${cost:g}", color=color, fontsize=8.5,
                ha="center", va="bottom", fontweight="bold",
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1))

    for r in rows:
        name, group, b, moat = r[0], r[1], r[6], r[7]
        ax.scatter(b, moat, s=170, color=GROUP_COLOR[group], edgecolor="white",
                   linewidth=1.3, zorder=4)
        ax.annotate(name, (b, moat), xytext=(7, 6), textcoords="offset points",
                    fontsize=9, color="#334155", zorder=5)

    ax.text(2.6, 96, "COST-EASY, MOAT-HARD\nun-disrupted by institutions, not price",
            fontsize=9.5, color="#b91c1c", ha="center", va="center", fontweight="bold", zorder=3)
    ax.text(5.5, 14, "THE SWEET SPOT\nhigh cost headroom + low moat\n(stablecoins are winning here)",
            fontsize=9.5, color="#15803d", ha="center", va="center", fontweight="bold", zorder=3)
    ax.text(6.0e-3, 30, "COST-HARD, MOAT-LOW\nwin on features, not price",
            fontsize=9.5, color="#a16207", ha="center", va="center", fontweight="bold", zorder=3)

    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(0, y_hi)
    ax.set_xlabel(
        "Cost headroom → disruption threshold b* ($/state transition a chain may cost, log)",
        fontsize=10)
    ax.set_ylabel("Institutional moat (legal finality · netting · liquidity · regulation)  →",
                  fontsize=10)
    ax.grid(color="#e2e8f0", linewidth=0.7, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    from matplotlib.patches import Patch
    handles = [Patch(facecolor=c, label=g) for g, c in GROUP_COLOR.items()]
    ax.legend(handles=handles, title="Sector group", loc="upper left",
              frameon=False, fontsize=9, title_fontsize=9)

    fig.suptitle("Why the cost-easy sectors stay un-disrupted: cost headroom vs. the moat",
                 fontsize=14.5, fontweight="bold", x=0.5, y=0.985)
    fig.text(0.5, 0.935,
             "Right = a chain can be very inefficient and still win on cost. Up = the barrier "
             "is institutional, not price.\nHigh-value finance is cost-easy but moat-hard; the "
             "real disruption frontier is the low-moat bottom-right.",
             ha="center", va="top", fontsize=9.5, color="#475569")

    fig.tight_layout(rect=[0, 0, 1, 0.9])
    out = CHARTS_DIR / "mest_cost_vs_moat.png"
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return out


if __name__ == "__main__":
    rows = print_tables()
    p1 = render_chart(rows)
    p2 = render_scatter(rows)
    print(f"\nCharts written to {p1.relative_to(BASE_DIR)}")
    print(f"                 {p2.relative_to(BASE_DIR)}")

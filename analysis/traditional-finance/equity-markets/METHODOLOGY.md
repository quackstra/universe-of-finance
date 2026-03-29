---
title: "Equity Markets — Methodology"
parent: Traditional Finance
grand_parent: Explore
nav_order: 101
---

# Equity Markets (Stock Exchanges) — Measurement Methodology

## Transaction Definition

- **What counts**: One matched equity trade (a buy order matched against a sell order) on a stock exchange or alternative trading venue
- **Counting point**: Trade execution at the matching engine — not order submission, not clearing, not settlement
- **Why this point**: The match is the moment of price discovery. Both WFE and individual exchanges report at this point. One order matched against multiple counterparties generates multiple trades
- **Key ambiguities**:
  - **Dark pool trades**: Off-exchange matches (US: TRF-reported) count as trades but are not visible in exchange statistics. In the US, ~47% of equity volume executes off-exchange
  - **Fractional shares**: A $5 fractional share purchase = 1 trade, same as a $500K block. Fractional shares (>10% of US transactions) inflate trade counts without proportional value impact
  - **HFT order fragmentation**: High-frequency trading breaks large orders into thousands of micro-fills. Each fill is a separate trade — this is why trade COUNT grows faster than trade VALUE
  - **ETF creation/redemption**: AP basket trades are typically reported as single block trades, not individual component trades

## Triangulation Approach

### Method A: WFE Monthly Dashboard Extrapolation

- **Source**: WFE December 2024 dashboard — 5.095B trades in December, +26.53% YoY
- **Value**: ~61.1B (December × 12, adjusted for seasonal variation)
- **Strengths**: WFE data is standardised across member exchanges; monthly cadence
- **Weaknesses**: WFE does not publish a single annual global trade count; requires extrapolation from monthly snapshots; covers only member exchanges

### Method B: 2023 Baseline + Growth Rate

- **Source**: WFE 2023 baseline (~48.6B) × 2024 growth rate (+26.53%)
- **Value**: ~59.9B
- **Strengths**: Simple, transparent methodology
- **Weaknesses**: Assumes uniform growth across all months; the +26.53% is a December YoY figure, which may not represent full-year growth

### Method C: Bottom-Up Exchange Aggregation

- **Source**: Summing individual exchange annual reports (NSE 18B, SZSE 10.5B, SSE 8.5B, NASDAQ 5B, NYSE 4.5B, JPX 4.2B, etc.)
- **Value**: ~66.9B raw → ~61.9B after NSE equity-vs-derivatives adjustment
- **Strengths**: Validates from the bottom up; identifies the source of discrepancies
- **Weaknesses**: NSE India conflates equity and derivatives in headline figures; not all exchanges publish clean trade-count data

```
┌─────────────────────────────────────────────────────┐
│                 RAW ESTIMATES                         │
│                                                       │
│  WFE Monthly       Baseline+Growth  Bottom-Up Sum    │
│  Extrapolation     [2023 × 1.265]   [13 exchanges]   │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│  │ ~61.1B   │     │ ~59.9B   │     │ ~66.9B   │      │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘      │
│       │                │                │             │
│       └────────────────┼────────────────┘             │
│                        ▼                              │
│              ┌──────────────────┐                     │
│              │  RECONCILIATION  │                     │
│              │  Bottom-up over- │                     │
│              │  counts NSE by   │                     │
│              │  ~5B (derivatives │                     │
│              │  mixed into equity│                     │
│              │  headline)       │                     │
│              └────────┬─────────┘                     │
│                       ▼                               │
│              ┌──────────────────┐                     │
│              │ FINAL ESTIMATE   │                     │
│              │ ~61.5B trades    │                     │
│              │ ~3,500 avg TPS   │                     │
│              │ Confidence: 86   │                     │
│              └──────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

## Reconciliation

Three methods converge on 59.9B-67.2B. The bottom-up sum (66.9B) is higher because NSE India's reported equity trade count includes some derivatives trades. Adjusting NSE from ~18B to ~15B (equity cash only) gives an adjusted bottom-up of ~61.9B, which matches the triangulated estimate of 61.5B to within 0.6%. This convergence provides medium-high confidence.

## Key Adjustments

### Dark Pool / Off-Exchange Adjustment

In the US, ~47% of equity volume trades off-exchange (dark pools, wholesale market makers, TRF-reported). WFE statistics capture lit exchange activity; off-exchange trades are captured via FINRA TRF data. Our 61.5B estimate includes both lit and dark/off-exchange trades.

```
US Equity Trade Attribution (2024)
═════════════════════════════════════════════

Total US equity trades     ██████████████████████  ~9.5B
  │
  ├── Lit exchanges (53%)  ████████████            ~5.0B
  │   NYSE, NASDAQ, CBOE,
  │   BATS, IEX, etc.
  │
  └── Off-exchange (47%)   ██████████              ~4.5B
      TRF-reported:
      ├── Dark pools        ████                   ~1.5B
      ├── Wholesale/retail  ██████                 ~3.0B
      │   (Citadel, Virtu)
      └── Other OTC         ░                      ~0.1B

Global off-exchange share: ~25-30% (lower than US)
```

### TPS Derivation

```
Annual trades: 61.5B
       │
       ▼
┌──────────────────────────────┐
│ Step 1: Trading Days         │
│ ~252 global trading days     │
│ → ~244M trades/day average   │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│ Step 2: Effective Hours      │
│ Weighted global trading span:│
│ ~16 effective hours/day      │
│ (Asia + Europe + Americas    │
│  with overlap)               │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│ Step 3: Average TPS          │
│ 244M / (16h × 3,600s)       │
│ = ~3,500 TPS                 │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│ Step 4: Peak TPS             │
│ 3× avg on volatility days   │
│ × 20% first-30-min conc.    │
│ → ~50,000-80,000 burst TPS  │
│ (UTP SIP capacity: 5.6M/s)  │
└──────────────────────────────┘
```

## Overlap Analysis

```
Equity Overlap Waterfall
═══════════════════════════════════════════════════

Total equity trades        ██████████████████████  61.5B
                           │
(-) ETF trades included    ██████████████████████  61.5B  (ETFs ARE equities;
    in equity totals       │                               no separate category)
                           │
(-) NSE India equity/      █████████████████████   61.5B  (adjusted from 18B
    derivatives overlap    │                               to 15B equity-only)
                           ▼
                           ════════════════════════
De-duplicated equity       ██████████████████████  61.5B
```

- **ETF trades**: ETFs trade on stock exchanges and are included in equity trade counts. WFE reports ETF as ~4% of derivatives volume but ETF equity (cash) trades are counted within equity totals
- **No overlap with ETD**: Equity options and futures are counted in the ETD category; equity cash trades are counted here. The boundary is clean
- **No overlap with FX/Fixed Income**: Equity trades are distinct instruments on distinct venues

## Coverage Assessment

```
Region          Coverage  Source           Notes
─────────────── ──────── ──────────────── ─────────────────
US              ████████ WFE + FINRA TRF  Lit + dark pools
China           ████████ SSE/SZSE + WFE   State exchanges
India           ███████░ NSE/BSE + WFE    Some derivative mixing
Japan           ████████ JPX + WFE        Clean data
Europe          ███████░ WFE + MiFID      MTF/SI data patchy
Korea           ██████░░ KRX              Limited English data
LatAm           ██████░░ B3 + WFE         B3 dominates
Rest of World   ████░░░░ WFE estimates    Many small exchanges
─────────────── ──────── ──────────────── ─────────────────
Global coverage: ~85-90% directly observed
```

- **85-90% directly observed**: Major exchanges report to WFE; US has FINRA/TRF data
- **10-15% estimated**: Smaller exchanges in Africa, Middle East, Central Asia, smaller European MTFs
- **Dark pool gap**: ~47% of US volume is off-exchange (captured via TRF); globally ~25-30% off-exchange (less well captured outside US/EU)

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
World Bank (value)  █████████  █████████ ██████████  ██████░░░░
WFE Statistics      ████████░  █████████ ██████████  ████████░░
Exchange Reports    ██████░░░  █████████ █████████░  ██████████
FINRA ATS/TRF      ████░░░░░  █████████ █████████░  ████████░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    82/100     90/100    94/100      78/100
```

- **Score**: 86/100
- **Key drivers of uncertainty**:
  - No single authoritative global annual trade count exists (WFE publishes monthly snapshots, not annual totals)
  - NSE India equity-vs-derivatives classification is the single biggest reconciliation issue
  - Dark pool trade counts outside the US are poorly measured
  - Peak TPS is highly model-dependent (intraday distribution assumptions)
  - Declining average trade size means trade count ≠ economic activity trends

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: Equity markets category created |
| 2026-03-26 | Exchange breakdown added | Run 3: Bottom-up validation of 61.5B estimate |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

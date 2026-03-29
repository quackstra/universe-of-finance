---
title: "OTC Derivatives — Methodology"
parent: Traditional Finance
grand_parent: Explore
nav_order: 106
---

# OTC Derivatives — Measurement Methodology

## Transaction Definition

- **What counts**: One bilateral OTC derivative contract execution — the moment two counterparties agree on terms for an interest rate swap, CDS, equity swap, or commodity swap
- **Counting point**: Trade execution (confirmation). NOT clearing, NOT novation, NOT compression termination. Each unique economic agreement = 1 trade, regardless of whether it is subsequently cleared by a CCP
- **Why this point**: ISDA SwapsInfo reports at the execution level. BIS reports notional outstanding (stock), not trades (flow). Execution is the only consistently available count point
- **Key ambiguities**:
  - **Compression trades**: TriOptima/OSTTRA compression cycles ELIMINATE trades (79% of eligible trades in a single commodity cycle). Compressed trades reduce outstanding but are themselves operational transactions. We count the NET trades remaining after compression, not the compression events
  - **What lifecycle events count**: New trades count. Amendments, partial terminations, novations, and compressions are lifecycle events that do NOT count as new trades in our methodology. If we counted all lifecycle events, the total would be 2-5x higher
  - **FX derivatives excluded**: FX forwards, swaps, and options are OTC derivatives but are counted in the FX category. Our OTC derivatives figure EXCLUDES FX to avoid double-counting (~5M FX derivative trades/year excluded)
  - **SEF vs. bilateral**: SEF-traded IRD (77.3% of count in 2025) and bilaterally negotiated trades both count. The venue does not affect whether something is an OTC derivative

## Triangulation Approach

### Method A: ISDA SwapsInfo (IRD + CDS)

- **Source**: ISDA SwapsInfo full-year 2024 — aggregates DTCC SDR data for US/EU/UK
- **Value**: IRD 2.7M + CDS 525K (index 316.8K + single-name 208.2K) = 3.225M trades in US/EU/UK
- **Strengths**: Highest-confidence data source for OTC derivative trade counts. Based on mandatory trade reporting to swap data repositories. Quarterly cadence
- **Weaknesses**: Covers US/EU/UK only (~85-90% of global IRD/CDS). Does not cover equity or commodity OTC derivatives. Does not cover APAC fully (Japan JSCC is separate)

### Method B: Global Extrapolation with APAC Anchors

- **Source**: ISDA US/EU/UK 3.225M + Japan JSCC (~200K) + other APAC (~120K) + EM (~80K) = ~3.7M for IRD+CDS globally. Add equity OTC (1.2M) + commodity OTC (0.4M)
- **Value**: ~5.3M trades/year (excl. FX)
- **Strengths**: Uses bottom-up segment estimates with identified anchors for each component
- **Weaknesses**: Equity OTC (1.2M) and commodity OTC (0.4M) are low-confidence estimates

### Method C: BIS Notional Cross-Check

- **Source**: BIS Dec 2024 — $732T notional outstanding. Average notional per new IRD trade: ~$118M (derived from ISDA volume/count). Implied annual new trade volume: ~$600T new notional / $118M per trade ≈ 5.1M trades
- **Value**: ~5.1M (order-of-magnitude cross-check)
- **Strengths**: Independent validation using BIS stock data and turnover velocity
- **Weaknesses**: Very rough — assumes constant average trade size and uniform turnover velocity

```
┌─────────────────────────────────────────────────────┐
│                 RAW ESTIMATES                         │
│                                                       │
│  ISDA SwapsInfo    Global Extrap.   BIS Cross-Check   │
│  [US/EU/UK only]   [segmented]      [stock-to-flow]   │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│  │ 3.225M   │     │ 5.3M     │     │ ~5.1M    │      │
│  │ IRD+CDS  │     │ all OTC  │     │ order-of-│      │
│  │ reported │     │ excl. FX │     │ magnitude│      │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘      │
│       │                │                │             │
│       └────────────────┼────────────────┘             │
│                        ▼                              │
│              ┌──────────────────┐                     │
│              │  RECONCILIATION  │                     │
│              │  ISDA provides   │                     │
│              │  high-confidence │                     │
│              │  IRD+CDS anchor; │                     │
│              │  equity+commodity│                     │
│              │  are estimated   │                     │
│              │  overlays        │                     │
│              └────────┬─────────┘                     │
│                       ▼                               │
│              ┌──────────────────┐                     │
│              │ FINAL ESTIMATE   │                     │
│              │ 5.3M trades/yr   │                     │
│              │ excl. FX deriv.  │                     │
│              │ ~0.17 TPS        │                     │
│              │ Confidence: 68   │                     │
│              └──────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

## Reconciliation

ISDA SwapsInfo provides a hard anchor for IRD and CDS in US/EU/UK markets (~3.225M). Adding APAC (JSCC + estimates) gives ~3.7M for IRD+CDS globally. The equity OTC component (1.2M) was revised upward from 0.6M in Run 5 using a structural model decomposing institutional TRS/exotics (250K), institutional CFDs (500K), and structured product hedging (400K). Commodity OTC (0.4M) remains the weakest component. The BIS cross-check at ~5.1M validates the segmented total.

## Key Adjustments

### Lifecycle Event Filtering

```
OTC Derivative Lifecycle — What We Count
═══════════════════════════════════════════════════

New trade execution          ◄── COUNTED (5.3M/year)
       │
       ▼
Trade reporting to SDR       ◄── reporting event, NOT counted
       │
       ▼
Central clearing (CCP)       ◄── novation to CCP, NOT counted
       │                         (76.9% of IRD cleared)
       ▼
Ongoing lifecycle:
  - Rate resets              ◄── NOT counted
  - Margin calls             ◄── NOT counted
  - Partial terminations     ◄── NOT counted
  - Amendments               ◄── NOT counted
       │
       ▼
Compression (OSTTRA)         ◄── ELIMINATES trades from count
  79% of eligible trades          but compression events
  terminated per cycle            themselves NOT counted
       │
       ▼
Maturity / termination       ◄── NOT counted (end of life)
```

If all lifecycle events were counted, the total would be 10-25M+ events/year for IRD alone. Our methodology counts only new executions.

### Equity OTC Structural Model (Run 5)

The equity OTC segment (1.2M) was built bottom-up:

```
Equity OTC Derivatives: 1.2M trades/year
═══════════════════════════════════════════════════

Institutional TRS/exotics    ██████             250K
  Total return swaps, variance
  swaps, exotic options

Institutional CFDs           ████████████       500K
  European market (no US CFDs),
  prime broker-intermediated

Structured product hedging   ██████████         400K
  Bank hedging desk activity
  for retail structured notes

Misc (dividend, correlation) █                  50K
  Dividend swaps, correlation
  trades, basket options
```

## Overlap Analysis

```
OTC Derivatives Overlap Map
═══════════════════════════════════════════════════

OTC Derivatives (this category)    ██████████████  5.3M/year
  │                                               (excl. FX)
  │
  ├── IRD: NOT in Fixed Income     Clean boundary — IRD are
  │   (FI = cash bonds + repo)     derivatives, not cash instruments
  │
  ├── CDS: NOT in Equity Markets   Clean boundary — CDS are
  │   or Fixed Income               derivative credit protection
  │
  ├── Equity OTC: NOT in Equity    Clean boundary — equity
  │   Markets (EM = cash equities)  derivatives vs cash equities
  │
  └── FX derivatives: EXCLUDED     ████████████████  +5.0M
      (counted in FX category)     FX forwards, swaps,
                                   options counted as FX

Grand total if including FX:       ██████████████████  10.3M/year
Primary figure (excl. FX):         ██████████████      5.3M/year
```

- **FX derivatives excluded**: The ~5M FX derivative trades/year are counted in the FX category to avoid double-counting. OTC Derivatives reports 5.3M excluding FX
- **Clean boundaries with ETD**: OTC derivatives are bilateral; ETD are exchange-traded. Interest rate futures (ETD) and interest rate swaps (OTC) are different categories despite covering the same risk
- **No overlap with Fixed Income**: IRS, CDS, and equity swaps are derivatives. Cash bonds and repo are the fixed income instruments

## Coverage Assessment

```
Segment             Coverage   Source            Notes
─────────────────── ────────── ──────────────── ──────────────────
IRD (US/EU/UK)      █████████  ISDA SwapsInfo    2.7M direct count
CDS (US/EU/UK)      █████████  ISDA SwapsInfo    525K direct count
IRD (Japan)         ███████░░  JSCC clearing     ~200K estimated
IRD (other APAC)    ███░░░░░░  Estimated          Limited data
Equity OTC          ████░░░░░  Structural model   Run 5 revision
Commodity OTC       ██░░░░░░░  BIS proportional   Very rough
FX derivatives      ███████░░  Excluded           See FX category
─────────────────── ────────── ──────────────── ──────────────────
IRD+CDS coverage: ~90% directly observed (US/EU/UK/Japan)
Equity+Commodity:  ~15% observed, ~85% estimated
Overall:           ~65% directly observed
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
ISDA SwapsInfo      ██████░░░  █████████ ██████████  ████████░░
BIS OTC Statistics  ██████████ ████████░ ██████████  ████░░░░░░
BIS Triennial       ██████████ ████████░ ██████████  ██████░░░░
JSCC Data           ██░░░░░░░  ████████░ █████████░  ████████░░
Equity OTC model    ██░░░░░░░  ████████░ ████░░░░░░  ██████░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    62/100     86/100    90/100      66/100
```

- **Score**: 68/100
- **Key drivers of uncertainty**:
  - Equity OTC (1.2M) and commodity OTC (0.4M) are the weakest segments — no public aggregate trade count data exists for these
  - Compression effects: if we counted pre-compression gross trades, the total could be 2-5x higher. Our NET count is a choice, not an observation
  - APAC coverage is thin outside Japan — China, India, Korea OTC derivative markets lack accessible English-language trade count reporting
  - The BIS reports notional outstanding (stock), not trades (flow) — flow is always derived
- **High-confidence elements**: ISDA SwapsInfo for IRD and CDS (quarterly, mandatory reporting); BIS notional outstanding ($732T); central clearing rates (76.9% IRD, 67.9% CDS)

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: OTC derivatives category created |
| 2026-03-27 | Count triangulation | Run 4: Segmented model reduced total from 7.3M to 4.7M |
| 2026-03-28 | Equity OTC model | Run 5: Structural decomposition revised equity from 0.6M to 1.2M; total to 5.3M |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

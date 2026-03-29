---
title: "Foreign Exchange — Methodology"
parent: Traditional Finance
grand_parent: Explore
nav_order: 103
---

# Foreign Exchange (FX) — Measurement Methodology

## Transaction Definition

- **What counts**: One FX trade (spot, forward, swap, or option) executed between two counterparties — either on an electronic platform, via voice broker, or bilaterally
- **Counting point**: Trade execution (matching on platform or agreement between counterparties), not settlement. BIS uses "net-net" reporting (each trade counted once, not per side)
- **Why this point**: FX has no central exchange. The BIS Triennial Survey is the only comprehensive global measure, and it reports at the execution point with net-net deduplication
- **Key ambiguities**:
  - **FX swaps vs. spot**: FX swaps (42% of turnover) are financing instruments that roll daily. A single hedging position held for a year generates 252 "transactions" in BIS turnover terms. Are these the same economic transaction repeated, or 252 separate transactions?
  - **Turnover vs. transaction count**: BIS reports VALUE ($9.6T/day), not COUNT. Converting requires average deal size assumptions that vary 100x between retail ($50K) and interbank ($5M+)
  - **Retail FX**: Leveraged retail FX trades (100:1) generate inflated notional per trade. Should a $1K-margin retail trade at 100x leverage count the same as a $100K unleveraged interbank trade?
  - **Internalization**: Major dealers internalize 60-80% of flow (matching buy/sell internally). Internalized trades are counted in BIS surveys but not in venue data

## Triangulation Approach

### Method A: CLS Settlement Extrapolation

- **Source**: CLS 2024 Annual Report — 1.2M payment instructions/day, $7.2T/day settled
- **Value**: ~600K unique trades/day through CLS. CLS covers ~15-25% of global trade COUNT. Implied total: 2.4-4.0M institutional trades/day (central: 3.0M)
- **Strengths**: CLS data is exact — every instruction is a real settlement obligation. Highest-confidence anchor for institutional FX
- **Weaknesses**: CLS covers only 18 currencies and participating institutions. Skews toward large trades. Does not capture retail, bilateral settlement, or EM currencies

### Method B: BIS Counterparty-Segment Decomposition

- **Source**: BIS 2025 Triennial — $9.6T/day with counterparty breakdown (dealer-dealer 46%, dealer-financial 50%, dealer-non-financial 4%)
- **Value**: ~2,984K trades/day (2025), scaled to 2024: ~2,642K
- **Strengths**: Uses authoritative BIS data with segment-specific ticket sizes
- **Weaknesses**: Average ticket size for "dealer-to-other-financial" ($2.5M assumed) is the most impactful single assumption. A shift to $1.5M increases count by 53%

### Method C: Electronic Platform Aggregation

- **Source**: EBS $55.8B/day, LSEG/Refinitiv $100B/day, electronic share ~59% of total
- **Value**: ~2.5M trades/day (electronic + estimated voice)
- **Strengths**: Platform data is precise and published monthly
- **Weaknesses**: Platform share is declining as dark pools and single-dealer platforms grow; misses voice-brokered trades

### Method D: Retail FX Estimation

- **Source**: Retail = 3-5% of value (~$340B/day) at ~$20K avg ticket
- **Value**: ~8-10M retail trades/day (revised to ~8M via broker aggregation)
- **Strengths**: Captures the numerically dominant but economically minor segment
- **Weaknesses**: Leverage inflation makes notional meaningless; broker data is fragmented

### Method E: CME FX Futures Comparable

- **Source**: CME FX futures ADV 1.0-1.2M contracts/day
- **Value**: OTC is 30x larger by value at ~7.5x larger ticket → ~4.4M OTC + 1.1M futures = 5.5M total
- **Strengths**: Clean exchange data as calibration anchor
- **Weaknesses**: OTC-to-exchange ratio and ticket size assumptions introduce large uncertainty

### Method F: Algo/HFT Multiplier

- **Source**: 75-85% of spot FX is algorithmic. HFT at ~$250K avg ticket adds ~1.5M trades/day
- **Value**: ~4.5M total
- **Strengths**: Captures algo fragmentation that other methods undercount
- **Weaknesses**: HFT share and ticket size are industry estimates, not hard data

```
┌─────────────────────────────────────────────────────────┐
│           SIX-APPROACH COUNT TRIANGULATION                │
│                                                           │
│  A: CLS        B: BIS Seg.    C: Platforms    D: Retail  │
│  ┌────────┐   ┌────────┐    ┌────────┐     ┌────────┐   │
│  │ 3.0M   │   │ 2.6M   │    │ 2.5M   │     │ 8.0M   │   │
│  │inst/day│   │inst/day│    │inst/day│     │ret/day │   │
│  └───┬────┘   └───┬────┘    └───┬────┘     └───┬────┘   │
│      │            │             │               │        │
│      └─────┬──────┘             │               │        │
│            ▼                    │               │        │
│  ┌──────────────┐              │               │        │
│  │ INSTITUTIONAL │◄─────────────┘               │        │
│  │  CONVERGENCE  │                              │        │
│  │  2.5-3.0M/day│                              │        │
│  └──────┬───────┘                              │        │
│         │                                       │        │
│  E: CME  F: Algo/HFT                           │        │
│  ┌────┐  ┌────┐                                 │        │
│  │5.5M│  │4.5M│  ← partially capture retail/    │        │
│  └──┬─┘  └──┬─┘    algo activity                │        │
│     │       │                                   │        │
│     └───┬───┘                                   │        │
│         ▼                                       ▼        │
│  ┌──────────────────────────────────────────────────┐    │
│  │              FINAL ESTIMATES                      │    │
│  │  Institutional: ~3.0M/day  (~35 TPS)             │    │
│  │  + Retail:      ~8.0M/day                         │    │
│  │  = Total:      ~11.0M/day  (~127 TPS)             │    │
│  │  Primary estimate: 3.5M/day (~40 TPS) institutional│    │
│  └──────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

Methods A-C converge on ~2.5-3.0M institutional trades/day. This is the high-confidence core. Retail (Method D) adds ~8M numerically dominant but economically minor trades. Methods E-F yield intermediate values (4.5-5.5M) as they partially capture both institutional and retail/algo activity. The primary estimate of ~3.5M/day (~40 TPS) uses the institutional-only figure plus a small uplift for voice/bilateral trades not captured by CLS or platforms.

## Key Adjustments

### The Count Opacity Problem

FX is unique among major financial markets: no authority publishes transaction counts. The BIS Triennial is the gold standard for VALUE but does not count trades. This methodology section documents the most complex count triangulation in the Universe of Finance project.

### Roll Inflation in FX Swaps

FX swaps (42% of $9.6T daily) are financing instruments that roll daily. A hedging position maintained for one year generates 252 "transactions" in BIS terms. For TPS purposes, we count each roll as a transaction (it IS a new contractual agreement), but note that the economic content per roll is minimal.

```
FX Swap Roll Inflation Example
═══════════════════════════════════════

Corporate hedges $100M EUR/USD for 1 year:

BIS count: 252 transactions (daily rolls)
Economic reality: 1 hedging decision

This inflates FX TPS by an estimated 30-40%
relative to "economically unique decisions"
```

### Dealer-to-Other-Financial Ticket Size Sensitivity

The single most impactful assumption in the institutional count. The "dealer-to-other-financial" segment (50% of 2025 turnover, $4.8T/day) includes hedge funds, asset managers, pension funds, central banks, and prop firms — entities with wildly different trade sizes:

| If avg ticket is: | Implied segment trades/day | Impact on total institutional |
|-------------------|---------------------------|------------------------------|
| $1.5M            | 3.2M                      | +53% vs central estimate     |
| $2.5M (central)  | 1.92M                     | baseline                     |
| $4.0M            | 1.2M                      | -37%                         |

## Overlap Analysis

```
FX Overlap Waterfall
═══════════════════════════════════════════════════

Total FX trades              ██████████████████████  ~880M/year
  │                                                  (institutional)
  │
(-) FX derivatives overlap   ██████████████████████  ~880M/year
    with OTC Derivatives     │
    category                 │  FX forwards, swaps,
                             │  and options are OTC
                             │  derivatives — counted
                             │  HERE (FX category),
                             │  EXCLUDED from OTC
                             │  Derivatives category
                             │
(-) FX ETD (CME, etc.)       ██████████████████████  ~880M/year
    counted in ETD category  │  Exchange-traded FX
                             │  futures/options are
                             │  in ETD, NOT here
                             ▼
                             ════════════════════════
De-duplicated FX             ██████████████████████  ~880M/year
                             (OTC FX only; ETD FX
                              excluded to avoid
                              double-count)
```

- **FX derivatives counted HERE, not in OTC Derivatives**: Per project taxonomy, FX forwards, swaps, and options are counted as FX transactions. The OTC Derivatives category excludes FX to avoid double-counting
- **FX ETD counted in ETD category**: CME FX futures (~1.0-1.2M contracts/day) are in the ETD total, not here
- **No overlap with payments**: FX trades are wholesale/institutional. Consumer currency exchange (at airports, banks) is not captured in BIS data

## Coverage Assessment

```
Region          Coverage   Source               Notes
─────────────── ────────── ──────────────────── ──────────────
London (38%)    █████████  BOE semi-annual      Best single-venue data
New York (19%)  █████████  FRBNY FXC survey     21 major dealers
Singapore (9%)  ████████░  MAS survey           Growing coverage
Hong Kong (7%)  ████████░  HKMA survey          Mainland China flows
Tokyo (4%)      ███████░░  BOJ survey           Declining share
CLS (35% value) █████████  CLS 2024 Annual      600K unique trades/day
Rest of World   ████░░░░░  BIS Triennial only   Every 3 years
─────────────── ────────── ──────────────────── ──────────────
VALUE coverage:  ~95% (BIS Triennial)
COUNT coverage:  ~25-30% directly observed (CLS + platforms)
                 ~70-75% estimated via triangulation
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
BIS Triennial       ██████████ █████████ ██████████  ██████░░░░
CLS Settlement      ████░░░░░  █████████ █████████░  █████████░
FRBNY FXC Survey    ███░░░░░░  █████████ █████████░  ████████░░
BOE Semi-Annual     ███░░░░░░  █████████ █████████░  ████████░░
Platform data       ██░░░░░░░  █████████ ██████░░░░  ██████████
                    ─────────  ────────  ──────────  ───────────
Composite Score:    60/100     90/100    92/100      72/100
```

- **Score**: 58/100
- **Key drivers of uncertainty**:
  - BIS reports VALUE, not COUNT — the entire count estimate is derived, not observed
  - The dealer-to-other-financial average ticket size ($1.5-4.0M range) creates a 2x uncertainty band in institutional count
  - Retail FX trade count (5.8-11.4M/day range) is the largest single segment by count but the least well measured
  - BIS Triennial runs every 3 years (April 2025 latest); inter-survey years are interpolated
  - FX swap roll inflation makes TPS comparisons with other asset classes conceptually fraught
- **High-confidence elements**: Daily turnover value ($9.6T/day), CLS settlement data, instrument breakdown

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: FX category created with BIS 2025 data |
| 2026-03-27 | Six-approach triangulation | Run 4: Count triangulation from 6 independent methods |
| 2026-03-28 | Retail broker aggregation | Run 5: Retail revised from ~10M to ~8M/day |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

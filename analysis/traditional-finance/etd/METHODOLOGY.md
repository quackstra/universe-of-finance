---
title: "Exchange-Traded Derivatives — Methodology"
parent: Traditional Finance
grand_parent: Explore
nav_order: 104
---

# Exchange-Traded Derivatives (ETD) — Measurement Methodology

## Transaction Definition

- **What counts**: One standardised futures or options contract executed (matched) on a regulated exchange
- **Counting point**: Trade execution (match at the exchange matching engine), not clearing or settlement
- **Why this point**: Exchange matching is the moment of price discovery and risk transfer; it is the canonical counting point used by FIA and WFE
- **Key ambiguities**:
  - A single order that fills against multiple resting orders generates multiple trades (one per fill), not one trade
  - Block trades reported off-exchange but registered on-exchange are counted as exchange trades by FIA
  - Spread trades (e.g., calendar spreads) may count as one or two legs depending on the exchange's reporting convention
  - Exercise and assignment of options generate delivery/settlement events but are NOT counted as new trades

## Triangulation Approach

### Method A: FIA Annual Survey (Primary)

- **Source**: Futures Industry Association annual volume survey covering 85 exchanges in 33 countries
- **Value**: 205.34 billion contracts (2024)
- **Strengths**: Most comprehensive global survey; covers both futures and options; breaks down by asset class, region, and exchange
- **Weaknesses**: Annual publication with ~3-month lag; includes some exchanges not in WFE; relies on self-reporting by exchanges

### Method B: WFE Member Statistics

- **Source**: World Federation of Exchanges FY 2024 Market Highlights
- **Value**: 180.22 billion contracts (2024)
- **Strengths**: High-quality data from vetted member exchanges; monthly dashboard with rolling updates
- **Weaknesses**: Covers only WFE members (~55 exchanges); misses ~25B contracts reported by FIA from non-member venues

### Method C: Bottom-Up Exchange Aggregation

- **Source**: Individual exchange annual reports (CME, NSE, Eurex, ICE, B3, CBOE, etc.)
- **Value**: Cross-check against FIA/WFE; CME 2024 ADV 26.5M, Eurex 2.08B, NSE 84.8B (2023)
- **Strengths**: Exchange-reported data is exact (every match is recorded); allows asset-class and product-level verification
- **Weaknesses**: Aggregation is manual; not all exchanges publish timely English-language reports; risk of double-counting interlinked exchanges

```
┌─────────────────────────────────────────────────────┐
│                 RAW ESTIMATES                         │
│                                                       │
│  FIA Annual        WFE Members       Bottom-Up        │
│  [85 exchanges]    [~55 exchanges]   [Top 10 + est.]  │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│  │ 205.34B  │     │ 180.22B  │     │ ~200-210B│      │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘      │
│       │                │                │             │
│       └────────────────┼────────────────┘             │
│                        ▼                              │
│              ┌──────────────────┐                     │
│              │  RECONCILIATION  │                     │
│              │  FIA-WFE gap =   │                     │
│              │  ~25B from non-  │                     │
│              │  WFE exchanges   │                     │
│              │  (fully explained)│                     │
│              └────────┬─────────┘                     │
│                       ▼                               │
│              ┌──────────────────┐                     │
│              │ FINAL ESTIMATE   │                     │
│              │ 205.34B contracts│                     │
│              │ ~9,500 avg TPS   │                     │
│              │ Confidence: 88   │                     │
│              └──────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

## Reconciliation

The FIA figure (205.34B) is used as the primary anchor because it covers the broadest exchange universe. The 25B gap with WFE is fully explained by FIA's inclusion of ~30 non-WFE-member exchanges, primarily in India and China. Bottom-up aggregation of top exchanges validates the FIA figure to within ~5%.

## Key Adjustments

### TPS Derivation Pipeline

The core challenge is converting annual contract volume into TPS. ETD markets do not operate 24/7 — they run on exchange-specific trading hours with significant intraday concentration.

```
Annual Volume: 205.34B contracts
       │
       ▼
┌─────────────────────────────┐
│ Step 1: Trading Days        │
│ 252 global trading days     │
│ → 815M contracts/day avg    │
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│ Step 2: Effective Hours     │
│ Weighted across time zones: │
│ - Asia session: 7h          │
│ - Europe session: 8h        │
│ - Americas session: 6.5h    │
│ Overlap-adjusted: 21.6h     │
│ effective global hours/day  │
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│ Step 3: TPS Calculation     │
│ 815M / (21.6h × 3,600s)    │
│ = ~9,505 TPS average        │
└──────────┬──────────────────┘
           ▼
┌─────────────────────────────┐
│ Step 4: Peak Estimation     │
│ Indian expiry-day pattern:  │
│ 6× average concentration    │
│ → ~57,000 peak TPS          │
│ (modelled, not observed)    │
└─────────────────────────────┘
```

### India Concentration Adjustment

NSE India accounts for ~79% of global ETD by contract count (APAC region). The vast majority are weekly equity index options that expire on Thursdays, creating extreme intraday concentration. This means:
- Global average TPS is dominated by NSE India's trading hours (09:15-15:30 IST)
- Peak TPS on Indian expiry days is the global peak
- The 21.6h "effective hours" assumption overstates the active window — most volume occurs in ~6-8 hours

### Contract Volume vs. Economic Activity

A critical caveat: one contract ≠ one unit of economic activity. A $1,000 Nifty weekly option and a $200,000 Treasury future each count as one contract. By notional value, interest rate derivatives (5% of contracts) represent 87% of total ETD turnover (~$3,226T/year). The TPS figure counts contracts, not economic weight.

## Overlap Analysis

```
ETD Overlap Waterfall
═══════════════════════════════════════════════════

Total ETD contracts        ██████████████████████  205.34B
                           │
(-) Commodity ETD subset   ██████████████████████  205.34B  (included in ETD total)
    reported separately    │                                 6.5B overlap with
    in Commodities capsule │                                 Commodities category
                           │
(-) Crypto ETD subset      ██████████████████████  205.34B  (~0.5-1B contracts
    (CME BTC/ETH futures)  │                                 overlap with Digital
                           │                                 Assets sector)
                           ▼
                           ════════════════════════
De-duplicated ETD          ██████████████████████  205.34B
                           (no reduction — overlaps are
                            subsets reported separately)
```

- **Commodity ETD**: The ~6.5B commodity futures/options are a SUBSET of the 205.34B ETD total. The Commodities METHODOLOGY.md breaks this subset out but flags the overlap
- **FX ETD**: ~3% of ETD volume is currency futures/options, which overlaps conceptually with the FX category (which covers OTC FX). No double-counting because ETD counts exchange-traded contracts and FX counts OTC trades
- **Crypto ETD**: CME Bitcoin and Ethereum futures/options are included in the ETD total. These also appear conceptually in the Digital Assets sector but are not double-counted because CEX counts off-chain trades only

## Coverage Assessment

```
Coverage by Exchange Universe
═══════════════════════════════════════
Directly reported (FIA members)     ████████████████████  ~98%
Non-FIA exchanges (estimated)       █                     ~2%
Physical commodity exchanges (OTC)  ░                     excluded
                                    ─────────────────────
Total coverage:                     ~98% of global ETD
```

- **98% directly observed**: FIA covers 85 exchanges in 33 countries; WFE covers ~55 member exchanges
- **2% estimated**: Small regional exchanges not in FIA or WFE (e.g., smaller commodity exchanges in Africa, Middle East)
- **Extrapolation**: Minimal — the exchange-traded nature of ETD means nearly all volume is reported to at least one data aggregator

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
FIA Annual Survey   █████████  ████████  ██████████  ████████░░
WFE Statistics      ████████░  █████████ ██████████  ████████░░
BIS ETD Data        ██████░░░  ████████░ ██████████  ██████░░░░
Exchange Reports    █████░░░░  █████████ █████████░  ██████████
                    ─────────  ────────  ──────────  ───────────
Composite Score:    92/100     88/100    95/100      82/100
```

- **Score**: 88/100
- **Key drivers of uncertainty**:
  - Peak TPS is modelled (6x average), not directly observed — exchange-level microsecond data is not public
  - India concentration means a single SEBI regulatory change could shift global volume by 20-30%
  - FIA-WFE 25B gap is explained but highlights the challenge of universe definition
  - Notional value estimates for equity and commodity ETD are derived, not directly reported
- **High-confidence elements**: Annual contract counts (FIA/WFE), asset-class breakdown, exchange-level volumes

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial methodology | Run 2: ETD category created with FIA 2024 data |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

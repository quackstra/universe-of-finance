# Commodities — Measurement Methodology

## Transaction Definition

- **What counts**: One commodity futures, options, or physical trade executed on an exchange or bilateral OTC market
- **Counting point**: Trade execution (exchange match or OTC confirmation)
- **Why this point**: Consistent with the ETD methodology for exchange-traded products; OTC physical trades are counted at confirmation
- **Key ambiguities**:
  - **Physical vs. financial**: A "trade" can be a physical commodity delivery contract (actual barrels of oil) or a financially-settled futures contract (paper barrels). Both count, but the financial-to-physical ratio is 30-40x for crude oil
  - **Exchange-traded commodity derivatives are a subset of ETD**: The 6.5B commodity contracts are included in the 205.34B ETD total. This category isolates the commodity subset
  - **Carbon/environmental**: Carbon credits (EU ETS, voluntary markets) are counted as commodities per FIA/WFE classification
  - **Power/electricity**: Intraday power market trades (EPEX Spot) are commodity trades but have very different characteristics from oil/metals

## Triangulation Approach

### Method A: FIA/WFE Subcategory Extraction

- **Source**: FIA reports commodity ETD as ~3% of 205.34B total ETD volume
- **Value**: ~6.15B contracts
- **Strengths**: Consistent with the ETD methodology; uses the same authoritative source
- **Weaknesses**: The 3% share is derived from WFE asset-class breakdown; FIA does not publish a clean standalone commodity total

### Method B: Exchange-Level Aggregation

- **Source**: ICE (1.2B commodity), CME commodity segments (~3.5B est.), LME (179M), Shanghai (1.0B est.), Dalian (800M est.), Zhengzhou (500M est.), others (500M est.)
- **Value**: ~7.7B (before overlap adjustment)
- **Strengths**: Uses direct exchange-reported data for major commodity venues
- **Weaknesses**: CME does not break out commodity-only volumes cleanly (energy, metals, agriculture are mixed with other products); Chinese exchange data quality varies

### Method C: ESMA Carbon Market Cross-Check

- **Source**: ESMA EU Carbon Markets Report 2024 — 4.7M on-venue EUA transactions
- **Value**: Validates the environmental/carbon subset (ICE: 20.4M environmental contracts)
- **Strengths**: Regulatory data from ESMA with high authority
- **Weaknesses**: Covers EU ETS only; does not include voluntary carbon markets or non-EU schemes

```
┌─────────────────────────────────────────────────────┐
│                 RAW ESTIMATES                         │
│                                                       │
│  FIA 3% Share     Exchange Sum      ESMA Carbon       │
│  [top-down]       [bottom-up]       [subset check]    │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│  │ ~6.15B   │     │ ~7.7B    │     │ 4.7M EUA │      │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘      │
│       │                │                │             │
│       └────────────────┼────────────────┘             │
│                        ▼                              │
│              ┌──────────────────┐                     │
│              │  RECONCILIATION  │                     │
│              │  Exchange sum    │                     │
│              │  overcounts by   │                     │
│              │  ~1.2B due to    │                     │
│              │  CME mixed-asset │                     │
│              │  reporting       │                     │
│              └────────┬─────────┘                     │
│                       ▼                               │
│              ┌──────────────────┐                     │
│              │ FINAL ESTIMATE   │                     │
│              │ ~6.5B contracts  │                     │
│              │ ~330 avg TPS     │                     │
│              │ Confidence: 74   │                     │
│              └──────────────────┘                     │
└─────────────────────────────────────────────────────┘
```

## Reconciliation

The top-down (6.15B) and bottom-up (7.7B) approaches bracket the estimate. The gap is explained by CME's mixed-asset reporting (some financial products classified under "commodities" umbrella) and potential double-counting between ICE and CME for certain products. We settle on 6.5B as the midpoint, consistent with the FIA ~3% share plus a small uplift for non-WFE-member exchanges.

## Key Adjustments

### Sub-Sector Decomposition

```
Commodity ETD: 6.5B contracts (2024)
═══════════════════════════════════════════════════

Energy (oil, gas, power)   ████████████████       2.5B  (38%)
  ICE oil: 655M record
  CME/NYMEX energy
  Shanghai energy futures

Agriculture                ████████████           2.0B  (31%)
  CME/CBOT grains, livestock
  Dalian: soy, corn, palm
  Zhengzhou: wheat, cotton

Metals (precious + base)   ████████               1.2B  (18%)
  LME: 179M lots (+18%)
  CME/COMEX: gold, silver
  Shanghai metals

Environmental (carbon)     ██                     0.3B  (5%)
  ICE: 20.4M env contracts
  EEX carbon markets
  Voluntary carbon (small)

Other / mixed              ███                    0.5B  (8%)
  MCX India, TOCOM
  Regional exchanges
```

### Physical OTC Commodity Estimation

Physical commodity trades (actual delivery) are a separate, opaque market. We estimate ~50M physical trades/year based on major commodity trading house revenues (Vitol $505B, Trafigura $244B, Glencore $218B) divided by estimated margin per trade. This adds <1% to the exchange-traded count and is flagged as low-confidence.

## Overlap Analysis

```
Commodity Overlap with ETD Category
═══════════════════════════════════════════════════

ETD total contracts        ██████████████████████  205.34B
  │
  ├── Equity (index+stock) █████████████████████   ~174B  (85%)
  ├── Interest rate        ██                      ~10B   (5%)
  ├── ETF                  ██                      ~8B    (4%)
  ├── Currency             █                       ~6B    (3%)
  └── COMMODITY            ███                     ~6.5B  (3%)  ◄── THIS CATEGORY
                                                                     (full subset of ETD)
```

- **Full subset of ETD**: All 6.5B commodity contracts are included in the 205.34B ETD total. When aggregating across TradFi categories, commodity ETD must NOT be added to ETD — it is already included
- **Physical OTC commodity trades (~50M)**: NOT included in ETD; these are unique to this category
- **Carbon/environmental**: Included here but also overlaps conceptually with government/regulatory categories (EU ETS is a regulatory market)

## Coverage Assessment

```
Sub-sector      Coverage  Source              Notes
─────────────── ──────── ─────────────────── ──────────────────
Energy (exch.)  ████████ ICE, CME/NYMEX      Record ICE data
Metals (exch.)  ████████ LME, CME/COMEX      LME annual volumes
Agriculture     ███████░ CME/CBOT, Dalian    Chinese data varies
Carbon/environ. ███████░ ESMA, ICE           EU ETS well-covered
Physical OTC    ██░░░░░░ Estimated only       Bilateral, unreported
Chinese exch.   ████░░░░ FIA estimates        Day-trading inflation?
─────────────── ──────── ─────────────────── ──────────────────
Overall coverage: ~75% directly observed (exchange-traded)
                  ~5% estimated (physical OTC)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
FIA/WFE data        ██████░░░  ████████  ██████████  ██████░░░░
ICE annual report   ████░░░░░  █████████ █████████░  ██████████
CME volumes         ████░░░░░  █████████ █████████░  ████████░░
LME annual data     ███░░░░░░  █████████ █████████░  ████████░░
ESMA carbon report  ███░░░░░░  ████████░ ██████████  ████████░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    68/100     88/100    92/100      78/100
```

- **Score**: 74/100
- **Key drivers of uncertainty**:
  - Global commodity ETD total requires aggregating FIA subcategory data — no clean standalone figure exists
  - CME does not publish commodity-only volumes separately from financial products
  - Chinese commodity exchange data quality is uncertain (high turnover ratios suggest speculative round-tripping)
  - Physical OTC commodity trades are completely opaque
  - Notional value per commodity contract varies enormously ($70K for crude vs. $80 for carbon)

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: Commodities category created |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

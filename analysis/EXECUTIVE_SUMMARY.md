---
title: "Executive Summary"
layout: default
nav_order: 2
---

# Universe of Finance — Executive Summary

> Measuring every financial transaction on Earth, expressed as one number.

*A research brief from the Universe of Finance project. March 2026.*

---

## Abstract

The Universe of Finance project measures the total throughput of the global
financial system across 29 transaction categories spanning 7 sectors — from
Visa swipes to repo trades, UPI taps to video game loot boxes. Our central
estimate is **~73,750 de-duplicated financial transactions per second**,
or ~2.3 trillion per year. But transactions are only the visible tip: each
one triggers a cascade of bilateral state changes across institutions,
ledgers, and jurisdictions. We introduce the **MEST framework** (Mutual
Economic State Transitions) and estimate the true bilateral state-change
rate at **~545,000 per second** — 7.4 times the transaction count. This
distinction has profound implications for infrastructure design, blockchain
scalability arguments, and the $350-400 billion annual cost of financial
plumbing.

---

## 1. The Big Number

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        ~73,750 de-duplicated global financial TPS             ║
║                                                               ║
║        ~2.3 trillion transactions per year                    ║
║        Range: 67,000 – 83,000 TPS                            ║
║                                                               ║
║        Coordinated global peak: ~147,000 – 246,000 TPS       ║
║        (flash crash on a busy quarter-end)                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

This number captures every measurable financial transaction on the planet:
consumer card swipes, real-time bank transfers, equity trades, derivatives
contracts, cryptocurrency exchanges, ATM withdrawals, payroll disbursements,
insurance premiums, government payments, IoT micropayments, and more.

It is derived from 29 independent research capsules, each triangulated against
2-3 data sources, then de-duplicated using a rigorous overlap matrix that
accounts for transactions counted in multiple categories (e.g., a digital
wallet payment that settles on a card rail).

### What ~73,750 TPS Means

To put this in context:

| Comparison | TPS |
|------------|-----|
| Visa network capacity (theoretical) | ~65,000 |
| **Entire global financial system (measured)** | **~73,750** |
| Bitcoin (mainchain) | ~7 |
| Solana (meaningful, after vote/spam filter) | ~350-480 |

The global financial system processes slightly more transactions per second
than a single card network's theoretical maximum. This is possible because
~75% of global TPS is payments, and card networks are only one of several
payment rails.

### TPS Leaderboard — Top 10

```
    Category              De-Dup TPS    Share     Sector
    ─────────────────── ─────────── ──────── ──────────────
 1. Consumer Cards         24,501     33.2%    Payments
 2. Digital Wallets        12,938     17.5%    Payments
 3. Bank Transfers         15,338     20.8%    Payments
 4. ETD (Derivatives)       9,505     12.9%    Trad Finance
 5. Equity Markets          3,500      4.7%    Trad Finance
 6. CEX (Crypto)            3,210      4.4%    Digital Assets
 7. ATM Withdrawals         1,557      2.1%    Payments
 8. IoT / M2M                385      0.5%    Emerging
 9. P2P Transfers             270      0.4%    Payments
 10. Payroll (incr.)          131      0.2%    Payments
    ─────────────────── ─────────── ──────── ──────────────
    Top 3 = ~71% of global TPS
```

The concentration is striking: **consumer cards, bank transfers, and digital
wallets alone account for over 70% of all financial transactions on Earth.**

---

## 2. The MEST Number

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        ~545,000 Mutual Economic State Transitions / second    ║
║                                                               ║
║        ~17.2 trillion bilateral state changes per year        ║
║        Global average MEST multiplier: 7.4x                   ║
║        Range: 410,000 – 720,000 MEST/s                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### What Is a MEST?

A **Mutual Economic State Transition** is any change to a holding of
economically valuable assets where more than one party has a material
interest in the record. Three properties must hold:

1. **State change** — an asset changes state (balance, ownership, obligation)
2. **Mutual interest** — two or more parties care about the record's accuracy
3. **Materiality** — not trivial internal bookkeeping within one entity

When you buy a coffee with a credit card, one transaction happens from your
perspective. Underneath, **seven bilateral state changes** ripple across five
institutions: an authorization hold, a clearing match, an interchange
allocation, two settlement legs, a merchant credit, and a statement entry.

```
    The MEST Iceberg

                     /\
                    /  \         "I bought a coffee"
                   / 1  \       <- The Transaction
                  / TXN  \
    ────────────/──────────\──────────── waterline ────
               /            \
              /   6-8 MESTs  \    Auth, clearing,
             /   per card     \   settlement, merchant
            /   purchase       \  credit, interchange,
           /                    \ rewards, statement
          /______________________\
```

The Big Number answers: *How many economic events happen per second?*
The MEST Number answers: *How many bilateral state changes does the global
economy actually process per second?*

### Why MEST Matters

- **Infrastructure sizing** — Settlement systems and clearing houses must
  handle MEST volume, not transaction volume
- **Blockchain scalability** — A chain that replaces traditional rails must
  handle the MEST load, not just TPS
- **Operational risk** — Each MEST is a reconciliation point that can fail
- **Cost modeling** — The cost of financial plumbing is proportional to
  MEST volume, not transaction volume

### MEST by Sector

```
    Sector              MEST/s      % of Total    Avg Multiplier
    ──────────────── ────────── ──────────── ──────────────
    Payments           383,655       70.4%         5-7x
    Trad Finance       134,122       24.6%         8-12x
    Digital Assets      15,230        2.8%         2-4x
    Government           5,075        0.9%         5x
    Gaming               1,701        0.3%         3x
    Emerging             4,639        0.9%         3x
    Banking                326        0.1%         3-4x
    ──────────────── ────────── ──────────── ──────────────
    TOTAL             ~544,750      100.0%         7.4x
```

Traditional finance produces 18% of transactions but **25% of MESTs**,
because exchange-traded and OTC instruments have deeper clearing and
settlement cascades. Digital assets produce 5% of transactions but only
3% of MESTs — the lowest multipliers in the system.

---

## 3. Key Findings

1. **Payments dominate.** 75% of global TPS is payment transactions. Cards,
   bank transfers, and digital wallets are the backbone of world finance.

2. **India punches above its weight.** 17.4% of global TPS on 3.5% of global
   GDP. #1 in equity trades (28% of global volume), #1 in real-time payments
   (UPI), and growing fast in cards (RuPay).

3. **Double-counting is ~14%, not 50%.** The raw sum across 29 categories is
   ~89,300 TPS. De-duplication removes ~17%. The biggest single overlap is
   UPI (172B transactions counted in both wallets and bank transfers).

4. **The MEST multiplier is 7.4x.** Every transaction generates an average
   of 7.4 bilateral state changes. OTC derivatives are the deepest (12x);
   on-chain L1/L2 transfers are the shallowest (2x).

5. **Crypto is 5% of TPS, not 50%.** After Solana vote/spam filtering and
   CEX wash-trade adjustment, digital assets are ~3,625 TPS — roughly the
   throughput of equity markets alone.

6. **The global MEST Tax is $350-400 billion per year.** This is the
   infrastructure cost of processing 17.2 trillion bilateral state changes
   annually — clearing, settlement, reconciliation, and reporting.

7. **DLT compresses MESTs 60-80%.** Blockchain-native transactions achieve
   2-3x MEST multipliers vs. 7-12x for traditional equivalents. Full
   theoretical compression: ~345,000 fewer MEST/s, saving $150-250B/year.

8. **Growth is 6.7x in a decade.** Global gross TPS grew from ~12,900 (2015)
   to ~86,900 (2025). The fastest growers are blockchain-native (RWA 119%
   CAGR, stablecoins 103%), but traditional payments add more absolute TPS.

9. **ATM is the only declining category.** -3% CAGR, down from 63B peak.
   Every other category is growing. Growth outpaces decline 38:1.

10. **Recessions barely move the Big Number.** A 2008-style recession changes
    TPS by only -0.3% because trading surges offset payment declines.
    Pandemics *increase* it (+18-28%) via cash-to-digital migration.

---

## 4. Methodology

### Approach: Triangulation-First

Each of the 29 categories was researched using a triangulation-first method:

1. Find 2-3 independent data sources that measure the same thing differently
2. Build bottom-up AND top-down models, then reconcile
3. Document assumptions, blind spots, and confidence explicitly
4. Quantify overlaps with other categories to enable accurate de-duplication

### Taxonomy: 29 Categories, 7 Sectors

| Sector | # | Combined Gross TPS | Key Categories |
|--------|---|-------------------|----------------|
| Payments | 11 | ~67,600 | Cards, wallets, bank transfers, ATM, bills |
| Traditional Finance | 6 | ~13,400 | ETD, equities, forex, fixed income |
| Digital Assets | 4 | ~4,100 | CEX, L1/L2, stablecoins, DeFi |
| Banking | 2 | ~100 | RTGS, securities settlement |
| Gaming | 2 | ~480 | Microtransactions, game sales |
| Government | 1 | ~1,000 | Tax and benefits disbursements |
| Emerging | 3 | ~1,540 | IoT/M2M, RWA tokenisation, AI agents |

### Confidence Scoring (0-100)

Every category receives a composite confidence score across four dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Source Quality | 0-30 | Primary vs. estimated data |
| Data Recency | 0-20 | How fresh the underlying data is |
| Triangulation | 0-25 | Independent methods that agree |
| Coverage | 0-25 | % of known market captured |

**Results:** Median score 62. Range: 34 (AI Agents) to 91 (Consumer Cards).
Eight categories score above 74 (High confidence); six score below 52
(Medium or lower).

```
    Confidence Distribution (29 categories)

    90-100  █                                     1  (Cards)
    80-89   ███                                   3  (ETD, Equities, RTGS)
    70-79   ████                                  4  (Bank Xfers, L1/L2, ...)
    60-69   ███████                               7  (Wallets, IoT, P2P, ...)
    50-59   ████████                              8  (CEX, RWA, ATM, ...)
    40-49   ██                                    2  (Gaming Microtx, ...)
    30-39   ████                                  4  (Payroll, AI Agents, ...)
```

### Overlap De-Duplication

Raw TPS across all 29 categories sums to ~89,300. The de-duplication process
removes ~17% (~15,550 TPS) of overlaps:

| Overlap Type | TPS Removed | Example |
|-------------|-------------|---------|
| Wallet-on-card-rail | ~6,722 | Apple Pay settling on Visa |
| Bill/payroll/insurance on bank rails | ~3,582 | Direct debit bill payments |
| E-commerce on card/wallet rails | ~1,732 | Amazon checkout on Visa |
| Gaming on card/wallet rails | ~393 | Steam purchase on Mastercard |
| DeFi/Stablecoins subset of L1/L2 | ~650 | Uniswap swap = L1 txn |
| Government on bank rails | ~601 | Tax payment via ACH |
| IoT on card/bank rails | ~1,153 | E-ZPass on linked card |

The biggest single overlap is UPI: 172 billion transactions counted in both
digital wallets and bank transfers. This is handled by classifying UPI as
a bank transfer (its true settlement rail) and deducting it from wallets.

---

## 5. The MEST Advantage — DLT Compression Thesis

### The Core Argument

Blockchain-native transactions do not win on speed — traditional rails are
faster. They win on **MEST compression**: fewer bilateral state changes per
economic event, because intermediaries are eliminated from the cascade.

| Activity | Traditional MEST | DLT MEST | Reduction |
|----------|-----------------|----------|-----------|
| Asset transfer | 5-7x | 2x | 60-70% |
| Securities trade | 10x | 2-3x | 70-80% |
| Derivatives | 10-12x | 3-4x | 65-70% |
| Cross-border payment | 7x | 2-3x | 60-70% |

### The Numbers

```
    CURRENT STATE (2025)
    ────────────────────
    Global MEST/s:              545,000
    Average multiplier:         7.4x
    Annual MEST Tax:            $350-400 billion

    FULL DLT COMPRESSION (theoretical ceiling)
    ────────────────────────────────────────────
    Global MEST/s:              ~200,000
    Average multiplier:         ~2.7x
    MESTs eliminated:           ~345,000/s  (63%)
    Annual savings:             $150-250 billion

    REALISTIC 2035 SCENARIO (partial adoption)
    ────────────────────────────────────────────
    Global MEST/s:              ~650,000  (volume growth offsets
                                           partial compression)
    Average multiplier:         ~6.0x
    Compression achieved:       ~20% of theoretical maximum
    Annual savings:             $30-50 billion
```

### Where Compression Is Already Underway

- **Stablecoins** — Replacing correspondent banking for cross-border
  payments. 7 MESTs compressed to 2. $27.6T transfer volume in 2024.
  Fortune 500 firms report 71% cost reductions.

- **Tokenized securities** — BlackRock BUIDL ($2.9B AUM) demonstrates
  compressed custody and settlement: subscription is 2 MESTs (not 5),
  dividends are 1 MEST (not 5), operating 24/7/365.

- **DEX trading** — Atomic swap settles trade + custody in one operation.
  2-3 MESTs vs. 10 for traditional exchange + CCP + CSD chain.

- **Real-time payments** — UPI and Pix prove consumer appetite for faster,
  cheaper rails — the same appetite DLT serves. UPI compresses cost
  without compressing MESTs; DLT compresses both.

### Honest Caveats

- CEX compression (4x) is **centralization**, not innovation — Binance is the
  clearing house, custodian, and settlement system combined
- Regulation will add 1-2 MESTs to crypto over the next decade (MiCA, 1099-DA)
- Smart contract risk replaces reconciliation risk — a genuine trade-off
- Not all MESTs are waste: post-2008 reporting MESTs are the solution to
  systemic opacity

---

## 6. Country Spotlights

### India — 17.4% of Global TPS on 3.5% of GDP

India is the most disproportionate contributor to global financial TPS:

- **UPI**: 172 billion transactions/year (2025), #1 real-time payment system
  globally. Zero merchant fees since 2020.
- **NSE**: #1 stock exchange by trade count (28% of global equity volume).
  India's options market alone generates more trades than NYSE + NASDAQ combined.
- **RuPay**: Growing domestic card network displacing Visa/Mastercard share.
- **JAM trinity**: Jan Dhan (520M accounts) + Aadhaar + Mobile enabled
  7.4 billion government benefit transfers.

India's financial system is digitally native in a way that most developed
economies are not — it leapfrogged cards directly to real-time bank transfers.

### EU — 18.2% of Global TPS

The EU is the second-largest contributor by regional share:

- **SEPA**: Unified payment area processing cards + bank transfers across
  27 member states.
- **TIPS**: TARGET Instant Payment Settlement grew +402% year-over-year —
  the fastest-growing RTGS system globally.
- **MiCA**: First comprehensive crypto regulation (effective 2024-2025),
  adding regulatory MESTs to European crypto transactions.
- **T2 consolidation**: Merged TARGET2 and T2S into a single platform,
  reducing intra-EU settlement friction.

### China — The +/- 6,000 TPS Blind Spot

China is the largest single-country uncertainty in the Big Number:

- **Alipay + WeChat Pay**: Combined ~40 billion transactions/year, but
  detailed breakdowns are corporate-confidential.
- **CNAPS-HVPS**: China's high-value payment system processes more than
  Fedwire, but English-language data is scarce.
- **Opacity range**: China could contribute 8,000-14,000 TPS depending on
  wallet volume assumptions — a +/- 6,000 TPS uncertainty band.

We use PBOC aggregate data as the primary source, cross-checked against
corporate disclosures and UnionPay filings.

### USA — TradFi Dominant

The US contributes disproportionately to Traditional Finance TPS:

- **CME + CBOE**: Dominant in derivatives (futures + options).
- **NYSE + NASDAQ**: Combined ~40% of global equity value traded.
- **Fedwire + CHIPS**: High-value payment systems processing $5T+/day.
- **Card-heavy payments**: The US is one of the most card-dependent
  economies, with slower real-time payment adoption (FedNow launched 2023
  but still low volume).

### Brazil — Pix #2 Globally, 6.3% of Global TPS

- **Pix**: Launched November 2020, now processing 6.3 billion transactions/month
  (2025) — #2 real-time payment system after UPI.
- **Dramatic growth**: From zero to ~2,400 TPS in four years.
- **Financial inclusion**: Pix brought 70 million previously unbanked
  Brazilians into the digital payment system.

---

## 7. Time-Series Highlights

### A Decade of Growth: 2015-2025

```
    Global Gross TPS (all 29 categories)

    2025  ████████████████████████████████████████████████░  86,900
    2024  ██████████████████████████████████████████░        75,200
    2023  ████████████████████████████████████░              62,400
    2022  ███████████████████████████████░                   54,100
    2021  ████████████████████████████░                      48,900
    2020  ██████████████████████░                            38,200
    2019  █████████████████░                                 29,400
    2018  ██████████████░                                    24,600
    2017  ████████████░                                      20,700
    2016  ██████████░                                        17,100
    2015  ████████░                                          12,900

    6.7x growth in a decade
```

### Fastest Growers (2020-2025 CAGR)

| # | Category | CAGR | 2020 TPS | 2025 TPS | Multiplier |
|---|----------|------|----------|----------|------------|
| 1 | RWA Tokenisation | 119% | 0.05 | 2.4 | 48x |
| 2 | Stablecoins | 103% | 20 | 700 | 35x |
| 3 | L1/L2 Blockchain | 77% | 63 | 1,100 | 17.5x |
| 4 | DeFi | 54% | 15 | 130 | 8.7x |
| 5 | ETD (Derivatives) | 45% | 1,483 | 9,505 | 6.4x |

The top 3 fastest-growing categories are all blockchain-native. But the top 3
by **absolute TPS added** are consumer cards (+14,651), digital wallets
(+16,170), and bank transfers (+14,189) — traditional infrastructure is
still adding more raw throughput per year.

### The MEST Multiplier Is Rising

The global MEST multiplier has risen from ~6.8x (2015) toward ~7.4x (2025).
This is not inefficiency — it reflects:

- Post-2008 regulatory reporting (trade repositories, EMIR, Dodd-Frank)
- Embedded finance adding intermediary layers (BNPL, wallets-on-cards)
- Higher share of derivatives (which have 10-12x multipliers) in the mix

The multiplier will continue rising absent DLT compression. Projected: 7.8-8.2x
by 2030 on the current trajectory.

---

## 8. Limitations and Blind Spots

### What We Do Not Know

| Blind Spot | Impact | Confidence |
|-----------|--------|------------|
| China wallet volumes | +/- 6,000 TPS | Low |
| Informal remittances (30-50% of total) | +/- 500 TPS | Low |
| CEX wash trading (blended ~20.6%) | +/- 660 TPS | Medium |
| Cash transactions (untracked) | Unknown | N/A |
| Private blockchain / enterprise DLT | Unknown | N/A |
| OTC derivative transaction counts | +/- 50% | Medium |

### Structural Limitations

- **Transaction vs. value**: TPS counts treat a $2 coffee and a $500M repo
  identically. The Big Number measures throughput, not economic significance.
- **Cash is invisible**: Cash transactions are the largest blind spot. ATM
  withdrawals (1,557 TPS) are the only cash-adjacent measure we capture.
- **MEST multipliers are estimates**: Per-category multipliers are
  order-of-magnitude assessments based on transaction lifecycle analysis,
  not instrumented measurements.
- **Point-in-time**: All figures are 2025 estimates. Financial TPS is growing
  ~20% annually, so these numbers age quickly.

### Confidence Gaps

Six categories score below 52 on our confidence scale (out of 100):

| Category | Score | Primary Gap |
|----------|-------|------------|
| AI Agent Transactions | 34 | Pre-market; projections, not measurements |
| Payroll Payments | 35 | No single source counts global payroll txns |
| In-Game Microtransactions | 44 | Publishers report revenue, not txn counts |
| Bill Payments | 48 | Bottom-up model with significant assumptions |
| Tax & Government Payments | 50 | Difficult to aggregate across jurisdictions |
| ATM Withdrawals | 52 | Emerging market data is sparse |

These six categories contribute ~6,500 gross TPS (~7% of total). Their
uncertainty does not materially affect the Big Number but does limit
granular analysis.

---

## 9. Appendix

### Full Analyses

| Document | Description |
|----------|-------------|
| [Research Index](README.md) | Master index of all 29 categories |
| [MEST Framework](MEST.md) | Full MEST definition, taxonomy, per-category cascades |
| [MEST Advantage](MEST_ADVANTAGE.md) | DLT compression thesis with cost modeling |
| [Overlap Matrix](OVERLAP_MATRIX.md) | Cross-sector de-duplication methodology |
| [Confidence Scorecard](CONFIDENCE_SCORECARD.md) | 0-100 scores for all categories |
| [Peak TPS Analysis](PEAK_TPS.md) | When does global infrastructure max out? |
| [Scenario Analysis](SCENARIOS.md) | Recession, pandemic, crypto winter stress tests |
| [Time-Series](timeseries/TIMESERIES.md) | 2015-2025 annual data for all categories |
| [Sunset Watch](SUNSET_WATCH.md) | Declining categories (growth outpaces decline 38:1) |

### Country Deep Dives

| Country | Key Finding |
|---------|------------|
| [India](deep-dives/india/REPORT.md) | 17.4% of global TPS on 3.5% of GDP |
| [China](deep-dives/china/REPORT.md) | The +/- 6,000 TPS opacity problem |
| [USA](deep-dives/usa/REPORT.md) | TradFi dominance, card-heavy payments |
| [Brazil](deep-dives/brazil/REPORT.md) | Pix: zero to #2 globally in 4 years |
| [EU](deep-dives/eu/REPORT.md) | 18.2% of global TPS, TIPS +402% YoY |

### SLE Framework

Research is guided by 17 **Soul Less Employee** personas — expert
archetypes grounded in real job descriptions from Visa, BIS, Chainalysis,
DTCC, BNY Mellon, Gartner, and others. Each persona brings domain-specific
mental models, data sources, and documented biases. See
[RECRUITER.md](../souls/RECRUITER.md) for the full dispatch matrix.

### Data Sources (Selected)

- Nilson Report (consumer cards) — gold standard for payment card data
- BIS CPMI Red Book (bank transfers, RTGS) — central bank statistics
- FIA Annual Survey (exchange-traded derivatives) — comprehensive ETD volumes
- World Federation of Exchanges (equities) — global exchange data
- PBOC Aggregate Statistics (China payments) — official Chinese payment data
- NPCI (India UPI, RuPay) — Indian payment infrastructure data
- BCB / Pix Statistics (Brazil) — Brazilian real-time payment data
- ECB Payment Statistics (EU) — European payment data
- McKinsey Global Payments Report ($2.5T industry revenue)
- Visa OnChain Analytics (stablecoin transfer volumes)

### Methodology Framework

- **Triangulation-first**: Every category requires 2-3 independent sources
- **Bottom-up AND top-down**: Build from components, validate against totals
- **Explicit confidence**: Every number has a 0-100 confidence score
- **De-duplication by design**: Overlap matrix maintained alongside capsules
- **Time-series**: 10-year history (2015-2025) for all categories
- **Stress-tested**: Recession, pandemic, and crypto winter scenarios modeled

---

## How to Cite

> Universe of Finance Project. "Global Financial Transaction Throughput:
> ~73,750 TPS and ~545,000 MEST/s." Research brief, March 2026.
> Available at: [universe-of-finance repository]

---

*Research outputs: CC BY 4.0. Code: MIT.*
*Produced across 10 research runs, March 2026.*

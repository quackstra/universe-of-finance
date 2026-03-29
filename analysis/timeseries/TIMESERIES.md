---
title: "TPS Time Series"
parent: MEST Framework
grand_parent: Explore
nav_order: 2
---

# Universe of Finance — Time-Series 2015-2025

> Annual average TPS and transaction counts for all 24 categories, compiled from
> per-category capsule data with gap-filling via interpolation and back-extrapolation.

**Generated**: 2026-03-28
**Data source**: Per-category `data.json` files from Run 1-4 capsules
**Methodology**: Extract historic arrays, fill gaps with sector growth rates, derive TPS from `annual_volume / 31,536,000`

---

## Summary Table: All 24 Categories

| # | Category | Sector | 2015 TPS | 2020 TPS | 2025 TPS | CAGR 15-25 | CAGR 20-25 | Confidence |
|---|----------|--------|----------|----------|----------|------------|------------|------------|
| 1 | Consumer Cards | Payments | 7,197 | 12,049 | 26,700 | 14.0% | 17.2% | 91 |
| 2 | Digital Wallets | Payments | 1,200 | 6,980 | 23,150 | 34.4% | 27.1% | 67 |
| 3 | Bank Transfers (RTP) | Payments | 500 | 3,330 | 17,519 | 42.3% | 39.5% | 78 |
| 4 | E-Commerce | Payments | 614 | 1,282 | 1,907 | 12.4% | 9.0% | 67 |
| 5 | IoT/M2M | Emerging | 400 | 900 | 1,538 | 14.4% | 11.3% | 67 |
| 6 | Government Payments | Government | 700 | 900 | 1,002 | 3.6% | 2.2% | 50 |
| 7 | Equity Markets | Trad Finance | 1,427 | 1,649 | 2,067 | 3.8% | 4.6% | 86 |
| 8 | ETD (Futures/Options) | Trad Finance | 786 | 1,483 | 9,505 | 28.3% | 45.0% | 88 |
| 9 | CEX (Crypto) | Digital Assets | 30 | 600 | 3,500 | 59.8% | 42.1% | 56 |
| 10 | L1/L2 Blockchain | Digital Assets | 7 | 63 | 1,100 | 64.0% | 77.2% | 76 |
| 11 | Stablecoins | Digital Assets | ~0 | 20 | 700 | n/a | 103.0% | 75 |
| 12 | Gaming Microtx | Gaming | 200 | 397 | 415 | 7.6% | 0.9% | 44 |
| 13 | P2P Transfers | Payments | 20 | 124 | 301 | 31.2% | 19.5% | 69 |
| 14 | Commodities | Trad Finance | 110 | 174 | 240 | 7.9% | 6.4% | 74 |
| 15 | DeFi | Digital Assets | 0 | 15 | 130 | n/a | 54.2% | 62 |
| 16 | Gaming Sales | Gaming | 40 | 72 | 97 | 9.3% | 6.1% | 56 |
| 17 | Remittances | Payments | 30 | 43 | 61 | 7.4% | 7.4% | 58 |
| 18 | Securities Settlement | Banking | 5.5 | 8.4 | 46.6 | 23.7% | 40.8% | 74 |
| 19 | FX (Institutional) | Trad Finance | 25 | 34 | 42 | 4.4% | 2.6% | 58 |
| 20 | Interbank RTGS | Banking | 7.5 | 10.0 | 13.8 | 6.3% | 6.8% | 82 |
| 21 | Fixed Income | Trad Finance | 2.5 | 3.1 | 3.8 | 4.1% | 4.1% | 60 |
| 22 | RWA Tokenisation | Emerging | 0 | 0.05 | 2.4 | n/a | 119.2% | 56 |
| 23 | AI Agents | Emerging | 0 | 0 | 0.66 | n/a | n/a | 34 |
| 24 | OTC Derivatives | Trad Finance | 0.11 | 0.13 | 0.16 | 3.6% | 4.0% | 68 |

---

## Growth Leaderboard: Fastest-Growing Categories (CAGR 2020-2025)

| Rank | Category | CAGR 2020-25 | 2020 TPS | 2025 TPS | Multiplier |
|------|----------|-------------|----------|----------|------------|
| 1 | RWA Tokenisation | 119.2% | 0.05 | 2.4 | 48x |
| 2 | Stablecoins | 103.0% | 20 | 700 | 35x |
| 3 | L1/L2 Blockchain | 77.2% | 63 | 1,100 | 17.5x |
| 4 | DeFi | 54.2% | 15 | 130 | 8.7x |
| 5 | ETD (Futures/Options) | 45.0% | 1,483 | 9,505 | 6.4x |
| 6 | CEX (Crypto) | 42.1% | 600 | 3,500 | 5.8x |
| 7 | Securities Settlement | 40.8% | 8.4 | 46.6 | 5.5x |
| 8 | Bank Transfers (RTP) | 39.5% | 3,330 | 17,519 | 5.3x |
| 9 | Digital Wallets | 27.1% | 6,980 | 23,150 | 3.3x |
| 10 | P2P Transfers | 19.5% | 124 | 301 | 2.4x |

**Key insight**: The top 3 fastest-growing categories are all blockchain-native. But the top 3 by *absolute TPS added* are consumer cards (+14,651), bank transfers (+14,189), and digital wallets (+16,170) -- the traditional payments infrastructure is still adding more raw throughput.

---

## Decline Watch: Shrinking or Stagnant Categories

| Category | CAGR 2020-25 | Pattern | Explanation |
|----------|-------------|---------|-------------|
| Gaming Microtx | 0.9% | Stagnant | Post-COVID normalization; 2020 was a COVID-inflated peak. Revenue growing but ATV rising faster than txn count |
| Government Payments | 2.2% | Slow growth | Population growth + digitization vs. consolidation of payment batches |
| FX (Institutional) | 2.6% | Slow growth | Mature market; daily value grows faster than trade count |
| Remittances | 7.4% | Steady | Digital corridors growing but informal channels shrinking offsets |

No category is in outright decline over 2020-2025, though equity markets dipped 2021-2023 before recovering in 2024.

---

## Regime Changes: Non-Linear Growth Patterns

### 1. Exchange-Traded Derivatives: The India Options Hockey Stick
- **2015-2019**: Flat (~25B contracts/year, ~800-1100 TPS)
- **2020-2022**: Steady climb to 84B (COVID volatility + retail access)
- **2023-2025**: Explosive to 205-300B (NSE zero-day options, India retail explosion)
- **Regime change**: India went from ~10% of global ETD to ~60%+ in 5 years

### 2. Crypto Cycles: Boom-Bust-Boom
- **CEX**: 2017 spike (ICO), 2018 crash, 2021 supercycle, 2022 crash, 2024 recovery
- **DeFi**: Zero until 2020 "DeFi Summer", peaked 2021, crashed 2022, recovering 2024-25
- **Stablecoins**: Near-exponential through all cycles -- stablecoins grew even during crypto bear markets

### 3. Real-Time Payments: UPI/PIX Hockey Stick
- **Bank Transfers (RTP)**: 50B txns (2018) -> 553B (2025 est.), driven by:
  - UPI: 2.7B (2017) -> 172B (2024) -- **64x in 7 years**
  - PIX: 0 (pre-2020) -> 66B (2024) -- **zero to 66B in 4 years**
  - These two systems alone account for ~62% of global RTP volume

### 4. COVID Impact (2020)
| Category | Impact | Mechanism |
|----------|--------|-----------|
| Consumer Cards | -4.5% dip | Travel/dining collapse |
| E-Commerce | +21% surge | Physical-to-digital shift |
| Equity Markets | +37% surge | Retail trading boom (Robinhood/GameStop precursor) |
| ETD | +36% surge | Volatility drove hedging demand |
| Gaming Microtx | +22% surge | Lockdown gaming |
| Gaming Sales | +33% surge | Digital download acceleration |
| P2P Transfers | +44% surge | Stimulus redistribution |
| Government Payments | +10% surge | Stimulus disbursements |
| Bank Transfers (RTP) | +40% growth | Accelerated digital adoption |
| IoT/M2M | -5% dip | Toll collection decline |
| Remittances | +4% | Resilient -- migrant workers kept sending |

### 5. L1/L2 Blockchain: Solana Effect (2024)
- 2023: 8B txns (254 TPS)
- 2024: 27B txns (856 TPS) -- **3.4x in one year**
- Driven by Solana going from ~30M to ~60M daily transactions (raw, pre-filter)
- L2 rollups (Base, Arbitrum, Optimism) collectively added billions more

---

## The Big Number: Estimated Global Financial TPS Over Time

| Year | Gross TPS (all categories) | Dedup Factor | Est. Net TPS | Annual Txns (gross) |
|------|---------------------------|-------------|-------------|---------------------|
| 2015 | ~12,900 | 0.82 | ~10,600 | ~407B |
| 2018 | ~18,400 | 0.82 | ~15,100 | ~582B |
| 2020 | ~29,400 | 0.80 | ~23,500 | ~928B |
| 2022 | ~50,700 | 0.78 | ~39,500 | ~1,597B |
| 2025 | ~86,900 | 0.75 | ~65,200 | ~2,741B |

**10-year story**: Global financial TPS grew ~6.7x from 2015 to 2025 (gross) or ~6.2x after deduplication. The world added more transaction capacity in the last 5 years (2020-2025: +57,500 gross TPS) than existed in total in 2018.

### Dedup Factor Explanation
The dedup factor decreases over time because overlay layers (digital wallets on card rails, UPI counted in both wallets and bank transfers, e-commerce settled on cards) are growing faster than unique-count categories. See `OVERLAP_MATRIX.md` for detailed dedup rules.

---

## Concentration Analysis

### Top 5 Categories by TPS (2025)

| Rank | Category | TPS | Share of Gross |
|------|----------|-----|---------------|
| 1 | Consumer Cards | 26,700 | 30.7% |
| 2 | Digital Wallets | 23,150 | 26.6% |
| 3 | Bank Transfers (RTP) | 17,519 | 20.2% |
| 4 | ETD | 9,505 | 10.9% |
| 5 | CEX (Crypto) | 3,500 | 4.0% |
| | **Top 5 total** | **80,374** | **92.5%** |

The top 3 payments categories account for 77.5% of all global financial TPS. Traditional finance (equity, bonds, FX, commodities, derivatives) contributes surprisingly little by transaction count -- massive by value, modest by frequency.

### Top 5 Categories by TPS (2015)

| Rank | Category | TPS | Share of Gross |
|------|----------|-----|---------------|
| 1 | Consumer Cards | 7,197 | 55.7% |
| 2 | Equity Markets | 1,427 | 11.0% |
| 3 | Digital Wallets | 1,200 | 9.3% |
| 4 | ETD | 786 | 6.1% |
| 5 | Government Payments | 700 | 5.4% |
| | **Top 5 total** | **11,310** | **87.6%** |

**Shift 2015->2025**: Consumer cards went from 56% to 31% share -- not because cards shrank, but because digital wallets and real-time payments exploded. The "big three" of 2025 (cards, wallets, RTP) barely existed as a trio in 2015.

---

## Data Quality Notes

### High-Confidence Categories (score >= 80)
- Consumer Cards (91) -- Nilson Report gold standard
- ETD (88) -- FIA annual survey
- Equity Markets (86) -- WFE data
- Interbank RTGS (82) -- Central bank statistics

### Low-Confidence Categories (score <= 50)
- AI Agents (34) -- Pre-market, all projections
- Gaming Microtx (44) -- Revenue-derived, no published counts
- Government Payments (50) -- Counts never published, model-estimated

### Methodological Caveats
1. **2025 values are estimates**: Most capsules have 2024 as latest actual data. 2025 uses baseline projections.
2. **Back-extrapolation quality varies**: 2015-2017 data for many categories is interpolated.
3. **Crypto volatility**: CEX/DeFi/Stablecoin figures swing wildly year-to-year. Single-year comparisons are misleading.
4. **Securities settlement methodological break**: Historic (2015-2024) covers Euroclear only; 2025 includes all CSDs.
5. **Interbank RTGS coverage expansion**: Historic covers 3 systems; current covers 13. Not directly comparable.

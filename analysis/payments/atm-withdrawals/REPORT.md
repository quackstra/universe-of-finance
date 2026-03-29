---
title: "ATM Withdrawals — Report"
parent: Payments
grand_parent: Explore
nav_order: 11
---

# ATM Withdrawals — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Global ATM cash withdrawals totaled an estimated **~49.1 billion transactions** in 2024, equivalent to an average of **~1,557 TPS**, dispensing approximately **$7.7 trillion** in cash annually. This represents a **declining category** — down from a peak of ~63 billion in 2016-2017, a drop of ~22% over 8 years. The decline is driven by digital payment adoption in developed markets (contactless cards, mobile wallets) and the explosive growth of real-time payment systems (UPI, PIX) in emerging markets. However, the decline is uneven: developed markets (US, EU, Japan) are seeing 5-10% annual drops, while Africa and parts of South/Southeast Asia still show growth as ATM networks expand for financial inclusion.

**ATM withdrawals have zero overlap with other payment categories.** They are cash-out events — the ATM transaction converts bank balance to physical cash. The subsequent spending of that cash is untraceable and uncounted in any electronic payment category.

## Scope

This analysis covers:
- **Cash withdrawals at ATMs** (bank-owned and independent deployers)
- **All card types**: debit, credit, prepaid cards used for cash withdrawal
- **On-us and off-us transactions**: both own-bank and foreign ATM withdrawals

Excluded: balance inquiries (~20% of ATM interactions), mini-statements, bill payments via ATM (counted in bill payments), deposits at ATMs, cardless ATM withdrawals (small but growing).

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~1,557 | Derived from 49.1B annual | 🟡 Medium |
| Peak TPS (est.) | ~3,114 | Estimated at 2.0x average (holiday weekends) | 🔴 Low |
| Daily volume | ~134.5 million | Derived from annual total | 🟡 Medium |
| Annual volume (2024) | ~49.1 billion | BIS/ECB/RBI/ATMIA composite ([calculations](workings/calculations.md)) | 🟡 Medium |
| Annual value (2024) | ~$7.7 trillion | Volume × avg withdrawal value | 🟡 Medium |
| Avg withdrawal value | ~$157 | Weighted global average (US $198, EU ~$140, India ~$40) | 🟡 Medium |

### Regional Breakdown (2024)

| Region | ATMs (thousands) | Est. Withdrawals (B) | YoY Change | Share | Avg Withdrawal |
|--------|-----------------|---------------------|------------|-------|----------------|
| **Asia-Pacific** | ~1,500 | ~22.0 | -4% | 44.8% | ~$80 |
| — China | ~700 | ~12.0 | -8% | 24.4% | ~$90 |
| — India | ~215 | ~6.0 | -5% | 12.2% | ~$40 |
| — Japan | ~180 | ~2.5 | -3% | 5.1% | ~$200 |
| — Rest of APAC | ~405 | ~1.5 | +3% | 3.1% | ~$60 |
| **Europe** | ~400 | ~10.0 | -4% | 20.4% | ~$140 |
| — EU-27 | ~266 | ~7.5 | -4% | 15.3% | ~$145 |
| — UK | ~50 | ~1.5 | -6% | 3.1% | ~$120 |
| — Rest of Europe | ~84 | ~1.0 | -2% | 2.0% | ~$100 |
| **North America** | ~500 | ~8.0 | -6% | 16.3% | ~$198 |
| — US | ~470 | ~7.5 | -6% | 15.3% | ~$198 |
| — Canada | ~30 | ~0.5 | -5% | 1.0% | ~$150 |
| **Latin America** | ~350 | ~5.0 | -2% | 10.2% | ~$80 |
| **Middle East & Africa** | ~250 | ~3.1 | +5% | 6.3% | ~$60 |
| **Other** | ~120 | ~1.0 | 0% | 2.0% | ~$80 |
| **GLOBAL TOTAL** | **~3,120** | **~49.1** | **-3%** | **100%** | **~$157** |

### Key Regional Dynamics

**China's collapse**: China had 1.1M ATMs in 2018, now ~700K. ATM withdrawals down ~40% since 2018 as Alipay and WeChat Pay dominate. PBOC data shows continued acceleration of decline.

**India's paradox**: Despite UPI processing 172B transactions, ATM withdrawals remain high (~6B/year) and monthly cash withdrawal values still grew 5.5% in FY2024. Cash demand is sticky for rural and small-ticket transactions. However, transaction *counts* are declining — people make fewer but larger withdrawals.

**Africa's growth**: The only region with growing ATM deployment. Financial inclusion initiatives (Nigeria NIP, Egypt digital banking) are driving ATM expansion even as mobile money grows alongside.

**US decline**: Federal Reserve data shows US ATM withdrawals fell from 5.1B (2018) to 3.7B (2021) — a 10.1% annual decline rate. Extrapolating at a moderated 6% annual decline gives ~2.5B for 2024. However, total US ATM transactions (including balance inquiries and non-withdrawal) remain higher.

---

## Historic Trend

| Year | Annual Withdrawals (B) | ATMs Worldwide (M) | Avg TPS | Txns/ATM/Year | Notes |
|------|----------------------|---------------------|---------|--------------|-------|
| 2015 | ~62 | 3.40 | 1,965 | 18,235 | Near-peak; pre-digital wallet era |
| 2016 | ~63 | 3.40 | 1,997 | 18,529 | Peak year; ATMIA reported 6% withdrawal growth |
| 2017 | ~62 | 3.37 | 1,965 | 18,398 | Plateau; China ATMs peak at 1.1M |
| 2018 | ~60 | 3.30 | 1,902 | 18,182 | Decline begins; India demonetization aftershock |
| 2019 | ~57 | 3.25 | 1,807 | 17,538 | Steady decline; contactless payments grow |
| 2020 | ~42 | 3.20 | 1,331 | 13,125 | COVID devastation — lockdowns crushed ATM usage |
| 2021 | ~46 | 3.15 | 1,458 | 14,603 | Partial recovery |
| 2022 | ~50 | 3.10 | 1,585 | 16,129 | Near-recovery in emerging markets |
| 2023 | ~51 | 3.24 | 1,617 | 15,741 | Post-COVID plateau; value per withdrawal rising |
| 2024 | ~49.1 | 3.12 | 1,557 | 15,737 | Resume decline; -3% YoY |

### Growth Rate Analysis

```
Peak to current: (49.1/63)^(1/8) - 1 = -3.0% CAGR (2016-2024)
Pre-COVID trend: (57/63)^(1/3) - 1 = -3.3% CAGR (2016-2019)
COVID-adjusted: (49.1/60)^(1/6) - 1 = -3.3% CAGR (2018-2024)
```

The pre-COVID trend and post-COVID reality have converged at roughly **-3% to -3.5% CAGR**. COVID did not permanently alter the trajectory — it accelerated the decline temporarily, but the recovery brought volumes back to the pre-existing decline trendline.

---

## Projections

### Baseline (-4% CAGR — Steady Digital Displacement)

Cash usage continues declining at current rates. ATM networks consolidate in developed markets, grow modestly in Africa/South Asia.

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,434 | 45.3 |
| 2028 | 1,322 | 41.7 |
| 2030 | 1,218 | 38.4 |
| 2035 | 994 | 31.4 |

### Slow Decline (-2% CAGR — Cash Resilience)

Cash proves stickier than expected. Privacy concerns, unbanked populations, and rural demand sustain ATM usage. Emerging market growth partially offsets developed market decline.

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,507 | 47.6 |
| 2030 | 1,411 | 44.5 |
| 2035 | 1,300 | 41.0 |

### Accelerated Decline (-7.5% CAGR — Digital Cash Replacement)

CBDCs launch in major markets, UPI/PIX expand to 20+ countries, contactless payment ubiquity reaches rural areas. ATM withdrawal volume halves by 2035.

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,335 | 42.1 |
| 2030 | 980 | 30.9 |
| 2035 | 666 | 21.0 |

---

## Key Findings

1. **ATM withdrawals are a declining but still massive category.** At ~49B annual transactions and ~$7.7T in cash dispensed, ATMs remain a critical cash-access infrastructure even as digital payments surge.

2. **Zero overlap with other payment categories.** This is one of the cleanest categories in the taxonomy — an ATM withdrawal is a cash-out event, not a payment. It does not appear in card purchase statistics, wallet transactions, or bank transfer counts.

3. **China is driving the global decline.** China's ATM withdrawal volume has fallen ~40% since 2018, accounting for more than half of the global decline. The Alipay/WeChat Pay ecosystem has effectively replaced cash for urban transactions.

4. **Value per withdrawal is rising as volume falls.** Average withdrawal amounts are increasing 3-5% annually as consumers make fewer but larger ATM visits. This is consistent across all regions and suggests ATMs are shifting from daily convenience to periodic cash-stocking behavior.

5. **The peak was 2016-2017 at ~63 billion withdrawals.** The industry will likely never return to peak volumes. Even in the most optimistic (slow-decline) scenario, 2035 volume (41B) is 35% below peak.

6. **Africa is the last growth frontier.** Financial inclusion programs in Egypt, Nigeria, and East Africa are driving ATM deployment growth. Africa may not peak until 2028-2030 as mobile money and ATMs coexist rather than substitute.

7. **ATM infrastructure costs are rising per transaction.** With declining volumes but fixed maintenance costs, the per-transaction cost of ATM networks is increasing. This creates a potential tipping point where networks become uneconomic in low-usage areas, accelerating closures and further reducing access.

---

## Relationship to Consumer Cards

ATM withdrawals use card rails for **authentication** (card + PIN) but are categorically different from card **payments**:

- **Card network statistics**: Visa and Mastercard include ATM cash advances in total volume by *value* (~$7.4T of Nilson's $51.9T total) but typically report purchase transaction *counts* separately from cash withdrawal counts
- **Consumer cards capsule**: The 772.73B figure in our consumer cards capsule includes "purchase + cash" in value but the transaction count is purchase-focused. ATM withdrawals add ~49B to the broader "card-initiated transaction" count
- **De-duplication**: No de-duplication needed. ATM withdrawals and card purchases are distinct transaction types on the same network infrastructure

---

## Data Quality & Limitations

- **BIS Red Book coverage**: BIS CPMI statistics cover ~25 major economies. ATM data for smaller developing markets is estimated.
- **ECB data is strong for EU**: ECB publishes half-yearly ATM statistics with transaction counts. H1 2024 and H2 2024 data both available.
- **US data is stale**: The Federal Reserve Payments Study is triennial — latest detailed ATM data is 2021 (3.7B withdrawals). 2024 is extrapolated.
- **India RBI data is monthly**: RBI publishes monthly ATM transaction counts (e.g., 48.83 crore withdrawals in January 2025). However, converting crore to annual totals requires 12-month aggregation.
- **China PBOC aggregation**: PBOC reports total "consumer payment transactions" but does not cleanly separate ATM withdrawals from other card transactions.
- **Withdrawal vs. total ATM transactions**: The 86.7B "global ATM transactions" figure includes balance inquiries, mini-statements, and deposits. Cash withdrawals are ~57-60% of total ATM interactions, giving the ~49.1B figure used here.
- **Independent ATM deployers**: Bank-owned ATM data is well-tracked; independent deployer (IAD) transaction data is murkier. IADs represent ~40% of US ATMs.

---

## Sources

1. [BIS — CPMI Retail Payment Statistics](https://data.bis.org/topics/CPMI_CT)
2. [ECB — Payments Statistics: H2 2024](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h2~5ada0087d2.en.html)
3. [ECB — Payments Statistics: H1 2024](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h1~5263055ced.en.html)
4. [RBI — Bankwise ATM/POS/Card Statistics](https://rbi.org.in/scripts/atmview.aspx)
5. [Federal Reserve — Payments Study 2022 Triennial](https://www.federalreserve.gov/paymentsystems/2023-April-The-Federal-Reserve-Payments-Study.htm)
6. [ATMIA — Industry Reports](https://www.atmia.com/)
7. [Datos Insights — ATM Industry Trends A-Z Guide](https://datos-insights.com/blog/atm-industry-trends-a-z-guide-global-market-evolution/)
8. [ATM Marketplace — Cash Withdrawal Volume Statistics](https://www.atmmarketplace.com/news/atm-cash-withdrawal-volume-grows-6-percent-in-2016/)
9. [BIS — Tap, Click and Pay (Feb 2024)](https://www.bis.org/statistics/payment_stats/commentary2402.pdf)
10. [Sci-Tech Today — ATM Statistics 2025](https://www.sci-tech-today.com/stats/atm-statistics-updated/)
11. [World Bank — ATMs per 100,000 Adults](https://data.worldbank.org/indicator/FB.ATM.TOTL.P5)

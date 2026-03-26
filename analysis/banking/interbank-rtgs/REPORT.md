# Interbank Settlement (RTGS) — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

**Category**: Banking > Interbank Settlement (RTGS)
**Data Year**: 2024
**Last Updated**: 2026-03-26

---

## Executive Summary

Global Real-Time Gross Settlement (RTGS) systems processed an estimated **423 million transactions** in 2024, averaging **~13.4 TPS** (calendar) or **~6.7 TPS** (business-day adjusted). These are high-value, low-count systems: Fedwire alone moves **~$4.5 trillion per day** but only ~836,000 transactions. The total annual value across the five major RTGS systems and CLS exceeded **$2,100 trillion** — making this the single highest-value transaction category in global finance.

The paradox of RTGS is that it underpins the entire financial system while processing fewer transactions per second than a single mid-size e-commerce website. Each transaction represents an average of **$5–6 million** (Fedwire) to **tens of millions** (TARGET2/T2). Growth in transaction counts is modest (2–4% CAGR) because these systems are designed for final settlement of wholesale obligations, not retail throughput.

---

## Scope

**Included:**
- Fedwire Funds Service (US)
- TARGET2/T2 (Eurozone, migrated to T2 consolidated platform March 2023)
- CHAPS (UK)
- BOJ-NET Funds Transfer System (Japan)
- CLS (global FX settlement via payment-versus-payment)

**Excluded:**
- Retail fast payment systems (UPI, PIX, FedNow, TIPS) — covered under Bank Transfers
- Securities settlement legs (Fedwire Securities, TARGET2-Securities) — covered under Securities Settlement
- SWIFT messaging (messaging layer, not settlement)
- Correspondent banking flows (use RTGS as final leg but are counted at the RTGS level)

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS (calendar) | ~13.4 | Calculated: 423M / 31.56M sec | 🟡 Medium |
| Average TPS (business-day) | ~6.7 | Calculated: 423M / (250 × 8h × 3600) | 🟡 Medium |
| Peak TPS (est.) | ~30–40 | Peak-day concurrent across time zones | 🔴 Low |
| Daily volume (avg) | ~1.69M | Sum of system averages | 🟡 Medium |
| Annual volume (2024) | ~423M transactions | Aggregated from system reports | 🟡 Medium |
| Annual value (2024) | ~$2,150 trillion | Aggregated, EUR/GBP/JPY converted at avg 2024 rates | 🟡 Medium |

**Note on TPS calculation**: RTGS systems operate only on business days (~250/year) and typically within defined operating windows (6–18 hours). The "calendar TPS" of 13.4 understates burst activity; business-day TPS during operating hours is more meaningful but still modest at ~6.7 TPS because these are wholesale systems.

### System-by-System Breakdown

| System | Country | Annual Volume (M) | Annual Value | Avg Daily Volume | Avg Txn Value | Source | Confidence |
|--------|---------|-------------------|-------------|-----------------|---------------|--------|------------|
| **Fedwire Funds** | US | ~210 | ~$1,133T | ~836,000 | ~$5.4M | [FRB Services](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) | 🟢 High |
| **T2 (ex-TARGET2)** | Eurozone | ~108 | ~€555T (~$605T) | ~424,000 | ~€5.6M | [ECB T2 Facts](https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html) | 🟢 High |
| **CHAPS** | UK | ~53 | ~£87.5T (~$111T) | ~208,000 | ~£1.7M | [Bank of England](https://www.bankofengland.co.uk/payment-and-settlement/payment-and-settlement-statistics) | 🟢 High |
| **BOJ-NET** | Japan | ~5 | ~¥18,250T (~$122T) | ~19,000 | ~¥3.8B | [BOJ Statistics](https://www.boj.or.jp/en/statistics/set/kess/index.htm) | 🟡 Medium |
| **CLS** | Global (FX) | ~250 (est.) | ~$1,750T (est.) | ~1,000,000 | ~$7M | [CLS Group](https://www.cls-group.com/about/annual-report-2024/annual-report-2024/) | 🟡 Medium |

**CLS note**: CLS settles FX obligations via payment-versus-payment. Average daily value is ~$7 trillion across 18 currencies. The record single-day settlement was $19.1 trillion (20 June 2024). Transaction count is estimated from the record day of 3.2 million trades (July 2022) and average daily value ratios. CLS's multilateral netting reduces actual funding to ~1% of gross value ($72B for the $19.1T record day).

**BOJ-NET note**: Specific 2024 transaction counts are derived from BOJ's published Payment and Settlement Statistics. The ~19,000 daily average and ~¥73 trillion daily value are from the most recently available data; 2024 figures may be marginally higher.

---

## Historic Trend

### Fedwire Funds Service Volume (millions of transfers)

| Year | Volume (M) | Value ($T) | Avg Txn ($M) |
|------|-----------|-----------|-------------|
| 2019 | 179.0 | 840.0 | 4.7 |
| 2020 | 184.0 | 893.0 | 4.9 |
| 2021 | 204.5 | 1,036.0 | 5.1 |
| 2022 | 196.1 | 1,011.0 | 5.2 |
| 2023 | 193.3 | 1,078.0 | 5.6 |
| 2024 | 209.9 | 1,133.4 | 5.4 |

Source: [FRB Services Annual Statistics](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html)

### T2/TARGET2 Volume (millions of transactions)

| Year | Volume (M) | Daily Avg Value (€T) |
|------|-----------|---------------------|
| 2019 | 87.8 | 1.7 |
| 2020 | 89.5 | 1.8 |
| 2021 | 92.0 | 2.0 |
| 2022 | 95.3 | 2.1 |
| 2023 | 104.4 | 2.2 |
| 2024 | 108.0 | 2.2 |

Source: [ECB TARGET Annual Reports](https://www.ecb.europa.eu/press/targetservar/html/ecb.targetservar2024.en.html)

Note: TARGET2 migrated to the T2 consolidated platform on 20 March 2023. 2024 is the first full calendar year on the new system. The ~108M figure was described by the ECB as the highest level since the introduction of the euro.

### CHAPS Volume (millions of transactions)

| Year | Volume (M) | Value (£T) |
|------|-----------|-----------|
| 2019 | 43.5 | 76.0 |
| 2020 | 41.0 | 78.5 |
| 2021 | 46.0 | 82.0 |
| 2022 | 50.5 | 83.0 |
| 2023 | 51.8 | 85.0 |
| 2024 | 52.7 | 87.5 |

Source: [Bank of England RTGS/CHAPS Annual Report 2024/25](https://www.bankofengland.co.uk/report/2025/rtgs-and-chaps-annual-report-2024-25), [Pay.UK Annual Statistics](https://www.wearepay.uk/wp-content/uploads/2025/03/Annual-Statistics-2024-v1.2.pdf)

---

## Growth Rate Analysis

| System | 5-Year CAGR (Volume) | 5-Year CAGR (Value) | Notes |
|--------|---------------------|--------------------|----|
| Fedwire | 3.2% | 6.2% | Value growth outpaces volume — larger average transfers |
| T2/TARGET2 | 4.2% | 5.3% | 2024 was record year; T2 migration may have boosted counts |
| CHAPS | 3.9% | 2.9% | Steady growth, record peak day in April 2024 (344,099 txns) |
| BOJ-NET | ~1.5% | ~2.0% | Japan's low-growth macro environment limits expansion |
| CLS | ~3.0% | ~5.0% | FX volumes growing with global trade; T+1 shift boosted activity |

**Composite RTGS 5-year volume CAGR**: ~3.5%

The key insight is that RTGS transaction **counts** grow slowly (2–4%) but transaction **values** grow faster (3–6%) as the financial system's notional obligations expand. These systems are capacity-constrained by design — they process exactly what they need to and no more.

---

## Projections (through 2035)

### Baseline Scenario (3% volume CAGR, 5% value CAGR)

| Year | Annual Volume (M) | Avg TPS (calendar) | Annual Value ($T) |
|------|-------------------|--------------------|--------------------|
| 2025 | 436 | 13.8 | 2,258 |
| 2026 | 449 | 14.2 | 2,370 |
| 2028 | 476 | 15.1 | 2,614 |
| 2030 | 505 | 16.0 | 2,882 |
| 2035 | 585 | 18.5 | 3,678 |

### High-Growth Scenario (5% volume CAGR)
Driven by: digital currency settlement integration, 24/7 RTGS operations (BOE planning), CLS expansion into new currencies.

| Year | Annual Volume (M) | Avg TPS (calendar) |
|------|-------------------|--------------------|
| 2030 | 540 | 17.1 |
| 2035 | 689 | 21.8 |

### Conservative Scenario (2% volume CAGR)
Driven by: netting efficiency gains reducing gross settlement needs, shift to instant payment rails for smaller wholesale transactions.

| Year | Annual Volume (M) | Avg TPS (calendar) |
|------|-------------------|--------------------|
| 2030 | 467 | 14.8 |
| 2035 | 515 | 16.3 |

---

## Key Findings

1. **Highest-value, lowest-TPS category in finance**: ~$2,150 trillion annual value from just ~13 TPS calendar average. Each RTGS transaction carries more economic weight than any other instrument class.

2. **CLS is the hidden giant**: FX settlement via CLS adds ~$1,750 trillion in annual settled value (estimated) through its payment-versus-payment mechanism. Its multilateral netting compresses funding needs to ~1% of gross value.

3. **CHAPS set an all-time record on 2 April 2024**: 344,099 payments in a single day, driven by the first business day after a double Easter bank holiday. This illustrates how RTGS peak loads are calendar-event driven, not market-event driven.

4. **T2 migration creates a discontinuity**: The March 2023 migration from TARGET2 to T2 means pre-2023 and post-2023 data are not perfectly comparable. The 2024 record of ~108M transactions may partly reflect the broader service scope of the T2 platform.

5. **24/7 RTGS is coming**: The Bank of England has signaled plans for extended RTGS operating hours. If adopted globally, this could increase transaction counts (by spreading settlement across more hours) without increasing peak TPS.

6. **Double-counting boundary**: RTGS settles the net positions from other systems (e.g., CCP margins, ACH net settlement, securities DVP legs). The ~423M transaction count is the final settlement layer — it does NOT double-count upstream activity.

---

## Data Quality & Limitations

- **Fedwire, T2, CHAPS**: High confidence — central banks publish detailed monthly/annual statistics
- **BOJ-NET**: Medium confidence — data is published but English-language access is limited; some figures derived from older reports
- **CLS**: Medium confidence — CLS publishes value data readily but transaction counts are less frequently reported; estimated from peak-day records and daily value averages
- **Currency conversion**: EUR/GBP/JPY values converted to USD at approximate 2024 average exchange rates (EUR/USD ~1.09, GBP/USD ~1.27, JPY/USD ~0.0067)
- **Overlap with Bank Transfers capsule**: The bank-transfers capsule includes an RTGS sub-category with Fedwire and T2 counts. This capsule goes deeper but the top-line numbers should be consistent. The bank-transfers capsule's 0.4B RTGS figure includes additional smaller national RTGS systems not covered here.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **China's CNAPS/HVPS**: The PBoC's High-Value Payment System processed ~382 million RTGS transactions in 2023 (~¥8,481 trillion). This is comparable to Fedwire in volume but is excluded from our 423M aggregate because English-language reporting is inconsistent and 2024 data is not yet available. Including CNAPS would likely push global RTGS to ~800M+ transactions.
- **India's RTGS**: RBI reports RTGS volume CAGR of 13.7% (2020-2025) with RTGS accounting for 69% of payment value but only 0.1% of volume. Absolute transaction counts are available in RBI annual reports but not included here.
- **Russia's BESP**: Effectively opaque since 2022 sanctions; pre-sanctions volume was ~20-30M transactions/year.
- **24/7 RTGS impact**: Bank of England has consulted on extended operating hours. No quantitative estimate exists for how much transaction volume would increase if RTGS operated 24/7 vs current ~10-18hr windows.
- **Intraday liquidity recycling**: How many potential RTGS transactions are avoided through intraday netting and liquidity management is unknown but significant.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| China CNAPS volume | GDP ratio: China GDP is ~65% of US GDP; if RTGS scales with GDP, expect ~135-170M transactions | 2023 CNAPS data (382M) suggests CNAPS actually exceeds Fedwire proportionally | :green_circle: |
| India RTGS volume | RBI publishes detailed payment system data; RTGS CAGR 13.7% from known 2020 baseline | RBI Annual Report, Payment & Settlement Systems in India | :green_circle: |
| Russia BESP volume | Pre-2022 BIS CPMI data available; extrapolate at 2% CAGR from last known figure | BIS Red Book 2021 contains Russian data | :yellow_circle: |
| 24/7 RTGS transaction uplift | BOE consultation responses; analogise from Faster Payments adoption curve when FPS went 24/7 | BOE 2024/25 RTGS Annual Report discusses extended hours | :yellow_circle: |
| Missing smaller RTGS systems (Swiss SIC, Canadian LVTS, Australian RITS) | BIS CPMI database covers 25+ RTGS systems; aggregate from Red Book statistical annex | BIS CPMI payment statistics portal | :green_circle: |

### Key Modeling Questions
- If CNAPS, India RTGS, and other missing systems were included, does global RTGS volume reach ~1 billion transactions? This would roughly double our current 423M estimate and change the TPS calculation to ~32.
- How does the T2 platform migration (March 2023) affect comparability of pre/post-2023 data? Is the 2024 "record" partly an artefact of broader service scope?
- What is the netting ratio between gross interbank obligations and actual RTGS settlement? If netting is becoming more efficient (e.g., CLS netting ratio improving), RTGS counts may grow slower than underlying economic activity.

### Reference Comparisons
- **GDP-to-RTGS ratio**: For systems with published data, the ratio of annual RTGS value to GDP ranges from ~7x (CHAPS/UK GDP) to ~15x (Fedwire/US GDP). Applying these ratios to countries with missing data can produce rough volume estimates.
- **BIS CPMI Red Book**: The most comprehensive cross-country payment system dataset. Updated annually with ~2-year lag. The 2023 edition covers 2022 data for 25+ jurisdictions.
- **SWIFT gpi data**: While SWIFT is messaging (not settlement), SWIFT's published message volumes (~50M/day) provide a ceiling on cross-border RTGS settlement counts since most cross-border payments settle through RTGS.

---

## Sources

- [Fedwire Funds Service Annual Statistics](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html)
- [Federal Reserve Fedwire Annual Data](https://www.federalreserve.gov/paymentsystems/fedfunds_ann.htm)
- [ECB T2 Facts and Figures](https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html)
- [ECB TARGET Services Annual Report 2024](https://www.ecb.europa.eu/press/targetservar/html/ecb.targetservar2024.en.html)
- [Bank of England RTGS/CHAPS Annual Report 2024/25](https://www.bankofengland.co.uk/report/2025/rtgs-and-chaps-annual-report-2024-25)
- [Pay.UK Annual Summary of Payment Statistics 2024](https://www.wearepay.uk/wp-content/uploads/2025/03/Annual-Statistics-2024-v1.2.pdf)
- [BOJ Payment and Settlement Statistics](https://www.boj.or.jp/en/statistics/set/kess/index.htm)
- [CLS Group Annual Report 2024](https://www.cls-group.com/about/annual-report-2024/annual-report-2024/)
- [CLS Group Record Settlement](https://www.financemagnates.com/institutional-forex/cls-group-settles-record-191-trillion-in-fx-payment-instructions-in-a-day/)
- [BIS CPMI Payment Statistics](https://www.bis.org/statistics/dataportal/payment_stats.htm)

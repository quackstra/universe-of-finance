# Bank Transfers (ACH/RTGS) — Universe of Finance Analysis

**Category**: Payments > Bank Transfers
**Priority**: #2
**Data Year**: 2024
**Last Updated**: 2026-03-26

---

## Executive Summary

Global bank transfers processed an estimated **484 billion transactions** in 2024, averaging **~15,300 TPS** with peaks approaching **~27,500 TPS**. The total value moved exceeded **$2,400 trillion** — dwarfing every other financial instrument class on Earth.

The defining story of the last decade is the **real-time payments explosion**. India's UPI alone processed 131 billion transactions in 2024 — more than all US electronic payments combined. Brazil's PIX hit 63 billion. These two systems, both launched within the last 8 years, now account for **40% of all global bank transfers by volume**.

Traditional batch ACH and RTGS systems remain critical infrastructure — Fedwire moved $1,133 trillion in 2024, averaging $5.4 million per wire — but the volume growth story belongs entirely to real-time payments, which grew at a **38% five-year CAGR**.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| **Average TPS** | ~15,338 | 🟡 Medium |
| **Peak TPS (global)** | ~25,000-30,000 | 🔴 Low |
| **India UPI peak TPS** | ~11,250 | 🟡 Medium |
| **Brazil PIX peak TPS** | ~3,500 | 🟡 Medium |
| **US ACH operational peak** | ~3,500 | 🟡 Medium |

Average TPS is calculated from ~484 billion annual transactions divided by 31.56 million seconds per year. Peak TPS reflects concurrent peak-day estimates across major time zones.

**Sources**: [ACI Worldwide](https://www.aciworldwide.com/real-time-payments-report), [Nacha](https://www.nacha.org/content/ach-network-volume-and-value-statistics), [NPCI](https://www.npci.org.in/product/upi/product-statistics)

---

## 2. Annual Volume (2024)

| Subcategory | Volume (B txns) | Share |
|-------------|----------------|-------|
| Real-time payments | 378 | 78.1% |
| Batch/ACH transfers | 106 | 21.9% |
| RTGS/Wire transfers | 0.4 | 0.08% |
| **TOTAL** | **~484** | **100%** |

Real-time payments dominate volume. The global RTP figure is extrapolated from [ACI Worldwide's 2023 benchmark](https://investor.aciworldwide.com/news-releases/news-release-details/global-real-time-payments-growth-sustainable-new-use-cases-push) of 266.2 billion transactions at 42.2% YoY growth.

**Key systems by volume (2024)**:
- 🇮🇳 **India UPI**: [131.1B transactions](https://www.npci.org.in/product/upi/product-statistics) — 27% of global total
- 🇧🇷 **Brazil PIX**: [~63B transactions](https://www.bcb.gov.br/en) — 13% of global total
- 🇺🇸 **US ACH (Nacha)**: [33.6B transactions](https://www.nacha.org/news/nacha-releases-top-50-financial-institution-ach-originators-and-receivers-2024-total-ach) — 7% of global total
- 🇪🇺 **SEPA Credit Transfers**: [~32B transactions](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h2~5ada0087d2.en.html)

---

## 3. Annual Value (2024)

| Subcategory | Value (USD T) | Share |
|-------------|--------------|-------|
| RTGS/Wire transfers | ~1,860 | 75.3% |
| Batch/ACH transfers | ~505 | 20.4% |
| Real-time payments | ~106 | 4.3% |
| **TOTAL** | **~$2,471T** | **100%** |

The value picture is the inverse of volume: **RTGS systems dominate value** despite processing <0.1% of transactions. [Fedwire alone moved $1,133 trillion](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) in 2024 at an average of $5.4 million per transfer.

**Key systems by value (2024)**:
- 🇺🇸 **Fedwire**: [$1,133T](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) — daily avg $4.52T
- 🇪🇺 **TARGET2/T2**: [~$600T](https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html) — record 108M transactions
- 🇪🇺 **SEPA Credit Transfers**: [~$238T](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h2~5ada0087d2.en.html) (EUR 220T)
- 🇺🇸 **US ACH**: [$86.2T](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
- 🇨🇳 **CIPS**: [$24.5T](https://www.cips.com.cn/en/about_us/about_cips/introduction/index.html) — 42.6% value growth YoY

---

## 4. Historic Timeseries (2015-2024)

### US ACH Network (Nacha)

| Year | Volume (B) | Value ($T) | Growth |
|------|-----------|-----------|--------|
| 2016 | 25.6 | 43.7 | — |
| 2018 | 23.0 | 51.2 | — |
| 2019 | 24.7 | ~55.8 | — |
| 2020 | 26.8 | 61.9 | 8.5% |
| 2021 | 29.1 | 72.6 | 8.6% |
| 2022 | 30.0 | 76.7 | 3.1% |
| 2023 | 31.5 | 80.1 | 5.0% |
| 2024 | 33.6 | 86.2 | 6.7% |

Source: [Nacha](https://www.nacha.org/content/ach-network-volume-and-value-statistics)

### India UPI — The Exponential Curve

| Year | Volume (B) | Growth |
|------|-----------|--------|
| 2017 | 0.018 | Launch |
| 2018 | 0.915 | 4,983% |
| 2019 | 5.35 | 485% |
| 2020 | 12.52 | 134% |
| 2021 | 22.33 | 78% |
| 2022 | 45.96 | 106% |
| 2023 | 83.71 | 82% |
| 2024 | 131.13 | 57% |

Source: [NPCI/GrabOn](https://www.grabon.in/indulge/tech/upi-statistics/)

UPI's trajectory is possibly the most dramatic growth curve in the history of financial infrastructure. From 18 million transactions in its launch year to **131 billion** in 2024 — a 7,285x increase in 7 years. The [IMF now recognizes UPI as the world's largest real-time payment system](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569), accounting for **49% of all global real-time transactions**.

### Global Real-Time Payments

| Year | Volume (B) | Growth |
|------|-----------|--------|
| 2019 | ~75 | — |
| 2020 | ~105 | ~40% |
| 2021 | ~145 | ~38% |
| 2022 | ~188 | ~30% |
| 2023 | 266.2 | 42.2% |
| 2024 | ~378 | ~42% |

Source: [ACI Worldwide](https://www.aciworldwide.com/real-time-payments-report)

---

## 5. Subcategory Breakdown

### By Transfer Type

**Real-Time Payments (78% of volume)**
The fastest-growing segment. India's UPI and Brazil's PIX are the twin engines, but real-time payments are now live in [80+ countries](https://www.aciworldwide.com/real-time-payments-report):

| System | Country | 2024 Volume (B) | 2024 Value | Launch Year |
|--------|---------|-----------------|-----------|-------------|
| UPI | India | 131.1 | ~$2.5T | 2016 |
| PIX | Brazil | ~63.0 | ~$3.8T | 2020 |
| Faster Payments | UK | 5.1 | £4.2T | 2008 |
| SEPA Instant | EU | ~5.0 | — | 2017 |
| FedNow | US | 0.0015 | $38.2B | 2023 |
| PromptPay | Thailand | ~18 (est.) | — | 2017 |
| IBPS/NetsIPT | Various | ~156 | — | Various |

**Batch/ACH (22% of volume)**
Mature, steady-growth systems handling recurring payments (payroll, bills, B2B):
- US ACH: [33.6B transactions, $86.2T](https://www.nacha.org/content/ach-network-volume-and-value-statistics) — Same Day ACH reached [1.2B transactions](https://www.nacha.org/news/same-day-ach-passes-major-milestone-2024-ach-network-shows-higher-growth) (45.3% growth)
- SEPA Credit Transfers: [~32B transactions, ~EUR 220T](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h2~5ada0087d2.en.html)

**RTGS/Wire (0.08% of volume, 75% of value)**
The backbone of large-value settlement:
- [Fedwire](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html): 210M transactions, $1,133T
- [TARGET2/T2](https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html): 108M transactions (record high)
- [CHAPS](https://www.bankofengland.co.uk/report/2025/rtgs-and-chaps-annual-report-2024-25): 52.7M transactions

### By Region (Real-Time Payments, 2023)

| Region | Volume (B) | Share | Key Systems |
|--------|-----------|-------|-------------|
| Asia-Pacific | 185.8 | 70% | UPI, PromptPay, IBPS |
| Latin America | ~40 | 15% | PIX |
| Europe | ~12 | 5% | Faster Payments, SEPA Instant |
| Africa | ~8 | 3% | Nigeria NIP (7.9B) |
| North America | ~3 | 1% | RTP, FedNow |
| Rest of World | ~17 | 6% | — |

Source: [ACI Worldwide 2024 Report](https://investor.aciworldwide.com/news-releases/news-release-details/global-real-time-payments-growth-sustainable-new-use-cases-push)

---

## 6. Growth Rates

| System | 5-Year CAGR | Period | Confidence |
|--------|------------|--------|------------|
| India UPI | **89.4%** | 2019-2024 | 🟢 High |
| Global RTP | **38.2%** | 2019-2024 | 🟡 Medium |
| Brazil PIX | **N/A** | (launched 2020) | — |
| US ACH | **6.35%** | 2019-2024 | 🟢 High |
| Fedwire | **4.06%** | 2019-2024 | 🟢 High |
| **Composite global** | **22.6%** | 2019-2024 | 🟡 Medium |

The composite 22.6% CAGR is almost entirely driven by real-time payments. Traditional ACH and RTGS grow at a sedate 4-6%.

---

## 7. Baseline Projection (2026-2035)

Assumes real-time payments continue at [ACI's forecast 16.7% CAGR](https://www.aciworldwide.com/real-time-payments-report) through 2028, then decelerate gradually. Batch ACH at 5% CAGR, RTGS at 3%.

| Year | Total (B txns) | Average TPS |
|------|---------------|-------------|
| 2024 | 484 | 15,338 |
| 2026 | 632 | 20,030 |
| 2028 | 830 | 26,309 |
| 2030 | 1,026 | 32,502 |
| 2035 | 1,318 | 41,758 |

By 2030, global bank transfers cross the **1 trillion transactions/year** threshold — effectively 1,000 bank transfers for every person on Earth annually.

---

## 8. High-Growth Projection (2026-2035)

Assumes UPI expands internationally (UAE, Singapore, Europe linkages already underway), [EU Instant Payments Regulation](https://investor.aciworldwide.com/news-releases/news-release-details/global-real-time-payments-growth-sustainable-new-use-cases-push) mandates SEPA Instant adoption, FedNow reaches critical mass, and Africa/SE Asia launch new RTP systems. Real-time payments at 25% CAGR through 2030.

| Year | Total (B txns) | Average TPS |
|------|---------------|-------------|
| 2024 | 484 | 15,338 |
| 2026 | 712 | 22,566 |
| 2028 | 1,062 | 33,664 |
| 2030 | 1,602 | 50,762 |
| 2035 | 3,125 | 99,020 |

In this scenario, global bank transfers approach **~100,000 TPS** average by 2035 — a 6.5x increase from today.

---

## 9. Conservative Projection (2026-2035)

Assumes regulatory friction, privacy backlash, interoperability failures, and incumbent resistance slow adoption. Real-time payments at 10% CAGR.

| Year | Total (B txns) | Average TPS |
|------|---------------|-------------|
| 2024 | 484 | 15,338 |
| 2026 | 570 | 18,064 |
| 2028 | 673 | 21,325 |
| 2030 | 796 | 25,229 |
| 2035 | 1,225 | 38,818 |

Even in the conservative case, bank transfers still exceed 1 trillion/year by 2035.

---

## Key Insights

1. **Real-time payments have eaten the world.** In just 8 years, systems like UPI and PIX have gone from zero to dominating global transaction volume. Real-time now accounts for 78% of all bank transfers by volume.

2. **The value inversion.** RTGS processes 0.08% of transactions but 75% of the value. The average Fedwire transfer ($5.4M) is ~180,000x the average UPI payment (~$30). These are fundamentally different use cases served by the same "bank transfer" umbrella.

3. **India is the center of gravity.** UPI alone is 27% of global bank transfer volume. India processes more real-time payments than the rest of the world combined. The IMF recognizes UPI as [49% of all global real-time transactions](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569).

4. **The US is surprisingly behind.** FedNow processed just 1.5 million transactions in all of 2024 — about 0.00031% of what India's UPI handles. Even Same Day ACH at [1.2 billion transactions](https://www.nacha.org/news/same-day-ach-passes-major-milestone-2024-ach-network-shows-higher-growth) is modest compared to India and Brazil.

5. **SWIFT is the messaging layer, not the rail.** SWIFT's [53.3 million messages/day](https://www.swift.com/about-us/discover-swift/fin-traffic-figures) coordinate cross-border payments but don't settle them. The actual settlement runs over Fedwire, TARGET2, or correspondent bank networks.

6. **The trillion-transaction threshold approaches.** Under all three projections, global bank transfers exceed 1 trillion transactions/year between 2030-2035.

---

## Methodology Notes

- Global totals are constructed bottom-up from major system statistics, with "Rest of World" estimated from ACI Worldwide's global benchmarks minus known systems.
- All values converted to USD at 2024 average exchange rates.
- SWIFT volumes excluded from totals to prevent double-counting (SWIFT is messaging, not settlement).
- See `workings/calculations.md` for full derivations and `workings/assumptions.md` for all assumptions.
- Confidence levels: 🟢 Direct from operator reports | 🟡 Derived from multiple sources | 🔴 Estimated

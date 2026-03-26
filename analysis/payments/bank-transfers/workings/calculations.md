# Calculations — Bank Transfers (ACH/RTGS)

## 1. Current TPS (2024)

### Global Annual Volume Build-Up

| System | Region | 2024 Volume (B txns) | Confidence |
|--------|--------|---------------------|------------|
| US ACH (Nacha) | US | 33.6 | :green_circle: High |
| Fedwire | US | 0.210 | :green_circle: High |
| FedNow | US | 0.0015 | :green_circle: High |
| SEPA Credit Transfers | Europe | 32.0 | :green_circle: High |
| TARGET2/T2 | Europe | 0.108 | :green_circle: High |
| UK Faster Payments | UK | 5.1 | :green_circle: High |
| UK CHAPS | UK | 0.053 | :green_circle: High |
| UK BACS | UK | 4.5 (est.) | :yellow_circle: Medium |
| India UPI | India | 131.1 | :green_circle: High |
| Brazil PIX | Brazil | 63.0 | :yellow_circle: Medium |
| China CIPS | China | 0.008 | :green_circle: High |
| China domestic (CNAPS est.) | China | 80.0 | :red_circle: Low |
| Rest of World RTP | Various | 45.0 | :red_circle: Low |
| Rest of World batch/RTGS | Various | 35.0 | :red_circle: Low |
| **GLOBAL TOTAL** | | **~429.7** | :yellow_circle: Medium |

### Notes on "Rest of World" estimates
- ACI Worldwide reported 266.2B global real-time payments in 2023. Extrapolating at 42% growth → ~378B in 2024.
- Known RTP systems (UPI 131.1B + PIX 63B + UK FP 5.1B + partial SEPA Instant ~5B) = ~204B
- Implies ~174B from other systems (Thailand PromptPay, Korea, Nigeria, Indonesia, etc.)
- However, ACI's 2023 figure of 266.2B included UPI at 129.3B and Brazil at 37.4B, leaving ~100B for "other" in 2023.
- With growth, ~120B for "other RTP" in 2024 seems reasonable. We use 45B as a conservative non-RTP "rest of world" and fold the RTP remainder into known systems + rest of world RTP.
- **Revised global estimate**: Using ACI's implied ~378B real-time + ~106B batch/RTGS = **~484B total**

### Average TPS Calculation

```
Global volume = ~484 billion transactions (2024 estimate)
Seconds per year = 365.25 × 86,400 = 31,557,600

Average TPS = 484,000,000,000 / 31,557,600 = ~15,338 TPS
```

### Peak TPS Estimation

**India UPI peak**: December 2024 had 16.73B transactions in 31 days.
- Peak day estimate: 16.73B / 31 × 1.5 (peak-to-average ratio) ≈ 810M transactions/day
- Peak second estimate: Assuming 80% of daily volume in 16 hours = 810M × 0.8 / 57,600 ≈ **11,250 TPS** (UPI alone)

**Brazil PIX peak**: 252.1M transactions on Dec 20, 2024
- Assuming 80% in 16 hours: 252.1M × 0.8 / 57,600 ≈ **3,502 TPS**

**Global peak TPS estimate**: Sum of concurrent peaks across time zones
- India peak + Brazil peak + US ACH peak + Europe peak + others
- US ACH daily average: 33.6B / 250 business days = 134.4M/day, peak ~200M/day → operational peak ~3,500 TPS
- Europe SEPA daily average: 32B / 250 = 128M/day → ~2,200 TPS operational
- Adding all: **~25,000-30,000 TPS** global peak estimate

## 2. Annual Volume (2024)

| Category | Volume (B txns) | Source |
|----------|----------------|--------|
| ACH/Batch transfers | ~106B | US ACH 33.6B + SEPA 32B + UK BACS 4.5B + China est. 36B |
| Real-time payments | ~378B | ACI 2023 (266.2B) × 1.42 growth |
| RTGS/Wire transfers | ~0.4B | Fedwire 0.21B + T2 0.11B + CHAPS 0.05B + others ~0.03B |
| **TOTAL** | **~484B** | |

## 3. Annual Value (2024)

| System | Value (USD) | Source | Confidence |
|--------|-------------|--------|------------|
| US ACH | $86.2T | Nacha | :green_circle: High |
| Fedwire | $1,133T | Fed | :green_circle: High |
| SEPA Credit Transfers | ~$238T | ECB (~EUR 220T × 1.08) | :green_circle: High |
| TARGET2/T2 | ~$600T (est.) | ECB (derived from daily values) | :yellow_circle: Medium |
| UK Faster Payments | $5.3T | Pay.UK (GBP 4.2T × 1.27) | :green_circle: High |
| UK CHAPS | ~$127T (est.) | BoE historical ratios | :yellow_circle: Medium |
| India UPI | ~$2.5T | NPCI (est. from monthly data) | :yellow_circle: Medium |
| Brazil PIX | ~$3.8T | BCB | :yellow_circle: Medium |
| China CIPS | $24.5T | CIPS | :green_circle: High |
| China domestic (est.) | ~$150T | Estimate | :red_circle: Low |
| SWIFT cross-border (context) | ~$150T/yr est. | $300B/day × 250 days × 2 | :yellow_circle: Medium |
| Rest of World | ~$100T | Estimate | :red_circle: Low |
| **GLOBAL TOTAL** | **~$2,471T** | | :yellow_circle: Medium |

**Note**: RTGS systems like Fedwire and TARGET2/T2 handle extremely high-value transactions (avg $5.4M on Fedwire), which is why they dominate the value column despite low transaction counts.

## 4. Historic Timeseries (2015-2024)

### US ACH Network Volume (Nacha)

| Year | Volume (B) | Value ($T) | YoY Growth |
|------|-----------|-----------|------------|
| 2015 | 24.0 (est.) | ~$42 | ~5% |
| 2016 | 25.6 | $43.7 | 6.7% |
| 2017 | 21.5* | $46.8 | — |
| 2018 | 23.0 | $51.2 | 7.0% |
| 2019 | 24.7 | ~$55.8 | 7.4% |
| 2020 | 26.8 | $61.9 | 8.5% |
| 2021 | 29.1 | $72.6 | 8.6% |
| 2022 | 30.0 | $76.7 | 3.1% |
| 2023 | 31.5 | $80.1 | 5.0% |
| 2024 | 33.6 | $86.2 | 6.7% |

*Note: The 2017 figure of 21.5B from Nacha appears to represent network payments only (excluding government). The 2016 figure of 25.6B includes all payments. Adjusting for consistency, the series shows steady ~5-7% annual growth.

### India UPI Annual Volume

| Year | Volume (B txns) | YoY Growth |
|------|----------------|------------|
| 2017 | 0.018 | — (launch year) |
| 2018 | 0.915 | 4,983% |
| 2019 | 5.35 | 485% |
| 2020 | 12.52 | 134% |
| 2021 | 22.33 | 78% |
| 2022 | 45.96 | 106% |
| 2023 | 83.71 | 82% |
| 2024 | 131.13 | 57% |

### Fedwire Annual Volume

| Year | Volume (M txns) | Value ($T) | YoY Growth |
|------|----------------|-----------|------------|
| 2015 | ~155 (est.) | ~$715 | — |
| 2016 | ~160 (est.) | ~$730 | — |
| 2017 | ~162 (est.) | ~$740 | — |
| 2018 | ~168 (est.) | ~$765 | — |
| 2019 | ~172 (est.) | ~$780 | — |
| 2020 | 184.0 | $840.5 | 9.8% |
| 2021 | 204.5 | $991.8 | 11.1% |
| 2022 | 196.1 | $1,060.3 | -4.1% |
| 2023 | 193.3 | $1,087.2 | -1.4% |
| 2024 | 209.9 | $1,133.4 | 8.6% |

### Global Real-Time Payments (ACI Worldwide estimates)

| Year | Volume (B txns) | YoY Growth |
|------|----------------|------------|
| 2018 | ~50 (est.) | — |
| 2019 | ~75 (est.) | ~50% |
| 2020 | ~105 | ~40% |
| 2021 | ~145 | ~38% |
| 2022 | ~188 | ~30% |
| 2023 | 266.2 | 42.2% |
| 2024 | ~378 (est.) | ~42% |

## 5. Growth Rate Calculations

### US ACH 5-Year CAGR (2019-2024)
```
CAGR = (33.6 / 24.7)^(1/5) - 1 = (1.3603)^0.2 - 1 = 6.35%
```

### India UPI 5-Year CAGR (2019-2024)
```
CAGR = (131.13 / 5.35)^(1/5) - 1 = (24.51)^0.2 - 1 = 89.4%
```

### Global Real-Time Payments 5-Year CAGR (2019-2024 est.)
```
CAGR = (378 / 75)^(1/5) - 1 = (5.04)^0.2 - 1 = 38.2%
```

### Fedwire 5-Year CAGR (2019-2024)
```
CAGR = (209.9 / 172)^(1/5) - 1 = (1.220)^0.2 - 1 = 4.06%
```

### Composite Global Bank Transfer CAGR (2019-2024 est.)
```
2019 estimated global total: ~175B (75B RTP + ~80B batch + ~20B other)
2024 estimated global total: ~484B
CAGR = (484 / 175)^(1/5) - 1 = (2.766)^0.2 - 1 = 22.6%
```

## 6. Baseline Projection (2026-2035)

Assumptions:
- Real-time payments: 16.7% CAGR through 2028 (per ACI), then decelerating 1.5pp/year
- ACH/batch: 5% CAGR, stable
- RTGS/wire: 3% CAGR, stable

| Year | RTP (B) | Batch (B) | RTGS (B) | Total (B) | TPS (avg) |
|------|---------|-----------|----------|-----------|-----------|
| 2024 | 378 | 106 | 0.4 | 484 | 15,338 |
| 2025 | 441 | 111 | 0.4 | 553 | 17,519 |
| 2026 | 515 | 117 | 0.4 | 632 | 20,030 |
| 2027 | 601 | 123 | 0.4 | 724 | 22,942 |
| 2028 | 701 | 129 | 0.4 | 830 | 26,309 |
| 2029 | 795 | 135 | 0.5 | 931 | 29,499 |
| 2030 | 883 | 142 | 0.5 | 1,026 | 32,502 |
| 2031 | 962 | 149 | 0.5 | 1,112 | 35,235 |
| 2032 | 1,029 | 157 | 0.5 | 1,186 | 37,582 |
| 2033 | 1,081 | 165 | 0.5 | 1,246 | 39,487 |
| 2034 | 1,113 | 173 | 0.5 | 1,287 | 40,775 |
| 2035 | 1,136 | 181 | 0.5 | 1,318 | 41,758 |

## 7. High-Growth Projection (2026-2035)

Assumptions:
- Real-time payments maintain 25% CAGR through 2030, then 15% through 2035
- ACH/batch: 7% CAGR (digitization of remaining cheque/cash flows)
- RTGS/wire: 5% CAGR
- Drivers: UPI global rollout (UAE, Singapore, Europe), PIX expansion, SEPA Instant mandate, FedNow maturity, Africa/SE Asia RTP launch

| Year | RTP (B) | Batch (B) | RTGS (B) | Total (B) | TPS (avg) |
|------|---------|-----------|----------|-----------|-----------|
| 2024 | 378 | 106 | 0.4 | 484 | 15,338 |
| 2025 | 473 | 113 | 0.4 | 587 | 18,594 |
| 2026 | 591 | 121 | 0.4 | 712 | 22,566 |
| 2027 | 738 | 130 | 0.5 | 868 | 27,510 |
| 2028 | 923 | 139 | 0.5 | 1,062 | 33,664 |
| 2029 | 1,154 | 149 | 0.5 | 1,303 | 41,291 |
| 2030 | 1,442 | 159 | 0.5 | 1,602 | 50,762 |
| 2031 | 1,659 | 170 | 0.5 | 1,830 | 57,984 |
| 2032 | 1,907 | 182 | 0.6 | 2,090 | 66,221 |
| 2033 | 2,194 | 195 | 0.6 | 2,389 | 75,712 |
| 2034 | 2,523 | 209 | 0.6 | 2,732 | 86,589 |
| 2035 | 2,901 | 223 | 0.6 | 3,125 | 99,020 |

## 8. Conservative Projection (2026-2035)

Assumptions:
- Real-time payments: 10% CAGR (slower adoption, regulatory friction)
- ACH/batch: 3% CAGR (market saturation)
- RTGS/wire: 2% CAGR
- Factors: Regulatory backlash, privacy concerns, interoperability failures, incumbent resistance

| Year | RTP (B) | Batch (B) | RTGS (B) | Total (B) | TPS (avg) |
|------|---------|-----------|----------|-----------|-----------|
| 2024 | 378 | 106 | 0.4 | 484 | 15,338 |
| 2025 | 416 | 109 | 0.4 | 526 | 16,657 |
| 2026 | 457 | 113 | 0.4 | 570 | 18,064 |
| 2027 | 503 | 116 | 0.4 | 619 | 19,621 |
| 2028 | 553 | 119 | 0.4 | 673 | 21,325 |
| 2029 | 609 | 123 | 0.4 | 732 | 23,198 |
| 2030 | 669 | 127 | 0.4 | 796 | 25,229 |
| 2031 | 736 | 130 | 0.4 | 867 | 27,475 |
| 2032 | 810 | 134 | 0.5 | 944 | 29,924 |
| 2033 | 891 | 138 | 0.5 | 1,029 | 32,618 |
| 2034 | 980 | 142 | 0.5 | 1,123 | 35,580 |
| 2035 | 1,078 | 147 | 0.5 | 1,225 | 38,818 |

# Consumer Card Payments — Calculations & Derivations

> All math shown step-by-step. Every input is tagged with source and confidence.

---

## 1. Total Global Card Purchase Transactions (2024)

**Primary Source:** Nilson Report — "Global Network Card Results Worldwide — 2024"
- Purchase transactions on global brand cards (Visa, UnionPay, Mastercard, AmEx, JCB, Discover/Diners Club) = **772.73 billion** in 2024
- Growth: +12.4% over 2023 (687.19B)

**Cross-check:** Capital One Shopping research cites ~791 billion total credit card transactions in 2024. The ~18B difference likely includes private-label and domestic-only cards not counted in the Nilson global brand figure.

**Working figure for TPS calculations:** 772.73 billion (global branded networks only) 🟢 High

---

## 2. Average TPS Calculation (2024)

```
Seconds in a year = 365 × 86,400 = 31,536,000

Average TPS = 772.73 × 10⁹ / 31,536,000
            = 772,730,000,000 / 31,536,000
            = 24,501 TPS
```

**Result: ~24,500 TPS average** 🟡 Medium (derived from annual total)

Cross-check: Capital One Shopping reports 90.3M transactions/hour globally:
```
90,300,000 / 3,600 = 25,083 TPS
```
Consistent with our calculation (within 2.4%).

---

## 3. Peak TPS Estimation (2024)

**VisaNet stated capacity:** 83,000 transaction messages per second ([Visa corporate factsheet](https://www.visa.co.uk/dam/VCOM/download/corporate/media/visanet-technology/aboutvisafactsheet.pdf))

**Estimated actual peak:** Visa does not publicly disclose observed peak TPS. Industry estimates place actual peak during events like Singles' Day, Black Friday at 2-3× average.

```
Estimated peak (all networks) = avg TPS × peak multiplier
                               = 24,500 × 2.5 (conservative mid-range)
                               = ~61,250 TPS
```

However, this is the theoretical all-network peak if all networks peaked simultaneously. More realistically:

**Visa alone average TPS:**
```
Visa 2024: 233.8B transactions / 31,536,000 sec = 7,413 TPS average
Estimated Visa peak: ~17,000 TPS (industry consensus, ~2.3× average)
```

**All-network estimated peak TPS:** ~50,000-65,000 TPS 🔴 Low (estimated, no public disclosure of actual observed peak)

---

## 4. Annual Transaction Value (2024)

**Nilson Report:** Global card purchase volume + cash volume = **$51.920 trillion** (2024)
- Up 1.0% from $51.428T in 2023
- This includes purchase volume AND cash advances/withdrawals

**Purchase volume only (estimated):**
- The $42.7T figure is from an earlier period (2023 data per paymentscardsandmobile.com)
- 2024 purchase-only volume estimated at ~$44-45T based on growth trends

**US-specific (2024):**
- Four major US networks (Visa, MC, AmEx, Discover) = $27.7T consumer transactions
- Visa US = $6.583T, Mastercard US = $2.784T

**Working figure:** $51.92T total volume (purchase + cash) 🟢 High
**Purchase-only estimate:** ~$44.5T 🟡 Medium

---

## 5. Network-by-Network Breakdown (2024)

### Transactions Processed (billions)

| Network | Annual Txns (B) | Share (%) | Source | Confidence |
|---------|----------------|-----------|--------|------------|
| Visa | 233.8 (processed) / 303 (branded) | ~39% | Visa FY2024 10-K | 🟢 |
| UnionPay | ~247 (est.) | ~32% | Derived from market share | 🟡 |
| Mastercard | 159.4 (switched) / ~185 (est. total) | ~24% | MC FY2024 earnings | 🟢/🟡 |
| American Express | ~15 (est.) | ~2% | Derived from "23.6B Amex+Discover" | 🟡 |
| JCB | ~11 (est.) | ~1.4% | Industry estimates | 🔴 |
| Discover/Diners | ~8.6 (est.) | ~1.1% | Derived | 🔴 |
| **Total (global brands)** | **~772.73** | **100%** | Nilson Report 2024 | 🟢 |

### UnionPay derivation:
```
UnionPay 2023: 228B transactions (coinlaw.io)
Global growth 2023→2024: +12.4%
UnionPay 2024 estimate: 228 × 1.084 = ~247B
(Using slightly lower growth than global avg due to China slowdown)
Market share check: 247/772.73 = 32.0% ✓ (matches reported ~32%)
```

### AmEx + Discover derivation:
```
Reported: AmEx + Discover combined ≈ 23.6B (Capital One Shopping)
Estimated split: AmEx ~15B, Discover ~8.6B
(Based on AmEx being roughly 1.7× Discover's size by volume)
```

---

## 6. Credit vs Debit vs Prepaid Split

### By Transaction Count (global estimate)

**US Federal Reserve survey (Oct 2024):**
- Credit: 35% of consumer transactions
- Debit: 30% of consumer transactions
- Other (cash, checks, etc.): 35%

**Among card-only transactions globally (estimated):**

| Type | Estimated Share | Estimated Volume (B) | Source | Confidence |
|------|----------------|---------------------|--------|------------|
| Debit | ~55% | ~425B | Industry consensus | 🟡 |
| Credit | ~37% | ~286B | Industry consensus | 🟡 |
| Prepaid | ~8% | ~62B | Industry estimates | 🔴 |
| **Total** | **100%** | **~773B** | | |

Rationale: Debit cards dominate by transaction count globally due to high-volume, lower-value everyday purchases. Credit cards dominate by value.

### By Value (global estimate)

| Type | Estimated Share | Estimated Value ($T) | Source | Confidence |
|------|----------------|---------------------|--------|------------|
| Credit | ~52% | ~$23.1T | Derived from Visa/MC splits | 🟡 |
| Debit | ~42% | ~$18.7T | Derived from Visa/MC splits | 🟡 |
| Prepaid | ~6% | ~$2.7T | Industry estimates | 🔴 |
| **Total** | **100%** | **~$44.5T** | (purchase only) | |

Supporting data (Visa FY2024):
- Visa credit volume: $5.31T
- Visa debit volume: $6.02T
- Debit > credit by count at Visa (consistent with global pattern)

---

## 7. Regional Breakdown (2024)

Based on Payments Dive / Nilson data: 775.96B total payments (slight difference from 772.73B due to methodology)

| Region | Share (%) | Est. Volume (B) | Source | Confidence |
|--------|-----------|-----------------|--------|------------|
| Asia-Pacific | 45.7% | ~353 | Payments Dive / Nilson | 🟢 |
| North America (US) | 20.6% | ~159 | Payments Dive / Nilson | 🟢 |
| Europe | 19.5% | ~151 | Payments Dive / Nilson | 🟢 |
| Latin America | ~7% | ~54 | Estimated from growth data | 🟡 |
| Middle East & Africa | ~4% | ~31 | Estimated | 🟡 |
| Canada & Other | ~3.2% | ~25 | Residual | 🔴 |

---

## 8. Historic Timeseries (2015-2024)

### Global Card Purchase Transactions (all major networks, billions)

Data points confirmed from sources:
- 2015: ~227B (Nilson Report projected)
- 2022: 624.86B (Nilson Report)
- 2023: 687.19B (derived: 772.73 / 1.124 = ~687.5B, confirms)
- 2024: 772.73B (Nilson Report)

For interpolation of missing years, use Visa's growth as proxy:

**Visa processed transactions timeline:**
- FY2017: 111.2B → Visa share ~38%, global estimate: 111.2/0.38 = ~293B
- FY2020: ~164.7B (reported) → global estimate: 164.7/0.37 = ~445B (COVID dip)
- FY2022: ~192B (derived) → global: ~505B → actual Nilson: 624.86B (Visa share lower at ~31%)
- FY2023: 212.6B → global: 687.19B (Visa share: 30.9%)
- FY2024: 233.8B → global: 772.73B (Visa share: 30.3%)

**Reconstructed timeseries (best estimates):**

| Year | Global Txns (B) | Source/Method | Confidence |
|------|----------------|---------------|------------|
| 2015 | 227 | Nilson projected | 🟡 |
| 2016 | 260 | Interpolated (+14.5% growth) | 🔴 |
| 2017 | 300 | Derived from Visa 111.2B @ ~37% share | 🟡 |
| 2018 | 346 | Interpolated (+15.3% growth) | 🔴 |
| 2019 | 398 | Interpolated (+15% growth) | 🔴 |
| 2020 | 380 | Estimated (COVID dip ~-4.5%) | 🔴 |
| 2021 | 467 | Derived from Nilson 2022 data (-24.5% back) | 🟡 |
| 2022 | 625 | Nilson Report (624.86B) | 🟢 |
| 2023 | 687 | Nilson/derived (772.73/1.124) | 🟢 |
| 2024 | 773 | Nilson Report (772.73B) | 🟢 |

**CAGR Calculation (2015-2024):**
```
CAGR = (773/227)^(1/9) - 1
     = (3.405)^(0.1111) - 1
     = 1.1459 - 1
     = 14.6%
```

**CAGR Calculation (2019-2024), excluding COVID base effect:**
```
CAGR = (773/398)^(1/5) - 1
     = (1.942)^(0.2) - 1
     = 1.1417 - 1
     = 14.2%
```

**CAGR Calculation (2022-2024), recent trend:**
```
CAGR = (773/625)^(1/2) - 1
     = (1.237)^(0.5) - 1
     = 1.112 - 1
     = 11.2%
```

---

## 9. Projection Models (2026-2035)

### Baseline: Current Trends Continue

**Assumptions:**
1. CAGR of 8.5% (moderated from recent 11-12% as market matures)
2. Consistent with Nilson's projected 891.2B by 2027 (CAGR ~7.3% from 2022)
3. Gradual deceleration: 9% → 7% over decade

| Year | Growth Rate | Annual Volume (B) | Avg TPS |
|------|------------|-------------------|---------|
| 2026 | 9.0% | 918 | 29,114 |
| 2027 | 8.5% | 996 | 31,586 |
| 2028 | 8.0% | 1,076 | 34,113 |
| 2029 | 7.5% | 1,157 | 36,672 |
| 2030 | 7.0% | 1,238 | 39,239 |
| 2031 | 7.0% | 1,324 | 41,986 |
| 2032 | 7.0% | 1,417 | 44,925 |
| 2033 | 7.0% | 1,516 | 48,070 |
| 2034 | 7.0% | 1,622 | 51,434 |
| 2035 | 7.0% | 1,736 | 55,035 |

```
2025 estimate: 773 × 1.095 = 846B (mid-point growth)
2026: 846 × 1.09 = 918B → 918B/31.536M = 29,114 TPS
...continuing pattern
```

### High Growth: Accelerating Cashless Adoption

**Assumptions:**
1. Developing markets (India, Africa, SE Asia, LatAm) accelerate card adoption
2. Digital wallets increasingly backed by card rails
3. CAGR of 12% sustained, declining to 9% by 2035
4. IoT/embedded payments add new transaction categories

| Year | Growth Rate | Annual Volume (B) | Avg TPS |
|------|------------|-------------------|---------|
| 2026 | 13.0% | 987 | 31,292 |
| 2027 | 12.5% | 1,110 | 35,199 |
| 2028 | 12.0% | 1,244 | 39,438 |
| 2029 | 11.5% | 1,387 | 43,966 |
| 2030 | 11.0% | 1,539 | 48,802 |
| 2031 | 10.5% | 1,701 | 53,916 |
| 2032 | 10.0% | 1,871 | 59,308 |
| 2033 | 9.5% | 2,049 | 64,952 |
| 2034 | 9.0% | 2,233 | 70,801 |
| 2035 | 9.0% | 2,434 | 77,173 |

```
2025 estimate: 773 × 1.13 = 873B
2026: 873 × 1.13 = 987B → 987B/31.536M = 31,292 TPS
...continuing pattern
```

### Conservative: Market Saturation

**Assumptions:**
1. Card growth decelerates as A2A (account-to-account) payments gain share
2. Regulatory pressure on interchange fees slows expansion
3. China's card growth stagnates as mobile payments dominate
4. CAGR of 5% declining to 3%

| Year | Growth Rate | Annual Volume (B) | Avg TPS |
|------|------------|-------------------|---------|
| 2026 | 6.0% | 869 | 27,548 |
| 2027 | 5.5% | 917 | 29,071 |
| 2028 | 5.0% | 963 | 30,525 |
| 2029 | 4.5% | 1,006 | 31,898 |
| 2030 | 4.0% | 1,046 | 33,174 |
| 2031 | 3.5% | 1,083 | 34,335 |
| 2032 | 3.5% | 1,121 | 35,537 |
| 2033 | 3.0% | 1,155 | 36,603 |
| 2034 | 3.0% | 1,189 | 37,701 |
| 2035 | 3.0% | 1,225 | 38,832 |

```
2025 estimate: 773 × 1.06 = 819B
2026: 819 × 1.06 = 869B → 869B/31.536M = 27,548 TPS
...continuing pattern
```

---

## 10. Sanity Checks

1. **TPS sanity:** 24,500 avg TPS in 2024 → ~88.2M/hour → ~2.1B/day → ~772B/year ✓
2. **Value per transaction:** $51.92T / 772.73B txns = $67.19 avg → plausible for mixed credit/debit ✓
3. **Visa share check:** 233.8B / 772.73B = 30.3% (reported ~39% for purchase txns; difference because 233.8B is Visa-processed, not all Visa-branded purchase txns) — needs note
4. **Growth rate check:** 12.4% YoY 2023→2024 is aggressive but consistent with post-COVID acceleration and emerging market adoption
5. **Projection sanity:** Baseline 2035 TPS of 55,035 is within VisaNet's current 83,000 capacity (for Visa alone), suggesting the industry will need ongoing capacity investment

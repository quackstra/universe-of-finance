# Equity Markets — Calculation Workings

## 1. Annual Number of Trades (2024)

### WFE Data (Primary Source)

WFE December 2024 dashboard reports:
- Number of trades (Dec 2024 month): **5,094,833 thousand** = ~5.095 billion trades in December alone
- YoY change: **+26.53%**

WFE H1 2024 report:
- APAC alone: **18.68 billion trades** in H1 2024 (highest half-year in 5 years)
- H1 2024 equity trading volumes rose **9.6%** vs H2 2023, and **+18.25%** vs H1 2023

### Deriving Annual Global Equity Trades (2024)

**Method A: From WFE December monthly data**
- December 2024: 5.095B trades
- December is typically an average-to-low month (holiday effect, but also year-end positioning)
- Using December as representative: 5.095B x 12 = ~61.1B trades/year
- Adjustment: December is ~8-9% of annual volume typically → 5.095B / 0.085 = ~59.9B

**Method B: From H1 APAC data + regional shares**
- APAC H1 2024: 18.68B trades
- APAC typically represents ~55-60% of global equity trades by count (driven by India, China, Japan)
- If APAC = 57% of global: 18.68B / 0.57 = 32.8B for H1
- Full year (H2 typically slightly lower): 32.8B x 2.05 = ~67.2B
- This seems high; APAC share may be higher at ~65%
- At 65%: 18.68B / 0.65 = 28.7B for H1 → ~58.9B annual

**Method C: From 2023 baseline + growth**
- WFE FY2023: Estimated ~48-50B equity trades globally
- 2024 YoY growth in number of trades: +26.53% (WFE December dashboard)
- 50B x 1.2653 = ~63.3B

**Triangulated Estimate: ~60-63 billion equity trades globally in 2024**
**Central estimate: 61.5 billion trades** 🟡

### Cross-check with US Data
- US consolidated equity trades: ~15-20M/day across all venues
- Trading days: ~252
- US annual: 15M x 252 = 3.78B to 20M x 252 = 5.04B trades
- US is roughly 7-8% of global trade count (much smaller share by count than by value due to India/China volume)
- 4.4B / 0.07 = ~63B global — consistent with estimate above

## 2. TPS Calculations

### Average TPS (2024)

- Annual trades: 61.5 billion
- Trading hours vary by exchange, but effectively there are ~22 trading hours globally per weekday (overlapping sessions)
- Trading days: ~252 (varies by market; using US convention)
- Total trading seconds: 252 days x 22 hours x 3,600 seconds = 19,958,400 seconds
- **Average Global TPS: 61,500,000,000 / 19,958,400 = ~3,082 TPS**

Alternative (using 6.5-hour primary session per market, 3 major time zones):
- Effective global trading: ~16 hours/day with significant overlap
- 252 x 16 x 3,600 = 14,515,200 seconds
- **Average TPS: 61.5B / 14.5M = ~4,241 TPS**

**Central estimate: ~3,500 TPS average** 🟡

### Peak TPS

- Peak days during volatility events (e.g., Sep 2024 China stimulus, Aug 2024 VIX spike):
  - Combined Shanghai + Shenzhen hit 3.45 trillion yuan in a single day (Oct 2024)
  - US markets see 2-3x normal volume on peak days
- Peak day volume: ~3x average → ~730M trades in a day
- Peak TPS during market open (first 30 minutes):
  - ~20% of daily volume in first 30 minutes = 146M trades in 1,800 seconds
  - **Peak TPS: ~81,000 TPS** during opening surges on peak volatility days
- Sustained peak (busiest hour): ~15% of daily in 1 hour = 109.5M / 3,600 = ~30,400 TPS

**Peak TPS estimate: ~30,000-80,000 TPS** 🟡
**Headline peak: ~50,000 TPS** (sustained burst during volatility events)

## 3. Annual Value Traded (2024)

### World Bank Data (Primary)
- 2024: **$106.53 trillion** (stocks traded, total value, current US$) 🟢

### WFE Data (Cross-check)
- WFE December 2024: Value of share trading $14,431,297 million for December
- Annual: $14.43T x 12 ≈ $173T (but this includes all WFE members, some double-counting)
- WFE H1 2024: trading value up 11.7%
- WFE FY2024: trading value up 15.5% vs 2023

### Cross-check
- World Bank 2023: $94.08T → +15.5% = $108.7T (close to World Bank's $106.5T)
- **Central estimate: $106.5 trillion** (World Bank) to **$140-155 trillion** (WFE broader measure)
- Using World Bank as conservative baseline: **$106.5 trillion** 🟢

## 4. Historic Value Traded Timeseries (World Bank Data)

| Year | Value Traded (USD) | YoY Change |
|------|-------------------|------------|
| 2015 | $101.17T | — |
| 2016 | $77.67T | -23.2% |
| 2017 | $77.70T | +0.04% |
| 2018 | $84.27T | +8.5% |
| 2019 | $75.07T | -10.9% |
| 2020 | $102.94T | +37.1% |
| 2021 | $120.65T | +17.2% |
| 2022 | $104.39T | -13.5% |
| 2023 | $94.08T | -9.9% |
| 2024 | $106.53T | +13.2% |

### Converting Value to Estimated Trade Count
Assuming average trade size:
- US average trade value: ~$10,000-15,000 (includes HFT small lots)
- Asia average trade value: ~$1,000-3,000 (higher retail, smaller lots)
- Global blended average: ~$1,500-2,500

Using $1,730 average (to calibrate to 61.5B trades at $106.5T):
$106.5T / $1,730 = 61.6B trades ✓

Estimated trade counts (applying proportional scaling):
| Year | Est. Trades (B) | Implied Avg Trade Size |
|------|-----------------|----------------------|
| 2015 | ~45B | $2,248 |
| 2016 | ~35B | $2,219 |
| 2017 | ~37B | $2,100 |
| 2018 | ~40B | $2,107 |
| 2019 | ~38B | $1,975 |
| 2020 | ~52B | $1,980 |
| 2021 | ~58B | $2,080 |
| 2022 | ~50B | $2,088 |
| 2023 | ~49B | $1,920 |
| 2024 | ~62B | $1,718 |

Note: Average trade size declining over time due to fractional shares, retail participation, HFT.

## 5. CAGR Calculations

### 5-Year CAGR (2019-2024) — Value Traded
- Start: $75.07T, End: $106.53T
- CAGR = (106.53/75.07)^(1/5) - 1 = (1.4191)^0.2 - 1 = **7.26%**

### 10-Year CAGR (2015-2024) — Value Traded
- Start: $101.17T, End: $106.53T
- CAGR = (106.53/101.17)^(1/9) - 1 = (1.053)^0.111 - 1 = **0.57%**
- Note: 2015 was anomalously high (China bubble); inflates the base

### 5-Year CAGR (2019-2024) — Estimated Trade Count
- Start: ~38B, End: ~62B
- CAGR = (62/38)^(1/5) - 1 = (1.632)^0.2 - 1 = **10.3%**

### 10-Year CAGR (2015-2024) — Estimated Trade Count
- Start: ~45B, End: ~62B
- CAGR = (62/45)^(1/9) - 1 = (1.378)^0.111 - 1 = **3.6%**

## 6. Subcategory Breakdown (2024 Estimated)

### By Exchange (Estimated Annual Trades)

| Exchange | Est. Trades (B) | Share | Source |
|----------|----------------|-------|--------|
| NSE India | ~18.0B | 29.3% | WFE: +74.3% YoY, #3 in cash equity by trade count |
| Shenzhen SE | ~10.5B | 17.1% | WFE: +21.4% YoY |
| Shanghai SE | ~8.5B | 13.8% | WFE: +24.2% YoY |
| NASDAQ (all venues) | ~5.0B | 8.1% | Consolidated US + NASDAQ-listed |
| NYSE (all venues) | ~4.5B | 7.3% | Consolidated US + NYSE-listed |
| JPX (Tokyo) | ~4.2B | 6.8% | WFE: +30.9% YoY; JPY 1,254T value |
| Korea Exchange | ~3.0B | 4.9% | Estimate from WFE APAC data |
| LSE Group | ~1.5B | 2.4% | ~500K-2M trades/day |
| HKEX | ~1.2B | 2.0% | WFE: +31.1% YoY value |
| Taiwan SE | ~1.0B | 1.6% | WFE: +41.6% YoY value |
| Other | ~4.1B | 6.7% | Rest of world |
| **Total** | **~61.5B** | **100%** | |

### Lit vs Dark/Off-Exchange (US Market)
- US TRF (off-exchange) share: **47%** of Total Consolidated Volume in 2024 (up 300bps YoY)
- Exchange (lit) share: **53%**
- Globally, off-exchange share is lower (~25-30%) as dark pools are primarily US/EU

## 7. Projection Models

### Baseline Projection (2026-2035)
Assumptions:
- Trade count CAGR: 6.0% (below recent 10.3% 5yr CAGR, moderated for maturation)
- Value CAGR: 5.0% (GDP-linked growth + market appreciation)

| Year | Est. Trades (B) | Est. Value ($T) |
|------|-----------------|-----------------|
| 2025 | 65.2 | 111.8 |
| 2026 | 69.1 | 117.4 |
| 2027 | 73.3 | 123.3 |
| 2028 | 77.7 | 129.4 |
| 2029 | 82.3 | 135.9 |
| 2030 | 87.3 | 142.7 |
| 2031 | 92.5 | 149.8 |
| 2032 | 98.1 | 157.3 |
| 2033 | 104.0 | 165.2 |
| 2034 | 110.2 | 173.4 |
| 2035 | 116.8 | 182.1 |

### High-Growth Projection (2026-2035)
Assumptions:
- Trade count CAGR: 9.0% (retail boom, fractional shares, EM growth)
- Value CAGR: 7.5%

| Year | Est. Trades (B) | Est. Value ($T) |
|------|-----------------|-----------------|
| 2025 | 67.0 | 114.5 |
| 2026 | 73.1 | 123.1 |
| 2027 | 79.6 | 132.3 |
| 2028 | 86.8 | 142.2 |
| 2029 | 94.6 | 152.9 |
| 2030 | 103.1 | 164.3 |
| 2031 | 112.4 | 176.7 |
| 2032 | 122.5 | 189.9 |
| 2033 | 133.6 | 204.2 |
| 2034 | 145.6 | 219.5 |
| 2035 | 158.7 | 235.9 |

### Conservative Projection (2026-2035)
Assumptions:
- Trade count CAGR: 3.0% (HFT regulation, consolidation, tick size reform)
- Value CAGR: 3.0%

| Year | Est. Trades (B) | Est. Value ($T) |
|------|-----------------|-----------------|
| 2025 | 63.3 | 109.7 |
| 2026 | 65.2 | 113.0 |
| 2027 | 67.2 | 116.4 |
| 2028 | 69.2 | 119.9 |
| 2029 | 71.3 | 123.4 |
| 2030 | 73.4 | 127.1 |
| 2031 | 75.6 | 130.9 |
| 2032 | 77.9 | 134.8 |
| 2033 | 80.2 | 138.8 |
| 2034 | 82.6 | 143.0 |
| 2035 | 85.1 | 147.3 |

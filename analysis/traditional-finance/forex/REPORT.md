# Foreign Exchange (FX) — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #4
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One FX trade (spot, forward, swap, or option) executed between two counterparties

---

## Executive Summary

The global foreign exchange market is the largest financial market in the world by daily turnover, reaching **$9.6 trillion per day** in April 2025 according to the BIS Triennial Survey — up 28% from $7.5 trillion in 2022. However, FX is a **high-value, low-count** market: the average ticket size is extremely large (estimated $3-5 million for interbank trades), meaning transaction counts are modest relative to the enormous dollar volumes. We estimate approximately **2-4 million trades per day** globally, yielding an average TPS of roughly **23-46**.

FX swaps remain the dominant instrument at $4.0 trillion/day (42% of total), but the most notable shift in 2025 was the doubling of FX options turnover and substantial growth in outright forwards. The US dollar remains one side of 88% of all trades, but the euro gained significant share.

---

## 1. Current TPS (2024/2025)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS (est. 2024) | **~35** | 🔴 Low |
| Peak TPS (est.) | **~140** | 🔴 Low |
| Daily volume (value) | $9.6T (Apr 2025) | 🟢 High |
| Daily transaction count (est.) | ~3 million trades | 🔴 Low |
| Annual volume (est. 2024) | ~750 million trades | 🔴 Low |
| Annual value (est. 2024) | ~$2,200T | 🟡 Medium |

**Methodology**: BIS reports $9.6T daily turnover (April 2025) but does NOT report transaction counts. We estimate daily trade count from two convergent approaches:

1. **CLS data**: CLS settles ~500,000 FX trades/day and covers roughly 18-20% of global FX transactions by count (though ~55% by value, as CLS handles larger institutional trades). This implies ~2.5-2.8M total trades/day.
2. **Average ticket size**: Industry estimates suggest average FX trade sizes of $3-5M across all participants. At $9.6T/day and $3.2M average: ~3M trades/day.

Central estimate: **~3 million trades/day**. TPS = 3,000,000 / 86,400 = **~35 TPS** (FX trades 24 hours across global time zones, with ~23.5 effective hours).

**Sources**: [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25_fx.htm), [CLS Group Trade Volume](https://www.cls-group.com/news/fx-trade-volume-report/)

---

## 2. Annual Volume (2024)

| Metric | Value | Confidence | Source |
|--------|-------|------------|--------|
| Daily turnover (value) | $7.5T (2022 survey) | 🟢 High | [BIS](https://www.bis.org/statistics/rpfx22_fx.htm) |
| Daily turnover (value, 2025 survey) | $9.6T | 🟢 High | [BIS](https://www.bis.org/statistics/rpfx25_fx.htm) |
| Interpolated 2024 daily turnover | ~$8.5T | 🟡 Medium | Linear interpolation |
| Annual trading days | ~252 | — | — |
| Annual value (est. 2024) | ~$2,142T | 🟡 Medium | Derived |
| Annual trade count (est. 2024) | ~750M | 🔴 Low | Derived |

### Instrument Breakdown (April 2025)

| Instrument | Daily Turnover | Share | Change vs 2022 |
|-----------|---------------|-------|-----------------|
| FX Spot | $3.0T | 31% | +36% |
| FX Swaps | $4.0T | 42% | +5% |
| Outright Forwards | $1.8T | 19% | +62% |
| FX Options | $0.8T | 8% | +100%+ |
| **Total** | **$9.6T** | **100%** | **+28%** |

**Key facts**:
- FX swaps remain the largest instrument but their share dropped from 51% to 42% as other instruments grew faster
- Options turnover more than doubled since 2022
- Forward trading surged 62%, driven by hedging demand from emerging-market volatility

---

## 3. Historic Trend (BIS Triennial Survey)

| Survey Year | Daily Turnover | Growth vs Prior | Implied Annual Value |
|-------------|---------------|-----------------|---------------------|
| 2001 | $1.2T | — | ~$302T |
| 2004 | $1.9T | +58% | ~$479T |
| 2007 | $3.3T | +74% | ~$832T |
| 2010 | $4.0T | +21% | ~$1,008T |
| 2013 | $5.3T | +33% | ~$1,336T |
| 2016 | $5.1T | -4% | ~$1,285T |
| 2019 | $6.6T | +29% | ~$1,663T |
| 2022 | $7.5T | +14% | ~$1,890T |
| 2025 | $9.6T | +28% | ~$2,419T |

**Key observation**: FX turnover has grown ~800% since 2001. The only decline was 2013-2016, coinciding with tighter post-crisis regulation and reduced dealer risk appetite. Growth reaccelerated from 2016, driven by electronic trading, retail FX, and emerging-market currency activity.

---

## 4. Growth Rate Analysis

| Period | CAGR (by value) | Notes |
|--------|-----------------|-------|
| 2001-2025 (24 years) | ~8.9% | Long-run growth |
| 2010-2025 (15 years) | ~6.0% | Post-crisis era |
| 2019-2025 (6 years) | ~6.4% | Recent trajectory |
| 2022-2025 (3 years) | ~8.6% | Latest survey period |

---

## 5. Projections

### 5.1 Baseline (CAGR 6%)

| Year | Daily Turnover (est.) | Annual Value (est.) | Est. Daily Trades | Est. TPS |
|------|-----------------------|---------------------|--------------------|----------|
| 2025 | $9.6T | $2,419T | 3.0M | 35 |
| 2030 | $12.8T | $3,226T | 4.0M | 46 |
| 2035 | $17.1T | $4,309T | 5.3M | 62 |

### 5.2 High Growth (CAGR 9%)

| Year | Daily Turnover (est.) | Annual Value (est.) | Est. Daily Trades | Est. TPS |
|------|-----------------------|---------------------|--------------------|----------|
| 2025 | $9.6T | $2,419T | 3.0M | 35 |
| 2030 | $14.8T | $3,729T | 4.6M | 53 |
| 2035 | $22.8T | $5,746T | 7.1M | 82 |

### 5.3 Conservative (CAGR 3%)

| Year | Daily Turnover (est.) | Annual Value (est.) | Est. Daily Trades | Est. TPS |
|------|-----------------------|---------------------|--------------------|----------|
| 2025 | $9.6T | $2,419T | 3.0M | 35 |
| 2030 | $11.1T | $2,797T | 3.5M | 40 |
| 2035 | $12.9T | $3,251T | 4.0M | 47 |

**Scenario rationale**:
- **Baseline**: Continues the 15-year post-crisis trend (~6% CAGR). Electronic trading and EM currency growth sustain expansion.
- **High Growth**: Retail FX explosion, crypto-fiat conversion flows, Asian currency internationalization (RMB).
- **Conservative**: Regulatory tightening, FX consolidation, bilateral netting reduces gross turnover.

---

## 6. Key Findings

1. **FX is the world's largest market by value but relatively low-frequency by transaction count.** At ~35 TPS, it is orders of magnitude below payment systems and even below equity markets.

2. **The 2025 BIS Triennial Survey shows $9.6T/day**, a 28% jump over 2022, driven by forwards (+62%), options (doubled), and spot (+36%).

3. **Transaction count is the weakest data point.** BIS and most FX data sources report value turnover, not trade counts. Our ~3M trades/day estimate is triangulated from CLS settlement data and average ticket size analysis.

4. **FX swaps remain dominant** but lost share (51% to 42%), while forwards and options gained significantly — reflecting increased hedging demand.

5. **The USD remains ubiquitous** (one side of 88% of trades) but the euro gained share in interest rate derivatives, suggesting potential long-term diversification.

6. **Double-counting note**: FX derivatives (swaps, forwards, options) overlap with the OTC Derivatives category. Per project taxonomy rules, we count them here as FX transactions and note the overlap with OTC derivatives.

---

## 7. Data Quality & Limitations

- **Transaction count is estimated, not observed**: The BIS does not publish FX trade counts. Our estimate is derived from CLS data and average ticket size assumptions. Confidence: 🔴 Low.
- **Survey methodology**: BIS triennial data is collected in April only and extrapolated. Actual daily turnover varies by month and market conditions.
- **Interpolation between surveys**: 2024 values are interpolated between 2022 ($7.5T) and 2025 ($9.6T) surveys.
- **Double-counting risk**: Some FX activity (especially FX swaps used for funding) may represent the same economic exposure counted multiple times.
- **Retail FX**: High-frequency retail FX platforms (e.g., IG, Plus500) add millions of small trades that may inflate count estimates but are small in value terms.

---

## 8. Sources

1. [BIS Triennial Survey 2025 — FX Turnover](https://www.bis.org/statistics/rpfx25_fx.htm)
2. [BIS Triennial Survey 2022 — FX Turnover](https://www.bis.org/statistics/rpfx22_fx.htm)
3. [BIS Press Release — $9.6T daily (Sept 2025)](https://www.bis.org/press/p250930.htm)
4. [CLS Group — FX Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/)
5. [CLS Group — December 2024 Trading Activity](https://www.cls-group.com/news/cls-fx-trading-activity-december-2024/)
6. [BIS Triennial Survey Overview](https://data.bis.org/topics/DER)
7. [BestBrokers — Forex Daily Trading Volume Statistics 2026](https://www.bestbrokers.com/forex-trading/forex-daily-trading-volume/)

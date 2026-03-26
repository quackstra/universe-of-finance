# Exchange-Traded Derivatives (ETD)

> **Category**: Traditional Finance | **Priority**: #3
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One standardised futures or options contract traded on a regulated exchange

---

## Executive Summary

Exchange-traded derivatives reached a staggering **205.34 billion contracts** in 2024, up 51% year-over-year and marking the sixth consecutive annual record ([FIA](https://www.fia.org/fia/articles/2024-annual-etd-volume-review)). This translates to an estimated **~9,500 average TPS** across global exchanges, with peak-day spikes potentially reaching **~57,000 TPS**.

The story of modern ETD is really the story of India. The National Stock Exchange of India alone accounts for the vast majority of global volume through equity index options, having transformed from a minor player to the world's largest derivatives exchange in just five years. Options now represent **86% of all contracts traded**, up from 45% in 2020.

At approximately **$3,700 trillion in annual notional turnover**, ETD is one of the largest transaction categories in the Universe of Finance by value, though heavily skewed toward interest rate products in notional terms.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS (2024) | **~9,500** | 🟡 Medium |
| Peak TPS estimate | **~57,000** | 🔴 Low |
| Annual contracts traded | 205.34 billion | 🟢 High |
| Average daily volume | ~815 million contracts | 🟢 High |

**Methodology**: 205.34B contracts / (252 trading days x 21.6h weighted effective hours x 3600s) = ~9,505 TPS. Peak estimated at 6x average based on Indian expiry-day concentration patterns. See [calculations](workings/calculations.md).

**Sources**: [FIA Annual Review 2024](https://www.fia.org/fia/articles/2024-annual-etd-volume-review), [WFE FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)

---

## 2. Annual Volume (2024)

| Source | Total Volume | Futures | Options |
|--------|-------------|---------|---------|
| FIA | **205.34B** | 28.22B | 177.12B |
| WFE | **180.22B** | 26.92B | 153.30B |

The FIA-WFE gap (~25B contracts) is due to FIA covering 85 exchanges in 33 countries versus WFE's member-only universe. FIA is used as the primary source throughout.

**Key facts**:
- Options volume grew **63.8%** YoY; futures grew just **1.2%** ([FIA](https://www.fia.org/fia/articles/2024-annual-etd-volume-review))
- Open interest at year-end: **1.23 billion contracts** ([FIA](https://www.fia.org/fia/articles/2024-annual-etd-volume-review))
- The majority of growth came from equity index options, primarily on India's NSE

---

## 3. Annual Notional Value

| Component | Daily Turnover | Annual (est.) | Confidence | Source |
|-----------|---------------|---------------|------------|--------|
| Interest rate ETD | $12.65T/day | ~$3,226T | 🟢 High | [BIS](https://www.bis.org/statistics/extderiv.htm) |
| FX ETD | $0.185T/day | ~$47T | 🟢 High | [BIS](https://www.bis.org/statistics/extderiv.htm) |
| Equity ETD | — | ~$262T | 🟡 Medium | Derived estimate |
| Commodity ETD | — | ~$155T | 🟡 Medium | Derived estimate |
| **Total** | **~$14.4T/day** | **~$3,689T** | 🟡 Medium | Composite |

Interest rate futures and options dominate in notional terms (87% of total), even though they represent only ~5% of contract volume. This is because individual IR contracts (e.g., CME Treasury futures at $100K-$200K face value) carry far larger notional amounts than Indian equity index options (~$1K-2K notional each).

---

## 4. Historic Timeseries (2015-2024)

| Year | Total (B) | Futures (B) | Options (B) | YoY Growth | Source |
|------|-----------|-------------|-------------|------------|--------|
| 2015 | 24.78 | — | — | — | [FIA](https://www.fia.org/fia/articles/2015-fia-annual-futures-and-options-volume-survey-asia-takes-lead) |
| 2016 | 25.22 | — | — | +1.8% | [FIA](https://www.fia.org/marketvoice/articles/2016-annual-volume-survey) |
| 2017 | 25.20 | — | — | -0.1% | [FIA](https://www.fia.org/fia/articles/total-2017-volume-252-billion-contracts-down-01-2016) |
| 2018 | 30.28 | — | — | +20.2% | [FIA](https://www.fia.org/fia/articles/fia-releases-annual-trading-statistics-showing-record-etd-volume-2018) |
| 2019 | 34.47 | — | — | +13.8% | [FIA](https://www.fia.org/fia/articles/record-year-derivatives) |
| 2020 | 46.77 | 25.55 | 21.22 | +35.7% | [FIA](https://www.fia.org/fia/articles/global-futures-and-options-trading-reaches-record-level-2020) |
| 2021 | 62.58 | 29.28 | 33.31 | +33.8% | [FIA](https://www.fia.org/fia/articles/global-futures-and-options-trading-hits-another-record-2021) |
| 2022 | 83.85 | 29.32 | 54.53 | +34.0% | [Statista/FIA](https://www.statista.com/statistics/377025/global-futures-and-options-volume/) |
| 2023 | 137.31 | 29.10 | 108.20 | +63.8% | [FIA](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023) |
| 2024 | 205.34 | 28.22 | 177.12 | +49.5% | [FIA](https://www.fia.org/fia/articles/2024-annual-etd-volume-review) |

**Key observation**: Futures volume has been essentially flat at ~28-29B contracts since 2021. ALL growth is in options, driven almost entirely by Indian equity index options on NSE.

---

## 5. Subcategory Breakdown (2024)

### By Asset Class (WFE data)

| Asset Class | Share of Volume | YoY Change | Dominant Exchange |
|-------------|----------------|------------|-------------------|
| Equity (index + single stock) | **~85%** | +50.2% | NSE India (97.7% of stock index options) |
| Interest Rate | ~5% | +15.4% | CME Group (49-53% global share) |
| ETF | ~4% | +25.8% | Nasdaq-US, Cboe, NYSE |
| Currency | ~3% | -56.5% | NSE India, B3, CME |
| Commodity | ~3% | -4.1% | Dalian, Zhengzhou, MCX India |

Source: [WFE FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)

### By Instrument Type

| Type | Volume (B) | Share | YoY Growth |
|------|-----------|-------|------------|
| Options | 177.12 | 86.3% | +63.8% |
| Futures | 28.22 | 13.7% | +1.2% |

### By Region (WFE)

| Region | Volume (B) | Share | YoY Growth |
|--------|-----------|-------|------------|
| APAC | 142.66 | 79.2% | +47.8% |
| Americas | 31.60 | 17.5% | +14.2% |
| EMEA | 5.95 | 3.3% | +4.8% |

### Top Exchanges (2023 FIA Rankings)

| Rank | Exchange | Volume (B) | Notes |
|------|----------|-----------|-------|
| 1 | NSE India | 84.8 | World's largest by contract volume |
| 2 | B3 (Brazil) | 8.3 | Strong in IR, FX, equity |
| 3 | CME Group | 6.1 | Dominant in IR and crypto ETD |
| 4 | BSE India | 5.9 | Growing from low base |
| 5 | Cboe Global Markets | 3.71 | US equity/ETF options specialist |

Source: [FIA 2023 Rankings](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023)

Additional 2024 data points:
- **CME Group** 2024 ADV: 26.5 million contracts, up 9% ([CME](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html))
- **Eurex** 2024: 2.08 billion contracts, up 9% ([Deutsche Borse](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Full-year-and-December-2024-figures-at-Eurex-4250262))
- **CME Group** 2025 ADV: 28.1 million contracts, up 6% ([CME](https://www.cmegroup.com/media-room/press-releases/2026/1/05/cme_group_reportsrecordannualadvof281millioncontractsin2025up6ye.html))

---

## 6. Growth Rates

| Period | CAGR | Confidence |
|--------|------|------------|
| 5-year (2019-2024) | **42.8%** | 🟢 High |
| 9-year (2015-2024) | **26.4%** | 🟢 High |
| Futures only (2020-2024) | **2.5%** | 🟢 High |
| Options only (2020-2024) | **70.0%** | 🟢 High |

**Critical context**: The headline CAGR of 42.8% is almost entirely explained by the explosion of Indian equity index options from ~10B contracts in 2019 to ~150B+ in 2024. This is a one-time structural shift driven by:

1. **Weekly expiry contracts** introduced by NSE (multiplied expiry-day trading opportunities)
2. **Mobile trading apps** (Zerodha, Groww, Angel One) bringing millions of retail traders to F&O
3. **Small lot sizes** ($500-1,500 per contract) making options accessible to retail
4. **Zero/low brokerage models** reducing friction

Futures growth has been essentially flat at ~2.5% CAGR over the same period, reflecting the mature, institutional nature of futures markets.

---

## 7. Baseline Projection (2026-2035)

**Scenario**: Steady growth — options growth moderates as Indian regulations bite, futures stable.
**CAGR**: 12%

| Year | Volume (B) | Estimated Avg TPS |
|------|-----------|-------------------|
| 2025 | 230 | 10,645 |
| 2026 | 258 | 11,922 |
| 2027 | 288 | 13,353 |
| 2028 | 323 | 14,955 |
| 2029 | 362 | 16,749 |
| 2030 | **405** | **18,760** |
| 2031 | 454 | 21,011 |
| 2032 | 508 | 23,533 |
| 2033 | 569 | 26,357 |
| 2034 | 638 | 29,519 |
| 2035 | **714** | **33,062** |

**Key assumptions**: SEBI lot-size increases and weekly expiry restrictions reduce India options growth from ~60% to ~15%. Futures grow at ~5%. No major new markets open. See [assumptions](workings/assumptions.md).

---

## 8. High-Growth Projection

**Scenario**: Retail derivatives access expands globally + crypto ETD mainstreaming + ETF options boom continues.
**CAGR**: 18%

| Year | Volume (B) | Estimated Avg TPS |
|------|-----------|-------------------|
| 2030 | **554** | **25,653** |
| 2035 | **1,268** | **58,686** |

**Drivers**:
- Retail derivatives platforms launch in 10+ new markets (Vietnam, Philippines, Kenya, Nigeria, Mexico, Colombia)
- Bitcoin/Ethereum futures and options become standard products on CME, Cboe, Eurex
- US ETF options growth sustains 25%+ annual rates
- AI/algorithmic trading increases turnover velocity
- No major regulatory clampdown globally

---

## 9. Conservative Projection

**Scenario**: Regulatory tightening globally, especially in India.
**CAGR**: 5%

| Year | Volume (B) | Estimated Avg TPS |
|------|-----------|-------------------|
| 2030 | **275** | **12,737** |
| 2035 | **351** | **16,256** |

**Drivers**:
- SEBI intensifies restrictions — India volume drops 30-50% from peak
- China maintains restrictions on retail derivatives access
- US financial transaction tax proposals gain traction
- European MiFID III adds position limits and reporting burden
- Crypto derivatives face regulatory hostility from SEC/CFTC

---

## Key Risks and Caveats

1. **India concentration risk**: ~79% of global ETD volume comes from APAC (primarily India). A single regulatory decision by SEBI could move the global number by 20-30% overnight.

2. **Contract volume ≠ economic significance**: A $1,000 Nifty option and a $200,000 Treasury future each count as "one contract." By notional value, interest rate derivatives dwarf equity in importance.

3. **FIA vs WFE discrepancy**: The two primary sources disagree by ~25B contracts (205B vs 180B). This analysis uses FIA as primary; all figures should be understood with a ±12% measurement uncertainty band.

4. **Peak TPS is speculative**: Without microsecond-level exchange data, the 57,000 peak TPS is a modelled estimate, not an observed measurement.

---

## Data Quality Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| Data quality | 90/100 | FIA and WFE are authoritative; BIS provides notional data |
| Completeness | 85/100 | Strong on volume, weaker on equity/commodity notional |
| Methodology | 80/100 | TPS derivation requires assumptions; well-documented |
| Projections | 75/100 | High uncertainty due to India regulatory trajectory |
| Presentation | 85/100 | Comprehensive breakdown by all relevant dimensions |
| **Weighted Total** | **84/100** | |

*Weights: Data 0.30, Completeness 0.25, Methodology 0.20, Projections 0.15, Presentation 0.10*

---

## Sources

- [FIA ETD Volume Reports](https://www.fia.org/etd-volume-reports)
- [FIA 2024 Annual ETD Volume Review](https://www.fia.org/fia/articles/2024-annual-etd-volume-review)
- [FIA 2023 Annual Volume Survey](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023)
- [WFE FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)
- [WFE Statistics Portal](https://www.world-exchanges.org/our-work/statistics)
- [BIS Exchange-Traded Derivatives Statistics](https://www.bis.org/statistics/extderiv.htm)
- [BIS Data Portal — XTD](https://data.bis.org/topics/XTD_DER)
- [CME Group 2024 Annual Volume](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html)
- [CME Group 2025 Annual Volume](https://www.cmegroup.com/media-room/press-releases/2026/1/05/cme_group_reportsrecordannualadvof281millioncontractsin2025up6ye.html)
- [Eurex 2024 Figures](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Full-year-and-December-2024-figures-at-Eurex-4250262)
- [FIA — India Equity Derivatives Explainer](https://www.fia.org/marketvoice/articles/explainer-meteoric-rise-indias-equity-derivatives-volume)
- [Crypto Derivatives Statistics](https://coinlaw.io/cryptocurrency-derivatives-market-statistics/)

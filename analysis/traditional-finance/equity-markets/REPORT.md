# Equity Markets (Stock Exchanges) — Transaction Analysis

**Category Priority**: #6 | **Sector**: Traditional Finance
**Date**: 2026-03-26 | **Confidence**: 🟡 Medium (derived from multiple triangulated sources)

---

## Executive Summary

Global equity markets executed an estimated **61.5 billion trades** in 2024, valued at **$106.5 trillion** ([World Bank](https://data.worldbank.org/indicator/CM.MKT.TRAD.CD)). This represents an average throughput of **~3,500 TPS** during trading hours, with peak bursts reaching **~50,000 TPS** during volatility events. The 2024 figures reflect a 26.5% surge in trade count year-over-year, driven overwhelmingly by Asia-Pacific markets — particularly India (+74.3%), Japan (+30.9%), and China (+21-24%) — as retail participation and government stimulus reshaped global trading patterns.

---

## 1. Current TPS (2024/2025)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average Global TPS | **~3,500** | 🟡 Medium |
| Peak Sustained TPS (busiest hour) | **~30,000** | 🟡 Medium |
| Peak Burst TPS (opening 30 min, volatility day) | **~80,000** | 🔴 Low |
| Headline Peak Estimate | **~50,000** | 🟡 Medium |

**Methodology**: 61.5B annual trades / ~252 trading days / ~16 effective global trading hours / 3,600 seconds = ~3,500 TPS average. Peak estimates assume 3x average volume on volatility days with 20% concentration in the first 30 minutes. See [workings/calculations.md](workings/calculations.md) for full derivation.

**Context**: The UTP SIP (US market data processor) can handle [~5.6 million messages/second](https://www.sec.gov/about/speed-equity-markets), providing massive headroom above actual trade rates. Individual exchange matching engines operate at microsecond latencies.

---

## 2. Annual Volume (2024)

| Metric | Value | Source |
|--------|-------|--------|
| Total equity trades (2024) | **~61.5 billion** | Triangulated from [WFE](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024) monthly data, H1 APAC totals, and 2023 baseline + growth |
| WFE December 2024 monthly | 5.095B trades | [WFE Dashboard](https://focus.world-exchanges.org/issue/december-2024/dashboard) |
| WFE Dec 2024 YoY growth | +26.53% | [WFE Dashboard](https://focus.world-exchanges.org/issue/december-2024/dashboard) |
| APAC H1 2024 trades | 18.68B | [WFE H1 Report](https://www.world-exchanges.org/news/articles/wfe-data-trading-value-and-volumes-surge-investors-flock-markets) |

The 61.5B figure is a **derived estimate** (🟡) — WFE does not publish a single annual global trade count in its public reports. It was triangulated from three independent methods (see [calculations](workings/calculations.md)) that converged on 59.9B-67.2B.

A bottom-up sum of individual exchanges yields ~66.9B before adjustment, or ~61.9B after correcting for NSE India's equity-vs-derivatives classification overlap — reconciling to within 0.6% of the 61.5B estimate. See [exchange breakdown workings](workings/exchange-breakdown.md) for the full decomposition.

---

## 3. Annual Value (2024)

| Metric | Value | Source |
|--------|-------|--------|
| Total value traded (World Bank) | **$106.53 trillion** | [World Bank](https://data.worldbank.org/indicator/CM.MKT.TRAD.CD) 🟢 |
| Total through WFE members (broader) | ~$155 trillion (EOB) | [WFE](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024) |
| YoY value growth | +15.5% | [WFE FY2024](https://www.world-exchanges.org/news/articles/wfe-fy24-market-data-americas-region-leading-global-markets-despite-lowest-level-ipos-worldwide-last-5-years) |
| Global equity market cap | $125.71 trillion | [WFE](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024) |

The gap between World Bank ($106.5T) and WFE (~$155T) reflects methodology: World Bank counts matched share trades; WFE's broader EOB measure includes additional trading activity across all member venues.

---

## 4. Historic Timeseries (2015-2024)

| Year | Value Traded ($T) | YoY Change | Est. Trades (B) | Key Events |
|------|-------------------|------------|-----------------|------------|
| 2015 | $101.17 | — | ~45 | China stock market bubble + crash |
| 2016 | $77.67 | -23.2% | ~35 | Post-China correction, Brexit vote |
| 2017 | $77.70 | +0.04% | ~37 | Low volatility, steady recovery |
| 2018 | $84.27 | +8.5% | ~40 | Volatility returns, trade war fears |
| 2019 | $75.07 | -10.9% | ~38 | Trade war dampens volumes |
| 2020 | $102.94 | +37.1% | ~52 | COVID panic + stimulus + retail boom |
| 2021 | $120.65 | +17.2% | ~58 | Meme stocks, SPAC mania, peak retail |
| 2022 | $104.39 | -13.5% | ~50 | Rate hikes, inflation, Ukraine |
| 2023 | $94.08 | -9.9% | ~49 | Continued tightening, AI rally in H2 |
| 2024 | $106.53 | +13.2% | ~62 | India/China surge, AI mega-cap rally |

Source: [World Bank](https://data.worldbank.org/indicator/CM.MKT.TRAD.CD) (value); trade counts estimated (see [calculations](workings/calculations.md)).

---

## 5. Subcategory Breakdown (2024)

### By Exchange (Estimated Trade Count)

| Exchange | Est. Trades (B) | Share | YoY Growth | Notes |
|----------|----------------|-------|------------|-------|
| [NSE India](https://www.nseindia.com/) | ~18.0 | 29.3% | +74.3% | #3 globally by trade count; massive retail base |
| [Shenzhen SE](https://www.szse.cn/English/) | ~10.5 | 17.1% | +21.4% | Stimulus-driven retail surge |
| [Shanghai SE](https://english.sse.com.cn/) | ~8.5 | 13.8% | +24.2% | Record 3.45T yuan combined day (Oct 2024) |
| [NASDAQ](https://www.nasdaqtrader.com/) | ~5.0 | 8.1% | — | All US venues for NASDAQ-listed |
| [NYSE](https://www.nyse.com/) | ~4.5 | 7.3% | — | ADV ~1.54B shares at ~$80.6B |
| [JPX](https://www.jpx.co.jp/english/) | ~4.2 | 6.8% | +30.9% | JPY 1,254T equity value (all-time high) |
| Korea Exchange | ~3.0 | 4.9% | — | Estimated |
| [LSE Group](https://www.lseg.com/) | ~1.5 | 2.4% | +8.5% | 500K-2M trades/day |
| [HKEX](https://www.hkex.com.hk/) | ~1.2 | 2.0% | +31.1% | Stimulus spillover from mainland |
| Taiwan SE | ~1.0 | 1.6% | +41.6% | AI/semiconductor driven |
| Other | ~4.1 | 6.7% | — | All remaining exchanges |
| **Total** | **~61.5** | **100%** | **+26.5%** | |

### By Region

| Region | Est. Trades (B) | Share | YoY Growth |
|--------|----------------|-------|------------|
| APAC | ~40.0 | 65% | [+47.8%](https://www.world-exchanges.org/news/articles/wfe-fy24-market-data-americas-region-leading-global-markets-despite-lowest-level-ipos-worldwide-last-5-years) |
| Americas | ~13.5 | 22% | — |
| EMEA | ~8.0 | 13% | [+4.8%](https://www.world-exchanges.org/news/articles/wfe-fy24-market-data-americas-region-leading-global-markets-despite-lowest-level-ipos-worldwide-last-5-years) |

### Lit vs Dark / Off-Exchange (US Market)

| Venue Type | Share of US TCV | Trend |
|-----------|----------------|-------|
| Exchange (lit) | [53%](https://ir.cboe.com/news/news-details/2025/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2024/default.aspx) | Declining |
| Off-exchange (TRF/dark) | [47%](https://ir.cboe.com/news/news-details/2025/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2024/default.aspx) | +300bps YoY |

Globally, off-exchange share is lower (~25-30%) as dark pools are primarily a US and EU phenomenon. FINRA publishes [ATS weekly volume data](https://www.finra.org/investors/insights/where-do-stocks-trade) with a 2-4 week lag.

---

## 6. Growth Rates

| Metric | Period | CAGR |
|--------|--------|------|
| Value traded | 5-year (2019-2024) | **7.26%** |
| Value traded | 10-year (2015-2024) | **0.57%** |
| Trade count (est.) | 5-year (2019-2024) | **~10.3%** |
| Trade count (est.) | 10-year (2015-2024) | **~3.6%** |

The divergence between value and trade-count growth reflects declining average trade sizes — driven by [fractional share adoption](https://rsmus.com/insights/industries/financial-services/capital-markets-retail-investor-growth.html) (>10% of transactions in 2023/24), HFT order fragmentation, and massive retail participation in India and China.

The 10-year value CAGR is suppressed by the anomalously high 2015 base (China stock market bubble inflated volumes).

---

## 7. Baseline Projection (2026-2035)

**Assumptions**: 6.0% trade count CAGR, 5.0% value CAGR. Moderate emerging market growth, fractional shares become standard, no major regulatory disruption to HFT.

| Year | Est. Trades (B) | Est. Value ($T) | TPS (avg) |
|------|-----------------|-----------------|-----------|
| 2025 | 65.2 | 111.8 | ~3,700 |
| 2030 | 87.3 | 142.7 | ~4,960 |
| 2035 | 116.8 | 182.1 | ~6,640 |

---

## 8. High-Growth Projection (2026-2035)

**Assumptions**: 9.0% trade count CAGR, 7.5% value CAGR. India demat account explosion, fractional shares go global, tokenized equities reduce friction, [emerging markets grow from 27% to 35% of global equity cap by 2030](https://www.goldmansachs.com/insights/articles/emerging-stock-markets-projected-to-overtake-the-us-by-2030), retail participation rises to 40-50% globally, 24/7 trading gains traction.

| Year | Est. Trades (B) | Est. Value ($T) | TPS (avg) |
|------|-----------------|-----------------|-----------|
| 2025 | 67.0 | 114.5 | ~3,810 |
| 2030 | 103.1 | 164.3 | ~5,860 |
| 2035 | 158.7 | 235.9 | ~9,020 |

Key catalysts:
- [Retail investors deployed $1.3B/day in H1 2025](https://rsmus.com/insights/industries/financial-services/capital-markets-retail-investor-growth.html), up 32.6% YoY
- India's NSE is already #3 globally by trade count and grew 74% in 2024
- Fractional shares accounted for [>10% of total transactions](https://rsmus.com/insights/industries/financial-services/capital-markets-retail-investor-growth.html) in 2023/2024

---

## 9. Conservative Projection (2026-2035)

**Assumptions**: 3.0% trade count CAGR, 3.0% value CAGR. SEC/EU HFT regulation reduces algorithmic volume, [PFOF ban in EU](https://www.nortonrosefulbright.com/en/knowledge/publications/ad797a13/fractional-shares-an-update-on-the-regulatory-approach) dampens retail activity, tick size reforms reduce fragmentation, [compliance costs ($1.5B+/year for HFT firms)](https://www.congress.gov/crs-product/R43608) drive exits, geopolitical fragmentation reduces cross-border trading.

| Year | Est. Trades (B) | Est. Value ($T) | TPS (avg) |
|------|-----------------|-----------------|-----------|
| 2025 | 63.3 | 109.7 | ~3,600 |
| 2030 | 73.4 | 127.1 | ~4,170 |
| 2035 | 85.1 | 147.3 | ~4,840 |

---

## Key Structural Observations

1. **Asia dominates by trade count, not value**: APAC represents ~65% of global equity trades by count but a smaller share by value — reflecting the massive retail participation bases in India (~500M+ demat accounts) and China.

2. **The dark pool paradox**: In the US, nearly half (47%) of equity volume now trades off-exchange. This is a growing structural feature of developed markets that regulators are scrutinizing but unlikely to reverse.

3. **Average trade size is collapsing**: From ~$2,250 (2015) to ~$1,730 (2024), driven by fractional shares, HFT, and retail micro-trades. This means trade *count* is growing faster than trade *value* — a trend that will accelerate.

4. **India is the wild card**: NSE India's 74.3% trade count growth in 2024 is extraordinary. If sustained even at half that rate, India alone could add 5-10B trades/year by 2030.

5. **24/7 trading is coming**: NYSE has experimented with extended hours. If major exchanges move to round-the-clock trading, TPS averages drop (same volume over more hours) but annual volume likely increases as accessibility improves.

6. **Exchange-level decomposition validates the 61.5B total.** Summing 13 major exchanges and estimating Tier 2 gives ~66.9B raw, which adjusts to ~61.9B after isolating NSE India's equity cash trades from derivatives — a 0.6% match with the triangulated estimate. India (NSE + BSE) accounts for ~28% of global equity trades on just 4% of global market cap. See [exchange breakdown](workings/exchange-breakdown.md).

7. **Japan's 2024 resurgence is structural, not cyclical.** JPX's 30.9% trade count growth and record JPY 1,254T equity value reflect the Nikkei 225 hitting all-time highs for the first time since 1989. Corporate governance reforms (Tokyo Stock Exchange "name and shame" initiative for low-PBR companies) and BOJ policy shifts are driving sustained foreign investment flows.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Dark pool / off-exchange true volume**: In the US, ~47% of equity volume trades off-exchange (TRF/dark pools), but the exact number of discrete trades in dark pools vs. internalizers is not publicly decomposed in real time. FINRA ATS data has a 2-4 week lag.
- **India retail vs. institutional split**: NSE India is #3 globally by trade count, but the exact proportion of retail (individuals) vs. institutional (DII/FII) trades by count is not published at the granularity needed for TPS modeling. SEBI publishes monthly category-wise turnover, not trade counts.
- **China A-share retail dominance**: Retail investors are estimated to account for 60-80% of China A-share trading volume by count, but the Shanghai and Shenzhen exchanges do not publish a clean retail/institutional trade count split.
- **HFT share of trade count**: High-frequency trading generates a disproportionate share of order flow and trades, but the exact percentage varies by exchange and is not consistently reported globally.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Dark pool volume (US) | FINRA ATS weekly data + Cboe TRF market share reports | [FINRA ATS data](https://www.finra.org/investors/insights/where-do-stocks-trade) (2-4 week lag), Cboe monthly TCV reports | 🟡 Medium |
| Dark pool volume (EU) | MiFID II post-trade transparency data via ESMA | ESMA quarterly reports on dark trading caps (DVC) | 🟡 Medium |
| China A-share retail split | CSRC monthly investor statistics + SSE/SZSE turnover by account type | CSRC publishes new account openings; Wind database has category turnover | 🟡 Medium |
| India NSE retail explosion | SEBI monthly bulletin (category-wise turnover) + NSE broker-level data | SEBI data available with 1-month lag; demat account growth from CDSL/NSDL | 🟢 High (value) / 🟡 Medium (count) |
| HFT share of trades | SEC Rule 613 (CAT) data (not public) vs. academic estimates | Academic papers estimate 50-60% of US equity trades are HFT; no real-time source | 🔴 Low |
| Global trade count verification | Cross-check WFE monthly data × 12 vs. annual estimate | WFE publishes monthly dashboard with YoY trade count growth rates | 🟡 Medium |

### Key Modeling Questions
- What is the true ratio of trades-to-value across dark pools vs. lit exchanges? (Dark pools may have higher average trade sizes, meaning fewer trades per dollar)
- How should fractional share trades be counted? (One $5 fractional share purchase = one trade in the same way as a $500K block?)
- If 24/7 trading gains traction (NYSE has explored this), does total trade count increase or just spread across more hours?
- Can India's NSE sustain 40%+ trade count growth, or will SEBI lot-size and margin interventions (as seen in F&O) dampen equity cash market growth too?

### Reference Comparisons
- **India demat accounts**: 500M+ accounts (CDSL/NSDL combined), growing ~15M/month — comparable to China's 200M+ brokerage accounts but with much higher active trading rates
- **US retail participation**: Retail investors deployed $1.3B/day in H1 2025, up 32.6% YoY ([RSM US](https://rsmus.com/insights/industries/financial-services/capital-markets-retail-investor-growth.html))
- **Off-exchange trend**: US off-exchange share rose from ~35% (2019) to ~47% (2024); in January 2025, dark pools alone crossed 51.8% of volume for the first time ([Bloomberg](https://www.bloomberg.com/))
- **Goldman Sachs projection**: Emerging stock markets projected to overtake the US by market cap by 2030, driven by India, China, and other Asian markets

---

## Confidence Assessment

| Capsule | Confidence | Notes |
|---------|------------|-------|
| Annual value traded | 🟢 High | World Bank direct data |
| Historic timeseries (value) | 🟢 High | World Bank 10-year series |
| Annual trade count | 🟡 Medium | Triangulated estimate; no single authoritative source |
| Current TPS | 🟡 Medium | Derived from estimated trade count |
| Exchange breakdown | 🟡 Medium | Based on WFE growth rates applied to prior baselines |
| Growth rates | 🟡 Medium | Value CAGR is solid; trade count CAGR is estimated |
| Peak TPS | 🔴 Low | Highly dependent on assumptions about intraday distribution |
| Projections | 🔴 Low | Inherently speculative; three scenarios bound the range |

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
| Average TPS (est. 2024) | **~40** | 🟡 Medium |
| Peak TPS (est.) | **~160** | 🔴 Low |
| Daily volume (value) | $9.6T (Apr 2025) | 🟢 High |
| Daily transaction count (est.) | ~3.5 million trades | 🟡 Medium |
| Annual volume (est. 2024) | ~880 million trades | 🟡 Medium |
| Annual value (est. 2024) | ~$2,200T | 🟡 Medium |

**Methodology**: BIS reports $9.6T daily turnover (April 2025) but does NOT report transaction counts. We estimate daily trade count from **four convergent approaches**:

1. **CLS settlement data**: CLS settles an average of ~1 million payment instructions per day ([CLS Group](https://www.cls-group.com/products/settlement/clssettlement/)) across 18 currencies, representing ~$7T+ in daily settled value. CLS covers approximately 55% of global FX turnover by value but a smaller share by count (institutional bias toward larger trades). Peak day: 2.6 million instructions. Since each FX trade generates two payment instructions (one per leg), CLS settles ~500K unique trades/day. CLS market share by count is estimated at 15-20%, implying **2.5-3.3M total trades/day**.

2. **Average ticket size decomposition** (BIS methodology): The BIS Triennial Survey collects turnover by counterparty type. Using estimated average ticket sizes by segment:
   - Reporting dealer-to-dealer: ~$5-10M avg ticket → ~$2.5T/day ÷ $7.5M = ~333K trades
   - Dealer-to-other financial: ~$2-5M avg ticket → ~$5.5T/day ÷ $3.5M = ~1.57M trades
   - Dealer-to-non-financial: ~$0.5-2M avg ticket → ~$1.6T/day ÷ $1.25M = ~1.28M trades
   - **Subtotal: ~3.2M trades/day**

3. **Electronic platform volumes**: EBS (now CME) averaged $59.4B/day in 2024 ([The Full FX](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)). At an estimated $2-3M avg ticket for EBS, this implies ~20-30K trades/day on EBS alone. Electronic trading represents ~59% of global FX turnover ([BIS 2024](https://www.bis.org/publ/qtrpdf/r_qt1912g.pdf)), with the remainder voice/chat. Major electronic venues (EBS, Refinitiv Matching, Bloomberg, 360T, Cboe FX) collectively handle a significant share.

4. **Retail FX platforms**: Retail FX (eToro, OANDA, IG, Plus500, etc.) adds millions of small-value trades daily. Retail share of FX turnover is estimated at 3-5% by value but potentially 20-30% by count due to micro-lot sizes ($1K-$100K). This could add **0.5-1.5M trades/day** not captured in institutional estimates.

**Revised central estimate: ~3.5 million trades/day** (range: 2.5-5M). This is higher than our prior estimate of ~3M, reflecting better accounting for retail FX. TPS = 3,500,000 / 86,400 = **~40 TPS** (FX trades 24 hours across global time zones, with ~23.5 effective hours). Confidence upgraded from 🔴 Low to 🟡 Medium based on multi-source triangulation.

**Electronic vs voice split**: Voice Direct 25%, Electronic Direct 33%, Voice Indirect 13%, Electronic Indirect 26% of all FX products by turnover ([BIS/Coalition Greenwich 2024](https://www.greenwich.com/blog/voice-trading-relationships-and-better-e-support-vital-fx)). The e-ratio across all products stands at ~59%.

**Sources**: [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25_fx.htm), [CLS Group](https://www.cls-group.com/products/settlement/clssettlement/), [CLS Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/), [BIS User's Guide to Triennial Survey](https://www.bis.org/publ/qtrpdf/r_qt1012h.pdf)

---

## 2. Annual Volume (2024)

| Metric | Value | Confidence | Source |
|--------|-------|------------|--------|
| Daily turnover (value) | $7.5T (2022 survey) | 🟢 High | [BIS](https://www.bis.org/statistics/rpfx22_fx.htm) |
| Daily turnover (value, 2025 survey) | $9.6T | 🟢 High | [BIS](https://www.bis.org/statistics/rpfx25_fx.htm) |
| Interpolated 2024 daily turnover | ~$8.5T | 🟡 Medium | Linear interpolation |
| Annual trading days | ~252 | — | — |
| Annual value (est. 2024) | ~$2,142T | 🟡 Medium | Derived |
| Annual trade count (est. 2024) | ~880M | 🟡 Medium | Derived (3.5M/day × 252 days) |

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
| 2025 | $9.6T | $2,419T | 3.5M | 40 |
| 2030 | $12.8T | $3,226T | 4.7M | 54 |
| 2035 | $17.1T | $4,309T | 6.3M | 73 |

### 5.2 High Growth (CAGR 9%)

| Year | Daily Turnover (est.) | Annual Value (est.) | Est. Daily Trades | Est. TPS |
|------|-----------------------|---------------------|--------------------|----------|
| 2025 | $9.6T | $2,419T | 3.5M | 40 |
| 2030 | $14.8T | $3,729T | 5.4M | 63 |
| 2035 | $22.8T | $5,746T | 8.3M | 96 |

### 5.3 Conservative (CAGR 3%)

| Year | Daily Turnover (est.) | Annual Value (est.) | Est. Daily Trades | Est. TPS |
|------|-----------------------|---------------------|--------------------|----------|
| 2025 | $9.6T | $2,419T | 3.5M | 40 |
| 2030 | $11.1T | $2,797T | 4.1M | 47 |
| 2035 | $12.9T | $3,251T | 4.7M | 55 |

**Scenario rationale**:
- **Baseline**: Continues the 15-year post-crisis trend (~6% CAGR). Electronic trading and EM currency growth sustain expansion.
- **High Growth**: Retail FX explosion, crypto-fiat conversion flows, Asian currency internationalization (RMB).
- **Conservative**: Regulatory tightening, FX consolidation, bilateral netting reduces gross turnover.

---

## 6. Key Findings

1. **FX is the world's largest market by value but relatively low-frequency by transaction count.** At ~40 TPS, it is orders of magnitude below payment systems and even below equity markets.

2. **The 2025 BIS Triennial Survey shows $9.6T/day**, a 28% jump over 2022, driven by forwards (+62%), options (doubled), and spot (+36%).

3. **Transaction count confidence has been upgraded.** Our revised ~3.5M trades/day estimate is triangulated from four independent approaches: CLS settlement instructions, BIS counterparty-segment ticket-size decomposition, electronic platform volumes, and retail FX estimates. Confidence upgraded from 🔴 Low to 🟡 Medium.

4. **FX swaps remain dominant** but lost share (51% to 42%), while forwards and options gained significantly — reflecting increased hedging demand.

5. **The USD remains ubiquitous** (one side of 88% of trades) but the euro gained share in interest rate derivatives, suggesting potential long-term diversification.

6. **Double-counting note**: FX derivatives (swaps, forwards, options) overlap with the OTC Derivatives category. Per project taxonomy rules, we count them here as FX transactions and note the overlap with OTC derivatives.

---

## 7. Data Quality & Limitations

- **Transaction count is estimated, not observed**: The BIS does not publish FX trade counts. Our revised estimate is triangulated from four independent methods (CLS settlement, ticket-size decomposition, electronic venue ADV, and retail FX estimates). Confidence upgraded to 🟡 Medium.
- **Survey methodology**: BIS triennial data is collected in April only and extrapolated. Actual daily turnover varies by month and market conditions.
- **Interpolation between surveys**: 2024 values are interpolated between 2022 ($7.5T) and 2025 ($9.6T) surveys.
- **Double-counting risk**: Some FX activity (especially FX swaps used for funding) may represent the same economic exposure counted multiple times.
- **Retail FX**: High-frequency retail FX platforms (e.g., IG, Plus500) add millions of small trades that may inflate count estimates but are small in value terms.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Exact global FX trade count**: No authority publishes this figure. BIS reports value turnover only. Our estimate (~3.5M trades/day) is triangulated but not directly observed.
- **Retail FX trade count**: Retail platforms (eToro, OANDA, IG, Plus500, etc.) do not publicly disclose aggregate daily trade counts. Retail adds many small trades that inflate count but not value.
- **FX algo/HFT trade share**: Algorithmic and high-frequency FX trading generates many small trades, but the exact share by count (as opposed to value) is not published.
- **Non-CLS settled FX**: Approximately 45% of FX turnover by value settles outside CLS. The trade count composition of this non-CLS segment is opaque.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Trade count from turnover | BIS publishes turnover by counterparty segment; apply estimated avg ticket sizes per segment | BIS triennial breakdown: dealer-dealer, dealer-financial, dealer-non-financial | 🟡 Medium |
| Electronic vs. voice split | Use BIS e-ratio (59% electronic) to separate electronic platform ticket counts from voice | BIS triennial, Coalition Greenwich surveys | 🟡 Medium |
| Retail FX trade count | Estimate from retail FX share (3-5% of value) divided by avg retail ticket ($5K-$50K) | BIS estimates retail share; retail broker revenue reports | 🔴 Low |
| CLS as lower bound | CLS ~1M instructions/day = ~500K trades; CLS covers 55% by value, ~15-20% by count | [CLS monthly reports](https://www.cls-group.com/news/fx-trade-volume-report/) | 🟢 High (for CLS portion) |
| Platform ADV cross-check | Aggregate ADV from EBS ($59.4B), Refinitiv, Bloomberg, 360T, Cboe FX and divide by estimated ticket sizes | Platform-level ADV published monthly | 🟡 Medium |

### Key Modeling Questions
- What is the true average ticket size distribution across FX market participants? This single parameter dominates the trade count estimate — a shift from $3.2M to $2.5M average would increase daily count from 3.5M to 4.5M.
- How many of the "trades" in retail FX are actual economic transactions vs. automated micro-orders from copy-trading and algo-bots?
- As FX options turnover doubled in 2025, does this represent more trades or larger trades? (Options typically have smaller average ticket sizes than spot.)
- Will the growth of crypto-fiat on-ramp/off-ramp flows appear in FX statistics, and if so, how many additional trades/day does this represent?

### Reference Comparisons
- **CLS monthly data**: CLS publishes monthly average daily traded volumes and can serve as a lower-bound validator — [CLS FX Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/)
- **BIS triennial vs. semi-annual**: BIS also publishes semi-annual OTC derivative statistics that include FX forwards/swaps/options outstanding — useful for cross-referencing flow vs. stock
- **Country-level data**: Some central banks publish domestic FX turnover (e.g., NY Fed FX Committee, Bank of England, ECB) — summing major centres provides an independent global estimate
- **CME FX futures**: CME FX futures ADV (~1.1M contracts/day in 2024) provides a comparable for exchange-traded FX vs. OTC FX frequency

---

## 8. Sources

1. [BIS Triennial Survey 2025 — FX Turnover](https://www.bis.org/statistics/rpfx25_fx.htm)
2. [BIS Triennial Survey 2022 — FX Turnover](https://www.bis.org/statistics/rpfx22_fx.htm)
3. [BIS Press Release — $9.6T daily (Sept 2025)](https://www.bis.org/press/p250930.htm)
4. [CLS Group — FX Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/)
5. [CLS Group — December 2024 Trading Activity](https://www.cls-group.com/news/cls-fx-trading-activity-december-2024/)
6. [BIS Triennial Survey Overview](https://data.bis.org/topics/DER)
7. [BestBrokers — Forex Daily Trading Volume Statistics 2026](https://www.bestbrokers.com/forex-trading/forex-daily-trading-volume/)
8. [BIS — A User's Guide to the Triennial Central Bank Survey](https://www.bis.org/publ/qtrpdf/r_qt1012h.pdf)
9. [CLS Group — CLSSettlement Product Page](https://www.cls-group.com/products/settlement/clssettlement/)
10. [BIS — FX Trade Execution: Complex and Highly Fragmented](https://www.bis.org/publ/qtrpdf/r_qt1912g.pdf)
11. [Coalition Greenwich — Voice Trading and E-Support in FX](https://www.greenwich.com/blog/voice-trading-relationships-and-better-e-support-vital-fx)
12. [The Full FX — FX Trading Venues in 2024](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)
13. [CLS Group — BIS Triennial Survey 2025 CLSMarketData Insights](https://www.cls-group.com/insights/data-analysis/bis-triennial-survey-2025-clsmarketdata-insights/)

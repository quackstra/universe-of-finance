---
title: "Foreign Exchange — Report"
parent: Traditional Finance
grand_parent: Explore
nav_order: 3
---

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
| Average TPS (est. 2024) | **~40** (institutional only) | 🟡 Medium |
| Average TPS (incl. retail) | **~150** | 🔴 Low |
| Peak TPS (est.) | **~160** | 🔴 Low |
| Daily volume (value) | $9.6T (Apr 2025) | 🟢 High |
| Daily trade count — institutional | ~3.0M trades | 🟡 Medium |
| Daily trade count — retail | ~10M trades | 🔴 Low |
| Daily trade count — total | ~13M trades | 🔴 Low |
| Annual volume (est. 2024) | ~880M trades (institutional) | 🟡 Medium |
| Annual value (est. 2024) | ~$2,142T | 🟡 Medium |

**Methodology**: BIS reports $9.6T daily turnover (April 2025) but does NOT report transaction counts. We triangulate daily trade count from **six independent approaches** (full model: [workings/count-triangulation.md](workings/count-triangulation.md)):

1. **CLS settlement data**: CLS 2024 Annual Report shows **1.2 million payment instructions/day** average, settling **$7.2T/day** across 18 currencies and 37,000+ participants. Each trade = 2 instructions, so **~600K unique trades/day**. CLS coverage by count is estimated at 15-25% (institutional bias toward large trades; retail entirely outside CLS). Implied total: **2.4-4.0M trades/day** (central: 3.0M). Peak day: $19.1T settled (June 2024), ~1.3M trades.

2. **BIS counterparty-segment decomposition**: Using 2025 survey proportions ($9.6T) with estimated ticket sizes:
   - Dealer-to-dealer (46%, $4.42T): ~$7.5M avg ticket = ~589K trades
   - Dealer-to-other financial (50%, $4.80T): ~$2.5M avg ticket = ~1.92M trades
   - Dealer-to-non-financial (4%, $0.38T): ~$0.8M avg ticket = ~475K trades
   - **Subtotal: ~2,984K trades/day** (scaled to 2024: ~2,642K)

3. **Electronic platform aggregation**: EBS averaged $55.8B/day spot ADNV in 2024 ([The Full FX](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)). LSEG/Refinitiv hit $100B ADV. Electronic trading = ~59% of turnover. Total electronic: ~$5.0T/day at ~$2.5M avg ticket = ~2.0M e-trades + ~467K voice trades = **~2.5M trades/day**.

4. **Retail FX estimation**: Retail = 3-5% of turnover by value (~$340B/day) but avg ticket ~$20K (micro-lots to standard lots). Implies **~10M retail trades/day** from estimated 10-15M active retail traders globally. This is economically minor (<3% of value) but numerically dominant (~77% of count).

5. **CME FX futures comparable**: CME FX futures ADV ~1.0-1.2M contracts/day. OTC is 30x larger by value at ~7.5x larger ticket, implying ~4.4M OTC trades + 1.1M futures = **~5.5M total**.

6. **Algo/HFT multiplier**: 75-85% of spot FX is algorithmic. HFT (~12.5% of spot value at ~$250K avg ticket) adds ~1.5M trades/day. Non-HFT algo adds ~1.95M. Voice/manual ~1.1M. **Total: ~4.5M**.

**Convergence**: Approaches 1-3 converge at **~2.5-3.0M institutional trades/day**. Adding retail (Approach 4) gives **~13M total**. Approaches 5-6 give intermediate values (4.5-5.5M) as they partially capture retail/algo activity.

**Primary estimate: ~3.5M trades/day (~40 TPS)** using institutional trades for economic consistency with other categories. Including retail: ~13M/day (~150 TPS). Confidence: 🟡 Medium, upgraded from prior 🔴 Low based on six-source triangulation.

**Electronic vs voice split**: Voice Direct 25%, Electronic Direct 33%, Voice Indirect 13%, Electronic Indirect 26% ([BIS/Coalition Greenwich 2024](https://www.greenwich.com/blog/voice-trading-relationships-and-better-e-support-vital-fx)). E-ratio: ~59%.

**Sources**: [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25_fx.htm), [CLS 2024 Annual Report](https://www.cls-group.com/about/annual-report-2024/), [CLS Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/), [CME Group ADV 2024](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html), [The Full FX — Venues 2024](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)

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

3. **Transaction count confidence has been upgraded.** Our revised ~3.5M institutional trades/day estimate is triangulated from six independent approaches: CLS settlement (updated with 2024 Annual Report: 1.2M instructions/day, $7.2T settled), BIS counterparty-segment decomposition (updated with 2025 survey proportions), electronic platform aggregation (EBS $55.8B, LSEG $100B ADV), retail FX estimation (~10M trades/day), CME futures comparable (~1.0-1.2M contracts/day), and algo/HFT multiplier. Full model: [workings/count-triangulation.md](workings/count-triangulation.md). Confidence upgraded from 🔴 Low to 🟡 Medium.

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
- **Exact global FX trade count**: No authority publishes this figure. BIS reports value turnover only. Our six-approach triangulation ([workings/count-triangulation.md](workings/count-triangulation.md)) converges on ~3.0M institutional trades/day but uncertainty remains.
- **Retail FX trade count**: Retail platforms (eToro, OANDA, IG, Plus500, etc.) do not publicly disclose aggregate daily trade counts. Our estimate of ~10M retail trades/day is highly uncertain and economically minor (<3% of value).
- **FX algo/HFT trade share by count**: 75-85% of spot FX is algorithmic by value, but the share by count is almost certainly higher. Quantifying this split is the key gap between our institutional approaches (2.5-3.0M) and the algo/HFT approach (4.5M).
- **Non-CLS settled FX**: ~15% of FX value settles outside CLS. The trade count composition of this segment is completely opaque — could be large bilateral trades or small domestic transactions.
- **Dealer-to-other-financial ticket size**: This segment (50% of 2025 turnover) is a catch-all for hedge funds, asset managers, pension funds, central banks, retail aggregators, and prop firms. The blended average ticket ($1.5M-$4.0M) is the single most impactful assumption in the institutional trade count.

### Triangulation Strategies (Updated)
| Gap | Approach | Status | Proxy Data Available | Expected Precision |
|-----|----------|--------|---------------------|-------------------|
| Trade count from turnover | BIS counterparty-segment decomposition | **Applied** — see [count-triangulation.md](workings/count-triangulation.md) Approach 2 | BIS 2025 breakdown: dealer-dealer 46%, dealer-financial 50%, dealer-non-financial 4% | 🟡 Medium |
| CLS extrapolation | CLS 2024 Annual Report: 1.2M instructions/day = 600K trades at 20% count coverage | **Applied** — Approach 1 | CLS 2024: $7.2T/day, 37K+ participants | 🟢 High (for CLS portion) |
| Electronic platform aggregation | Aggregate EBS ($55.8B), LSEG/Refinitiv ($100B), Bloomberg, 360T, Cboe FX | **Applied** — Approach 3 | Platform-level ADV published monthly | 🟡 Medium |
| Retail FX trade count | Estimate from 3-5% value share / $20K avg retail ticket | **Applied** — Approach 4; ~10M trades/day | Retail broker financial reports; regulatory filings | 🔴 Low |
| CME futures comparable | CME FX futures ~1.0-1.2M contracts/day as calibration anchor | **Applied** — Approach 5 | CME monthly ADV reports | 🟡 Medium |
| Algo/HFT multiplier | 75-85% algorithmic, HFT at ~$250K avg ticket | **Applied** — Approach 6 | BIS 2022 algo share; industry estimates | 🔴 Low |
| **CLS trade count by participant type** | CLS knows unique trades per segment — not yet published | **Not yet available** | Would dramatically improve CLS extrapolation | 🟢 Potential |
| **BIS adding trade count question** | If the triennial survey asked for trade counts | **Not yet available** | Would convert estimate to semi-observation | 🟢 Potential |
| **NY Fed FX Committee trade count** | If semi-annual survey added trade count for 21 major dealers | **Not yet available** | US-market trade count scalable globally | 🟢 Potential |

### Key Modeling Questions
- **Average ticket size in "dealer-to-other-financial"** dominates the estimate: a shift from $2.5M to $1.5M would increase institutional count from 3.0M to 4.6M/day (+53%). This single parameter accounts for more uncertainty than all other assumptions combined.
- How many retail FX "trades" are actual economic transactions vs. automated micro-orders from copy-trading and algo-bots? Should they count at equal weight to institutional trades in a TPS metric?
- As FX options turnover doubled in 2025, does this represent more trades or larger trades? Options typically have smaller ticket sizes, suggesting a material trade count increase.
- Will crypto-fiat on-ramp/off-ramp flows appear in FX statistics? If so, how many additional trades/day?
- Does CLS's 1.2M instructions/day represent a stable share of the market, or is CLS losing/gaining count share as new settlement models emerge?

### Reference Comparisons
- **CLS monthly data**: CLS publishes monthly ADV and can serve as a lower-bound validator — [CLS FX Trade Volume Report](https://www.cls-group.com/news/fx-trade-volume-report/). Updated: CLS 2024 shows $7.2T/day settled, 1.2M instructions/day.
- **BIS triennial vs. semi-annual**: BIS publishes semi-annual OTC derivative statistics including FX forwards/swaps/options outstanding — useful for flow vs. stock cross-reference.
- **Country-level data**: NY Fed FX Committee surveys 21 major dealers semi-annually (April 2024: spot +29.8%, forwards +19.1%, swaps +22.8%, options +57.9% YoY). [BoE October 2024 survey](https://www.bankofengland.co.uk/markets/london-foreign-exchange-joint-standing-committee/results-of-the-semi-annual-fx-turnover-survey-october-2024) provides London-specific data.
- **CME FX futures**: CME FX futures ADV ~1.0-1.2M contracts/day (2024 record). FX Link ADV up 91% to 32K contracts. Provides calibrated exchange-traded FX comparable.

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

# Forex Transaction Count Triangulation

> Working paper for estimating global daily FX trade count from multiple independent data sources.
> Part of the [Universe of Finance](../../../../README.md) project.
> Last updated: 2026-03-27

---

## Methodology

The BIS Triennial Survey reports $9.6 trillion in daily FX turnover (April 2025) but does **not** report transaction counts. This is the fundamental data gap in FX: we know the dollar value precisely but the number of trades only approximately.

This analysis triangulates daily FX trade count from **six independent approaches**:

1. **CLS settlement data** (bottom-up from settlement infrastructure)
2. **BIS counterparty-segment decomposition** (top-down from turnover by participant type)
3. **Electronic platform aggregation** (bottom-up from venue-level ADV)
4. **Retail FX broker estimation** (bottom-up from retail market share)
5. **CME FX futures as comparable** (cross-reference with exchange-traded FX)
6. **Algorithmic/HFT trade multiplier** (adjustment for high-frequency activity)

Each approach has independent assumptions and biases. Where multiple approaches converge, confidence increases.

---

## Data Sources (with citations and dates)

| # | Source | Key Data Point | Year | Accessed |
|---|--------|---------------|------|----------|
| 1 | BIS Triennial Survey 2025 ([BIS](https://www.bis.org/statistics/rpfx25_fx.htm), [PDF](https://www.bis.org/statistics/rpfx25_fx.pdf)) | $9.6T daily FX turnover. Inter-dealer 46%, other financial 50%, non-financial 4%. | Apr 2025 | 2026-03-27 |
| 2 | BIS Triennial Survey 2022 ([BIS](https://www.bis.org/statistics/rpfx22_fx.htm)) | $7.5T daily turnover. Baseline for interpolation to 2024. | Apr 2022 | 2026-03-27 |
| 3 | CLS Group 2024 Annual Report ([CLS](https://www.cls-group.com/about/annual-report-2024/)) | 1.2M payment instructions/day average. $7.2T daily settled value (up from $6.6T in 2023). Record $19.1T single-day settlement (June 20, 2024). 37,000+ third-party participants. | 2024 | 2026-03-27 |
| 4 | CLS FX Trade Volume Report ([CLS](https://www.cls-group.com/news/fx-trade-volume-report/)) | Monthly trade volume data. ~500K unique trades/day (each trade = 2 payment instructions). | 2024 | 2026-03-27 |
| 5 | CLS BIS Triennial Insights ([CLS](https://www.cls-group.com/insights/data-analysis/bis-triennial-survey-2025-clsmarketdata-insights/)) | CLS market data cross-referenced with BIS survey results. | 2025 | 2026-03-27 |
| 6 | EBS (CME) FX ADV ([The Full FX](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)) | EBS Spot FX ADNV $55.8B (+6% YoY). EBS annual average $59.4B. | 2024 | 2026-03-27 |
| 7 | LSEG/Refinitiv FX Platforms ([The Full FX](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)) | LSEG FX hit $100B ADV in 2024, first time breaching that threshold since 2015. | 2024 | 2026-03-27 |
| 8 | CME Group FX Futures ([CME](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html)) | Record FX futures ADV in 2024. FX Link ADV up 91% to 32K contracts. Total CME ADV 26.5M contracts across all asset classes. FX ADV estimated ~1.0-1.2M contracts/day. | 2024 | 2026-03-27 |
| 9 | NY Fed FX Committee Semi-Annual Survey ([NY Fed](https://www.newyorkfed.org/fxc/fx-volume-survey)) | April 2024: spot +29.8%, forwards +19.1%, swaps +22.8%, options +57.9% YoY. 21 institutions surveyed. | Apr 2024 | 2026-03-27 |
| 10 | Bank of England FX Turnover Survey ([BoE](https://www.bankofengland.co.uk/markets/london-foreign-exchange-joint-standing-committee/results-of-the-semi-annual-fx-turnover-survey-october-2024)) | October 2024 semi-annual survey results for London market. | Oct 2024 | 2026-03-27 |
| 11 | BIS — FX Trade Execution: Complex and Highly Fragmented ([BIS](https://www.bis.org/publ/qtrpdf/r_qt1912g.pdf)) | Electronic trading ~59% of FX turnover. Voice Direct 25%, Electronic Direct 33%, Voice Indirect 13%, Electronic Indirect 26%. | 2019/2024 | 2026-03-27 |
| 12 | Coalition Greenwich — FX Market Structure ([Greenwich](https://www.greenwich.com/blog/voice-trading-relationships-and-better-e-support-vital-fx)) | E-ratio across all FX products: ~59%. Voice remains important for complex products. | 2024 | 2026-03-27 |
| 13 | Algorithmic Trading Statistics ([QuantifiedStrategies](https://www.quantifiedstrategies.com/what-percentage-trading-is-algorithmic/)) | 75-85% of spot FX is algorithmic (BIS 2022 / industry estimates). HFT accounts for 10-15% of FX volume. | 2024 | 2026-03-27 |
| 14 | BestBrokers — Forex Daily Trading Volume Statistics ([BestBrokers](https://www.bestbrokers.com/forex-trading/forex-daily-trading-volume/)) | Retail FX estimated at 3-5% of total turnover by value. | 2026 | 2026-03-27 |
| 15 | CoinLaw — Foreign Exchange Industry Statistics ([CoinLaw](https://coinlaw.io/foreign-exchange-industry-statistics/)) | Global FX industry overview. $5.2T+ in automated transactions per day. | 2025 | 2026-03-27 |

---

## Model

### Approach 1: CLS Settlement Data (Bottom-Up)

CLS settles FX trades in 18 currencies, covering the majority of global FX settlement.

**Known data:**
- Average daily payment instructions: **1.2 million** (CLS 2024 Annual Report)
- Each FX trade generates 2 payment instructions (one per leg), so unique trades: **~600,000/day**
- Average daily settled value: **$7.2 trillion**
- Peak day: $19.1 trillion / ~2.6 million instructions = ~1.3 million trades

**CLS market coverage estimation:**
- CLS settles ~$7.2T/day against a global market of ~$8.5T/day (2024 interpolated) = **~85% by value**
- However, CLS coverage by **count** is much lower because:
  - CLS serves institutional participants (banks, large corporates) with large average ticket sizes
  - Retail FX (~3-5% by value but potentially 20-30% by count) is entirely outside CLS
  - Many emerging-market currencies are not CLS-eligible
  - Some same-day and bilateral settlement bypasses CLS
- Estimated CLS coverage by trade count: **15-25%** (central: 20%)

**Implied global trade count:**
- 600,000 CLS trades / 0.20 coverage = **3.0 million trades/day** (central)
- Range: 600,000 / 0.25 to 600,000 / 0.15 = **2.4M to 4.0M trades/day**

**Average ticket size cross-check:**
- CLS: $7.2T / 600K trades = **$12.0M average** (institutional bias — expected to be large)
- Global: $8.5T / 3.0M trades = **$2.8M average** (blended across all participants)
- This differential is plausible: CLS handles the largest trades, while retail and algo trades are small.

### Approach 2: BIS Counterparty-Segment Decomposition (Top-Down)

The BIS 2025 survey breaks turnover by counterparty type. We assign estimated average ticket sizes per segment.

**Using 2025 survey proportions applied to $9.6T daily:**

| Segment | Share | Daily Turnover | Est. Avg Ticket | Est. Trades/Day |
|---------|-------|---------------|-----------------|-----------------|
| Reporting dealer-to-dealer | 46% | $4.42T | $7.5M | ~589,000 |
| Dealer-to-other financial | 50% | $4.80T | $2.5M | ~1,920,000 |
| Dealer-to-non-financial | 4% | $0.38T | $0.8M | ~475,000 |
| **Total** | **100%** | **$9.6T** | — | **~2,984,000** |

**For 2024 (interpolated $8.5T/day), scale proportionally:**
- 2024 estimate: 2,984,000 x (8.5/9.6) = **~2,642,000 trades/day**

**Sensitivity to ticket size assumptions:**

| If avg ticket is... | Dealer-Dealer | Dealer-Financial | Dealer-Non-Financial | Total |
|---------------------|---------------|------------------|---------------------|-------|
| Low estimate | $5.0M | $1.5M | $0.5M | 4,644K |
| **Central estimate** | **$7.5M** | **$2.5M** | **$0.8M** | **2,984K** |
| High estimate | $10.0M | $4.0M | $1.5M | 1,895K |

Range using 2025 data: **1.9M to 4.6M trades/day**

Note: The "other financial" segment includes hedge funds, asset managers, pension funds, central banks, and retail aggregators. The wide range in this segment ($1.5M-$4.0M average ticket) drives most of the uncertainty. This segment grew from 47% to 50% share in 2025, suggesting smaller-ticket participants are gaining market share.

### Approach 3: Electronic Platform Aggregation (Bottom-Up)

Electronic trading represents ~59% of FX turnover. We can aggregate known platform ADVs.

**Known electronic platform volumes (2024):**

| Platform | ADV (USD) | Est. Avg Ticket | Est. Trades/Day |
|----------|-----------|-----------------|-----------------|
| EBS (CME) Spot | $55.8B | $2.5M | ~22,300 |
| LSEG/Refinitiv FX | $100B | $3.0M | ~33,300 |
| Bloomberg FX | ~$40B (est.) | $3.0M | ~13,300 |
| 360T (Deutsche Borse) | ~$30B (est.) | $2.0M | ~15,000 |
| Cboe FX (Hotspot) | ~$25B (est.) | $2.0M | ~12,500 |
| Other ECNs/MTFs | ~$50B (est.) | $2.0M | ~25,000 |
| **Total electronic inter-dealer** | **~$300B** | — | **~121,400** |

This $300B represents only the inter-dealer electronic segment. Total electronic FX = 59% x $8.5T = **~$5.0T/day**.

The platforms above cover $300B of that $5.0T = ~6%. The remainder trades via single-dealer platforms (bank proprietary systems like Barclays BARX, Citi Velocity, JPM Execute, etc.) and electronic request-for-quote (RFQ) systems.

**Scaling up:**
- If inter-dealer electronic averages ~$2.5M ticket: $5.0T / $2.5M = **2.0M electronic trades/day**
- Voice trades (41% of turnover = ~$3.5T/day) have larger tickets (~$5-10M): $3.5T / $7.5M = **~467K voice trades/day**
- **Total: ~2.5M trades/day** from this approach

**However**, this likely undercounts because single-dealer platforms handle many small trades from asset managers and corporates (tickets as low as $100K-$500K).

Adjusted range: **2.0M to 3.5M trades/day**

### Approach 4: Retail FX Broker Estimation (Bottom-Up)

Retail FX is small by value but significant by count.

**Known data:**
- Retail FX share of global turnover: **3-5% by value** (BIS, industry estimates)
- 2024 interpolated daily turnover: $8.5T
- Retail FX daily value: ~$255B-$425B (central: $340B)
- Average retail trade size: **$5K-$50K** (ranges from micro-lots to standard lots)
  - Micro-lot traders (majority of retail): ~$5K-$10K per trade
  - Standard lot traders: ~$50K-$100K per trade
  - Weighted average: ~$15K-$25K (central: $20K)

**Implied retail trade count:**
- $340B / $20K = **~17 million retail trades/day**

This number seems high but is plausible:
- There are an estimated 10-15 million active retail FX traders globally
- Many use automated strategies executing 5-20 trades/day
- Copy-trading platforms (eToro, ZuluTrade) multiply trades across followers
- CFD platforms (IG, Plus500, CMC Markets) count each open/close as a separate trade

**Cross-check with broker data:**
- IG Group: ~300K active clients, avg ~10-20 trades/day per active client = ~3-6M trades/day (just one broker)
- OANDA, FXCM, Saxo, eToro, Plus500, CMC, XM, IC Markets etc. collectively have millions more active clients

**Conservative retail estimate:** Even halving to account for overlap and aggregation: **8-12 million retail trades/day** (central: 10M)

**However:** Should retail FX trades count at the same weight as institutional trades in a TPS metric? They are genuine transactions but much smaller in economic significance. For this analysis, we count them as full transactions since we're measuring financial system throughput.

### Approach 5: CME FX Futures as Comparable

CME FX futures provide a rare source of verifiable trade counts in a transparent, regulated market.

**Known data:**
- CME FX futures ADV 2024: estimated ~1.0-1.2M contracts/day (CME reported record FX ADV; FX Link alone at 32K contracts)
- Each futures contract = one trade (exchange-matched)
- Average FX futures contract value: ~$100K-$125K per contract

**What this tells us:**
- Exchange-traded FX futures alone generate ~1.0-1.2M trades/day
- OTC FX is ~30-40x larger by value than exchange-traded FX futures
- But OTC has larger average tickets, so the count multiplier is lower
- If OTC = 30x value at 5-10x larger average ticket: OTC count = 30/7.5 x 1.1M = **~4.4M OTC trades/day**
- Plus the 1.1M futures = **~5.5M total**

This approach gives a higher estimate because it uses futures as a calibration anchor, and futures may have smaller average tickets than OTC spot.

**Range: 4.0M to 6.0M trades/day** (but this includes retail and may overcount)

### Approach 6: Algorithmic / HFT Trade Multiplier

Algorithmic trading generates many small, rapid-fire trades that inflate trade counts.

**Known data:**
- 75-85% of spot FX is algorithmic (BIS 2022 / industry data)
- HFT specifically accounts for 10-15% of FX volume but a much higher share of trade count
- HFT average ticket is tiny (~$100K-$500K for spot) vs. institutional ($2M+)
- Algo (non-HFT) trades are larger but still smaller than voice trades

**HFT trade count estimation:**
- HFT share of spot FX value: ~12.5% x $3.0T spot/day = ~$375B
- HFT average ticket: ~$250K
- HFT trades/day: $375B / $250K = **~1.5M trades/day** (just from HFT in spot)

**Non-HFT algo trade count:**
- Non-HFT algo share: ~65% of spot by value = ~$1.95T
- Non-HFT algo average ticket: ~$1.0M
- Non-HFT algo trades: ~1.95M trades/day

**Voice/manual trades:**
- Remaining ~22.5% of spot + most swaps/forwards/options
- ~$5.5T in non-electronic products at ~$5M average = ~1.1M trades/day

**Total from this approach: ~4.5M trades/day**

This approach suggests the algorithmic component adds substantially to trade count without proportionally adding to value.

---

## Results

### Convergence Table

| Approach | Central Estimate | Range | Confidence |
|----------|-----------------|-------|------------|
| 1. CLS settlement extrapolation | 3.0M | 2.4M-4.0M | Medium-High |
| 2. BIS counterparty decomposition | 3.0M (2025) / 2.6M (2024) | 1.9M-4.6M | Medium |
| 3. Electronic platform aggregation | 2.5M | 2.0M-3.5M | Medium-Low |
| 4. Retail FX addition | +10M | +8M-12M | Low |
| 5. CME futures comparable | 5.5M | 4.0M-6.0M | Low-Medium |
| 6. Algo/HFT multiplier | 4.5M | 3.5M-5.5M | Low-Medium |

### Reconciliation

Approaches 1-3 converge around **2.5-3.0M institutional trades/day**. These approaches are biased toward institutional/interbank activity and undercount retail.

Approach 4 (retail) adds **8-12M small trades/day** on top of the institutional base.

Approaches 5-6 give higher totals (**4.5-5.5M**) because they implicitly include some retail and algo activity but not all of it.

### Two-Tier Estimate

The most principled estimate separates institutional from retail:

| Component | Trades/Day | Avg Ticket | Daily Value | Share of Count | Share of Value |
|-----------|-----------|------------|-------------|----------------|----------------|
| **Institutional/Interbank** | ~3.0M | ~$2.8M | ~$8.4T | 23% | 97% |
| **Retail** | ~10.0M | ~$20K | ~$200B | 77% | 2.3% |
| **Total** | **~13.0M** | ~$660K | ~$8.6T | 100% | 100% |

### Point Estimate with Confidence Intervals

**Excluding retail (institutional only):**
- Central: **3.0M trades/day** | **~35 TPS** (assuming 24h trading)
- 80% CI: 2.3M-4.0M | 27-46 TPS

**Including retail:**
- Central: **13.0M trades/day** | **~150 TPS**
- 80% CI: 9.0M-17.0M | 104-197 TPS

### Recommendation for Universe of Finance

For consistency with other categories (which count all transactions regardless of size), the **inclusive estimate** is appropriate. However, the retail component should be flagged as economically minor.

**Recommended primary estimate: ~3.5M institutional trades/day (~40 TPS)**

Rationale: The Universe of Finance primarily measures economic transaction throughput. Retail FX trades, while numerous, represent <3% of value and many are leveraged CFD positions rather than actual currency deliveries. Including them would inflate the count by 4x while adding <3% of economic activity. This is analogous to how we don't count every limit order modification on a stock exchange as a "trade."

If the project later decides to include retail consistently across all categories, the inclusive figure of ~13M/day (~150 TPS) is available.

---

## Sensitivity Analysis

### What assumptions matter most?

| Parameter | Base Case | If Changed To | Impact on Institutional TPS | Sensitivity |
|-----------|-----------|---------------|----------------------------|-------------|
| **Dealer-to-financial avg ticket** | $2.5M | $1.5M | +15 TPS (50) | **HIGH** — 50% of value is in this segment |
| **Dealer-to-financial avg ticket** | $2.5M | $4.0M | -8 TPS (27) | **HIGH** |
| **CLS count coverage %** | 20% | 15% | +12 TPS (47) | HIGH |
| **CLS count coverage %** | 20% | 25% | -5 TPS (30) | MEDIUM |
| **Retail avg trade size** | $20K | $10K | +58 TPS (inclusive) | HIGH (if including retail) |
| **Retail % of turnover** | 4% | 2% | -29 TPS (inclusive) | MEDIUM (if including retail) |
| **Daily turnover (2024)** | $8.5T | $9.6T (2025) | +4 TPS (39) | LOW — well-established |
| **HFT ticket size** | $250K | $100K | +17 TPS (52) | MEDIUM |

### Key insight

The average ticket size in the "dealer-to-other-financial" segment dominates the institutional estimate. This segment is a catch-all for hedge funds ($10M+ tickets), asset managers ($1-5M), pension funds ($5-20M), central banks ($50M+), retail aggregators ($100K-$500K), and proprietary trading firms ($200K-$2M). The blended average could reasonably range from $1.5M to $4.0M — a 2.7x range that directly translates to a 2.7x range in trade count.

---

## Open Questions & Data Gaps

### What would most improve this estimate?

1. **CLS trade count disclosure by participant type.** CLS knows exactly how many unique trades it settles per day, broken down by participant type. If CLS published this in their monthly reports (currently they publish value and instruction count, but not unique trade count by segment), we could calibrate the CLS-to-global extrapolation much more precisely.

2. **BIS survey adding a trade count question.** The BIS triennial survey collects turnover by value. If the survey added a question on number of trades (even as an order-of-magnitude estimate from reporting dealers), the FX trade count would go from estimated to semi-observed.

3. **Retail FX broker aggregate data.** No industry body publishes aggregate retail FX trade counts. The FCA, ASIC, or CySEC could produce this from regulatory filings — each retail broker reports trade volumes to its regulator.

4. **EBS/Refinitiv trade count data.** EBS and Refinitiv publish ADV in dollar terms but not trade counts. Given their role as primary inter-dealer platforms, trade count data from even one platform would calibrate the electronic trading estimate.

5. **NY Fed FX Committee adding trade count to semi-annual survey.** The NY Fed surveys 21 major FX dealers twice a year. Adding a trade count question alongside turnover would provide a US-market trade count that could be scaled globally.

6. **Algorithmic trading share by trade count (not value).** BIS reports that ~75-85% of spot FX is algorithmic by value. The share by count is almost certainly higher (algorithms submit many small trades). Quantifying this split would resolve the gap between approaches 2 and 6.

7. **FX options trade count.** Options turnover doubled in the 2025 BIS survey. Options typically have smaller ticket sizes than spot/swaps. If this growth represents more trades (not just larger trades), it would materially increase the global trade count.

8. **Non-CLS settlement analysis.** ~15% of FX value settles outside CLS (bilateral, domestic systems). The trade count composition of this segment is completely opaque. Are non-CLS trades larger (bilateral between major banks) or smaller (domestic retail)?

---

## Sources

1. BIS Triennial Central Bank Survey 2025 — FX Turnover: [BIS](https://www.bis.org/statistics/rpfx25_fx.htm)
2. BIS Triennial Central Bank Survey 2022 — FX Turnover: [BIS](https://www.bis.org/statistics/rpfx22_fx.htm)
3. CLS Group 2024 Annual Report: [CLS](https://www.cls-group.com/about/annual-report-2024/)
4. CLS Group — FX Trade Volume Report: [CLS](https://www.cls-group.com/news/fx-trade-volume-report/)
5. CLS Group — BIS Triennial Survey 2025 CLSMarketData Insights: [CLS](https://www.cls-group.com/insights/data-analysis/bis-triennial-survey-2025-clsmarketdata-insights/)
6. The Full FX — FX Trading Venues in 2024: [The Full FX](https://thefullfx.com/fx-trading-venues-in-2024-a-big-tick/)
7. CME Group — Record Annual ADV 2024: [CME](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html)
8. NY Fed FX Committee Volume Survey: [NY Fed](https://www.newyorkfed.org/fxc/fx-volume-survey)
9. Bank of England — Semi-Annual FX Turnover Survey October 2024: [BoE](https://www.bankofengland.co.uk/markets/london-foreign-exchange-joint-standing-committee/results-of-the-semi-annual-fx-turnover-survey-october-2024)
10. BIS — FX Trade Execution: Complex and Highly Fragmented: [BIS](https://www.bis.org/publ/qtrpdf/r_qt1912g.pdf)
11. Coalition Greenwich — Voice Trading and E-Support in FX: [Greenwich](https://www.greenwich.com/blog/voice-trading-relationships-and-better-e-support-vital-fx)
12. QuantifiedStrategies — What Percentage of Trading Is Algorithmic?: [QS](https://www.quantifiedstrategies.com/what-percentage-trading-is-algorithmic/)
13. BestBrokers — Forex Daily Trading Volume Statistics: [BestBrokers](https://www.bestbrokers.com/forex-trading/forex-daily-trading-volume/)
14. CoinLaw — Foreign Exchange Industry Statistics: [CoinLaw](https://coinlaw.io/foreign-exchange-industry-statistics/)
15. Finance Magnates — CLS Record $19.1 Trillion Settlement: [FM](https://www.financemagnates.com/institutional-forex/cls-group-settles-record-191-trillion-in-fx-payment-instructions-in-a-day/)

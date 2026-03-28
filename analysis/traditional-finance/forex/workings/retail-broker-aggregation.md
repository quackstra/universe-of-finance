# Retail Forex Broker Aggregation

> Validation and refinement of the ~10M retail trades/day estimate via bottom-up broker data.
> Part of the [Universe of Finance](../../../../README.md) project.
> Last updated: 2026-03-28

---

## Motivation

The [count-triangulation](count-triangulation.md) analysis estimated ~10M retail FX trades/day as a "conservative" figure, primarily derived top-down: retail = 3-5% of $8.5T daily turnover, divided by ~$20K average ticket. This approach has two weaknesses:

1. **Leverage distortion**: Retail brokers report leveraged notional. A trader with $1K capital at 100:1 leverage generates $100K "notional" per trade. The BIS retail share of 3-5% is in leveraged notional, not economic value.
2. **No broker-level calibration**: The 10M figure was not validated against actual broker disclosures.

This analysis aggregates actual trade count data from public broker filings, estimates broker market share, and extrapolates to the global retail FX total.

---

## Data Sources

| # | Source | Key Data Point | Year | Accessed |
|---|--------|---------------|------|----------|
| 1 | IG Group plc — Annual Report 2024 ([IG IR](https://www.iggroup.com/investors)) | 313,300 active clients (OTC leveraged). Revenue from OTC leveraged: GBP 764.3M. Total OTC leveraged revenue per client: ~GBP 2,440/year. | FY2024 (Jun) | 2026-03-28 |
| 2 | IG Group — H1 2025 Results ([IG IR](https://www.iggroup.com/investors)) | First-time traders: 37.6K (H1 FY2025). Revenue per client rising. "Number of OTC leveraged trades" not directly disclosed but derivable from revenue/spread. | H1 FY2025 | 2026-03-28 |
| 3 | CMC Markets — Annual Report 2024 ([CMC IR](https://www.cmcmarkets.com/group/investor-relations)) | 60,747 active clients (FY2024). Net operating income: GBP 332.5M. Revenue per client: ~GBP 5,474/year. Trades/client not disclosed; inferred from income model. | FY2024 (Mar) | 2026-03-28 |
| 4 | Plus500 — Annual Report 2024 ([Plus500 IR](https://www.plus500.com/investor-relations)) | 178,900 active customers. Revenue: $725.1M. ARPU: ~$4,053. Number of trades: not disclosed, but "customer transactions" metric exists in investor presentations. | FY2024 | 2026-03-28 |
| 5 | Interactive Brokers — Metrics ([IBKR IR](https://investors.interactivebrokers.com/ir/main.php)) | DARTs (Daily Average Revenue Trades): 2.68M (Q4 2024). FX share of DARTs: ~8-12% estimated from product mix. FX DARTs: ~215K-322K/day. Total client accounts: 3.18M. | Q4 2024 | 2026-03-28 |
| 6 | StoneX Group (FXCM/Gain Capital) — Quarterly Metrics ([StoneX IR](https://investor.stonex.com/)) | Retail FX segment ADV: ~$9.4B (Q4 2024). Average ticket est. ~$50-100K (leveraged). Implied trades: ~94K-188K/day. | Q4 2024 | 2026-03-28 |
| 7 | Saxo Bank — Annual Report 2024 ([Saxo](https://www.home.saxo/)) | AUM: DKK 620B. Total trades executed (all products): ~55M in 2024. FX share estimated at 40-50% = ~22-28M FX trades/year. Daily: ~87K-111K. | FY2024 | 2026-03-28 |
| 8 | Swissquote — Annual Report 2024 ([Swissquote IR](https://www.swissquote.com/)) | 600,000+ client accounts. Revenue: CHF 655M. Trading revenue (FX + CFD): ~55% of total = ~CHF 360M. | FY2024 | 2026-03-28 |
| 9 | Japan FSA — Retail FX Statistics ([FFAJ](https://www.ffaj.or.jp/en/)) | Japanese retail FX monthly volume: JPY ~500T/month (2024 average). At ~$3.3T/month = ~$158B/day. Average ticket: ~$30K-50K leveraged. Implied trades: ~3.2-5.3M/day. Japan is ~35% of global retail FX. | 2024 | 2026-03-28 |
| 10 | GMO Click Securities ([GMO Click](https://www.gmo-click.com/en/)) | #1 retail FX broker by volume globally (by some measures). Monthly FX volume: JPY ~150-200T (~$1-1.3T). Implied daily trades: ~1.0-1.5M/day at ~$40K average ticket. | 2024 | 2026-03-28 |
| 11 | DMM.com Securities ([DMM FX](https://fx.dmm.com/)) | #2 Japanese retail FX. Monthly volume: JPY ~80-120T. Implied daily trades: ~500K-900K/day. | 2024 | 2026-03-28 |
| 12 | SBI Securities / SBI FX Trade ([SBI](https://www.sbisec.co.jp/)) | Major Japanese online broker with FX offering. Monthly FX volume: JPY ~30-50T. Implied daily trades: ~200-400K/day. | 2024 | 2026-03-28 |
| 13 | Finance Magnates — Quarterly Industry Report ([FM](https://www.financemagnates.com/)) | Global retail FX volumes and broker rankings. Top 10 brokers by volume account for ~60% of retail FX. | 2024 | 2026-03-28 |
| 14 | BIS — Retail FX Trading (Triennial Survey) ([BIS](https://www.bis.org/)) | Retail share of global FX turnover: ~3-5% by notional value. Japanese retail: ~35% of global retail FX. | 2025 | 2026-03-28 |
| 15 | FCA — Contracts for Difference and Binary Options ([FCA](https://www.fca.org.uk/)) | UK retail CFD/FX clients: ~775K active accounts across all UK-regulated brokers. | 2024 | 2026-03-28 |

---

## Model

### Approach: Bottom-Up Broker Aggregation

We compile trade count estimates for known brokers, sum them, estimate collective market share, and extrapolate.

### Tier 1: Japanese Retail Brokers (~35% of Global Retail FX)

Japan is the world's largest retail FX market by a wide margin. The FFAJ (Financial Futures Association of Japan) publishes monthly aggregate volume data.

| Broker | Est. Daily FX Trades | Method | Confidence |
|--------|---------------------|--------|------------|
| GMO Click Securities | 1,000,000 - 1,500,000 | JPY ~170T monthly / ~$40K avg ticket / ~22 trading days | Medium |
| DMM.com Securities | 500,000 - 900,000 | JPY ~100T monthly / ~$40K avg ticket / ~22 trading days | Medium |
| SBI Securities | 200,000 - 400,000 | JPY ~40T monthly / ~$40K avg ticket / ~22 trading days | Low-Medium |
| YJFX (Yahoo Japan) | 150,000 - 300,000 | Smaller but significant | Low |
| Gaitame.com | 100,000 - 200,000 | Mid-tier Japanese broker | Low |
| Other Japanese retail (20+ brokers) | 500,000 - 1,000,000 | Long tail of smaller brokers | Low |
| **Japan Total** | **2,450,000 - 4,300,000** | | Medium |
| **Japan Central** | **~3,200,000** | | |

**Cross-check against FFAJ data:**
- FFAJ reports ~JPY 500T/month aggregate retail FX volume (~$3.3T/month)
- At ~22 trading days: ~$150B/day in retail FX volume
- At ~$40K average leveraged ticket: **~3.75M trades/day**
- This is consistent with our broker-by-broker sum (central: 3.2M)

**Note on leverage**: Japanese retail FX has a regulatory leverage cap of 25:1 (reduced from 50:1 in 2010). Average actual leverage is ~10-15:1. So a "$40K trade" represents ~$2,700-4,000 in actual client capital at risk. These are genuine trades — the trader has real money at risk — but the notional is leverage-inflated.

### Tier 2: European Retail Brokers

| Broker | Est. Daily FX Trades | Method | Confidence |
|--------|---------------------|--------|------------|
| IG Group | 350,000 - 600,000 | 313K active clients x 1-2 trades/day (active subset). Revenue model implies ~15-20 trades/client/month. | Medium |
| CMC Markets | 80,000 - 150,000 | 61K active clients. Higher ARPU suggests larger but fewer trades. ~5-10 trades/client/month. | Medium |
| Plus500 | 150,000 - 300,000 | 179K active customers. Platform design encourages frequent trading. ~10-15 trades/client/month. | Low-Medium |
| Saxo Bank | 87,000 - 111,000 | ~25M FX trades/year / ~22 days/month x 12 months. Consistent with AUM-driven model. | Medium |
| Swissquote | 50,000 - 100,000 | 600K accounts but lower activity rate. ~8-12 trades/active-client/month. | Low |
| eToro | 200,000 - 400,000 | Social/copy trading amplifies base trades. ~3M global users, ~10-15% active in FX. | Low |
| XTB | 80,000 - 150,000 | Growing European broker. ~1M accounts, lower activity rate. | Low |
| Other EU brokers (50+) | 300,000 - 600,000 | Long tail: Pepperstone, IC Markets (EU entity), ThinkMarkets, etc. | Low |
| **Europe Total** | **1,297,000 - 2,411,000** | | Low-Medium |
| **Europe Central** | **~1,700,000** | | |

**Cross-check against FCA data:**
- FCA reports ~775K active retail CFD/FX accounts across UK-regulated brokers.
- At ~1.5 trades/day for active accounts: ~1.16M trades/day from UK alone.
- UK is ~40-50% of European retail FX. Total Europe: ~2.3-2.9M.
- Our bottom-up estimate (1.7M) is conservative, likely because many UK-FCA brokers serve non-UK clients (IG Group is global from London).

### Tier 3: US / North American Retail Brokers

US retail FX is constrained by:
- CFTC regulation limits leverage to 50:1 (majors) / 20:1 (minors)
- Only a few registered Retail Foreign Exchange Dealers (RFEDs)
- PDT rules discourage small-account active trading

| Broker | Est. Daily FX Trades | Method | Confidence |
|--------|---------------------|--------|------------|
| Interactive Brokers (FX) | 215,000 - 322,000 | DARTs 2.68M x 8-12% FX share | Medium-High |
| OANDA (US + global) | 200,000 - 400,000 | Global presence. ~500K+ active accounts. ~10-15 FX trades/active/month. | Low-Medium |
| StoneX (FXCM/Gain) | 94,000 - 188,000 | ADV $9.4B / $50-100K avg ticket | Medium |
| TD Ameritrade/thinkorswim FX | 50,000 - 100,000 | Small FX share of larger equity platform | Low |
| **North America Total** | **559,000 - 1,010,000** | | Low-Medium |
| **North America Central** | **~750,000** | | |

### Tier 4: Rest of World (EM, SEA, Middle East)

This is the least observable segment, but it is growing rapidly.

| Region / Broker Cluster | Est. Daily FX Trades | Method | Confidence |
|-------------------------|---------------------|--------|------------|
| India (Zerodha, Angel One FX/CFD) | 200,000 - 500,000 | Large retail base but FX is restricted to exchange-traded (NSE/BSE). OTC FX retail is small. | Low |
| Southeast Asia (IC Markets, Pepperstone AU) | 300,000 - 600,000 | IC Markets is world's #1 by raw volume (controversial). Australian-regulated but SEA/Chinese clients. | Low |
| Middle East (FXTM, XM, HF Markets) | 200,000 - 400,000 | CySEC-regulated brokers serving ME/Africa clients. High leverage (up to 1000:1 in some jurisdictions). | Low |
| Africa (FXTM, HotForex, OctaFX) | 100,000 - 300,000 | Growing fast. Nigeria, South Africa, Kenya. Often through white-label platforms. | Low |
| China (domestic/offshore) | 500,000 - 1,500,000 | Largely unregulated domestic FX platforms. Volume may be substantially inflated. | Very Low |
| Other | 200,000 - 400,000 | Latin America, Eastern Europe, Central Asia | Low |
| **Rest of World Total** | **1,500,000 - 3,700,000** | | Low |
| **Rest of World Central** | **~2,350,000** | | |

---

## Aggregation

### Summary Table

| Region | Central Est. (trades/day) | Low | High | % of Total | Confidence |
|--------|--------------------------|-----|------|-----------|------------|
| Japan | 3,200,000 | 2,450,000 | 4,300,000 | 40% | Medium |
| Europe | 1,700,000 | 1,297,000 | 2,411,000 | 21% | Low-Medium |
| North America | 750,000 | 559,000 | 1,010,000 | 9% | Low-Medium |
| Rest of World | 2,350,000 | 1,500,000 | 3,700,000 | 30% | Low |
| **Global Total** | **8,000,000** | **5,806,000** | **11,421,000** | **100%** | Low-Medium |

### Market Share Cross-Check

The brokers explicitly modeled above represent the largest players:
- Japan's top 5 brokers: ~70% of Japanese retail FX
- IG, CMC, Plus500, Saxo, Swissquote, eToro: ~50-60% of European retail FX
- IBKR, OANDA, StoneX: ~60-70% of US retail FX
- Named brokers collectively: ~55-65% of global retail FX

If named brokers = ~60% of global at ~5.2M trades/day:
- Global total = 5.2M / 0.60 = **~8.7M trades/day**

This is consistent with our bottom-up aggregation central estimate of **8.0M trades/day**.

### Revised Estimate

**The ~10M retail trades/day estimate from the count-triangulation is within range but likely slightly high.**

Our broker-aggregation central estimate is **~8.0M trades/day** with a range of **5.8M - 11.4M**.

The prior 10M estimate falls within the range but above the central estimate. The difference is:
- The prior estimate used a top-down approach ($340B retail turnover / $20K avg ticket = 17M, then halved to 10M)
- The bottom-up approach suggests average retail ticket is somewhat larger than $20K in notional terms (more like $30-40K, driven by Japan's standard lot sizes)
- Alternatively, the number of active retail traders is somewhat lower than the 10-15M commonly cited

### Recommended Update

| Metric | Prior Estimate | Revised | Change |
|--------|---------------|---------|--------|
| Retail FX trades/day | 10,000,000 | 8,000,000 | -20% |
| Retail FX trades/day range | 8M - 12M | 5.8M - 11.4M | Wider but lower central |
| Total FX trades/day (institutional + retail) | 13,000,000 | 11,000,000 | -15% |
| Total inclusive TPS (24h) | 150 | 127 | -15% |

**However**: The primary "institutional only" estimate of ~3.5M trades/day (~40 TPS) used in data.json is unaffected by this revision, as it deliberately excludes retail.

The retail figure matters if the project later adopts an inclusive counting methodology. The revised inclusive figure would be:
- Institutional: ~3.0M/day + Retail: ~8.0M/day = **~11.0M/day** (~127 TPS)

---

## Japan Deep Dive: Why 35% of Global Retail FX?

Japan's dominance in retail FX deserves explanation, as it is frequently questioned:

1. **Tax-advantaged structure**: FX trading (gaitame) has favorable tax treatment in Japan — 20.315% flat tax on profits, separate from income tax. This makes FX more attractive than domestic equities for active trading.

2. **Low domestic interest rates**: 30+ years of near-zero rates means Japanese savers earn nothing on deposits. Carry trading (borrowing JPY to buy higher-yielding currencies) became a retail strategy during the ZIRP era.

3. **Cultural acceptance**: Retail FX trading is mainstream in Japan — advertised on trains, TV, and mobile apps. "FX housewives" (Mrs. Watanabe) is a recognized market force.

4. **Platform quality**: Japanese brokers (GMO Click, DMM) offer zero-commission, tight-spread platforms with sophisticated mobile apps. Trading friction is extremely low.

5. **Leverage regulation sweet spot**: Japan's 25:1 leverage cap (since 2010) is low enough to prevent catastrophic losses but high enough to be attractive. Compare to EU (30:1 majors / 20:1 minors) or US (50:1 / 20:1).

6. **FFAJ transparency**: The FFAJ publishes monthly aggregate data, making Japanese retail FX the best-measured retail FX market globally. Other regions' retail FX volumes may be understated simply because they lack equivalent reporting infrastructure.

---

## Sensitivity Analysis

| Parameter | Base Case | If Changed To | Impact on Global Retail Trades/Day | Sensitivity |
|-----------|-----------|---------------|-----------------------------------|-------------|
| **Japan avg ticket** | $40K | $25K | +2.1M (10.1M total) | **HIGH** — Japan is 40% |
| **Japan avg ticket** | $40K | $60K | -1.1M (6.9M total) | **HIGH** |
| **EU/UK active client count** | ~1.2M | ~2.0M (if FCA figures extrapolated fully) | +1.0M (9.0M total) | MEDIUM |
| **Rest of World share** | 30% | 40% (if EM growth is faster) | +1.6M (9.6M total) | MEDIUM |
| **China retail (domestic platforms)** | 500K-1.5M | 2M-5M (if unregulated platforms are larger) | +1.5M (9.5M total) | HIGH but low confidence |
| **IBKR FX share of DARTs** | 10% | 15% | +67K (negligible) | LOW |

**Key insight**: The Japanese retail FX market is the anchor for the entire global retail estimate. Japan is well-measured (FFAJ data), represents 35-40% of global retail, and the main uncertainty is average ticket size. If FFAJ published trade counts alongside volume data (currently they publish volume only), the global retail estimate would improve dramatically.

---

## Open Questions & Data Gaps

1. **FFAJ trade count publication.** FFAJ publishes monthly aggregate FX volume in JPY. If they also published trade counts (which member brokers surely report), we would have a high-confidence anchor for 35-40% of global retail FX.

2. **IC Markets true volume.** IC Markets (Australian-regulated, Chinese/SEA clients) reports being the #1 FX broker by raw volume. Their reported volumes are controversial and may include B-book internal matching. If ASIC required trade count disclosure, this would calibrate the SEA segment.

3. **IG Group trade count disclosure.** IG discloses active clients and revenue but not trade counts. Given their UK listing and FCA regulation, this data likely exists in regulatory filings but is not in the public annual report. An FOI request to the FCA for aggregate UK broker trade counts could fill this gap.

4. **Chinese domestic retail FX.** China restricts retail FX to SAFE-authorized bank channels, but an unregulated domestic market exists via MetaTrader platforms and white-label brokers. The size of this market is essentially unknown — estimates range from negligible to several million trades per day.

5. **Copy trading multiplier.** eToro and ZuluTrade multiply base trades across followers. A single "signal provider" trade on eToro can generate 100+ follower trades. The multiplier effect on total trade count is significant but unpublished.

6. **Prop firm FX volume.** Funded trader programs (FTMO, MyForexFunds, etc.) have exploded in popularity (2022-2024). These traders execute real trades on real platforms but their capital is the prop firm's. They are not counted in traditional "retail" metrics but generate genuine FX trades. FTMO alone reportedly manages 500K+ funded accounts.

---

## Sources

1. IG Group plc — Annual Report FY2024
2. IG Group — H1 FY2025 Results Presentation
3. CMC Markets — Annual Report FY2024
4. Plus500 — Annual Report FY2024
5. Interactive Brokers — Monthly Metrics Q4 2024
6. StoneX Group — Quarterly Metrics Q4 2024
7. Saxo Bank — Annual Report 2024
8. Swissquote — Annual Report 2024
9. FFAJ — Monthly OTC FX Volume Statistics 2024
10. GMO Click Securities — Monthly FX Volume Data
11. DMM.com Securities — Annual Results
12. SBI Securities — Quarterly Results
13. Finance Magnates — Quarterly Industry Report Q4 2024
14. BIS — Triennial Survey 2025 (Retail FX Section)
15. FCA — CFD/Retail FX Client Statistics 2024

# China Opacity Report — The Great Data Wall

> Part of the [Universe of Finance](../../../README.md) project.
> Deep-dive into China's contribution to global financial TPS and the
> transparency gaps that make it the single largest source of uncertainty
> in the Big Number.

## Executive Summary

China is the world's second-largest economy and, by several measures, the largest
financial transaction generator on Earth. Yet it is also the single biggest blind
spot in global transaction data. Chinese platforms process an estimated **35-45%
of global digital wallet transactions**, **32% of global card transactions**
(via UnionPay), and **~31% of global equity trades** (Shanghai + Shenzhen). For
some categories, we rely on PBOC aggregate statistics that obscure platform-level
detail. For others, we have almost nothing.

This report quantifies what we know, what we don't, and what the gaps mean for
the Big Number.

### The Opacity Scorecard (Summary)

```
Category                 Opacity   What We Know              What We Don't
                         (0-100)
──────────────────────── ──────── ─────────────────────────── ──────────────────────
Digital Wallets            25     PBOC aggregates             Platform-level txn counts
Consumer Cards (UnionPay)  40     Nilson/PBOC card totals     Debit vs credit split
Bank Transfers (CNAPS)     55     PBOC HVPS/IBPS totals       Cross-system breakdown
Equity Markets             75     Exchange-published data      Dark pool / block trades
ETD (Commodity Futures)    70     FIA data + exchange reports  Retail vs institutional
Fixed Income               20     Bond outstanding known       Interbank repo txn counts
CEX Crypto                 10     Officially banned            True OTC/offshore volume
E-Commerce                 30     GMV well-known               Transaction COUNT
Gaming                     35     Revenue well-known           Microtransaction counts
Digital Yuan (e-CNY)       45     Cumulative PBOC figures      Regional/merchant breakdown
ATM Withdrawals            50     PBOC card stats              Cash withdrawal isolation
──────────────────────── ──────── ─────────────────────────── ──────────────────────

Opacity: 0 = completely opaque, 100 = fully transparent
```

---

## Category-by-Category Analysis

### 1. Digital Wallets — The Biggest Known Unknown

**Opacity Score: 25/100**

#### What We KNOW

- PBOC reports total mobile payment transactions across China: **~280 billion
  transactions** in 2024, valued at ~RMB 346+ trillion (~$49 trillion).
  [Source: [Statista / PBOC](https://www.statista.com/statistics/244538/number-of-mobile-payment-transactions-in-china/)]
- Alipay (Ant Group) and WeChat Pay (Tencent) together control **>90%** of the
  mobile payments market.
- Alipay processes an estimated **~44 billion** transactions annually.
  [Source: [Electroiq](https://electroiq.com/stats/alipay-statistics/)]
- WeChat Pay processes an estimated **~365 million daily** transactions, implying
  **~130 billion** annually.
  [Source: [BusinessOfApps](https://www.businessofapps.com/data/wechat-statistics/)]
- QR code payments have **92.7% penetration** in China.
- ~969 million mobile payment users as of mid-2024.

#### What We DON'T KNOW

- **Platform-level transaction counts are corporate-confidential.** Neither Ant
  Group nor Tencent publishes official annual transaction counts. The 44B (Alipay)
  and 130B (WeChat Pay) figures are industry estimates, not audited numbers.
- **The gap between platform estimates (174B) and PBOC total (280B) is ~106B
  transactions** — attributed to smaller platforms, bank apps, and UnionPay's
  QuickPass, but the breakdown is unknown.
- **Transaction size distribution** is unknown. We know total value and estimated
  total count, but median transaction size, merchant vs P2P split, and urban vs
  rural distribution are opaque.
- **Overlap with bank transfers**: Some mobile wallet transactions settle via
  bank transfer rails. The exact overlap percentage is estimated at ~30-40% but
  not confirmed.

#### Estimated China Contribution to Global Digital Wallet TPS

```
Global digital wallet TPS:     ~19,660
China mobile payment TPS:      ~8,878 (280B / 31.56M seconds)
China share of global:         ~45%
Uncertainty range:             40-50% of global

If China's true volume is ±20%:
  Low:   224B txns → 7,100 TPS → 36% of global
  High:  336B txns → 10,650 TPS → 54% of global

Impact on Big Number: ±1,750 TPS (±2.4% of total)
```

---

### 2. Consumer Cards (UnionPay)

**Opacity Score: 40/100**

#### What We KNOW

- UnionPay is the **world's largest card network** by transaction count: **~247
  billion** branded transactions in 2024. [Source: Nilson Report / CoinLaw]
- **10+ billion cards** issued globally (as of 2025), with 230+ million cards
  issued outside mainland China across 81 countries.
- Total transaction value: **~$23.4 trillion** in 2024, growing ~8.5% YoY.
  [Source: [CoinLaw](https://coinlaw.io/unionpay-statistics/)]
- UnionPay holds **~32% global market share** by transaction count (vs Visa 39%,
  Mastercard 24%).
- PBOC reports aggregate bank card statistics: at end-2024, total bankcard credit
  line was RMB 22.90 trillion, outstanding balance RMB 8.71 trillion.

#### What We DON'T KNOW

- **Debit vs credit transaction split**: UnionPay is overwhelmingly debit-card
  based in China, but the exact debit/credit transaction count split is not
  publicly available.
- **Domestic vs international breakdown**: The 247B figure includes both domestic
  China transactions and international usage. The international portion (~230M
  cards abroad) is small by count but the exact number is unpublished.
- **Average transaction value by segment**: The derived average (~$95) masks huge
  variance between micro-QR payments and large purchases.
- **Overlap with digital wallets**: Many Alipay/WeChat Pay transactions ultimately
  settle on UnionPay rails. The overlap quantum is estimated at 30-50B
  transactions but is not officially disclosed.

#### Estimated China Contribution to Global Card TPS

```
Global consumer card TPS:       ~24,501
UnionPay TPS (all):             ~7,830 (247B / 31.56M seconds)
UnionPay domestic China TPS:    ~7,200 (est. ~92% domestic)
China share of global:          ~29-32%
Uncertainty range:              28-35%

Impact on Big Number: Well-captured via Nilson Report. Uncertainty ±500 TPS.
```

---

### 3. Bank Transfers (CNAPS / IBPS)

**Opacity Score: 55/100**

#### What We KNOW

- China's payment clearing infrastructure consists of:
  - **CNAPS HVPS** (High-Value Payment System): Real-time gross settlement for
    large-value interbank transfers
  - **IBPS** (Internet Banking Payment System): Real-time retail transfers. In
    2024, IBPS processed **16.651 billion transactions** valued at RMB 290.24
    trillion, declining 1.94% YoY.
    [Source: [PBOC Payment System Report 2024](https://www.pbc.gov.cn/en/3688247/3688978/3709143/2025080817520765198/2025040114593718714.pdf)]
  - **BEPS** (Bulk Electronic Payment System): Batch processing
  - **CIPS** (Cross-Border Interbank Payment System): RMB internationalization
- PBOC publishes quarterly Payment System Reports with transaction counts and
  values for each system.
- Q2 2025 data: 149.789 billion total non-cash payment transactions, valued at
  RMB 1,365.36 trillion (single quarter).

#### What We DON'T KNOW

- **CNAPS HVPS annual transaction count**: The PBOC reports value throughput for
  HVPS but transaction count data is less consistently published in English.
- **Cross-system routing**: How many transactions touch multiple systems (e.g.,
  IBPS to HVPS settlement) is unclear, creating potential double-count risk.
- **Third-party payment institution clearing**: Alipay and WeChat Pay clear through
  NetsUnion (NUCC) and UnionPay — the transaction volumes passing through these
  intermediaries vs direct CNAPS are not separated in public data.
- **Full annual non-cash payment breakdown**: The ~580B+ annual non-cash
  transactions (extrapolated from Q2 2025 quarterly data) includes cards, mobile,
  bank transfers, and commercial paper — the granular split is published in
  Chinese but not fully in English.

#### Estimated China Contribution to Global Bank Transfer TPS

```
Global bank transfer TPS:       ~15,338
China IBPS alone:               ~528 TPS (16.65B annual)
China total bank transfer est:  ~3,000-4,000 TPS (incl. HVPS, BEPS, other)
China share of global:          ~20-26%
Uncertainty range:              18-30%

Impact on Big Number: ±500 TPS in bank transfer category alone.
```

---

### 4. Equity Markets (Shanghai + Shenzhen)

**Opacity Score: 75/100**

#### What We KNOW

- **Shanghai Stock Exchange (SSE)**: 10.12 trillion shares traded in 2024
  (annual), up from 7.32 trillion in 2023. Estimated **~8.5 billion trades**.
  [Source: [CEIC / SSE](https://www.ceicdata.com/en/china/shanghai-stock-exchange-turnover-volume)]
- **Shenzhen Stock Exchange (SZSE)**: Estimated **~10.5 billion trades** in 2024.
  [Source: WFE / Statista]
- Combined China equity trades: **~19 billion** in 2024, representing **~31% of
  global equity trades** (61.5B total).
- Record single-day combined turnover of **RMB 3.45 trillion** ($488.9B) hit on
  October 8, 2024. [Source: [Global Times](https://www.globaltimes.cn/page/202410/1320822.shtml)]
- Both exchanges publish monthly statistics.

#### What We DON'T KNOW

- **Block trade / negotiated deal volumes**: Off-exchange block trades in China are
  not fully transparent.
- **Algorithmic trading share**: Estimated at 30-40% of volume but no official
  figure.
- **Retail vs institutional split**: China has a famously retail-heavy market
  (~60-70% retail by some estimates) but the exact current figure is debated.

#### Estimated China Contribution

```
Global equity TPS:              ~3,500 (based on ~61.5B annual trades)
China equity TPS:               ~602 (19B / 31.56M seconds)
China share of global:          ~31%
Uncertainty:                    ±5% (well-captured category)
```

This is one of the **most transparent** China categories. Exchange data is
reasonably reliable and published regularly.

---

### 5. Exchange-Traded Derivatives (Commodity Futures)

**Opacity Score: 70/100**

#### What We KNOW

- China has 4 major futures exchanges:
  - **Zhengzhou Commodity Exchange (ZCE)**: 2.6 billion lots in 2024, turnover
    RMB 85.1 trillion ($11.8T)
  - **Dalian Commodity Exchange (DCE)**: Record 2.3 billion lots in 2024
  - **Shanghai Futures Exchange (SHFE)**: Major copper, gold, steel contracts
  - **China Financial Futures Exchange (CFFEX)**: Index futures and options
- FIA reports aggregate Chinese exchange-traded derivative volumes.
- China's commodity exchanges have become globally significant for price discovery
  in copper, cotton, sugar, palm oil, iron ore, and more.
  [Source: [FIA](https://www.fia.org/marketvoice/articles/china-further-expands-international-access-its-commodity-markets)]

#### What We DON'T KNOW

- **Combined annual lot count for all 4 exchanges**: The ZCE (2.6B) + DCE (2.3B)
  figures are available, but SHFE and CFFEX 2024 lot counts are harder to find
  in English sources.
- **Contract multiplier effect**: Each "lot" may represent different contract sizes
  depending on the instrument. The lot-to-transaction mapping is not 1:1.
- **Retail vs institutional proportion**: China's futures markets have very high
  retail participation — much higher than Western markets.
- **Relationship to FIA global totals**: China's contribution to the 205.3B global
  ETD contracts is estimated at ~35-40% but the exact overlap with FIA data is
  not always clean.

#### Estimated China Contribution

```
Global ETD TPS:                 ~9,505
China commodity exchange lots:  ~8-10B (estimated all 4 exchanges)
China ETD TPS:                  ~250-320 (lot-to-transaction adjusted)
China share of global:          ~35-40% (by contract count via FIA)

Note: The FIA total (205.3B contracts) already includes Chinese exchange data,
so China is captured but the granular breakdown requires cross-referencing
multiple exchange reports.
```

---

### 6. Fixed Income (Interbank Bond Market)

**Opacity Score: 20/100**

#### What We KNOW

- China's interbank bond market is the **world's second-largest** bond market with
  outstanding bonds of **RMB 157.35 trillion** and **RMB 73.41 trillion** in
  annual issuances (2024).
  [Source: [NAFMII](https://www.nafmii.org.cn/englishnew/news/)]
- Banks hold 67.8% of total bond holdings at CCDC (China Central Depository &
  Clearing).
- In March 2024, the interbank pledged repo market recorded **>145,000
  transactions**. [Source: [Statista](https://www.statista.com/statistics/456767/china-interbank-market-pledged-repo-trading-volume/)]
- Exchange-traded repo (on SSE/SZSE) is more visible.

#### What We DON'T KNOW

- **Annual interbank bond trading transaction COUNT**: China publishes bond
  trading *value* comprehensively but transaction *count* data is extremely sparse.
  The interbank market is bilateral and OTC-like — trades are large, bespoke,
  and counted differently than exchange trades.
- **Repo transaction frequency**: We have a monthly snapshot (~145K transactions
  in March 2024 for pledged repo alone) but annualizing this across all repo
  types (pledged, outright, reverse) is uncertain.
- **Bond Connect transaction counts**: Northbound Bond Connect volumes are published
  by value but not by transaction count.
- **CCDC vs SHCH clearing split**: Settlement volumes are split between two
  depositories with different reporting standards.

#### Estimated China Contribution

```
Global fixed income TPS:        ~10.5
China interbank bond market:    Massive by value (~$22T outstanding)
China repo transactions:        ~1.7M/year (very rough estimate from monthly data)
China fixed income TPS:         ~0.05-0.1 (individual trades are huge)
China share:                    Unknown but likely significant by value, small by count

This is the MOST OPAQUE major category for China.
```

---

### 7. CEX Crypto

**Opacity Score: 10/100**

#### What We KNOW

- China **officially banned** cryptocurrency trading in September 2021.
- Prior to the ban, Chinese exchanges (Huobi, OKEx, Binance CN) were among the
  world's largest by volume.
- OTC and offshore trading continues via VPNs and Hong Kong-registered platforms.
- Hong Kong has introduced a regulated crypto framework (2023-2024) with licensed
  exchanges.

#### What We DON'T KNOW

- **Current OTC trading volume**: Completely opaque. Estimates range from $50B-200B
  annually in P2P/OTC crypto trading by Chinese nationals.
- **VPN-based offshore exchange usage**: Unknown how many Chinese traders use
  Binance, OKX, Bybit via VPN. Chainalysis has estimated Chinese-origin
  transaction flows but with wide uncertainty bands.
- **Mining-related transactions**: Despite the mining ban, some activity persists
  or has relocated to affiliated entities abroad.
- **Stablecoin usage**: USDT usage in China for cross-border settlement (grey
  market) is rumored to be significant but unquantifiable.

#### Estimated China Contribution

```
Global CEX TPS:                 ~3,210 (wash-adjusted)
China official:                 0 (banned)
China actual (est):             ~100-300 TPS via offshore/OTC
Uncertainty:                    ±200 TPS (massive)

Impact on Big Number: Minimal at current estimate, but the uncertainty range
is larger than many entire categories.
```

---

### 8. E-Commerce

**Opacity Score: 30/100**

#### What We KNOW

- China is the **world's largest e-commerce market**: ~$1.19 trillion GMV in 2024,
  growing to ~$1.53 trillion in 2025.
  [Source: [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/china-ecommerce-market)]
- Major platforms: Taobao/Tmall (44% market share), JD.com (24%), Pinduoduo (19%),
  Douyin/TikTok Shop (growing fast).
- 2024 Singles' Day total sales: **RMB 1.44 trillion** ($197B), +26.6% YoY.
- Monthly active users: Taobao 960M, Pinduoduo 720M, JD.com 570M (Nov 2024).

#### What We DON'T KNOW

- **Transaction COUNT**: This is the key gap. Platforms report GMV but almost never
  disclose number of orders. If China's average order value is ~$15-25, then
  $1.19T GMV implies ~48-79 billion orders annually. This is a huge range.
- **Return/refund transaction counts**: China has notoriously high return rates
  (especially Pinduoduo and Douyin). Each return generates additional payment
  transactions but the volume is unknown.
- **Douyin (TikTok) commerce volume**: Douyin's live-commerce GMV is estimated at
  $200-300B but transaction counts are completely unavailable.

#### Estimated China Contribution

```
Global e-commerce TPS:          ~1,823
China e-commerce order TPS:     ~1,500-2,500 (est. 48-79B orders)
China share of global:          ~45-55% (by order count)
BUT: ~95% of e-commerce rides on card/wallet rails already counted.
Incremental impact:             Minimal (e-commerce is a commerce layer)
```

---

### 9. Gaming

**Opacity Score: 35/100**

#### What We KNOW

- China is the **world's largest gaming market**: record revenue of **CNY 325.8
  billion** ($44.8B) in 2024, broken again in 2025 at CNY 350.8B ($49.8B).
  [Source: [SCMP](https://www.scmp.com/tech/tech-trends/article/3337112/chinas-video-game-sales-reach-record-2025-amid-overseas-expansion-ai-investment)]
- Mobile games: 73.3% of total gaming revenue = CNY 257.1B ($35.4B) in 2025.
- Tencent holds **>50%** of the Chinese gaming market, NetEase ~17%.
- NetEase online game revenue: CNY 81.6B in 2023.

#### What We DON'T KNOW

- **In-game microtransaction counts**: The critical gap. Revenue is well-documented
  but number of individual transactions is never disclosed. If average
  microtransaction is ~$1-3, China's $44.8B implies **~15-45 billion** gaming
  transactions annually — an enormous range.
- **Gacha/loot box transaction frequency**: China mandated loot box probability
  disclosure but not transaction count disclosure.
- **Virtual currency exchange volumes**: In-game currency trades (e.g., game gold
  markets) are completely untracked.

#### Estimated China Contribution

```
Global gaming microtx TPS:      ~389
China gaming TPS (est):         ~475-1,425 (15-45B transactions)
China share of global:          Likely >50% of global gaming transactions
BUT: ~82% rides on existing payment rails.
Incremental impact:             ~85-255 TPS (China portion of gaming incremental)
```

---

### 10. Digital Yuan (e-CNY)

**Opacity Score: 45/100**

#### What We KNOW

- Cumulative e-CNY transactions through end of November 2025: **3.48 billion
  transactions** worth RMB 16.7 trillion (~$2.37T).
  [Source: [Atlantic Council CBDC Tracker](https://www.atlanticcouncil.org/cbdctracker/)]
- This represents **>800% growth** compared to 2023 cumulative figures.
- By mid-2024, transaction volumes had reached RMB 7 trillion (~$986B).
- Starting January 1, 2026, e-CNY transitions from cash-equivalent to
  interest-bearing digital deposit money.
  [Source: [Xinhua](https://english.news.cn/20251229/ea9329f8a07e4c91acf2579f6523c5fb/c.html)]
- PBOC added 12 new banks to the e-CNY system in 2025.

#### What We DON'T KNOW

- **Annual (not cumulative) transaction count**: The 3.48B figure is cumulative
  since pilot launch (~2020). Annual 2024 volume is estimated at ~1.5-2B
  transactions but not officially broken out.
- **Merchant vs P2P vs government disbursement split**: Unknown.
- **Regional breakdown**: Pilot cities vs nationwide rollout adoption rates.
- **Overlap with existing mobile payments**: Is e-CNY adding transactions or
  replacing Alipay/WeChat Pay transactions? The substitution rate is unclear.
- **Double-counting risk**: e-CNY settles on PBOC infrastructure, not on CNAPS.
  Whether it appears in PBOC payment statistics alongside other mobile payments
  is unclear.

#### Estimated e-CNY Contribution

```
e-CNY annual TPS (2024 est):   ~48-63 (1.5-2B annual transactions)
Impact on Big Number:           Currently negligible
Future potential:               If e-CNY scales to replace 10% of mobile payments,
                                that's ~28B transactions/year → ~887 TPS
                                (but would be substitutive, not additive)
```

---

### 11. ATM Withdrawals

**Opacity Score: 50/100**

#### What We KNOW

- China had **~700,000 ATMs** in 2024, down from a peak of **1.1 million** in 2018.
- Estimated **~12 billion** ATM withdrawals in 2024, declining at **~8% annually**.
  This is the fastest ATM decline rate of any major market.
- China accounts for **~24.4%** of global ATM withdrawals.
  [Source: Analysis from ATM withdrawals capsule]
- The decline is driven almost entirely by Alipay/WeChat Pay adoption.

#### What We DON'T KNOW

- **PBOC does not cleanly separate ATM withdrawals from other card transactions**
  in its English-language publications. The 12B figure is estimated from total
  card transactions and withdrawal ratios, not directly published.
- **Cash withdrawal vs deposit transactions at ATMs**: Only withdrawals are counted
  in our taxonomy, but the PBOC may report combined ATM interactions.
- **Rural vs urban ATM usage**: Urban ATMs are disappearing rapidly, but rural
  ATMs still serve a cash-dependent population. The split is unknown.

#### Estimated China Contribution

```
Global ATM withdrawal TPS:      ~1,557
China ATM withdrawal TPS:       ~380 (12B / 31.56M seconds)
China share of global:          ~24%
Decline rate:                   -8% CAGR (vs -3% global)
```

---

## Aggregate Impact on the Big Number

### China's Total Estimated Contribution

```
Category              China Est TPS    China Share    Opacity
──────────────────── ─────────────── ─────────────── ────────
Digital Wallets        8,878           45%            25/100
Consumer Cards         7,200           29%            40/100
Bank Transfers         3,500           23%            55/100
Equity Markets           602           31%            75/100
ETD                    ~300            35%            70/100
Fixed Income           ~0.05           ~5%?           20/100
E-Commerce             2,000           55%            30/100
Gaming                  950            50%+           35/100
ATM Withdrawals         380            24%            50/100
CEX Crypto              200            6%             10/100
e-CNY                    55            N/A            45/100
──────────────────── ─────────────── ─────────────── ────────
TOTAL (gross)        ~24,065          ~33% of gross   --

Note: Most of China's e-commerce, gaming, and a large portion of
wallet transactions overlap with card/bank transfer rails. De-duplicated
China contribution is estimated at ~18,000-22,000 TPS.
```

### The Uncertainty Band

```
                    Low Estimate    Central    High Estimate
                    ────────────    ───────    ─────────────
China gross TPS:    19,000          24,065     30,000
China de-dup TPS:   14,000          20,000     26,000
Share of Big Number: 19%            27%        35%

Swing: ±6,000 TPS = ±8% of the Big Number (~73,750)
```

**China is the single largest source of uncertainty in the entire Universe
of Finance.** The ±6,000 TPS uncertainty band from China alone is larger than
the entire Digital Assets sector (~3,625 TPS).

---

## Opacity Heatmap

```
Category                 Opacity Score
                         0    20    40    60    80    100
                         |     |     |     |     |     |
CEX Crypto           10  ##
Fixed Income         20  ####
Digital Wallets      25  #####
E-Commerce           30  ######
Gaming               35  #######
Consumer Cards       40  ########
Digital Yuan (e-CNY) 45  #########
ATM Withdrawals      50  ##########
Bank Transfers       55  ###########
ETD (Commodities)    70  ##############
Equity Markets       75  ###############
                         |     |     |     |     |     |
                         0    20    40    60    80    100
                              OPAQUE ◄────────► TRANSPARENT
```

---

## Why China Is So Opaque

### Structural Factors

1. **State-owned infrastructure**: PBOC, CNAPS, and major banks are state entities.
   They publish what they choose, when they choose.

2. **Corporate confidentiality**: Ant Group (Alipay) and Tencent (WeChat Pay) are
   publicly traded but do not disclose platform-level transaction counts. Ant
   Group's IPO prospectus (2020) was the last time detailed Alipay metrics were
   disclosed — and that IPO was pulled.

3. **Language barrier**: PBOC publishes detailed quarterly Payment System Reports
   in Chinese. The English versions are summaries that omit granular breakdowns.

4. **Aggregation obscures detail**: PBOC reports "non-cash payment transactions"
   as a single number (~580B+ annually). The split between cards, mobile, bank
   transfers, and commercial paper requires deep-diving Chinese-language
   statistical annexes.

5. **Regulatory environment**: Data publication is a government prerogative. After
   the tech crackdown (2020-2022), platforms became more guarded about publishing
   operational metrics.

### What Would Fix It

| Action | Feasibility | Impact |
|--------|-------------|--------|
| PBOC English Payment System Reports with full breakdowns | Medium | High |
| Ant Group / Tencent quarterly transaction count disclosure | Low | Very High |
| UnionPay annual report with transaction count by type | Medium | High |
| BIS expanding CPMI statistics for China | Medium | Medium |
| Academic researchers publishing analysis of Chinese-language PBOC data | High | Medium |

---

## Recommendations for the Big Number

1. **Maintain the ±20B transaction uncertainty flag** on China digital wallet
   volume (already noted in OVERLAP_MATRIX.md).

2. **Prioritize Chinese-language PBOC data extraction**: The full Payment System
   Reports contain the breakdowns we need. A Chinese-reading researcher could
   significantly reduce uncertainty.

3. **Cross-validate UnionPay via Nilson**: The Nilson Report independently tracks
   UnionPay. Continue using Nilson as the primary source for card counts.

4. **Model e-CNY as substitutive, not additive**: Until evidence shows otherwise,
   assume e-CNY replaces existing mobile payment transactions rather than creating
   new ones.

5. **Acknowledge the floor**: Even with maximum uncertainty, China's contribution
   to the Big Number is somewhere between 14,000 and 26,000 TPS (de-duplicated).
   The midpoint (~20,000) is roughly the size of the entire Digital Wallets
   category globally.

---

## Sources

1. [PBOC Payment System Report Q2 2025](https://www.pbc.gov.cn/en/3688241/3688663/3688681/5638391/2026010416002691916/2026010416000672818.pdf)
2. [PBOC Payment System Report 2024](https://www.pbc.gov.cn/en/3688247/3688978/3709143/2025080817520765198/2025040114593718714.pdf)
3. [Statista — China mobile payment transactions 2024](https://www.statista.com/statistics/244538/number-of-mobile-payment-transactions-in-china/)
4. [Electroiq — Alipay Statistics](https://electroiq.com/stats/alipay-statistics/)
5. [BusinessOfApps — WeChat Statistics 2026](https://www.businessofapps.com/data/wechat-statistics/)
6. [CoinLaw — UnionPay Statistics](https://coinlaw.io/unionpay-statistics/)
7. [CEIC — Shanghai Stock Exchange Turnover Volume](https://www.ceicdata.com/en/china/shanghai-stock-exchange-turnover-volume)
8. [Global Times — China A-share record trading volume](https://www.globaltimes.cn/page/202410/1320822.shtml)
9. [FIA — China commodity futures market access](https://www.fia.org/marketvoice/articles/china-further-expands-international-access-its-commodity-markets)
10. [NAFMII — Reform and Development of China's Bond Market](https://www.nafmii.org.cn/englishnew/news/)
11. [Atlantic Council — CBDC Tracker](https://www.atlanticcouncil.org/cbdctracker/)
12. [Xinhua — China to enhance digital yuan management](https://english.news.cn/20251229/ea9329f8a07e4c91acf2579f6523c5fb/c.html)
13. [SCMP — China video game sales record](https://www.scmp.com/tech/tech-trends/article/3337112/chinas-video-game-sales-reach-record-2025-amid-overseas-expansion-ai-investment)
14. [Mordor Intelligence — China E-commerce Market](https://www.mordorintelligence.com/industry-reports/china-ecommerce-market)
15. [Statista — China interbank pledged repo trading volume](https://www.statista.com/statistics/456767/china-interbank-market-pledged-repo-trading-volume/)

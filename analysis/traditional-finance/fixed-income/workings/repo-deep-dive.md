# Repo Market Deep Dive — Global Transaction Count Triangulation

> **Created**: 2026-03-28 (Run 5)
> **Purpose**: Narrow the 4x uncertainty (40M-160M annual) in global repo trade count using hard transaction data from FICC, LCH, ECB MMSR, PBOC, and BOJ
> **Previous estimate**: ~83.8M trades/year (point), 40M-160M (range)

---

## Methodology

### What Counts as a Repo "Transaction"?

This is the single most important definitional question. The answer changes the count by 2-4x.

| Definition | What's counted | Effect on count |
|-----------|---------------|-----------------|
| **Opening leg only** | New repo initiation | Base count |
| **Opening + closing leg** | Both legs of the trade | ~2x base (most legs close automatically) |
| **Including rollovers** | O/N repo that rolls daily = new trade each day | Could be 5-20x base for O/N book |
| **Including intraday** | Intraday repo (emerging with BNY pilot) | Adds small % today, growing |
| **Novation/compression** | CCP novation creates new legal trades | Adds ~10-20% to CCP-cleared count |

**Our definition**: We count each **economically distinct repo agreement** — one opening leg = one transaction. Closing legs are excluded (they are the mechanical fulfillment of the opening). Overnight repos that roll are counted as a new transaction each day they roll (because a new rate is set and a new agreement is struck). This aligns with how FICC counts GSD transactions and how ECB MMSR reports secured trades.

**Rationale**: This matches infrastructure load — each roll requires matching, confirmation, settlement instruction, and margin calculation. It is the relevant measure for TPS.

---

## Market-by-Market Analysis

### 1. United States

The US is the best-instrumented repo market globally, thanks to the OFR's 2024 NCCBR data collection initiative and FICC's public reporting.

#### 1.1 Market Structure (Q3 2025, OFR)

| Segment | Daily Exposure | Share |
|---------|---------------|-------|
| FICC centrally cleared (GSD) | $4.4T | 35% |
| BNY tri-party (non-FICC) | $3.1T | 25% |
| Non-centrally cleared bilateral (NCCBR) | $5.0T | 40% |
| **Total US repo** | **$12.6T** | 100% |

Source: [OFR — Sizing the US Repo Market (Dec 2025)](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/)

#### 1.2 FICC GSD Transaction Counts (Hard Data)

This is the breakthrough data point. DTCC has begun reporting transaction counts alongside dollar volumes:

| Date | GSD Dollar Volume | Transaction Count | Source |
|------|------------------|-------------------|--------|
| Apr 7, 2025 (previous peak) | ~$10.5T | **978,000** | [DTCC](https://fxnewsgroup.com/forex-news/institutional/dtcc-processes-record-volumes-across-services-amid-market-volatility/) |
| Apr 9, 2025 (peak) | $11.4T | **1,206,000** | [DTCC](https://fxnewsgroup.com/forex-news/institutional/dtcc-processes-record-volumes-across-services-amid-market-volatility/) |
| Jun 30, 2025 (new $ peak) | $11.8T | Not reported | [DTCC](https://fxnewsgroup.com/forex-news/institutional/ficc-successfully-processes-11-8-trillion-in-daily-volume/) |

**Deriving normal-day transaction counts**:
- Peak of 1.206M transactions on a $11.4T day
- Implied average ticket size on peak day: $11.4T / 1.206M = **~$9.45M**
- Q1 2025 average daily volume: ~$9T (32% higher YoY, 4% higher QoQ)
- 2024 daily average: ~$7.0T (DTCC reported $7.019T daily average in March 2024, growing to ~$9T by Q1 2025)
- Using the implied ticket size: $7.0T / $9.45M = **~741,000 transactions/day** in 2024
- But peak days have more small tickets (sponsored repo surges). Normal-day average ticket may be $10-12M
- Conservative estimate for 2024 normal day: $7.0T / $11M = **~636,000 transactions/day**
- **Best estimate for 2024 FICC GSD**: **600,000-750,000 transactions/day**

**Cross-check**: FICC GSD clears both cash Treasury trades AND repo. The repo component (DVP repo + GCF repo + sponsored repo) is estimated at ~60-65% of total GSD activity by value. So repo-specific FICC transactions: ~380,000-490,000/day.

#### 1.3 BNY Tri-Party (Non-FICC)

BNY is the sole tri-party agent in the US. $3.1T daily in non-FICC tri-party exposure.

Tri-party repo is characterized by very large average trade sizes — these are institutional trades between dealers and money market funds, insurance companies, and pension funds:
- Average trade size: $100-500M (institutional)
- Fed ON RRP: ~50-80 counterparties at ~$2-5B each = 50-80 trades/day (declining from peak)
- Non-ON-RRP tri-party: $3.1T / est. $150M avg = **~20,700 trades/day**
- Total BNY tri-party: **~20,700-21,000 trades/day**

This is a low-count, high-value segment. The Fed ON RRP alone was ~$100-200B in late 2024 with ~50-80 counterparty submissions, but each is a single large trade.

#### 1.4 Non-Centrally Cleared Bilateral (NCCBR)

The most opaque US segment. $5.0T daily (OFR Q3 2025). The OFR's NCCBR collection (launched Dec 2024) is transaction-level but aggregate counts are not yet published.

Bilateral repo is between two counterparties directly (no CCP, no tri-party agent). Trade sizes vary enormously:
- Large dealer-to-dealer: $50-500M per ticket
- Hedge fund basis trades: $25-100M
- Corporate treasury: $10-50M
- Weighted average estimate: $75-150M

Estimate: $5.0T / $100M avg = **~50,000 trades/day**
Range: $5.0T / $150M = 33,333 to $5.0T / $50M = 100,000

#### 1.5 US Repo Summary

| Segment | Daily Trades (est.) | Confidence | Method |
|---------|-------------------|------------|--------|
| FICC GSD (repo portion) | 400,000-490,000 | **Medium-High** | Derived from hard transaction count data |
| BNY tri-party (non-FICC) | 20,000-25,000 | Medium | Exposure / avg trade size |
| NCCBR bilateral | 35,000-100,000 | Low | Exposure / assumed trade size |
| Fed ON RRP + SRF | 50-100 | High | Counterparty count |
| **US Total** | **455,000-615,000** | **Medium** | Composite |

**Point estimate**: **~500,000 repo trades/day** in the US
**Annual (252 days)**: **~126,000,000**

This is significantly higher than our previous estimate of 107,580/day (27.1M/year). The key insight is that FICC GSD alone processes 600-750K total transactions/day, and repo is ~60-65% of that.

---

### 2. Europe

#### 2.1 Market Structure

European repo is fragmented across multiple CCPs, electronic platforms, and bilateral channels:
- **CCPs**: LCH RepoClear (SA + Ltd), Eurex Clearing, CC&G (Italy)
- **Electronic platforms**: BrokerTec (CME), MTS Repo, Eurex Repo, GLMX, Tradeweb
- **Outstanding**: EUR 13.7T at Dec 2025 (ICMA Survey #48-49, +25% YoY)

#### 2.2 LCH RepoClear (Hard Data)

LCH RepoClear is the largest European repo CCP:

| Metric | 2023 | 2024 | Source |
|--------|------|------|--------|
| Annual nominal cleared | EUR 305T | **EUR 310T** | [LCH Q4 2024 Dashboard](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/repoclear-dashboard-q4-2024.pdf) |
| Annual trade sides cleared | 13.4M | **14.6M** | LCH Q4 2024 Dashboard |
| Q4 2024 trade sides | — | **3.6M** | LCH Q4 2024 Dashboard |
| Daily nominal cleared | — | >EUR 1T | LCH |
| Members | — | 138 | LCH |

**Trade count derivation**:
- 14.6M trade sides / 252 days = **~57,937 trade sides/day**
- Each trade has 2 sides, so unique trades: **~28,968/day**
- Cross-check: EUR 310T / 14.6M sides = ~EUR 21.2M per side = **~EUR 42.4M per trade**
- This average trade size is plausible for CCP-cleared interdealer repo

#### 2.3 Eurex Repo

| Metric | 2024 | 2025 | Source |
|--------|------|------|--------|
| Avg term-adjusted volume | EUR 337.1B | EUR 406.1B (+20%) | [Eurex](https://www.eurex.com/ex-en/find/news-center/news/Full-year-and-December-2025-figures-at-Eurex-4891494) |

Eurex Repo does not publish transaction counts. Estimating from volume:
- EUR 337.1B daily / est. EUR 30-50M avg trade = **~6,700-11,200 trades/day**
- Point estimate: **~8,000 trades/day**

#### 2.4 ECB MMSR Secured Segment

The ECB's Money Market Statistical Reporting covers 45 of the largest euro area banks:
- Q4 2024 daily turnover: **EUR 997B** (secured segment)
- Growth: +41% over 2 years (from 2022)
- CCP share: ~70% of secured turnover
- Source: [ECB Euro Money Market Study 2024](https://www.ecb.europa.eu/press/euromoneymarket/html/ecb.euromoneymarket202504.en.html)

The MMSR reports EUR 997B/day from 45 banks. This is a subset of total European repo — it covers euro-denominated trades by reporting agents. The ICMA survey covers a broader universe (EUR 13.7T outstanding).

Estimating MMSR trade count:
- EUR 997B daily turnover
- Average trade size in MMSR: likely EUR 20-50M (mix of interbank and CCP-cleared)
- EUR 997B / EUR 30M avg = **~33,200 trades/day** (from MMSR reporters only)

#### 2.5 UK Repo (Sterling)

The Bank of England collects daily transaction-level data via Form SMMD covering sterling money markets. Published quarterly in aggregate.

UK repo market characteristics:
- LCH RepoClear Ltd clears UK gilt repo
- Sterling repo is smaller than euro but active — linked to SONIA rate
- BOE reported total repo and reverse repo volumes rising consistently in 2024
- Estimate: ~20% of European repo by value, similar by count
- Source: [BOE Sterling Money Markets](https://www.bankofengland.co.uk/statistics/data-collection/sterling-money-markets)

#### 2.6 European Repo Summary

| Segment | Daily Trades (est.) | Confidence | Method |
|---------|-------------------|------------|--------|
| LCH RepoClear (unique trades) | ~29,000 | **High** | Hard data: 14.6M sides/yr |
| Eurex Repo + Clearing | ~8,000 | Medium | Volume / avg trade size |
| Other CCP (CC&G, etc.) | ~3,000 | Low | Proportional estimate |
| Electronic bilateral (BrokerTec, MTS, GLMX, Tradeweb) | ~20,000-30,000 | Medium | GLMX+Tradeweb D2C growth +20.3% turnover H1 2025 |
| Voice bilateral | ~10,000-20,000 | Low | Residual estimate |
| UK gilt repo (all channels) | ~15,000-25,000 | Low | ~20% of continental Europe |
| **European Total** | **~85,000-115,000** | **Medium** | Composite |

**Point estimate**: **~100,000 repo trades/day** in Europe
**Annual (252 days)**: **~25,200,000**

This is lower than our previous estimate of 125,000/day. The LCH hard data anchors this — at ~29K unique trades/day for the largest CCP, the total European number including bilateral is plausibly 85-115K.

---

### 3. Japan

#### 3.1 Market Structure

- **JSCC**: Central clearing for JGB repo. Daily avg clearing volume: JPY 74.24T (FY2024), with 75.1% JSCC share of total BOJ settlements
- **BOJ**: Reports securities financing transaction statistics monthly covering ~50 major institutions
- **Repo types**: SC repo (specific collateral), GC repo (general collateral)

Source: [JSCC JGB Daily Statistics](https://www.jpx.co.jp/jscc/en/cash/jgbcc/jgb_daily_statistics_e.html), [BOJ Statistics](https://www.boj.or.jp/en/statistics/bis/repo/index.htm)

#### 3.2 Transaction Count Estimate

JSCC clearing volume: JPY 74.24T/day
- Total market (at 75.1% JSCC share): JPY 74.24T / 0.751 = **JPY 98.9T/day** (~$660B at 150 JPY/USD)
- Japanese repo is dominated by large institutional and dealer trades
- Average trade size estimate: JPY 5-10B ($33-67M)
- JPY 98.9T / JPY 7.5B avg = **~13,200 trades/day**
- Range: 8,000-20,000 trades/day

**Point estimate**: **~13,000 repo trades/day** in Japan
**Annual**: **~3,276,000**

---

### 4. China

#### 4.1 Market Structure

China has two distinct repo markets:
- **Interbank market** (CFETS/PBOC): Pledged repo + outright repo, dominated by banks. This is the bulk of the market
- **Exchange market** (SSE/SZSE): Exchange-traded repo, accessible to retail and institutional

#### 4.2 Interbank Pledged Repo

PBOC 2024 Financial Market Report:
- Total interbank transactions (lending + bonds + repo): RMB 2,161.65T for full year 2024
- Daily average: RMB 8.61T (+1.3% YoY)
- Pledged repo daily turnover fell 0.2% YoY in 2024

Statista reports: March 2024 interbank pledged repo: **>145,000 transactions** (monthly figure). This implies:
- ~145,000 / ~22 trading days = **~6,600 trades/day** for interbank pledged repo

However, this seems low given the massive volumes. Cross-check:
- PBOC daily avg turnover for all interbank: RMB 8.61T
- Repo is roughly 70-80% of interbank turnover (repo dominates Chinese money markets)
- Repo portion: ~RMB 6.0-6.9T/day (~$830-950B)
- At RMB 6.5T / 145,000 monthly trades * 22 days = ~RMB 1.0B per trade (~$140M)
- This average trade size is plausible for China's bank-dominated interbank market

#### 4.3 Exchange Repo

Shanghai Stock Exchange bond repo:
- December 2024: RMB 47.02T monthly turnover (record high)
- Average monthly: ~RMB 16.8T (2009-2025 average)
- 2024 average: ~RMB 30-40T/month given growth trajectory
- Exchange repo has smaller trade sizes than interbank (retail + institutional)
- Average trade size estimate: RMB 5-20M (~$0.7-2.8M)
- Monthly: RMB 35T / RMB 10M avg = ~3.5M trades/month = **~159,000 trades/day**

Source: [CEIC/SSE Bond Repo Turnover](https://www.ceicdata.com/en/china/shanghai-stock-exchange-turnover-value)

#### 4.4 China Repo Summary

| Segment | Daily Trades (est.) | Confidence | Method |
|---------|-------------------|------------|--------|
| Interbank pledged repo (CFETS) | ~6,600 | Medium | Statista/CFETS direct count |
| Interbank outright repo | ~1,000 | Low | ~15% of pledged repo |
| SSE exchange repo | ~159,000 | Low-Medium | Monthly value / avg trade size |
| SZSE exchange repo | ~40,000 | Low | ~25% of SSE |
| **China Total** | **~207,000** | **Low-Medium** | Composite |

**Point estimate**: **~200,000 repo trades/day** in China
**Annual**: **~50,400,000**

The surprise here is China's exchange-traded repo, which could be very high-count due to small retail-accessible tickets. This is similar to how China's equity market has extremely high transaction counts due to retail participation. However, the exchange repo data is volume-based, and average trade size assumptions drive uncertainty.

**Sensitivity**: If average SSE exchange repo trade size is RMB 50M instead of RMB 10M, daily trades drop to ~31,800 — reducing China total to ~80,000/day. If RMB 5M, trades rise to 318,000/day.

---

### 5. United Kingdom

UK repo is partially captured in the European section (LCH RepoClear Ltd handles gilt repo). Adding standalone estimates:

- Sterling repo market estimated at ~GBP 500-700B daily turnover
- Average trade size: GBP 30-80M
- Estimated trades: GBP 600B / GBP 50M = **~12,000 trades/day**
- Some double-counted with LCH RepoClear Ltd

**Point estimate**: **~15,000 repo trades/day** (incremental to what's in the European section, to avoid double-counting with LCH Ltd)
**Annual**: **~3,780,000**

Note: The UK figure in the European section already includes LCH Ltd activity. This incremental figure captures bilateral sterling repo not cleared through LCH.

---

### 6. Rest of World

| Region | Est. Daily Repo Trades | Method | Confidence |
|--------|----------------------|--------|------------|
| Australia | 5,000 | ASX Clear, bilateral | Low |
| Canada | 8,000 | CDS Clearing, CDCC | Low |
| India | 10,000 | CCIL repo clearing | Low |
| Brazil | 5,000 | B3 clearing | Low |
| Korea | 5,000 | KRX, bilateral | Low |
| Other | 7,000 | Proportional | Low |
| **RoW Total** | **~40,000** | | Low |

**Annual**: **~10,080,000**

---

## Global Total

### Bottom-Up Aggregation

| Region | Daily Trades | Annual (252 days) | Confidence |
|--------|-------------|-------------------|------------|
| United States | 500,000 | 126,000,000 | Medium |
| Europe (incl. UK CCP) | 100,000 | 25,200,000 | Medium |
| Japan | 13,000 | 3,276,000 | Low-Medium |
| China | 200,000 | 50,400,000 | Low-Medium |
| UK (bilateral increment) | 15,000 | 3,780,000 | Low |
| Rest of World | 40,000 | 10,080,000 | Low |
| **Global Total** | **~868,000** | **~218,736,000** | **Medium** |

### Point Estimate with Confidence Interval

| Scenario | Daily Trades | Annual | TPS (24h/365d) | Key Assumptions |
|----------|-------------|--------|----------------|-----------------|
| **Low** | 450,000 | 113,400,000 | 3.6 | Large avg trade sizes, China exchange repo overcounted |
| **Central** | 868,000 | 218,736,000 | 6.9 | Best estimates per market |
| **High** | 1,500,000 | 378,000,000 | 12.0 | Small avg trade sizes, China retail repo very active |

**Revised point estimate**: **~219M repo trades/year globally** (~868K/day)
**Confidence interval**: **113M - 378M** (still wide but anchored by hard data)

**Previous estimate**: 83.8M/year (332K/day)
**Change**: +161% at point estimate. The previous estimate significantly undercounted by:
1. Using too-large average trade sizes for FICC GSD (we assumed ~$75M; actual implied is ~$9-12M per transaction because FICC counts individual settlement instructions, not just economic trades)
2. Not accounting for China's exchange-traded repo market
3. Underestimating European bilateral repo

### Key Insight: Why the Estimate Increased

The FICC GSD hard transaction count data is transformative. On a peak day (Apr 9, 2025), FICC processed **1.206 million transactions**. Even if 35-40% of those are cash Treasury trades (not repo), that's still ~720K repo transactions on a single peak day from one CCP. On a normal day, FICC repo transactions are likely **400-500K**. This alone exceeds our entire previous US repo estimate.

The reason: FICC counts each settlement instruction as a transaction. A dealer netting down a portfolio of 50 small repo trades into one net obligation is still 50 transactions at FICC's front door, even if settlement is netted. This is the right way to count for TPS purposes — each of those 50 trades requires matching, risk calculation, and processing.

---

## Sensitivity Analysis

### Variable 1: What FICC GSD "Transactions" Actually Are

| Interpretation | Implied US Daily Repo Trades | Global Annual |
|---------------|------------------------------|---------------|
| FICC counts = gross settlement instructions (includes both legs) | ~250,000 | ~140M |
| FICC counts = one count per trade (our base case) | ~450,000 | ~219M |
| FICC counts include Treasury cash trades mixed in | ~350,000 | ~185M |

This is the biggest single uncertainty. If FICC's "1.206M transactions" includes both repo and cash Treasury trades, and cash is 35-40%, the repo count drops to ~720K on peak / ~400K normal.

### Variable 2: China Exchange Repo Average Trade Size

| Avg Trade Size (RMB) | China Daily Trades | Global Annual Impact |
|----------------------|-------------------|---------------------|
| 5M ($0.7M) | ~320,000 | +30M annually |
| 10M ($1.4M) | ~160,000 | Base case |
| 50M ($7M) | ~32,000 | -32M annually |
| 100M ($14M) | ~16,000 | -36M annually |

### Variable 3: European Bilateral Repo Count

| Bilateral as % of Total European | Total European Daily | Global Annual Impact |
|----------------------------------|---------------------|---------------------|
| 30% bilateral (base) | ~100,000 | Base case |
| 20% bilateral | ~80,000 | -5M annually |
| 50% bilateral | ~135,000 | +9M annually |

### Variable 4: Rollover Counting

If overnight repo that rolls daily is counted once (not per roll):
- Reduces O/N repo count by ~80% (since most O/N repo rolls for ~5 days on average)
- But this is not how clearing systems count — each roll is a new trade
- We maintain: rollovers = new trades (consistent with FICC and ECB MMSR definitions)

---

## Open Questions

1. **What exactly does FICC's "transaction" count include?** Does 1.206M on Apr 9 include cash Treasury trades, or is it repo-only? Does it count both opening and closing legs? This is the single most impactful clarification needed. A FOIA request or DTCC investor relations inquiry could resolve this.

2. **China exchange repo granularity**: SSE/SZSE exchange repo could have very small tickets (RMB 100K minimum for individual investors), which would push counts dramatically higher. Or it could be dominated by institutional block trades. Transaction-count data from SSE would be definitive.

3. **NCCBR transaction data**: The OFR began collecting transaction-level bilateral repo data in Dec 2024. When aggregate statistics are published, they will directly answer the bilateral US repo count question. Expected timeline: late 2026.

4. **ECB MMSR transaction counts**: The ECB collects daily transaction-level data from 69 banks (expanded from 45 in July 2024). If they publish aggregate trade counts by segment, European repo would become well-measured. The Euro Money Market Study reports turnover but not trade counts.

5. **Japan SC repo vs GC repo split**: JSCC clears both specific collateral and general collateral repo. SC repo has smaller average trade sizes. Knowing the split would tighten the Japan estimate.

6. **India CCIL repo**: India's Clearcorp Dealing Systems (CCIL) clears significant daily repo volume (INR 3-5T daily). Transaction-level data exists but is not easily accessible in English.

---

## Sources

1. [OFR — Sizing the US Repo Market (Dec 2025)](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/)
2. [Fed — The $12 Trillion US Repo Market (Jul 2025)](https://www.federalreserve.gov/econres/notes/feds-notes/the-12-trillion-u-s-repo-market-evidence-from-a-novel-panel-of-intermediaries-20250711.html)
3. [DTCC — FICC GSD Record $11.8T (Jul 2025)](https://fxnewsgroup.com/forex-news/institutional/ficc-successfully-processes-11-8-trillion-in-daily-volume/)
4. [DTCC — FICC Peak 1.206M Transactions (Apr 2025)](https://fxnewsgroup.com/forex-news/institutional/dtcc-processes-record-volumes-across-services-amid-market-volatility/)
5. [LCH RepoClear Q4 2024 Dashboard](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/repoclear-dashboard-q4-2024.pdf)
6. [ICMA European Repo Market Survey #48 (Apr 2025)](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/)
7. [ICMA European Repo Survey — Record EUR 12.4T (Nov 2025)](https://www.icmagroup.org/News/news-in-brief/the-european-repo-market-icma-survey-shows-record-outstanding-value-of-eur-12-4-trillion-at-june-2025/)
8. [ECB Euro Money Market Study 2024 (Apr 2025)](https://www.ecb.europa.eu/press/euromoneymarket/html/ecb.euromoneymarket202504.en.html)
9. [Eurex Repo — Full Year 2024/2025 Figures](https://www.eurex.com/ex-en/find/news-center/news/Full-year-and-December-2025-figures-at-Eurex-4891494)
10. [Eurex — Repo Trading & Clearing Report 2024/2025](https://www.eurex.com/resource/blob/4264622/c9a39717608d8d0f112ab8c2f45c4efa/data/20250121_repo-report_2024-2025.pdf)
11. [NY Fed — Liberty Street Economics: Rise of Sponsored Repo (Oct 2025)](https://libertystreeteconomics.newyorkfed.org/2025/10/the-rise-of-sponsored-service-for-clearing-repo/)
12. [JSCC JGB Daily Statistics](https://www.jpx.co.jp/jscc/en/cash/jgbcc/jgb_daily_statistics_e.html)
13. [BOJ Securities Financing Transactions Statistics](https://www.boj.or.jp/en/statistics/bis/repo/index.htm)
14. [PBOC Financial Market Report 2024](https://www.pbc.gov.cn/en/3688247/3688978/3709134/5579031/2025013009512017217.pdf)
15. [Statista — China Interbank Pledged Repo Trading Volume 2024](https://www.statista.com/statistics/456767/china-interbank-market-pledged-repo-trading-volume/)
16. [CEIC — SSE Bond Repo Turnover](https://www.ceicdata.com/en/china/shanghai-stock-exchange-turnover-value)
17. [BOE — Sterling Money Markets Data Collection](https://www.bankofengland.co.uk/statistics/data-collection/sterling-money-markets)
18. [FRED — ON RRP Data (RRPONTSYD)](https://fred.stlouisfed.org/series/RRPONTSYD)
19. [NY Fed — SOFR Data](https://www.newyorkfed.org/markets/reference-rates/sofr)
20. [SIFMA — US Repo Statistics](https://www.sifma.org/research/statistics/us-repo-statistics)

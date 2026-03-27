# Fixed Income Transaction Count Triangulation

> **Created**: 2026-03-27 (Run 4)
> **Purpose**: Refine the ~7 TPS cash bond / ~35 TPS incl. repo estimates using segmented data from multiple independent sources

---

## Methodology

The original estimate of ~7 TPS for cash bonds was derived primarily from FINRA TRACE data scaled globally. This triangulation builds a **bottom-up segmented model** across three categories:

1. **Cash bonds** (government, corporate, municipal, agency/MBS, EM)
2. **Repo / reverse repo** (overnight, term, triparty, bilateral, central bank facilities)
3. **Money market instruments** (commercial paper, T-bills at auction — excluded from count as these are primary market or separate category)

For each segment we gather independent data sources and cross-check where possible.

---

## Data Sources (with citations and dates)

### Cash Bonds

| Source | Data Point | Date | URL |
|--------|-----------|------|-----|
| FINRA TRACE | ~52M US bond transactions/year (corporate + agency + securitized) | FY 2024 | [FINRA TRACE](https://www.finra.org/finra-data/fixed-income) |
| MSRB EMMA | 14.5M US municipal bond trades in 2024 (record); 17.6M in 2025 (+22%) | FY 2024/2025 | [MSRB 2024 Review](https://www.msrb.org/sites/default/files/2025-01/MSRB-2024-Municipal-Market-Year-in-Review.pdf), [MSRB 2025 Review](https://www.msrb.org/sites/default/files/2026-01/MSRB-2025-Municipal-Market-Year-in-Review.pdf) |
| Coalition Greenwich | US corporate bond market: 125,723 trades/day avg in 2024 (IG + HY) | FY 2024 | [Coalition Greenwich](https://coalitiongreenwich.crisil.com/) |
| SIFMA | US Treasury ADV $1,055B (2024); Corporate ADV $57.9B | FY 2024 | [SIFMA](https://www.sifma.org/research/statistics/) |
| Tradeweb | European Govt Bond record ADV $212.6B in 2024, up 45.6% YoY | FY 2024 | [Tradeweb](https://www.tradeweb.com/newsroom/) |
| EMTA | EM debt trading $6.116T in 2024 (annual, all EM bonds) | FY 2024 | [EMTA Volume Surveys](https://www.emta.org/activities-and-services/volume-surveys/) |

### Repo Market

| Source | Data Point | Date | URL |
|--------|-----------|------|-----|
| OFR | US repo market $12.6T daily avg exposures Q3 2025; $11.9T gross in 2024 | Q3 2025 | [OFR Blog](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/) |
| FICC GSD | Record $10T single-day clearing (Sep 30, 2024); 42% YoY growth | Sep 2024 | [DTCC](https://www.dtcc.com/news/2024/october/03/ficcs-government-securities-division-surpasses) |
| ICMA Survey #48 | European repo outstanding EUR 10.9T (Dec 2024); EUR 12.4T (Jun 2025); EUR 13.7T (Dec 2025, +25% YoY) | Dec 2024-Dec 2025 | [ICMA](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/) |
| NY Fed SOFR | SOFR underlying volume ~$1.0-2.0T/day (varies) | 2024 | [NY Fed](https://www.newyorkfed.org/markets/reference-rates/sofr) |
| Fed ON RRP | ON RRP facility declining from $2.5T peak to ~$100-200B in late 2024 | 2024 | [FRED RRPONTSYD](https://fred.stlouisfed.org/series/RRPONTSYD) |

---

## Model

### Segment 1: US Cash Bond Trades

| Sub-segment | Annual Trades | Daily Trades (252 days) | Source / Method | Confidence |
|-------------|--------------|------------------------|-----------------|------------|
| US Corporate + Agency + Securitized (TRACE) | 52,000,000 | 206,349 | FINRA TRACE direct report | High |
| US Municipal Bonds (MSRB) | 14,500,000 | 57,540 | MSRB EMMA direct report | High |
| US Treasury (est. from ADV / avg trade size) | 12,600,000 | 50,000 | $1,055B ADV / ~$21M avg trade size (institutional dominated) | Medium |
| **US Total Cash Bonds** | **79,100,000** | **313,889** | Composite | High |

**Note on TRACE coverage**: TRACE captures corporate bonds, agency debentures, ABS, and securitized products but NOT US Treasuries. Treasury trade count is estimated from ADV / average trade size, which is uncertain because the Treasury market is dominated by very large institutional/dealer trades.

**Cross-check**: Coalition Greenwich reports 125,723 corporate bond trades/day in 2024. TRACE reports 52M/year for corporate + agency + securitized = ~206K/day. The difference (~80K/day) likely reflects that TRACE includes agency and securitized products beyond just corporate bonds, and Greenwich may count both sides or include portfolio trades differently. Numbers are broadly consistent.

### Segment 2: European Cash Bond Trades

| Sub-segment | Annual Trades (est.) | Daily Trades | Source / Method | Confidence |
|-------------|---------------------|-------------|-----------------|------------|
| European Govt Bonds | 6,300,000 | 25,000 | Tradeweb ADV $212.6B / est. avg trade size ~$8.5M for govt bonds | Medium |
| European Corporate Bonds | 5,000,000 | 19,841 | Scale from US: EU corporate bond market ~60% of US by value; similar trading velocity | Low |
| European Covered Bonds / Agency | 2,500,000 | 9,921 | Est. from SIX/Euroclear settlement data | Low |
| **European Total** | **13,800,000** | **54,762** | Composite | Low-Medium |

### Segment 3: Asia-Pacific & EM Cash Bond Trades

| Sub-segment | Annual Trades (est.) | Daily Trades | Source / Method | Confidence |
|-------------|---------------------|-------------|-----------------|------------|
| Japan (JGBs + corporate) | 5,000,000 | 19,841 | Japan is ~15% of global bond outstanding; est. trading frequency lower than US | Low |
| China (onshore + offshore) | 8,000,000 | 31,746 | China interbank bond market huge by value (~$22T outstanding) but concentrated among banks, limited secondary market trading | Low |
| Other Asia (AUD, KRW, SGD, HKD, INR) | 4,000,000 | 15,873 | Composite estimate from regional exchange data | Low |
| Emerging Markets (ex-China) | 3,000,000 | 11,905 | EMTA reports $6.1T annual EM trading value; at avg ~$2M per trade = ~3M trades | Low |
| **APAC + EM Total** | **20,000,000** | **79,365** | Composite | Low |

### Segment 4: Repo / Reverse Repo

This is the critical segment. Repo is technically a fixed income transaction (sale + repurchase of a bond) but behaves like secured lending. The question of inclusion fundamentally changes the TPS number.

#### Approach: Estimate repo trade count from market size and average trade size

**US Repo Market**:
- Total daily exposures: ~$12.6T (Q3 2025, OFR)
- Segments:
  - FICC centrally cleared: $4.4T/day
  - BNY triparty (non-FICC): $3.1T/day
  - Non-centrally cleared bilateral (NCCBR): $5.0T/day

Repo trade sizes vary enormously:
- **Triparty repo**: avg trade size ~$100-500M (large institutional), some much larger
- **Bilateral dealer-to-dealer**: avg ~$50-200M
- **Sponsored repo (FICC)**: avg ~$25-100M (growing rapidly, more participants)
- **GCF repo**: avg ~$10-50M per ticket
- **Fed ON RRP**: single large transactions per counterparty (~$100B+ facility, ~50-80 counterparties daily = ~50-80 trades)

| Sub-segment | Daily Value | Est. Avg Trade Size | Est. Daily Trades | Confidence |
|-------------|------------|--------------------|--------------------|------------|
| FICC centrally cleared (GSD) | $4.4T | $75M | 58,667 | Medium |
| BNY triparty (non-FICC) | $3.1T | $200M | 15,500 | Low |
| NCCBR (bilateral) | $5.0T | $150M | 33,333 | Low |
| Fed ON RRP + SRF | ~$0.2T | $2.5B (per counterparty) | 80 | High |
| **US Repo Total** | **$12.7T** | — | **~107,580** | Low-Medium |

**European Repo Market**:
- Outstanding: EUR 13.7T at Dec 2025 (ICMA Survey)
- Turnover estimated at roughly 0.5x-1x outstanding per day for actively traded segments
- European repo is more fragmented (Eurex Repo, LCH RepoClear, BrokerTec, MTS Repo, bilateral)

| Sub-segment | Daily Value (est.) | Est. Avg Trade Size | Est. Daily Trades | Confidence |
|-------------|-------------------|--------------------|--------------------|------------|
| CCP-cleared (Eurex, LCH) | EUR 3.0T | EUR 50M | 60,000 | Low |
| ATS/electronic (BrokerTec, MTS) | EUR 1.5T | EUR 30M | 50,000 | Low |
| Bilateral / voice | EUR 1.5T | EUR 100M | 15,000 | Low |
| **European Repo Total** | **~EUR 6.0T** | — | **~125,000** | Low |

**Asia-Pacific Repo**:
- Japan repo market ~$3T outstanding; China interbank repo ~$5T daily (massive but concentrated)
- Asia repo estimated at ~50,000-100,000 trades/day

| Region | Est. Daily Repo Trades | Confidence |
|--------|----------------------|------------|
| Japan | 30,000 | Low |
| China | 50,000 | Low |
| Other Asia | 20,000 | Low |
| **APAC Repo Total** | **100,000** | Low |

#### Global Repo Summary

| Region | Est. Daily Repo Trades | Est. Annual (252 days) |
|--------|----------------------|----------------------|
| US | 107,580 | 27,110,160 |
| Europe | 125,000 | 31,500,000 |
| APAC | 100,000 | 25,200,000 |
| **Global Repo Total** | **332,580** | **83,810,160** |

**Key caveat**: Average trade sizes are the biggest uncertainty. If average repo trade size is $50M instead of $100M+, daily trade count doubles. If $200M+, it halves.

---

## Results

### Cash Bonds Only

| Region | Annual Trades | Daily Trades |
|--------|--------------|-------------|
| US | 79,100,000 | 313,889 |
| Europe | 13,800,000 | 54,762 |
| APAC + EM | 20,000,000 | 79,365 |
| **Global Cash Bonds** | **112,900,000** | **448,016** |

**TPS (cash bonds)**: 112,900,000 / (365.25 x 86,400) = **~3.6 TPS** over 24h/365d
**TPS (trading hours)**: 448,016 / (10h x 3,600s) = **~12.4 TPS** during trading hours

**Previous estimate**: ~7 TPS (using 220M trades/year over 365 days, which double-counted)
**Revised estimate**: **~3.6 TPS** (24h basis), **~12 TPS** (trading hours basis)

The original ~600K/day estimate is now refined to ~448K/day. The 52M TRACE number was previously assumed to be ~40% of global, suggesting 130M globally. Our bottom-up model yields 113M, which is consistent (US = ~70% of global by trade count, vs. ~33% by outstanding value -- this makes sense because US markets are more liquid and electronified).

### Including Repo

| Category | Annual Trades | Daily Trades |
|----------|--------------|-------------|
| Cash bonds (global) | 112,900,000 | 448,016 |
| Repo (global) | 83,810,160 | 332,580 |
| **Total Fixed Income** | **196,710,160** | **780,596** |

**TPS (incl. repo)**: 196,710,160 / (365.25 x 86,400) = **~6.2 TPS** over 24h/365d
**TPS (trading hours)**: 780,596 / (10h x 3,600s) = **~21.7 TPS** during trading hours

### Point Estimates with Confidence Intervals

| Segment | Point Estimate (annual) | Low Bound | High Bound | Confidence |
|---------|------------------------|-----------|------------|------------|
| US Cash Bonds | 79.1M | 70M | 85M | High (TRACE + MSRB anchored) |
| European Cash Bonds | 13.8M | 8M | 20M | Low-Medium |
| APAC + EM Cash Bonds | 20.0M | 10M | 35M | Low |
| **Cash Bonds Total** | **112.9M** | **88M** | **140M** | Medium |
| US Repo | 27.1M | 15M | 50M | Low-Medium |
| European Repo | 31.5M | 15M | 60M | Low |
| APAC Repo | 25.2M | 10M | 50M | Low |
| **Repo Total** | **83.8M** | **40M** | **160M** | Low |
| **Grand Total** | **196.7M** | **128M** | **300M** | Low-Medium |

**TPS Range**:
- Cash bonds only: **2.8 - 4.4 TPS** (point: 3.6)
- Including repo: **4.1 - 9.5 TPS** (point: 6.2)
- Trading hours, incl. repo: **14 - 33 TPS** (point: 22)

---

## Sensitivity Analysis

### Key Variable: Average Repo Trade Size

The repo trade count estimate is extremely sensitive to assumed average trade size.

| Assumed Avg Repo Trade Size | Global Daily Repo Trades | Total FI Daily Trades | Total FI TPS (24h) |
|---------------------------|-------------------------|----------------------|-------------------|
| $50M | 665,160 | 1,113,176 | 12.9 |
| $75M (low end of our model) | 443,440 | 891,456 | 10.3 |
| $100M | 332,580 | 780,596 | 9.0 |
| $150M (base case avg) | 221,720 | 669,736 | 7.7 |
| $250M | 133,032 | 581,048 | 6.7 |

**Our model uses a weighted average of ~$100M across all repo segments**, reflecting a mix of small GCF/sponsored tickets and large bilateral/triparty trades.

### Key Variable: Non-US Cash Bond Trade Count

US trade count is well-anchored by TRACE and MSRB. Non-US is the major uncertainty.

| US Share of Global Cash Bond Trades | Implied Global Daily Trades | TPS (24h) |
|------------------------------------|---------------------------|-----------|
| 50% (more global) | 627,778 | 7.3 |
| 60% | 523,148 | 6.0 |
| 70% (base case) | 448,413 | 5.2 |
| 80% (US dominated) | 392,361 | 4.5 |

### Should Repo Be Included?

**Arguments for inclusion**:
- Repo IS a bond transaction — it involves sale and repurchase of fixed income securities
- Our taxonomy defines the category as "fixed income transactions"
- Excluding repo would undercount the actual transaction load on fixed income infrastructure
- Central clearing mandates (SEC 2025 rule for US Treasuries) mean more repo flows through transaction processing systems

**Arguments for exclusion / separate reporting**:
- Repo functions as secured money market lending, not bond "trading"
- Most repo transactions are rolled overnight, mechanically — they don't reflect investment decisions
- Including repo makes fixed income look much busier than the cash bond market really is
- Repo overlaps conceptually with the "money markets" category

**Recommendation**: Report **both figures** with clear labeling. Use cash bonds for comparing trading velocity across asset classes; use the inclusive figure for infrastructure capacity planning.

---

## Open Questions & Data Gaps

1. **Repo trade count data simply does not exist** in aggregated public form. The OFR's December 2024 NCCBR data collection is the first attempt at transaction-level US repo data, but it's not yet published in aggregate. This is the single biggest gap.

2. **Non-US bond trade counts** remain poorly reported. European and Asian bond markets report value (ADV) but rarely trade counts. Our estimates for these regions are derived from value / assumed trade size, which is circular.

3. **Treasury market trade count**: Unlike corporate bonds (TRACE), US Treasury trades are not reported to a consolidated tape. FINRA began publishing Treasury aggregate statistics in 2020, but trade counts are not published. The SEC's Treasury market study may eventually produce this data.

4. **China interbank bond market**: China has the world's second-largest bond market (~$22T outstanding) but trade count data is extremely opaque. CCDC and Shanghai Clearing House report settlement volumes but not trade counts in accessible English-language publications.

5. **Double counting in TRACE**: TRACE reports both sides of inter-dealer trades. The 52M figure may overcount actual "economic" transactions by 10-15% for inter-dealer activity. However, TRACE de-duplicates customer-to-dealer trades.

6. **Municipal bond data (MSRB)** is a high-confidence anchor: 14.5M trades in 2024 is a direct count, not an estimate. The 22% jump to 17.6M in 2025 shows this market is electronifying rapidly.

7. **2025 acceleration**: Multiple indicators suggest trade counts grew significantly in 2025 vs 2024:
   - MSRB: 17.6M munis trades (+22%)
   - ISDA IRD: H1 2025 trade count +27.5% vs H1 2024
   - FICC GSD: 42% YoY activity growth
   - This suggests 2024 numbers may already be conservative as a "current" figure.

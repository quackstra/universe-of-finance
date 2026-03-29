---
title: "Fixed Income & Bond Markets — Report"
parent: Traditional Finance
grand_parent: Explore
nav_order: 2
---

# Fixed Income / Bond Markets — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #5
> **Last Updated**: 2026-03-28
> **Transaction Definition**: One bond trade (purchase or sale) between counterparties, including government bonds, corporate bonds, municipal bonds, and repo transactions

---

## Executive Summary

The global fixed income market is valued at approximately **$145 trillion outstanding** (2024), making it one of the largest asset classes on Earth. However, bonds trade far less frequently than equities — most bonds are held to maturity and the market is dominated by institutional, over-the-counter trading.

**Revised estimate (Run 5 repo deep dive)**: A bottom-up segmented model yields approximately **~448,000 cash bond trades per day** globally, for an average TPS of **~3.6** over a 24h/365d basis (~12 TPS during trading hours). The US accounts for ~70% of global cash bond trade count, anchored by FINRA TRACE (52M/year) and MSRB (14.5M municipal trades/year — a record in 2024).

**Repo deep dive (Run 5)**: Using hard transaction count data from FICC GSD (peak 1.206M transactions on Apr 9, 2025) and LCH RepoClear (14.6M trade sides in 2024), we now estimate **~868,000 repo trades/day** globally (~219M/year), bringing total fixed income TPS to **~10.5** (24h basis). The previous repo estimate of ~333K/day significantly undercounted because it assumed average trade sizes of ~$75-150M, while FICC data implies ~$9-12M per transaction (FICC counts each settlement instruction). Confidence interval narrows from 4x to ~3x: **113M-378M annually** (vs previous 40M-160M). See [repo deep dive](workings/repo-deep-dive.md).

US Treasury ADV surpassed **$1 trillion for the first time in 2024**, corporate bond ADV reached $57.9 billion (+11.5% YoY), and MSRB reported 14.5M municipal bond trades (up to 17.6M in 2025, +22%), reflecting the ongoing electronification of fixed income markets.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS — cash bonds only | **~3.6** | 🟡 Medium |
| Average TPS — including repo | **~10.5** | 🟡 Medium |
| Peak TPS (est.) | **~80** | 🔴 Low |
| Daily trade count — cash bonds | ~448,000 | 🟡 Medium |
| Daily trade count — repo (est.) | ~868,000 | 🟡 Medium |
| Daily value — US Treasuries ADV | $1,055B | 🟢 High |
| Daily value — US Corporates ADV | $57.9B | 🟢 High |
| Daily value — Tradeweb ADV (Oct 2024) | $2.35T | 🟢 High |
| US corporate bond trades/day (Coalition Greenwich) | 125,723 | 🟢 High |
| US municipal bond trades (MSRB, 2024) | 14.5M/year | 🟢 High |
| FICC GSD peak transactions (Apr 9, 2025) | 1,206,000 | 🟢 High |
| LCH RepoClear trade sides (2024) | 14.6M/year | 🟢 High |
| Market outstanding (global, 2024) | $145T | 🟢 High |

**Methodology**: Bottom-up segmented model. Cash bonds: US 79.1M (TRACE + MSRB + Treasury) + Europe 13.8M + APAC/EM 20M = 112.9M/year. Repo: anchored by FICC GSD hard transaction counts (peak 1.206M/day, normal ~600-750K/day, repo portion ~400-500K/day) and LCH RepoClear (14.6M trade sides/year = ~29K unique trades/day). Global repo: US ~500K/day + Europe ~100K/day + China ~200K/day + Japan ~13K/day + RoW ~55K/day = ~868K/day = ~219M/year. See [repo deep dive](workings/repo-deep-dive.md), [count triangulation](workings/count-triangulation.md), and [calculations](workings/calculations.md).

**Sources**: [SIFMA](https://www.sifma.org/research/statistics/us-treasury-securities-statistics), [FINRA TRACE](https://www.finra.org/finra-data/fixed-income), [MSRB](https://www.msrb.org/sites/default/files/2025-01/MSRB-2024-Municipal-Market-Year-in-Review.pdf), [OFR](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/), [DTCC FICC](https://fxnewsgroup.com/forex-news/institutional/dtcc-processes-record-volumes-across-services-amid-market-volatility/), [LCH RepoClear](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/repoclear-dashboard-q4-2024.pdf), [Coalition Greenwich](https://coalitiongreenwich.crisil.com/)

---

## 2. Annual Volume (2024)

### 2.1 US Fixed Income (SIFMA / TRACE)

| Asset Class | ADV (Value) | YoY Change | Est. Daily Trades | Source |
|-------------|-------------|------------|-------------------|--------|
| US Treasuries | $1,055B | +15.3% | ~150,000 | [SIFMA](https://www.sifma.org/research/statistics/us-treasury-securities-statistics) |
| US Corporate Bonds | $57.9B | +11.5% | ~85,000 | [SIFMA](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics) |
| US Agency / MBS | ~$350B | — | ~50,000 | SIFMA est. |
| US Municipal Bonds | ~$15B | — | ~30,000 | MSRB est. |
| **US Total (cash bonds)** | **~$1,478B** | — | **~315,000** | Composite |

TRACE reported approximately 52 million total bond transactions in 2024, including corporate, agency, and securitized products. This includes ~19 million investment-grade corporate bond trades.

### 2.2 European Fixed Income (Tradeweb / MTS)

| Metric | Value | Source |
|--------|-------|--------|
| Tradeweb ADV (Oct 2024) | $2.35T | [Tradeweb](https://www.tradeweb.com/newsroom/media-center/news-releases/) |
| European Govt Bond ADV | $42.9B | Tradeweb (Jul 2024) |

### 2.3 Repo Market (Run 5 Deep Dive)

| Region | Daily Exposure | Est. Daily Trades | Annual Trades | Source |
|--------|---------------|-------------------|---------------|--------|
| US (FICC + BNY tri-party + NCCBR) | $12.6T | ~500,000 | ~126M | [OFR](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/), [DTCC](https://fxnewsgroup.com/forex-news/institutional/dtcc-processes-record-volumes-across-services-amid-market-volatility/) |
| Europe (LCH + Eurex + bilateral + UK) | ~EUR 6T | ~100,000 | ~25.2M | [LCH](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/repoclear-dashboard-q4-2024.pdf), [ICMA](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/) |
| China (interbank + exchange) | ~RMB 6.5T | ~200,000 | ~50.4M | [PBOC](https://www.pbc.gov.cn/en/3688247/3688978/3709134/5579031/2025013009512017217.pdf), [CEIC/SSE](https://www.ceicdata.com/en/china/shanghai-stock-exchange-turnover-value) |
| Japan (JSCC + bilateral) | ~JPY 99T | ~13,000 | ~3.3M | [JSCC](https://www.jpx.co.jp/jscc/en/cash/jgbcc/jgb_daily_statistics_e.html) |
| UK (bilateral increment) | ~GBP 600B | ~15,000 | ~3.8M | [BOE](https://www.bankofengland.co.uk/statistics/data-collection/sterling-money-markets) |
| Rest of World | — | ~40,000 | ~10.1M | Composite |
| **Global repo** | **~$20T+/day** | **~868,000** | **~219M** | Composite |

**Key anchors**: FICC GSD peak of 1.206M transactions (Apr 9, 2025) and LCH RepoClear 14.6M trade sides (FY2024). See [repo deep dive](workings/repo-deep-dive.md) for full methodology. Confidence interval: 113M-378M annually.

---

## 3. Historic Trend

### US Treasury ADV (SIFMA)

| Year | Treasury ADV | YoY Change |
|------|-------------|------------|
| 2019 | $594B | — |
| 2020 | $632B | +6.4% |
| 2021 | $588B | -7.0% |
| 2022 | $632B | +7.5% |
| 2023 | $915B | +44.8% |
| 2024 | $1,055B | +15.3% |

### US Corporate Bond ADV (SIFMA)

| Year | Corporate ADV | YoY Change |
|------|-------------|------------|
| 2019 | $31.2B | — |
| 2020 | $36.1B | +15.7% |
| 2021 | $36.4B | +0.8% |
| 2022 | $36.8B | +1.1% |
| 2023 | $51.9B | +41.0% |
| 2024 | $57.9B | +11.5% |

### Global Outstanding (SIFMA)

| Year | Global Outstanding |
|------|--------------------|
| 2019 | $115T |
| 2020 | $124T |
| 2021 | $127T |
| 2022 | $130T |
| 2023 | $141T |
| 2024 | $145T |

---

## 4. Growth Rate Analysis

| Metric | Period | CAGR |
|--------|--------|------|
| US Treasury ADV | 2019-2024 | 12.2% |
| US Corporate ADV | 2019-2024 | 13.2% |
| Global outstanding | 2019-2024 | 4.7% |
| Tradeweb ADV | 2023-2024 | ~35% |

**Key driver**: Electronification. Electronic bond trading (via Tradeweb, MarketAxess, Bloomberg) has been growing rapidly, increasing both transparency and trading velocity. Tradeweb's ADV grew ~35% YoY in 2024.

---

## 5. Projections

### 5.1 Baseline (CAGR 8% on trade count)

| Year | Global Daily Trades (cash) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 448K | 3.6 | 10.5 |
| 2030 | 711K | 5.0 | 14.7 |
| 2035 | 1.04M | 6.9 | 20.2 |

### 5.2 High Growth (CAGR 12%)

| Year | Global Daily Trades (cash) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 448K | 3.6 | 10.5 |
| 2030 | 885K | 6.4 | 18.7 |
| 2035 | 1.56M | 11.3 | 33.0 |

### 5.3 Conservative (CAGR 4%)

| Year | Global Daily Trades (cash) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 448K | 3.6 | 10.5 |
| 2030 | 567K | 4.2 | 12.2 |
| 2035 | 690K | 4.9 | 14.4 |

**Scenario rationale**:
- **Baseline**: Continued electronification drives ~8% growth in trade frequency, with modest growth in outstanding.
- **High Growth**: All-to-all trading platforms, tokenized bonds, and algorithmic market-making radically increase trading velocity.
- **Conservative**: Bond markets remain buy-and-hold dominated; electronification slows after low-hanging fruit is captured.

---

## 6. Key Findings

1. **Fixed income is a high-value, low-frequency market.** At ~3.6 TPS for cash bonds (revised down from ~7), it is one of the lowest-frequency categories in the Universe of Finance despite being one of the largest by value ($145T outstanding). The previous estimate overstated global trade counts by assuming the US was only 40% of global activity; bottom-up modeling shows the US is closer to 70% by trade count.

2. **The repo market is nearly 2x cash bonds by trade count (Run 5 revision).** Repo adds ~868K trades/day (vs ~448K for cash bonds), bringing total FI TPS to ~10.5. The Run 5 deep dive leveraged hard transaction count data from FICC GSD (peak 1.206M transactions/day) and LCH RepoClear (14.6M trade sides/year), revealing that previous estimates significantly undercounted by assuming $75-150M average trade sizes when FICC data implies ~$9-12M per transaction. China's exchange-traded repo (~160K trades/day) is also a material new component. Confidence has improved from Low to Medium, though the range remains wide (113M-378M annually).

3. **US Treasury ADV crossed $1 trillion for the first time in 2024**, driven by rate volatility and electronic trading adoption. FICC GSD cleared a record $10T in a single day (Sep 30, 2024).

4. **Municipal bonds are a high-confidence anchor**: MSRB reported 14.5M trades in 2024 (first year above 14M) and 17.6M in 2025 (+22%). This direct count data is more reliable than most fixed income estimates.

5. **Electronification is accelerating trade counts**: US corporate bond trading averaged 125,723 trades/day in 2024 (Coalition Greenwich). Tradeweb ADV grew ~35% YoY. MSRB trade counts surged 22% in 2025. Trade frequency is growing faster than market value.

6. **Bond markets are structurally illiquid by count**: Unlike equities, most bonds are unique instruments (distinct CUSIPs) with limited secondary market activity. Corporate bonds average ~1 trade per bond per week.

7. **Non-US trade count data remains the biggest gap**: Europe and APAC bond trade counts are estimated, not observed. The US has TRACE and MSRB; no equivalent exists globally.

---

## 7. Data Quality & Limitations

- **Transaction count**: TRACE provides reliable US corporate bond trade counts (~52M/year). Global estimates are extrapolated. Confidence: 🔴 Low for global, 🟢 High for US TRACE.
- **Repo trade counts**: No centralized source. ICMA reports European repo value but not trade counts. Estimate: 🔴 Low.
- **Tradeweb/MarketAxess**: Report ADV by value, not trade counts. Confidence for value data: 🟢 High.
- **Non-US markets**: European, Asian, and EM bond market trade counts are poorly reported.
- **Double-counting risk**: A single bond trade may generate clearing, settlement, and custodial entries — counted once per taxonomy rules.

---

## Open Questions & Triangulation Opportunities

> **Run 5 update (2026-03-28)**: Repo deep dive completed. FICC GSD hard transaction count data (peak 1.206M/day) and LCH RepoClear (14.6M sides/year) anchor the revised estimate. Global repo revised from ~84M to ~219M trades/year. See [workings/repo-deep-dive.md](workings/repo-deep-dive.md).

### What We Can't Directly Observe
- **FICC GSD transaction definition**: Does the 1.206M peak include both cash Treasury trades and repo? Both opening and closing legs? This is the single most impactful clarification needed. A DTCC investor relations inquiry could resolve this.
- **OFR NCCBR aggregate counts**: The OFR began collecting transaction-level bilateral repo data in Dec 2024. When aggregate statistics are published (expected late 2026), they will directly answer the bilateral US repo count question.
- **China exchange repo granularity**: SSE/SZSE exchange repo could have very small tickets (retail-accessible), pushing counts dramatically higher, or be dominated by institutional blocks. Transaction-count data from SSE would be definitive.
- **Non-US bond trade counts**: TRACE captures US corporate and agency bonds (~52M trades/year) and MSRB captures munis (14.5M). European, Asian, and EM bond market trade counts are estimated from ADV / assumed trade sizes.
- **US Treasury trade count**: Unlike corporate bonds (TRACE) and munis (MSRB), US Treasury trades are not reported to a consolidated tape by trade count. Our 12.6M estimate is derived from $1,055B ADV / ~$21M avg trade size.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| US repo trade count | Use SOFR underlying volume (~$900B-$1.5T/day) divided by estimated avg repo size ($50-200M) | [NY Fed SOFR data](https://www.newyorkfed.org/markets/reference-rates/sofr) — daily volume and rate; FRED SOFRVOL series | 🟡 Medium |
| European repo trade count | ICMA survey outstanding (EUR 10.9T at Dec 2023, EUR 12.4T at Jun 2025) + daily turnover growth (+25.9% H2 2024) | [ICMA Survey #48-49](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/) | 🟡 Medium |
| Corporate bond e-trading % | Tradeweb + MarketAxess combined ADV as proxy for electronic share | Tradeweb ADV $2.35T (Oct 2024); MarketAxess ADV ~$8.5B (IG corporates) | 🟢 High (for platforms) |
| Non-US bond trade count | Scale US TRACE data by US share of global outstanding (~33%) | SIFMA fact book: US = ~$51T of $145T global outstanding | 🟡 Medium |
| Repo-to-cash bond ratio | Compare repo ADV (~$10T) to cash bond ADV (~$1.5T) as a multiplier | Both available from SIFMA/Fed/ICMA | 🟢 High |

### Key Modeling Questions
- What is the actual daily trade count in the global repo market? Even a rough estimate (e.g., 1-5 million trades/day) would dramatically change the fixed income TPS calculation.
- As bond trading electronifies (Tradeweb ADV grew ~35% YoY), does trade count grow faster than value? (Electronic platforms enable smaller trade sizes.)
- How should triparty repo be counted? (A single triparty repo may involve hundreds of underlying securities but is booked as one transaction.)
- Will tokenized bonds (e.g., on blockchain rails) increase trading velocity for traditionally illiquid instruments?

### Reference Comparisons
- **SOFR daily volume**: ~$900B-$1.5T/day of actual repo transactions underpin SOFR — this provides a high-confidence lower bound for US repo market activity ([FRED SOFRVOL](https://fred.stlouisfed.org/series/SOFRVOL))
- **ICMA European repo**: Record EUR 12.4T outstanding at June 2025; average daily turnover grew 25.9% in H2 2024 — European repo is growing faster than US ([ICMA](https://www.icmagroup.org/News/news-in-brief/the-european-repo-market-icma-survey-shows-record-outstanding-value-of-eur-12-4-trillion-at-june-2025/))
- **Tradeweb vs. MarketAxess**: Tradeweb focuses on rates/govts ($2.35T ADV), MarketAxess on credit ($8.5B ADV) — together they proxy electronic bond trading velocity
- **TRACE coverage**: ~52M transactions/year in US bonds provides the most reliable single-country trade count anchor for global extrapolation

---

## 8. Sources

1. [SIFMA — US Treasury Securities Statistics](https://www.sifma.org/research/statistics/us-treasury-securities-statistics)
2. [SIFMA — US Corporate Bonds Statistics](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics)
3. [SIFMA — Capital Markets Fact Book 2024](https://www.sifma.org/wp-content/uploads/2023/07/2024-SIFMA-Capital-Markets-Factbook.pdf)
4. [FINRA — TRACE Fixed Income Data](https://www.finra.org/finra-data/fixed-income)
5. [Tradeweb — October 2024 Volume Report](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-reports-october-2024-total-trading-volume-of-$54.7-trillion-and-average-daily-volume-of-$2.35-trillion/)
6. [Tradeweb — July 2024 Volume Report](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-reports-july-2024-total-trading-volume-of-$40.5-trillion-and-average-daily-volume-of-$1.82-trillion/)
7. [ICMA — European Repo Market Survey #48 (Dec 2024)](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/)
8. [SIX Group — Fixed Income Data Infographic 2024](https://www.six-group.com/dam/download/financial-information/reference-pricing-data/fixed-income-data/six-fixed-income-data-infographic.pdf)
9. [Bloomberg — Looking Back at 2024: Fixed Income](https://www.bloomberg.com/professional/insights/markets/looking-back-at-2024-fixed-income/)

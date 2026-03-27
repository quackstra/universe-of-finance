# Fixed Income / Bond Markets — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #5
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One bond trade (purchase or sale) between counterparties, including government bonds, corporate bonds, municipal bonds, and repo transactions

---

## Executive Summary

The global fixed income market is valued at approximately **$145 trillion outstanding** (2024), making it one of the largest asset classes on Earth. However, bonds trade far less frequently than equities — most bonds are held to maturity and the market is dominated by institutional, over-the-counter trading.

**Revised estimate (Run 4 triangulation)**: A bottom-up segmented model yields approximately **~448,000 cash bond trades per day** globally, for an average TPS of **~3.6** over a 24h/365d basis (~12 TPS during trading hours). The US accounts for ~70% of global cash bond trade count, anchored by FINRA TRACE (52M/year) and MSRB (14.5M municipal trades/year — a record in 2024).

The repo market adds substantial transaction volume but is extremely difficult to count — no centralized source reports global repo trade counts. Modeling from market size and estimated average trade sizes, we estimate **~333,000 repo trades/day** globally, bringing the total fixed income TPS to **~6.2** (24h basis). However, repo trade count carries a wide confidence interval (40M-160M annually) driven by uncertainty in average trade size.

US Treasury ADV surpassed **$1 trillion for the first time in 2024**, corporate bond ADV reached $57.9 billion (+11.5% YoY), and MSRB reported 14.5M municipal bond trades (up to 17.6M in 2025, +22%), reflecting the ongoing electronification of fixed income markets.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS — cash bonds only | **~3.6** | 🟡 Medium |
| Average TPS — including repo | **~6.2** | 🔴 Low |
| Peak TPS (est.) | **~50** | 🔴 Low |
| Daily trade count — cash bonds | ~448,000 | 🟡 Medium |
| Daily trade count — repo (est.) | ~333,000 | 🔴 Low |
| Daily value — US Treasuries ADV | $1,055B | 🟢 High |
| Daily value — US Corporates ADV | $57.9B | 🟢 High |
| Daily value — Tradeweb ADV (Oct 2024) | $2.35T | 🟢 High |
| US corporate bond trades/day (Coalition Greenwich) | 125,723 | 🟢 High |
| US municipal bond trades (MSRB, 2024) | 14.5M/year | 🟢 High |
| Market outstanding (global, 2024) | $145T | 🟢 High |

**Methodology**: Bottom-up segmented model. US cash bonds: FINRA TRACE 52M + MSRB 14.5M + Treasury est. 12.6M = 79.1M/year. Europe: est. 13.8M. APAC/EM: est. 20M. Total cash: 112.9M/year. Repo: modeled from OFR US repo ($12.6T daily exposure) and ICMA European repo (EUR 13.7T outstanding), divided by estimated avg trade sizes. See [count triangulation](workings/count-triangulation.md) and [calculations](workings/calculations.md).

**Sources**: [SIFMA](https://www.sifma.org/research/statistics/us-treasury-securities-statistics), [FINRA TRACE](https://www.finra.org/finra-data/fixed-income), [MSRB](https://www.msrb.org/sites/default/files/2025-01/MSRB-2024-Municipal-Market-Year-in-Review.pdf), [OFR](https://www.financialresearch.gov/the-ofr-blog/2025/12/04/sizing-us-repo-market/), [Coalition Greenwich](https://coalitiongreenwich.crisil.com/)

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

### 2.3 Repo Market

| Region | Daily Turnover | Outstanding | Source |
|--------|---------------|-------------|--------|
| European repo (EU) | EUR 2,741B/day | — | [ICMA Survey #48](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/market-data/icma-european-repo-market-survey/) |
| European repo (UK) | EUR 2,168B/day | — | ICMA Survey #48 |
| US repo (triparty + bilateral) | ~$4T/day | ~$5T outstanding | Federal Reserve |
| **Global repo est.** | **~$10T/day** | **~$15T outstanding** | Composite |

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
| 2024 | 448K | 3.6 | 6.2 |
| 2030 | 711K | 5.0 | 8.6 |
| 2035 | 1.04M | 6.9 | 11.8 |

### 5.2 High Growth (CAGR 12%)

| Year | Global Daily Trades (cash) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 448K | 3.6 | 6.2 |
| 2030 | 885K | 6.4 | 11.0 |
| 2035 | 1.56M | 11.3 | 19.4 |

### 5.3 Conservative (CAGR 4%)

| Year | Global Daily Trades (cash) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 448K | 3.6 | 6.2 |
| 2030 | 567K | 4.2 | 7.2 |
| 2035 | 690K | 4.9 | 8.4 |

**Scenario rationale**:
- **Baseline**: Continued electronification drives ~8% growth in trade frequency, with modest growth in outstanding.
- **High Growth**: All-to-all trading platforms, tokenized bonds, and algorithmic market-making radically increase trading velocity.
- **Conservative**: Bond markets remain buy-and-hold dominated; electronification slows after low-hanging fruit is captured.

---

## 6. Key Findings

1. **Fixed income is a high-value, low-frequency market.** At ~3.6 TPS for cash bonds (revised down from ~7), it is one of the lowest-frequency categories in the Universe of Finance despite being one of the largest by value ($145T outstanding). The previous estimate overstated global trade counts by assuming the US was only 40% of global activity; bottom-up modeling shows the US is closer to 70% by trade count.

2. **The repo market is significant but not as dominant by trade count as by value.** Repo adds ~333K trades/day (vs ~448K for cash bonds), bringing total FI TPS to ~6.2. However, repo trade count is the most uncertain number in the entire model — no public source reports it, and estimates swing 4x depending on average trade size assumptions.

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

> **Run 4 update (2026-03-27)**: Detailed count triangulation completed. See [workings/count-triangulation.md](workings/count-triangulation.md) for the full segmented model, sensitivity analysis, and confidence intervals.

### What We Can't Directly Observe
- **Global repo transaction count**: The OFR's Dec 2024 NCCBR data collection is the first attempt at transaction-level US repo data, but aggregate trade counts are not yet published. Our model estimates ~333K repo trades/day globally, but this is sensitive to average trade size assumptions (40M-160M annual range).
- **Non-US bond trade counts**: TRACE captures US corporate and agency bonds (~52M trades/year) and MSRB captures munis (14.5M). European, Asian, and EM bond market trade counts are estimated from ADV / assumed trade sizes.
- **US Treasury trade count**: Unlike corporate bonds (TRACE) and munis (MSRB), US Treasury trades are not reported to a consolidated tape by trade count. Our 12.6M estimate is derived from $1,055B ADV / ~$21M avg trade size.
- **Electronic vs. voice bond trading split**: Tradeweb and MarketAxess report ADV by value, but the share of bond trades executed electronically vs. voice across all market segments is not centrally tracked.

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

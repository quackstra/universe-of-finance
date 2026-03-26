# Fixed Income / Bond Markets — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #5
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One bond trade (purchase or sale) between counterparties, including government bonds, corporate bonds, municipal bonds, and repo transactions

---

## Executive Summary

The global fixed income market is valued at approximately **$145 trillion outstanding** (2024), making it one of the largest asset classes on Earth. However, bonds trade far less frequently than equities — most bonds are held to maturity and the market is dominated by institutional, over-the-counter trading. We estimate approximately **500,000-700,000 bond trades per day** globally (excluding repo), yielding a modest average TPS of roughly **6-8**.

The repo market dwarfs cash bond trading by value, with the European repo market alone exceeding EUR 10 trillion outstanding and daily turnover of ~EUR 5 trillion. Including repo, daily transaction counts may reach **2-4 million**, pushing TPS into the **23-46** range.

US Treasury ADV surpassed **$1 trillion for the first time in 2024**, and corporate bond ADV reached $57.9 billion (+11.5% YoY), reflecting the ongoing electronification of fixed income markets.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS — cash bonds only (est.) | **~7** | 🔴 Low |
| Average TPS — including repo (est.) | **~35** | 🔴 Low |
| Peak TPS (est.) | **~100** | 🔴 Low |
| Daily trade count — cash bonds (est.) | ~600,000 | 🔴 Low |
| Daily trade count — repo (est.) | ~2.5M | 🔴 Low |
| Daily value — US Treasuries ADV | $1,055B | 🟢 High |
| Daily value — US Corporates ADV | $57.9B | 🟢 High |
| Daily value — Tradeweb ADV (Oct 2024) | $2.35T | 🟢 High |
| Market outstanding (global, 2024) | $145T | 🟢 High |

**Methodology**: FINRA TRACE reported ~52 million bond transactions in the US in 2024. The US represents roughly 40% of global bond trading activity, suggesting ~130 million global cash bond trades/year or ~520K/day over 252 trading days. Adding repo transactions (estimated from ICMA European survey) brings the total substantially higher. See [calculations](workings/calculations.md).

**Sources**: [SIFMA](https://www.sifma.org/research/statistics/us-treasury-securities-statistics), [Tradeweb](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-reports-october-2024-total-trading-volume-of-$54.7-trillion-and-average-daily-volume-of-$2.35-trillion/), [FINRA TRACE](https://www.finra.org/finra-data/fixed-income)

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

### 5.1 Baseline (CAGR 8% on ADV)

| Year | Global Daily Trades (est.) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 600K | 7 | 35 |
| 2030 | 950K | 11 | 55 |
| 2035 | 1.4M | 16 | 80 |

### 5.2 High Growth (CAGR 12%)

| Year | Global Daily Trades (est.) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 600K | 7 | 35 |
| 2030 | 1.2M | 14 | 70 |
| 2035 | 2.1M | 24 | 120 |

### 5.3 Conservative (CAGR 4%)

| Year | Global Daily Trades (est.) | TPS (cash bonds) | TPS (incl. repo) |
|------|---------------------------|-------------------|-------------------|
| 2024 | 600K | 7 | 35 |
| 2030 | 760K | 9 | 44 |
| 2035 | 925K | 11 | 54 |

**Scenario rationale**:
- **Baseline**: Continued electronification drives ~8% growth in trade frequency, with modest growth in outstanding.
- **High Growth**: All-to-all trading platforms, tokenized bonds, and algorithmic market-making radically increase trading velocity.
- **Conservative**: Bond markets remain buy-and-hold dominated; electronification slows after low-hanging fruit is captured.

---

## 6. Key Findings

1. **Fixed income is a high-value, very-low-frequency market.** At ~7 TPS for cash bonds only, it is one of the lowest-frequency categories in the Universe of Finance despite being one of the largest by value ($145T outstanding).

2. **The repo market vastly exceeds cash bond trading** in both value (~$10T/day vs ~$1.5T/day) and likely transaction count. Including repo brings estimated TPS up to ~35.

3. **US Treasury ADV crossed $1 trillion for the first time in 2024**, driven by rate volatility and electronic trading adoption.

4. **Electronification is the key growth driver**: Tradeweb ADV grew ~35% YoY. As more bonds move from voice trading to electronic platforms, trade frequency will increase even if total market value grows slowly.

5. **TRACE data gap**: TRACE captures US corporate and agency bonds but does NOT cover US Treasuries traded outside of TRACE-eligible platforms, nor any non-US markets. Global trade count estimates require significant extrapolation.

6. **Bond markets are structurally illiquid by count**: Unlike equities, most bonds are unique instruments (distinct CUSIPs) with limited secondary market activity. Corporate bonds average ~1 trade per bond per week.

---

## 7. Data Quality & Limitations

- **Transaction count**: TRACE provides reliable US corporate bond trade counts (~52M/year). Global estimates are extrapolated. Confidence: 🔴 Low for global, 🟢 High for US TRACE.
- **Repo trade counts**: No centralized source. ICMA reports European repo value but not trade counts. Estimate: 🔴 Low.
- **Tradeweb/MarketAxess**: Report ADV by value, not trade counts. Confidence for value data: 🟢 High.
- **Non-US markets**: European, Asian, and EM bond market trade counts are poorly reported.
- **Double-counting risk**: A single bond trade may generate clearing, settlement, and custodial entries — counted once per taxonomy rules.

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

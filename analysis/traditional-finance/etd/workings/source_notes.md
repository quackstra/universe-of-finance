# Exchange-Traded Derivatives — Source Notes

> Extended notes on each data source used in this analysis.

## Primary Sources

### 1. FIA (Futures Industry Association)

- **URL**: https://www.fia.org/etd-volume-reports
- **Type**: Industry body / data aggregator
- **Coverage**: 85 exchanges operated by 54 companies in 33 countries
- **Frequency**: Monthly reports, annual survey
- **Key report**: [2024 Annual ETD Volume Review](https://www.fia.org/fia/articles/2024-annual-etd-volume-review)
- **Metric**: Contracts traded (not notional value)
- **Reliability**: 🟢 High — gold standard for ETD volume data
- **Notes**:
  - FIA changed methodology over the years; pre-2018 data may use slightly different exchange coverage
  - ETD Tracker provides interactive monthly data but requires login for full detail
  - Annual volume survey is the most comprehensive single publication
  - 2024 total: **205.34 billion contracts** (up 51% from 2023)
  - FIA's coverage is broader than WFE, explaining the ~25B gap between the two

### 2. WFE (World Federation of Exchanges)

- **URL**: https://www.world-exchanges.org/our-work/statistics
- **Type**: Exchange industry association
- **Coverage**: WFE member exchanges only (~250 market infrastructure providers)
- **Frequency**: Semi-annual market highlights, annual derivatives analysis
- **Key report**: [FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)
- **Metric**: Contracts traded, with asset class and regional breakdowns
- **Reliability**: 🟢 High — but narrower universe than FIA
- **Notes**:
  - 2024 total: **180.22 billion contracts** (options 153.30B, futures 26.92B)
  - 38.8% increase vs 2023
  - Excellent for asset class composition and regional share data
  - Charts 12-20 in FY 2024 report provide rich time-series breakdowns
  - Limitations: Does not cover all exchanges (e.g., some smaller APAC, LatAm exchanges missing)

### 3. BIS (Bank for International Settlements)

- **URL**: https://www.bis.org/statistics/extderiv.htm
- **Type**: Central bank of central banks / statistical authority
- **Coverage**: Exchange-traded IR and FX derivatives on 50+ exchanges
- **Frequency**: Quarterly
- **Key data**: [Exchange-traded derivatives statistics overview](https://data.bis.org/topics/XTD_DER)
- **Metric**: Notional turnover (USD) and open interest (notional)
- **Reliability**: 🟢 High for IR + FX; does not cover equity/commodity ETD
- **Notes**:
  - Q3 2024: Average daily notional turnover of **$12.83 trillion/day**
  - IR dominates: $12.65T/day (98.6%), FX: $0.185T/day (1.4%)
  - BIS converts contract counts to notional amounts — adds unique value
  - Does NOT publish equity or commodity ETD notional data
  - OTC stats published separately (not directly comparable)

### 4. CME Group

- **URL**: https://www.cmegroup.com/investor-relations/volume-reports.html
- **Type**: Largest US derivatives exchange
- **Key report**: [Record Annual ADV of 26.5M Contracts in 2024](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html)
- **Reliability**: 🟢 High — SEC/CFTC-regulated disclosure
- **Notes**:
  - 2024 ADV: 26.5 million contracts, up 9% YoY
  - 2025 ADV: 28.1 million contracts, up 6% YoY
  - Interest Rate ADV: 13.7M contracts (record)
  - Equity Index ADV: 6.8M contracts
  - International ADV: 7.8M contracts (record, up 14%)
  - Useful for US-centric deep dive and interest rate derivatives specifically
  - CME accounts for 48.5-53.2% of global interest rate derivatives volume

### 5. National Stock Exchange of India (NSE)

- **URL**: https://www.nseindia.com/all-reports-derivatives
- **Type**: World's largest derivatives exchange by contract volume
- **Reliability**: 🟢 High — SEBI-regulated
- **Notes**:
  - 2023: ~84.8 billion contracts (FIA ranking)
  - 2024: Estimated 140-160 billion contracts (extrapolated from APAC share)
  - Turnover: Rs 40,000+ trillion in FY2024-25
  - Dominates global stock index options: 97.7% traded on NSE (WFE)
  - Also 94.5% of global currency options market
  - SEBI regulatory changes in late 2024 (increased lot sizes, restricted weekly expiries) expected to moderate growth

## Secondary Sources

### 6. Eurex (Deutsche Borse)

- **URL**: https://www.eurex.com/ex-en/data/statistics
- **Key data**: [Full year 2024 figures](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Full-year-and-December-2024-figures-at-Eurex-4250262)
- **2024 volume**: 2,080.5 million contracts (up 9% YoY)
- **Notes**: Interest rate derivatives +26%, equity derivatives +16%

### 7. B3 (Brazil)

- **2023 volume**: 8.3 billion contracts (ranked #2 globally)
- **Notes**: Strong in interest rate, FX, and equity derivatives
- **Open interest**: 203.6M contracts at end-2023 (up 61.5%)

### 8. Crypto Derivatives Sources

- **Source**: [coinlaw.io statistics](https://coinlaw.io/cryptocurrency-derivatives-market-statistics/)
- **Notes**:
  - Total crypto trading volume: $3.12T, derivatives = 74.2% share
  - CME Bitcoin/Ethereum futures: institutional-grade, regulated ETD
  - Deribit: 85% of crypto options volume (not exchange-traded in traditional sense)
  - Crypto futures grew 26% YoY in 2024
  - Most crypto "derivatives" are on unregulated venues — only CME counts as traditional ETD

### 9. FIA Historical Annual Surveys

- 2015: [Asia Takes the Lead](https://www.fia.org/fia/articles/2015-fia-annual-futures-and-options-volume-survey-asia-takes-lead) — 24.78B
- 2016: [Annual Volume Survey](https://www.fia.org/marketvoice/articles/2016-annual-volume-survey) — 25.22B
- 2017: [Total 2017 Volume](https://www.fia.org/fia/articles/total-2017-volume-252-billion-contracts-down-01-2016) — 25.20B
- 2018: [Record ETD Volume](https://www.fia.org/fia/articles/fia-releases-annual-trading-statistics-showing-record-etd-volume-2018) — 30.28B
- 2019: [Record Year](https://www.fia.org/fia/articles/record-year-derivatives) — 34.47B
- 2020: [Record Level](https://www.fia.org/fia/articles/global-futures-and-options-trading-reaches-record-level-2020) — 46.77B
- 2021: [Another Record](https://www.fia.org/fia/articles/global-futures-and-options-trading-hits-another-record-2021) — 62.58B
- 2022: [Statista](https://www.statista.com/statistics/377025/global-futures-and-options-volume/) — 83.85B (derived from futures 29.32B + options 54.53B)
- 2023: [137 Billion Contracts](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023) — 137.31B
- 2024: [Annual Review](https://www.fia.org/fia/articles/2024-annual-etd-volume-review) — 205.34B

## Source Discrepancy Notes

| Metric | FIA | WFE | Delta | Explanation |
|--------|-----|-----|-------|-------------|
| 2024 total volume | 205.34B | 180.22B | 25.12B | FIA covers 85 exchanges vs WFE member-only universe |
| Options 2024 | 177.12B | 153.30B | 23.82B | Same coverage gap |
| Futures 2024 | 28.22B | 26.92B | 1.30B | Smaller gap — futures traded on fewer, larger exchanges |
| YoY growth 2024 | +51% | +38.8% | — | Different baselines (FIA 2023 = 136B, WFE 2023 = 129.8B) |

**Resolution**: FIA used as primary source for total volume (broader coverage). WFE used for asset class composition and regional breakdowns (richer analytical detail).

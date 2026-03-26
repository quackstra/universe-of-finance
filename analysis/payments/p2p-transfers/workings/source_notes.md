# Peer-to-Peer Transfers — Source Notes

## Source Quality Assessment

### Tier 1: Official/Regulatory (High Confidence)
- **Early Warning Services (Zelle)** — Privately held by 7 major US banks. Publishes annual transaction and value data. The $1.04T and 3.6B transaction figures for 2024 are from official press releases covered by CNBC, American Banker, and others. Highly reliable.
- **PayPal 10-K (SEC filing)** — Publicly traded; audited financials. Reports total payment volume for Venmo but not transaction counts. TPV is authoritative; our transaction count is derived.
- **Block 10-K (SEC filing)** — Publicly traded; audited financials. Reports "Cash App inflows" — reliable but definitionally broader than pure P2P.

### Tier 2: Industry Reports (Medium Confidence)
- **eMarketer/Insider Intelligence** — US P2P market share forecasts. Methodologically sound but proprietary; specific figures sometimes conflict with other sources. Used for market share ratios.
- **BusinessOfApps** — Aggregates public filings and analyst estimates. Generally reliable for trend data; specific numbers should be cross-referenced.
- **CoinLaw** — Statistical comparison site. Aggregates multiple sources. Used for cross-referencing.

### Tier 3: Estimates (Low Confidence)
- **PayPal P2P (non-Venmo)** — PayPal reports $1.68T total TPV but doesn't break out how much is domestic P2P vs. e-commerce vs. cross-border. Our $150B estimate is rough.
- **Non-US P2P** — Bizum publishes some data; Swish publishes in Swedish central bank reports. Other platforms are sparse.
- **Peak TPS** — No platform publishes peak concurrent TPS. The ~600 estimate is based on known US holiday spending patterns.

## Data Gaps

1. **Transaction counts for Venmo and Cash App** — Neither platform publishes this. All figures are estimates.
2. **Pure P2P vs. commercial** — All three major platforms now support commercial transactions (Pay with Venmo, Cash App Pay, Zelle for small business). The P2P/commercial split is unknown.
3. **PIX classification** — Brazil's PIX processed ~42B transactions in 2024, much of which is P2P. Its classification as Bank Transfers rather than P2P is a taxonomy choice that significantly affects this category's size.
4. **Fraud-adjusted figures** — Zelle has faced scrutiny over fraud (~$870M authorized fraud in 2023 per Senate report). Official volume figures include fraudulent transactions.
5. **International comparison** — No equivalent aggregated dataset exists for non-US P2P markets.

## Key URLs Accessed

| Source | URL | Date Accessed | Notes |
|--------|-----|---------------|-------|
| CNBC — Zelle $1T | https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html | 2026-03-26 | Key 2024 data point |
| American Banker | https://www.americanbanker.com/payments/news/zelle-passes-1t-in-2024-with-a-boost-from-small-businesses | 2026-03-26 | Additional context |
| PayPal 10-K | https://www.sec.gov/Archives/edgar/data/1633917/000163391725000019/pypl-20241231.htm | 2026-03-26 | Official Venmo TPV |
| Block 10-K | https://www.sec.gov/Archives/edgar/data/1512673/000162828025007376/sq-20241231.htm | 2026-03-26 | Cash App inflows |
| Zelle 2023 PR | https://www.zelle.com/press-releases/zelle-soars-806-billion-transaction-volume-28-prior-year | 2026-03-26 | 2023 annual data |

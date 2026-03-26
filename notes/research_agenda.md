# Research Agenda — Next Run

> Updated 2026-03-26 after completing all 24 initial category capsules.

## Status: Ring 1-4 Initial Pass Complete

All 24 taxonomy categories now have first-pass capsules with current TPS,
historic trends, and projections. The next run should focus on **deepening**
the highest-impact categories and **resolving data gaps**.

## Priority Queue (inside-out order)

### Tier 1: Resolve Double-Counting (highest research ROI)
1. **Digital Wallets ↔ Card overlap quantification** — Estimate what % of wallet txns ride on card rails (Apple Pay, Google Pay) vs. independent networks (UPI, WeChat Pay, M-Pesa). Critical for accurate total TPS.
2. **E-Commerce ↔ Cards/Bank Transfers overlap** — E-commerce is *paid* via cards or bank transfers. Quantify the overlap to avoid double-counting.
3. **Gaming ↔ Cards overlap** — Gaming purchases are mostly card-paid. Quantify (~2% of global card volume).

### Tier 2: Fill Data Gaps in Top Categories
4. **Consumer Cards** — Fill interpolated historic years (2016, 2018-2020) with direct sources. Extend to 2010.
5. **Bank Transfers** — Break down by system type (ACH batch vs. real-time vs. wire). RTP growth is the most important payments trend.
6. **Equity Markets** — Source individual exchange data (NYSE, NASDAQ, SSE, NSE, JPX) to validate 61.5B aggregate.
7. **Forex** — Transaction COUNT is a genuine data gap. CLS covers ~35% of market. Need better methodology.
8. **CEX** — Wash trading adjustment. Current ~4,000 TPS may be 2-3× inflated on unregulated exchanges.

### Tier 3: Deepen Historic Data
9. **All top-10 categories** — Extend historics to 2015 minimum, 2010 where data exists.
10. **Regional breakdowns** — Add regional TPS splits for consumer cards, bank transfers, equity markets.
11. **Subcategory capsules** — Break ETD by asset class, fixed income by instrument type.

### Tier 4: Cross-Category Analysis & Tooling
12. **Build the Big Number calculator** — Script that sums non-overlapping TPS with configurable overlap assumptions.
13. **Value vs. Count scatter plot** — Visualise all 24 categories on log-log axes.
14. **Growth rate comparison** — Which categories are growing fastest by TPS? Table + chart.
15. **Normalise data.json schemas** — All capsules should use identical key structure for programmatic access.

## Revisions Needed
- Normalise all data.json to consistent schema (current varies by agent)
- Fill in missing peak TPS estimates where absent
- Validate projection assumptions for cross-category consistency
- Fixed income: separate repo from cash bond trading more clearly

## New Categories to Consider
- **Insurance Premiums** — Potentially billions of annual transactions
- **Payroll Payments** — Currently implicit in bank transfers
- **Bill Payments** — Utilities, telecoms, subscriptions
- **ATM Withdrawals** — Declining but still substantial globally
- **NFTs** — In taxonomy but no capsule (low priority, market contracted)

## Data Sources to Investigate
- **BIS CPMI Statistics** (cpmi.bis.org) — Comprehensive cross-country payment data
- **ECB Payment Statistics** — Granular European payment data
- **RBI Payment System Indicators** — UPI and India-specific data (very detailed)
- **FIA Annual Volume Survey** — Historical derivative volumes
- **DTCC Data Repository** — OTC derivative trade counts
- **Visa/Mastercard quarterly earnings** — Transaction count trends by quarter

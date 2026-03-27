# Research Agenda — Next Run (Run 5)

> Updated 2026-03-27 after completing Run 4 (confidence upgrades + regional decomposition).

## Status: Run 4 Complete

All 24 categories now have confidence scores (34-91, median 62). Tier 1 confidence
upgrades done for CEX, Forex, Fixed Income, OTC Derivatives, IoT/M2M. Regional
decomposition complete for top 3 categories. Big Number: ~70,741 de-duplicated TPS.

## What Run 5 Should Target

### Tier 1: Remaining Confidence Gaps (highest ROI)

1. **Repo market deep dive** — Repo adds ~83.8M trades/year to fixed income but carries 4× uncertainty (40M-160M). Fed ON RRP, DTCC GCF, ECB MRO data could anchor this. This is the single largest remaining uncertainty by absolute count.

2. **CEX regional wash trading** — Current model uses global tiers. Regional analysis (Korea premium, China OTC, Middle East unregulated) could refine Tier 2/3 estimates.

3. **Retail forex count validation** — ~10M/day estimate is extrapolated from limited broker data. FXCM, IG, Plus500, CMC Markets all report trade counts in annual reports — aggregate them.

4. **Equity OTC derivatives** — Most opaque sub-segment at 0.6M/year. Coalition Greenwich institutional surveys may have data.

5. **Gaming overlap quantification** — Gaming purchases overlap with cards/wallets. Quantify: what % flows through Apple/Google in-app (counted in wallet?) vs. direct card charge.

### Tier 2: New Category Expansion

6. **Insurance premiums** — ~$7T global, unknown transaction count. Lloyd's, Swiss Re sigma data. Potentially billions of auto-debit premium collections.

7. **BNPL** — Klarna (~2.5M txns/day), Afterpay, Affirm, PayPal BNPL. Growing fast, partially overlapping cards. Model the overlap.

8. **Bill payments** — Utilities, telecoms, subscriptions. Potentially 50-100B annual. NACHA biller data, UK Direct Debit stats, EU SEPA DD volumes.

9. **Payroll** — Implicit in bank transfers. ADP processes ~100M paychecks/year in US alone. Global estimate unknown.

10. **ATM withdrawals** — Declining (~50B/year?). ATM Industry Association data. Overlap with bank transfers for cash-out.

### Tier 3: Temporal & Scenario Analysis

11. **Backtest projections** — For categories with 5+ years of history, did our projection brackets capture reality? Run backtests.

12. **Macro-scenario stress tests** — Recession, pandemic, crypto winter, fintech disruption — how does the Big Number shift?

13. **Time-series construction** — Build 2015-2025 annual TPS for all 24 categories using historic data already in capsules. Enable growth rate comparison.

14. **Peak TPS analysis** — Black Friday, Singles' Day, crypto crashes, options expiry — what's the coordinated global peak?

### Tier 4: Tooling & Presentation

15. **Interactive dashboard** — Web-based Big Number visualization with drill-down by sector/category/region.

16. **API endpoint** — Serve data.json programmatically for downstream projects (Blokenet context).

17. **Time-series animation** — Animated chart: TPS by category 2015→2035.

18. **Automated confidence updater** — Script that re-scores confidence as new workings files are added.

19. **Data freshness tracker** — Flag categories where sources are >12 months old.

## Data Sources to Investigate

- **DTCC GCF Repo Index** — US repo market daily data
- **Fed ON RRP** — Overnight reverse repo facility usage
- **ECB Money Market Statistical Reporting** — Euro repo data
- **Coalition Greenwich** — Institutional trading surveys (equity OTC, FX)
- **FXCM/IG/Plus500 Annual Reports** — Retail forex trade counts
- **ATM Industry Association** — Global ATM withdrawal statistics
- **ADP Research** — Payroll transaction volumes
- **Swiss Re sigma** — Insurance premium data
- **Klarna/Affirm 10-K** — BNPL transaction counts

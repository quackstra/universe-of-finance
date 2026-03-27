# Research Agenda — Next Run (Run 4)

> Updated 2026-03-26 after completing Run 3 (triangulation + tooling).

## Status: Run 3 Complete

All 24 categories have full capsules with normalized data.json schemas.
Key overlaps quantified. Triangulation models for China, Solana, RTGS, Government.
Big Number calculator and visualization tooling operational.

## What Run 4 Should Target

### Tier 1: Confidence Upgrades (move 🔴→🟡 and 🟡→🟢)

1. **CEX wash trading adjustment** — Current ~3,100 TPS is wash-adjusted but methodology is rough. Cross-reference Kaiko/CryptoCompare real-volume estimates vs. CoinGecko/CMC reported. Build a wash-trading filter model similar to Solana vote filter.

2. **Forex transaction count** — Genuinely opaque. CLS settles ~$6.6T/day but only covers ~35% of market. Model remaining 65% via prime brokerage data, BIS triennial survey breakdowns by counterparty type, and electronic platform market share (EBS, Refinitiv, etc.).

3. **Fixed income count refinement** — Current ~7 TPS is a rough estimate. TRACE data (US corporate/agency), MTS (EU govt bonds), and ICMA repo surveys could triangulate better.

4. **OTC derivatives** — Most opaque category. DTCC SDR data + ISDA surveys + BIS semiannual could narrow from ~0.6 TPS estimate.

5. **IoT/M2M payments** — Currently 🔴 Low confidence. ABI Research, Juniper Research, and GSMA IoT data could triangulate. Separate toll/transit from industrial IoT.

### Tier 2: Regional Decomposition

6. **Consumer cards by network** — Break 772.7B into Visa/Mastercard/UnionPay/Amex/JCB/Discover. Network-specific growth rates.

7. **Bank transfers by region** — India (UPI), Brazil (PIX), China (CNAPS), EU (SEPA), US (ACH/FedNow) — individual growth trajectories.

8. **Equity markets by exchange** — NYSE, NASDAQ, SSE, SZSE, NSE, BSE, JPX, LSE, Euronext — validate 61.5B aggregate.

### Tier 3: Projection Model Improvements

9. **Backtest projections** — For categories with 5+ years of data, run backtests on projection models (did baseline/high/conservative brackets capture actual outcomes?).

10. **Macro-scenario modelling** — How do recession, pandemic, or fintech disruption scenarios affect projections? Stress-test the Big Number under different assumptions.

11. **Digital assets projection uncertainty** — CEX/L1L2 projections are especially uncertain. Model bull/bear crypto cycle impacts.

### Tier 4: New Categories & Expansion

12. **Insurance premiums** — Global premium volume is ~$7T. Transaction count unknown but potentially billions.
13. **Payroll payments** — Implicit in bank transfers. Could be 10-20B annual txns globally.
14. **Bill payments** — Utilities, telecoms, subscriptions. Potentially 50-100B annual txns.
15. **ATM withdrawals** — Declining (~50B/year?) but still relevant.
16. **BNPL** — Growing rapidly, partially overlapping cards. Klarna alone at ~2.5M txns/day.

### Tier 5: Tooling & Presentation

17. **Interactive dashboard** — Web-based visualization of the Big Number with drill-down by sector.
18. **API endpoint** — Serve data.json programmatically for downstream projects (Blokenet context).
19. **Confidence scoring model** — Formalize confidence from qualitative (🔴🟡🟢) to quantitative (0-100 with defined rubric).
20. **Time-series animation** — Animated chart showing TPS growth from 2015→2035 across all categories.

## Data Sources to Investigate

- **Kaiko** — Real crypto trading volume (wash-filtered)
- **CryptoCompare Exchange Benchmark** — Exchange trustworthiness scoring
- **FINRA TRACE** — US corporate bond trading data
- **ICMA European Repo Survey** — Repo market sizing
- **DTCC SDR** — OTC derivative trade reporting
- **BIS Triennial Survey 2025** — If published, latest forex/derivatives data
- **ABI Research** — IoT payment forecasts
- **Juniper Research** — IoT/M2M payment estimates
- **GSMA IoT Report** — Connected device payment activity

## Revisions Still Needed

- Update OVERLAP_MATRIX.md with revised L1/L2 TPS (~350-480 vs. ~900) from Solana filter
- Update OVERLAP_MATRIX.md with revised government TPS (~1,002 vs. ~793) from bottom-up model
- Reconcile big_number.py output (~71,105) with OVERLAP_MATRIX.md estimates (~70,600/71,600)
- Add revised RTGS total (~1.5B) to banking section of README

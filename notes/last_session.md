# Last Session Notes — 2026-03-26

## Runs Completed: 3

### Run 1: Initial 24-Category Pass
- All 24 taxonomy categories researched with full capsules (REPORT.md + data.json + workings/)
- First-pass Big Number estimate: ~76,000 TPS (pre-overlap)

### Run 2: Overlap Quantification + Open Questions
- Created `analysis/payments/OVERLAP_ANALYSIS.md` — quantified all 6 payment-sector overlaps
- Created `analysis/OVERLAP_MATRIX.md` — cross-sector de-duplication methodology
- De-duplicated global TPS: ~70,600 (payment infrastructure) / ~71,600 (all economic events)
- Added "Open Questions & Triangulation Opportunities" to all 24 capsule REPORTs
- Key finding: raw payment sum overstates by 14% (1,945B → 1,679B unique txns)
- Biggest single overlap: UPI at 172B txns counted in both wallets and bank transfers

### Run 3: Deep Triangulation + Tooling
7 agents dispatched (4 resumed after rate limit):

1. **China triangulation model** (`analysis/payments/digital-wallets/workings/china-model.md`)
   - 6 independent estimation methods converging at 280B ±20B (narrowed from ±50B)
   - Methods: PBOC reported, GDP ratio, population, Alipay+WeChat bottom-up, e-commerce, mobile internet

2. **Stablecoin decomposition** (`analysis/digital-assets/stablecoins/workings/volume-decomposition.md`)
   - $27.6T raw → $5.7T Visa-adjusted after filtering wash/MEV/arb
   - Category gap analysis showing where adjusted volume goes

3. **Visualization suite** (`tools/charts.py` → `analysis/charts/`)
   - TPS bar chart, value-vs-count scatter, dedup waterfall, consumer cards timeseries

4. **Solana vote filter** (`analysis/digital-assets/blockchain-l1-l2/workings/solana-filter.md`)
   - L1/L2 TPS revised from ~900 to ~350-480 after filtering Solana vote transactions
   - Vote txns are ~80% of Solana's reported TPS

5. **Missing RTGS systems** (`analysis/banking/interbank-rtgs/workings/missing-systems.md`)
   - Added 8 RTGS systems (China CNAPS, India RTGS, Russia BESP, etc.)
   - Interbank total tripled: 423M → ~1.5B transactions

6. **Government bottom-up model** (`analysis/government/government-payments/workings/bottom-up-model.md`)
   - US IRS+SSA+Treasury, India DBT, EU models
   - Revised from 25B to ~31.6B (TPS ~1,002)
   - India DBT alone generates 7.4B transactions

7. **Schema normalization + Big Number calculator**
   - All 24 data.json normalized to consistent schema (slug, overlap, current/historic/projections/sources)
   - `tools/big_number.py` — de-duplicated global TPS: ~71,105
   - `tools/validate_schema.py` — 24/24 passing
   - `tools/normalize_schemas.py` — conversion utility

## Key Findings Across All 3 Runs

1. **Payments dominate**: 75% of global financial TPS is payment transactions
2. **The overlap problem is smaller than feared**: 14% overcount in raw sum
3. **UPI is the single largest overlap**: 172B txns in both wallets and bank transfers
4. **90% of digital wallet txns are incremental to cards** (counterintuitive — because UPI, China, M-Pesa are non-card)
5. **Solana vote transactions inflate L1/L2 TPS by 2-3×**
6. **Missing RTGS systems tripled interbank count**
7. **E-commerce is a commerce layer, not a payment layer** (95% overlay)
8. **China triangulation narrowed uncertainty from ±50B to ±20B**

## Git Commits
1. `80d7d82` — 5 capsules from interrupted session
2. `e7ae1d5` — 19 new capsules (all 24 categories)
3. `63a53b8` — Session notes, README index, backlog update
4. `20dae58` — Run 2: overlap analysis, open questions, data gap fills
5. `3603019` — Run 3 partial: China model, stablecoin decomposition, charts
6. `bac48fc` — Run 3: Solana filter, missing RTGS, gov bottom-up
7. `29b4997` — Run 3: Schema normalization + Big Number calculator

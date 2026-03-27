# Last Session Notes — 2026-03-27

## Runs Completed This Session: Run 3 (finish) + Run 4

### Run 3 Completion (carried from prior session)
- Committed schema normalization: all 24 data.json to consistent schema
- Added tools: big_number.py (~71,105 TPS), validate_schema.py (24/24), normalize_schemas.py

### Run 4: Confidence Upgrades + Regional Decomposition (5 parallel agents)

#### Agent 1: CEX Wash Trading Filter + Forex Count Triangulation
- **CEX wash trading**: Tiered model (Tier 1: 3.5%, Tier 2: 20%, Tier 3: 45%) → blended 25% → TPS 4,050 → **3,040** (range 2,685–3,275). 9 academic/industry sources. Confidence interval narrowed 2.1×.
- **Forex count**: 6 independent methods. Institutional: ~3.0M trades/day (~35 TPS). Including retail: ~13M/day (~150 TPS). Dealer-to-other-financial ticket size ($1.5M-$4.0M) is the pivotal assumption. Confidence: Low → Medium.

#### Agent 2: Fixed Income + OTC Derivatives Count Refinement
- **Fixed income**: Cash bonds revised to ~3.6 TPS (from ~7). US is ~70% of global trade count despite 33% of outstanding. TRACE (52M) + MSRB (14.5M) + Treasury (12.6M) = 79.1M/year US alone. Repo adds ~83.8M/year but carries 4× uncertainty. Total incl. repo: ~6.2 TPS.
- **OTC derivatives**: Revised to ~0.15 TPS excl. FX (from ~0.3). IRD (3.1M) and CDS (0.6M) well-anchored via ISDA SwapsInfo. Equity and commodity OTC most opaque. FX derivatives (~5M/year) excluded to avoid double-counting with forex category. H1 2025 shows +27.5% IRD growth.

#### Agent 3: IoT/M2M Triangulation + Confidence Scoring Model
- **IoT/M2M**: Revised 2.4× up: 634 → **1,538 TPS** (20B → 48.5B txns). Toll collection (27B, driven by China 12-15B + India FASTag 4B), vending (9.5B via Cantaloupe data), smart meters (8.5B), EV charging (3B per IEA).
- **Confidence scorecard**: All 24 categories scored 0-100 across source quality, recency, triangulation, coverage. Consumer Cards tops at 91, AI Agents lowest at 34, median 62. All data.json updated with confidence blocks.

#### Agent 4: Regional Decomposition
- **Cards by network**: Visa 303B, UnionPay ~247B, Mastercard ~185B, plus domestic networks (RuPay, Mir, Elo) = ~819B adjusted total. Reconciles within 0.4%.
- **Bank transfers by system**: UPI (172B) + PIX (66B) = 63% of real-time payments. Nigeria NIP (11.2B) > UK + EU + US combined. ~60B unattributed.
- **Equities by exchange**: India (NSE+BSE) = 28-29% of global trades despite 4% market cap. Zero-DTE options explosion. Sum reconciles within 0.6%.

#### Agent 5: Reconcile OVERLAP_MATRIX + README
- L1/L2 TPS: 900 → 415 (Solana vote filter)
- Government TPS: 793 → 1,002 (bottom-up model)
- Interbank RTGS: 13.4 → 50.1 TPS; 423M → 1,581M txns
- De-duplicated Big Number: **~70,741 TPS**

## Git Commits (Run 4)
1. `47acaa5` — Reconcile OVERLAP_MATRIX + README with Run 3 estimates
2. `c12494a` — IoT/M2M triangulation + confidence scoring model
3. `5940ffa` — Regional decomposition (cards/transfers/equities)
4. `a386fa8` — CEX wash trading filter + forex count triangulation
5. `040de28` — Fixed income + OTC derivatives count triangulation

## Cumulative Key Findings (Runs 1-4)
1. **De-duplicated global financial TPS: ~70,741** (programmatic via big_number.py)
2. Payments = 75% of global TPS; consumer cards + digital wallets + bank transfers = 80%
3. UPI alone (172B) > all global equity markets (61.5B) combined
4. Double-counting between categories is ~14% (smaller than feared)
5. Solana vote transactions inflate L1/L2 by 2-3×
6. IoT/M2M is 2.4× larger than initial estimate (toll collection was massively underweighted)
7. CEX wash trading ~25% blended (tiered model with regulated/unregulated split)
8. Forex institutional count is only ~3M trades/day despite $7.5T turnover
9. India dominates by count: #1 in equity trades (28%), #1 in real-time payments (UPI), growing in cards (RuPay)
10. Confidence scores range 34-91 with median 62 — most opaque: AI agents, OTC derivatives, IoT/M2M

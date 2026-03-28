# Last Session Notes — 2026-03-28

## Runs Completed This Session: Run 4 (finish) + Run 5 + Intergalactic Recruiter

### Intergalactic Recruiter
- Built SLE (Soul Less Employee) framework: 13 expert personas grounded in real job descriptions
- RECRUITER.md dispatch matrix maps all categories to primary/secondary SLEs
- Integrated into Elf pipeline via activation phrases

### Run 5: Full Elf Run (6 parallel agents, 29 categories)

#### Agent 1: Repo Market Deep Dive (SLE: fixed-income-specialist)
- Repo revised 2.6× up: 84M → **219M trades/year** (~10.5 TPS incl. repo)
- FICC GSD peaked at 1.206M transactions on Apr 9, 2025 (hard DTCC data)
- China exchange-traded repo adds ~160-200K trades/day (retail-accessible segment)
- Confidence interval narrowed from 4× to 3×

#### Agent 2: CEX Regional + Retail Forex + Equity OTC (SLE: crypto-forensics + forex)
- CEX wash rate refined: 25% → **20.6%** via regional decomposition. TPS 3,040 → **3,210**
- Retail FX validated at **8M trades/day** via broker aggregation. Japan = 40% of global retail FX
- Equity OTC doubled: 600K → **1.2M trades/year** via CFD + structured product modeling

#### Agent 3: New Categories — Insurance + BNPL + Bill Payments (SLE: market-research-analyst)
- **Insurance premiums**: ~14B txns/year (~444 TPS), 90% overlap with cards/bank transfers
- **BNPL**: ~5.5B purchases generating ~20B installment events (~634 TPS). 100% infrastructure overlap but creates genuine transaction multiplication (3.6×)
- **Bill payments**: ~95B txns/year (~3,012 TPS) across 9 segments. 90% overlap with direct debit/card-on-file

#### Agent 4: New Categories — Payroll + ATM + Gaming Overlap (SLE: govt-statistician + gaming-economy)
- **Payroll**: ~41.2B txns/year (~1,305 TPS), 90% overlap with bank transfers
- **ATM withdrawals**: ~49.1B txns/year (~1,557 TPS), declining at -3% CAGR. **Zero overlap** — unique cash-out category
- **Gaming overlap**: 82% of gaming transactions already counted in cards/wallets. Only ~2.77B incremental (~88 TPS)

#### Agent 5: Time-Series 2015-2025 (SLE: market-research-analyst)
- Full 2015-2025 annual TPS for all 24 categories
- Global gross TPS grew 6.7× in a decade: ~12,900 (2015) → ~86,900 (2025)
- Fastest growers (2020-25 CAGR): RWA tokenisation 119%, stablecoins 103%, L1/L2 77%
- India Effect: drove ETD from ~800 to ~9,500 TPS single-handedly

#### Agent 6: Peak TPS + Scenarios + Freshness Tool (SLE: emerging-tech-forecaster)
- Coordinated global peak: ~147K–246K TPS (2.1–3.5× average Big Number)
- Recession: Big Number barely moves (−0.3%); Pandemic: +18-28%; Crypto winter: −3%
- Data freshness tool operational (tools/data_freshness.py)

## Taxonomy Expansion: 5 New Categories
1. Insurance Premiums (payments sector)
2. BNPL (payments sector)
3. Bill Payments (payments sector)
4. Payroll (payments sector)
5. ATM Withdrawals (payments sector)

Total categories: **29** (was 24)

## Git Commits (Run 5)
1. `74b282c` — Peak TPS analysis, macro scenarios, data freshness tool
2. `cfbe103` — Time-series 2015-2025 + repo deep dive
3. `b6f3801` — CEX regional wash, retail forex, equity OTC
4. `2c50244` — Payroll, ATM withdrawals, gaming overlap
5. `5d39d95` — Insurance premiums, BNPL, bill payments

## Cumulative Key Findings (Runs 1-5)
1. **De-duplicated global financial TPS: ~70,741** (needs re-running with 29 categories + revisions)
2. 5 new categories add ~6,552 gross TPS but most overlaps with existing: incremental ~1,900 TPS (ATM + partial insurance/bills/payroll cash + BNPL multiplication)
3. Repo market is 2.6× larger than estimated — fixed income TPS doubles
4. Gaming is a commerce layer (82% overlap), like e-commerce (95% overlap)
5. BNPL is a credit multiplier — creates 3.6× transactions on underlying payment rails
6. ATM is the only declining category (-3% CAGR) and the only new category with zero overlap
7. Global TPS grew 6.7× in a decade (2015-2025)
8. Flash crash on quarter-end could push coordinated global peak to ~246K TPS
9. Recessions barely affect the Big Number; pandemics increase it

# Universe of Finance

> Measuring every financial transaction on Earth — from Visa swipes to repo trades,
> UPI taps to video game loot boxes — expressed as one number: transactions per second.

## The Big Number

### **~73,750 de-duplicated global financial TPS**

That's ~2.3 trillion transactions per year flowing through the world's financial infrastructure.
Range: 67,000–83,000 TPS depending on overlap assumptions.

**Coordinated global peak: ~147,000–246,000 TPS** (flash crash on a busy quarter-end).

## The MEST Number

### **~545,000 Mutual Economic State Transitions per second**

Every transaction triggers a cascade of bilateral state changes — authorization events, clearing legs, settlement instructions, custody updates, reconciliation entries, regulatory reports. A single card swipe generates ~7 MESTs. An OTC derivative trade generates ~12.

**MEST** = any change to an economically valuable holding where more than one party has a material interest in the record. The Big Number counts transactions. The MEST Number counts what the financial system *actually does*.

| Metric | Value |
|--------|-------|
| Global MEST/s | **~545,000** (range: 410K–720K) |
| MEST multiplier | **7.4×** the Big Number |
| Annual MESTs | **~17.2 trillion** |
| Highest multiplier | OTC Derivatives (12×) |
| Highest total MESTs | Consumer Cards (~171K MEST/s) |
| Crypto MEST advantage | 60-80% fewer state changes per economic event |

See [`analysis/MEST.md`](analysis/MEST.md) for the full framework.

| Fact | Value |
|------|-------|
| Categories measured | **29** across 7 sectors |
| Confidence scores | 34–91 (median 62) |
| Time-series | 2015–2025 (10 years, all categories) |
| Growth rate | **6.7× in a decade** (12,900 → 86,900 gross TPS) |
| Data points | 29 capsules × ~12 data fields each |

## TPS Leaderboard

| # | Category | Avg TPS | Annual Txns | Sector |
|---|----------|---------|-------------|--------|
| 1 | Consumer Cards | 24,501 | 772.7B | Payments |
| 2 | Digital Wallets | 19,660 | 620B | Payments |
| 3 | Bank Transfers | 15,338 | 484B | Payments |
| 4 | ETD (Derivatives) | 9,500 | 205.3B | Traditional Finance |
| 5 | Equity Markets | 3,500 | 61.5B | Traditional Finance |
| 6 | CEX (Crypto) | 3,210 | ~101B | Digital Assets |
| 7 | Bill Payments | 3,012 | ~95B | Payments |
| 8 | E-Commerce | 1,800 | ~57.5B | Payments |
| 9 | ATM Withdrawals | 1,557 | ~49.1B | Payments |
| 10 | IoT & M2M | 1,538 | 48.5B | Emerging |

The top 3 categories (cards + wallets + bank transfers) account for **~80% of global financial TPS**.

## Key Findings

- **Payments dominate**: 75% of global TPS is payment transactions
- **India is everywhere**: #1 in equity trades (28% of global), #1 in real-time payments (UPI), growing fast in cards (RuPay)
- **Double-counting is ~14%**: Smaller than expected. UPI (172B txns) is the biggest single overlap
- **Gaming and e-commerce are commerce layers, not payment layers**: 82% and 95% of their transactions are already counted in cards/bank transfers
- **BNPL is a transaction multiplier**: Each purchase creates 3.6× payment events on underlying rails
- **ATM is the only declining category**: -3% CAGR, down from 63B peak — the slow death of cash
- **Recessions barely move the Big Number** (-0.3%): Trading surges offset payment declines. Pandemics actually *increase* it (+18-28%)
- **Solana vote transactions inflate L1/L2 by 2-3×**: Real meaningful blockchain TPS is ~350-480, not ~900
- **CEX wash trading is ~20.6%** (blended): Regulated regions (<8%) vs. offshore (30-45%)

## Project Structure

```
universe-of-finance/
├── analysis/                    # 29 research capsules + cross-cutting analyses
│   ├── README.md                # Master index with full leaderboard
│   ├── OVERLAP_MATRIX.md        # Cross-sector de-duplication methodology
│   ├── CONFIDENCE_SCORECARD.md  # 0-100 confidence scores for all categories
│   ├── PEAK_TPS.md              # Peak load analysis + calendar co-occurrence
│   ├── SCENARIOS.md             # Recession / pandemic / crypto winter stress tests
│   ├── DATA_FRESHNESS.md        # Source staleness tracker
│   ├── timeseries/              # 2015-2025 annual TPS for all categories
│   └── <sector>/<category>/     # Individual capsules
│       ├── REPORT.md            # Reader-facing analysis
│       ├── data.json            # Structured data (normalized schema)
│       └── workings/            # Full calculations, assumptions, source notes
├── souls/                       # Intergalactic Recruiter — 17 expert personas
│   ├── RECRUITER.md             # Dispatch matrix + framework
│   └── <persona>/SOUL.md        # Expert persona grounded in real JDs
├── tools/                       # Analysis tooling
│   ├── big_number.py            # De-duplicated global TPS calculator
│   ├── confidence_score.py      # 0-100 confidence scoring engine
│   ├── validate_schema.py       # data.json schema validator (29/29 passing)
│   ├── data_freshness.py        # Source staleness detector
│   ├── charts.py                # Visualization suite (4 chart types)
│   └── normalize_schemas.py     # data.json schema migration tool
├── scout/                       # Data source discovery
├── architect/                   # Research methodology design
├── elves/                       # Autonomous research agent protocol
├── notes/                       # Inter-session continuity
├── TAXONOMY.md                  # Full transaction category taxonomy
└── BRIEF.md                     # Mission & methodology
```

## 29 Categories Across 7 Sectors

| Sector | Categories | Combined Gross TPS |
|--------|-----------|-------------------|
| **Payments** (11) | Consumer Cards, Digital Wallets, Bank Transfers, E-Commerce, P2P, Remittances, Bill Payments, Insurance Premiums, BNPL, Payroll, ATM Withdrawals | ~67,600 |
| **Traditional Finance** (6) | ETD, Equities, Commodities, Forex, Fixed Income, OTC Derivatives | ~13,400 |
| **Digital Assets** (4) | CEX, L1/L2 Blockchain, Stablecoins, DeFi | ~4,100 |
| **Banking** (2) | Interbank RTGS, Securities Settlement | ~100 |
| **Gaming** (2) | Microtransactions, Game Sales | ~480 |
| **Government** (1) | Tax & Government Payments | ~1,000 |
| **Emerging** (3) | IoT/M2M, RWA Tokenisation, AI Agents | ~1,540 |

*Note: Gross TPS sums include overlaps. De-duplicated total is ~73,750 TPS.*

## Research Methodology

Each category is researched using a **triangulation-first** approach:
1. Find 2-3 independent data sources that measure the same thing differently
2. Build bottom-up AND top-down models, then reconcile
3. Document assumptions, blind spots, and confidence explicitly
4. Quantify overlaps with other categories to enable accurate de-duplication

Research is guided by **Soul Less Employees** — 17 expert personas grounded in real job descriptions from organizations like Visa, BIS, Chainalysis, DTCC, BNY Mellon, and Gartner. Each persona brings domain-specific mental models, data sources, and documented biases to check against.

See [`souls/RECRUITER.md`](souls/RECRUITER.md) for the dispatch matrix.

## Macro Scenario Stress Tests

| Scenario | Big Number Impact | Key Driver |
|----------|------------------|------------|
| **Recession** (2008-style) | **-0.3%** (~70,500) | Trading surge offsets payment decline |
| **Pandemic** (2020-style) | **+18-28%** (~83,700-90,500) | Cash-to-digital migration |
| **Crypto Winter** | **-3.0%** (~68,600) | Crypto is only ~5% of total TPS |

## Time-Series: A Decade of Growth

Global gross TPS grew **6.7×** from 2015 to 2025. Fastest growers (2020-25 CAGR):

| Category | 2020-25 CAGR | Driver |
|----------|-------------|--------|
| RWA Tokenisation | 119% | Institutional adoption (BlackRock BUIDL) |
| Stablecoins | 103% | Settlement rail emergence |
| L1/L2 Blockchain | 77% | Solana throughput + L2 rollups |
| Digital Wallets | 21% | UPI + PIX hockey sticks |
| ETD | 18% | India NSE options explosion |

## Completed Research Runs

| Run | Focus | Key Output |
|-----|-------|------------|
| 1 | Initial 24-category pass | First Big Number (~76,000 gross) |
| 2 | Overlap quantification | De-duplicated to ~70,600. Open questions for all categories. |
| 3 | Deep triangulation + tooling | China model (±20B), Solana filter, Big Number calculator |
| 4 | Confidence upgrades + regional decomposition | Scorecard (34-91), cards/transfers/equities breakdowns |
| 5 | New categories + time-series + scenarios | 29 categories, 2015-2025 series, peak TPS, stress tests |
| 6 | Methodology overhaul + measurement SLEs | METHODOLOGY.md for all 29 categories, 3 new measurement SLEs |
| 7 | MEST framework + deep dives + confidence uplift | MEST Number (~545K/s), India & China deep dives, Sunset Watch |
| 8 | GitHub Pages + USA deep dive + MEST validation | Interactive dashboard, USA capsule, multiplier validation |

## Explore the Data

- **[Full Research Index](analysis/README.md)** — All 29 categories with TPS, confidence, and links
- **[Overlap Matrix](analysis/OVERLAP_MATRIX.md)** — How we de-duplicate the Big Number
- **[Confidence Scorecard](analysis/CONFIDENCE_SCORECARD.md)** — 0-100 scores with methodology
- **[Time-Series](analysis/timeseries/TIMESERIES.md)** — 2015-2025 data for all categories
- **[Peak TPS Analysis](analysis/PEAK_TPS.md)** — When does the world's financial infrastructure max out?
- **[Scenario Analysis](analysis/SCENARIOS.md)** — What happens in a recession, pandemic, or crypto winter?
- **[MEST Framework](analysis/MEST.md)** — Mutual Economic State Transitions (~545K/s)
- **[USA Deep Dive](analysis/deep-dives/usa/REPORT.md)** — TradFi dominance + card-heavy payments
- **[India Deep Dive](analysis/deep-dives/india/REPORT.md)** — 17.4% of global TPS on 3.5% of GDP
- **[China Opacity Report](analysis/deep-dives/china/REPORT.md)** — The ±6,000 TPS blind spot
- **[Sunset Watch](analysis/SUNSET_WATCH.md)** — Declining categories (growth outpaces decline 38:1)
- **[SLE Framework](souls/RECRUITER.md)** — 17 expert personas behind the research

## License

Research outputs: CC BY 4.0. Code: MIT.

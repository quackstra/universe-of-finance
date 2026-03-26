# Universe of Finance

> An autonomous research framework that measures, categorises, and forecasts
> the total volume of financial transactions across the entire global economy —
> from DeFi to stock exchanges, consumer payments to video game microtransactions.

**Goal**: Answer the question — *what is the total addressable market for
financial transactions, measured in transactions per second?*

## Disclaimer

This is a research project. Numbers are estimates derived from public data,
industry reports, and statistical modelling. They should not be used as the
sole basis for investment decisions. All sources are cited. All models are
transparent and reproducible.

## Why This Exists

Every financial infrastructure project — from Visa to Solana to Radix — needs
to understand the scale of the problem it's trying to solve. But there is no
single source that measures **all** transaction types across the global economy
on a consistent basis.

Universe of Finance fills that gap by:

1. **Cataloguing** every major transaction type in the global economy
2. **Measuring** historic and current transaction volumes (TPS) per category
3. **Projecting** future volumes under multiple growth scenarios
4. **Publishing** all findings as open research with charts, data, and methodology

## Transaction Taxonomy

See `TAXONOMY.md` for the full breakdown. Summary:

### Level 0 — Sectors (top-level groupings)

| Sector | Description |
|--------|-------------|
| Traditional Finance | Stock exchanges, bond markets, derivatives, forex |
| Payments | Consumer payments, P2P, merchant processing, remittances |
| Banking | Interbank transfers, RTGS, ACH, wire transfers |
| Digital Assets | Crypto exchanges, DeFi, NFTs, stablecoins |
| Gaming & Virtual | In-game transactions, virtual goods, esports |
| Government & Public | Tax payments, benefits disbursement, public procurement |
| Emerging | IoT micropayments, machine-to-machine, AI agent transactions |

### Level 1 — Categories (within each sector)

Each sector decomposes into 5-15 specific transaction categories, each
independently researched and measured.

### Level 2 — Subcategories (granular breakdowns)

Individual protocols, networks, or platforms within each category.

## Inside-Out Research Strategy

Research expands outward from the centre like ripples:

```
THE CENTRE → biggest categories TODAY (current TPS)
    Ring 1 → expand depth (historic, subcategories, projections)
    Ring 2 → medium-scale categories
    Ring 3 → smaller & emerging categories
    Ring 4 → nascent & speculative categories
```

We measure consumer cards and bank transfers before IoT micropayments
because the top 5 categories likely represent 80%+ of global TPS. Context
from the giants calibrates everything else.

## Research Capsules

A **research capsule** is the atomic unit of output: one measurement of
transactions for one category over one time period, plus all accompanying
analysis. Each Elf run targets **48+ capsules** before assessing taxonomy
gaps and preparing the next session's agenda.

See `elves/run_protocol.md` for the full 5-step run process (A-E).

## Pipeline

```
┌──────────┐     ┌────────────┐     ┌──────────┐     ┌───────────┐
│  Scout   │────▶│  Architect │────▶│  Elves   │────▶│  Publish  │
│          │     │            │     │          │     │           │
│ Find     │     │ Design     │     │ Execute  │     │ Generate  │
│ data     │     │ research   │     │ research │     │ reports,  │
│ sources  │     │ methodology│     │ & model  │     │ charts,   │
│          │     │            │     │          │     │ forecasts │
└──────────┘     └────────────┘     └──────────┘     └───────────┘
```

### 1. Scout (automated, recurring)

Discovers and validates data sources for transaction volume data:
- Central bank reports (BIS, Federal Reserve, ECB, etc.)
- Industry associations (Visa, Mastercard annual reports, WFE, FIA)
- Blockchain explorers and analytics platforms
- Gaming industry reports (Newzoo, SuperData)
- Academic papers and government statistics
- API endpoints for real-time data where available

Output: prioritised backlog of **categories** to research, with known data sources.

### 2. Architect (research design)

Takes a category and produces a research methodology:
- Identifies the best available data sources
- Defines measurement methodology (what counts as a "transaction"?)
- Designs the data collection approach
- Specifies the projection models to use
- Sets quality criteria for the research

Output per category:
- `METHODOLOGY.md` — data sources, collection plan, measurement definitions
- Updates to `TAXONOMY.md` if new categories are identified

### 3. Elves (autonomous researchers)

Execute the research plan:
- Collect data from identified sources
- Normalise to consistent units (TPS, daily volume, annual volume)
- Build historic timeseries where possible
- Generate projection models (baseline, high-growth, conservative)
- Produce charts and visualisations
- Write analysis reports

### 4. Publish (output)

All findings published to the repo:
- `analysis/<category>/REPORT.md` — full research report
- `analysis/<category>/data.json` — structured data
- `analysis/<category>/charts/` — generated visualisations
- `analysis/README.md` — master index with summary table
- `models/` — projection model definitions and outputs

## Projection Models

Three scenarios are maintained for every category:

| Model | Assumptions |
|-------|-------------|
| **Baseline** | Current growth rates continue, no major disruptions |
| **High Growth** | Accelerating digitalisation, DeFi adoption, emerging market growth |
| **Conservative** | Regulatory headwinds, market consolidation, slower adoption |

Each model projects out to **2030** and **2035** with explicit assumptions documented.

## Repo Structure

```
universe-of-finance/
├── README.md                    # This file
├── BRIEF.md                     # Mission & methodology
├── TAXONOMY.md                  # Transaction category taxonomy
├── AGENTS.md                    # AI agent discovery (agents.md standard)
├── CLAUDE.md                    # Claude Code operating instructions
├── run.sh                       # Pipeline orchestration
├── scout/                       # Data source discovery
│   ├── scout.py                 # Source scanner
│   ├── analyzer.py              # Report generator
│   ├── charts.py                # Visualisation engine
│   ├── config.yaml              # Sources, categories, filters
│   └── backlog.yaml             # Discovered categories (output)
├── architect/                   # Research methodology design
│   ├── SKILL.md                 # Architect agent instructions
│   └── references/
│       ├── methodology.md       # Research methodology patterns
│       └── quality_gates.md     # Research quality checklist
├── elves/                       # Autonomous research agents
│   ├── survival_guide.md        # Standing brief for research elves
│   ├── run_protocol.md          # Standard run protocol (Steps A-E)
│   └── validation_gates.sh      # Data validation script
├── notes/                       # Inter-session continuity
│   ├── research_agenda.md       # Next run's work queue
│   └── last_session.md          # Previous run's notes
├── categories/                  # Category specs (Architect output)
│   ├── traditional-finance/
│   │   ├── stock-exchanges/METHODOLOGY.md
│   │   ├── derivatives/METHODOLOGY.md
│   │   └── ...
│   ├── payments/
│   │   ├── consumer-cards/METHODOLOGY.md
│   │   ├── remittances/METHODOLOGY.md
│   │   └── ...
│   ├── digital-assets/
│   │   ├── defi/METHODOLOGY.md
│   │   ├── crypto-exchanges/METHODOLOGY.md
│   │   └── ...
│   └── ...
├── analysis/                    # Generated research reports
│   ├── README.md                # Master index
│   └── <category>/
│       ├── REPORT.md            # Clean, reader-facing analysis
│       ├── data.json            # Structured data with source URLs
│       ├── charts/              # Generated visualisations
│       └── workings/            # Full calculations, source notes, assumptions
├── models/                      # Projection models
│   ├── baseline/
│   ├── high-growth/
│   └── conservative/
├── data/                        # Collected raw data (structured)
├── tools/                       # Utility scripts
└── logs/                        # Run logs
```

## Key Metrics

For each transaction category, we measure:

| Metric | Unit | Description |
|--------|------|-------------|
| **Peak TPS** | tx/sec | Maximum observed transactions per second |
| **Average TPS** | tx/sec | Average sustained throughput |
| **Daily Volume** | tx/day | Total daily transaction count |
| **Annual Volume** | tx/year | Total annual transaction count |
| **Annual Value** | USD/year | Total annual transaction value |
| **Growth Rate** | %/year | Year-over-year volume growth |

## The Big Number

The ultimate deliverable is **The Big Number** — the sum total of all
financial transactions happening across the global economy, expressed as TPS.
This number is recalculated as each category completes research.

Current estimate: **TBD** (research in progress)

## Contributing

This is an open research project. To contribute:
1. Identify a transaction category not yet covered
2. Find reliable data sources for that category
3. Open an issue or PR with the data and methodology

## License

Research outputs are published under CC BY 4.0. Code is MIT licensed.

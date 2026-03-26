# Universe of Finance — Project Brief

> Measure the unmeasured: a comprehensive, open-source census of every
> financial transaction type in the global economy.

## Mission

Build the definitive open dataset of global financial transaction volumes —
historic, current, and projected — across every asset class, payment rail,
and transaction type. Published as transparent, reproducible research with
full source attribution.

## The Question We're Answering

**What is the total addressable market for financial transactions, measured
in volume (TPS)?**

Sub-questions:
- How many transactions per second does the global economy process today?
- How is that distributed across sectors (TradFi, payments, DeFi, gaming, etc.)?
- How has this changed over the last 10-20 years?
- Where is it going in the next 5-10 years?
- What are the fastest-growing categories?
- Where are the bottlenecks and underserved markets?

## Core Principles

### 1. Measure, Don't Guess

Every number must have a source. When exact data isn't available, we use
bounded estimates with explicit methodology:
- **Direct measurement**: API data, exchange reports, blockchain explorers
- **Reported figures**: Annual reports, central bank statistics, industry bodies
- **Derived estimates**: Extrapolated from partial data with documented assumptions
- **Expert consensus**: Cited analyst reports and academic papers

Every figure is tagged with its confidence level:
- 🟢 **High** — direct measurement or audited report
- 🟡 **Medium** — derived from reliable partial data
- 🔴 **Low** — estimate based on limited data or extrapolation

### 2. Consistent Units

All data normalised to consistent units for comparison:
- **TPS** (transactions per second) — the primary metric
- **Daily/Annual volume** — total transaction counts
- **USD value** — total value transacted (where meaningful)
- **Growth rate** — compound annual growth rate (CAGR)

### 3. Categories, Not Brands

We measure "consumer card payments", not "Visa". Individual networks and
platforms are data points within categories. The taxonomy is functional,
not corporate.

### 4. Transparent Methodology

Every research output includes:
- Data sources with URLs/citations
- Collection methodology
- Assumptions and limitations
- Confidence intervals where applicable
- Reproducibility instructions

### 5. Multiple Futures

No single projection. Three scenarios minimum:
- **Baseline**: extrapolate current trends
- **High Growth**: accelerating digitalisation, new categories emerge
- **Conservative**: regulatory friction, market saturation, consolidation

## Pipeline Architecture

```
Scout → Architect → Elves → Publish
```

### Scout: Data Source Discovery

The Scout module continuously identifies and validates data sources:

**Primary sources** (highest confidence):
- Bank for International Settlements (BIS) — triennial surveys, CPMI stats
- World Federation of Exchanges (WFE) — exchange statistics
- Federal Reserve, ECB, Bank of England — payments statistics
- Visa/Mastercard — quarterly earnings and annual reports
- Blockchain explorers — on-chain transaction data

**Secondary sources** (medium confidence):
- Industry reports (McKinsey, BCG, Nilson Report)
- Academic papers and government statistics
- Trade associations (FIA, ISDA, SWIFT)

**Tertiary sources** (lower confidence, useful for emerging categories):
- Gaming industry reports (Newzoo, SuperData)
- Fintech reports and startup metrics
- IoT and M2M transaction estimates

### Architect: Research Methodology Design

For each category, the Architect produces a `METHODOLOGY.md` that defines:

1. **Scope**: What counts as a "transaction" in this category?
2. **Data sources**: Ranked by reliability, with collection approach
3. **Time range**: Historic data availability (how far back?)
4. **Normalisation**: How to convert reported figures to TPS
5. **Projection approach**: Which model(s) apply and why
6. **Known gaps**: What data is missing and how to handle it
7. **Cross-references**: Related categories and double-counting risks

### Elves: Research Execution

Autonomous research agents that:
- Collect data from identified sources
- Parse and normalise to standard format
- Build timeseries datasets
- Run projection models
- Generate visualisations
- Write analysis reports

### Publish: Output Generation

All outputs committed to the repo:
- Per-category research reports with charts
- Master summary table
- Aggregate "Big Number" calculation
- Model comparison visualisations

## Integration Points

| System | Integration |
|--------|-------------|
| **Radix North Pole** | DeFi transaction data feeds North Pole's market sizing |
| **Blokenet** | Infrastructure capacity requirements derived from TPS projections |
| **FirehoseFM** | Research findings can be narrated as content segments |

## Quality Gates

Before any research output publishes:

- [ ] All figures have cited sources
- [ ] Confidence levels assigned to every estimate
- [ ] Methodology documented and reproducible
- [ ] Double-counting risks identified and addressed
- [ ] Charts render correctly with labelled axes
- [ ] Projection assumptions explicitly stated
- [ ] Peer categories cross-referenced for consistency
- [ ] Data structured in machine-readable format (JSON)

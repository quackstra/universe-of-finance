---
title: About
nav_order: 4
---

# About the Universe of Finance

The Universe of Finance is an open research project with a single mission: **measure every financial transaction on Earth** and express it as one number — transactions per second.

From Visa swipes to repo trades, UPI taps to video game loot boxes, we count them all, de-duplicate the overlaps, and publish the result with full methodology and workings.

## The Two Numbers

### The Big Number: ~73,750 TPS

The de-duplicated global financial throughput — roughly 2.3 trillion transactions per year flowing through the world's financial infrastructure. Range: 67,000--83,000 TPS depending on overlap assumptions. This counts distinct economic events: a card payment, a stock trade, a remittance.

### The MEST Number: ~545,000/s

Monetary-Equivalent Settlement Throughput — the total bilateral state changes the financial system actually performs. Every transaction triggers a cascade: authorization, clearing, settlement, custody updates, reconciliation, regulatory reporting. A single card swipe generates ~7 MESTs. An OTC derivative trade generates ~12. The MEST multiplier across all categories averages **7.4x** the Big Number.

## Methodology

Every category is researched using a **triangulation-first** approach:

1. Find 2--3 independent data sources that measure the same thing differently
2. Build bottom-up AND top-down models, then reconcile
3. Document assumptions, blind spots, and confidence explicitly
4. Quantify overlaps with other categories to enable accurate de-duplication

No single source is trusted alone. Where sources disagree, the delta becomes the confidence interval.

## Soul Less Employees

Research is guided by **17 AI expert personas** grounded in real job descriptions from organizations including Visa, BIS, DTCC, Chainalysis, BNY Mellon, Gartner, and BlackRock. Each persona brings domain-specific mental models, preferred data sources, and documented biases to check against.

An Intergalactic Recruiter persona manages dispatch — matching research questions to the right expert based on domain fit, not keyword matching. See the [SLE Profiles](explore/souls.html) for the full roster.

## Research Runs

| Run | Focus |
|:----|:------|
| 1 | Initial 24-category pass — first Big Number (~76,000 gross) |
| 2 | Overlap quantification — de-duplicated to ~70,600 |
| 3 | Deep triangulation + tooling — China model, Solana filter, Big Number calculator |
| 4 | Confidence upgrades + regional decomposition — scorecard (34--91) |
| 5 | New categories + time-series + scenarios — 29 categories, 2015--2025 series |
| 6 | Methodology overhaul + measurement SLEs — METHODOLOGY.md for all 29 categories |
| 7 | MEST framework + deep dives + confidence uplift — India and China deep dives |
| 8 | GitHub Pages + USA deep dive + MEST validation — interactive dashboard |
| 9 | MEST Advantage Paper — DLT compression thesis with cost modeling |

## Data Structure

Each of the 29 categories is a **research capsule** containing:

- `REPORT.md` — Reader-facing analysis with key findings, TPS estimate, and confidence score
- `data.json` — Structured data following a normalized schema (validated by `tools/validate_schema.py`)
- `workings/` — Full calculations, source notes, assumptions, and intermediate estimates

Cross-cutting analyses (overlap matrix, confidence scorecard, peak TPS, scenarios, time-series) sit at the `analysis/` level and draw from all capsules.

## How to Cite

> Universe of Finance, [quackstra.github.io/universe-of-finance](https://quackstra.github.io/universe-of-finance), 2026.

## License

Research outputs: **CC BY 4.0**. Code: **MIT**.

## Source

[GitHub Repository](https://github.com/quackstra/universe-of-finance)

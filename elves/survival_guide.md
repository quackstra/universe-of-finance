# Universe of Finance — Elves Survival Guide

> Standing brief for autonomous research agents. Re-read after every
> context compaction.

## Your Role

You are a research Elf — an autonomous agent that executes financial
research following a methodology designed by the Architect. You collect
data, normalise it, build projections, create visualisations, and write
analysis reports.

**Before starting work**, read `elves/run_protocol.md` for the full
session protocol (Steps A-E) and inside-out prioritisation rules.

## Research Capsules

A **research capsule** is your atomic unit of output: one measurement of
transactions for one category over one time period, plus all accompanying
analysis. Your target is **48+ capsules per run**. See `run_protocol.md`
for the full definition.

## Inside-Out Priority

Always work from the centre outward:
1. **Biggest categories TODAY** (current TPS) — consumer cards, bank transfers, equity markets
2. **Expand depth** on those (historic data, subcategories, projections)
3. **Medium categories** (FX, crypto, gaming)
4. **Smaller/emerging categories** (IoT, AI agents, RWAs)

The research agenda in `notes/research_agenda.md` specifies the current queue.

## Core Rules

### 1. Follow the Methodology

Every category has a `METHODOLOGY.md` written by the Architect. Follow it
precisely. The methodology specifies:
- What to measure and what to exclude
- Which data sources to use (in priority order)
- How to normalise data to TPS
- Which projection models to apply
- What quality checks to run

**Do not invent your own methodology.** If the methodology has a gap,
flag it — don't silently fill it with assumptions.

### 2. Every Number Needs a Source — Cite Heavily

No number appears in a report without a citation. **Hyperlink directly to
the source whenever possible.** Do not leave any relevant source uncited.

Format for reports (with hyperlinks):

```markdown
Consumer card networks processed approximately 640 billion transactions
in 2024 ([Nilson Report #1243, March 2025](https://nilsonreport.com/...)),
equivalent to ~20,300 TPS average.
```

For derived calculations, **show the math** inline or link to workings:

```markdown
Average TPS = 640B transactions / (365 days × 86,400 sec/day) = **20,289 TPS**
(see [detailed calculation](workings/calculations.md#consumer-cards-tps))
```

For data.json, every data point includes source URL:

```json
{
  "value": 20289,
  "source": "Nilson Report #1243, March 2025",
  "url": "https://nilsonreport.com/...",
  "confidence": "high",
  "accessed": "2026-03-26"
}
```

When multiple sources disagree, report the range and explain the discrepancy.
Prefer primary sources over secondary, recent over old, audited over estimated.

### 3. Tag Confidence Honestly

Every figure gets a confidence tag:
- 🟢 **High** — direct measurement or audited report
- 🟡 **Medium** — derived from reliable partial data
- 🔴 **Low** — estimate based on limited data or extrapolation

When in doubt, tag lower. Honesty about uncertainty is more valuable than
false precision.

### 4. Show All Work — But Keep Reports Clean

Use the `workings/` subdirectory to separate the audit trail from the
consumable report:

```
analysis/<sector>/<category>/
├── REPORT.md              # Clean, reader-facing analysis
├── data.json              # Structured data
├── charts/                # Visualisations
└── workings/              # Full audit trail
    ├── calculations.md    # Step-by-step math with all assumptions
    ├── source_notes.md    # Extended notes on each source consulted
    └── assumptions.md     # Detailed assumption documentation
```

**REPORT.md** = concise, every number hyperlinked, calculations summarised.
**workings/** = full derivations, raw source extracts, assumption reasoning.
Anyone questioning a number drills into workings/ for the paper trail.

### 5. Structured Data First, Prose Second

Before writing the narrative report:
1. Collect all data points into `data.json`
2. Write calculation derivations to `workings/calculations.md`
3. Generate charts from the structured data
4. Write the report referencing the data, charts, and workings

The JSON is the source of truth. The report is the explanation. The
workings/ directory is the audit trail.

### 6. Charts Must Be Correct

Every chart must:
- Have labelled axes with units
- Include a title and data source attribution
- Use consistent colour schemes across the project
- Be generated from `data.json`, not hand-drawn
- Render as PNG for GitHub display

Use matplotlib with the project's standard style (see `scout/charts.py`).

### 7. Three Projections, Always

Every category gets three projection scenarios:
- **Baseline**: current trends continue
- **High Growth**: accelerating factors dominate
- **Conservative**: headwinds dominate

Each scenario must have **numbered, explicit assumptions**. A projection
without assumptions is a guess, not a model.

## Output Structure

For each category, produce:

```
analysis/<sector>/<category>/
├── REPORT.md          # Clean, reader-facing analysis (hyperlinked sources)
├── data.json          # Structured data (all figures, sources, projections)
├── charts/
│   ├── historic_tps.png       # Historic TPS timeseries
│   ├── volume_breakdown.png   # Subcategory breakdown
│   ├── projections.png        # Three-scenario projection chart
│   └── ...                    # Additional charts as needed
└── workings/
    ├── calculations.md    # Full math: every derivation, step by step
    ├── source_notes.md    # Extended notes on each source consulted
    └── assumptions.md     # All assumptions documented with reasoning
```

### REPORT.md Template

```markdown
# [Category Name] — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary
[2-3 sentences: current TPS, key trend, notable finding]

## Scope
[What's measured, per the methodology]

## Current State

### Transaction Volume
| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Peak TPS | ... | ... | 🟢/🟡/🔴 |
| Average TPS | ... | ... | 🟢/🟡/🔴 |
| Daily volume | ... | ... | 🟢/🟡/🔴 |
| Annual volume | ... | ... | 🟢/🟡/🔴 |
| Annual value | ... | ... | 🟢/🟡/🔴 |

### Historic Trend
[Chart: historic_tps.png]
[Narrative explaining the trend]

### Subcategory Breakdown
[Chart: volume_breakdown.png]
[Table with per-subcategory figures]

## Projections

### Baseline (Current Trends Continue)
**Assumptions:**
1. [Explicit assumption]
2. [Explicit assumption]

| Year | Projected TPS | Annual Volume |
|------|---------------|---------------|
| 2026 | ... | ... |
| 2028 | ... | ... |
| 2030 | ... | ... |
| 2035 | ... | ... |

### High Growth
**Assumptions:**
1. [Different assumption]
2. [Different assumption]

[Same table format]

### Conservative
**Assumptions:**
1. [Restrictive assumption]
2. [Restrictive assumption]

[Same table format]

[Chart: projections.png — all three scenarios on one chart]

## Key Findings
1. [Notable insight]
2. [Notable insight]
3. [Notable insight]

## Data Quality & Limitations
- [Known gaps]
- [Confidence caveats]
- [Double-counting considerations]

## Sources
1. [Full citation]
2. [Full citation]
...
```

### data.json Schema

```json
{
  "category": "string",
  "sector": "string",
  "last_updated": "YYYY-MM-DD",
  "current": {
    "peak_tps": { "value": 0, "source": "", "confidence": "high|medium|low" },
    "avg_tps": { "value": 0, "source": "", "confidence": "high|medium|low" },
    "daily_volume": { "value": 0, "source": "", "confidence": "high|medium|low" },
    "annual_volume": { "value": 0, "source": "", "confidence": "high|medium|low" },
    "annual_value_usd": { "value": 0, "source": "", "confidence": "high|medium|low" }
  },
  "historic": [
    { "year": 2020, "annual_volume": 0, "avg_tps": 0, "source": "" }
  ],
  "projections": {
    "baseline": [
      { "year": 2026, "tps": 0, "annual_volume": 0 }
    ],
    "high_growth": [
      { "year": 2026, "tps": 0, "annual_volume": 0 }
    ],
    "conservative": [
      { "year": 2026, "tps": 0, "annual_volume": 0 }
    ]
  },
  "subcategories": [
    { "name": "", "tps": 0, "share_pct": 0 }
  ],
  "sources": [
    { "id": 1, "citation": "", "url": "", "accessed": "YYYY-MM-DD" }
  ]
}
```

## Git Protocol

- Commit prefix: `[UoF] <category>: <what>`
- One category per research batch
- NEVER force push or reset hard
- Commit data.json and charts before the report (data first)

## Validation Gates

After completing research on a category, run `elves/validation_gates.sh`:
1. JSON schema validation (data.json is well-formed)
2. Source citation check (every number in REPORT.md has a source)
3. Chart render check (all referenced PNGs exist)
4. Projection sanity check (no negative TPS, no >100% CAGR without justification)

Only commit if all gates pass.

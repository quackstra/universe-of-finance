# Universe of Finance — Elves Survival Guide

> Standing brief for autonomous research agents. Re-read after every
> context compaction.

## Your Role

You are a research Elf — an autonomous agent that executes financial
research following a methodology designed by the Architect. You collect
data, normalise it, build projections, create visualisations, and write
analysis reports.

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

### 2. Every Number Needs a Source

No number appears in a report without a citation. Format:

- Direct data: `4,200 TPS (Source: Visa Q3 2025 Earnings, p.12)`
- Derived: `~3,500 TPS (Derived: 302M daily tx / 86,400 sec; Source: WFE Monthly Stats, Jan 2026)`
- Estimate: `~500-800 TPS (Estimate: based on [methodology]; Confidence: 🟡 Medium)`

### 3. Tag Confidence Honestly

Every figure gets a confidence tag:
- 🟢 **High** — direct measurement or audited report
- 🟡 **Medium** — derived from reliable partial data
- 🔴 **Low** — estimate based on limited data or extrapolation

When in doubt, tag lower. Honesty about uncertainty is more valuable than
false precision.

### 4. Structured Data First, Prose Second

Before writing the narrative report:
1. Collect all data points into `data.json`
2. Generate charts from the structured data
3. Write the report referencing the data and charts

The JSON is the source of truth. The report is the explanation.

### 5. Charts Must Be Correct

Every chart must:
- Have labelled axes with units
- Include a title and data source attribution
- Use consistent colour schemes across the project
- Be generated from `data.json`, not hand-drawn
- Render as PNG for GitHub display

Use matplotlib with the project's standard style (see `scout/charts.py`).

### 6. Three Projections, Always

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
├── REPORT.md          # Full research report
├── data.json          # Structured data (all figures, sources, projections)
└── charts/
    ├── historic_tps.png       # Historic TPS timeseries
    ├── volume_breakdown.png   # Subcategory breakdown
    ├── projections.png        # Three-scenario projection chart
    └── ...                    # Additional charts as needed
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

# Universe of Finance — Standard Elf Run Protocol

> This document defines the standard structure for a single autonomous
> research run. Every Elf session follows steps A through E in order.
> Re-read this after every context compaction.

## Inside-Out Prioritisation

Research expands outward from the centre like ripples:

```
                         ┌─ Future (projections)
                    ┌────┤
               ┌────┤    └─ Past (historic data)
          ┌────┤    │
     ┌────┤    │    └─ Smaller categories
     │    │    └─ Medium categories
     │    └─ Biggest categories TODAY (current TPS)
     └─ THE CENTRE: largest transaction volumes right now
```

**Start with the biggest categories by current transaction volume.**
Measure what's happening *today* first. Then expand:
- **Outward by scale**: from the biggest categories to progressively smaller ones
- **Outward in time**: from the present into historic data and future projections
- **Outward in detail**: from headline numbers to subcategory breakdowns

This means the first research capsules should be current-year TPS estimates
for the highest-volume categories (consumer cards, bank transfers, equity
markets). Only after these are established do we invest in deep historics,
granular subcategories, or emerging/nascent categories.

### Why Inside-Out?

1. **The Big Number gets useful fast** — even rough estimates of the top 5
   categories give us 80%+ of total global TPS
2. **Context compounds** — understanding the biggest categories first gives
   context for calibrating smaller ones
3. **Diminishing returns are visible** — we can see when additional research
   effort adds less marginal precision to the total

## Research Capsules

A **research capsule** is the atomic unit of research output:

> One measurement of transactions for one category over one time period,
> plus all accompanying analysis.

Examples of research capsules:
- "Consumer Card Payments — 2025 current TPS estimate"
- "Equity Markets — 2020-2025 historic timeseries"
- "DeFi DEX Swaps — 2030 baseline projection"
- "Foreign Exchange — subcategory breakdown (spot/forward/swap/options)"

Each capsule has:
- A **finding** (the number or dataset)
- **Sources** (cited, hyperlinked)
- **Methodology** (how the number was derived)
- **Confidence** tag (🟢/🟡/🔴)
- **Calculations** shown in full (in supporting files if complex)

A capsule is "complete" when it passes validation and is committed.

### Capsule Sizing

Not all capsules are equal effort. A current-year TPS estimate from a
published report might take minutes. A 10-year historic reconstruction
from scattered sources might take significant effort. The 48-capsule
target per run is a throughput floor, not a ceiling — adjust if capsules
are unusually heavy.

## Standard Run Steps

### Step A: Session Start — Review & Orient

1. **Read `notes/last_session.md`** — pick up where the last run left off
2. **Read `notes/research_agenda.md`** — the planned work queue for this run
3. **Run `./run.sh scout`** — refresh the backlog to see current state
4. **Check `analysis/README.md`** — see what's already done
5. **Plan the session** — select which capsules to produce, following
   inside-out priority from the research agenda

If no `last_session.md` exists (first run), start from the top of the
scout backlog, targeting current-year TPS for the highest-volume categories.

### Step B: Research — Produce Capsules (target: 48+)

Execute research following inside-out priority:

1. For each category in priority order:
   a. If no methodology exists, design one (Architect step)
   b. Collect data, compute metrics, cite sources
   c. Write findings to the appropriate analysis files
   d. Generate charts where useful
   e. Run validation gates
   f. Commit the capsule

2. Track capsule count. Continue expanding outward until at least **48
   research capsules** have been produced in this session. A capsule counts
   when it has:
   - A quantified finding with source citation
   - Confidence tag
   - Calculation methodology (inline for simple, `workings/` for complex)
   - Passed validation

3. **Cross-pollinate as you go** — if researching consumer cards reveals a
   data source useful for bank transfers, note it for that category's turn.

### Step C: Taxonomy Review — Assess Coverage

After hitting the 48-capsule floor, step back and assess:

1. **Missing sectors?** — Has research revealed transaction types not in
   TAXONOMY.md? (e.g., "insurance premium payments" might not fit neatly
   into existing categories)
2. **Missing categories?** — Are there significant sub-segments within
   existing sectors that deserve their own research track?
3. **Category splits?** — Is a category too broad? Should "Digital Wallets"
   be split into "Developed Market Wallets" and "Emerging Market Wallets"?
4. **Category merges?** — Are two categories so overlapping that they should
   be combined?

Update `TAXONOMY.md` and `scout/config.yaml` if changes are needed.
Document the rationale in `notes/taxonomy_changes.md`.

### Step D: Retrospective — Review Prior Research

Review existing research for updates needed:

1. **Stale data** — Any categories where newer data is now available?
2. **Cross-category conflicts** — Do any findings from this run conflict
   with prior research? (e.g., a total that should sum correctly doesn't)
3. **Confidence upgrades** — Can any 🔴 Low estimates be upgraded with
   new data found during this run?
4. **Double-counting discoveries** — Have you found overlap between
   categories that wasn't previously identified?
5. **Methodology improvements** — Based on what you learned, should any
   METHODOLOGY.md be revised?

Create issues or notes for each finding. Fix quick wins immediately.
Queue larger revisions for the next run's research agenda.

### Step E: Session End — Prepare Notes for Next Run

Write two files:

#### `notes/last_session.md`

```markdown
# Last Session Notes — [DATE]

## Capsules Produced: [COUNT]

## Categories Researched
- [category]: [what was done]
- [category]: [what was done]

## Key Findings
- [Notable discovery or insight]

## Taxonomy Changes
- [Any additions/modifications to TAXONOMY.md]

## Issues Found in Prior Research
- [Any conflicts or stale data discovered]

## Unfinished Work
- [Anything started but not completed]
```

#### `notes/research_agenda.md`

```markdown
# Research Agenda — Next Run

## Priority Queue (inside-out order)
1. [Next highest-priority capsule/category]
2. [...]
3. [...]

## Revisions Needed
- [Prior research that needs updating]

## New Categories to Add
- [Any categories identified in Step C]

## Data Sources to Investigate
- [Sources discovered during this run that weren't used yet]
```

Commit both files with prefix `[UoF] session-notes:`.

## File Organisation for Supporting Materials

To keep reports clean but still show all work:

```
analysis/<sector>/<category>/
├── REPORT.md              # Clean, consumable analysis
├── data.json              # Structured data
├── charts/                # Visualisations
└── workings/              # Supporting calculations and source notes
    ├── calculations.md    # Full math with step-by-step derivations
    ├── source_notes.md    # Extended notes on each source
    └── assumptions.md     # Detailed assumption documentation
```

- **REPORT.md** — the reader-facing document. Concise, well-structured,
  every number hyperlinked to its source. Calculations summarised in-line.
- **workings/** — the audit trail. Full calculations, raw source extracts,
  detailed assumption reasoning. Anyone questioning a number in the report
  can drill into workings/ for the complete paper trail.

## Citation Standards

### In Reports

Every number must link to its source. Format:

```markdown
Consumer card networks processed approximately 640 billion transactions
in 2024 ([Nilson Report #1243, March 2025](https://nilsonreport.com/...)),
equivalent to ~20,300 TPS average.
```

For derived calculations, show the work inline or link to workings:

```markdown
Average TPS = 640B transactions / (365 days × 86,400 sec/day) = **20,289 TPS**
(see [detailed calculation](workings/calculations.md#consumer-cards-tps))
```

### In data.json

Every data point includes source URL:

```json
{
  "value": 20289,
  "source": "Nilson Report #1243, March 2025",
  "url": "https://nilsonreport.com/...",
  "confidence": "high",
  "accessed": "2026-03-26"
}
```

### In Workings

Full citations with:
- Document title, author, publication date
- Specific page/table/chart number
- Direct URL (hyperlinked)
- Date accessed
- Relevant excerpt or screenshot description

### Source Ranking

When multiple sources disagree:
1. Prefer primary sources (the entity's own report) over secondary
2. Prefer more recent data over older
3. Prefer audited/official figures over estimates
4. When sources conflict, report the range and explain the discrepancy

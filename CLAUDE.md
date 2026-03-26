# Universe of Finance — Claude Code Operating Instructions

## Project Identity

This is **Universe of Finance** — an autonomous research framework measuring
global financial transaction volumes. Part of the Quackstra ecosystem.

## Code Standards

### Python
- Target: Python 3.12+
- Style: Black formatter defaults (line length 88)
- Type hints on public functions
- Tests: pytest

### Git
- Commit prefix: `[UoF]` for framework, `[UoF] <category-slug>:` for research
- Commits describe the "why", not the "what"

### Data
- All structured data in JSON (data.json per category)
- Charts as PNG, generated from data via matplotlib
- Reports in Markdown with source citations

## Pipeline

```
Scout → Architect → Elves → Publish
```

- `run.sh scout` — refresh category backlog
- `run.sh architect` — design methodology for next pending category
- `run.sh analyze` — execute research for next methodology-ready category
- `run.sh all` — full pipeline

## Key Files

- `TAXONOMY.md` — the transaction category taxonomy (living document)
- `scout/config.yaml` — data source configuration
- `scout/backlog.yaml` — prioritised research backlog (auto-generated)
- `architect/SKILL.md` — Research Architect instructions
- `elves/survival_guide.md` — Research Elf standing brief

## Rules

- Every number in a report MUST have a cited source
- Every estimate MUST have a confidence tag (🟢/🟡/🔴)
- Every projection MUST have three scenarios with explicit assumptions
- NEVER fabricate data sources — if a source doesn't exist, say so
- ALWAYS run validation gates before committing research outputs
- NEVER commit secrets or API keys

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

## Trigger Phrases

When Ferg says **"okay elves, explore the universe"**, immediately execute
a full autonomous elf run:

1. `cd /home/quackstra/universe-of-finance`
2. Execute the full Steps A-E protocol from `elves/run_protocol.md`
3. Target 48+ research capsules per run, inside-out priority
4. This is a fire-and-go command — no confirmation needed, just start working

## Pipeline

```
Scout → Architect → Elves → Publish
```

- `run.sh scout` — refresh category backlog
- `run.sh architect` — design methodology for next pending category
- `run.sh analyze` — execute research for next methodology-ready category
- `run.sh elf-run` — full autonomous elf run (Steps A-E, 48+ capsules)
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

# Research Quality Gates

> Checklist for validating research outputs before publication.

## Methodology Quality (Architect output)

| # | Gate | Description |
|---|------|-------------|
| 1 | Scope clarity | "Transaction" precisely defined; included/excluded explicit |
| 2 | Source validity | At least one primary source identified with URL/reference |
| 3 | Source diversity | Multiple independent sources for cross-validation |
| 4 | Normalisation rigour | TPS conversion formula explicit and testable |
| 5 | Gap honesty | Known data gaps acknowledged, not papered over |
| 6 | Double-count awareness | Overlap with adjacent categories identified |
| 7 | Projection diversity | Three distinct scenarios with different assumptions |
| 8 | Falsifiability | Predictions specific enough to be proven wrong |

## Research Output Quality (Elves output)

| # | Gate | Description |
|---|------|-------------|
| 1 | Source citation | Every number has a cited source |
| 2 | Confidence tagging | Every estimate tagged 🟢/🟡/🔴 |
| 3 | Unit consistency | All figures in standard units (TPS, daily, annual) |
| 4 | Sanity check | Numbers pass basic reasonableness tests |
| 5 | Cross-reference | At least two independent sources agree (±20%) |
| 6 | Chart accuracy | Visualisations match underlying data |
| 7 | Data structured | Raw data in machine-readable JSON |
| 8 | Reproducible | Another researcher could recreate the analysis |

## Sanity Checks

Apply these common-sense tests to every estimate:

- **Population check**: Does the daily transaction count exceed the
  relevant population? (e.g., 10B card transactions/day with 4B cardholders
  = 2.5 tx/person/day — plausible?)
- **Hours check**: Does the peak TPS assume transactions happen 24/7 or
  only during business hours?
- **Growth check**: Does the projected CAGR exceed 50%? If so, justify
  explicitly (only plausible for very early-stage categories)
- **Sum check**: Do the subcategories sum to approximately the total?
  (±10% tolerance for rounding and gaps)
- **Value/volume ratio**: Is the implied average transaction size reasonable?
  (e.g., $50M average for consumer payments = something is wrong)

## Scoring (0-100)

For research outputs, score across these dimensions:

| Dimension | Weight | Scoring Criteria |
|-----------|--------|------------------|
| Data quality | 0.30 | Sources, confidence, cross-validation |
| Completeness | 0.25 | Coverage of subcategories, time range |
| Methodology | 0.20 | Rigour, reproducibility, normalisation |
| Projections | 0.15 | Model quality, assumption clarity |
| Presentation | 0.10 | Charts, clarity, structure |

# Last Session Notes — 2026-07-19 (Run 13)

## Run Completed This Session: Run 13 — "The Gulf & the Corridors"

Theme: fill the last major regional gap (the Middle East), then follow the value/count
thread it exposes into insurance claims and remittance corridors. Also fixed a broken
core tool discovered at session start.

## Capsules Produced: ~48

## Categories / Tracks Researched

- **Infrastructure fix** — `tools/big_number.py` crashed at session start
  (`KeyError: 'slug'`). Root cause: the loader walked *all* `data.json` files, including
  `deep-dives/*/` and `timeseries/` which are not category files and lack a `slug`. Fixed
  by skipping files without a slug. Big Number recomputes cleanly at **73,716 TPS**.

- **Middle East / Gulf deep dive** (NEW, centerpiece) — the last major region without a
  deep dive. ~800 TPS (~1.1% of global). Per-country: Saudi ~400 (12.6B non-cash retail,
  mada 8.9B, sarie 593M), UAE ~155 (Aani, cards Dh511.4B, $50B remittance origin),
  Kuwait ~45 (KNET), Qatar ~35 (Fawran), Bahrain ~20 (BenefitPay 421M), Oman ~15,
  Israel ~100, Levant ~30. Signature insight: **the Middle East is Africa inverted** —
  low transaction count, extreme value per transaction (SWFs ~$4-5T, oil settlement,
  world's #2-3 remittance origin). REPORT + data.json + workings.

- **Insurance Claims deep dive** (NEW) — followed up Run 12's most surprising finding.
  Separated the claim lifecycle: **claim events** (administrative EDI) ~35B/yr = ~1,110
  TPS gross vs **settlement payments** (money) ~2.5-4B/yr = ~80-130 TPS gross vs
  **net-new to Big Number** ~90-100 TPS (refined from Run 12's 55-148). Batch ratio
  (4-8 claims/payment) is the dominant uncertainty. Confidence 55→60 (🔴→🟡).

- **Remittance Corridor mapping** (NEW) — top 10 corridors, ~$194.5B, ~18.7 TPS
  (~33% of global remittance count). Per-corridor value/ticket/txns/TPS/informal-share.
  US→Mexico is #1 (6.06 TPS). Gulf originates 6 of the top 10.

## Key Findings

- **The value/count spectrum has two poles.** Africa (Run 11) = maximal count, minimal
  value. Middle East (Run 13) = minimal count, maximal value. Every category sits
  somewhere on this axis, and it is the cleanest organizing principle we have found.
- **Independent triangulation held.** Gulf outbound remittance TPS derived in the Middle
  East deep dive (~7.5) matched the Gulf-corridor sum in the Remittance Corridors deep
  dive (~7.5) within 1% — two different methods, same answer. ✅
- **Insurance is a messaging industry with a payment attached.** 20× more administrative
  events than money-movements. Always specify the layer.
- **Sovereign digitization is real and fast.** Saudi went 70%→79% retail-electronic in a
  single year — faster than any market-driven transition on record.

## Taxonomy Changes

See `notes/taxonomy_changes.md`. Summary: no new Big Number *categories* (SWF flows and
insurance claims are documented as value-not-count adjacencies / blind spots, not counted
categories). One new blind-spot entry proposed: **Sovereign Wealth / wholesale sovereign
flows** — the purest value/count decoupling catalogued.

## Issues Found in Prior Research

- `big_number.py` was silently broken since country deep dives were added (their data.json
  files broke the category loader). **Fixed this run.** Recommend a CI smoke-test that runs
  `big_number.py` so this cannot regress.
- The Run 12 "conservative Big Number revision to ~76,900 TPS" is **not** reflected in the
  category `data.json` values, so the programmatic tool still returns 73,716. This gap is
  unresolved — see research agenda Tier 1. The number should be either integrated into the
  data (updating China/insurance/remittance category values + adding shadow-banking/e-CNY
  rows) or explicitly documented as a manual overlay separate from the programmatic figure.

## Unfinished Work

- Big Number reconciliation (73,716 programmatic vs 76,900 Run 12 overlay) — deferred to
  next run; needs a decision on whether to mutate category data.json or keep as overlay.
- No CI smoke-test added yet for big_number.py (recommended above).

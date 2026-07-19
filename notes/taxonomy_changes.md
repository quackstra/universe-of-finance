# Taxonomy Changes — Run 13 (2026-07-19)

## Decision Summary: No new counted categories; one new blind-spot entry.

Run 13 produced three deep dives (Middle East, Insurance Claims, Remittance Corridors).
Each raised a taxonomy question. Resolutions:

### 1. Sovereign Wealth / wholesale sovereign flows — ADD as blind-spot (not a category)

The Middle East deep dive surfaced ~$4-5T in GCC sovereign wealth fund AUM transacting at
near-zero count but extreme value-per-ticket. This is the purest **value/count decoupling**
in the project — the exact mirror of African mobile money.

- **Do NOT** add as a Big Number (TPS) category — its transaction count is negligible
  (perhaps single-digit TPS × 10⁻³), so it adds nothing to the count-based Big Number.
- **DO** add to the value-not-count blind-spots section (alongside Run 12's opaque
  categories), because it is enormous by *value* and by *systemic importance*.
- Recommended taxonomy note: "7.x Sovereign Wealth & Wholesale Sovereign Flows —
  value-dominant, count-negligible. Not summed into the Big Number; tracked for the
  Total-Value and TTR frameworks."

### 2. Insurance Claims — CONFIRMED as adjacency, NOT a standalone category

The Insurance Claims deep dive explicitly recommends keeping claims as a documented
adjacency (~95 TPS net-new) rather than a counted category, because ~85-90% of claim
settlement value already rides counted ACH/card rails. The existing **Insurance Premiums**
category (inbound) is unchanged. No taxonomy edit required beyond a cross-reference.

### 3. Remittance sub-corridors — NO split needed

The corridor mapping deepens the existing **Remittances** category but does not warrant
splitting it. Corridors are an analysis lens, not separate rails. Keep Remittances as one
category; the corridor deep dive lives under `deep-dives/`.

## Category count unchanged: 29 counted categories.

## Recommended TAXONOMY.md edits (for next run to apply)
- Add the Sovereign Wealth blind-spot entry under the value-not-count section.
- Add a cross-reference from Insurance Premiums → Insurance Claims deep dive.
- Add a cross-reference from Remittances → Remittance Corridors deep dive.

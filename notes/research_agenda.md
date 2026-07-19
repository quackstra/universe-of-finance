# Research Agenda — Next Run (Run 14)

> Updated 2026-07-19 after completing Run 13 (The Gulf & the Corridors).

## Status: Run 13 Complete

Middle East / Gulf deep dive published (last major regional gap filled). Insurance Claims
and Remittance Corridors deep dives added. `tools/big_number.py` slug crash fixed. ~48
capsules. No new counted categories; Sovereign Wealth added as a value-not-count blind spot.

## Priority Queue (inside-out order)

### Tier 1: Resolve the Big Number reconciliation (carried from Run 13)

1. **Programmatic vs overlay gap.** The tool returns **73,716 TPS**; Run 12's "conservative
   revision" claimed **~76,900 TPS**. These are not reconciled. Decide and execute ONE of:
   - (a) Integrate the revision into category `data.json` (update China/insurance/
     remittance values; add shadow-banking + e-CNY rows) so the tool returns ~76,900, OR
   - (b) Formalize a "manual overlay" layer in `big_number.py` (a documented additive block
     for opaque/net-new categories) so both the base 73,716 and the overlay total are
     reported side by side.
   Recommendation: (b) — keeps the audited base clean and makes the overlay explicit.

2. **Add a CI smoke-test** that runs `tools/big_number.py` and asserts a non-crash + a
   plausible total range. The slug bug went undetected for multiple runs; a 5-line test
   prevents recurrence. (See `.github/` — a workflow likely already exists to extend.)

### Tier 2: Apply the Run 13 taxonomy notes

3. Apply `notes/taxonomy_changes.md`: add the Sovereign Wealth blind-spot entry to
   TAXONOMY.md; add cross-references (Insurance Premiums↔Claims, Remittances↔Corridors).

### Tier 3: Deepen the value/count framework

4. **The Value/Count Spectrum paper** — Run 13 crystallized a strong organizing principle:
   Africa (max count, min value) ↔ Middle East (min count, max value). Publish a standalone
   cross-cutting paper plotting every category on this axis (value-per-transaction on one
   axis, TPS on the other). This is a genuinely novel framing worth a shareable document
   (like the MEST Advantage paper).

5. **China Shadow Banking v2** — get 2025 PBOC WMP data (still pending from Run 12/13).

6. **e-CNY / mBridge tracking** — UAE + Saudi are mBridge participants (surfaced in the
   Middle East deep dive). Track mBridge production milestones; this is where CBDC meets
   high-value cross-border settlement.

### Tier 4: Remaining country/region deep dives

7. **Turkey** — deliberately excluded from the Middle East deep dive (Europe/Asia bridge,
   huge lira transaction volumes, high inflation → high nominal TPS). Deserves its own dive.
8. **Southeast Asia** (Indonesia/Vietnam/Philippines domestic) — QRIS, VietQR growth.

## Revisions Needed

- Integrate or overlay the Run 12 ~76,900 figure (Tier 1 above) — the single biggest
  open inconsistency in the corpus.
- Consider upgrading Remittances category confidence given the new corridor triangulation.

## Data Sources to Investigate (carried + new)

- **PBOC 2025 Annual Report** — WMP, shadow banking, e-CNY.
- **BIS mBridge status updates** — production milestones.
- **World Bank Migration & Development Brief 41** (next edition) — refreshed corridor data.
- **NAIC / CAQH 2025 Index** — refine the insurance claim batch ratio (dominant uncertainty).
- **SAMA / CBUAE / QCB annual reports** — firmer Gulf transaction counts to upgrade
  Middle East confidence from 56.

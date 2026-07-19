# Remittance Corridors — Calculations

> Run 13 (2026-07-19). SECONDS_PER_YEAR = 31,536,000.
> Method: TPS = annual_txns / SPY, where annual_txns = corridor_value / avg_ticket.
> Arithmetic verified programmatically (implied txns == stated txns for all 10 corridors).

## Per-corridor derivation

For each corridor: `txns = value_USD / avg_ticket_USD`; `TPS = txns / 31,536,000`.

| Corridor | Value | Ticket | Txns | TPS |
|----------|-------|--------|------|-----|
| US→Mexico | $65B | $340 | 191.2M | 6.06 |
| Nepal→India | $13.5B | $150 | 90.0M | 2.85 |
| UAE→India | $30B | $400 | 75.0M | 2.38 |
| Saudi→India | $12B | $250 | 48.0M | 1.52 |
| US→India | $28B | $700 | 40.0M | 1.27 |
| Saudi→Pakistan | $9B | $250 | 36.0M | 1.14 |
| US→Philippines | $14B | $400 | 35.0M | 1.11 |
| UAE→Pakistan | $6B | $300 | 20.0M | 0.63 |
| UAE→Philippines | $7B | $350 | 20.0M | 0.63 |
| Kuwait/Qatar→India | $10B | $280 | 35.7M | 1.13 |
| **Total** | **$194.5B** | — | **591M** | **18.74** |

## Ticket size rationale
- **US→India ($700)**: skilled H-1B/green-card workers send larger, less frequent transfers.
- **Nepal→India ($150)**: low-wage labor, high-frequency small transfers, open border.
- **Gulf→South Asia ($250–400)**: blue-collar migrant workers, monthly wage remittances.
- **US→Mexico ($340)**: World Bank corridor average.

## Global share
- Global remittance count (category REPORT): ~1.8B txns/yr = ~57 TPS
- Top-10 = 591M txns = 18.74 TPS = **32.9% of global count**
- US→Mexico alone = 191M = **10.6% of global count**

## Informal uplift
- Global: formal $685B → true ~$1.1T = ~$415B informal = **~60% uplift** (World Bank)
- Informal tickets skew smaller (cash, ~$100–200) → higher txn count per dollar
- Top-10 blended informal share ~17% by value; applying with smaller informal tickets
  (~$180 avg) → informal txns ≈ ($194.5B × 0.17) / $180 ≈ 184M... but this over-weights;
  using marginal informal-only value of ~$33B (17% of $194.5B) at $180 ticket = 184M txns
  = 5.8 TPS. **Range ~5–8 TPS** informal uplift in top corridors.
- Consistent with Run 12 global informal remittance estimate: **+22–36 TPS** across ALL
  corridors (top-10 are ~1/4 to 1/3 of that).

## Gulf triangulation
- Gulf-originated corridors in table: UAE→India, Saudi→India, Saudi→Pakistan, UAE→Pakistan,
  UAE→Philippines, Kuwait/Qatar→India
- Sum: $30+12+9+6+7+10 = **$74B**; txns 75+48+36+20+20+35.7 = 234.7M = **7.44 TPS**
- Middle East deep dive independently estimated Gulf outbound remittances at **~7.5 TPS**
  (from UAE $50B + Saudi comparable, avg ticket ~$415). **Match within 1%.** ✅

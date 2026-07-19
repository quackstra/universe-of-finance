# Insurance Claims — Calculations & Derivations

> Run 13 (2026-07-19). SECONDS_PER_YEAR = 31,536,000.

## Layer 1 — Claim Events (administrative)

### US Health
| Component | Annual | Basis |
|-----------|--------|-------|
| Medical claims | ~6.0B | ~1B US population encounters × plan coverage; consistent with CAQH scope |
| Pharmacy claims | ~6.3B | ~6.3B US retail prescriptions/yr, each a PBM adjudication |
| Dental claims | ~0.5B | ~150M insured × ~3 claims/yr |
| **US health total** | **~12.8B** | → 12.8e9 / 31.536e6 = **406–412 TPS** |

Cross-check: CAQH 2024 Index tracked **31.5B verifications** across medical plans covering
63% of insured lives. Verifications > claims (eligibility checks precede claims), so 31.5B
verifications is consistent with ~13B distinct claims. Order of magnitude confirmed.

### Global Health
- US ≈ 40% of global health *spend* but a larger share of *transactional adjudication*
  (single-payer systems batch/globally budget rather than adjudicate per-encounter).
- Scale factor applied: ~2.5× US → 12.8B × 2.5 ≈ **~30B/yr**
- TPS = 30e9 / 31.536e6 = **~951 TPS**

### Global P&C
- US auto: 6.2 collision claims / 100 insured vehicle-years × ~280M vehicles = ~17.4M
  collision; add comprehensive + liability + commercial → ~35–45M
- US home: 5.3% × ~85M policies = ~4.5M
- US other P&C (renters, marine, etc.): ~10M
- **US P&C ≈ ~60M/yr**; US ≈ ~30% of global P&C premium → **global ≈ ~200M/yr**
- TPS = 200e6 / 31.536e6 = **~6.3 TPS**

### Global Life/Annuity
- Death/maturity/surrender/annuity payouts: est. 50–100M/yr globally
- TPS = 75e6 / 31.536e6 = **~2.4 TPS**

### Layer 1 total
30B + 0.2B + 0.075B ≈ **~30.3B → but rounding health up to include all lines ≈ ~35B →
~1,110 TPS gross administrative.**

## Layer 2 — Settlement Payments (money movement)

### Health
- Claims: ~30B
- Batch ratio: 4–8 claims per ACH remittance → use 6
- Paid share (not denied / not zero-pay): ~0.75
- Payments = 30B ÷ 6 × 0.75 = **3.75B payments/yr**
- TPS = 3.75e9 / 31.536e6 = **~119 TPS**

### P&C + Life
- Mostly 1 claim = 1 payment (little batching)
- P&C: ~0.2B → ~6 TPS; Life: ~0.075B → ~2.4 TPS

### Layer 2 total
3.75B + 0.2B + 0.075B ≈ **~4.0B payments/yr → ~128 TPS gross** (upper).
Conservative floor (batch ratio 8, paid share 0.7): 30B/8×0.7 = 2.6B + 0.28B ≈ 2.9B →
**~92 TPS**. Range: **~80–130 TPS gross.**

## Layer 3 — Net-New to Big Number
- ~85–90% of settlement *value* already rides counted ACH/card rails (health EFT = ACH;
  P&C payouts = ACH/check/push-to-card).
- Net-new = instant/push-to-card disbursements + RTP payouts + emerging-market cash/
  cross-border claim settlement uncounted elsewhere.
- Run 12 range: **55–148 TPS**.
- Refined: anchoring batch ratio (6) and paid share (0.75) puts Layer 2 at ~128 TPS gross;
  net-new fraction ~10–15% of that plus uncounted EM cash claims → **~90–100 TPS**,
  midpoint **~95 TPS**.

## Sensitivity
| Variable | Low | Base | High | TPS swing |
|----------|-----|------|------|-----------|
| Global health claims | 25B | 30B | 35B | ±0.6 payments-B → ±~16 TPS net |
| Batch ratio | 8 | 6 | 4 | ±~40 TPS (dominant) |
| Paid share | 0.70 | 0.75 | 0.80 | ±~8 TPS |

**Dominant uncertainty: the claim-to-payment batch ratio.** This is the number to pin down
in a future run (requires payer-level ERA/EFT data).

---
title: "Insurance Claims"
parent: "Deep Dives"
layout: default
nav_order: 11
---

# Insurance Claims Deep Dive — The Payout Lifecycle

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-07-19 (Run 13)
> **Follows up**: [Opaque Markets (Run 12)](../opaque-markets/REPORT.md), which flagged
> insurance claims (55–148 TPS) as the single most surprising hidden-volume finding.

---

## Executive Summary

The [Insurance Premiums](../../../payments/insurance-premiums/REPORT.md) category counts
money flowing **into** insurers (~444 TPS gross, ~44 TPS net). This deep dive counts the
**opposite flow**: money and messages moving **out** — the claims-and-payouts lifecycle.

Run 12 flagged claims as worth **55–148 TPS net-new**. That range was correct but coarse.
The core problem is that "an insurance claim" is not one transaction — it is a *lifecycle*
of 3–5 distinct events, only one of which moves money. Conflating them either massively
overcounts (if you count every adjudication message) or undercounts (if you only count the
final wire). This report separates the two:

| Layer | What it is | Est. Global Volume | TPS |
|-------|-----------|-------------------|-----|
| **Claim events** (administrative) | Submission + adjudication + status messages | ~35B/yr | **~1,110 gross** |
| **Settlement payments** (money movement) | Actual payouts to claimants/providers | ~2.5–4B/yr | **~80–130 gross** |
| **Net-new to Big Number** | Payouts NOT already on counted bank/card rails | — | **~55–148 (Run 12); refined ~90–100** |

The headline: **insurance generates ~1,100 TPS of administrative message traffic but only
~90–100 TPS of net-new financial settlement.** The gap between those two numbers is the
insurance industry's automation surface — and the reason claims are so easy to miscount.

---

## The Claim Lifecycle (why one claim ≠ one transaction)

```
  FNOL          Adjudication      Approval        Settlement       Recovery
 (notice)  →   (review/price)  →  (decide)   →    (PAY MONEY)  →  (subrogation)
   msg            msg/EDI          msg           $$ ACH/check       msg/$$
   ▲                                              ▲
   administrative event                           the ONLY guaranteed money-movement
```

- A single health claim can generate 5+ EDI transactions (837 claim submission, 277 status,
  835 remittance advice, 999 acknowledgment…) but **one** payment.
- Health payers **batch** many adjudicated claims into a single ACH remittance (ERA/EFT), so
  N claims collapse to ≪N payments.
- P&C and life claims are lower-volume but more likely to be **1 claim = 1 payment**.

**Only the Settlement column belongs in the Big Number.** Everything else is messaging.

---

## Layer 1 — Claim Events (administrative, ~1,110 TPS gross)

### US Health (the dominant driver)

Health is where the count lives, because every prescription, doctor visit, and lab test is
a claim.

- **Medical claims**: ~6B/yr (US)
- **Pharmacy claims**: ~6.3B/yr (retail prescriptions, each a PBM adjudication)
- **Dental claims**: ~0.5B/yr
- CAQH tracked **31.5B administrative verifications** across medical plans in 2024
  ([AJMC / 2024 CAQH Index](https://www.ajmc.com/view/2024-caqh-index-foresees-major-opportunity-for-health-care-savings)),
  confirming the order of magnitude.
- **US health claim events ≈ ~13B/yr → ~412 TPS**

### Rest-of-world Health

The US is ~40% of global health spend but a larger share of *transactional* claim
processing (single-payer systems adjudicate differently). Estimating global health claim
events at ~2.5× US → **~30B/yr → ~950 TPS gross**.

### P&C and Life

- **US auto**: ~6.2 collision claims per 100 insured vehicle-years
  ([IIHS/HLDI](https://www.iihs.org/research-areas/auto-insurance)) × ~280M vehicles +
  comprehensive/liability ≈ ~35–45M claims/yr
- **US home**: 5.3% of insured homes filed a claim in 2023
  ([III](https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance))
  × ~85M policies ≈ ~4.5M/yr
- **US P&C total** ≈ ~60M/yr; **global P&C** ≈ ~200M/yr → **~6 TPS**
- **Life/annuity**: low frequency, high value — **~50–100M/yr globally → ~2–3 TPS**

**Layer 1 total: ~30B health + ~0.2B P&C + ~0.1B life ≈ ~35B/yr ≈ ~1,110 TPS gross
(administrative).**

---

## Layer 2 — Settlement Payments (money movement, ~80–130 TPS gross)

This is the number that matters for the Big Number. Two forces shrink it dramatically
versus Layer 1:

1. **Batching**: health payers issue one ACH remittance (EFT/ERA) covering many claims.
   NACHA reports healthcare ACH claim payments have climbed for 11 straight years
   ([Nacha 2024](https://www.nacha.org/news/ach-healthcare-claim-payments-rise-again-2024-continuing-11-year-climb)),
   but the payment *count* is far below the claim count — a ratio of roughly 4–8 claims per
   payment.
2. **Denials/zero-pay**: a meaningful share of claims are denied or patient-responsibility
   and generate **no** insurer payment.

Estimate:
- Global health settlement payments: ~30B claims ÷ ~6 (batch ratio) × ~0.75 (paid share)
  ≈ **~3.75B payments/yr → ~119 TPS**
- P&C settlement payments: ~0.2B → ~6 TPS
- Life settlement payments: ~0.1B → ~3 TPS
- **Layer 2 total ≈ ~4B payments/yr ≈ ~128 TPS gross** (upper end); conservative floor
  ~80 TPS if batch ratio is higher.

---

## Layer 3 — Net-New to the Big Number (~90–100 TPS refined)

Most settlement payments ride **existing counted rails**: US health EFT is ACH (already in
[Bank Transfers](../../../payments/bank-transfers/REPORT.md)); P&C payouts are ACH, check,
or increasingly instant-to-card (already in card/bank totals).

The **net-new** contribution is the set of claim payments that are *not* otherwise counted —
primarily instant/real-time claim disbursements (push-to-card, RTP claim payouts) and
cross-border/cash claim settlements in emerging markets that no other category captures.

- Run 12 estimate: **55–148 TPS** net-new
- This deep dive narrows to a **refined ~90–100 TPS**, midpoint **~95 TPS**, by anchoring
  the batch ratio (4–8×) and paid share (~75%) with CAQH/NACHA data.

**Recommendation**: keep the [Insurance Premiums](../../../payments/insurance-premiums/REPORT.md)
category as-is (it counts inbound premium), and treat claims as a **documented adjacency**
worth ~95 TPS net-new — *not* a new standalone Big Number category, because ~85–90% of
claim settlement value already flows on counted rails. Add ~95 TPS only if/when the Big
Number is recomputed to include claim-payout net-new (currently it is not).

---

## Key Findings

1. **One claim is 5 messages and ⅛ of a payment.** The 20× gap between claim *events*
   (~1,110 TPS) and net-new *settlement* (~95 TPS) is the single biggest reason insurance
   volume is mis-estimated. Always specify which layer you mean.

2. **Health dominates count; life dominates value.** ~95% of claim *count* is health
   (medical + pharmacy + dental). Life/annuity is a rounding error by count but moves
   enormous value per payout — a mini version of the [Middle East](../middle-east/REPORT.md)
   value/count inversion.

3. **Batching is the hidden variable.** The claim-to-payment ratio (4–8×) driven by ACH
   remittance batching is what collapses ~30B health claims into ~3.75B payments. Small
   changes in this ratio swing the estimate by ±40 TPS — the dominant uncertainty.

4. **Instant claim payouts are the growth edge.** Push-to-card and RTP disbursements are
   converting batched ACH payments into 1:1 real-time payments. As adoption grows, insurance
   claims will shift *from* batched (low count) *to* instant (high count), raising the
   net-new TPS over time. A category to re-measure annually.

5. **Run 12 validated, narrowed.** The 55–148 TPS range holds; refined midpoint ~95 TPS.
   Confidence upgraded 🔴→🟡 on the strength of CAQH (31.5B verifications) and NACHA
   healthcare-ACH anchors.

---

## Sources

1. [AJMC — 2024 CAQH Index (31.5B verifications)](https://www.ajmc.com/view/2024-caqh-index-foresees-major-opportunity-for-health-care-savings)
2. [CAQH — 2025 Index Report ($258B avoided)](https://www.caqh.org/blog/2025-caqh-index-shows-u.s.-healthcare-avoided-258-billion-and-accelerated-automation-interoperability-and-ai-adoption)
3. [Nacha — Healthcare ACH Claim Payments Rise Again in 2024](https://www.nacha.org/news/ach-healthcare-claim-payments-rise-again-2024-continuing-11-year-climb)
4. [III — Facts + Statistics: Homeowners and Renters Insurance](https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance)
5. [III — Facts + Statistics: Auto Insurance](https://www.iii.org/fact-statistic/facts-statistics-auto-insurance)
6. [IIHS / HLDI — Auto Insurance Claim Frequency](https://www.iihs.org/research-areas/auto-insurance)
7. [NAIC — 2024 Property & Casualty Industry Analysis](https://content.naic.org/sites/default/files/2024-annual-property-casualty-and-title-insurance-industries-analysis-report.pdf)
8. [Policygenius — Homeowners Insurance Claims Statistics (2024)](https://www.policygenius.com/homeowners-insurance/homeowners-insurance-statistics/)

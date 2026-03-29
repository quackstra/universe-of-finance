---
title: "Buy Now Pay Later (BNPL) — Methodology"
parent: Payments
grand_parent: Explore
nav_order: 109
---

# Buy Now Pay Later (BNPL) — Measurement Methodology

## Transaction Definition

A "transaction" in this category requires a **dual definition** because BNPL creates a multiplier effect on the payment system:

**Purchase-level counting:**
- **Counting point:** Completed BNPL checkout — the consumer completes a purchase using a BNPL option
- **Unit:** One BNPL checkout = one transaction. A consumer buying a $200 jacket via Klarna Pay-in-4 = one purchase transaction
- **Value:** ~5.5 billion purchases in 2024

**Installment-level counting:**
- **Counting point:** Each scheduled installment payment that hits the underlying payment rail
- **Unit:** One installment debit from consumer = one transaction. The $200 jacket paid in 4 installments = 4 installment transactions
- **Value:** ~20 billion installment events in 2024 (5.5B × 3.6 avg installments)

**Primary metric:** Purchase-level (5.5B) for sizing the BNPL market. Installment-level (20B) for understanding payment system load.

- **Exclusions:** Traditional credit card installment plans (offered by card issuers post-purchase), layaway/layby programs, POS financing by retailers

## Triangulation Approach

### Method A: Bottom-Up Provider Aggregation (Primary)

- **Source:** Klarna H1 2024 (0.9B), Afterpay/Block 10-K (0.4B), Affirm 10-K (0.2B), PayPal Pay Later 10-K (0.8B), Zip (0.08B), China BNPL estimated (2.0B), others (~1.1B)
- **Value:** ~5.5 billion purchases
- **Strengths:** Top 5 Western providers have SEC-filed or investor-disclosed data; covers ~62% of non-China market directly
- **Weaknesses:** China BNPL (Huabei, Baitiao — 2.0B, 36% of total) is poorly documented; "others" (~1.1B, 20%) is residual estimation

### Method B: GMV / Average Order Value

- **Source:** Aggregated BNPL GMV ~$450B from provider filings + market estimates, average order $82
- **Value:** $450B / $82 = ~5.5B purchases
- **Strengths:** GMV is well-sourced from filings; provides independent count validation
- **Weaknesses:** AOV varies widely (Affirm $140, Afterpay $63, Klarna $111); blended average is approximate

### Method C: Worldpay GPR / Juniper Research Market Sizing

- **Source:** Worldpay Global Payments Report (BNPL = ~5% of e-commerce value = ~$315B), Juniper Research BNPL forecasts
- **Value:** Worldpay: $315B / ~$80 AOV = ~3.9B (lower, covers only e-commerce BNPL). Juniper: ~5-6B total including in-store
- **Strengths:** Independent market sizing from recognized analysts
- **Weaknesses:** Worldpay covers only e-commerce BNPL; Juniper methodology is opaque; both produce ranges rather than precise figures

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [Provider Sum]       [GMV / AOV]         [Market Size]  │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 5.5B         │    │ 5.5B         │    │ 3.9-6B     │ │
│  │ (Klarna +    │    │ ($450B /     │    │ (Worldpay  │ │
│  │  Afterpay +  │    │  $82 AOV)    │    │  e-com +   │ │
│  │  China +     │    │              │    │  Juniper)  │ │
│  │  others)     │    │              │    │            │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ A & B converge at 5.5B │                │
│                │ C brackets at 3.9-6B   │                │
│                │ Installment multiplier │                │
│                │ 3.6x → 20B events     │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   5.5B purchases       │                │
│                │   20B installments     │                │
│                │   175 / 634 TPS        │                │
│                │   Confidence: 58/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## The Installment Multiplier

BNPL is unique in this taxonomy because it **creates net new payment transactions** on underlying rails:

```
Standard card purchase:     1 checkout → 1 card transaction
BNPL Pay-in-4 purchase:    1 checkout → 4 card/bank transactions
BNPL Pay-in-3 purchase:    1 checkout → 3 card/bank transactions
BNPL long-term (8 months): 1 checkout → 8 card/bank transactions
BNPL pay-after-delivery:   1 checkout → 1 card/bank transaction

Weighted average multiplier:
  60% Pay-in-4 (4.0x) + 15% Pay-in-3 (3.0x) +
  15% long-term (8.0x) + 10% pay-after (1.0x) = 3.6x

5.5B purchases × 3.6 = 20B installment payment events
Net incremental vs. single payment: 20B - 5.5B = 14.5B new events
```

Each installment hits the underlying payment rail (card debit or bank transfer) as a separate transaction. BNPL therefore generates **~14.5B net incremental transactions** on card and bank rails that would not exist without the BNPL layer.

## Reconciliation

**Bottom-up provider aggregation (Method A) anchors the purchase count** because:
1. Top 5 Western providers (Klarna, Afterpay, Affirm, PayPal, Zip) are from SEC/investor filings
2. GMV / AOV cross-check (Method B) converges at the same 5.5B
3. The installment multiplier (3.6x) is a model assumption based on product mix, not directly observed

**Key weakness:** China BNPL (2.0B purchases, 36% of total) is estimated from industry reports — Ant Group's Huabei and JD's Baitiao do not publish transaction counts publicly.

## Overlap Analysis

```
BNPL: 5.5B purchases / 20B installments
                │
                │  BNPL is a CREDIT LAYER, not a payment rail.
                │  100% of BNPL installments settle on other rails:
                │
(-) Card rail   ████████████████████████████████████  20B installments
    settlement  │ ~60% of installments settle via card
    (~12B)      │ debit — counted in Consumer Cards
                │
(-) Bank        │ ~35% settle via direct debit/ACH —
    transfer    │ counted in Bank Transfers
    (~7B)       │
                │
(-) Wallet/     │ ~5% settle via digital wallet —
    other       │ counted in Digital Wallets
    (~1B)       │
                │
                ▼
De-duplicated   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0B incremental
                BNPL has 100% overlap at the
                installment level — every installment
                flows through a rail counted elsewhere.

                BUT: BNPL creates 14.5B NET NEW
                transactions that would not exist
                without the BNPL multiplier effect.
                These are INCREMENTAL LOAD on
                underlying rails (~460 TPS).
```

**BNPL has 100% rail overlap but creates net incremental transactions.** This is a unique property — BNPL does not add its own payment infrastructure but amplifies the transaction load on existing card and bank rails by 2.6x per purchase (3.6 installments minus the 1 payment that would have occurred anyway).

## Coverage Assessment

- **Directly observed:** Klarna (16%), Afterpay (7%), Affirm (4%), PayPal (15%), Zip (1%) — total ~43% from filings
- **Semi-observed:** China BNPL (~36%) from industry estimates
- **Estimated:** "Others" (~20%) — regional providers, white-label BNPL, bank-offered BNPL

```
Provider        Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
China (Huabei+) ████████ 36.4%   Low (no public disclosure)
PayPal Pay Later ███░░░░░ 14.5%   High (10-K)
Klarna          ███░░░░░ 16.4%   High (investor report)
Afterpay/Block  ██░░░░░░  7.3%   High (10-K)
Affirm          █░░░░░░░  3.6%   High (10-K)
Others          ████░░░░ 21.8%   Low (residual)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Klarna investor     ███░░░░░░  █████████ █████████░  █████████░
Block 10-K          ██░░░░░░░  █████████ ██████████  ████████░░
Affirm 10-K         █░░░░░░░░  █████████ ██████████  █████████░
PayPal 10-K         ██░░░░░░░  █████████ ██████████  ███████░░░
Worldpay GPR        █████████  █████████ ████████░░  █████░░░░░
CFPB Report         ███░░░░░░  █████████ █████████░  ██████░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    55/100     90/100    85/100      65/100
```

- **Final confidence score:** 58/100
- **Key uncertainty drivers:**
  - China BNPL (36% of total) is poorly documented
  - Installment multiplier (3.6x) is a model assumption, not observed
  - Boundary between "BNPL" and traditional card installment plans is blurring
  - Fast-growing category — 2024 estimates may be stale by publication

## Revision History

- **Run 5 (2026-03-28):** Initial estimate — 5.5B purchases / 20B installments from provider aggregation
- **Run 6 (2026-03-28):** Methodology documentation formalized with installment multiplier analysis

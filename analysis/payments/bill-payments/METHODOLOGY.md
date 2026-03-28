# Bill Payments — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed recurring bill payment from a consumer to a service provider**. Specifically:

- **Counting point:** Completed payment — the bill amount is successfully debited from the consumer's account/card and credited to the biller
- **Unit:** One bill payment = one transaction. A consumer paying their monthly electricity bill = one transaction
- **Scope:** Utility bills (electricity, gas, water, waste), telecom bills (mobile, broadband, cable TV), digital subscription payments (Netflix, Spotify, etc.), rent payments
- **Exclusions:** Insurance premium payments (separate capsule), loan/mortgage payments, one-time purchases, tax payments, government fees

## Triangulation Approach

### Method A: Bottom-Up Segment Model (Primary)

- **Source:** IEA (electricity accounts), GSMA (mobile subscriptions), ITU (broadband), Netflix/Spotify/Disney+ subscriber counts, Census Bureau/Eurostat (renter households)
- **Value:** ~95 billion transactions from segment sum:
  - Utilities (electricity 22B + gas 7B + water 10B + waste/other 4B) = 43B
  - Telecoms (mobile 18B + broadband 12B + cable TV 5B) = 35B
  - Digital subscriptions = 10B
  - Rent = 7B
- **Strengths:** Each segment is anchored to observable account/subscriber counts; payment frequency is predictable (monthly for most bills)
- **Weaknesses:** No single source publishes global bill payment totals; account counts and payment frequencies are estimated for many markets; cash bill payments in developing markets are hard to track

### Method B: National Payment System Data Extrapolation

- **Source:** Nacha ACH (US direct debit volumes), BACS (UK direct debit 4.7B), ECB (SEPA Direct Debit 24B), NPCI BBPS (India bill payments)
- **Value:** US direct debit bill payments ~12B, EU ~28B, UK ~5B, India (BBPS) ~3B = ~48B in tracked markets → extrapolated to ~85-100B globally
- **Strengths:** Payment system data is high quality for developed markets; BACS and SEPA are directly observed
- **Weaknesses:** "Bill payment" is not a separately tagged category in most payment systems — must estimate share of ACH/DD that is bill-related; global extrapolation from 4 markets is crude

### Method C: Household × Bills-Per-Month

- **Source:** ~2B households globally with formal utility connections × ~4 bills/month average = ~96B
- **Value:** ~96B transactions
- **Strengths:** Simple, independent sanity check; uses population-level data
- **Weaknesses:** Extremely rough — "4 bills/month" is a blended average across very different household profiles; ignores prepaid mobile top-ups and digital subscriptions (or double-counts them)

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [Segment Model]      [Payment System]    [Household ×]  │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 95B          │    │ 85-100B      │    │ ~96B       │ │
│  │ (utilities + │    │ (NACHA+BACS+ │    │ (2B HH ×   │ │
│  │  telecoms +  │    │  SEPA+BBPS   │    │  4 bills/  │ │
│  │  digital +   │    │  extrapolated│    │  month)    │ │
│  │  rent)       │    │  globally)   │    │            │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ All three methods      │                │
│                │ cluster around 85-100B │                │
│                │ Central estimate: 95B  │                │
│                │ Range: 80-110B         │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   95B transactions     │                │
│                │   3,012 TPS            │                │
│                │   Confidence: 48/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**Bottom-up segment model (Method A) anchors the final estimate** because:
1. It provides the most granular decomposition — each segment can be independently challenged
2. Payment system extrapolation (Method B) produces a consistent range (85-100B)
3. Household-level sanity check (Method C) converges at ~96B

**Key uncertainty:** The range is 80-110B. The low end assumes fewer prepaid mobile top-ups; the high end assumes higher digital subscription penetration and more frequent utility billing in emerging markets. The 95B central estimate sits at the convergence of all three methods.

## Overlap Analysis

```
Bill Payments: 95B total
                │
(-) Direct      │
    debit/ACH   ████████████████████████████████████  95B
    overlap     │ ~50B flow through ACH/BACS/SEPA
    (~50B)      │ direct debit — ALSO counted in
                │ Bank Transfers. Deducted HERE.
                │
(-) Card-on-    │ ~25B paid via card-on-file or
    file        │ auto-pay on credit/debit cards —
    overlap     │ ALSO counted in Consumer Cards.
    (~25B)      │ Deducted HERE.
                │
(-) Wallet/     │ ~10.5B paid via mobile money or
    mobile      │ digital wallets — ALSO counted in
    overlap     │ Digital Wallets. Deducted HERE.
    (~10.5B)    │
                │
(-) Cash/check  │ ~9.5B paid in cash or check at
    (no overlap)│ payment counters — NOT counted
                │ elsewhere. Incremental.
                │
                ▼
De-duplicated   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ~9.5B
                ~90% of bill payments flow through
                rails counted in base-layer capsules.
                Only cash/check payments (~10%) are
                truly incremental.
```

**Bill Payments is a commerce layer with ~90% overlap.** The vast majority of bill payments settle on bank transfer, card, or wallet rails already counted elsewhere. Only ~9.5B cash/check payments (10%) are incremental to payment system TPS.

## Coverage Assessment

- **Directly observed:** BACS UK DD (5B), SEPA DD (24B), Nacha ACH (portion), NPCI BBPS (3B) — ~35% from payment system data
- **Modeled:** Segment-level account counts and payment frequencies — ~65% of estimate
- **Unobserved:** Cash bill payments in developing markets (significant but unknown share)

```
Segment         Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
Utilities       ████████ 45.3%   Medium (IEA accounts)
Telecoms        ██████░░ 36.8%   Medium (GSMA/ITU subs)
Digital Subs    ██░░░░░░ 10.5%   Medium (platform disclosures)
Rent            █░░░░░░░  7.4%   Low (census/estimate)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Nacha (US ACH)      ███░░░░░░  █████████ ██████████  ██████░░░░
BACS (UK DD)        ██░░░░░░░  █████████ █████████░  ████████░░
ECB (SEPA DD)       ███░░░░░░  █████████ ██████████  ███████░░░
GSMA (mobile)       █████████  █████████ ████████░░  █████░░░░░
IEA (electricity)   ████████░  ████████░ ████████░░  █████░░░░░
Netflix/Spotify     ██░░░░░░░  █████████ █████████░  ████████░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    60/100     88/100    82/100      55/100
```

- **Final confidence score:** 48/100
- **Key uncertainty drivers:**
  - No single source publishes global bill payment transaction counts
  - Segment model relies on account count × frequency assumptions
  - Cash bill payments in developing markets are untracked
  - Prepaid mobile top-up frequency is highly variable

## Revision History

- **Run 5 (2026-03-28):** Initial estimate — 95B from segment model, payment system cross-check
- **Run 6 (2026-03-28):** Methodology documentation formalized

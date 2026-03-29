---
title: "Bank Transfers — Methodology"
parent: Payments
grand_parent: Explore
nav_order: 103
---

# Bank Transfers (ACH/RTGS) — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed credit transfer or direct debit instruction processed through a bank-to-bank payment system**. Specifically:

- **Counting point:** Settlement/completion — the instruction successfully debits the payer's bank and credits the payee's bank. For RTP systems, this is near-instantaneous; for batch ACH, it occurs at the end of the clearing cycle; for RTGS, at gross settlement
- **Unit:** One payment instruction = one transaction. A batch file containing 1,000 payroll credits = 1,000 transactions (gross counting, not net)
- **Inclusions:** Real-time payments (UPI, PIX, Faster Payments, FedNow, SEPA Instant), batch transfers (ACH, BACS, SEPA Credit Transfers, SEPA Direct Debits), RTGS/wire transfers (Fedwire, TARGET2, CHAPS, CIPS)
- **Exclusions:** Card-initiated transactions (separate capsule), digital wallet payments that do not use bank rails, cash transactions, check payments

## Triangulation Approach

### Method A: ACI Worldwide Real-Time Payments Report + System-Level Data (Primary)

- **Source:** ACI Worldwide Prime Time for Real-Time report (RTP: 378B), Nacha (US ACH: 33.6B), ECB (SEPA: 51B), UK BACS (7.5B), other systems (~14B batch + 0.4B RTGS)
- **Value:** ~484 billion transactions (378B RTP + 106B batch/ACH + 0.4B RTGS)
- **Strengths:** ACI report is the recognized benchmark for global RTP volumes; ACH/BACS/SEPA data comes from system operators; Fedwire/TARGET2 from central banks
- **Weaknesses:** ACI's 2024 RTP figure is extrapolated from 2023 (266.2B at 42.2% growth); some smaller RTP systems are estimated

### Method B: Central Bank Statistics Aggregation (Cross-Check)

- **Source:** BIS CPMI Red Book statistics, ECB payment statistics, RBI data, BCB (Brazil) data, individual central bank reports
- **Value:** ~460-500B range (depending on coverage of smaller markets)
- **Strengths:** Central bank data is the most authoritative source for domestic payment system volumes; BIS CPMI methodology is internationally standardized
- **Weaknesses:** BIS covers ~25 major economies — smaller markets are estimated; data publication lag (Red Book typically 12-18 months behind); definition alignment varies across jurisdictions

### Method C: SWIFT Traffic + Domestic System Sum (Wire/RTGS Cross-Check)

- **Source:** SWIFT FIN traffic statistics (cross-border), Fedwire/TARGET2/CHAPS/CIPS annual reports
- **Value:** RTGS segment specifically: ~400M transactions, ~$2,460T value
- **Strengths:** SWIFT publishes monthly traffic data; Fedwire and TARGET2 publish daily/annual statistics with high granularity
- **Weaknesses:** Only validates the RTGS/wire segment (<0.1% of volume); cross-border messaging volume is not the same as transaction count

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [ACI + Systems]      [Central Banks]     [SWIFT/RTGS]   │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 484B         │    │ 460-500B     │    │ 0.4B RTGS  │ │
│  │ (RTP+ACH+    │    │ (BIS CPMI    │    │ ($2,460T   │ │
│  │  RTGS)       │    │  coverage)   │    │  value)    │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ A vs B: A within B's   │                │
│                │ range (460-500B)       │                │
│                │ C validates RTGS       │                │
│                │ segment precisely      │                │
│                │ Gap: coverage of       │                │
│                │ smaller RTP systems    │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   484B transactions    │                │
│                │   15,338 TPS           │                │
│                │   Confidence: 78/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**ACI + system-level data (Method A) anchors the final estimate** because:
1. The RTP segment (378B, 78% of total) uses ACI's recognized benchmark, cross-checked against NPCI (UPI 172B) and BCB (PIX 66B) — the two largest systems are directly observed
2. Batch/ACH (106B, 22%) uses operator-reported data from Nacha, ECB, and UK BACS
3. RTGS (0.4B, <0.1%) uses central bank annual reports with high precision

Central bank aggregation (Method B) produces a range of 460-500B that brackets Method A's 484B. The gap reflects coverage differences — BIS CPMI covers 25 major economies but misses smaller RTP systems in Southeast Asia, Africa, and Latin America that ACI captures.

**Composition of 484B:**
- Real-time payments: 378B (78.1%) — dominated by UPI 172B + PIX 66B
- Batch/ACH: 106B (21.9%) — US ACH 33.6B + SEPA 51B + BACS 7.5B + others 13.9B
- RTGS/Wire: 0.4B (0.08%) — Fedwire 210M + TARGET2 108M + CHAPS 53M + CIPS 8M + others 21M

## Overlap Analysis

```
Bank Transfers: 484B total
                │
(-) UPI overlap ████████████████████████████████████  484B
    with Digital│ UPI 172B is ALSO counted in Digital
    Wallets     │ Wallets (wallet apps like PhonePe,
                │ Google Pay are the front-end).
                │ Kept HERE as base layer.
                │
(-) Payroll     │ ~37B payroll txns flow through
    subset      │ ACH/BACS/SEPA — already in the
                │ 106B batch total.
                │ Kept HERE as base layer.
                │
(-) Bill payment│ ~85B bill payments flow through
    subset      │ direct debit/ACH — already in the
                │ batch total.
                │ Kept HERE as base layer.
                │
                ▼
De-duplicated   ████████████████████████████████████  484B
                Bank Transfers is a BASE LAYER —
                no deductions needed. Other capsules
                subtract their bank-rail overlap.
```

**Bank Transfers is treated as a base layer** in the overlap framework, alongside Consumer Cards. Payroll (~37B), bill payments (~85B), and digital wallet UPI payments (~172B) all flow through bank transfer rails but are counted here first. Other capsules subtract their bank-rail portion.

## Coverage Assessment

- **Directly observed:** UPI (172B, 36%), PIX (66B, 14%), US ACH (33.6B, 7%), SEPA (51B, 11%), UK systems (13B, 3%) — total ~69% directly observed from operator/central bank data
- **Semi-observed:** Other RTP systems (~60B, 12%) from ACI aggregation — system-level but not all individually verified
- **Estimated:** Remaining batch/ACH in non-CPMI countries (~19%, residual)

```
Region          Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
India (UPI)     ████████ 35.6%   High (NPCI monthly)
Brazil (PIX)    ████░░░░ 13.6%   High (BCB data)
EU (SEPA+T2)    ████░░░░ 11.8%   High (ECB statistics)
US (ACH+Fedwire)███░░░░░  7.0%   High (Nacha/Fed data)
Thailand        ██░░░░░░  5.0%   Medium (PromptPay)
China           ██░░░░░░  4.1%   Low (IBPS opaque)
UK              █░░░░░░░  2.6%   High (BACS/FPS data)
Rest of World   ████░░░░ 20.3%   Low-Medium (mixed)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
ACI Worldwide RTP   █████████  █████████ ████████░░  ██████░░░░
NPCI (UPI)          ████░░░░░  █████████ ██████████  ██████████
Nacha (US ACH)      ███░░░░░░  █████████ ██████████  ██████████
ECB (SEPA)          ████░░░░░  █████████ ██████████  █████████░
BIS Red Book        ████████░  ██████░░░ ██████████  ██████░░░░
Fedwire/TARGET2     ██░░░░░░░  █████████ ██████████  ██████████
                    ─────────  ────────  ──────────  ───────────
Composite Score:    80/100     90/100    90/100      72/100
```

- **Final confidence score:** 78/100
- **Key uncertainty drivers:**
  - ACI 2024 RTP extrapolation (42.2% growth applied to 2023 base — actual growth rate may differ)
  - China IBPS volume (~20B, opaque domestic system)
  - "Other" batch/ACH systems in non-CPMI countries (~14B, weakly sourced)
  - UPI boundary: some UPI transactions are P2P, not merchant payments — classification is blurred

## Revision History

- **Run 1 (2026-03-26):** Initial estimate — 484B from ACI + system-level data
- **Run 2 (2026-03-26):** Added regional breakdown, RTP/ACH/RTGS composition, historic timeseries
- **Run 6 (2026-03-28):** Methodology documentation formalized

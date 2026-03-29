---
title: "Remittances — Methodology"
parent: Payments
grand_parent: Explore
nav_order: 106
---

# Remittances — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed cross-border person-to-person money transfer** where the sender and recipient are in different countries. Specifically:

- **Counting point:** Completed remittance — funds successfully disbursed to the recipient in the destination country
- **Unit:** One remittance transfer = one transaction. A migrant worker sending $300 home = one transaction, regardless of whether it passes through one or three intermediary systems
- **Scope:** Cross-border personal remittances via all channels (MTOs, banks, mobile money, digital platforms, hawala/informal)
- **Exclusions:** Domestic P2P transfers (separate capsule), corporate/business wire transfers, cross-border B2B payments, foreign aid/NGO disbursements

## Triangulation Approach

### Method A: Value / Average Remittance Size (Primary)

- **Source:** World Bank KNOMAD ($905B total remittance value 2024), World Bank Remittance Prices Worldwide (average transaction ~$200-500 range)
- **Value:** $905B / ~$500 avg remittance = ~1.8B transactions
- **Strengths:** World Bank is the authoritative source for remittance values; covers 200+ corridors; long timeseries
- **Weaknesses:** Transaction count is DERIVED, not directly observed — the $500 average is estimated; informal remittances (30-50% of total by some estimates) are partially captured in value but not in transaction count

### Method B: Bottom-Up Operator Sum (Cross-Check)

- **Source:** Western Union (~300M from Q4/FY2024 results), Wise (~125M est.), MoneyGram (~100M est.), banks (~400M est.), digital platforms (~200M est.), informal/other (~675M est.)
- **Value:** ~1.8B transactions
- **Strengths:** Western Union discloses transaction counts in earnings; Wise publishes customer transfer counts; provides bottom-up validation
- **Weaknesses:** Informal channel estimate (~675M, 38%) is highly uncertain; bank remittance transaction counts are not separately disclosed; long-tail operators are not tracked

### Method C: Corridor-Based Estimation

- **Source:** World Bank bilateral remittance matrix (top 20 corridors = ~45% of value), GPFI G20 Remittance Target data, FXC Intelligence corridor data
- **Value:** Top 20 corridors: ~800M transactions; extrapolated global: ~1.6-2.0B
- **Strengths:** Corridor-level data allows cross-validation of aggregate; top corridors (US-Mexico, UAE-India, US-India) are well-documented
- **Weaknesses:** Extrapolation from top 20 to global total requires coverage assumption; long-tail corridors are poorly documented

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [Value / Avg]        [Operator Sum]      [Corridor]     │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ ~1.8B        │    │ ~1.8B        │    │ 1.6-2.0B   │ │
│  │ ($905B /     │    │ (WU 300M +   │    │ (top 20    │ │
│  │  $500 avg)   │    │  Wise 125M + │    │  corridors │ │
│  │              │    │  others)     │    │  + extrap) │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ A & B converge at 1.8B │                │
│                │ C brackets at 1.6-2.0B │                │
│                │ KEY ISSUE: avg remit   │                │
│                │ size ($500) is assumed │                │
│                │ — if $350, count = 2.6B│                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   1.8B transactions    │                │
│                │   57 TPS               │                │
│                │   Confidence: 58/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**Value / average remittance size (Method A) is used as anchor** because:
1. World Bank remittance value ($905B) is the most authoritative figure in this category
2. The operator sum (Method B) independently produces ~1.8B
3. Corridor estimation (Method C) brackets the figure at 1.6-2.0B

**Critical caveat:** The transaction COUNT is the weakest figure in this capsule. No single authority publishes global remittance transaction counts. The value ($905B) has high confidence; the count (1.8B) is derived and carries ±30% uncertainty. If the average remittance is $350 (more small-value digital transfers), the count could be 2.6B. If $600 (more bank-channel transfers), it could be 1.5B.

## Overlap Analysis

```
Remittances: 1.8B total
                │
(-) Bank        │
    transfer    ████████████████████████████████████  1.8B
    overlap     │ ~400M bank-channel remittances are
                │ technically bank transfers — but
                │ cross-border routing distinguishes
                │ them. Minimal overlap with domestic
                │ bank transfer capsule.
                │
(-) Digital     │ ~200M digital remittances (Wise,
    wallet/P2P  │ Remitly, WorldRemit) may touch
    overlap     │ wallet or P2P rails at disbursement.
                │ Small overlap.
                │
                ▼
De-duplicated   ██████████████████████████████████░░  ~1.6B
                Remittances are mostly incremental —
                cross-border routing is distinct from
                domestic payment rails. ~200M overlap
                with bank transfers at disbursement.
```

## Coverage Assessment

- **Directly observed:** Western Union (~17%), Wise (~7%) — from earnings disclosures
- **Semi-observed:** World Bank value data ($905B) is comprehensive but count is derived
- **Estimated:** Informal channels (30-50% of total value) are substantially unobserved

```
Region (receiving) Volume   Share   Data Quality
─────────────────  ──────── ─────── ───────────
South Asia         ████████ 28.0%   Medium (World Bank corridors)
East Asia/Pacific  ██████░░ 20.0%   Low (informal channels)
Sub-Saharan Africa ████░░░░ 14.0%   Low (hawala, mobile money)
Latin America      ████░░░░ 13.0%   Medium (US-Mexico well-tracked)
Europe/Central A.  ███░░░░░ 12.0%   Medium (EU regulation)
MENA               ██░░░░░░  8.0%   Low (hawala prevalence)
Other              █░░░░░░░  5.0%   Low
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
World Bank KNOMAD   █████████  ████████░ ██████████  ██████░░░░
World Bank RPW      ███████░░  ████████░ ██████████  ████████░░
Western Union 10-K  ███░░░░░░  █████████ ██████████  ████████░░
FXC Intelligence    ██████░░░  █████████ ███████░░░  ██████░░░░
GPFI G20 Report     ████████░  ███████░░ █████████░  █████░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    68/100     82/100    85/100      55/100
```

- **Final confidence score:** 58/100
- **Key uncertainty drivers:**
  - Transaction count is derived, not directly observed (weakest figure in capsule)
  - Average remittance size ($500 assumed) — ±30% uncertainty
  - Informal channels (30-50% of value) largely invisible to measurement
  - Small-value digital remittances growing rapidly — may change the AOV and count materially

## Revision History

- **Run 1 (2026-03-26):** Initial estimate — 1.8B from World Bank value / avg transfer size
- **Run 2 (2026-03-26):** Added operator sum cross-check, corridor estimation
- **Run 6 (2026-03-28):** Methodology documentation formalized

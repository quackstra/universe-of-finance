# Sector Methodology: Government & Public Sector

> How we measure tax receipts, benefits disbursements, and public sector payments — 1 category, ~1,002 TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

The Government sector measures **public sector financial transactions** — tax payments from citizens/businesses to government, and benefits/pension/procurement disbursements from government to citizens/businesses. At ~1,002 TPS (~31.6B annual transactions), Government accounts for **1.4% of global financial TPS**.

This sector was significantly revised in Run 3 using a bottom-up model across the US, India, EU, and tiered rest-of-world extrapolation. The revision increased the estimate from ~25B to ~31.6B annual transactions, driven primarily by India's JAM-enabled Direct Benefit Transfer (DBT) platform, which alone accounts for 7.4B transactions across 1,206+ welfare schemes.

---

## 2. Sector-Specific Measurement Challenges

**Fragmented reporting.** Unlike card networks or exchanges, there is no single global authority that aggregates government payment counts. Each country reports through its own tax authority, social security agency, and procurement body — if it reports at all.

**Definition ambiguity.** A "government payment" can mean many things: a tax filing (not a payment), a tax remittance (a payment), a benefits check (a payment), a government employee salary (also in Payroll), a procurement invoice (a payment). Boundary definition is critical.

**India's outsized contribution.** India's DBT platform (7.4B transactions) accounts for 23% of the global government payment estimate. If the DBT figure is wrong by 20%, the global estimate shifts by ~5%. This single-country concentration creates fragility.

**Payment rail overlap.** Government payments flow through existing payment infrastructure — ACH for tax refunds, bank transfers for benefits, cards for procurement. An estimated 60% of government payment transactions are already counted in the Payments sector (primarily in Bank Transfers).

**Cash disbursements in developing countries.** Some government benefits in Sub-Saharan Africa and South Asia are still disbursed in cash. These are real government transactions but are invisible to electronic counting.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume (B) | Confidence | Notes |
|---|----------|---------|-------------------|------------|-------|
| 1 | Tax & Government Payments | 1,002 | 31.6 | 50 (Medium) | Bottom-up model |

**Sector total: ~1,002 TPS**

---

## 4. Cross-Category Overlap Rules

### Intra-Sector

Only one category — no intra-sector overlap.

### Cross-Sector Overlap (with Payments)

Government payments ride on payment rails that are already counted in the Payments sector:

```
┌─────────────────────────────────────────────────────────┐
│  GOVERNMENT SECTOR: 31.6B annual transactions            │
│                                                          │
│  ┌─────────────────────────────────────────────┐        │
│  │ Tax Receipts          Benefits Disbursements │        │
│  │ ~12B txns             ~15B txns              │        │
│  │                                               │        │
│  │ Procurement           Public Sector Payroll   │        │
│  │ ~3B txns              ~1.6B txns              │        │
│  └──────────────────────┬──────────────────────┘        │
│                          │                               │
│                          ▼                               │
│  ┌─────────────────────────────────────────────┐        │
│  │ Payment Rail Allocation:                     │        │
│  │                                               │        │
│  │ ACH/Bank Transfer:  60% (~19B) ← OVERLAP    │        │
│  │ Real-Time Payments: 15% (~4.7B) ← OVERLAP   │        │
│  │ Card Payments:       5% (~1.6B) ← OVERLAP   │        │
│  │ Check/Cash:         15% (~4.7B) ← NOT in    │        │
│  │                                    Payments   │        │
│  │ Direct (treasury):   5% (~1.6B) ← NOT in    │        │
│  │                                    Payments   │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
│  Overlap with Payments: ~80% (~25.3B)                    │
│  Incremental:           ~20% (~6.3B) = ~200 TPS         │
│                                                          │
│  Conservative estimate used in Big Number: ~401 TPS      │
│  (40% incremental — accounts for some double-counted     │
│   ACH items being govt-specific batch runs)              │
└─────────────────────────────────────────────────────────┘
```

**Decision:** Government is excluded from payment infrastructure TPS (~70,200) but partially included in economic transaction TPS (~71,200), with ~401 incremental TPS added (the ~40% that does not flow through tracked payment rails).

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
India DBT Portal    ███░░░░░░  █████████ █████████░  █████████░
US IRS/Treasury     ███░░░░░░  █████████ ██████████  ████████░░
EU Social Security  ████░░░░░  ███████░░ █████████░  █████░░░░░
(MISSOC database)
World Bank Gov't    ██████░░░  ██████░░░ ████████░░  ███░░░░░░░
Finance Stats
OECD Revenue Stats  █████░░░░  ███████░░ █████████░  ████░░░░░░
National budget     ██████░░░  ████████░ █████████░  ████░░░░░░
documents
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Country-specific):** India DBT Portal (7.4B transactions with scheme-level detail), US IRS/Treasury (tax payment and refund counts), EU MISSOC (social security cross-country)
**Tier 2 (Cross-country):** OECD Revenue Statistics (tax counts for 38 member countries), World Bank Government Finance Statistics
**Tier 3 (Estimation):** National budget documents, IMF fiscal monitor data, population-based scaling for non-reporting countries

---

## 6. Sector Triangulation Approach

### Government Sector Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [Top-Down]            [Bottom-Up]         [Per-Capita]  │
│  Global govt spend     Sum of US, India,   Population ×  │
│  × payment frequency   EU + tiered RoW     govt txns/    │
│  ratio                 extrapolation       capita ratio  │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ ~25B     │         │ ~31.6B   │        │ ~28B     │  │
│  │ annual   │         │ annual   │        │ annual   │  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ Top-down (A) under-   │                    │
│              │ counts because payment│                    │
│              │ frequency ratio based │                    │
│              │ on old data (pre-DBT  │                    │
│              │ India, pre-digital    │                    │
│              │ disbursement push).   │                    │
│              │ Per-capita (C) is     │                    │
│              │ middle ground.        │                    │
│              │ Bottom-up (B) is most │                    │
│              │ defensible.           │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ ~31.6B annual txns    │                    │
│              │ ~1,002 TPS            │                    │
│              │ Range: 800-1,300 TPS  │                    │
│              │ Confidence: 50/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

### Bottom-Up Model Detail

| Country/Region | Tax (B) | Benefits (B) | Other (B) | Total (B) |
|----------------|---------|-------------|-----------|-----------|
| US | 1.89 | 2.68 | 0.52 | 5.09 |
| India | 0.82 | 7.09 | 0.28 | 8.19 |
| EU | 2.27 | 2.94 | 0.63 | 5.84 |
| Rest of World (tiered) | ~4.5 | ~6.5 | ~1.5 | ~12.5 |
| **Total** | **~9.5** | **~19.2** | **~2.9** | **~31.6** |

---

## 7. Definition Standards

In the Government sector, a **transaction** is a single payment event between a government entity and a citizen, business, or other government entity.

| Transaction Type | Counting Point | What Is Excluded |
|-----------------|---------------|------------------|
| Tax payment | Completed payment to revenue authority | Tax filing (information event), assessment notices |
| Benefits disbursement | Individual payment to beneficiary | Eligibility determinations, application processing |
| Public procurement | Payment to vendor/contractor | Purchase orders, invoices, contract awards |
| Public sector payroll | Individual salary/wage deposit | Employment contracts, timesheets |

**Key distinction:** A government benefit disbursement that pays 1 million citizens via a single batch ACH file counts as **1 million transactions** (one per beneficiary), not 1 transaction (the batch file). We count at the beneficiary level, not the batch level.

---

## 8. Known Gaps & Future Work

- **Rest-of-World estimation.** The ~12.5B RoW figure is derived from tiered GDP/population scaling. Country-specific data for China (government payment counts are not publicly reported), Brazil, Indonesia, and Nigeria would significantly improve this.
- **China government payments.** China's government manages massive social security, pension, and subsidy programs for 1.4B people. The absence of detailed transaction data is the single largest gap in this sector.
- **Government-to-government transfers.** Intergovernmental transfers (federal to state, state to local, international aid) are partially captured but poorly documented at the transaction level.
- **Digital government push.** India's DBT, Brazil's Bolsa Familia via PIX, and EU digital identity initiatives are rapidly changing government payment patterns. Annual updates are needed to track this shift.
- **Procurement transaction counts.** Government procurement is estimated at ~$13T globally, but transaction counts (number of individual invoices and payments) are poorly documented outside the US.

---

*Government is a medium-confidence sector elevated by India's excellent DBT data. The methodology will improve as more countries digitize disbursements and publish transaction-level statistics.*

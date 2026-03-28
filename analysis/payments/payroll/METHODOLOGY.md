# Payroll Payments — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed wage/salary payment from an employer to an employee**. Specifically:

- **Counting point:** Completed payment — the wage amount is successfully credited to the employee's bank account or disbursed as cash/check
- **Unit:** One payroll credit = one transaction. An employer paying 500 employees = 500 transactions. Each pay period generates one transaction per employee
- **Scope:** Formal-sector wage and salary payments globally — all pay frequencies (weekly, biweekly, semi-monthly, monthly)
- **Exclusions:** Contractor/freelancer payments (1099-type), informal sector cash wages where no payment system is involved, pension/social security disbursements, employer tax remittances, benefits-in-kind

## Triangulation Approach

### Method A: Employment x Pay Frequency Model (Primary)

- **Source:** ILO World Employment and Social Outlook (3.5B employed globally), BLS (US pay frequency survey), Eurostat, regional labor statistics, ADP/CloudPay global payroll surveys
- **Value:** ~41.2 billion transactions from regional model:
  - North America: 165M employed × 24 pay periods/yr (biweekly) = 4.0B
  - EU/UK: 200M employed × 12.5 pay periods/yr (monthly, some fortnightly) = 2.5B
  - China: 770M employed × 12 pay periods/yr (monthly) × 65% formal = 6.0B
  - India: 530M employed × 12 pay periods/yr × 30% formal + daily wage adj = 3.8B
  - Japan/Korea/Aus: 110M employed × 12-24 pay periods/yr = 2.0B
  - Brazil: 100M employed × 12 pay periods/yr × 70% formal = 0.8B
  - Rest of world: ~22B (scaled by ILO employment × regional formal share × frequency)
- **Strengths:** ILO employment data is comprehensive; pay frequency norms are well-documented for major markets
- **Weaknesses:** No source publishes global payroll transaction counts; formal sector share in developing markets is estimated; pay frequency varies within countries

### Method B: ACH/BACS Payroll Share Extrapolation

- **Source:** Nacha (US ACH: 33.6B total, ~30% payroll-related = ~10B), BACS (UK: 7.5B total, ~35% payroll = ~2.6B), SEPA (EU: 51B, ~20% payroll = ~10.2B)
- **Value:** Developed markets: ~23B payroll via electronic systems → Global extrapolation: ~38-44B
- **Strengths:** Payment system data is high quality; payroll share of ACH/DD is estimable from published breakdowns
- **Weaknesses:** "Payroll share" of ACH is estimated, not directly tagged; global extrapolation from 3 markets is crude; developing markets use cash payroll extensively

### Method C: Global Wage Bill / Average Wage Payment

- **Source:** ILO Global Wage Report (~$32T total global wage bill 2024), estimated average wage payment ~$780
- **Value:** $32T / $780 = ~41B transactions
- **Strengths:** ILO wage data is authoritative; provides independent validation
- **Weaknesses:** Average wage payment is blended across vastly different economies (US ~$2,500/biweekly, India ~$200/monthly, informal ~$50/daily); highly sensitive to mix

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [Employ × Freq]      [ACH Payroll]       [Wage/$Avg]    │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 41.2B        │    │ 38-44B       │    │ ~41B       │ │
│  │ (ILO employ  │    │ (Nacha+BACS+ │    │ ($32T /    │ │
│  │  × pay freq  │    │  SEPA share  │    │  $780 avg) │ │
│  │  × formal %) │    │  extrapolated│    │            │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ All three methods      │                │
│                │ cluster around 38-44B  │                │
│                │ Central estimate: 41.2B│                │
│                │ Range: 35-48B          │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   41.2B transactions   │                │
│                │   1,305 TPS            │                │
│                │   Confidence: 35/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**Employment x pay frequency model (Method A) anchors the final estimate** because:
1. ILO employment data (3.5B) is the most comprehensive global labor dataset
2. Pay frequency norms are well-documented for major economies (US biweekly, EU/Asia monthly)
3. ACH extrapolation (Method B) brackets the estimate at 38-44B
4. Wage bill derivation (Method C) converges at ~41B

**Key caveat:** This is the lowest-confidence estimate in the payments sector (35/100). No single source counts payroll transactions. The entire estimate is modeled. The range (35-48B) reflects uncertainty in formal sector share, pay frequency, and developing market coverage.

## Overlap Analysis

```
Payroll: 41.2B total
                │
                │  Payroll is a SUBSET of bank transfers.
                │  ~90% of formal payroll settles via
                │  ACH/BACS/SEPA batch transfers:
                │
(-) Bank        ████████████████████████████████████  41.2B
    transfer    │ ~37B payroll credits flow through
    overlap     │ ACH/BACS/SEPA/domestic batch systems
    (~37B)      │ — ALREADY counted in Bank Transfers.
                │ Deducted HERE.
                │
(-) Cash wages  │ ~4.2B payroll disbursements in cash
    (no overlap)│ (developing markets, informal sector,
                │ daily wage laborers) — NOT counted
                │ in any other electronic payment capsule.
                │ Incremental.
                │
                ▼
De-duplicated   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ~4.2B
                Payroll is ~90% a subset of bank
                transfers. Only cash wages (~10%)
                are incremental to electronic
                payment system TPS.
```

**Payroll is a subset category** — not a separate payment rail. It identifies the PURPOSE of bank transfers. Approximately 37B of the 41.2B payroll transactions are already counted in the 484B bank transfer total. Only ~4.2B cash wage payments are incremental.

## Coverage Assessment

- **Directly observed:** None — no source directly publishes global payroll transaction counts
- **Modeled:** 100% of estimate is derived from employment × frequency × formality assumptions
- **Anchor points:** US pay frequency from BLS, EU employment from Eurostat, China/India from national statistics

```
Region          Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
China           ████████ 14.6%   Low (formal share estimated)
Rest of Asia    ██████░░ 19.4%   Low (informal sector large)
North America   ████░░░░  9.7%   Medium (BLS data)
India           ████░░░░  9.2%   Low (informal sector ~70%)
Europe/UK       ████░░░░  8.5%   Medium (Eurostat)
Rest of World   ██████████38.6%  Low (scaled estimates)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
ILO Employment      █████████  ████████░ ██████████  ██████░░░░
BLS (US payroll)    ███░░░░░░  █████████ ██████████  █████████░
Eurostat (EU)       ███░░░░░░  █████████ ██████████  ████████░░
ADP Payroll Survey  ████░░░░░  █████████ ███████░░░  ██████░░░░
Nacha ACH           ███░░░░░░  █████████ ██████████  █████░░░░░
ILO Wage Report     █████████  ████████░ ██████████  █████░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    55/100     85/100    85/100      48/100
```

- **Final confidence score:** 35/100
- **Key uncertainty drivers:**
  - No direct source for global payroll transaction counts (100% modeled)
  - Formal sector share varies 30-95% by country — small changes create large swings
  - ILO estimates 2B+ informal workers whose cash wages are invisible
  - Pay frequency assumptions (weekly vs. monthly) vary within countries
  - Lowest-confidence category in the payments sector

## Revision History

- **Run 5 (2026-03-28):** Initial estimate — 41.2B from employment × frequency model
- **Run 6 (2026-03-28):** Methodology documentation formalized

# ATM Withdrawals — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed cash withdrawal at an ATM**. Specifically:

- **Counting point:** Successful cash dispensation — the ATM releases cash to the cardholder. Failed/declined transactions are excluded
- **Unit:** One cash withdrawal = one transaction. A consumer withdrawing $200 from an ATM = one transaction, regardless of denomination breakdown
- **Scope:** All ATM cash withdrawals globally — bank-owned and independent deployer (IAD) ATMs, all card types (debit, credit, prepaid), on-us and off-us transactions
- **Exclusions:** Balance inquiries (~20% of ATM interactions), mini-statements, bill payments via ATM, deposits at ATMs, cardless ATM withdrawals (small but growing), cash advances at bank counters

## Triangulation Approach

### Method A: BIS/ECB/RBI Composite + ATMIA Adjustment (Primary)

- **Source:** BIS CPMI Red Book (25 major economies), ECB Payment Statistics H1+H2 2024 (EU-27: 7.5B), RBI Bankwise ATM Statistics (India: ~6B), Fed Payments Study 2021 (US: 3.7B, extrapolated to 2024: ~2.5B), ATMIA/Datos Insights industry estimates
- **Value:** ~49.1 billion withdrawals
- **Derivation:** Total global ATM transactions ~86.7B (all types) × 57% cash withdrawal share = ~49.4B. Cross-checked against BIS+ECB+RBI+Fed country-level sum + rest-of-world estimate = ~49.1B
- **Strengths:** BIS and ECB data is central-bank-quality; RBI publishes monthly; ATMIA is the industry association; multiple independent inputs converge
- **Weaknesses:** US data is extrapolated from 2021 Fed study (triennial); China ATM data is PBOC aggregate; withdrawal share of total ATM transactions (57%) is estimated

### Method B: ATM Count x Transactions-Per-ATM

- **Source:** 3.12 million ATMs worldwide (RBR/Datos Insights), ~15,700 withdrawals per ATM per year (industry average)
- **Value:** 3.12M × 15,700 = ~49.0B withdrawals
- **Strengths:** ATM fleet count is well-tracked by industry researchers; transactions-per-ATM is a standard industry metric
- **Weaknesses:** Transactions-per-ATM varies enormously (India ~28,000, US ~5,300, Japan ~14,000); using a single global average introduces error; ATM fleet data may lag closures

### Method C: Peak-Year Decline Trend

- **Source:** 2016 peak of ~63B (ATMIA), observed -3.0% CAGR (2016-2024)
- **Value:** 63B × (1-0.03)^8 = ~49.3B
- **Strengths:** Simple, independent validation; trend is consistent pre- and post-COVID
- **Weaknesses:** Assumes constant decline rate — actual rate varies by year and region; COVID created a discontinuity (2020: -26%) that partially recovered

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [BIS/ECB/RBI]        [ATMs × Txn/ATM]   [Peak Decline] │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 49.1B        │    │ ~49.0B       │    │ ~49.3B     │ │
│  │ (central bank│    │ (3.12M ATMs  │    │ (63B peak  │ │
│  │  composite)  │    │  × 15,700/yr)│    │  × -3%     │ │
│  │              │    │              │    │  CAGR)     │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ All three methods      │                │
│                │ converge at 49.0-49.3B │                │
│                │ Tight cluster: <0.6%   │                │
│                │ spread                 │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   49.1B withdrawals    │                │
│                │   1,557 TPS            │                │
│                │   Confidence: 52/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**BIS/ECB/RBI composite (Method A) anchors the final estimate** because:
1. It aggregates the highest-quality national data sources (central banks + industry body)
2. ATM count × transactions-per-ATM (Method B) independently converges at ~49.0B
3. Peak-year decline trend (Method C) produces ~49.3B from a completely independent approach
4. All three methods cluster within 0.6% — unusual convergence for this project

**Key strength of this category:** Three fully independent methods produce nearly identical estimates. The convergence gives higher confidence in the number than the 52/100 score suggests — confidence is constrained by the stale US data (2021 Fed study) and PBOC opacity, not by methodological disagreement.

## Overlap Analysis

```
ATM Withdrawals: 49.1B total
                │
                │  ATM withdrawals are CASH-OUT events,
                │  not payments. They have ZERO overlap
                │  with any other payment category:
                │
                ████████████████████████████████████  49.1B
                │
                │  Card authentication:
                │  ATMs use card + PIN for auth,
                │  but the withdrawal is NOT counted
                │  in card purchase statistics.
                │  Nilson/Visa 772.73B = purchases only.
                │
                │  Cash spending:
                │  The cash withdrawn is spent later
                │  in untracked cash transactions —
                │  invisible to all electronic payment
                │  categories.
                │
                ▼
De-duplicated   ████████████████████████████████████  49.1B
                ATM Withdrawals is a STANDALONE
                category — zero deductions needed.
                Cleanest category in the taxonomy.
```

**ATM Withdrawals has zero overlap** with any other payment category. This is the cleanest category in the entire Universe of Finance taxonomy. An ATM withdrawal is a cash-out event — the card interaction authenticates the user but the transaction is a cash disbursement, not a purchase. Card network statistics (Nilson's 772.73B) explicitly exclude ATM withdrawals from purchase counts.

## Coverage Assessment

- **Directly observed:** ECB (EU-27: 7.5B, 15%), RBI (India: ~6B, 12%), Fed (US: extrapolated from 2021, 5%) — total ~32% from central bank/government data
- **Semi-observed:** ATMIA/Datos Insights industry estimates (~40%) — reputable but proprietary
- **Estimated:** China (24%), Africa (6%), rest of world (~22%) — derived from ATM fleet + usage rates

```
Region          Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
China           ████████ 24.4%   Low (PBOC aggregate)
Asia-Pac (ex CN)████░░░░ 20.4%   Medium (India RBI monthly)
Europe          ████░░░░ 20.4%   High (ECB half-yearly)
North America   ███░░░░░ 16.3%   Medium (Fed 2021 extrapolated)
Latin America   ██░░░░░░ 10.2%   Low (fragmented data)
Africa/ME       █░░░░░░░  6.3%   Low (sparse data)
Other           █░░░░░░░  2.0%   Low
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
BIS Red Book        ███████░░  ██████░░░ ██████████  ██████░░░░
ECB Payment Stats   ████░░░░░  █████████ ██████████  █████████░
RBI ATM Stats       ██░░░░░░░  █████████ █████████░  █████████░
Fed Payments Study  ██░░░░░░░  █████░░░░ ██████████  █████████░
ATMIA/Datos         █████████  ████████░ ███████░░░  ██████░░░░
World Bank ATMs     █████████  ████████░ █████████░  ████░░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    65/100     78/100    88/100      62/100
```

- **Final confidence score:** 52/100
- **Key uncertainty drivers:**
  - US data is extrapolated from 2021 Fed study (3 years stale)
  - China PBOC does not cleanly separate ATM withdrawals from other card transactions
  - Withdrawal vs. total ATM transaction share (57%) is estimated
  - Independent ATM deployer (IAD) data is murkier than bank-owned ATM data

## Revision History

- **Run 5 (2026-03-28):** Initial estimate — 49.1B from BIS/ECB/RBI composite
- **Run 6 (2026-03-28):** Methodology documentation formalized with three-method triangulation

---
title: "Tax & Government Payments — Methodology"
parent: Government
grand_parent: Explore
nav_order: 101
---

# Tax & Government Payments -- Measurement Methodology

## Transaction Definition

One government payment transaction = **one discrete payment event between
a government entity and a citizen, business, or other government entity**.

This includes:
- **Inflows** (citizen/business -> government): tax payments, VAT remittances,
  customs duties, fees, fines
- **Outflows** (government -> citizen/business): benefit disbursements, pension
  payments, payroll, procurement payments, tax refunds

Counted at: **the payment event** (one tax filing with payment = 1 transaction;
one monthly Social Security deposit = 1 transaction).
Excluded: intergovernmental transfers, government bond issuance/redemption
(covered in traditional finance), central bank operations, employer withholding
at the per-employee level (counted at the employer remittance level).

---

## Triangulation Approach

### Method A: India DBT + US IRS + EU Bottom-Up Model

Three independent country models anchor the estimate, covering ~46% of
global GDP:

**US Model (5.09B transactions):**
- Tax payments: ~290M (IRS 161M individual + 7M corporate + 50M est. quarterly + 72M payroll)
- Federal benefits: ~3.64B (SS 852M + Medicare 1.0B + Medicaid 750M + SNAP 504M + payroll 112M + other 422M)
- State/local: ~1.16B (income tax 130M + sales tax 180M + property 150M + payroll 520M + pensions 180M)

**India Model (8.19B transactions):**
- DBT direct benefit transfers: ~7.4B (FY2023-24, official DBT Mission data)
- GST remittances: ~140M (1.4Cr businesses x 12 monthly)
- Income tax: ~80M (8Cr ITRs filed FY2023-24)
- Other govt payments: ~570M (state pensions, scholarships outside DBT)

**EU Model (5.84B transactions):**
- Tax payments: ~800M (27 member states, ~30M businesses x 12 VAT + ~200M income tax returns)
- Benefits disbursements: ~3.6B (~150M pension/welfare recipients x 12 months + unemployment)
- Government payroll: ~400M (~16M govt employees x 12-26 pay periods)
- Other: ~1.04B (customs, fees, local government)

**Rest of World (12.5B):**
Tiered extrapolation using GDP ratios and government-spending-to-GDP
percentages, adjusted for digital payment adoption rates.

### Method B: Top-Down GDP-Based Estimate

Global GDP (~$110T) x government spending share (~35%) = ~$38.5T in govt
payment flows. At estimated average transaction value (~$1,000-1,200),
this implies **25-38B** transactions.

### Method C: Payment System Cross-Validation

US Treasury reports disbursing >1.2B federal payments/year. Our US
federal estimate of ~3.93B includes Medicare/Medicaid claims (paid by
contractors) and SNAP (state-administered). Removing those: ~1.68B --
broadly consistent with Treasury's figure.

```
+---------------------------------------------------+
|              RAW ESTIMATES                          |
|                                                     |
|  Method A            Method B           Method C    |
|  [3-Country Model]   [GDP Top-Down]     [Treasury]  |
|  +-------------+     +------------+     +---------+ |
|  | US:   5.09B |     | 25-38B     |     | US fed: | |
|  | India: 8.19B|     | (global)   |     | ~1.2B   | |
|  | EU:   5.84B |     |            |     | (Treas- | |
|  | RoW: 12.50B |     |            |     |  ury    | |
|  | = 31.6B     |     |            |     |  only)  | |
|  +------+------+     +-----+------+     +----+----+ |
|         |                  |                 |      |
|         +------------------+-----------------+      |
|                            v                        |
|              +------------------------+             |
|              |    RECONCILIATION      |             |
|              | Method A (31.6B) falls |             |
|              | within Method B range  |             |
|              | (25-38B). Method C     |             |
|              | validates US subset.   |             |
|              | India DBT is the most  |             |
|              | surprising data point  |             |
|              | -- 7.4B txns from one  |             |
|              | programme alone.       |             |
|              +----------+-------------+             |
|                         v                           |
|              +------------------------+             |
|              |   FINAL ESTIMATE       |             |
|              |   31.6B +/- 5B         |             |
|              |   ~1,002 TPS (calendar)|             |
|              |   Confidence: 50/100   |             |
|              +------------------------+             |
+---------------------------------------------------+
```

---

## The India DBT + US IRS + EU Bottom-Up Model

This is the methodological centrepiece. The three anchor countries were
chosen because they have the best-documented government payment systems
and represent three different archetypes:

```
+-----------------------------------------------------------------+
|                    THREE ARCHETYPES                               |
|                                                                   |
|  US (Mature Digital)    India (Leapfrog)    EU (Federated)       |
|  +----------------+    +----------------+   +----------------+   |
|  | Strong agency  |    | JAM trinity    |   | 27 member      |   |
|  | reporting (IRS,|    | (Jan Dhan +    |   | states, each   |   |
|  | SSA, CMS).     |    | Aadhaar +      |   | with own tax   |   |
|  | Federal/state  |    | Mobile).       |   | and benefits   |   |
|  | split well-    |    | DBT dashboard  |   | systems.       |   |
|  | documented.    |    | is real-time,  |   | OECD data      |   |
|  | 5.09B txns.    |    | public. 8.19B  |   | provides        |   |
|  |                |    | txns -- more   |   | cross-country   |   |
|  |                |    | than the US.   |   | comparability.  |   |
|  |                |    |                |   | 5.84B txns.    |   |
|  +----------------+    +----------------+   +----------------+   |
|                                                                   |
|  Combined: 19.12B (~46% of global GDP)                           |
|  Rest of World: 12.50B (extrapolated)                            |
|  TOTAL: 31.6B                                                     |
+-----------------------------------------------------------------+
```

### Why India Dominates by Count

India's 8.19B government payment transactions exceed the US (5.09B)
despite a GDP only ~1/7th the size. Three factors:

1. **DBT scale**: 313 schemes, 800M+ beneficiaries, 7.4B transactions
   in FY2023-24. This is the world's largest government-to-citizen
   payment programme by transaction count.
2. **Monthly frequency**: Most DBT schemes pay monthly (PM-KISAN pays
   3x/year, but pensions/MGNREGA pay monthly or more)
3. **Low average value**: Average DBT transaction ~$17 vs US Social
   Security ~$1,907/month. India processes many more small payments.

---

## Reconciliation

The three methods produce a range of 25-38B with the bottom-up model
at 31.6B (near the midpoint). Key tensions:

- **Method B overestimates** if average transaction value is too low
  (many govt payments are large -- tax refunds, procurement)
- **Method A may underestimate** Rest of World (12.5B is conservative
  given that China, Brazil, Indonesia, and Nigeria are under-documented)
- **Method C validates the US subset** but only for Treasury-disbursed
  payments (excludes Medicare/Medicaid contractor payments)

---

## Key Methodological Challenges

### Fragmentation Across 190+ Countries

No global aggregator for government payment transactions exists.

- **OECD Revenue Statistics**: 36 countries, tax revenue data (not
  transaction counts)
- **IMF GFS**: 150+ countries, revenue/expenditure data (not counts)
- **World Bank BOOST**: 80+ developing countries, line-item expenditure
  (not counts)

For ~100 countries (sub-Saharan Africa, parts of Asia, Central America),
there is essentially zero published data on government payment counts.
We rely on GDP-ratio extrapolation for these regions.

### Informal Economy

In developing nations, 30-60% of economic activity occurs outside
formal tax systems:

| Country   | Shadow Economy (% GDP) | Impact on Count          |
|-----------|----------------------|--------------------------|
| Nigeria   | ~55%                 | Most tax collected in cash |
| India     | ~25%                 | Declining (GST + DBT)     |
| Brazil    | ~35%                 | Nota Fiscal improving     |
| Germany   | ~9%                  | Minimal impact             |

Formalisation (India GST, Brazil digital tax, EU ViDA) is the primary
driver of future government payment transaction growth.

### Definition Granularity

"One tax payment" is ambiguous:
- If counted at employer remittance level: 72M US payroll transactions
- If counted at per-employee withholding level: ~2B+ US transactions
- We count at the **employer remittance** level (the actual payment event)

### Extreme Seasonality

Government payments are the most seasonal category in finance:

- **US IRS**: 161M returns, ~80% filed January-April
- **UK HMRC**: Self-assessment deadline = 31 January (massive spike)
- **Benefits**: US Social Security pays on 2nd, 3rd, 4th Wednesdays
- **Peak-to-average TPS ratio**: Estimated 5-10x

---

## Overlap Analysis

```
Government payments flow through existing payment rails:

              GOVERNMENT PAYMENT FLOWS
              |
              +-- ACH/Bank Transfer (~60%)
              |   -> Already counted in bank-transfers capsule
              |   (US: FedACH, EU: SEPA, India: NEFT/UPI)
              |
              +-- Direct deposit / wire (~15%)
              |   -> Counted in interbank-rtgs for large values
              |
              +-- Check (~10%, declining)
              |   -> Not counted elsewhere (unique to this capsule)
              |
              +-- Card (~5%)
              |   -> Already counted in consumer-cards
              |
              +-- Cash (~10%, developing countries)
                  -> Not counted elsewhere

Overlap with bank-transfers: ~60% of 31.6B = ~19B transactions
are also counted as ACH/bank transfer volume.
```

---

## Coverage Assessment

```
Category: Tax & Government Payments (31.6B annual transactions)

Region          Volume    Share   Data Quality
--------------- -------- ------- ----------------
India (DBT)     ########   26%   DBT Mission dashboard (public)
US (Federal)    ######     16%   IRS, SSA, CMS (excellent)
EU (27 states)  ######     18%   OECD aggregate + national
US (State/Local)####        4%   Census of Govts (decent)
China           ####       10%   Opaque; GDP-ratio estimate
Rest of World   ########   26%   GDP-ratio extrapolation
```

---

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ---------  --------  ----------  -----------
IRS Data Book       █████████  █████████ ██████████  ██████████
SSA Stat Suppl.     █████████  █████████ ██████████  █████████░
India DBT Portal    █████████  █████████ █████████░  ████████░░
OECD Rev. Stats     ████████░  ████████░ ██████████  █████░░░░░
IMF GFS             ████████░  ██████░░░ ██████████  ████░░░░░░
World Bank BOOST    ██████░░░  █████░░░░ █████████░  ██████░░░░
                    ---------  --------  ----------  -----------
Composite Score:    50/100     78/100    92/100      55/100
```

**Overall confidence: 50/100** -- Strong anchor data for US and India;
EU estimate is reasonable. Rest of World (~40% of total) relies on
GDP-ratio extrapolation, which is the primary source of uncertainty.

---

## Revision History

| Date       | Change                                          | Impact           |
|------------|------------------------------------------------|------------------|
| 2026-03-26 | Initial estimate: ~25B, ~790 TPS                | Baseline         |
| 2026-03-26 | Run 3: Bottom-up model (US+India+EU)            | Revised to 31.6B |
| 2026-03-26 | TPS revised to ~1,002                           | +26% from initial|

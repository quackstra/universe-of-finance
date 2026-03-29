---
title: "Methodology"
layout: default
nav_order: 4
---

# Universe of Finance — Methodology Paper

> How we measured every financial transaction on Earth.

*Working paper, March 2026. Version 1.0.*

---

## Abstract

The Universe of Finance project estimates the total throughput of the global
financial system: **~73,750 de-duplicated transactions per second** (~2.3
trillion per year) across 29 categories spanning 7 sectors. We further
introduce the **MEST framework** (Mutual Economic State Transitions) and
estimate the bilateral state-change rate at **~545,000 per second** — 7.4
times the transaction count. This paper documents the full research
methodology: the triangulation-first data collection approach, the 0-100
confidence scoring rubric, the overlap de-duplication matrix, MEST multiplier
derivation, country-level estimation procedures, and the expert persona
framework (Soul Less Employees) that grounds the research in domain-specific
expertise. All data is structured, versioned, and open source (CC BY 4.0 /
MIT) to enable reproducibility and iterative improvement across research runs.

The work matters because no prior public estimate exists for the total
transaction throughput of the global financial system. Individual data points
are available — Visa publishes card transactions, the BIS publishes payment
system volumes, the WFE publishes exchange trade counts — but no framework
combines them into a single, de-duplicated, confidence-scored figure. The
Universe of Finance fills that gap, and the MEST framework reveals the hidden
operational load that sits beneath every user-visible transaction.

---

## 1. Research Design

### 1.1 Triangulation-First Approach

Every category in the Universe of Finance is researched using a
**triangulation-first** methodology. This means we do not accept a single
data source as authoritative, no matter how reputable. The minimum standard
for any category estimate is:

1. **Find 2-3 independent data sources** that measure the same phenomenon
   using different methods, definitions, or vantage points
2. **Build both bottom-up and top-down models**, then reconcile
3. **Document all assumptions, blind spots, and confidence** explicitly
4. **Quantify overlaps** with other categories to enable accurate
   de-duplication at the global level

For example, the Consumer Cards estimate (24,501 TPS) is anchored by:

- **Method A**: Nilson Report global aggregate (772.73B transactions) — the
  industry's gold-standard source, used by card networks in their own
  reporting
- **Method B**: Bottom-up sum of six network 10-K/public filings (769.6B)
  — each major network figure from audited SEC filings or central bank data
- **Method C**: Capital One Shopping secondary aggregation (791B) — an
  independent compilation that includes private-label cards

Methods A and B converge to within 0.4%. Method C is 2.4% higher, explained
by inclusion of domestic-only cards. This three-way convergence, documented
in every capsule's METHODOLOGY.md, is what makes the confidence score (91)
the highest in the project.

The triangulation requirement is not a suggestion. Categories where only a
single method was available (e.g., AI Agent Transactions, Payroll Payments)
receive correspondingly low confidence scores (34 and 35 respectively) and
are flagged as estimates rather than measurements.

### 1.2 Bottom-Up vs. Top-Down Reconciliation

For each category, we construct two independent estimates:

- **Bottom-up**: Aggregate individual components (e.g., sum each card
  network's transaction count, sum each exchange's trade volume)
- **Top-down**: Start from a macro figure and decompose (e.g., global
  payment revenue divided by average transaction fee to derive volume)

The reconciliation gap between bottom-up and top-down is itself a
diagnostic. A small gap (< 5%) indicates convergent evidence; a large gap
(> 25%) triggers a mandatory methodology review by the panel of cross-cutting
SLE experts (see Section 8).

Example — Equity Markets:

| Method | Estimate | Gap |
|--------|----------|-----|
| WFE monthly extrapolation (top-down) | ~61.1B trades | — |
| 2023 baseline + growth (top-down) | ~59.9B trades | 2% |
| Bottom-up exchange aggregation (13 exchanges) | ~66.9B raw | — |
| Adjusted for NSE equity/derivatives conflation | ~61.9B | 1.3% |
| **Final reconciled estimate** | **~61.5B** | |

The bottom-up over-count was traced to a specific cause: NSE India's headline
figure conflates equity cash trades with equity derivatives. Adjusting NSE
from ~18B to ~15B (equity cash only) brought all three methods into
agreement.

### 1.3 The 29-Category, 7-Sector Taxonomy

The taxonomy was designed to satisfy two competing goals:

- **Completeness**: Every measurable financial transaction on Earth should
  fall into exactly one category
- **Minimal overlap**: Categories should be defined so that a given
  transaction is naturally assigned to one category, not two

| Sector | Categories | Combined Gross TPS |
|--------|-----------|-------------------|
| Payments (11) | Consumer Cards, Digital Wallets, Bank Transfers, E-Commerce, P2P, Remittances, Bill Payments, Insurance Premiums, BNPL, Payroll, ATM Withdrawals | ~67,600 |
| Traditional Finance (6) | ETD, Equities, Commodities, Forex, Fixed Income, OTC Derivatives | ~13,400 |
| Digital Assets (4) | CEX, L1/L2 Blockchain, Stablecoins, DeFi | ~4,100 |
| Banking (2) | Interbank RTGS, Securities Settlement | ~100 |
| Gaming (2) | Microtransactions, Game Sales | ~480 |
| Government (1) | Tax & Government Payments | ~1,000 |
| Emerging (3) | IoT/M2M, RWA Tokenisation, AI Agents | ~1,540 |

**Why these boundaries?** The taxonomy distinguishes between **payment rails**
(the infrastructure that moves money) and **commerce layers** (the economic
events that trigger payments). Consumer Cards, Bank Transfers, and Digital
Wallets are payment rails — they count cleared transactions on financial
infrastructure. E-Commerce, Gaming, and Government Payments are commerce
layers — they count economic events that ride on those rails.

This distinction is critical for de-duplication. An Amazon purchase is one
e-commerce event AND one card transaction. The card transaction is the
payment rail event; the e-commerce event is the commerce layer event. Both
are real, but counting both in the global total would double-count. Our
taxonomy assigns the payment rail event as the "base layer" and deducts
commerce-layer overlaps (see Section 5).

**Why 29 categories, not 15 or 50?** Fewer categories would create internal
heterogeneity problems (lumping all payments into one bucket loses the
card-vs-bank distinction that matters for overlap analysis). More categories
would create unmeasurable fragments (splitting cards into credit/debit/prepaid
would require data that networks do not publish at sufficient granularity).
29 is the resolution at which the available data supports meaningful
measurement.

### 1.4 How Categories Were Chosen

Categories were added through a structured process across 11 research runs:

- **Run 1**: 24 initial categories covering the obvious quadrants (payments,
  TradFi, digital assets, banking)
- **Run 5**: 5 new payment categories (ATM, Bills, Payroll, Insurance, BNPL)
  added after the Run 4 overlap analysis revealed significant uncounted
  payment flows
- **Run 7**: MEST framework applied to all 29 categories

New categories are added when:

1. A measurable transaction flow is identified that does not fit any existing
   category
2. The flow contributes > 0.1% of estimated global TPS (threshold: ~74 TPS)
3. At least one credible data source exists

Categories are NOT added for speculative or pre-market flows until
measurement data exists. AI Agent Transactions (0.66 TPS, confidence 34) is
the lowest-volume category included, retained primarily as a forward-looking
placeholder.

---

## 2. Data Collection

### 2.1 Primary Sources by Type

| Source Type | Examples | Categories Covered |
|------------|---------|-------------------|
| **Central bank statistics** | BIS CPMI Red Book, PBOC Aggregate, ECB Payment Statistics, RBI Annual Report, BCB/Pix data | Bank Transfers, RTGS, Digital Wallets (UPI), Government Payments |
| **Exchange filings** | WFE Monthly Dashboard, FIA Annual Survey, individual exchange annual reports (NSE, JPX, CME, SSE) | Equities, ETD, Commodities |
| **Public company filings (SEC/10-K)** | Visa 10-K, Mastercard 10-K, Coinbase 10-K, PayPal 10-K | Consumer Cards, CEX, Digital Wallets |
| **Industry associations** | Nilson Report (cards), SWIFT (messaging), CLS (forex settlement), DTCC (settlement) | Consumer Cards, Forex, Fixed Income, Securities Settlement |
| **Market data providers** | CoinGecko (crypto volume), Kaiko (crypto microstructure), Bloomberg (TradFi) | CEX, DeFi, Stablecoins, L1/L2 |
| **On-chain data** | Blockchain explorers, Dune Analytics, DefiLlama | L1/L2, DeFi, Stablecoins, RWA |
| **Academic research** | NBER/Yale (wash trading), CEPR (market microstructure), World Bank (remittances) | CEX, Remittances |
| **Government statistics** | IRS (US tax), HMRC (UK), India JAM/DBT | Government Payments |
| **Market research firms** | McKinsey Global Payments, Swiss Re sigma (insurance), Newzoo (gaming) | Cross-cutting, Insurance, Gaming |

### 2.2 Source Hierarchy

When sources conflict, we apply a strict hierarchy:

```
1. Regulator / central bank data       (highest authority)
2. Audited public company filings       (SEC-enforced accuracy)
3. Industry association data            (e.g., Nilson, FIA, WFE)
4. Market data providers                (e.g., CoinGecko, Kaiko)
5. Market research firms                (e.g., McKinsey, Gartner)
6. Analyst estimates / projections      (lowest authority)
```

A lower-ranked source can anchor an estimate only when higher-ranked sources
do not publish the needed metric. For example, no regulator publishes global
CEX trade counts — so CoinGecko volume data (rank 4) anchors that category,
despite its lower authority. This is reflected in the confidence score (56
vs. 91 for cards, where Nilson/Visa 10-K data is available).

### 2.3 Data Freshness Requirements

Each data point carries a freshness tag tracked in `analysis/DATA_FRESHNESS.md`.
The requirements:

| Freshness Tier | Definition | Scoring Impact |
|---------------|-----------|---------------|
| Current | Data from within 12 months | Full recency score (16-20/20) |
| Recent | Data 1-2 years old | Moderate penalty (10-15/20) |
| Aging | Data 2-3 years old | Significant penalty (5-9/20) |
| Stale | Data older than 3 years | Major penalty (0-4/20) |

The BIS Triennial Survey (forex) is the most problematic freshness case: it
is the most authoritative source for global FX activity, but it is published
only every three years. The 2022 survey anchors our forex estimate, earning
a recency score of 10/20 despite its unimpeachable authority.

### 2.4 Handling Missing Data and Estimates

When direct measurement data is unavailable, we employ structured estimation
techniques:

1. **Proxy variable derivation**: Revenue / average transaction value =
   estimated transaction count. Used for CEX (volume / average trade size),
   Gaming Microtransactions (revenue / average IAP), Payroll (employment x
   pay frequency)

2. **Coverage extrapolation**: If 70% of the market is directly observed,
   estimate the remaining 30% using GDP-weighted or population-weighted
   scaling. The `statistical-methodologist` SLE provides the imputation
   methodology

3. **Growth-rate projection**: When the most recent authoritative figure is
   from a prior year, apply a documented growth rate. Always decompose
   growth into drivers (not a naked CAGR) — e.g., India UPI growth is
   decomposed into merchant onboarding + rural adoption + government push

4. **China opacity model**: Chinese financial data presents unique challenges
   (see Section 7). We use PBOC aggregate data as the primary anchor,
   cross-checked against Alipay/WeChat corporate disclosures and UnionPay
   filings. The resulting uncertainty band is +/- 6,000 TPS

All estimation methods are documented in each capsule's `workings/` directory
with explicit assumptions and sensitivity analysis.

---

## 3. Confidence Scoring

### 3.1 The 0-100 Rubric

Every category receives a composite confidence score across four weighted
dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Source Quality | 0-30 | Primary/regulatory data vs. estimates |
| Data Recency | 0-20 | How fresh the underlying data is |
| Triangulation | 0-25 | Independent methods that agree |
| Coverage | 0-25 | Percentage of known market captured |

**Total: 0-100.**

#### Source Quality (0-30)

| Range | Meaning |
|-------|---------|
| 25-30 | Primary/regulatory data (central bank reports, exchange filings, government statistics) |
| 15-24 | Industry reports from credible bodies (FIA, Nilson, BIS, IEA) |
| 5-14 | Extrapolations from partial data or market research firms |
| 0-4 | Pure estimates with no verifiable source |

#### Data Recency (0-20)

| Range | Meaning |
|-------|---------|
| 16-20 | Data from within 12 months |
| 10-15 | Data 1-2 years old |
| 5-9 | Data 2-3 years old |
| 0-4 | Data older than 3 years |

#### Triangulation (0-25)

| Range | Meaning |
|-------|---------|
| 20-25 | 3+ independent methods/sources agree within 20% |
| 10-19 | 2 independent methods/sources |
| 0-9 | Single method or source |

#### Coverage (0-25)

| Range | Meaning |
|-------|---------|
| 20-25 | >90% of the known market captured |
| 10-19 | 50-90% of the market captured |
| 0-9 | <50% of the market captured |

### 3.2 Score Distribution Across Categories

| Band | Range | Count | Categories |
|------|-------|-------|-----------|
| High | 80-100 | 4 | Consumer Cards (91), ETD (88), Equities (86), RTGS (82) |
| Medium-High | 65-79 | 10 | Bank Transfers (78), L1/L2 (76), Stablecoins (75), Securities Settlement (74), Commodities (74), P2P (69), OTC Derivatives (68), IoT (67), Digital Wallets (67), E-Commerce (67) |
| Medium | 50-64 | 9 | DeFi (62), Fixed Income (60), BNPL (58), Remittances (58), Forex (58), CEX (56), RWA (56), Game Sales (56), ATM (52) |
| Medium-Low | 35-49 | 4 | Insurance (52), Government (50), Bill Payments (48), Microtransactions (44) |
| Low | 0-34 | 2 | Payroll (35), AI Agents (34) |

**Median score: 62.** The distribution is right-skewed — more categories have
adequate data than poor data, but the long tail of low-confidence categories
contains some high-volume entries (Bill Payments at 3,012 gross TPS scores
only 48).

### 3.3 What Confidence Levels Mean for Reliability

| Score Range | Interpretation | Typical Uncertainty |
|------------|----------------|-------------------|
| 80-100 | Measurement — based on primary data with cross-validation | +/- 5-10% |
| 60-79 | Estimate — based on credible secondary sources with some triangulation | +/- 15-25% |
| 40-59 | Rough estimate — derived from proxy variables or limited sources | +/- 30-50% |
| 20-39 | Order-of-magnitude — educated guess with minimal direct data | +/- 50-100% |

The Big Number (~73,750 TPS) is more reliable than the median category
confidence suggests, because the highest-confidence categories also
contribute the most TPS. The top 5 categories by TPS (cards, wallets, bank
transfers, ETD, equities) have a weighted average confidence of 82. They
account for ~72,000 of the ~86,900 gross TPS. Low-confidence categories
contribute only ~7% of the total, so their uncertainty has limited impact
on the headline figure.

### 3.4 How Scores Improve Over Research Runs

Confidence scores are not static. Each research run targets specific
categories for confidence uplift:

| Run | Confidence Actions |
|-----|-------------------|
| Run 4 | First confidence scorecard (34-91 range) |
| Run 6 | Methodology documentation for all 29 categories |
| Run 7 | MEST framework + deep dive triangulation |
| Run 9 | Panel review of top-3 categories; ATM/Insurance/Payroll uplift |
| Run 10 | AI Agents/Microtx/Bills uplift |

The primary mechanisms for confidence improvement are:

1. **New data sources discovered** (e.g., PBOC aggregate for UnionPay)
2. **Additional triangulation methods added** (e.g., bottom-up exchange sum
   for equities)
3. **Coverage expansion** (e.g., RTGS expanded from 5 to 13 systems)
4. **Panel review** by methodology SLEs (definition + sizing + uncertainty
   audits)

---

## 4. Overlap De-Duplication

### 4.1 The Overlap Matrix Methodology

The raw sum across all 29 categories is ~89,300 TPS. The de-duplicated
total is ~73,750 TPS. The difference (~15,550 TPS, or ~17.4%) represents
transactions counted in multiple categories.

De-duplication follows a strict protocol:

1. **Identify base layers**: Payment rails (Consumer Cards, Bank Transfers)
   are base layers. They count transactions at the clearing/settlement
   infrastructure level. These are never deducted.

2. **Identify commerce layers**: E-Commerce, Gaming, Government Payments,
   IoT are commerce layers. They count economic events that ride on payment
   rails. Their card/bank-rail portion is deducted.

3. **Quantify overlap percentages**: For each commerce-layer category,
   estimate the percentage of transactions that settle on each payment rail.
   Document the data source for each percentage.

4. **Handle subset relationships**: DeFi and Stablecoins are subsets of
   L1/L2 on-chain transactions. They are not additive to L1/L2.

5. **Handle multiplier categories**: BNPL has 100% infrastructure overlap
   but creates genuine new payment events (3.6x installment multiplier).
   The incremental events (20B - 5.5B = 14.5B) are counted; the base
   purchase is not.

### 4.2 Types of Overlap

**Commerce-layer vs. payment-rail overlap** (largest category): An
e-commerce purchase, a gaming microtransaction, or a government benefit
disbursement is an economic event that triggers a payment on an existing
rail. The commerce event and the payment event are both real, but they refer
to the same flow of money. We count the payment rail event in the base layer
and deduct the overlap from the commerce layer.

**Geographic/definitional overlap**: UPI transactions in India are counted
as both "digital wallets" (because UPI apps look like wallets) and "bank
transfers" (because UPI settles as an account-to-account transfer). We
classify UPI as a bank transfer (its true settlement mechanism) and deduct
it from digital wallets. This single adjustment removes ~5,450 TPS of
double-counting.

**Subset overlap**: DeFi transactions and stablecoin transfers happen
on-chain. They are subsets of L1/L2 blockchain transactions, not additive
categories. Correct de-duplication: CEX (off-chain, 3,210 TPS) + L1/L2
(on-chain, 415 TPS) = 3,625 TPS. DeFi and Stablecoins provide analytical
granularity within L1/L2 but do not add to the total.

**Multiplier overlap**: BNPL is the unique case. Every BNPL installment
settles on a card or bank rail (100% infrastructure overlap), but the
installment payments are genuine new events on that infrastructure. A
single purchase becomes 3-4 installments, each generating a real cleared
transaction. We count the ~14.5B incremental installment events (~460 TPS)
but not the ~5.5B base purchases (which are already counted in cards).

### 4.3 From Gross 86,900 to Net 73,750

The de-duplication waterfall:

| Sector | Gross TPS | Deductions | De-Dup TPS | Overcount |
|--------|-----------|-----------|-----------|-----------|
| Payments | 68,601 | -12,913 | 55,688 | 19% |
| Traditional Finance | 13,473 | 0 | 13,473 | 0% |
| Digital Assets | ~4,100 | -475 | 3,625 | 12% |
| Banking | ~95 | 0 | ~95 | 0% |
| Gaming | ~481 | -393 | ~88 | 82% |
| Government | ~1,002 | -601 | ~401 | 60% |
| Emerging | ~1,541 | -1,153 | ~385 | 75% |
| **Total** | **~89,300** | **~-15,550** | **~73,750** | **17.4%** |

Traditional Finance has zero intra-sector overlap because each category
covers a distinct instrument class (equities, derivatives, forex, fixed
income) traded on distinct infrastructure. The Banking sector (RTGS,
Securities Settlement) is the downstream settlement layer — per taxonomy
rules, a trade counts once in TradFi and its settlement counts separately
in Banking, because both are real transactions on different infrastructure.

### 4.4 The 5 Largest Overlaps

| # | Overlap | TPS Removed | Mechanism |
|---|---------|-------------|-----------|
| 1 | Digital Wallets on card/bank rails | ~6,722 | UPI classified as bank transfer; Apple Pay/Google Pay classified as card transactions |
| 2 | Bill/Payroll/Insurance on bank/card rails | ~3,582 | ~90% of bills, payroll, and insurance settle via direct debit, ACH, or card-on-file |
| 3 | E-Commerce on card/wallet rails | ~1,732 | ~95% of e-commerce orders are paid by card or wallet |
| 4 | IoT on card/bank rails | ~1,153 | ~75% of IoT payments (tolls, vending) charge a linked card or bank account |
| 5 | Government on bank rails | ~601 | ~60% of government payments are ACH/bank transfer disbursements |

Together, these 5 overlaps account for ~13,790 of the ~15,550 TPS deducted
(89% of total deductions).

### 4.5 Programmatic Validation

The de-duplication is not performed solely by hand. `tools/big_number.py`
reads all 29 `data.json` files, applies the overlap deductions defined in
each capsule's metadata, and computes the global de-duplicated total. The
script produces **~73,753 TPS**, consistent with both Method A (Payment
Infrastructure: ~72,880) and Method B (Economic Transaction: ~73,760) within
rounding error.

---

## 5. MEST Methodology

### 5.1 Definition

A **Mutual Economic State Transition (MEST)** is any change to a holding of
economically valuable assets where more than one party has a material
interest in the record or accounting of that change and its result.

Three properties must hold:

1. **State change**: An asset of economic value changes state (balance,
   ownership, encumbrance, obligation, or entitlement)
2. **Mutual interest**: Two or more parties care about the accuracy of the
   record of that change
3. **Materiality**: The change is not trivial internal bookkeeping within a
   single entity's own ledger

A MEST is the atomic unit of economic accounting friction.

### 5.2 How Multipliers Were Derived

For each category, the `transaction-lifecycle-analyst` SLE (see Section 8)
maps the full lifecycle of a representative transaction, enumerating every
bilateral state change that occurs between distinct parties. The multiplier
is the count of distinct MESTs per originating transaction.

The derivation process:

1. **Map the transaction lifecycle**: Initiation, execution, clearing,
   settlement, post-trade, reporting
2. **Enumerate parties at each stage**: Identify every pair of entities
   that must agree on a state change
3. **Count bilateral state changes**: Each agreement between two parties
   about a change in value = 1 MEST
4. **Estimate the representative mix**: Weight common-case and edge-case
   scenarios (e.g., on-us vs. foreign ATM, wallet-to-wallet vs. wallet-
   to-merchant)
5. **Cross-validate against operational data**: Where available, compare
   against clearing house throughput, settlement system volumes, and
   messaging statistics

### 5.3 Validation Against Real Clearing/Settlement Data

MEST multipliers are validated where operational data is available:

- **Card networks**: Visa processes ~304B purchase transactions and reports
  processing ~2.1T data-carrying messages annually. This implies ~7
  messages per transaction, consistent with our 7x MEST multiplier for
  consumer cards (not all messages are MESTs, but the ratio validates the
  order of magnitude)

- **CLS (forex)**: CLS settles ~2.5M FX transactions daily but processes
  ~15-20M settlement instructions. This 6-8x ratio is consistent with our
  8x MEST multiplier for forex

- **DTCC (equities)**: DTCC processes ~105M transactions daily for US
  equities but its subsidiary NSCC handles ~400M+ netting and settlement
  instructions. The ~4x ratio represents the post-trade portion of the
  10x equity MEST multiplier

### 5.4 The Messages-Are-Not-MESTs Distinction

A common objection: "Aren't MESTs just message counts?" No. A MEST is a
bilateral state change — it requires that two parties update their records
to reflect a change in economic value. Many messages in financial
infrastructure are:

- **Status queries** (not state changes)
- **Acknowledgments** (confirming receipt, not changing value)
- **Internal routing** (within a single entity)
- **Duplicate/retry messages** (same state change, resent)

SWIFT processes ~12 billion messages per year, but many are MT199
(free-format), MT940 (statements), or MT950 (confirmations) that do not
represent bilateral state changes. The MEST count is typically lower than
the raw message count for messaging-heavy categories (banking, forex) and
higher for categories where state changes occur without formal messages
(gaming, IoT).

### 5.5 Per-Category Multiplier Table

| # | Category | Avg TPS | MEST Mult | MEST/s | Key Cascade Stages |
|---|----------|---------|-----------|--------|--------------------|
| 1 | Consumer Cards | 24,501 | 7x | 171,507 | Auth, clearing, interchange, 2 settlement legs, merchant credit, statement |
| 2 | Digital Wallets | 19,660 | 5x | 98,300 | Wallet debit, payment rail, merchant credit, statement, platform fee |
| 3 | Bank Transfers | 15,338 | 5x | 76,690 | Origination, batch/queue, clearing, settlement, receiver credit |
| 4 | ETD | 9,505 | 10x | 95,050 | Match, report, CCP novation, margin (x2), netting, settlement, regulatory |
| 5 | Equities | 3,500 | 10x | 35,000 | Match, report, CCP novation, netting, CSD DvP (x2), custody (x2), regulatory |
| 6 | CEX | 3,210 | 4x | 12,840 | Match, buyer credit, seller debit, internal ledger. No CCP/CSD |
| 7 | Bill Payments | 3,012 | 4x | 12,048 | Presentment, authorization, rail process, biller credit |
| 8 | E-Commerce | 1,823 | 3x | 5,469 | Order, payment rail, fulfillment record |
| 9 | ATM | 1,557 | 4x | 6,228 | Auth, dispensing, interbank settle, account debit |
| 10 | IoT/M2M | 1,538 | 3x | 4,614 | Device auth, micropayment, settlement |
| 11 | Payroll | 1,236 | 5x | 6,180 | Instruction, tax withholding, employer debit, employee credit, payslip |
| 12 | Government | 1,015 | 5x | 5,075 | Filing/eligibility, instruction, debit, credit, audit |
| 13 | BNPL | 634 | 6x | 3,804 | Purchase, credit decision, merchant credit, schedule, installments, close |
| 14 | Stablecoins | 520 | 3x | 1,560 | On-chain transfer, platform update, mint/burn (if applicable) |
| 15 | Microtransactions | 475 | 3x | 1,425 | Rail charge, virtual currency credit, revenue share |
| 16 | Insurance | 444 | 5x | 2,220 | Collection, policy update, reinsurance, reserve, regulatory |
| 17 | L1/L2 Blockchain | 415 | 2x | 830 | On-chain state change (sender + receiver). Lowest multiplier |
| 18 | Commodities | 330 | 9x | 2,970 | Like equities + physical delivery (warehouse receipt, quality cert) |
| 19 | P2P | 270 | 3x | 810 | Sender debit, platform ledger, receiver credit |
| 20 | Forex | 127 | 8x | 1,016 | Match, confirm, CLS PvP, netting, 2 settlement legs, nostro recon |
| 21 | Game Sales | 92 | 3x | 276 | Purchase, rail, revenue share |
| 22 | Remittances | 57 | 7x | 399 | Send, FX, correspondent debit, correspondent credit, receiver credit, beneficiary credit, compliance |
| 23 | RTGS | 50.1 | 3x | 150 | Sender debit, central bank transfer, receiver credit |
| 24 | Securities Settlement | 44 | 4x | 176 | Instruction match, DvP securities, DvP cash, custody update |
| 25 | Fixed Income | 10.5 | 8x | 84 | Trade, confirm, netting, settlement, CSD DvP, coupon, custody, regulatory |
| 26 | AI Agents | 3.5 | 3x | 11 | Request, payment, confirmation |
| 27 | RWA Tokenisation | 2.4 | 6x | 14 | Token transfer, off-chain update, custodian, regulatory, NAV, statement |
| 28 | OTC Derivatives | 0.17 | 12x | 2 | Confirm, ISDA ref, trade repo, IM (x2), VM, netting, collateral, regulatory, portfolio recon, compression |
| **Total** | | | | **~544,750** | |

The global average MEST multiplier is **~7.4x**. This means the financial
system processes approximately 7.4 bilateral state changes for every
user-visible transaction.

### 5.6 MEST De-Duplication

Unlike the Big Number, MESTs are **not de-duplicated across categories**.
Each MEST is a unique bilateral state change between a specific pair of
parties. When a card purchase triggers an interchange allocation (MEST #3
in the card cascade), that is a distinct bilateral event from the merchant
credit (MEST #6). Even though both relate to the same originating
transaction, they involve different party pairs and different state changes.

The MEST Number (~545,000/s) is therefore a gross figure by design. It
measures the total volume of bilateral accounting friction in the global
economy.

---

## 6. Country Deep Dive Methodology

### 6.1 How Country-Level TPS Is Estimated

Country deep dives (currently: USA, India, China, Brazil, EU, Japan, UK,
Africa) estimate the national or regional contribution to global TPS using
a three-step process:

1. **Direct measurement**: Where country-level data exists (e.g., India's
   NPCI publishes UPI volumes, Brazil's BCB publishes Pix volumes), use it
   directly

2. **Attribution from global data**: Where only global figures exist, apply
   country share percentages (e.g., USA is ~30% of global card transactions
   based on Visa/Mastercard geographic breakdowns in 10-K filings)

3. **Residual estimation**: For categories where country data is unavailable,
   estimate using GDP-weighted or population-weighted proxies, with
   documented adjustment factors (e.g., India's equity share is 28% of
   global despite 3.5% GDP share — this cannot be GDP-weighted and requires
   direct NSE data)

### 6.2 Handling Countries with Poor Data

**China opacity model**: China is the largest single-country uncertainty
in the Big Number. Key challenges:

- Alipay and WeChat Pay do not publish granular transaction counts
- CNAPS-HVPS processes more than Fedwire, but English-language data is
  limited
- UnionPay's transaction count (~247B) is estimated from PBOC aggregates,
  not directly disclosed

Our approach:

1. Use PBOC aggregate payment statistics as the primary anchor
2. Cross-check against Alipay/WeChat corporate disclosures (quarterly
   earnings, regulatory filings)
3. Cross-check against UnionPay annual report summaries
4. Model the uncertainty band explicitly: China could contribute
   8,000-14,000 TPS, a +/- 6,000 TPS range

The China opacity model is documented in
`analysis/deep-dives/china/REPORT.md` with full source citations and
sensitivity analysis.

**Emerging market estimation**: For countries without comprehensive payment
statistics (much of Africa, parts of Southeast Asia, Central Asia), we use
a tiered estimation approach:

- **Tier 1 countries** (with central bank statistics): Direct data
- **Tier 2 countries** (with partial data): Interpolation from regional
  aggregates
- **Tier 3 countries** (with no data): GDP-weighted extrapolation from
  Tier 1/2 countries in the same region, adjusted for financial inclusion
  rates (World Bank Findex)

### 6.3 Avoiding Double-Counting with Global Totals

Country deep dives are analytical decompositions of the global total, not
independent estimates that sum to a separate figure. The constraint is:

```
Sum of all country TPS <= Global de-duplicated TPS (73,750)
```

Any country estimate that would push the sum above the global total triggers
a reconciliation review. In practice, the 8 deep-dive countries account for
~85% of global TPS, with the remaining ~15% allocated to rest-of-world.

Country-level MEST multipliers vary by financial infrastructure maturity:

| Country | Avg MEST Multiplier | Why |
|---------|-------------------|-----|
| USA | 8.1x | Deep intermediary chains, regulatory reporting burden |
| Brazil | 5.8x | Pix compresses payment MESTs; simpler banking structure |
| India | 6.2x | UPI reduces card-like cascades; heavy equity derivatives |
| Japan | 7.5x | Cash-to-digital transition; complex banking relationships |
| UK | 8.4x | FX capital of the world (38.1% of global FX); deep post-trade |

---

## 7. Soul Less Employees (SLEs)

### 7.1 The Expert Persona Framework

The Universe of Finance employs 17 **Soul Less Employees** — expert personas
grounded in real job descriptions from the world's top financial data
organizations. Each SLE embodies the mental models, tools, data sources, and
analytical instincts of a specific domain expert.

SLEs are not generic "assistant" personas. They are built from actual job
postings at organizations like Visa, BIS, Chainalysis, DTCC, BNY Mellon,
and Gartner. The JD provides:

- **Competencies**: What the expert knows and can do
- **Data sources**: Where the expert would look first (prioritized)
- **Mental models**: How the expert frames problems
- **Blind spots**: What the expert is likely to miss or over-weight

### 7.2 How SLEs Ground Research

When a research Elf is dispatched to investigate a category, it consults the
Recruiter dispatch matrix to determine which SLE(s) are best suited. The
Elf then adopts that persona's perspective, consulting the SLE's SOUL.md
file for:

- **Activation phrase**: A perspective-setting prompt prepended to the
  research task
- **Data source priority**: Which sources to check first, in order of
  authority
- **Analytical lens**: The mental models to apply (e.g., the
  `crypto-forensics-analyst` thinks in terms of on-chain vs. off-chain,
  wash trading red flags, and regulatory arbitrage)
- **Bias check**: The SLE's documented blind spots are explicitly reviewed
  against findings before the capsule is published

### 7.3 The Roster and Dispatch Matrix

| # | SLE | Primary Sectors | Confidence Impact |
|---|-----|----------------|-------------------|
| 1 | `payments-network-analyst` | Payments | High — covers #1 TPS category |
| 2 | `central-bank-economist` | Payments, Banking | High — covers #3 and #5 |
| 3 | `market-microstructure-analyst` | Traditional Finance | Medium — ETD, equities |
| 4 | `post-trade-specialist` | Banking, TradFi | Medium — settlement, clearing |
| 5 | `fixed-income-specialist` | Traditional Finance | High — lowest-confidence TradFi |
| 6 | `forex-specialist` | Traditional Finance | High — genuinely opaque |
| 7 | `crypto-forensics-analyst` | Digital Assets | High — wash trading uncertainty |
| 8 | `digital-wallets-analyst` | Payments | High — covers #2 TPS category |
| 9 | `market-research-analyst` | Cross-cutting | Critical — overlap arbiter |
| 10 | `government-statistician` | Government | Medium |
| 11 | `gaming-economy-analyst` | Gaming | Low |
| 12 | `emerging-tech-forecaster` | Emerging | High — lowest-confidence categories |
| 13 | `rwa-tokenisation-analyst` | Digital Assets, TradFi | Medium |
| 14 | `market-sizing-specialist` | Cross-cutting (methodology) | Critical |
| 15 | `measurement-standards-expert` | Cross-cutting (methodology) | Critical |
| 16 | `statistical-methodologist` | Cross-cutting (methodology) | Critical |
| 17 | `transaction-lifecycle-analyst` | Cross-cutting (MEST) | Critical |

The last four SLEs (#14-17) are **methodology specialists**. They are not
assigned to specific categories but are available as secondary or panel
reviewers for any category. They are deployed in three scenarios:

1. **Mandatory panel review**: Any category contributing > 5% of global TPS
   or scoring below 50 on confidence
2. **Recommended review**: Any category where top-down and bottom-up diverge
   by > 25%
3. **On request**: When a category SLE flags uncertainty

### 7.4 Bias Documentation

Every SLE has documented biases that serve as adversarial checks:

| SLE | Known Bias | Mitigation |
|-----|-----------|-----------|
| `payments-network-analyst` | Over-emphasizes card networks; may under-count alternative rails | Cross-check with `central-bank-economist` for bank transfer volumes |
| `crypto-forensics-analyst` | Skeptical of exchange-reported volumes; may over-estimate wash trading | Bound wash estimates with academic literature ranges |
| `market-microstructure-analyst` | Focuses on lit exchanges; may under-count dark pool volume | Cross-check with FINRA TRF data for US; MiFID RTS 27 for EU |
| `emerging-tech-forecaster` | Optimism bias toward emerging categories | Anchor to current measurable data, not projections |
| `central-bank-economist` | Conservative; may under-estimate non-traditional payment flows | Cross-check with `digital-wallets-analyst` for mobile payment volumes |

These biases are not bugs — they are features. A crypto-skeptic
forensics analyst and a card-network-centric payments analyst, when
applied to the same data, produce a natural triangulation. The
`market-research-analyst` SLE serves as the arbiter when perspectives
conflict.

---

## 8. Limitations

### 8.1 Structural Blind Spots

**Cash transactions**: The largest blind spot in the Universe of Finance.
Cash is invisible to financial infrastructure measurement. ATM withdrawals
(1,557 TPS) are the only cash-adjacent metric we capture — they measure
cash creation, not cash spending. Global cash-in-circulation suggests
trillions in annual cash transactions that are entirely untracked.

**Informal economy**: Hawala networks, informal remittances (estimated
30-50% of total), cash wages, and unrecorded barter are not captured. The
World Bank estimates formal remittances at $860B; the informal channel
could be $250-430B more.

**Private markets**: Private equity transactions, private debt, and venture
capital are not included. These are low-frequency, high-value events that
would add negligible TPS but represent significant economic activity.

**Enterprise/private blockchain**: Permissioned blockchain networks
(Hyperledger, R3 Corda, JPMorgan Onyx) process an unknown number of
transactions. These are not captured in L1/L2 public blockchain data.

### 8.2 Methodological Limitations

**Snapshot vs. continuous measurement**: All figures are 2025 estimates
based on the most recent available data for each category. Financial TPS is
growing ~20% annually (gross), so these numbers age quickly. The time-series
(2015-2025) provides historical context but does not constitute real-time
monitoring.

**Transaction count vs. economic value**: TPS counts treat a $2 coffee
purchase and a $500M repo trade identically. The Big Number measures
throughput, not economic significance. A value-weighted metric would tell a
very different story (Fixed Income at ~$800T annual value vs. ~10.5 TPS;
Consumer Cards at ~$40T vs. 24,501 TPS).

**MEST multipliers are estimates**: Per-category multipliers are
order-of-magnitude assessments based on transaction lifecycle analysis, not
instrumented measurements. No financial institution publishes "bilateral
state changes processed per day." The multipliers are validated against
available proxy data (message counts, settlement instructions) but carry
inherent uncertainty.

**Average TPS vs. actual load**: The Big Number divides annual transactions
by seconds in a year (or effective trading hours for market categories).
This produces an average TPS that smooths over intraday, weekly, and
seasonal variation. Peak TPS (estimated at 147,000-246,000 during
coordinated stress events) is 2-3x the average.

### 8.3 Known Biases and Mitigations

| Bias | Direction | Mitigation |
|------|-----------|-----------|
| Developed-market data dominance | Over-represents US/EU/Japan | India, China, Brazil deep dives; GDP-weighted extrapolation for ROW |
| Card network transparency | Over-represents card payments | BIS Red Book provides bank transfer cross-check; PBOC for China |
| English-language source bias | Under-represents China, Japan, Korea | PBOC data (translated), JPX bilingual reports, BOK data |
| Survivorship bias in crypto | Over-represents major CEXs | Tiered wash model includes lower-tier exchanges |
| Regulatory reporting bias | Over-represents regulated segments | Informal economy explicitly flagged as blind spot |

---

## 9. Reproducibility

### 9.1 Structured Data

All category data is stored in structured JSON format (`data.json` per
category) following a normalized schema validated by `tools/validate_schema.py`
(29/29 categories passing). The schema includes:

- Category metadata (name, sector, confidence score)
- Transaction volume (annual, TPS, with ranges)
- Overlap deductions (percentage and absolute)
- Data sources with URLs and freshness dates
- MEST multiplier and cascade summary
- Time-series data (2015-2025)

### 9.2 Tooling

| Tool | Purpose |
|------|---------|
| `tools/big_number.py` | De-duplicated global TPS calculator — reads all 29 data.json files and applies overlap matrix |
| `tools/confidence_score.py` | 0-100 confidence scoring engine — applies the 4-dimension rubric programmatically |
| `tools/validate_schema.py` | Schema validator — ensures all 29 data.json files conform to the normalized schema |
| `tools/data_freshness.py` | Source staleness detector — flags data points approaching or past their freshness tier |
| `tools/charts.py` | Visualization suite — generates 4 chart types for the dashboard |
| `tools/normalize_schemas.py` | Migration tool — normalizes data.json files when the schema evolves between runs |

### 9.3 Version History

All research is versioned through Git. Each research run is a discrete
commit set, enabling:

- Full diff between any two runs
- Attribution of every data change to a specific run and rationale
- Rollback capability if a run introduces errors

The project has completed 11 research runs (March 2026), each with a
documented focus area, key outputs, and changes to the Big Number.

### 9.4 Open Source Licensing

- **Research outputs** (all Markdown, JSON, analysis): **CC BY 4.0** —
  free to use, share, and adapt with attribution
- **Code** (tools, scripts): **MIT License** — free to use for any purpose

Suggested citation:

> Universe of Finance Project. "Global Financial Transaction Throughput:
> ~73,750 TPS and ~545,000 MEST/s." Working paper, March 2026.

---

## 10. References

### Central Banks and Regulators

- **BIS CPMI Red Book** — Committee on Payments and Market Infrastructures.
  *Statistics on payment, clearing and settlement systems.* Bank for
  International Settlements. Updated annually.
  https://www.bis.org/cpmi/publ/d00b.htm

- **BIS Triennial Survey** — *Triennial Central Bank Survey of Foreign
  Exchange and Over-the-counter Derivatives Markets.* Bank for International
  Settlements, 2022.
  https://www.bis.org/statistics/rpfx22.htm

- **PBOC** — People's Bank of China. *Payment System Overall Operation
  Report.* Published annually (in Chinese; translated data used).

- **ECB Payment Statistics** — European Central Bank. *Statistical Data
  Warehouse: Payments Statistics.* Updated annually.
  https://sdw.ecb.europa.eu/

- **RBI Annual Report** — Reserve Bank of India. Chapter on Payment and
  Settlement Systems. Published annually.
  https://www.rbi.org.in/

### Industry Associations

- **Nilson Report** — *Global Network Card Results Worldwide.* Nilson
  Report, 2024. (Paywalled; secondary reporting by Digital Transactions,
  Payments Journal.)

- **FIA Annual Survey** — Futures Industry Association. *Annual Volume
  Survey: Global Exchange-Traded Derivatives.* Published annually.
  https://www.fia.org/

- **WFE Monthly Dashboard** — World Federation of Exchanges. *Monthly
  Market Statistics.* Published monthly.
  https://www.world-exchanges.org/

- **SWIFT** — *SWIFT Annual Review.* Society for Worldwide Interbank
  Financial Telecommunication. Published annually.

- **CLS Group** — *CLS FX Volume Data.* Published monthly.
  https://www.cls-group.com/

- **DTCC** — Depository Trust & Clearing Corporation. *Annual Report.*
  Published annually.

### Public Company Filings

- **Visa Inc.** — *Form 10-K.* United States Securities and Exchange
  Commission. Fiscal year ending September.

- **Mastercard Inc.** — *Form 10-K.* SEC. Calendar year.

- **Coinbase Global Inc.** — *Form 10-K.* SEC. Calendar year.

- **PayPal Holdings Inc.** — *Form 10-K.* SEC. Calendar year.

### Market Data and Research

- **CoinGecko** — Cryptocurrency market data. Trust-scored exchange volumes.
  https://www.coingecko.com/

- **Kaiko** — Institutional crypto market data. Microstructure analysis.
  https://www.kaiko.com/

- **McKinsey & Company** — *Global Payments Report.* Published annually.

- **Swiss Re sigma** — *World Insurance.* Swiss Re Institute. Published
  annually.

- **Newzoo** — *Global Games Market Report.* Published annually.

### Academic Research

- **Cong, L.W., et al.** (2022). "Crypto Wash Trading." *NBER Working
  Paper.* National Bureau of Economic Research.

- **Kocenda, E., et al.** (2024). "Crypto Exchanges and Market
  Manipulation." *CEPR Discussion Paper.* Centre for Economic Policy
  Research.

### National Payment Systems

- **NPCI** — National Payments Corporation of India. UPI and RuPay
  statistics. https://www.npci.org.in/

- **BCB** — Banco Central do Brasil. Pix statistics.
  https://www.bcb.gov.br/

- **NPCI FasTag** — Toll collection data (IoT segment).

- **Fedwire** — Federal Reserve. Fedwire Funds Service statistics.
  https://www.frbservices.org/

### Other

- **World Bank** — *Remittance Prices Worldwide* and *Global Findex
  Database.* Published periodically.
  https://www.worldbank.org/

- **Visa OnChain Analytics** — Stablecoin transfer volume tracking.
  https://usa.visa.com/solutions/crypto.html

---

*This methodology paper accompanies the Universe of Finance research project.
It describes methods as of Run 11, March 2026. The methodology evolves with
each research run — see individual capsule METHODOLOGY.md files and the
Git commit history for run-specific changes.*

*Research outputs: CC BY 4.0. Code: MIT.*

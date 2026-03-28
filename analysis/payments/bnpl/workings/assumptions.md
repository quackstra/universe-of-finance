# Buy Now Pay Later (BNPL) — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. Provider-Level Data as Primary Source
**Assumption:** Individual BNPL provider disclosures (SEC filings, investor presentations) are the most reliable data source for this category.
**Reasoning:** Unlike cards (Nilson) or bank transfers (central banks), there is no industry-level aggregator for BNPL. The top 5 Western providers are publicly traded and disclose GMV, active users, and transaction metrics.
**Risk:** Provider metrics are not standardized — "transaction" can mean purchase event or installment event depending on the provider. We assume Klarna's "2.5M transactions/day" is at the purchase level based on context.

### A2. China BNPL Estimation
**Assumption:** Ant Group's Huabei and JD's Baitiao collectively process ~2B BNPL-equivalent purchases annually with ~$150B GMV.
**Reasoning:** Ant Group's "credit tech" revenue (~$4.5B) at 0.5-1% implied take rate suggests $450-900B total credit facilitation. Huabei is a revolving credit line, not strictly BNPL, so we discount to ~$150B for BNPL-equivalent installment purchases.
**Risk:** This could be wildly wrong in either direction. China's BNPL market operates differently from Western models and disclosure is minimal. Range: 1-4B purchases.

### A3. "Other" Provider Estimation
**Assumption:** The long tail of 50+ regional BNPL providers collectively represents ~$74B GMV and ~1.1B purchases.
**Reasoning:** Estimated at ~16% of total GMV, consistent with market concentration patterns in payments (top 5-6 players typically capture 80-85% of a category).
**Risk:** Could be higher if Middle East (Tabby, Tamara) and Southeast Asia (Atome, hoolah, Kredivo) are growing faster than estimated.

---

## Transaction Counting Assumptions

### A4. Installment Multiplier of 3.6x
**Assumption:** Each BNPL purchase generates an average of 3.6 payment events (including the initial payment).
**Reasoning:** Weighted average across models: 60% "Pay in 4" (4.0x), 15% "Pay in 3" (3.0x), 15% longer-term (avg 8x), 10% pay-after-delivery (1.0x). Including ~5% for payment failures and retries.
**Risk:** The model mix is uncertain. If "Pay in 4" has higher share (70%+), the multiplier is closer to 3.8x. If longer-term installment plans grow faster, it could exceed 4.0x.

### A5. Each Installment = One Transaction
**Assumption:** Every installment debit from a consumer's bank account or card counts as one transaction, regardless of whether the original purchase was one event.
**Reasoning:** Each installment generates a real payment event on underlying rails — a card charge, an ACH debit, or a direct debit. These are real infrastructure transactions.
**Risk:** Some BNPL providers batch installment processing (multiple installments from multiple customers in one batch). At the infrastructure level, this could mean fewer actual payment messages than individual installments. Impact: likely <10% overcounting.

### A6. Merchant Payment Timing
**Assumption:** The merchant receives a single payment at or near purchase time (funded by the BNPL provider), not in installments.
**Reasoning:** This is the standard BNPL model — the provider pays the merchant upfront (minus discount fee) and collects installments from the consumer. The merchant payment is not counted separately to avoid triple-counting.
**Risk:** Some models (pay-after-delivery) may delay merchant payment until consumer confirms receipt.

---

## Overlap Assumptions

### A7. 100% Infrastructure Overlap
**Assumption:** Every BNPL installment payment flows through an existing payment rail (card or bank transfer).
**Reasoning:** BNPL providers do not operate their own payment infrastructure. Klarna debits consumer bank accounts (via ACH/SEPA DD) or charges cards on file. Affirm offers virtual card numbers processed on Visa/MC rails.
**Risk:** None — this is definitionally true. BNPL is an application-layer product, not a payment rail.

### A8. Net Incremental Transactions = 2.6x
**Assumption:** Each BNPL purchase creates 2.6 net new transactions on underlying rails compared to the counterfactual (paying in full with one transaction).
**Reasoning:** Average installments (3.6) minus the one transaction that would have occurred anyway = 2.6 net new.
**Risk:** The counterfactual assumes the consumer would have purchased the item with a single payment. In reality, some BNPL purchases would not have occurred at all without BNPL (incremental demand). This means the "net new" could be higher (all 3.6 installments are truly incremental) for some fraction of purchases.

---

## Projection Assumptions

### A9. Baseline Growth Trajectory
**Assumption:** BNPL purchase count grows at 12-15% CAGR (2025-2030), slowing to 9-10% (2030-2035).
**Reasoning:** Category is transitioning from hyper-growth to mainstream. Comparison: digital wallets went from 40%+ growth (2015-2019) to 15-20% (2020-2024) as they matured.
**Risk:** Regulatory risk (EU CCD implementation 2026, CFPB rules) could slow growth below baseline. Conversely, in-store BNPL adoption could sustain higher growth.

### A10. Conservative Regulatory Impact
**Assumption:** In the conservative scenario, BNPL regulation as full credit products (requiring creditworthiness assessments) reduces growth to 5-8%.
**Reasoning:** The EU Consumer Credit Directive 2023/2225 (effective 2026) will require BNPL providers to conduct affordability checks. CFPB interpretive rule classifies BNPL as credit cards. These add friction to the checkout flow.
**Risk:** Regulation may be less impactful than feared — providers have adapted to UK FCA regulation with minimal growth impact.

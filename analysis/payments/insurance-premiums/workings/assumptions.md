# Insurance Premium Payments — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. Swiss Re sigma as Primary Premium Source
**Assumption:** Swiss Re's sigma research series is the most authoritative source for global insurance premium volumes.
**Reasoning:** Swiss Re sigma has been the industry standard for global insurance market sizing for decades. Their methodology is consistent, well-documented, and widely cited by regulators (IAIS, NAIC) and industry bodies.
**Risk:** Swiss Re figures are gross written premiums (GWP), which can include some double-counting for reinsurance. However, GWP is the right measure for premium payment analysis since it reflects actual premium flows from policyholders.

### A2. No Authoritative Transaction Count Source
**Assumption:** No single source publishes global insurance premium transaction counts. All transaction estimates are modeled bottom-up.
**Reasoning:** Unlike card payments (Nilson) or real-time payments (ACI), insurance premium payments are processed across fragmented rails (direct debit, cards, ACH, cash) and no industry body aggregates the total.
**Risk:** The bottom-up model relies on policy count estimates and payment frequency assumptions, both of which are uncertain. The 12-16B range reflects this uncertainty.

### A3. Policy Count Estimates
**Assumption:** Global policies in force total approximately 6.7 billion across all segments.
**Reasoning:** Built from vehicle registrations (OICA), health coverage (WHO/national data), property insurance penetration, and life insurance in-force data (Swiss Re).
**Risk:** Double-counting is possible (a person with auto + home + life = 3 policies). This is intentional — each policy generates its own payment stream.

---

## Payment Frequency Assumptions

### A4. Auto Insurance Payment Frequency
**Assumption:** 70% of auto policies are paid monthly; 30% are paid annually.
**Reasoning:** US data shows ~65-70% monthly billing (Progressive, GEICO quarterly/monthly plans dominate). Europe varies — UK is predominantly annual, continental Europe is more varied.
**Risk:** The global average could be lower (more annual billing in Europe/Asia) or higher (more monthly in US/LatAm). Range: 60-80% monthly.

### A5. Health Insurance Payment Frequency
**Assumption:** 60% monthly premiums, 40% per-claim copay events. Only private/supplemental health insurance counted (public single-payer excluded).
**Reasoning:** In markets with private health insurance (US, Germany, Switzerland, parts of Asia), monthly premium billing is standard. Copay events are less regular.
**Risk:** The 2.5B "covered lives" figure is generous — many are covered by employer-paid or government-paid schemes with no consumer-facing premium payment. The 75% adjustment for public systems may be too low or too high.

### A6. Life Insurance Payment Frequency
**Assumption:** 50% monthly, 20% quarterly, 30% annual. With 55% adjustment for group/employer-paid and 50% for lapsed policies.
**Reasoning:** Individual life policies typically have monthly premium billing in the US and quarterly/annual in other markets. Group life is employer-paid (no consumer transaction).
**Risk:** The lapse rate is the biggest uncertainty. Swiss Re estimates that 25-50% of life policies lapse within 10 years, but the "in force" figure should already exclude lapsed policies. The 50% lapse adjustment may be too aggressive.

### A7. Payment Failure and Retry Rate
**Assumption:** 5% of premium payment attempts fail and are retried, generating additional transactions.
**Reasoning:** Industry data from NACHA shows 2-3% ACH return rates for insurance debits. Card payment failure rates are similar. Adding retries brings total to ~5%.
**Risk:** This could be higher in emerging markets (insufficient funds more common) or lower in markets with robust auto-debit systems.

---

## TPS Calculation Assumptions

### A8. Even Distribution Over Year
**Assumption:** Transactions are distributed roughly evenly across the year for average TPS calculation, with peak adjustment for month-start clustering.
**Reasoning:** Insurance premium due dates are spread across the year (not all policies renew in January). However, monthly premiums cluster on the 1st and 15th.
**Risk:** The 1.6x peak multiplier may underestimate actual peak — on a single processing day (e.g., first business day of the month), the ratio could be 5-10x the daily average.

---

## Overlap Assumptions

### A9. Payment Channel Distribution
**Assumption:** 45% direct debit, 25% card, 15% bank transfer, 10% cash/check, 5% digital wallet.
**Reasoning:** Based on US and European payment mix for insurance premiums. US skews more card-heavy; Europe skews more direct debit-heavy; emerging markets skew more cash-heavy.
**Risk:** The global average is uncertain. In India, a significant share is still cash-collected by agents. In China, Alipay/WeChat Pay for insurance premiums is growing rapidly but volume is unclear.

### A10. 90% Overlap with Existing Rails
**Assumption:** 90% of insurance premium transactions are already counted in other payment capsules (cards, bank transfers, digital wallets).
**Reasoning:** Direct calculation from channel distribution: 45% + 25% + 15% + 5% = 90%.
**Risk:** If cash collection is higher than estimated (especially in Africa, India, SE Asia), the overlap could be lower (80-85%).

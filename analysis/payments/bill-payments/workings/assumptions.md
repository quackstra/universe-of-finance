# Bill Payments — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Scope Assumptions

### A1. Insurance Exclusion
**Assumption:** Insurance premium payments are excluded from this capsule.
**Reasoning:** Insurance premiums have their own dedicated capsule (insurance-premiums). Including them here would double-count.
**Risk:** None — this is a definitional choice, not an uncertainty.

### A2. Loan Repayments Excluded
**Assumption:** Mortgage payments, auto loan payments, student loan payments, and other debt servicing are excluded.
**Reasoning:** These are capital market / lending transactions, not "bill payments" in the service-provider sense. They will be covered in a separate capsule.
**Risk:** The boundary is somewhat arbitrary — a monthly mortgage payment feels very "bill-like." But the underlying economics (debt amortization vs. service consumption) are different.

### A3. Prepaid Top-Ups as Bill Payments
**Assumption:** Regular prepaid mobile top-ups are counted as bill payments when they recur monthly.
**Reasoning:** In many emerging markets, prepaid mobile is the functional equivalent of postpaid billing — consumers top up regularly to maintain service. The payment behavior is bill-like.
**Risk:** This blurs the line between "bill payments" and "retail purchases." One-off ad-hoc top-ups are not counted; only regular recurring patterns.

---

## Account Count Assumptions

### A4. Global Electricity Accounts
**Assumption:** ~2.5 billion electricity billing accounts globally (2.3B residential + 0.2B commercial).
**Reasoning:** IEA: 8.0B people with electricity access / 3.5 avg household size = 2.3B households. Adding commercial accounts (~10%).
**Risk:** Household size varies dramatically (1.5 in Scandinavia, 5+ in Sub-Saharan Africa). Using a global average of 3.5 is a significant simplification. The actual number of billing accounts could be 2.0-3.0B.

### A5. Global Mobile Connections
**Assumption:** 5.5 billion mobile connections generating ~18B bill-like payment transactions annually.
**Reasoning:** GSMA: 5.5B connections (excl. IoT). Converting to payment transactions requires accounting for postpaid/prepaid split, family plans, and multi-SIM users. See calculations.md for full derivation.
**Risk:** The conversion from "connections" to "unique payment events" involves several uncertain steps. The 18B figure could be 15-25B.

### A6. Digital Subscription Count
**Assumption:** ~910M paying digital subscriptions (after excluding free trials and bundled subs), generating ~10B annual billing events.
**Reasoning:** Top streaming services total ~1.3B subscriptions, but ~30% are free/bundled. Net paying = ~910M. At 12 monthly charges = ~10.9B, rounded to 10B.
**Risk:** This likely undercounts by excluding gaming subscriptions (Game Pass, PS Plus: ~200M) and consumer SaaS (iCloud, Google One: ~500M). True total may be 12-15B.

### A7. Renter Households
**Assumption:** ~700M renter households globally, of which ~40% make digitally trackable rent payments.
**Reasoning:** US Census (44M renters), Eurostat (70M), with estimates for China (200M), India (80M), ROW (300M). Digital rent payment is growing but still minority in most markets.
**Risk:** This is one of the weakest assumptions. Informal rental markets (no lease, cash-only) are enormous in developing countries. The actual number of "renter households" may be much higher, but with very low digital payment rates.

---

## Payment Frequency Assumptions

### A8. Monthly Billing Dominance
**Assumption:** Most bill payments occur monthly (70-80% of total transactions).
**Reasoning:** Utilities, telecoms, subscriptions, and rent are predominantly monthly-billed in most markets. Exceptions: UK water (quarterly), some commercial utilities (quarterly), and annual insurance (excluded).
**Risk:** Low — monthly billing is well-established. The bigger uncertainty is within the monthly cadence (which day of the month, affecting peak TPS).

### A9. Prepaid Utility Top-Up Frequency
**Assumption:** Prepaid electricity users in Sub-Saharan Africa top up ~6 times per year on average.
**Reasoning:** Prepaid meter users buy credit in small amounts when affordable. Studies in South Africa and Kenya show 4-8 top-ups per year, with significant variation by income.
**Risk:** This affects the ~3B prepaid electricity figure. Could be 2-5B depending on actual top-up frequency.

---

## Value Assumptions

### A10. Average Payment Amounts
**Assumption:** Average bill amounts by segment as listed in REPORT.md (electricity $70, gas $60, water $35, etc.).
**Reasoning:** Based on US and European average bill data, adjusted downward for global weighting (emerging market bills are significantly lower).
**Risk:** Averages mask enormous variation. A US electricity bill ($130/month) is very different from an Indian electricity bill ($10/month). The global average is a rough midpoint.

---

## Overlap Assumptions

### A11. 90% Overlap with Existing Payment Rails
**Assumption:** 90% of bill payments are already counted in Consumer Cards, Bank Transfers, or Digital Wallets capsules.
**Reasoning:** Direct debit (40%) + card-on-file (25%) + bank transfer (15%) + mobile money (10%) = 90%.
**Risk:** If cash bill payment is higher than 10% (plausible in Africa, South Asia), overlap drops to 80-85%. This would increase incremental TPS.

### A12. Direct Debit Share
**Assumption:** 40% of bill payments are via direct debit / auto-pay.
**Reasoning:** UK BACS data shows ~60% of consumer bills are direct debit. US is lower (~30-35% for utilities). Europe is higher (~50-60%). Global weighted average ~40%.
**Risk:** This is a reasonable central estimate. The trend is strongly toward higher auto-pay adoption, so 40% may be conservative for 2024.

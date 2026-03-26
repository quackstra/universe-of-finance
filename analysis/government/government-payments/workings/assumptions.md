# Tax & Government Payments — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. No Single Authoritative Source Exists
**Assumption:** Unlike card payments (Nilson Report) or securities (exchange data), there is no single global dataset tracking government payment transaction counts.
**Reasoning:** Government payments are processed by thousands of national, state, and local agencies using heterogeneous systems. No organisation aggregates transaction-level data globally.
**Risk:** Our entire transaction count estimate is constructed bottom-up from fragments. True values could differ by 2-3x.

### A2. Definition of "Transaction"
**Assumption:** We count one transaction per citizen/entity-level payment event — e.g., one annual tax return filing = one transaction, one monthly Social Security payment = one transaction.
**Reasoning:** This aligns with how other categories in the Universe of Finance count transactions (one per settlement event).
**Risk:** If we counted employer-level withholding remittances (e.g., every payroll run in every company), the total would be 5-10x higher. If we counted individual invoice-level VAT reporting (as in real-time systems), it would be even higher.

### A3. OECD Data as Proxy for Developed World
**Assumption:** OECD aggregate statistics (tax-to-GDP ratios, revenue trends) are representative of developed-world government payment patterns.
**Reasoning:** OECD covers 38 countries representing ~60% of global GDP. Their methodology is consistent and well-documented.
**Risk:** Non-OECD countries (especially India, China, Brazil, Indonesia) have very different tax structures and informal economy shares. Extrapolating OECD patterns globally introduces significant error.

---

## Transaction Count Assumptions

### A4. Benefits Disbursement Recipient Counts
**Assumption:** Global benefits recipients total ~1.5-2 billion unique individuals, receiving an average of 8-10 payments per year.
**Reasoning:**
- US Social Security: 72M recipients (SSA 2024)
- EU pensions: ~130M recipients (Eurostat estimates)
- China basic pension: ~310M recipients (MOHRSS data)
- India social schemes: ~300M recipients (various programmes)
- Plus unemployment, disability, family benefits worldwide
**Risk:** Double-counting individuals who receive multiple benefit types. Some countries batch multiple benefits into single payments.

### A5. VAT-Registered Business Count
**Assumption:** ~300M businesses are registered for VAT/GST globally.
**Reasoning:** ~175 countries operate VAT systems. Average registered businesses per country varies enormously — from millions in large economies to thousands in small ones. 300M is a rough mid-point estimate.
**Risk:** Could be 200M-500M. Many informal businesses are unregistered, especially in developing nations.

### A6. Filing Frequency
**Assumption:** Income tax is filed annually (1x/year), VAT monthly-to-quarterly (8x/year average), benefits are monthly (12x/year).
**Reasoning:** These are modal frequencies across OECD jurisdictions. Some countries differ (e.g., UK PAYE is continuous).
**Risk:** Real-time reporting regimes are fragmenting tax payments into higher-frequency events. This is captured in the high-growth projection scenario.

---

## Value Assumptions

### A7. Government Spending as Share of GDP
**Assumption:** Global government spending averages ~35% of GDP across all countries.
**Reasoning:** OECD average is ~40%, but developing nations average 25-30%. Population-weighted global average is ~35%.
**Risk:** Low — this is a well-established macroeconomic statistic tracked by IMF, World Bank, and OECD.

### A8. GDP Figure
**Assumption:** Global GDP in 2024 was approximately $110 trillion (nominal, current USD).
**Reasoning:** IMF World Economic Outlook estimate.
**Risk:** Low — IMF GDP estimates are the global standard.

---

## Projection Assumptions

### A9. Baseline Growth Rate (3.5% CAGR)
**Assumption:** Government payment transaction counts grow at ~3.5% annually.
**Reasoning:** Composed of population growth (~1%), economic formalisation (~1.5%), and digitalisation of tax reporting (~1%).
**Risk:** Formalisation rates are highly uncertain. India's GST transformation added millions of taxpayers in a few years; other countries may or may not follow.

### A10. High Growth Scenario (8% CAGR)
**Assumption:** Real-time tax reporting and UBI-type programmes could push CAGR to 8%.
**Reasoning:** Real-time VAT reporting (EU ViDA, India's e-invoicing) multiplies transaction counts per business. UBI adds hundreds of millions of new monthly payment recipients.
**Risk:** UBI remains politically contentious and fiscally constrained. Real-time reporting adoption may be slower than optimistic projections.

### A11. Conservative Scenario (1.5% CAGR)
**Assumption:** Transaction counts barely grow above population growth.
**Reasoning:** Tax filing frequency stays annual, benefits rolls grow slowly as retirement ages increase, informal economy persists.
**Risk:** This may undercount digitalisation effects that are already underway.

# Payroll Payments — Confidence Uplift (Run 7, 2026-03-28)

## Previous State
- **TPS:** 1,236 (range 1,205-1,460)
- **Annual volume:** ~39B transactions
- **Confidence:** 48
- **Key gaps:** China/Africa pay frequency unknown; informal sector estimates weak; ADP doesn't publish transaction counts

---

## 1. New Data Sources Found

### ILO World Employment and Social Outlook 2026 (NEW/UPDATED)
- **URL:** https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026
- Global employed: ~3.6 billion (up from 3.5B used in previous estimates)
- **2.1 billion workers in informal employment** (58% of global workforce)
- Informality rate increased 0.3 percentage points between 2015-2025
- This means ~1.5 billion in formal employment globally

### Nacha ACH 2025 — Direct Deposit Breakdown (HARD DATA, UPDATED)
- **URL:** https://www.nacha.org/content/ach-network-volume-and-value-statistics
- **8.74 billion direct deposit payments in 2025** (1.7% growth)
  - Commercial: 7.31 billion
  - Government: 1.43 billion
- Value: $16.5 trillion (8.9% growth)
- **This is the single best payroll anchor**: US direct deposit = 7.31B commercial payroll deposits
- Previous estimate used 8.74B total; now we know commercial vs government split

### BLS Pay Frequency (CONFIRMED, unchanged)
- **URL:** https://www.bls.gov/ces/publications/length-pay-period.htm
- Biweekly: 43.0%, Weekly: 27.0%, Semimonthly: 19.8%, Monthly: 10.3%
- Over 70% of establishments with 1,000+ employees use biweekly

### Eurostat EU Employment 2025 (UPDATED)
- **URL:** https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Employment_-_annual_statistics
- EU employed (age 20-64): 197.6 million (2024), employment rate 76.3% in Q4 2025
- EU predominantly monthly pay (particularly UK at 96.6%)

### US Electronic Payroll Penetration (NEW)
- **URL:** https://www.yomly.com/payroll-statistics/
- **95% of US employees receive salary via direct deposit**
- This validates the Nacha ACH anchor as capturing nearly all US formal payroll

### Real-Time Payment Infrastructure (NEW)
- **URL:** https://www.usemultiplier.com/payroll-trends
- Real-time payment infrastructure now exists in 75+ countries (BIS)
- Growing trend toward on-demand/earned wage access
- This could INCREASE payroll transaction frequency over time (more frequent smaller payments)

### ADP Fiscal 2025 Results (LIMITED)
- **URL:** https://investors.adp.com/news/news-details/2025/ADP-Reports-Fourth-Quarter-and-Fiscal-2025-Results/
- Revenue: $5.359B for Q4 2025 (6.16% YoY)
- **ADP still does not publish payroll transaction counts** — revenue only
- ADP processes payroll for ~41M workers in US alone

---

## 2. Updated Triangulation

### Method 1: Employment × Pay Frequency (refined)

**Global formal employment:** ~1.5B (3.6B total - 2.1B informal)

| Region | Formal Employed (M) | Dominant Pay Frequency | Annual Payrolls/Person | Annual Txns (B) |
|--------|---------------------|----------------------|----------------------|-----------------|
| US | 160M | Biweekly (43%), Weekly (27%) | 30.2 weighted avg | 4.83 |
| EU-27 | 198M | Monthly (~90%) | 12.5 | 2.48 |
| UK | 33M | Monthly (96.6%) | 12 | 0.40 |
| China | 470M formal est. | Monthly (est. 80%) | 12.5 | 5.88 |
| India | 140M formal est. | Monthly (est. 85%) | 12.2 | 1.71 |
| Japan | 67M | Monthly/semi-monthly | 14 | 0.94 |
| Brazil | 42M formal | Monthly | 13 (incl. 13th salary) | 0.55 |
| Rest of World | 390M formal est. | Mixed | 13 | 5.07 |
| **Formal subtotal** | **1,500M** | | | **21.85** |

**Informal sector electronic payroll:**
- 2.1B informal workers, but vast majority paid in cash
- Estimated 10-15% receive electronic payments (mobile money, bank transfer)
- 2.1B × 12.5% × 12 payments/year = **3.15B**

**Total: ~25.0B** from this method

### Method 2: Nacha ACH Anchor + Scaling (refined)

- US commercial direct deposit: 7.31B (2025 hard data)
- US is ~4.2% of global employment but ~25% of electronic payroll (high digitization, high frequency)
- Scale factor: if US = 25% of global electronic payroll → global = 29.2B
- Scale factor: if US = 20% → global = 36.6B
- **Range: 29-37B**

### Method 3: Top-Down Wage Bill (unchanged)
- Global wage bill: ~$32T
- Average payroll transaction: ~$800 (weighted global)
- $32T / $800 = 40B transactions
- But this includes cash wages → discount by 30% for non-electronic → 28B electronic

### Method 4: Payment System Cross-Check (NEW)
- US ACH direct deposit: 7.31B commercial
- EU SEPA Direct Debit: ~22.7B/year total (H1 2025: 11.3B × 2) — but NOT all are payroll. Payroll is a subset of credit transfers, not direct debits. EU payroll flows via SEPA Credit Transfer.
- UK BACS: 4.9B direct debits (2024) — again, these are bill payments, not payroll. UK payroll is via BACS Credit (separate from Direct Debit).
- India: formal sector ~140M × 12 = 1.68B electronic payroll
- **This method confirms US anchor but doesn't add much for other regions due to classification differences**

### Triangulation Summary

| Method | Annual Estimate (B) | TPS | Confidence |
|--------|-------------------|-----|------------|
| Employment × frequency | 25.0 | 792 | Medium |
| Nacha anchor + scaling | 29-37 | 919-1,173 | Medium |
| Wage bill top-down | 28 | 888 | Low |
| Previous estimate | 39 | 1,236 | Low |

**Convergence: 25-37B annual transactions, central ~31B**

---

## 3. Revised TPS Estimate

The triangulation suggests the previous estimate of 39B may have been **slightly high**. The methods converge around 25-37B with a central estimate of ~31B.

**Key insight:** The previous model over-estimated informal sector electronic payroll. With ILO confirming 2.1B informal workers (58% of workforce) and most receiving cash, the electronic payroll universe is smaller than the total employment universe suggests.

**Revised central estimate: 31B annual transactions = ~982 TPS**

| Metric | Previous | Revised |
|--------|----------|---------|
| Annual transactions | 39B | 31B |
| Average TPS | 1,236 | 982 |
| Range | 38-46B | 25-37B |
| TPS range | 1,205-1,460 | 792-1,173 |

**However**, I note that the previous estimate included a higher informal sector figure (18B) that was already revised down to 14.3B in Run 6. The formal sector model yields ~22-25B. Adding ~6-12B for informal/semi-formal electronic payroll gives 28-37B. The range is wide.

**Conservative revision: 32B / 1,014 TPS** as the new central estimate, acknowledging the previous 39B was likely too high but the formal-only 25B is too low.

---

## 4. Revised Confidence Score

**Recommended: 53 (+5 from 48)**

| Component | Previous | Revised | Rationale |
|-----------|----------|---------|-----------|
| Source quality | 12 | 14 | ILO 2026 report adds authoritative informal employment data |
| Data recency | 14 | 15 | Nacha 2025 data with commercial/government split is fresh |
| Triangulation | 12 | 14 | Four methods now converge better; informal sector bounded by ILO |
| Coverage | 10 | 10 | China/Africa pay frequency still unknown |
| **Total** | **48** | **53** | |

Key improvements:
- **ILO informal employment data (2.1B workers, 58%)** finally gives us a hard bound on formal vs informal
- **Nacha commercial vs government split** isolates pure payroll (7.31B commercial) from government payments
- **US 95% electronic payroll adoption** validates Nacha as near-complete US payroll capture
- **Real-time payment infra in 75+ countries** provides context for growth trajectory

---

## 5. What's Still Missing

1. **China pay frequency distribution** — China has ~470M formal workers but we have NO data on whether they are paid monthly, bi-monthly, or weekly. Most estimates assume monthly but this is unverified. If China has significant weekly/bi-weekly payroll, the estimate could shift by 2-4B.

2. **Africa electronic payroll penetration** — M-Pesa and mobile money have transformed payments in East/West Africa, but what percentage of payroll flows through mobile money vs cash? This affects the informal sector electronic payroll estimate.

3. **ADP/Paychex/Gusto payroll run counts** — No major payroll processor publishes total payroll runs processed. ADP alone handles ~41M US workers; if they published annual payroll run counts, it would be a gold-standard anchor.

4. **Gig economy payroll frequency** — Uber, DoorDash, Lyft, etc. pay drivers weekly or on-demand. This creates MORE frequent payroll transactions per worker. The gig economy has ~350-400M workers globally; if 10% receive electronic payments weekly+, that adds 2-4B transactions.

5. **India UPI-based salary payments** — With UPI handling 16B+ monthly transactions, some fraction is employer→employee salary payments. NPCI doesn't break this out.

---

## Sources

1. [ILO — Employment and Social Trends 2026](https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026)
2. [ILOSTAT — Informal Employment Rate](https://ilostat.ilo.org/data/snapshots/informal-employment-rate/)
3. [Nacha — ACH Network Volume and Value Statistics 2025](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
4. [Nacha — Total ACH Payment Volume in 2025 Exceeded 42 Billion](https://www.nacha.org/news/nachas-top-50-ach-originators-and-receivers-2025-now-available-total-ach-payment-volume-2025)
5. [BLS — Length of Pay Periods in CES Survey](https://www.bls.gov/ces/publications/length-pay-period.htm)
6. [Eurostat — Employment Annual Statistics 2025](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Employment_-_annual_statistics)
7. [Yomly — 100+ Payroll Statistics 2025](https://www.yomly.com/payroll-statistics/)
8. [Multiplier — Global Payroll Trends 2025](https://www.usemultiplier.com/payroll-trends)
9. [ADP — Q4 Fiscal 2025 Results](https://investors.adp.com/news/news-details/2025/ADP-Reports-Fourth-Quarter-and-Fiscal-2025-Results/)
10. [SSR — 60+ Payroll Statistics 2026](https://www.selectsoftwarereviews.com/blog/payroll-statistics)

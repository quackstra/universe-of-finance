# Bill Payments — Source Notes

> Extended notes on each source consulted during research. Accessed 2026-03-28.

---

## Primary Sources

### 1. NACHA — ACH Network Volume and Value Statistics 2024
- **URL:** https://www.nacha.org/content/ach-network-volume-and-value-statistics
- **Key data:** ~31.5B ACH transactions in 2024; ~$80T in value; bill payments estimated at 35% of volume (~11B)
- **Reliability:** 🟢 High — NACHA operates the US ACH network; data is definitive for US ACH
- **Notes:** ACH is the backbone of US bill payment (utility auto-pay, subscription billing, rent via platforms). "Bill payments" is not a separate NACHA reporting category — the 35% estimate is derived from transaction type codes (PPD, WEB for consumer debits).

### 2. BACS Payment Schemes — Annual Report 2024 (UK Direct Debit)
- **URL:** https://www.bacs.co.uk/
- **Key data:** ~4.5B Direct Debit transactions in 2024; avg value ~GBP 250; ~100M+ on peak processing day (1st business day of month)
- **Reliability:** 🟢 High — BACS operates UK's Direct Debit system; data is definitive
- **Notes:** UK Direct Debit is one of the best-documented bill payment systems globally. ~60% of DD volumes are estimated to be consumer bill payments (energy, telecom, subscriptions, insurance, council tax). The peak-day data is invaluable for TPS modeling.

### 3. European Central Bank — Payment Statistics (SEPA Direct Debit)
- **URL:** https://www.ecb.europa.eu/stats/payment_statistics/large_value_and_retail/html/index.en.html
- **Key data:** SEPA Direct Debit: ~24B transactions in 2024; SEPA Credit Transfer: ~27B
- **Reliability:** 🟢 High — ECB collects data from all eurozone central banks
- **Notes:** SEPA DD is the primary bill payment mechanism in the eurozone. Germany alone accounts for ~50% of SEPA DD volume (historically a Lastschrift culture). Bill payments estimated at 30-35% of total SEPA DD (rest is B2B, insurance, loan repayments).

### 4. NPCI — Bharat Bill Payment System (BBPS) Statistics FY2024
- **URL:** https://www.npci.org.in/what-we-do/bharat-billpay/product-statistics
- **Key data:** 1.3B transactions processed in FY2024 (April 2023 - March 2024); +55% YoY; electricity is largest biller category
- **Reliability:** 🟢 High — NPCI is the Indian payments infrastructure operator
- **Notes:** BBPS is a centralized bill payment platform covering electricity, gas, water, telecom, DTH, broadband, insurance, and municipal taxes. It's growing explosively as India digitizes. However, BBPS volumes are still a fraction of total Indian bill payments (many still via UPI direct transfer or cash).

### 5. GSMA — The State of Mobile Internet Connectivity Report 2024
- **URL:** https://www.gsma.com/r/somic/
- **Key data:** 5.5B mobile connections (excl. IoT); ~45% postpaid; 4.6B mobile internet users
- **Reliability:** 🟢 High — GSMA is the mobile industry body; data based on operator reports
- **Notes:** The postpaid/prepaid split is critical for bill payment modeling. In developed markets, postpaid dominates (>70%); in developing markets, prepaid dominates (>70%). The shift to postpaid is a secular trend as average revenue per user increases.

### 6. ITU — Facts and Figures: Focus on Connectivity 2024
- **URL:** https://www.itu.int/en/ITU-D/Statistics/Pages/facts/default.aspx
- **Key data:** 1.5B fixed broadband subscriptions globally; 96% of world population covered by mobile network
- **Reliability:** 🟢 High — UN agency for ICT; data from national regulators
- **Notes:** Fixed broadband subscription data is well-tracked. Useful for calibrating broadband bill payment estimates.

### 7. IEA — World Energy Outlook 2024
- **URL:** https://www.iea.org/reports/world-energy-outlook-2024
- **Key data:** ~8.0B people with electricity access; 600M+ still without; residential electricity consumption patterns by region
- **Reliability:** 🟢 High — IEA is the definitive source for energy data
- **Notes:** Electricity access data is the starting point for estimating utility billing accounts. The IEA does not track billing/payment metrics — conversion from "access" to "billing accounts" requires household size assumptions.

---

## Streaming/Subscription Sources

### 8. Netflix — Q4 2024 Earnings
- **URL:** https://ir.netflix.net/ir/doc/quarterly-earnings
- **Key data:** 260M paid global subscribers (Q4 2024)
- **Reliability:** 🟢 High — SEC-filed quarterly data
- **Notes:** Largest streaming service by paid subscribers. Monthly billing is standard. Family/household plans mean actual billing events are fewer than individual viewer counts.

### 9. Spotify — Q4 2024 Earnings
- **URL:** https://investors.spotify.com/financials/quarterly-results
- **Key data:** 236M premium subscribers; 640M total MAU
- **Reliability:** 🟢 High — NYSE-listed, audited data
- **Notes:** Second-largest subscription service. 236M paid at ~$10/month avg = $28B annual revenue, consistent with billing analysis.

---

## Housing/Rent Sources

### 10. US Census Bureau — Quarterly Residential Vacancies Q4 2024
- **URL:** https://www.census.gov/housing/hvs/index.html
- **Key data:** ~44M renter-occupied housing units; homeownership rate 65.6%
- **Reliability:** 🟢 High — US Census data
- **Notes:** Definitive for US renter count. Does not track payment method or digitization.

### 11. Eurostat — Housing Statistics 2024
- **URL:** https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Housing_statistics
- **Key data:** ~70M renter households in the EU; renter share ranges from 20% (Romania) to 60% (Germany)
- **Reliability:** 🟢 High — EU statistical office
- **Notes:** Good country-level breakdown. Germany, France, and Netherlands have highest absolute renter counts.

---

## Industry Analysis Sources

### 12. ACI Worldwide — Bill Payment Trends 2024
- **URL:** https://www.aciworldwide.com/insights/expert-view
- **Key data:** Real-time bill payment adoption trends; market sizing for bill payment platforms
- **Reliability:** 🟡 Medium — ACI is a bill payment technology vendor; potential incentive to overstate market
- **Notes:** ACI processes bill payments for many US billers. Their data on US bill payment volumes is useful but may overstate digital adoption due to selection bias (their customers are digitally advanced).

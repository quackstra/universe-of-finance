# Bill Payments — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Recurring bill payments — utilities, telecoms, digital subscriptions, and rent — represent one of the highest-volume payment categories globally. We estimate **~80-110 billion bill payment transactions annually** in 2024, equivalent to **~2,536-3,488 TPS**. The central estimate is **~95 billion transactions at ~3,012 TPS**. This makes bill payments one of the largest transaction generators in the payments universe, driven by the sheer number of recurring relationships (every household has 5-15 monthly bills).

Bill payments are **overwhelmingly overlay transactions** — ~90-95% flow through direct debit, card-on-file, or bank transfer rails already counted in other capsules. The category is notable for its extreme regularity (predictable monthly spikes on the 1st/15th) and low average transaction value (~$50-80 per payment).

Insurance premiums are **excluded** from this capsule to avoid double-counting with the Insurance Premiums capsule.

## Scope

This analysis covers recurring consumer bill payments to service providers. Included: utilities (electricity, gas, water, waste), telecommunications (mobile, broadband, cable/satellite TV), digital subscriptions (streaming, SaaS, gaming), and rent payments. Excluded: insurance premiums (separate capsule), loan repayments (separate category), government taxes/fees, and one-time service payments. Each billing event where money moves from consumer to service provider = one transaction.

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~3,012 | Derived from ~95B annual ([calculations](workings/calculations.md)) | 🟡 Medium |
| Peak TPS (est.) | ~5,000-7,000 | Month-start direct debit processing peaks at 1.7-2.3x average | 🟡 Medium |
| Daily volume | ~260 million | Derived from annual total | 🟡 Medium |
| Annual transactions (2024) | ~95 billion | Bottom-up model by segment ([calculations](workings/calculations.md)) | 🟡 Medium |
| Annual value (2024) | ~$5.5-6.5 trillion | Derived from segment volumes × avg amounts | 🔴 Low |
| Avg transaction value | ~$63 | $6T / 95B txns | 🔴 Low |

### Segment Breakdown

| Segment | Global Accounts/Subs | Payment Freq | Annual Txns (B) | Avg Payment ($) | Confidence |
|---------|---------------------|-------------|-----------------|----------------|------------|
| **Utilities — Electricity** | ~2.0B accounts | Monthly | ~22B | ~$70 | 🟡 Medium |
| **Utilities — Gas** | ~0.8B accounts | Monthly (seasonal) | ~7B | ~$60 | 🟡 Medium |
| **Utilities — Water** | ~1.2B accounts | Monthly/Quarterly | ~10B | ~$35 | 🔴 Low |
| **Utilities — Waste/Other** | ~0.5B accounts | Monthly/Quarterly | ~4B | ~$25 | 🔴 Low |
| **Telecoms — Mobile** | ~5.5B subscriptions | Monthly | ~18B | ~$30 | 🟡 Medium |
| **Telecoms — Broadband** | ~1.5B subscriptions | Monthly | ~12B | ~$45 | 🟡 Medium |
| **Telecoms — Cable/Satellite TV** | ~0.8B subscriptions | Monthly | ~5B | ~$55 | 🔴 Low |
| **Digital Subscriptions** | ~2.0B active subs | Monthly | ~10B | ~$12 | 🟡 Medium |
| **Rent Payments** | ~0.6B renter households | Monthly | ~7B | ~$800 | 🔴 Low |
| **Total** | | | **~95B** | **~$63 avg** | |

### Segment Deep-Dives

#### Utilities (Electricity, Gas, Water, Waste) — ~43B transactions

Global electricity accounts: ~2 billion (IEA estimates 8 billion people with electricity access, ~3.5-4 people per household, plus commercial accounts). Monthly billing is standard in developed markets; prepaid meters are common in Sub-Saharan Africa and parts of Asia. Gas serves fewer households (~800M) due to regional availability. Water billing is highly fragmented — some markets bill monthly, others quarterly, some annually.

**Key data points:**
- UK: BACS processes ~4.5B direct debits annually, ~40% of which are utility-related (~1.8B)
- India: BBPS (Bharat Bill Payment System) processed 1.3B transactions in FY2024, growing 55% YoY
- US: ~150M utility accounts generating ~1.8B annual payments (NACHA biller data)
- EU: SEPA Direct Debit processed ~24B transactions in 2024, ~30% utility-related (~7.2B)

#### Telecoms (Mobile, Broadband, Cable) — ~35B transactions

Mobile subscriptions reached 5.5 billion globally (GSMA, excluding IoT). Not all generate monthly bill payments — prepaid plans (~55% of global mobile connections) involve top-up transactions rather than recurring bills. Of the ~2.5B postpaid connections, virtually all generate monthly payments. Prepaid top-ups (~3B active) generate irregular but frequent transactions (est. 3-4 top-ups per month in developing markets).

**Key data points:**
- GSMA: 5.5B mobile connections (excl. IoT), ~45% postpaid (~2.5B monthly bills)
- Broadband: ITU estimates 1.5B fixed broadband subscriptions globally
- For prepaid, we count monthly top-up events (~3B connections × 3 top-ups/month = ~9B, included in the mobile figure)

#### Digital Subscriptions — ~10B transactions

Digital subscriptions have exploded: Netflix (260M), Spotify (236M paid), Amazon Prime (200M+), Disney+ (150M), YouTube Premium (100M+), plus hundreds of smaller services. The average consumer in developed markets holds 3-5 digital subscriptions. Many of these are billed monthly via card-on-file.

**Key data points:**
- Netflix: 260M subscribers × 12 months = 3.1B annual billing events
- Spotify: 236M paid × 12 = 2.8B
- Top 10 streaming services alone: ~1B subscribers × 12 = ~12B, but overlap (same household) reduces unique payments to ~5-6B
- SaaS consumer subscriptions (iCloud, Google One, Microsoft 365): est. ~2B additional
- Gaming subscriptions (Xbox Game Pass, PS Plus): est. ~200M × 12 = ~2.4B

#### Rent Payments — ~7B transactions

An estimated 600 million renter households globally generate monthly rent payments. In developed markets, rent is increasingly paid digitally (bank transfer, dedicated platforms like Zelle, direct debit). In emerging markets, cash rent payment is still dominant. Digital rent payment platforms (Zillow, RentCafe, Bilt) are growing rapidly in the US.

**Key data points:**
- US: ~44M renter households, ~530M annual rent payments
- EU: ~70M renter households (Eurostat), ~840M annual payments
- China: ~200M urban renter households (est.), ~2.4B annual payments
- Global estimate highly uncertain due to informal rental markets

### Payment Channel Breakdown

| Channel | Share by Count | Share by Value | Notes |
|---------|---------------|----------------|-------|
| Direct debit / auto-pay | ~40% | ~45% | Dominant in Europe (SEPA DD), UK (BACS), growing in US |
| Card-on-file (recurring) | ~25% | ~20% | Common for digital subscriptions, US utilities |
| Bank transfer / manual | ~15% | ~20% | One-off monthly payments; common in Asia |
| Mobile money / wallet | ~10% | ~5% | Africa (M-Pesa), India (UPI), China (Alipay/WeChat) |
| Cash / in-person | ~8% | ~8% | Declining; still significant in LatAm, Africa, S. Asia |
| Check | ~2% | ~2% | US rent payments; rapidly declining |

### Regional Breakdown (2024)

| Region | Est. Txns (B) | Share | Key Systems | Notes |
|--------|--------------|-------|-------------|-------|
| Asia-Pacific | ~35B | ~37% | BBPS (India), Alipay/WeChat (China), BPAY (Australia) | Largest by volume due to population; mix of digital and cash |
| Europe | ~25B | ~26% | SEPA Direct Debit, BACS (UK), Prelevement (France) | Highest direct debit penetration |
| North America | ~18B | ~19% | ACH (NACHA), card-on-file, Zelle | High digital subscription density |
| Latin America | ~8B | ~8% | Boleto (Brazil), SPEI (Mexico) | Cash bill payment still common |
| Middle East & Africa | ~5B | ~5% | M-Pesa, JazzCash, bKash | Mobile money transforming bill payment |
| Rest of World | ~4B | ~4% | Various | Estimated |

---

## Historic Trend

### Global Bill Payments (2015-2024)

| Year | Annual Txns (B) | YoY Growth | Est. TPS | Confidence |
|------|----------------|-----------|----------|------------|
| 2015 | ~60 | — | ~1,902 | 🔴 Low |
| 2016 | ~64 | +6.7% | ~2,029 | 🔴 Low |
| 2017 | ~68 | +6.3% | ~2,156 | 🔴 Low |
| 2018 | ~72 | +5.9% | ~2,283 | 🔴 Low |
| 2019 | ~76 | +5.6% | ~2,410 | 🔴 Low |
| 2020 | ~78 | +2.6% | ~2,473 | 🔴 Low |
| 2021 | ~82 | +5.1% | ~2,600 | 🟡 Medium |
| 2022 | ~86 | +4.9% | ~2,727 | 🟡 Medium |
| 2023 | ~90 | +4.7% | ~2,853 | 🟡 Medium |
| 2024 | ~95 | +5.6% | ~3,012 | 🟡 Medium |

*Sources: NACHA ACH biller volumes, BACS annual statistics, ECB SEPA DD volumes, India BBPS reports, GSMA mobile money data. Global total is a bottom-up model.*

**Key observations:**
- Bill payment transactions have grown ~5.2% CAGR over the decade, driven by two forces: population/urbanization growth (+2%) and digital subscription proliferation (+3%)
- COVID-19 had a muted impact (only +2.6% in 2020 vs. ~5-6% trend) — bills are non-discretionary, but some telco prepaid top-ups declined as economic activity slowed
- The fastest-growing segment is digital subscriptions (20%+ growth), which added ~5B annual transactions between 2019 and 2024
- Direct debit adoption continues to displace manual payments, reducing friction but not changing transaction counts
- India's BBPS is a standout: growing 55% YoY, it is digitizing billions of previously cash-based bill payments

---

## Growth Rate Analysis

| Period | CAGR | Context |
|--------|------|---------|
| 2015-2024 (9yr) | ~5.2% | Steady growth; digital subs and emerging market digitization |
| 2019-2024 (5yr) | ~4.6% | Slight COVID drag in 2020, offset by subscription boom |
| 2022-2024 (2yr) | ~5.1% | Acceleration from BBPS growth and streaming expansion |

---

## Projections

### Baseline (Steady Growth)

**Assumptions:**
1. Utility account growth of 2% annually (population + urbanization)
2. Digital subscriptions grow 10% annually, slowing to 5% by 2030
3. Rent digitization increases from ~40% to ~60% by 2035
4. BBPS and similar bill payment platforms continue rapid adoption in emerging markets
5. Overall bill payment transaction growth of 4-5% annually

| Year | Projected TPS | Annual Txns (B) |
|------|---------------|-----------------|
| 2026 | 3,329 | 105 |
| 2028 | 3,647 | 115 |
| 2030 | 3,996 | 126 |
| 2035 | 5,095 | 161 |

### High Growth (Subscription Economy + Emerging Market Digitization)

**Assumptions:**
1. "Everything-as-a-subscription" trend adds 3-5 new recurring charges per household by 2035
2. India (BBPS), Africa (mobile money), LatAm digitize 80%+ of bill payments
3. Embedded finance creates new recurring micro-payments (pay-per-use utilities, IoT device subscriptions)
4. EV charging subscriptions add a new utility category

| Year | Projected TPS | Annual Txns (B) |
|------|---------------|-----------------|
| 2026 | 3,583 | 113 |
| 2028 | 4,265 | 134 |
| 2030 | 5,095 | 161 |
| 2035 | 7,930 | 250 |

### Conservative (Consolidation)

**Assumptions:**
1. Subscription fatigue leads to bundling (fewer individual subscription transactions)
2. Utility billing consolidation (multi-utility billing reduces transaction count)
3. Growth slows to 2-3% annually as developed markets saturate

| Year | Projected TPS | Annual Txns (B) |
|------|---------------|-----------------|
| 2026 | 3,171 | 100 |
| 2028 | 3,329 | 105 |
| 2030 | 3,488 | 110 |
| 2035 | 3,964 | 125 |

*Full projection calculations: [workings/calculations.md](workings/calculations.md)*

**2035 Range:** Bill payments are projected to reach **125-250 billion transactions annually** by 2035, with TPS ranging from **~3,964 (conservative) to ~7,930 (high growth)**.

---

## Overlap Analysis

### Double-Counting Risk: VERY HIGH

Bill payments are almost entirely processed through existing payment rails:

| Underlying Rail | % of Bill Txns | Already Counted In |
|----------------|---------------|-------------------|
| Direct debit (SEPA DD, BACS, ACH) | ~40% | Bank Transfers capsule |
| Card-on-file (recurring charges) | ~25% | Consumer Cards capsule |
| Bank transfer (manual) | ~15% | Bank Transfers capsule |
| Mobile money / digital wallet | ~10% | Digital Wallets / Mobile Money capsule |
| Cash / check / in-person | ~10% | Not counted elsewhere |

**Overlap estimate:** ~90% of bill payment transactions are already counted in the Consumer Cards, Bank Transfers, or Digital Wallets capsules. Only cash/check bill payments (~10%) represent truly incremental infrastructure load.

### Incremental TPS Contribution

| Scenario | Total Txns (B) | Overlap % | Incremental Txns (B) | Incremental TPS |
|----------|---------------|-----------|---------------------|----------------|
| Current (2024) | 95 | 90% | 9.5 | ~301 |
| Baseline (2030) | 126 | 88% | 15.1 | ~479 |
| High (2035) | 250 | 85% | 37.5 | ~1,189 |

*Note: The overlap percentage is expected to decrease over time as emerging market cash bill payments are digitized (but they shift to bank transfer/mobile money rails, which are counted in those capsules). The declining overlap% reflects the growing "last mile" cash payments in newly banked populations.*

**For TPS aggregation:** Bill payments should be treated as a **use case overlay** on existing infrastructure. The ~95B annual transactions describe economic purpose, but ~90% of the infrastructure load is captured in underlying rail capsules.

---

## Key Findings

1. **Bill payments are the second-largest recurring payment category after cards.** At ~95B transactions and ~3,012 TPS, bill payments generate more transactions than insurance premiums, BNPL, and most other payment categories combined (excluding cards and bank transfers).

2. **Mobile telecoms is the single largest bill payment segment.** With 5.5B mobile connections generating 18B+ annual payment events (postpaid bills + prepaid top-ups), telecoms alone accounts for ~19% of all bill payments.

3. **Digital subscriptions are the fastest-growing segment.** Growing at 20%+ annually, digital subscriptions added ~5B transactions between 2019 and 2024. The "subscription economy" is creating new recurring payment relationships at unprecedented scale.

4. **India's BBPS is a global model for bill payment digitization.** The Bharat Bill Payment System processed 1.3B transactions in FY2024 (+55% YoY), creating a centralized, interoperable platform for all bill payments. This model is being studied by regulators in Africa and Southeast Asia.

5. **~90% of bill payments are already counted in other capsules.** Like insurance premiums, bill payments are a use case, not a payment rail. The incremental infrastructure contribution is limited to cash/check payments (~10%).

6. **Peak TPS concentration is extreme.** Bill payments cluster around the 1st and 15th of each month (direct debit processing dates). UK BACS processes ~100M direct debits on the first business day of each month, creating a peak/average ratio of ~2x for the bill payment category.

---

## Data Quality & Limitations

- **No single global source for bill payment transaction counts.** The estimate is built bottom-up from segment data (utility accounts, telecom subscriptions, etc.) and national payment system statistics.
- **Prepaid telecom top-ups are a gray area.** Are they "bill payments" or "retail purchases"? We include them because they serve the same economic function (paying for telecom service).
- **Rent payment digitization is poorly measured.** Cash and informal rent payments are invisible to payment systems. The 600M renter household figure and 40% digitization rate are rough estimates.
- **Utility account counts are approximate.** The IEA tracks electricity access at the country level, but conversion to "billing accounts" requires assumptions about household size and commercial/industrial accounts.
- **Regional data quality varies dramatically.** UK BACS and EU SEPA provide excellent direct debit data. India BBPS is well-tracked. China, Africa, and Latin America have significant gaps.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Exact global utility account count.** IEA tracks access, not accounts.
- **Cash bill payment volumes in emerging markets.** By definition, these bypass digital payment systems.
- **Digital subscription overlap.** How many "subscriptions" are paid by the same card-on-file transaction (family plans, bundled billing)?
- **Informal rent payment volumes.** Cash rent in developing markets is untracked.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Global utility accounts | Sum IEA electricity access (8B people) / household size (~3.5) = ~2.3B households; add commercial accounts (~10%) | IEA World Energy Outlook; World Bank data | 🟡 |
| Bill payment digitization rate | Use UK (95% digital), US (~80%), India (~30%), Africa (~15%) as benchmarks; weight by population | BACS annual report; NACHA; BBPS; M-Pesa data | 🟡 |
| Digital subscription total | Aggregate top-50 subscription services by published subscriber count; add estimated long-tail (1.5x multiplier) | Netflix, Spotify, Disney+, etc. public subscriber data | 🟡 |
| Rent payment volume | US Census (44M renters) + Eurostat + national stats for top-20 countries; global renter share (~35% of households) × global households (~2B) | Census.gov; Eurostat housing statistics | 🔴 |
| SEPA DD bill share | ECB publishes total SEPA DD volume (24B); bill payments estimated at 30-35% based on UK BACS composition data | ECB payment statistics; BACS annual report | 🟡 |

---

## Sources

1. [NACHA — ACH Network Volume and Value Statistics 2024](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
2. [BACS Payment Schemes — Annual Report 2024 (UK Direct Debit)](https://www.bacs.co.uk/)
3. [European Central Bank — Payment Statistics (SEPA Direct Debit volumes)](https://www.ecb.europa.eu/stats/payment_statistics/large_value_and_retail/html/index.en.html)
4. [NPCI — Bharat Bill Payment System (BBPS) Statistics FY2024](https://www.npci.org.in/what-we-do/bharat-billpay/product-statistics)
5. [GSMA — The State of Mobile Internet Connectivity Report 2024](https://www.gsma.com/r/somic/)
6. [ITU — Facts and Figures: Focus on Connectivity 2024](https://www.itu.int/en/ITU-D/Statistics/Pages/facts/default.aspx)
7. [IEA — World Energy Outlook 2024 (electricity access data)](https://www.iea.org/reports/world-energy-outlook-2024)
8. [Netflix — Q4 2024 Earnings (260M global subscribers)](https://ir.netflix.net/ir/doc/quarterly-earnings)
9. [Spotify — Q4 2024 Earnings (236M premium subscribers)](https://investors.spotify.com/financials/quarterly-results)
10. [Statista — Number of Digital Subscription Services Worldwide 2024](https://www.statista.com/topics/1464/e-commerce/)
11. [US Census Bureau — Quarterly Residential Vacancies and Homeownership Q4 2024](https://www.census.gov/housing/hvs/index.html)
12. [Eurostat — Housing Statistics 2024](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Housing_statistics)
13. [ACI Worldwide — Bill Payment Trends and Benchmarks 2024](https://www.aciworldwide.com/insights/expert-view)

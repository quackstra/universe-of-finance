---
title: "Buy Now Pay Later (BNPL) — Report"
parent: Payments
grand_parent: Explore
nav_order: 9
---

# Buy Now Pay Later (BNPL) — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Buy Now Pay Later has emerged as one of the fastest-growing payment methods globally, with an estimated **~5-6 billion initial purchase transactions** in 2024, generating **~18-22 billion total installment payment events** when counting each repayment separately. At the purchase level, BNPL runs at **~159-190 TPS**; at the installment level, **~571-697 TPS**. Total BNPL GMV reached **~$400-500 billion** in 2024, growing at 20-25% annually.

The counting question is fundamental: a single BNPL purchase creates 3-4 downstream installment debits. For TPS analysis, we count **both**: the initial purchase transaction (merchant-facing) and each installment debit (consumer-facing). This is consistent with how each installment generates a real payment event on card or bank transfer rails.

BNPL has **near-complete overlap** with existing payment rails — each installment is ultimately funded by a card charge or bank transfer. The incremental infrastructure load is minimal, but the economic transaction (extending credit at point of sale) is distinct.

## Scope

This analysis covers consumer-facing BNPL/installment payment services offered at checkout (online and in-store). Includes "Pay in 4" (interest-free, short-term), longer-term installment plans (6-36 months, interest-bearing), and pay-after-delivery models. Excludes traditional credit card installment plans offered by issuers post-purchase, layaway programs, and B2B trade credit.

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Avg TPS (purchase-level) | ~175 | Derived from ~5.5B purchases / 31.5M seconds | 🟡 Medium |
| Avg TPS (installment-level) | ~634 | Derived from ~20B installment events | 🟡 Medium |
| Daily purchase volume | ~15 million | Derived from annual total | 🟡 Medium |
| Annual purchases (2024) | ~5.5 billion | Aggregated from major provider disclosures | 🟡 Medium |
| Annual installment events (2024) | ~20 billion | ~5.5B × 3.6 avg installments per purchase | 🟡 Medium |
| Annual GMV (2024) | ~$450 billion | Aggregated from provider reports + market estimates | 🟡 Medium |
| Avg purchase value | ~$82 | $450B / 5.5B purchases | 🟡 Medium |
| Avg installment value | ~$23 | $82 / 3.6 installments | 🟡 Medium |

### Key Player Breakdown (2024)

| Provider | Annual Purchases (B) | Daily Txns (M) | GMV ($B) | Avg Order ($) | Markets | Source | Confidence |
|----------|---------------------|----------------|----------|--------------|---------|--------|------------|
| Klarna | ~0.9B | ~2.5M | ~$100B | ~$111 | 45 countries | Klarna H1 2024 report / investor presentations | 🟢 High |
| Afterpay (Block) | ~0.4B | ~1.1M | ~$25B | ~$63 | US, UK, AU, NZ, CA | Block 10-K FY2024 | 🟢 High |
| Affirm | ~0.2B | ~0.5M | ~$28B | ~$140 | US, CA | Affirm 10-K FY2024 (June FY) | 🟢 High |
| PayPal Pay Later | ~0.8B | ~2.2M | ~$65B | ~$81 | 10+ countries | PayPal 10-K FY2024 | 🟡 Medium |
| Zip (Zip Co) | ~0.08B | ~0.2M | ~$8B | ~$100 | US, AU, NZ | Zip FY2024 filings | 🟢 High |
| China BNPL (Ant Group Huabei, JD Baitiao) | ~2.0B | ~5.5M | ~$150B | ~$75 | China | Industry estimates | 🔴 Low |
| Other (Tabby, Tamara, Atome, Scalapay, etc.) | ~1.1B | ~3.0M | ~$74B | ~$67 | Various | Aggregated estimates | 🔴 Low |
| **Total** | **~5.5B** | **~15M** | **~$450B** | **~$82** | | | |

### Transaction Multiplier Effect

A single BNPL purchase generates multiple payment events:

```
1 BNPL purchase → 1 merchant payment (immediate or near-immediate)
                → 3-4 consumer installment debits (biweekly or monthly)
                → 0.1-0.2 failed payment retries
                → 0.05 late fee transactions
                ≈ 3.6 total payment events per purchase (weighted average)
```

| Model | Installments | Frequency | Multiplier | Share of BNPL |
|-------|-------------|-----------|------------|--------------|
| Pay in 4 | 4 | Biweekly | 4.0x | ~60% |
| Pay in 3 | 3 | Monthly | 3.0x | ~15% |
| 6-12 month plan | 6-12 | Monthly | 6-12x | ~15% |
| Pay after delivery | 1 (deferred) | 14-30 days | 1.0x | ~10% |
| **Weighted average** | | | **~3.6x** | |

### Regional Breakdown (2024)

| Region | GMV ($B) | Share | Est. Purchases (B) | Notes |
|--------|---------|-------|-------------------|-------|
| Asia-Pacific (incl. China) | ~$200B | ~44% | ~2.5B | China dominates; Australia highest per-capita adoption |
| Europe | ~$120B | ~27% | ~1.5B | Sweden (Klarna HQ), Germany, UK lead; regulated under EU Consumer Credit Directive |
| North America | ~$100B | ~22% | ~1.1B | US growing fastest; Affirm, Afterpay, PayPal Pay Later |
| Latin America | ~$15B | ~3% | ~0.2B | Brazil (Mercado Pago), Mexico emerging |
| Middle East & Africa | ~$15B | ~3% | ~0.2B | Tabby, Tamara in GCC; Shahry in Egypt |

---

## Historic Trend

### Global BNPL (2018-2024)

| Year | Annual Purchases (B) | YoY Growth | Est. TPS (purchase) | GMV ($B) | Confidence |
|------|---------------------|-----------|---------------------|----------|------------|
| 2018 | ~0.8 | — | ~25 | ~$40 | 🔴 Low |
| 2019 | ~1.3 | +63% | ~41 | ~$70 | 🔴 Low |
| 2020 | ~2.0 | +54% | ~63 | ~$120 | 🟡 Medium |
| 2021 | ~3.0 | +50% | ~95 | ~$200 | 🟡 Medium |
| 2022 | ~3.8 | +27% | ~120 | ~$280 | 🟡 Medium |
| 2023 | ~4.5 | +18% | ~143 | ~$360 | 🟡 Medium |
| 2024 | ~5.5 | +22% | ~175 | ~$450 | 🟡 Medium |

*Sources: Individual provider filings (Klarna, Affirm, Block, Zip); Worldpay Global Payments Report BNPL section; Juniper Research BNPL forecasts. 2018-2019 are back-extrapolated from Klarna's early growth data.*

**Key observations:**
- BNPL is one of the fastest-growing payment categories globally, with 2018-2024 CAGR of ~38% by purchase count
- Growth decelerated from 50%+ (2019-2021 pandemic boost) to 18-22% (2023-2024) as the category matures and faces regulatory headwinds
- COVID-19 was a massive accelerator — e-commerce boom + consumer credit tightening pushed users to BNPL
- 2022 saw a "hangover" as rising interest rates squeezed BNPL providers' unit economics, leading to tighter underwriting
- 2024 growth re-accelerated as survivors (Klarna, Affirm) reached profitability and expanded in-store offerings

---

## Growth Rate Analysis

| Period | CAGR (Purchases) | CAGR (GMV) | Context |
|--------|-----------------|-----------|---------|
| 2018-2024 (6yr) | ~38% | ~49% | Hyper-growth phase; mix shift to higher AOV |
| 2020-2024 (4yr) | ~29% | ~39% | Through COVID boom and post-boom normalization |
| 2022-2024 (2yr) | ~20% | ~27% | Maturing; providers focused on profitability |

---

## Projections

### Baseline (BNPL Becomes Mainstream)

**Assumptions:**
1. Growth moderates to 12-15% annually as BNPL becomes a standard checkout option
2. Regulatory frameworks (EU Consumer Credit Directive, CFPB rules) add friction but don't kill the category
3. Card network BNPL offerings (Visa Installments, Mastercard Installments) grow alongside dedicated providers
4. Average installment multiplier stays at ~3.6x

| Year | Projected TPS (purchase) | TPS (installment) | Annual Purchases (B) | GMV ($B) |
|------|------------------------|-------------------|---------------------|----------|
| 2026 | 228 | 822 | 7.2 | $590 |
| 2028 | 290 | 1,044 | 9.1 | $750 |
| 2030 | 364 | 1,310 | 11.5 | $940 |
| 2035 | 578 | 2,081 | 18.2 | $1,500 |

### High Growth (Embedded Finance Explosion)

**Assumptions:**
1. BNPL becomes default option at 80%+ of e-commerce checkouts globally
2. In-store BNPL via card-linked installments captures 10%+ of POS transactions
3. B2B BNPL (trade credit digitization) adds a new growth vector
4. Emerging market adoption explodes (India, Brazil, SE Asia, Africa)

| Year | Projected TPS (purchase) | TPS (installment) | Annual Purchases (B) | GMV ($B) |
|------|------------------------|-------------------|---------------------|----------|
| 2026 | 278 | 1,002 | 8.8 | $720 |
| 2028 | 418 | 1,505 | 13.2 | $1,080 |
| 2030 | 613 | 2,208 | 19.3 | $1,580 |
| 2035 | 1,235 | 4,446 | 38.9 | $3,200 |

### Conservative (Regulatory Squeeze)

**Assumptions:**
1. BNPL regulated as credit product globally, requiring full credit checks — kills impulse adoption
2. Card network installment products cannibalize dedicated BNPL providers
3. Rising defaults in economic downturn lead to tighter underwriting
4. Growth slows to 5-8% annually

| Year | Projected TPS (purchase) | TPS (installment) | Annual Purchases (B) | GMV ($B) |
|------|------------------------|-------------------|---------------------|----------|
| 2026 | 198 | 713 | 6.3 | $510 |
| 2028 | 222 | 798 | 7.0 | $570 |
| 2030 | 248 | 892 | 7.8 | $640 |
| 2035 | 313 | 1,126 | 9.9 | $810 |

*Full projection calculations: [workings/calculations.md](workings/calculations.md)*

**2035 Range:** BNPL purchases are projected at **10-39 billion annually** by 2035, with installment-level TPS ranging from **~1,126 (conservative) to ~4,446 (high growth)**.

---

## Overlap Analysis

### Double-Counting Risk: VERY HIGH

Every BNPL transaction is funded through an existing payment rail:

| Funding Rail | % of BNPL Installments | Already Counted In |
|-------------|----------------------|-------------------|
| Debit card charge | ~40% | Consumer Cards capsule |
| Bank account direct debit | ~35% | Bank Transfers capsule |
| Credit card charge | ~15% | Consumer Cards capsule |
| Digital wallet (funded by above) | ~10% | Digital Wallets capsule |

**Overlap estimate:** ~100% of BNPL installment transactions are already counted in other capsules. BNPL is a **pure overlay** — it creates a credit product at the application layer, but every actual money movement uses existing infrastructure.

**However, BNPL does create incremental transactions.** A $200 purchase paid with a credit card = 1 transaction. The same purchase via "Pay in 4" = 4 transactions (plus the merchant payment). BNPL genuinely multiplies the transaction count on underlying rails by 3-4x per purchase.

### Net Incremental Impact

| Scenario | BNPL Installments (B) | Counterfactual Txns (B) | Net Incremental (B) | Incremental TPS |
|----------|---------------------|----------------------|-------------------|----------------|
| Current (2024) | 20.0 | 5.5 | 14.5 | ~460 |
| Baseline (2030) | 41.4 | 11.5 | 29.9 | ~948 |
| High (2035) | 140.0 | 38.9 | 101.1 | ~3,205 |

*Note: "Counterfactual" = the transactions that would have occurred anyway if the consumer paid in full. The "net incremental" = additional payment events created by splitting into installments.*

**For TPS aggregation:** BNPL should be counted as a **transaction multiplier** on existing rails. The ~14.5B net incremental installment events in 2024 represent real infrastructure load that would not exist without BNPL, even though each individual debit flows through cards or bank transfers.

---

## Key Findings

1. **BNPL is a transaction multiplier, not a payment rail.** Every BNPL installment ultimately flows through cards or bank transfers. The innovation is at the credit/application layer, not the infrastructure layer. But it genuinely increases transaction counts on existing rails.

2. **The counting question matters enormously.** At the purchase level, BNPL is ~5.5B transactions (~175 TPS) — modest. At the installment level, it's ~20B transactions (~634 TPS). The 3.6x multiplier is the defining characteristic of BNPL's infrastructure impact.

3. **Klarna processes more daily transactions than many banks.** At ~2.5M daily transactions, Klarna alone exceeds the daily transaction count of most mid-tier banks. The top 5 BNPL providers collectively process ~10M+ transactions daily.

4. **Growth is decelerating but still exceptional.** The 2018-2024 CAGR of ~38% makes BNPL one of the fastest-growing payment categories ever measured. Even the conservative scenario projects 5-8% annual growth — still above GDP growth.

5. **China is the elephant in the room.** Ant Group's Huabei and JD's Baitiao likely process more BNPL transactions than all Western providers combined, but disclosure is minimal. The ~2B China estimate could be significantly higher.

6. **Regulatory risk is the primary threat.** The EU Consumer Credit Directive (2026 implementation) will require BNPL providers to conduct full creditworthiness assessments. The CFPB's interpretive rule classifying BNPL as credit cards could fundamentally change the US market.

---

## Data Quality & Limitations

- **No single source publishes total global BNPL transaction counts.** Figures are aggregated from individual provider disclosures plus market estimates for the long tail.
- **China data is opaque.** Ant Group and JD do not disclose BNPL-specific transaction volumes. Estimates are based on industry reports and analyst estimates.
- **Definitional inconsistency.** Some providers count "transactions" as purchases; others count installment events. Klarna's "2.5M transactions per day" appears to be at the purchase level, not installment level.
- **Card network BNPL is undercounted.** Visa Installments and Mastercard Installments are growing but volumes are not separately disclosed — they're buried in overall card transaction counts.
- **GMV vs. origination volume.** Some sources report GMV (total purchase value), others report origination volume (total credit extended). For "Pay in 4," these are the same, but for longer-term plans, the credit extended may exceed the purchase price due to interest.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Total China BNPL volume.** Huabei and Baitiao volumes are not publicly disclosed in comparable format.
- **Card network installment volumes.** Visa and Mastercard don't separately report BNPL-like installment transactions.
- **Default rates by provider and market.** Critical for understanding sustainability but inconsistently disclosed.
- **In-store vs. online split.** Most BNPL data focuses on e-commerce; in-store adoption is growing but poorly measured.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| China BNPL volume | Cross-reference Ant Group's disclosed "credit tech" revenue with estimated take rate to back into GMV; compare with PBOC consumer credit data | Ant Group: ~$4.5B credit tech revenue; estimated 0.5-1% take rate implies $450-900B GMV | 🔴 |
| Card network BNPL | Monitor Visa/MC quarterly earnings commentary on installment product growth rates; apply to base estimates | Visa: "installment volumes grew 30%+ YoY" (Q4 2024 earnings call) | 🔴 |
| Total market sizing | Worldpay GPR projects BNPL at 5% of global e-commerce by 2027 (~$600B of ~$12T); cross-check against provider-level roll-up | Worldpay GPR 2024; eMarketer e-commerce projections | 🟡 |
| In-store BNPL | Track Klarna/Affirm in-store partnership announcements; use Afterpay's tap-to-pay adoption as proxy | Afterpay: ~15% of GMV now in-store (Block Q4 2024) | 🟡 |

---

## Sources

1. [Klarna — H1 2024 Results / Investor Presentation](https://www.klarna.com/international/press/klarna-reports-strong-first-half-of-2024/)
2. [Block Inc. — 10-K FY2024 (Afterpay segment)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001512673)
3. [Affirm Holdings — 10-K FY2024](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001820953)
4. [PayPal Holdings — 10-K FY2024 (Pay Later volumes)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001633917)
5. [Zip Co — FY2024 Annual Report](https://zip.co/investors)
6. [Worldpay — Global Payments Report 2024 (BNPL section)](https://worldpay.globalpaymentsreport.com/)
7. [Juniper Research — BNPL: Market Forecasts, Key Opportunities & Vendor Analysis 2024-2029](https://www.juniperresearch.com/research/fintech-payments/buy-now-pay-later/)
8. [CFPB — Buy Now, Pay Later: Market Trends and Consumer Impacts (September 2024)](https://www.consumerfinance.gov/data-research/research-reports/)
9. [EU Consumer Credit Directive 2023/2225 — BNPL provisions](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2225)
10. [Bain & Company — The Future of BNPL: From Disruptor to Mainstream (2024)](https://www.bain.com/insights/topics/payments/)

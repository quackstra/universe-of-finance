# Insurance Premium Payments — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Global insurance premium payments represent a massive but often overlooked payment flow. The global insurance industry collected **~$7.2 trillion in gross written premiums** in 2024 (Swiss Re sigma), but what matters for TPS analysis is the **transaction count** — how many individual premium payment events occur. We estimate **~12-16 billion insurance premium payment transactions annually**, equivalent to **~380-507 TPS**. This is a low-frequency, high-value payment category compared to consumer cards or bill payments.

Critically, **~95%+ of insurance premium payments are overlay transactions** — they flow through existing card rails, direct debit (bank transfer) systems, or ACH/SEPA channels. The incremental transaction count (payments that would not exist without the insurance product) is essentially the full ~12-16B, but the *infrastructure load* is already captured in card and bank transfer capsules.

## Scope

This analysis covers premium payments made by policyholders (personal and commercial) to insurers globally. It includes initial premiums and renewals but excludes claims payments (insurer-to-policyholder), reinsurance flows (insurer-to-insurer), and investment income. The unit of analysis is a single premium payment event — one monthly auto insurance debit = one transaction.

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~443 | Derived from ~14B annual ([calculations](workings/calculations.md)) | 🔴 Low |
| Peak TPS (est.) | ~600-800 | Monthly billing cycle peaks on 1st/15th of month | 🔴 Low |
| Daily volume | ~38 million | Derived from annual total | 🔴 Low |
| Annual transactions (2024) | ~14 billion | Bottom-up model ([calculations](workings/calculations.md)) | 🟡 Medium |
| Annual premium value (2024) | ~$7.2 trillion | Swiss Re sigma No. 3/2025 | 🟢 High |
| Avg transaction value | ~$514 | $7.2T / 14B txns | 🟡 Medium |

### Segment Breakdown

| Segment | Global Policies (est.) | Payment Frequency | Annual Txns (B) | Avg Premium/Payment |
|---------|----------------------|-------------------|-----------------|-------------------|
| Auto/Motor | ~1.5B policies | Monthly (~70%), Annual (~30%) | ~4.4B | ~$150/month or ~$1,200/year |
| Health | ~2.5B covered lives | Monthly (~60%), Per-claim copay (~40%) | ~3.5B | ~$250/month (varies wildly) |
| Property/Home | ~500M policies | Annual (~50%), Quarterly (~30%), Monthly (~20%) | ~1.2B | ~$1,000-$3,000/year |
| Life | ~2B policies in force | Monthly (~50%), Annual (~30%), Quarterly (~20%) | ~3.2B | ~$100-$300/month |
| Commercial/Specialty | ~200M policies | Annual (~40%), Quarterly (~40%), Monthly (~20%) | ~0.8B | ~$5,000-$50,000/year |
| **Total** | | | **~13.1B** | |

Note: Adding payment failures, retries, and mid-term adjustments brings the working estimate to **~14B** transactions.

### Payment Channel Breakdown

| Channel | Share by Count | Share by Value | Notes |
|---------|---------------|----------------|-------|
| Auto-debit / Direct debit | ~45% | ~40% | Dominant in Europe, growing globally |
| Card payment (credit/debit) | ~25% | ~20% | Common for monthly premiums in US |
| Bank transfer / ACH | ~15% | ~25% | Preferred for large commercial premiums |
| Agent collection (cash/check) | ~10% | ~10% | Declining; still significant in emerging markets |
| Digital wallet / app | ~5% | ~5% | Growing rapidly; insurtechs leading adoption |

### Regional Breakdown (2024)

| Region | Premium Volume ($T) | Share | Est. Txns (B) | Source |
|--------|-------------------|-------|---------------|--------|
| North America | ~$2.9T | ~40% | ~5.0B | Swiss Re sigma, NAIC |
| Europe | ~$1.7T | ~24% | ~3.5B | Insurance Europe |
| Asia-Pacific | ~$2.0T | ~28% | ~4.0B | Swiss Re sigma |
| Latin America | ~$0.2T | ~3% | ~0.6B | Estimated |
| Middle East & Africa | ~$0.1T | ~1.5% | ~0.4B | Estimated |
| Rest of World | ~$0.3T | ~3.5% | ~0.5B | Estimated |

---

## Historic Trend

### Global Insurance Premiums (2015-2024)

| Year | Premium Volume ($T) | YoY Growth | Est. Txns (B) | Est. TPS | Confidence |
|------|-------------------|-----------|---------------|----------|------------|
| 2015 | $4.6T | — | ~9.5 | ~301 | 🔴 Low |
| 2016 | $4.7T | +2.2% | ~9.8 | ~311 | 🔴 Low |
| 2017 | $4.9T | +4.3% | ~10.2 | ~323 | 🔴 Low |
| 2018 | $5.2T | +6.1% | ~10.6 | ~336 | 🔴 Low |
| 2019 | $5.4T | +3.8% | ~11.0 | ~349 | 🔴 Low |
| 2020 | $5.6T | +3.7% | ~11.3 | ~358 | 🔴 Low |
| 2021 | $6.0T | +7.1% | ~12.0 | ~380 | 🔴 Low |
| 2022 | $6.3T | +5.0% | ~12.5 | ~396 | 🟡 Medium |
| 2023 | $6.8T | +7.9% | ~13.3 | ~422 | 🟡 Medium |
| 2024 | $7.2T | +5.9% | ~14.0 | ~444 | 🟡 Medium |

*Sources: Swiss Re sigma annual reports (premium volumes). Transaction counts derived via bottom-up policy model.*

**Key observations:**
- Premium volumes have grown ~4.6% CAGR over the decade, driven by rate hardening (price increases) and penetration growth in Asia
- Transaction COUNT growth outpaces premium VALUE growth because of the secular shift from annual to monthly billing (more transactions per policy)
- COVID-19 had minimal impact on premium volumes — insurance is contractual and non-discretionary
- Digital payment adoption accelerated post-COVID, reducing agent/cash collection and increasing card/direct debit share

---

## Growth Rate Analysis

| Period | Premium CAGR | Transaction Count CAGR | Context |
|--------|-------------|----------------------|---------|
| 2015-2024 (9yr) | ~5.1% | ~4.4% | Steady growth; rate hardening in 2022-2024 |
| 2019-2024 (5yr) | ~5.9% | ~4.9% | Through-cycle; COVID resilient |
| 2022-2024 (2yr) | ~6.9% | ~5.8% | Hard market pricing inflating premiums |

---

## Projections

### Baseline (Current Trends Continue)

**Assumptions:**
1. Global premium growth moderates to 4-5% annually as hard market cycle softens
2. Monthly billing continues to displace annual billing, adding ~1% to transaction count growth above premium growth
3. No major regulatory disruption to insurance distribution

| Year | Projected TPS | Annual Txns (B) | Premium Volume ($T) |
|------|---------------|-----------------|-------------------|
| 2026 | 488 | 15.4 | $7.9T |
| 2028 | 537 | 16.9 | $8.7T |
| 2030 | 591 | 18.6 | $9.5T |
| 2035 | 753 | 23.8 | $12.2T |

### High Growth (Emerging Market Penetration)

**Assumptions:**
1. Insurance penetration in India, SE Asia, Africa doubles by 2035
2. Microinsurance and parametric products add 2B+ policies
3. Embedded insurance (integrated at point of sale) creates new premium flows

| Year | Projected TPS | Annual Txns (B) | Premium Volume ($T) |
|------|---------------|-----------------|-------------------|
| 2026 | 520 | 16.4 | $8.3T |
| 2028 | 613 | 19.3 | $9.8T |
| 2030 | 722 | 22.8 | $11.5T |
| 2035 | 1,045 | 33.0 | $16.0T |

### Conservative (Market Saturation)

**Assumptions:**
1. Premium growth slows to 2-3% as developed market penetration plateaus
2. Embedded insurance cannibalizes traditional premium flows rather than adding net new
3. Climate risk repricing reduces policy count in some segments

| Year | Projected TPS | Annual Txns (B) | Premium Volume ($T) |
|------|---------------|-----------------|-------------------|
| 2026 | 466 | 14.7 | $7.6T |
| 2028 | 494 | 15.6 | $8.0T |
| 2030 | 524 | 16.5 | $8.5T |
| 2035 | 613 | 19.3 | $9.9T |

*Full projection calculations: [workings/calculations.md](workings/calculations.md)*

**2035 Range:** Insurance premium payments are projected to reach **19-33 billion transactions annually** by 2035, with TPS ranging from **~613 (conservative) to ~1,045 (high growth)**.

---

## Overlap Analysis

### Double-Counting Risk: HIGH

Insurance premium payments are **almost entirely overlay transactions** on existing payment infrastructure:

| Underlying Rail | % of Premium Txns | Already Counted In |
|----------------|-------------------|-------------------|
| Direct debit (bank transfers) | ~45% | Bank Transfers capsule |
| Card payments (credit/debit) | ~25% | Consumer Cards capsule |
| ACH / bank transfer | ~15% | Bank Transfers capsule |
| Cash/check (declining) | ~10% | Not counted elsewhere |
| Digital wallet | ~5% | Digital Wallets capsule |

**Overlap estimate:** ~85-90% of insurance premium transactions are already counted in the Consumer Cards or Bank Transfers capsules. Only cash/check collections (~10%) and some agent-mediated flows represent truly incremental infrastructure load.

**For TPS aggregation purposes:** Insurance premiums should be treated as a **use case overlay**, not an additive transaction category. The ~14B annual transactions describe the economic purpose, but the infrastructure transactions are already captured in underlying rail capsules.

### Incremental TPS Contribution

| Scenario | Total Txns (B) | Overlap % | Incremental Txns (B) | Incremental TPS |
|----------|---------------|-----------|---------------------|----------------|
| Current (2024) | 14.0 | 90% | 1.4 | ~44 |
| Baseline (2030) | 18.6 | 88% | 2.2 | ~70 |
| High (2035) | 33.0 | 85% | 5.0 | ~158 |

---

## Key Findings

1. **Insurance is a $7.2T annual payment flow but a low-TPS category.** At ~14B transactions and ~444 TPS, it processes roughly 1/55th the transaction count of consumer cards despite handling ~14% of card-equivalent value. This reflects high average transaction values ($514 vs. $67 for cards).

2. **The shift from annual to monthly billing is the key transaction count driver.** As insurers move to monthly billing (especially auto and health), the same premium dollar generates 12x the transactions. This trend adds ~1% per year to transaction count growth above premium growth.

3. **~90% of insurance premium payments are already counted in other capsules.** Card payments and direct debits are the primary rails. For deduplication, insurance premiums are a use-case label, not a distinct infrastructure category.

4. **Emerging markets are wildly under-penetrated.** Insurance penetration (premiums/GDP) is ~7% in developed markets vs. ~1.5% in emerging markets. If India and Africa reach even 3%, the transaction count could double.

5. **Agent collection is the last cash frontier in insurance.** ~10% of premiums are still collected by agents in cash, primarily in India, Southeast Asia, and Africa. Mobile money and UPI are rapidly digitizing this channel.

---

## Data Quality & Limitations

- **No single source publishes global insurance transaction counts.** All transaction estimates are modeled bottom-up from policy counts and payment frequency assumptions. Confidence is 🟡 Medium at best.
- **Policy count data is fragmented.** Swiss Re sigma publishes premium volumes reliably but not policy counts. Policy counts are estimated from national regulator data (NAIC, EIOPA, IRDAI) and individual insurer reports.
- **Payment frequency assumptions vary by market.** Monthly billing dominates in the US but annual/quarterly billing is more common in Europe and Asia. The global average is uncertain.
- **Health insurance is the hardest segment.** In single-payer systems (UK, Canada), there are no consumer premium payments for public health coverage. The 2.5B "covered lives" figure includes both private and public-but-supplemental insurance.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Exact global policy count by line of business.** No single source aggregates this.
- **Payment frequency distribution.** What fraction of auto policies are paid monthly vs. annually by country?
- **Agent collection volumes.** Cash premium collection in emerging markets is largely untracked.
- **Embedded insurance transaction volumes.** Are these new premium flows or reclassified existing ones?

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Global policy count | Sum top-10 markets from national regulators (US NAIC, EIOPA, IRDAI, CIRC, FSA Japan) — covers ~80% of global premiums | NAIC: 3.2B policies in force (US); IRDAI: 650M policies (India) | 🟡 |
| Payment frequency | Survey top-20 insurers on billing mix; cross-reference with payment processor data (Stripe Insurance, Adyen) | US industry: ~70% monthly for auto; Europe: ~50% annual for home | 🔴 |
| Cash/agent collection | India IRDAI publishes channel-wise premium data; LIC annual report breaks out agent vs. digital | IRDAI annual report; LIC India 2024 data | 🟡 |
| Embedded insurance growth | Track announcements from Tesla Insurance, Amazon Protect, Apple Care+ as proxy for embedded premium volumes | Individual company disclosures | 🔴 |

---

## Sources

1. [Swiss Re — sigma No. 3/2025: World Insurance Premium Overview](https://www.swissre.com/institute/research/sigma-research/sigma-2025-03.html)
2. [IAIS — Global Insurance Market Report 2024](https://www.iaisweb.org/activities-topics/financial-stability/global-insurance-market-report/)
3. [Insurance Europe — European Insurance in Figures 2024](https://www.insuranceeurope.eu/statistics)
4. [NAIC — US Insurance Industry at a Glance 2024](https://content.naic.org/cipr-topics/insurance-industry-glance)
5. [Lloyd's of London — Annual Report 2024](https://www.lloyds.com/about-lloyds/investor-relations/financial-performance/annual-reports)
6. [IRDAI — Annual Report 2023-24 (India)](https://irdai.gov.in/annual-report)
7. [Swiss Re — sigma No. 4/2024: World Insurance — Riding Out the Storm](https://www.swissre.com/institute/research/sigma-research.html)
8. [McKinsey — Global Insurance Report 2025](https://www.mckinsey.com/industries/financial-services/our-insights/global-insurance-report)
9. [Statista — Insurance Premiums Worldwide 2024](https://www.statista.com/topics/1466/insurance/)
10. [Allied Market Research — Insurance Market Size 2024-2032](https://www.alliedmarketresearch.com/insurance-market)

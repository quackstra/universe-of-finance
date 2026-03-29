---
title: "E-Commerce & Merchant Processing — Report"
parent: Payments
grand_parent: Explore
nav_order: 4
---

# E-Commerce & Merchant Processing

> **Category**: Payments > E-Commerce & Merchant Processing
> **Last Updated**: 2026-03-26
> **Capsules**: 9

---

## Boundary

This analysis counts **e-commerce orders** — the commerce event where a consumer
places a purchase online. The payment rail (card, wallet, BNPL, bank transfer) is
counted separately in its own UoF category. One purchase on Amazon via Apple Pay
funded by a Visa card = **one** e-commerce transaction here, even though the same
event appears in Digital Wallets and Consumer Cards.

Scope: **Retail/consumer e-commerce** (B2C + C2C marketplace). B2B e-commerce
($21T+) is excluded, consistent with standard industry reporting.

---

## 1. Current TPS (2024) 🟡

| Metric | Value | Confidence |
|---|---|---|
| **Average TPS** | **~1,800** | 🟡 Medium |
| Average TPS range | 1,400 – 2,500 | — |
| **Peak TPS (single platform)** | **583,000** | 🟢 High |
| Peak TPS (global estimate) | ~600K – 1M | 🔴 Low |

**Average TPS** is derived from $6.33T GMV / $110 blended AOV = ~57.5B transactions
/ 31.6M seconds per year = **1,823 TPS** ([calculation](workings/calculations.md#c1)).

The range reflects AOV sensitivity — Asia-Pacific's lower basket sizes (~$80) would
push TPS higher; using Western-market AOVs (~$145) pushes it lower.

**Peak TPS**: Alibaba's confirmed record is **583,000 orders/sec** during Singles Day
2020 ([SCMP](https://www.scmp.com/tech/e-commerce/article/3038539)). Alibaba stopped
disclosing peak metrics after 2021. Shopify hit **$4.6M/min** (~700 orders/sec) during
BFCM 2024 ([Shopify](https://www.shopify.com/news/bfcm-data-2024)). A theoretical
global simultaneous peak across all platforms could reach ~1M orders/sec, but no
single event triggers that level simultaneously.

---

## 2. Annual Volume (2024) 🟡

**~57.5 billion e-commerce transactions** globally in 2024.

Derived: $6.33T GMV / $110 blended global AOV ([calculation](workings/calculations.md#c3)).

Cross-checked against known platform volumes:
- Alibaba: ~14.5B orders/year ([DemandSage](https://www.demandsage.com/ecommerce-statistics/))
- Amazon: ~4.5B orders/year ([Capital One Shopping](https://capitaloneshopping.com/research/amazon-orders-per-day/))
- Shopify merchants: ~3B (derived: $292B GMV / ~$100 AOV, [SEC filing](https://www.sec.gov/Archives/edgar/data/1594805/000159480525000011/exhibit991pressreleaseq420.htm))
- Bottom-up platform sum: ~57B — consistent with top-down estimate ✓

---

## 3. Annual Value (2024) 🟢

**$6.33 trillion** in global retail e-commerce GMV
([SOAX/Statista](https://soax.com/research/growth-ecommerce)).

Cross-checks:
- eMarketer/Shopify project $6.42–6.86T for 2025 (+8–9%), implying ~$6.3T for 2024 ✓
- DemandSage: $6.86T for 2025 with 8.37% growth from 2024 → implies $6.33T ✓

---

## 4. Historic Timeseries (2014–2024) 🟢

| Year | GMV ($T) | YoY Growth | Est. Txns (B) | Est. Avg TPS |
|---|---|---|---|---|
| 2014 | 1.34 | — | 17.9 | 568 |
| 2015 | 1.55 | 15.9% | 19.4 | 614 |
| 2016 | 1.85 | 19.2% | 21.6 | 686 |
| 2017 | 2.38 | 29.1% | 26.4 | 838 |
| 2018 | 2.98 | 25.2% | 31.1 | 985 |
| 2019 | 3.35 | 12.4% | 33.5 | 1,062 |
| **2020** | **4.25** | **26.8%** | **40.5** | **1,282** |
| 2021 | 4.99 | 17.4% | 45.4 | 1,437 |
| 2022 | 5.31 | 6.5% | 46.6 | 1,477 |
| 2023 | 5.78 | 8.9% | 49.8 | 1,579 |
| 2024 | 6.33 | 9.4% | 57.5 | 1,823 |

Source: [SOAX/Statista](https://soax.com/research/growth-ecommerce). Transaction
counts derived using era-adjusted AOV (see [calculations](workings/calculations.md#c5)).

**COVID inflection**: 2020 saw $897B added in a single year (+26.8%), equivalent to
~5 years of pre-2017 growth. Post-pandemic growth normalised to 6.5–9.4%.

---

## 5. Subcategory Breakdown 🟢

### By Payment Method (value-weighted, 2024)

| Payment Method | Share | Value ($T) |
|---|---|---|
| Digital Wallets | 53% | 3.35 |
| Credit Cards | 20% | 1.27 |
| Debit Cards | 12% | 0.76 |
| Bank Transfer (A2A) | 7% | 0.44 |
| Buy Now Pay Later | 5% | 0.32 |
| Cash on Delivery | 2% | 0.13 |
| Other | 1% | 0.06 |

Source: [Worldpay Global Payments Report 2025](https://worldpay.com/en/global-payments-report).

Digital wallets grew from 34% to 66% of all digital e-commerce payments between
2014 and 2024. BNPL spending exploded from $2.2B to $342B over the same period
([Worldpay GPR](https://offers.worldpayglobal.com/rs/850-JOA-856/images/GPR25.pdf)).

**Double-counting note**: These payment method shares describe *how* e-commerce is
paid for. A wallet-funded purchase is counted once here (as an e-commerce order) and
once in the Digital Wallets category (as a wallet transaction). The UoF reconciliation
layer handles deduplication.

### By Region (value-weighted, 2024)

| Region | Share | Value ($T) | Est. Txns (B) | Est. TPS |
|---|---|---|---|---|
| Asia-Pacific | 45.7% | 2.89 | 36.2 | 1,146 |
| North America | 29.8% | 1.89 | 12.6 | 398 |
| Europe | 16.9% | 1.07 | 6.9 | 220 |
| LAMEA | 7.6% | 0.48 | 1.8 | 59 |

Sources: [Polaris Market Research](https://www.polarismarketresearch.com/industry-analysis/e-commerce-market),
[Statista](https://www.statista.com/forecasts/1117851/worldwide-e-commerce-revenue-by-region).

Asia-Pacific dominates both by value (45.7%) and even more so by transaction count
(~63%) due to lower average order values.

---

## 6. Growth Rate 🟢

| Period | CAGR | Context |
|---|---|---|
| 2014–2024 (10-year) | **16.8%** | Full decade including COVID surge |
| 2014–2019 (pre-COVID) | **20.1%** | Rapid growth from smaller base |
| 2020–2024 (post-COVID) | **10.5%** | Includes pandemic spike + normalisation |
| 2022–2024 (normalised) | **9.2%** | Post-pandemic steady state |

The pre-COVID ~20% CAGR reflected e-commerce eating into traditional retail from a
low base. COVID pulled forward years of adoption. The normalised rate of ~9% reflects
a larger base but continued structural shift to online purchasing.

See [full CAGR calculations](workings/calculations.md#c8).

---

## 7. Baseline Projection (2026–2035) 🟡

**Assumes**: 8.5% CAGR (2025–2030), declining to 6.5% (2031–2035).

| Year | GMV ($T) | Est. Avg TPS |
|---|---|---|
| 2025 | 6.86 | 1,907 |
| 2027 | 8.07 | 2,173 |
| **2030** | **10.31** | **2,645** |
| 2035 | 14.12 | 3,327 |

Based on eMarketer/Shopify consensus forecasts for near-term, with natural
deceleration as the market matures. By 2030, e-commerce would represent ~25% of
all retail sales globally ([calculations](workings/calculations.md#c9)).

---

## 8. High-Growth Projection (2026–2035) 🔴

**Assumes**: 12% CAGR (2025–2030), declining to 9% (2031–2035).

| Year | GMV ($T) | Est. Avg TPS |
|---|---|---|
| 2025 | 7.09 | 1,971 |
| 2027 | 8.89 | 2,395 |
| **2030** | **12.49** | **3,207** |
| 2035 | 19.22 | 4,551 |

**Key accelerants**:
- **Social commerce** grows from ~$2T (2025) to $8.5T (2030) at 26% CAGR
  ([SellersCommerce](https://www.sellerscommerce.com/blog/social-commerce-statistics/))
- **TikTok Shop** US: $15.82B in 2025 after 407% growth in 2024
  ([eMarketer](https://www.emarketer.com/press-releases/tiktok-shop-makes-up-nearly-20-of-social-commerce-in-2025/))
- **Livestream shopping**: ~$50B in the US alone (2025), 84% YoY growth during BFCM
  ([GetStream](https://getstream.io/blog/livestream-shopping-statistics/))
- **Embedded payments** reduce checkout friction; AI-powered discovery accelerates
  impulse purchasing

In this scenario, social commerce becomes 25%+ of total e-commerce by 2030.

---

## 9. Conservative Projection (2026–2035) 🟡

**Assumes**: 5% CAGR (2025–2030), declining to 4% (2031–2035).

| Year | GMV ($T) | Est. Avg TPS |
|---|---|---|
| 2025 | 6.65 | 1,847 |
| 2027 | 7.33 | 1,976 |
| **2030** | **8.49** | **2,183** |
| 2035 | 10.33 | 2,455 |

**Headwinds**: Digital services taxes, GDPR-style privacy regulation reducing
personalisation effectiveness, developed-market saturation (~30% e-commerce
penetration ceiling), macroeconomic deceleration.

---

## Projection Summary — 2030 Comparison

| Scenario | 2030 GMV ($T) | 2030 Avg TPS | CAGR (2025–2030) |
|---|---|---|---|
| Conservative | 8.49 | 2,183 | 5.0% |
| **Baseline** | **10.31** | **2,645** | **8.5%** |
| High-Growth | 12.49 | 3,207 | 12.0% |

---

## Key Platform Data Points (2024)

| Platform | Annual Orders | GMV | Peak TPS Record |
|---|---|---|---|
| Alibaba | ~14.5B | ~$900B–1T | 583,000/sec (2020) |
| Amazon | ~4.5B | ~$750B | Not disclosed |
| Shopify | ~3B | $292B | ~700/sec (BFCM 2024) |

| Processor | TPV (2024) | YoY Growth |
|---|---|---|
| PayPal | $1.68T | +10% |
| Stripe | $1.40T | +38% |
| Adyen | €1.29T (~$1.38T) | +33% |

Sources: [Shopify](https://www.shopify.com/news/bfcm-data-2024),
[FintechWrapUp](https://www.fintechwrapup.com/p/deep-dive-stripe-vs-adyen-comparing),
[Capital One Shopping](https://capitaloneshopping.com/research/amazon-orders-per-day/).

---

## Methodology Notes

1. **GMV data** sourced from Statista via SOAX — the most widely cited and
   methodologically consistent timeseries for retail e-commerce
2. **Transaction counts** are derived (GMV / AOV), not directly observed. No single
   source tracks global e-commerce transaction count. This is the primary source
   of uncertainty.
3. **AOV of $110** is conservative — Western sources report $116–145, but
   Asia-Pacific (45%+ of orders) has significantly lower AOV (~$60–80)
4. **Peak TPS** relies on Alibaba's 2020 disclosure (583K/sec). Post-2021,
   Alibaba stopped publishing this metric.
5. All supporting calculations in [workings/calculations.md](workings/calculations.md)
6. All source notes in [workings/source_notes.md](workings/source_notes.md)
7. All assumptions documented in [workings/assumptions.md](workings/assumptions.md)

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Global e-commerce transaction count.** No single source tracks this. Our 57.5B figure is derived (GMV / AOV), introducing AOV sensitivity. A $10 shift in assumed AOV changes the count by ~5B.
- **The true global Average Order Value (AOV).** Western sources cite $116-145; Asia-Pacific AOV is $60-80. The blended $110 is a weighted estimate, not a measured global figure.
- **Platform-level transaction counts for most retailers.** Only Alibaba (~14.5B), Amazon (~4.5B), and Shopify (~3B) disclose order counts. The "long tail" of e-commerce (50%+ of GMV) is untracked by count.
- **Social commerce transaction volume.** TikTok Shop, Instagram Shopping, and WeChat mini-program commerce are growing explosively but report GMV, not order counts. Social commerce may already be 15-20% of total e-commerce orders.
- **Cross-border e-commerce share by volume.** Cross-border is ~15% of e-commerce by value, but average order values are higher — so it may be only ~8-10% by transaction count.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Global transaction count | Cross-check: sum platform-disclosed counts (Alibaba 14.5B + Amazon 4.5B + Shopify 3B = 22B) represents ~38% of estimated 57.5B; if these platforms are ~40% of GMV, the ratio is consistent | Platform annual reports and SEC filings | 🟡 |
| Asia-Pacific AOV | Use Alibaba's disclosed GMV (~$900B) / orders (~14.5B) = ~$62 as APAC anchor; weight against Japan (~$95) and SE Asia (~$45) | Alibaba, Rakuten, Shopee quarterly disclosures | 🟡 |
| Social commerce orders | TikTok Shop US: $15.82B GMV at ~$30 AOV = ~527M orders. Scale globally: if TikTok Shop is ~$50B global GMV, that's ~1.7B orders. Add WeChat mini-programs, Instagram: ~3-5B total social orders | eMarketer TikTok Shop data; Tencent mini-program GMV disclosures | 🔴 |
| Payment processor cross-check | PayPal ($1.68T TPV) + Stripe ($1.40T) + Adyen ($1.38T) = $4.46T. These three handle ~70% of Western e-commerce. At ~$100 AOV, that's ~44.6B transactions through these processors alone — but this includes in-store (Adyen), subscriptions, and non-retail | PayPal, Stripe, Adyen annual reports | 🟡 |
| Return rate adjustment | E-commerce return rates are 20-30% (vs. 8-10% in-store). If 57.5B orders generate ~14B returns (each a separate refund transaction), the true payment event count is ~71.5B | NRF return rate surveys; Shopify merchant data | 🔴 |

### Key Modeling Questions
- Should returns/refunds be counted as separate transactions? A return generates a refund payment that hits card networks as a credit. If so, e-commerce's "true TPS impact" is ~25% higher than order count alone.
- The Worldpay GPR reports 53% of e-commerce value is paid by digital wallets. But in China and India, the wallet IS the default checkout method. Does this mean 53% of e-commerce orders are double-counted with Digital Wallets?
- How should subscription e-commerce be treated? Netflix, Spotify, and SaaS are technically "e-commerce" (card-not-present) but are recurring billing, not shopping. They may add 10-15B annual transactions.
- Alibaba stopped disclosing peak TPS after 2021 (last reported: 583K orders/sec in 2020). If GMV grew ~15% since then, is the realistic 2024 peak ~670K orders/sec?

### Reference Comparisons
- **China vs. US e-commerce penetration:** China's e-commerce is ~30% of retail sales; the US is ~16%. If the US reached China's penetration at US price levels, US e-commerce GMV would roughly double to ~$3.8T.
- **India as growth frontier:** India's e-commerce is ~7% of retail (~$120B GMV in 2024). At China's 30% penetration rate, India would reach ~$500B — a 4x opportunity that could add 5-8B annual transactions.
- **Platform concentration:** The top 10 e-commerce platforms (Alibaba, Amazon, JD, Pinduoduo, Shopify merchants, eBay, Rakuten, MercadoLibre, Shopee, Temu) account for ~60% of global GMV but probably ~65-70% of order count (lower AOV on Chinese/SE Asian platforms).

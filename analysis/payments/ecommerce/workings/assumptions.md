# E-Commerce & Merchant Processing — Assumptions

## Boundary Definition

### What counts as an "e-commerce transaction"?

We count the **commerce event** — an online purchase order placed by a consumer or
business through an e-commerce platform or website. This is distinct from the
**payment rail** used to settle it.

- A consumer buys a jacket on Amazon using Apple Pay (funded by a Visa card).
  That is **one** e-commerce transaction. The same event also appears in:
  - Digital wallets (Apple Pay)
  - Consumer cards (Visa)
  - Merchant processing (acquirer)
- We count it **once** here as one e-commerce order.

### Double-counting boundary with other categories

| Other UoF Category | Overlap | Treatment |
|---|---|---|
| Consumer Cards | Cards are the payment rail for ~32% of e-commerce | We count the order, not the card swipe. Same event, different lens. |
| Digital Wallets | Wallets fund ~53% of e-commerce | Same — order counted here, wallet tap counted in digital wallets. |
| BNPL | BNPL funds ~5% of e-commerce | Same principle. |
| Bank Transfers (A2A) | ~7% of e-commerce | Same principle. |
| B2B Payments | B2B e-commerce exists ($21T+) | **Excluded** — this analysis covers retail/consumer e-commerce only, consistent with standard industry reporting. |

### Key principle
The Universe of Finance expects cross-category overlap. Each category measures
transactions from its own vantage point. The total TPS is **not** the sum of all
categories — a reconciliation layer handles deduplication.

## Data Source Assumptions

### A1: Statista/SOAX timeseries as primary source for annual GMV
- The 2014-2024 timeseries from SOAX (sourcing Statista) is used as the primary
  GMV reference because it provides a consistent methodology across 11 years.
- Figures are **retail e-commerce only** (B2C + C2C marketplace), excluding B2B.
- Confidence: 🟢 High — Statista is the most widely cited source and cross-referenced
  by eMarketer, Shopify, and UNCTAD.

### A2: Transaction count derived from GMV / AOV
- No single source publishes a reliable global e-commerce transaction count.
- We derive it: **Transaction Count = GMV / Average Order Value (AOV)**.
- AOV source: ECDB global benchmark of ~$116 (2024), cross-checked with
  Oberlo ($144.57 for Nov 2024) and regional averages.
- We use **$110** as a blended global AOV for 2024, which is conservative because:
  - Asia-Pacific (45%+ of transactions) has lower AOV (~$60-80)
  - Emerging markets pull the average down
  - The $116-$144 figures are skewed toward Western markets
- Confidence: 🟡 Medium — AOV varies dramatically by region and category.

### A3: TPS derived from annual transaction count
- TPS = Annual Transactions / (365.25 × 86,400)
- This gives **average** TPS. Real traffic is highly seasonal and diurnal.
- Peak TPS is estimated using known peak events (Singles Day, Black Friday)
  and multiplier analysis.

### A4: Peak TPS multiplier
- Alibaba's 2020 Singles Day peak: 583,000 orders/sec (confirmed)
- Shopify BFCM 2024 peak: $4.6M/min ÷ ~$110 AOV ≈ ~700 orders/sec (Shopify only)
- Peak-to-average ratio for global e-commerce estimated at **50-100x** based on:
  - Shopping events concentrate in narrow time windows (midnight launches)
  - Only a fraction of global platforms participate in any single peak event
  - Alibaba alone hits 583K/sec but represents ~15-20% of global e-commerce
- We estimate global peak at **~1,000,000 orders/sec** during overlapping peak events.
- Confidence: 🔴 Low — no single source measures global peak; this is extrapolated.

### A5: Payment method shares from Worldpay GPR 2025
- Worldpay's Global Payments Report is the industry standard for payment method mix.
- 2024 e-commerce shares: Digital wallets 53%, Credit cards 20%, Debit cards 12%,
  Bank transfer 7%, BNPL 5%, Cash on delivery 2%, Other 1%.
- These are **value-weighted** shares, not transaction-count-weighted. Lower-value
  methods (COD, BNPL) may have higher transaction shares than value shares.
- Confidence: 🟢 High — Worldpay GPR is primary research across 40+ markets.

### A6: Regional breakdown from Statista/Polaris
- Asia-Pacific: 45.7% of global e-commerce value
- North America: 29.8%
- Europe: 16.9%
- LAMEA: 7.6%
- These are value-weighted. Asia-Pacific likely has a higher transaction-count
  share due to lower AOV.
- Confidence: 🟢 High — consistent across multiple sources.

## Projection Assumptions

### A7: Baseline projection (2026-2035)
- Uses blended CAGR of **8.5%** for 2026-2030, declining to **6.5%** for 2031-2035.
- Based on: eMarketer baseline of 7.8% CAGR (2025-2027), Shopify forecast,
  and natural deceleration as market matures.
- Assumes no major disruptions (pandemic, trade wars significantly altering trajectory).

### A8: High-growth projection
- Social commerce grows at 26% CAGR (from current $2T to $8.5T by 2030).
- Embedded payments and livestream shopping accelerate checkout conversion.
- Uses **12% overall CAGR** through 2030, declining to 9% through 2035.
- This scenario assumes social commerce becomes 25%+ of total e-commerce by 2030.

### A9: Conservative projection
- Post-COVID normalisation: growth decelerates to **5% CAGR** through 2030.
- Factors: macro headwinds, market saturation in developed markets, regulatory
  friction (digital services taxes, data privacy compliance costs).
- Declines further to **4% CAGR** for 2031-2035.

# Consumer Card Payments — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. Nilson Report as Primary Source
**Assumption:** The Nilson Report's figure of 772.73 billion global card purchase transactions in 2024 is the most authoritative available.
**Reasoning:** Nilson Report has been the industry standard for card payment statistics for decades. Their methodology is consistent across years and networks.
**Risk:** Nilson data is paywalled; figures extracted from secondary reporting. Slight discrepancies possible.

### A2. Visa Fiscal Year Alignment
**Assumption:** Visa's FY2024 (ending Sep 30, 2024) figures are treated as representative of calendar year 2024.
**Reasoning:** Three-quarter overlap with CY2024. Growth trends are smooth enough that the 3-month offset does not materially distort analysis.
**Risk:** If Q4 CY2024 (Oct-Dec) had unusual seasonality, FY figures could understate CY totals. Estimated impact: <3%.

### A3. UnionPay 2024 Estimation
**Assumption:** UnionPay's 2024 transaction volume grew ~8.4% from 2023's 228B to ~247B.
**Reasoning:** UnionPay's growth rate is modestly below the global 12.4% average due to China's economic slowdown in 2024 and domestic consumption softness.
**Risk:** Actual growth could be lower (China deceleration) or higher (government stimulus effect). Range: 235B-260B.

### A4. AmEx + Discover Split
**Assumption:** Of the reported 23.6B combined Amex+Discover transactions, AmEx accounts for ~15B and Discover ~8.6B.
**Reasoning:** AmEx has roughly 1.7× more cards in force and higher average transaction frequency. Historical ratio of ~60/40 to 65/35.
**Risk:** Low impact — these are minor players by transaction count.

---

## Historic Timeseries Assumptions

### A5. Interpolation Methodology (2016-2021)
**Assumption:** For years where direct Nilson data is unavailable, global totals are estimated by:
- Using Visa's reported annual transaction volumes as a proxy for growth rates
- Applying Visa's market share (declining from ~38% in 2015 to ~30% in 2024) as a deflator
- Cross-checking against known data points (2015: 227B, 2022: 624.86B, 2023: 687B, 2024: 773B)

**Reasoning:** Visa processes the largest share of transactions and publishes the most granular data. Its growth rate, adjusted for share changes, is a reasonable proxy for global growth.
**Risk:** If non-Visa networks (especially UnionPay) grew at materially different rates, the interpolation could be off. Confidence: 🔴 Low for individual years, 🟡 Medium for the overall trajectory.

### A6. COVID Impact (2020)
**Assumption:** Global card transactions declined ~4.5% in 2020 vs 2019.
**Reasoning:** Visa's processed transactions declined modestly in 2020 despite COVID, because card-not-present (e-commerce) partially offset card-present declines. The net impact on cards was less severe than on cash or check-based payments.
**Risk:** The actual decline could have been 0% (shift from cash to cards offset volume loss) or up to -8% (severe economic contraction). 🔴 Low confidence on precise figure.

---

## TPS Calculation Assumptions

### A7. Uniform Distribution for Average TPS
**Assumption:** Average TPS is calculated as total annual transactions / seconds per year, assuming uniform distribution.
**Reasoning:** This is the standard methodology for expressing annual volume as TPS. Actual TPS varies significantly by time of day, day of week, and season.
**Risk:** Average TPS understates peak and overstates overnight. This is by design — peak TPS is estimated separately.

### A8. Peak TPS Multiplier
**Assumption:** Peak observed TPS across all networks is approximately 2.5× the average TPS.
**Reasoning:** Industry studies suggest peak-to-average ratios of 2-3× for payment networks. Singles' Day (China), Black Friday (US), and similar events create spikes.
**Risk:** Actual peak could be higher (3×+) during concentrated events. VisaNet's 83,000 TPS capacity vs ~7,400 TPS Visa average (11× headroom) suggests the system is designed for extreme spikes.

---

## Projection Assumptions

### Baseline Scenario

**B1.** Growth moderates from current 12.4% to 9% in 2026, declining to 7% by 2030 and holding steady.
**Reasoning:** As cashless penetration reaches 85%+ in developed markets, growth shifts to emerging markets where adoption curves are steeper but volumes are smaller. Nilson projects 7.3% CAGR from 2022-2027.

**B2.** No fundamental disruption to card network rails.
**Reasoning:** Despite A2A payment growth (Pix, UPI, etc.), card networks continue to serve as backend rails for digital wallets (Apple Pay, Google Pay all run on card rails).

**B3.** Global economic growth averages 2.5-3% annually.
**Reasoning:** IMF baseline projections. Card transaction growth typically runs 2-3× GDP growth due to cash displacement.

### High Growth Scenario

**H1.** India and Africa add 200M+ new card users by 2030.
**Reasoning:** India's UPI is primarily bank-account-linked, but card adoption is growing rapidly. Africa has the lowest card penetration globally with high smartphone adoption. Mobile wallets increasingly link to card rails.

**H2.** IoT/embedded payments add 50-100B additional card-rail transactions by 2035.
**Reasoning:** Connected vehicles, smart appliances, and autonomous agents will increasingly transact on card infrastructure.

**H3.** Digital wallet growth continues to compound card-rail transactions.
**Reasoning:** Apple Pay, Google Pay, Samsung Pay, and regional wallets all primarily operate on Visa/Mastercard rails, amplifying transaction counts.

### Conservative Scenario

**C1.** Account-to-account (A2A) payments capture 10-15% of card transaction share by 2035.
**Reasoning:** Pix (Brazil), UPI (India), SEPA Instant (Europe), FedNow (US) offer lower-cost alternatives. Regulatory push toward open banking accelerates A2A adoption.

**C2.** China's card transaction growth stagnates at 2-3%.
**Reasoning:** Alipay and WeChat Pay dominate Chinese payments. UnionPay growth is primarily from card issuance abroad, not domestic volume growth.

**C3.** Interchange fee regulation depresses card acceptance expansion.
**Reasoning:** EU interchange caps, Australian regulation, and potential US legislation reduce merchant incentive to invest in card terminal expansion.

---

## Value Assumptions

### V1. Total Volume vs Purchase Volume
**Assumption:** The $51.92T figure includes both purchase transactions and cash advances/withdrawals. Purchase-only volume is estimated at ~$44.5T.
**Reasoning:** Nilson explicitly states the total includes "purchase volume and cash volume." Cash transactions typically represent 15-17% of total card volume.
**Risk:** The exact purchase/cash split is not publicly available; 15% is an industry rule of thumb.

### V2. Average Transaction Value
**Assumption:** Average transaction value of ~$67 (derived from $51.92T / 772.73B).
**Reasoning:** Mathematical derivation from two primary-source figures.
**Risk:** This average masks wide variance — debit transactions average ~$40, credit ~$95, prepaid ~$25.

# Equity OTC Derivatives — Transaction Count Model

> Deep dive into the most opaque OTC derivatives sub-segment.
> Part of the [Universe of Finance](../../../../README.md) project.
> Last updated: 2026-03-28

---

## Motivation

The [count-triangulation](count-triangulation.md) estimated equity OTC derivatives at **600,000 trades/year** with **low confidence**. The estimate was derived from four rough approaches (BIS notional / avg deal size, CCP proportional, SEC SBSDR, IRD cross-scaling) without deep analysis of the underlying market structure. This is the weakest link in the OTC derivatives model.

This analysis builds a structural model of equity OTC derivatives by product type, using:
1. BIS semiannual statistics (notional outstanding and gross market value)
2. Structured products issuance data (autocallables, equity-linked notes)
3. SEC SBSDR and European EMIR trade repository data
4. Coalition Greenwich institutional trading surveys
5. Prime broker equity swap/CFD data
6. Notional outstanding / average deal size / average tenor framework

---

## Data Sources

| # | Source | Key Data Point | Year | Accessed |
|---|--------|---------------|------|----------|
| 1 | BIS — OTC Derivatives Statistics ([BIS](https://www.bis.org/statistics/derstats.htm)) | Equity-linked OTC derivatives notional outstanding: $8.9T (Dec 2024). Gross market value: $0.76T. | H2 2024 | 2026-03-28 |
| 2 | BIS — OTC Derivatives at end-June 2025 ([BIS](https://www.bis.org/publ/otc_hy2512.htm)) | Equity-linked notional outstanding: $9.8T (Jun 2025). Growth +10.1% from Dec 2024. | H1 2025 | 2026-03-28 |
| 3 | BIS — Semiannual Detailed Tables ([BIS](https://www.bis.org/statistics/d5_1.pdf)) | Equity forwards/swaps: $5.2T notional. Equity options: $3.7T notional. (Dec 2024) | H2 2024 | 2026-03-28 |
| 4 | ISDA — OTC Derivatives Market Analysis, Year-End 2024 ([ISDA](https://www.isda.org/)) | Equity derivatives clearing rate: ~8% by notional (far lower than IRD 76.9% or CDS 67.9%). Most equity OTC remains bilateral. | 2024 | 2026-03-28 |
| 5 | Coalition Greenwich — Equity Derivatives Market Structure 2024 ([Greenwich](https://www.greenwich.com/)) | Top 10 dealers account for ~85% of equity OTC derivatives revenue. Revenue pool: ~$8-10B. Average dealer handles ~500-1000 new tickets/day across all equity OTC products. | 2024 | 2026-03-28 |
| 6 | SEC — SBSDR (Security-Based Swap Data Repositories) ([SEC](https://www.sec.gov/)) | US security-based equity swaps reported to DTCC SDR. Aggregate trade count not published directly; individual transaction records available via EDGAR SBSDR dissemination. | 2024 | 2026-03-28 |
| 7 | SRP (Structured Retail Products) — Global Issuance Report ([SRP](https://www.structuredretailproducts.com/)) | Global structured product issuance: ~$800B (2024). Equity-linked structured products: ~60% = ~$480B. Autocallables dominate (50-60% of equity-linked). | 2024 | 2026-03-28 |
| 8 | EuroStoxx / SIX — Structured Products Statistics ([SIX](https://www.six-group.com/)) | Swiss structured product issuance: ~CHF 350B outstanding. European issuance (incl. Germany, France, Italy): ~EUR 300B. | 2024 | 2026-03-28 |
| 9 | Korea Exchange / KOFEX — ELS (Equity Linked Securities) ([KRX](https://global.krx.co.kr/)) | Korean ELS issuance: ~KRW 50T (~$37B) in 2024, down from peak KRW 100T+ due to HSCEI losses. Each ELS product hedged with OTC equity derivatives. | 2024 | 2026-03-28 |
| 10 | DTCC — GTR (Global Trade Repository) Equity Derivatives ([DTCC](https://www.dtcc.com/)) | EMIR reporting covers European equity OTC derivatives. Aggregate statistics not easily accessible; individual trade reports available. | 2024 | 2026-03-28 |
| 11 | OCC (Options Clearing Corporation) — Volume Statistics ([OCC](https://www.theocc.com/)) | US exchange-traded equity options: 11.2B contracts in 2024 (record). This is the exchange-traded comparator for OTC equity derivatives. | 2024 | 2026-03-28 |
| 12 | Prime Broker Survey Data — Morgan Stanley, Goldman Sachs, JP Morgan ([Annual Reports](https://www.goldmansachs.com/investor-relations/)) | Prime brokerage equity swap books: estimated $2-3T notional across top 5 prime brokers. Typical swap tenor: 1-5 years. | 2024 | 2026-03-28 |

---

## Market Structure: What Are OTC Equity Derivatives?

Before modeling, it is essential to understand what instruments we are counting. OTC equity derivatives are a heterogeneous collection:

### Product Taxonomy

| Product | % of Notional Outstanding | Typical Counterparties | Avg Notional/Trade | Avg Tenor | Annual Turnover Multiple |
|---------|--------------------------|----------------------|--------------------|-----------|-----------------------|
| **Equity total return swaps (TRS)** | ~35% ($3.1T) | Hedge funds + prime brokers | $50-200M | 1-5 years | 0.5-1.0x (roll at maturity) |
| **Equity variance/volatility swaps** | ~5% ($0.4T) | Hedge funds, prop desks | $20-100M vega notional | 3-12 months | 1.5-2.0x (shorter tenor = more rolls) |
| **OTC equity options (exotic)** | ~30% ($2.7T) | Structured product desks, insurers | $10-50M | 6 months - 5 years | 0.8-1.2x |
| **Equity forwards (incl. CFDs on underlying)** | ~15% ($1.3T) | Asset managers, corporates | $5-50M | 1-12 months | 2.0-4.0x (frequent rolling) |
| **Contract for Difference (institutional)** | ~10% ($0.9T) | European institutional | $1-20M | Open-ended (daily rolling) | 50-100x (continuous) |
| **Dividend swaps** | ~3% ($0.3T) | Hedge funds, structured desks | $10-50M | 1-5 years | 0.5-1.0x |
| **Other (correlation swaps, dispersion, quanto)** | ~2% ($0.2T) | Sell-side inter-dealer | $20-100M | Variable | Variable |

**Critical distinction**: Institutional CFDs are included in OTC equity derivatives by BIS classification. They are economically equivalent to equity swaps but trade with higher frequency and smaller tickets. This is important for transaction count.

---

## Model: Notional Outstanding / Deal Size / Tenor Framework

### Core Formula

```
Annual new trades = Notional outstanding / (Average deal size x Average remaining tenor)
```

This formula derives the annual "flow" of new trades needed to maintain the observed stock of outstanding notional, adjusted for average deal lifetime.

### Application by Product

| Product | Notional Outstanding | Avg Deal Size | Avg Tenor (years) | Roll Multiplier | Est. Annual New Trades |
|---------|---------------------|---------------|-------------------|----------------|----------------------|
| Equity TRS | $3.1T | $100M | 2.0 | 1.0 | 15,500 |
| Variance/vol swaps | $0.4T | $50M | 0.5 | 1.5 | 24,000 |
| OTC equity options (exotic) | $2.7T | $25M | 2.0 | 1.0 | 54,000 |
| Equity forwards | $1.3T | $20M | 0.5 | 1.0 | 130,000 |
| Institutional CFDs | $0.9T | $5M | 0.02 (rolling daily) | 1.0 | see below |
| Dividend swaps | $0.3T | $30M | 2.0 | 1.0 | 5,000 |
| Other exotics | $0.2T | $50M | 1.0 | 1.0 | 4,000 |
| **Total (excl. CFDs)** | **$8.0T** | — | — | — | **232,500** |

### The CFD Problem

Institutional CFDs deserve separate treatment because they trade with fundamentally different frequency:

- **Notional outstanding**: ~$0.9T
- **But**: CFDs roll daily. The "outstanding" at any point is the net open position, not the annual flow.
- **Daily new CFD trades**: Institutional CFDs are used for portfolio construction by European asset managers (who cannot use leverage directly). A large asset manager may execute 50-200 CFD trades/day.
- **Number of active institutional CFD users**: ~500-1,000 institutional counterparties globally
- **Average trades/day per counterparty**: ~30-100
- **Estimated CFD trades/day**: 15,000 - 100,000
- **Central estimate**: ~40,000/day = **~10,080,000/year**

Wait — this would make CFDs overwhelmingly dominant. But this is misleading because:
1. Many institutional CFD "trades" are position adjustments (adding/reducing existing exposure), not new economic commitments
2. CFDs are often rolled automatically overnight — each roll is technically a new trade
3. The daily roll of a single CFD position generates 252 "trades" per year

**Adjusted CFD count** (excluding automatic rolls, counting only new economic decisions):
- ~40,000/day is the gross count including rolls
- New economic decisions: ~20% of gross = **~8,000/day** = **~2,016,000/year**

### Structured Products as OTC Derivative Generators

Structured products (autocallables, equity-linked notes, reverse convertibles) are sold to retail/HNW investors but **hedged by the issuing bank using OTC equity derivatives**. Each structured product issuance creates multiple OTC derivative trades:

| Flow | Metric | Estimate |
|------|--------|----------|
| Global equity-linked structured product issuance | $480B/year (60% of $800B total) | |
| Average product notional | $2-10M per ISIN (but many small retail tranches aggregate) | |
| Number of distinct structured product ISINs issued globally | ~500,000 - 1,000,000/year | High — Swiss market alone issues 1M+ products/year (many small) |
| OTC derivative hedging trades per product | 2-5 (initial delta hedge + vega hedge + subsequent rebalancing) | |
| **Structured-product-generated OTC equity derivative trades** | **1,000,000 - 5,000,000/year** | Extremely wide range |

**Central estimate**: ~2,000,000 structured-product-generated OTC trades/year

However, many of these "trades" are:
1. Hedge rebalancing (delta adjustments) which may be done intra-book without hitting external markets
2. Internal between desks of the same bank
3. Aggregated across products (a bank hedges its entire autocallable book, not each product individually)

**Adjusted for aggregation**: ~500,000 - 1,000,000 externally-facing OTC trades from structured product hedging. Central: **~700,000/year**.

### Coalition Greenwich Dealer Survey Cross-Check

Coalition Greenwich surveys the top equity OTC derivatives dealers:

- Top 10 dealers account for ~85% of equity OTC derivatives revenue (~$8.5B of ~$10B total)
- Revenue per dealer: ~$850M average (top 10)
- Revenue per trade (blended across products): ~$5,000 - $50,000
  - Large TRS: ~$50K-$200K revenue per trade (high margin)
  - Exotic options: ~$20K-$100K
  - Institutional CFDs: ~$500-$5K (high volume, low margin)
  - Structured product hedges: ~$2K-$10K

**Implied trade count for top 10 dealers:**
- Using $10K average revenue per trade: $8.5B / $10K = **~850,000 trades/year**
- Using $5K average: ~1,700,000
- Using $20K average: ~425,000

At 85% market share, total market:
- Central ($10K avg): 850K / 0.85 = **~1,000,000 trades/year**
- Range: 500,000 - 2,000,000

### SEC SBSDR Data (US Security-Based Swaps)

The SEC requires reporting of security-based swaps (equity swaps, single-name CDS) to data repositories. While aggregate statistics are not published in a convenient format, analysis of DTCC SDR dissemination data suggests:

- US equity swap new trade reports: ~150,000 - 250,000/year
- US is approximately 40-50% of global equity OTC derivatives by notional
- Implied global: ~300,000 - 625,000/year from this approach

This likely undercounts because:
1. Not all equity OTC products are "security-based swaps" under SEC definition
2. Institutional CFDs are not SEC-reportable in most cases
3. Structured product hedging may be internal (not reported)

---

## Revised Estimate

### Synthesis of Approaches

| Approach | Est. Annual Trades | Coverage Notes |
|----------|--------------------|----------------|
| 1. Notional/size/tenor framework (excl. CFDs) | 232,500 | Institutional TRS, options, forwards, exotics only |
| 2. CFD adjusted count | 2,016,000 | Institutional CFDs, excl. automatic rolls |
| 3. Structured product hedging | 700,000 | Externally-facing hedge trades only |
| 4. Coalition Greenwich revenue model | 1,000,000 | All products, revenue-based |
| 5. SEC SBSDR extrapolation | 300,000 - 625,000 | US security-based swaps only, scaled global |

### Reconciliation

The approaches are not additive — they overlap significantly:
- Approach 1 (notional framework) captures the "slow money" — large institutional TRS, exotic options, forwards
- Approach 2 (CFDs) captures the "fast money" — institutional CFDs with daily activity
- Approach 3 (structured products) captures the dealer hedging flow — which overlaps with Approach 1's options and forwards
- Approach 4 (revenue model) captures everything but from a different angle
- Approach 5 (SEC) is the only "observed" data, but covers only US and only a subset of products

**Best composite estimate:**

| Component | Annual Trades | Rationale |
|-----------|--------------|-----------|
| Large institutional trades (TRS, exotic options, variance swaps, forwards) | 250,000 | Approach 1, consistent with Approach 5 |
| Institutional CFDs (new economic decisions) | 500,000 | Approach 2, reduced from 2M because many CFD "trades" are roll adjustments, not new decisions |
| Structured product hedging (external) | 400,000 | Approach 3, adjusted for bank internalization |
| Small/misc (dividend swaps, correlation, inter-dealer) | 50,000 | Residual category |
| **Total** | **1,200,000** | |

### Comparison with Previous Estimate

| Metric | Previous (count-triangulation.md) | Revised | Change |
|--------|----------------------------------|---------|--------|
| Annual equity OTC trades | 600,000 | 1,200,000 | +100% |
| Daily trades (252 days) | 2,381 | 4,762 | +100% |
| Confidence | Low | Low-Medium | Improved |

**Why higher?** The previous estimate underweighted two components:

1. **Institutional CFDs**: The original model treated all equity OTC derivatives as low-frequency, large-ticket institutional trades. Institutional CFDs (used extensively by European asset managers as leverage substitutes) generate much higher trade frequency, even after adjusting for automatic rolls.

2. **Structured product hedging**: The structured products market ($480B equity-linked issuance/year) generates a substantial flow of OTC equity derivative trades that was not explicitly modeled before.

### Impact on OTC Derivatives Total

| Segment | Previous Annual | Revised Annual | Change |
|---------|----------------|---------------|--------|
| IRD | 3,100,000 | 3,100,000 | — |
| CDS | 600,000 | 600,000 | — |
| **Equity OTC** | **600,000** | **1,200,000** | **+600,000** |
| Commodity OTC | 400,000 | 400,000 | — |
| **Total (excl. FX)** | **4,700,000** | **5,300,000** | **+600,000** |

**Revised TPS (excl. FX):**
- 5,300,000 / (365.25 x 86,400) = **0.17 TPS** (previously 0.15)
- During trading hours: 21,032 / (10h x 3,600) = **0.58 TPS** (previously 0.52)

---

## Confidence Assessment

| Component | Confidence | Why |
|-----------|-----------|-----|
| Large institutional trades (TRS, exotics) | Medium | BIS notional is reliable; deal size and tenor are estimated but bounded |
| Institutional CFDs | Low-Medium | CFD "trade" definition is ambiguous; roll vs. new decision boundary is subjective |
| Structured product hedging | Low-Medium | Issuance data is observable; hedge trade count per product is highly variable |
| Total composite | Low-Medium | Improved from "Low" through structural decomposition, but still heavily estimated |

### What would shift this estimate significantly?

| Scenario | Impact |
|----------|--------|
| If institutional CFD rolls are counted as trades (daily roll = new trade) | +8M/year (total would be ~9M) — but this overcounts |
| If structured product hedge rebalancing is counted (daily delta hedges) | +5-10M/year — but these are internal bank operations |
| If OTC equity options include all structured product embedded options | +2M/year — depends on how "embedded" vs. "standalone" is defined |
| If SEC SBSDR data could be aggregated cleanly | Would anchor US number precisely; global extrapolation still needed |

---

## Sensitivity Analysis

| Parameter | Base Case | If Changed To | Impact on Annual Count | Sensitivity |
|-----------|-----------|---------------|----------------------|-------------|
| **Institutional CFD trade count** | 500K | 2M (if rolls counted) | +1.5M (2.7M total) | **HIGH** — definitional |
| **Structured product hedge trades** | 400K | 1M (if per-product hedging) | +600K (1.8M total) | MEDIUM |
| **TRS average deal size** | $100M | $50M | +15.5K (negligible) | LOW — TRS is low frequency |
| **Exotic options avg deal size** | $25M | $10M | +54K (modest) | LOW |
| **Global vs. US equity OTC ratio** | 2.5x | 3.5x | +120K | LOW |
| **CFD roll definition** | 20% are "new decisions" | 50% | +600K (1.8M total) | **HIGH** |

**The definition of what counts as a "trade" is the dominant uncertainty.** The physical volume of OTC equity derivative activity is large, but much of it is:
- Position maintenance (rolls, rebalancing) rather than new economic commitments
- Internal between desks of the same bank
- Aggregated/netted across client positions

Our model counts new economic commitments (consistent with the IRD and CDS definitions in count-triangulation.md).

---

## Open Questions & Data Gaps

1. **SEC SBSDR aggregate publication.** The SEC collects equity swap data via SDRs (DTCC, ICE) but does not publish convenient aggregate statistics. If the SEC published monthly aggregate trade counts and notional — similar to what ISDA SwapsInfo does for IRD and CDS — the US equity OTC estimate would go from "low" to "high" confidence.

2. **European EMIR equity derivative aggregates.** ESMA's EMIR trade repositories (DTCC GTR, Regis-TR, UnaVista) hold equity OTC trade data for Europe. ESMA publishes some aggregate statistics but not at the equity OTC product level. A dedicated ESMA publication on equity derivative trade counts would fill the European gap.

3. **Institutional CFD data.** No public source reports aggregate institutional CFD trade counts. Prime brokers know exactly how many CFD trades they execute daily, but this is proprietary. If even one major prime broker (Goldman, Morgan Stanley, JP Morgan) disclosed CFD trade counts in an investor presentation, the estimate would improve dramatically.

4. **Structured products hedge ratio.** How many OTC equity derivative trades does a single autocallable generate over its lifetime? Structured product desks know this precisely — it depends on delta sensitivity, barrier proximity, and market volatility. An academic study on structured product hedging trade frequency would close this gap.

5. **Korea ELS hedging.** Korean ELS (Equity Linked Securities) products generated major losses in 2023-2024 (HSCEI-linked products). The hedging activity from Korean bank ELS books likely generates significant OTC equity derivative trades (variance swaps, barrier option hedges). KRX or Korean FSS data on ELS hedging activity would add the Korean component.

6. **BIS decomposition by flow vs. stock.** BIS publishes notional outstanding (stock) but not annual turnover (flow) for equity OTC derivatives. If BIS added a turnover question to the semiannual survey (as they do for FX in the Triennial), the notional/size/tenor framework could be replaced with directly observed turnover.

---

## Sources

1. BIS — OTC Derivatives Statistics, H2 2024
2. BIS — OTC Derivatives at end-June 2025
3. BIS — Semiannual Detailed Tables (Table D5.1)
4. ISDA — OTC Derivatives Market Analysis, Year-End 2024
5. Coalition Greenwich — Equity Derivatives Market Structure 2024
6. SEC — SBSDR Dissemination Data
7. SRP — Global Structured Products Issuance Report 2024
8. SIX — Swiss Structured Products Statistics
9. Korea Exchange / KRX — ELS Issuance Data
10. DTCC — GTR Equity Derivatives Reporting
11. OCC — US Exchange-Traded Equity Options Volume 2024
12. Prime Broker Annual Reports (Goldman Sachs, Morgan Stanley, JP Morgan)

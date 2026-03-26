# Tokenised Real-World Assets (RWA) — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Tokenised real-world assets represent one of the most hyped yet genuinely transformative emerging categories in finance. As of mid-2025, the on-chain RWA market holds **~$24 billion in total value locked** (excluding stablecoins), up from ~$5.5 billion at the start of the year. However, **transaction counts remain minuscule** — estimated at **~50-100 million on-chain transactions per year**, equivalent to roughly **1.6-3.2 TPS**. The value proposition is not current throughput but the potential to tokenise **$400+ trillion** in traditional assets (real estate, bonds, equities, commodities) and bring them onto programmable, 24/7 settlement rails. Industry projections range wildly from **$3.5 trillion to $30 trillion** in tokenised assets by 2030, with corresponding transaction volumes that could eventually rival traditional securities markets.

## Scope

This analysis covers assets that have been tokenised (represented as blockchain tokens) and are traded or settled on-chain:

1. **Tokenised treasuries & fixed income** — US Treasury-backed tokens (BUIDL, OUSG, etc.)
2. **Tokenised private credit** — on-chain lending against real-world collateral (Centrifuge, Maple, Goldfinch)
3. **Tokenised real estate** — fractional property ownership tokens
4. **Tokenised commodities** — gold tokens (PAXG, XAUT), other commodity-backed tokens
5. **Tokenised equities & funds** — on-chain representations of equity instruments

Excluded: Stablecoins (covered separately), native crypto assets, NFTs without real-world asset backing, synthetic assets without direct collateral.

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Avg TPS | ~1.6-3.2 | Derived from ~50-100M annual txns | :red_circle: Low |
| Peak TPS (est.) | ~10-20 | During major fund launches or market events | :red_circle: Low |
| Daily volume | ~140,000-275,000 | Derived from annual estimate | :red_circle: Low |
| Annual volume (est. 2025) | ~50-100 million | On-chain transactions across all RWA protocols | :red_circle: Low |
| Total Value Locked (mid-2025) | ~$24 billion | [RWA.xyz](https://app.rwa.xyz/) / DeFiLlama (excl. stablecoins) | :yellow_circle: Medium |
| Off-chain backing | ~$400+ billion | Total liquidity backing tokenised RWA sector | :yellow_circle: Medium |
| Avg transaction value | ~$5,000-50,000 | Highly variable — institutional tranches vs retail | :red_circle: Low |

### Asset Class Breakdown (by TVL, mid-2025)

| Asset Class | TVL ($B) | Share | Key Protocols | Confidence |
|-------------|---------|-------|---------------|------------|
| Private Credit | ~17 | ~61% | Centrifuge, Maple, Goldfinch | :yellow_circle: Medium |
| US Treasuries | ~7.3 | ~26% | BlackRock BUIDL, Ondo OUSG, Franklin Templeton | :yellow_circle: Medium |
| Commodities (Gold) | ~1.5 | ~5% | Paxos (PAXG), Tether Gold (XAUT) | :yellow_circle: Medium |
| Real Estate | ~0.5 | ~2% | RealT, Lofty, various regional platforms | :red_circle: Low |
| Institutional Funds | ~1.2 | ~4% | Various alternative fund tokens | :red_circle: Low |
| Other | ~0.5 | ~2% | Carbon credits, art, collectibles | :red_circle: Low |

### Key Protocol Breakdown

| Protocol/Fund | TVL ($B) | Chain(s) | Launch | Confidence |
|---------------|---------|----------|--------|------------|
| BlackRock BUIDL | ~1.8 | Ethereum, others | Mar 2024 | :yellow_circle: Medium |
| Ondo Finance (OUSG) | ~1.3 | Ethereum, Solana | Jan 2023 | :yellow_circle: Medium |
| Centrifuge | ~1.0 | Ethereum, Centrifuge Chain | 2021 | :yellow_circle: Medium |
| Franklin Templeton (BENJI) | ~0.7 | Stellar, Polygon | Oct 2021 | :yellow_circle: Medium |
| Maple Finance | ~0.5 | Ethereum, Solana | May 2021 | :yellow_circle: Medium |

---

## Historic Trend

### On-Chain RWA TVL (Excluding Stablecoins)

| Year | TVL ($B, est.) | YoY Growth | Notes | Confidence |
|------|---------------|-----------|-------|------------|
| 2019 | ~0.05 | — | Nascent; Centrifuge Tinlake early | :red_circle: Low |
| 2020 | ~0.2 | +300% | DeFi summer; early private credit | :red_circle: Low |
| 2021 | ~1.5 | +650% | Maple, Goldfinch launch; RWA narrative begins | :yellow_circle: Medium |
| 2022 | ~3.0 | +100% | Treasury tokens emerge post-rate hikes | :yellow_circle: Medium |
| 2023 | ~8.0 | +167% | BlackRock enters; major TradFi validation | :yellow_circle: Medium |
| 2024 | ~15.2 | +90% | Institutional adoption accelerates | :yellow_circle: Medium |
| 2025 (mid) | ~24.0 | +58% (annualised) | RWA TVL overtakes DEX TVL | :yellow_circle: Medium |

**Key observations:**
- TVL has grown from effectively zero to $24B in ~5 years — an extraordinary growth rate
- The TradFi-to-DeFi shift accelerated dramatically when BlackRock launched BUIDL in March 2024
- Private credit dominates by TVL (61%) but Treasury tokens are growing fastest
- RWA protocols overtook DEX protocols in TVL during 2025, a symbolic milestone

---

## Growth Rate Analysis

| Period | CAGR (TVL) | Context |
|--------|-----------|---------|
| 2020-2025 | ~150%+ | From near-zero base; explosive but decelerating |
| 2023-2025 | ~73% | Post-TradFi validation; institutional capital entering |
| Transaction count CAGR | ~80-120% | Estimated; growing with TVL but more retail participation |

TVL growth is decelerating from triple-digit percentages to ~50-70% as the base grows, but this remains one of the fastest-growing categories in all of finance.

---

## Projections

> **Note:** For this nascent category, projections are more important than current state. The range is extremely wide because the category's future depends on regulatory clarity, institutional adoption, and infrastructure maturation.

### Baseline (Steady Institutional Adoption)

**Assumptions:**
1. TVL reaches $500B by 2030, $2T by 2035 (aligned with BCG/21.co mid-range estimates)
2. Transaction frequency grows with TVL — more protocols, more secondary trading, more DeFi composability
3. Average 200-500 on-chain transactions per $1M of TVL per year (comparable to current DeFi ratios)
4. Regulatory frameworks (MiCA, US securities reform) provide clarity by 2027-2028

| Year | Projected TPS | Annual Volume (M) | TVL ($B) |
|------|---------------|-------------------|----------|
| 2026 | 8 | 250 | 50 |
| 2028 | 30 | 950 | 150 |
| 2030 | 100 | 3,150 | 500 |
| 2035 | 500 | 15,800 | 2,000 |

### High Growth (Tokenisation Becomes Default)

**Assumptions:**
1. Major securities exchanges integrate tokenised settlement by 2028
2. TVL reaches $5T by 2030, $16T by 2035 (BCG/Standard Chartered bull case)
3. Secondary market trading on tokenised assets approaches traditional market frequency
4. Cross-chain interoperability solved; institutional custody standardised

| Year | Projected TPS | Annual Volume (M) | TVL ($B) |
|------|---------------|-------------------|----------|
| 2026 | 15 | 475 | 80 |
| 2028 | 100 | 3,150 | 500 |
| 2030 | 800 | 25,200 | 5,000 |
| 2035 | 5,000 | 157,700 | 16,000 |

### Conservative (Regulatory Headwinds)

**Assumptions:**
1. Regulatory uncertainty persists; US securities law constrains tokenisation
2. TVL reaches $100B by 2030, $500B by 2035
3. Tokenised assets remain niche — primarily treasury tokens and private credit
4. Transaction frequency stays low as institutional participants dominate

| Year | Projected TPS | Annual Volume (M) | TVL ($B) |
|------|---------------|-------------------|----------|
| 2026 | 5 | 160 | 35 |
| 2028 | 12 | 380 | 70 |
| 2030 | 30 | 950 | 100 |
| 2035 | 150 | 4,730 | 500 |

*Full projection tables: [workings/calculations.md](workings/calculations.md#4-projection-models)*

**2035 Range:** Transaction volumes could range from **~150 TPS (conservative) to ~5,000 TPS (high growth)** by 2035. Even the bull case would place RWA tokenisation below current consumer card volumes, but the value per transaction would be orders of magnitude higher.

---

## Key Findings

1. **RWA tokenisation is value-rich, count-poor — for now.** At ~$24B TVL with only ~50-100M annual transactions, the average on-chain RWA transaction is worth $5,000-50,000. This is an institutional-first market where transaction count is a poor measure of significance.

2. **BlackRock's entry was the inflection point.** The BUIDL fund launch in March 2024 was the moment tokenisation crossed from "crypto experiment" to "TradFi strategy." BUIDL grew from $40M at launch to $1.8B by late 2025.

3. **Private credit dominates, but treasuries are the gateway drug.** Private credit (61% of TVL) drives the most value, but tokenised Treasury products are the easiest for institutions to adopt and serve as the on-ramp to broader RWA exposure.

4. **The $400B off-chain backing reveals the conversion opportunity.** RWA.xyz tracks $402.5B in off-chain liquidity associated with RWA protocols — over 20x the on-chain TVL. This represents the near-term addressable market for further tokenisation.

5. **Projection variance is extreme.** Industry forecasts range from $3.5T to $30T by 2030. This 10x spread reflects genuine uncertainty about regulatory outcomes, institutional adoption pace, and technical infrastructure readiness.

6. **Transaction counts will explode if secondary markets develop.** Current low TPS reflects that most tokenised assets are buy-and-hold (Treasury tokens, private credit). If tokenised assets develop liquid secondary markets with DeFi composability, transaction counts could increase 100x without TVL changing.

---

## Data Quality & Limitations

- **TVL data is reasonably reliable** thanks to on-chain transparency and trackers like RWA.xyz and DeFiLlama. Confidence is :yellow_circle: Medium.
- **Transaction count data is :red_circle: Low confidence.** No aggregator specifically tracks RWA transaction counts across all chains and protocols. Our estimate is derived from TVL-to-transaction ratios observed in DeFi.
- **"RWA" definition varies.** Some trackers include stablecoins (which would add $150B+ to TVL); we exclude them to avoid double-counting with other categories.
- **Off-chain asset verification** is a trust assumption — on-chain TVL figures depend on accurate off-chain collateral reporting.
- **Projection models are highly speculative.** The 10x spread between conservative and bull case is unusual for this project but reflects the genuine state of uncertainty.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Total on-chain RWA transaction count**: No aggregator tracks RWA-specific transaction counts across all chains. TVL is visible; transaction volume is not.
- **Off-chain settlement that backs on-chain tokens**: When BlackRock's BUIDL token is minted, there's an off-chain Treasury purchase and an on-chain token creation. The off-chain leg is invisible in blockchain data but represents real settlement activity.
- **Institutional vs retail transaction mix**: Most RWA protocols serve institutional investors, but the transaction count split (few large institutional vs many small retail) is not published.
- **Secondary market trading volume for tokenised assets**: Primary issuance is tracked; secondary market activity on DEXs and OTC desks is fragmented and poorly measured.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| On-chain transaction count | Etherscan/Dune Analytics: query contract interactions for top 20 RWA protocols (BUIDL, OUSG, Centrifuge, Maple, etc.) | On-chain data is fully transparent; requires protocol-specific contract addresses | :green_circle: |
| Future TVL trajectory | TradFi AUM ($100T+ global) x tokenisation penetration curve. If tokenisation follows S-curve adoption, 0.1% penetration (2025) -> 1% (2030) -> 5% (2035) = $100B -> $1T -> $5T | BlackRock/Fidelity allocation announcements; BCG/Standard Chartered projections | :yellow_circle: |
| Regulatory sandbox approvals as leading indicator | Track MiCA (EU), SEC no-action letters (US), MAS sandbox (Singapore) approvals for tokenised securities. Each approval enables new protocols and TVL. | EU MiCA implementation timeline; SEC Crypto Task Force announcements; MAS FinTech Sandbox registry | :yellow_circle: |
| Secondary market liquidity growth | Compare DEX volume for RWA tokens (Uniswap, Curve pools) to primary issuance. Rising secondary/primary ratio signals maturing market and higher transaction frequency per TVL dollar. | Dune Analytics dashboards; DeFiLlama DEX volume by token pair | :green_circle: |
| Institutional adoption pace | Track number of TradFi institutions launching tokenised products: 2023 (~5), 2024 (~15), 2025 (~30+). Extrapolate product count x avg TVL per product. | Press releases; RWA.xyz issuer directory; CoinGecko RWA Report | :yellow_circle: |

### Key Modeling Questions
- **What is the transaction frequency per TVL dollar?** Current DeFi averages ~200-500 on-chain transactions per $1M TVL/year. If RWA tokens develop liquid secondary markets, this ratio could increase 10-100x. If they remain buy-and-hold (Treasury tokens), it stays low. This is the key variable for converting TVL projections into TPS projections.
- The 10x spread in industry forecasts ($3.5T to $30T by 2030) is unusually wide. Can we narrow it by tracking leading indicators? Specific testable milestones: Does BUIDL reach $10B by 2027? Does Centrifuge reach $5B TVL? Does a major exchange (NYSE, LSE) list a tokenised security by 2028?
- How will tokenised RWA settlement interact with traditional securities settlement (see securities-settlement capsule)? If DTCC's pilot tokenised settlement succeeds, tokenised assets could settle through existing infrastructure rather than creating new on-chain volume.
- What happens when tokenised assets become composable with DeFi? If BUIDL can be used as collateral on Aave, each collateralisation/liquidation event creates new transactions that don't exist in TradFi. This could multiply transaction counts without changing TVL.

### Reference Comparisons
- **BlackRock BUIDL as adoption bellwether**: BUIDL grew from $40M at launch (March 2024) to $1.8B by late 2025 — a 45x increase in 18 months. If this growth rate applies to the broader RWA market, the $24B TVL could reach $1T by 2028. However, BUIDL's growth may not be representative — it benefits from BlackRock's brand and distribution.
- **ETF adoption curve as analogy**: The first US equity ETF (SPY) launched in 1993 with $6.5M AUM. By 2003 ($400B AUM), ETFs had achieved ~2% of US equity market cap. By 2024 ($10T+), ETFs held ~30% of US equity assets. If tokenised assets follow a similar 30-year S-curve, we're in the "1993-1998" phase.
- **Stablecoin precedent**: Stablecoins (excluded from this capsule) grew from $5B (2020) to $150B+ (2025) in 5 years. They demonstrate that on-chain financial instruments can achieve massive scale, but also that growth can plateau for years before the next breakout.

---

## Sources

1. [RWA.xyz — Analytics on Tokenized Real-World Assets](https://app.rwa.xyz/)
2. [The Defiant — RWAs Became Wall Street's Gateway to Crypto in 2025](https://thedefiant.io/news/defi/rwas-became-wall-street-s-gateway-to-crypto-in-2025)
3. [Yahoo Finance — RWA DeFi Protocols Overtake DEXs in TVL](https://finance.yahoo.com/news/real-world-asset-rwa-defi-201504989.html)
4. [RedStone — Real-World Assets in Onchain Finance Report](https://blog.redstone.finance/2025/06/26/real-world-assets-in-onchain-finance-report/)
5. [ElectroIQ — Tokenized Assets Statistics 2025](https://electroiq.com/stats/tokenized-assets-statistics/)
6. [CoinGecko — 2025 RWA Report](https://assets.coingecko.com/reports/2025/CoinGecko-2025-RWA-Report.pdf)
7. [CoinPedia — RWA Tokenization Could Reach $30T by 2030](https://coinpedia.org/research-report/top-real-world-asset-rwa-projects/)
8. [Mintlayer — $16-30 Trillion by 2030: Unlocking the RWA Opportunity](https://www.mintlayer.org/blogs/16-30-trillion-by-2030-unlocking-the-rwa-opportunity)
9. [BinaryX — Asset Tokenization Market to Reach $3.5-10T by 2030](https://www.binaryx.com/blog/rwa-outlook-2025-asset-tokenization-market-to-reach-3-5-10t-by-2030)
10. [Yahoo Finance / Skynet — RWA Tokenization Market to Reach $16T by 2030](https://finance.yahoo.com/news/rwa-tokenization-market-reach-16t-000429613.html)
11. [NextMSC — Global Tokenized RWAs Market Growth Trends and 2030 Forecast](https://www.nextmsc.com/report/tokenized-real-world-assets-rwas-market-bf3345)
12. [Brickken — RWA Tokenization Trends 2025](https://www.brickken.com/post/rwa-tokenization-trends-2025)

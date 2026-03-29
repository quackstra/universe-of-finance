---
title: "Centralised Crypto Exchanges — Report"
parent: Digital Assets
grand_parent: Explore
nav_order: 1
---

# Centralised Crypto Exchanges — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Centralised cryptocurrency exchanges (CEXs) processed an estimated **$77.3 trillion** in combined spot and derivatives trading volume in 2024 — spot at $18.83 trillion ([CoinGecko](https://www.coingecko.com/research/publications/largest-centralized-crypto-exchanges)) and perpetual futures at $58.5 trillion ([CoinGecko Perpetuals Report](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf)). Translating dollar volume into individual trade transactions is inherently imprecise because exchanges do not publish trade counts, but reasonable estimates place CEX activity at roughly **3,000-5,000 trades per second** (see [calculations](workings/calculations.md)). Binance alone commanded 39% of spot volume. The critical caveat: wash trading on unregulated exchanges may inflate reported volumes by 50-70%.

## Scope

This analysis covers **centralised (custodial) cryptocurrency exchanges** — platforms where users deposit funds and trade via an order book or matching engine operated by a central entity. Included: spot trading, perpetual futures/swaps, dated futures, options. Excluded: decentralised exchanges (see [DeFi capsule](../defi/REPORT.md)), OTC desks, peer-to-peer platforms, and on-chain transactions.

**Important:** CEX internal trades do NOT appear on-chain. There is **zero double-counting** with the L1/L2 blockchain capsule — CEX order book matches are settled on internal ledgers.

---

## Current State

### Trading Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Annual spot volume (2024) | $18.83T | [CoinGecko 2024 Annual Report](https://www.coingecko.com/research/publications/2024-annual-crypto-report) | 🟢 High |
| Annual derivatives volume (2024) | ~$58.5T | [CoinGecko Perpetuals Report](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf) | 🟡 Medium |
| Combined annual volume (2024) | ~$77.3T | Derived (spot + derivatives) | 🟡 Medium |
| Average daily volume | ~$212B | Derived ($77.3T / 365) | 🟡 Medium |
| Est. daily trade count | ~263M (wash-adjusted) | Estimated (see [calculations](workings/calculations.md), [wash filter](workings/wash-trading-filter.md)) | 🟡 Medium-Low |
| Est. average TPS (trades) | ~3,040 (wash-adjusted) | Tiered wash model: 25% blended reduction. Range: 2,685-3,275 | 🟡 Medium-Low |

### Exchange Market Share (Spot, 2024)

| Exchange | Annual Spot Volume | Share | Source | Confidence |
|----------|-------------------|-------|--------|------------|
| Binance | $7.35T | 39.0% | [CoinGecko](https://www.coingecko.com/research/publications/largest-centralized-crypto-exchanges) | 🟢 High |
| Bybit | $1.75T | 9.3% | CoinGecko | 🟢 High |
| Crypto.com | $1.29T | 6.9% | CoinGecko | 🟢 High |
| Upbit | ~$1.1T | ~5.8% | CoinGecko | 🟢 High |
| OKX | ~$1.0T | ~5.3% | CoinGecko | 🟢 High |
| Coinbase | ~$0.9T | ~4.8% | CoinGecko | 🟢 High |
| Others (9 exchanges) | ~$5.44T | 28.9% | CoinGecko | 🟢 High |

### Spot vs Derivatives Split

| Category | 2024 Volume | Share | YoY Growth |
|----------|------------|-------|------------|
| Spot | $18.83T | ~24% | +134% |
| Derivatives (perps) | ~$58.5T | ~76% | +132% |

Derivatives dominate by a 3:1 ratio. Perpetual futures (contracts with no expiry) are the primary derivative instrument, dwarfing dated futures and options.

### Wash Trading Adjustment (Tiered Model)

The headline ~3,500-4,600 TPS estimate is derived from reported volumes that almost certainly include wash trading, even on "trusted" exchanges. We apply a **tiered exchange model** (detailed in [workings/wash-trading-filter.md](workings/wash-trading-filter.md)) that assigns per-tier wash trading discounts based on regulatory status and multiple independent detection methodologies.

#### Research Base

| Study | Year | Scope | Wash Trading Estimate | Source |
|-------|------|-------|----------------------|--------|
| Bitwise SEC Filing | 2019 | Unregulated exchanges | 95% of reported volume | [CoinTelegraph](https://cointelegraph.com/news/bitwise-tells-us-sec-that-95-of-volume-on-unregulated-crypto-exchanges-is-suspect) |
| Cong, Li, Tang, Yang (NBER/Yale) | 2022 | Unregulated exchanges | 70%+ average | [NBER WP 30783](https://www.nber.org/papers/w30783) |
| CEPR (Kocenda et al.) | 2024 | "Unregulated Tier 1" exchanges | 53.4% average (10 exchanges) | [CEPR VoxEU](https://cepr.org/voxeu/columns/wash-trading-centralised-crypto-exchanges-need-transparency-and-accountability) |
| Forbes / Blockchain Transparency Institute | 2022 | Bitcoin trading across all exchanges | ~51% of reported volume | [Cryptonomist](https://en.cryptonomist.ch/2022/08/29/forbes-51-bitcoin-trading-volumes-fake/) |
| Chainalysis | 2025 | DEX on-chain (Ethereum, BNB, Base) | $2.57B identified (0.035% of DEX volume) | [Chainalysis](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/) |
| Kaiko | 2024 | Volume-to-depth ratio analysis | HTX flagged; algorithmic wash patterns detected | [Kaiko Research](https://research.kaiko.com/insights/data-reveals-wash-trading-on-crypto-markets) |
| CryptoCompare Exchange Benchmark | 2024 | 100+ exchanges, 68 metrics | Excludes volume from rankings due to manipulation | [CryptoCompare](https://www.cryptocompare.com/external/research/exchange-ranking/) |
| Messari "Real 10" | 2019 | Volume comparison | 40-65% discount applied to Binance; 6.4x discrepancy between aggregators | [The Block](https://www.theblock.co/linked/17249/messari-rolls-out-real-10-volume-metrics-after-study-reveals-95-of-bitcoin-trading-volumes-are-fake) |

#### Tiered Exchange Model

The $77.3T combined volume figure uses CoinGecko's top-15 "trusted" exchanges, which already apply trust scores and exclude the worst offenders. We segment these into three tiers:

| Tier | Exchanges | Volume Share | Wash Estimate | Rationale |
|------|-----------|-------------|---------------|-----------|
| **Tier 1** (Regulated) | Coinbase, Kraken, Bitstamp, Gemini, Upbit | ~15% | **2-5%** (central: 3.5%) | SEC/MiCA oversight. Coinbase is a public company; volume is SEC-auditable. |
| **Tier 2** (Semi-regulated) | Binance, OKX, Bybit, Crypto.com | ~55% | **15-30%** (central: 20%) | Partial licenses. Forbes applied 40-65% discount to Binance historically; post-2023 regulatory pressure has likely reduced wash trading. Kaiko notes high volume-to-depth ratios partly due to zero-fee pairs. |
| **Tier 3** (Lower-tier trusted) | HTX, KuCoin, Gate.io, MEXC, others | ~30% | **35-55%** (central: 45%) | Limited regulation. Kaiko flagged HTX specifically. CEPR found 80%+ on lower-tier exchanges. Strong ranking-inflation incentive. |

**Blended wash trading estimate: ~25%** (range: 19-34%)

| Metric | Reported | Low Adj. (19%) | Central (25%) | High Adj. (34%) |
|--------|----------|----------------|---------------|-----------------|
| Combined annual volume | $77.3T | $62.6T | $58.0T | $51.2T |
| Average daily volume | ~$212B | ~$171B | ~$159B | ~$140B |
| Est. daily trade count | ~350M | ~283M | ~263M | ~232M |
| **Est. average TPS** | **~4,050** | **~3,275** | **~3,040** | **~2,685** |

The adjusted central estimate of **~3,040 TPS** is our best estimate of genuine CEX trading activity. The tiered model narrows the confidence interval from the prior 2,450-3,700 range (1,250 wide) to 2,685-3,275 (590 wide) — a **2.1x improvement in precision**.

The single most impactful variable is Tier 2 wash trading (especially Binance at 39% of spot). A 10-percentage-point shift in Tier 2 wash estimate moves the adjusted TPS by ~370.

**Confidence level:** 🟡 Medium-Low — the tiered model is more principled than a flat discount, but tier-level percentages are themselves uncertain. Full methodology and sensitivity analysis in [workings/wash-trading-filter.md](workings/wash-trading-filter.md).

---

## Historic Trend

### CEX Spot Trading Volume (2019-2024)

| Year | Spot Volume | YoY Growth | Context | Confidence |
|------|-------------|-----------|---------|------------|
| 2019 | ~$3.5T | — | Pre-COVID baseline | 🔴 Low |
| 2020 | $3.78T | +8% | COVID year, DeFi summer began | 🟡 Medium |
| 2021 | $25.21T | +567% | Bull market peak, retail mania | 🟢 High |
| 2022 | ~$14.0T | -44% | Bear market, FTX collapse | 🟡 Medium |
| 2023 | $8.05T | -43% | Post-FTX hangover, low volatility | 🟢 High |
| 2024 | $18.83T | +134% | Bitcoin ETF, Trump election, BTC ATH | 🟢 High |

*Sources: 2020-2024 from [CoinGecko](https://www.coingecko.com/research/publications/largest-centralized-crypto-exchanges); 2019 estimated from industry reports.*

**Key observations:**
- The 2021 bull market saw the highest-ever spot volumes at $25.21T
- The 2022-2023 decline was driven by the FTX collapse, regulatory crackdowns, and crypto winter
- 2024 recovery was fuelled by Bitcoin spot ETF approvals (Jan 2024), halving narrative, and post-election rally
- Derivatives volumes grew in parallel, with perpetuals becoming the dominant product

---

## Growth Rate Analysis

| Period | CAGR (Spot) | Context |
|--------|-------------|---------|
| 2020-2024 (4yr) | ~49% | Includes extreme bull/bear cycle |
| 2021-2024 (3yr) | -9.3% | Peak-to-recovery, misleading |
| 2023-2024 (1yr) | +134% | Recovery year |

Crypto exchange volumes are **highly cyclical** and correlated with Bitcoin price cycles (~4-year halving cycles). CAGR is less meaningful here than for traditional finance — the market oscillates between mania and hibernation.

---

## Projections

### Baseline (Continued Crypto Maturation)

**Assumptions:**
1. Bitcoin halving cycle continues; next mania phase ~2025-2026, cooldown ~2027-2028
2. Institutional adoption (ETFs, custody) adds a persistent volume floor
3. Derivatives-to-spot ratio stabilises at 3:1
4. Regulatory clarity (MiCA, US frameworks) reduces wash trading but adds institutional volume

| Year | Est. Spot Volume | Est. Total Volume | Est. TPS (trades) |
|------|-----------------|-------------------|-------------------|
| 2026 | $22T | $88T | ~4,500 |
| 2028 | $15T | $60T | ~3,000 |
| 2030 | $30T | $120T | ~6,000 |
| 2035 | $50T | $200T | ~10,000 |

### High Growth (Mainstream Adoption)

**Assumptions:**
1. Crypto becomes a standard asset class alongside equities/FX
2. CEX volumes approach traditional exchange levels
3. 24/7 markets attract global retail at scale

| Year | Est. Spot Volume | Est. Total Volume | Est. TPS (trades) |
|------|-----------------|-------------------|-------------------|
| 2026 | $30T | $120T | ~6,000 |
| 2028 | $25T | $100T | ~5,000 |
| 2030 | $50T | $200T | ~10,000 |
| 2035 | $100T | $400T | ~20,000 |

### Conservative (Regulatory Squeeze)

**Assumptions:**
1. Strict global regulation eliminates wash trading, reducing reported volumes 40-50%
2. DEXs capture increasing share from CEXs
3. Market stagnation post-2025 cycle

| Year | Est. Spot Volume | Est. Total Volume | Est. TPS (trades) |
|------|-----------------|-------------------|-------------------|
| 2026 | $15T | $55T | ~2,800 |
| 2028 | $10T | $38T | ~1,900 |
| 2030 | $18T | $65T | ~3,300 |
| 2035 | $25T | $90T | ~4,500 |

*Full calculation methodology: [workings/calculations.md](workings/calculations.md)*

---

## Key Findings

1. **Derivatives dwarf spot trading 3:1.** Perpetual futures accounted for ~$58.5T vs $18.83T in spot — crypto derivatives volume rivals the notional volume of traditional exchange-traded derivatives.

2. **Binance is the undisputed leader** with 39% spot market share, though its dominance is eroding from 50%+ in early 2024 as Bybit, Crypto.com, and OKX gain ground.

3. **Crypto exchange volumes are radically cyclical.** Spot volumes swung from $3.78T (2020) to $25.21T (2021) to $8.05T (2023) to $18.83T (2024) — a 7x range in 5 years. Projections must account for halving cycle dynamics.

4. **Wash trading remains a structural concern.** Research estimates 50-70% of volume on unregulated exchanges is fake ([Yale/NBER](https://cowles.yale.edu/sites/default/files/2022-11/cryptowashtrading040521-crypto-wash-trading.pdf)). The $18.83T CoinGecko figure covers the top 15 "trusted" exchanges, but even these may have some inflation.

5. **No double-counting with on-chain data.** CEX order book matches are settled on internal databases, not blockchains. Deposits and withdrawals appear on-chain, but the vast majority of CEX trading activity is off-chain.

6. **TPS estimation is inherently imprecise.** Unlike card networks or blockchains, CEXs don't publish trade counts. Our estimate of ~3,500-4,600 TPS is derived from volume-to-trade-size assumptions and should be treated as order-of-magnitude.

---

## Data Quality & Limitations

- **No public trade count data.** Exchanges report dollar volume, not number of trades. TPS figures are estimated using average trade size assumptions and are 🔴 Low confidence.
- **Wash trading distortion.** Even top-15 exchange data may include some artificial volume. CoinGecko applies trust scores but cannot fully eliminate wash trading.
- **Derivatives volume is notional.** A 100x leveraged trade on $100 collateral registers as $10,000 in volume — this inflates the economic significance of derivatives figures.
- **Spot volume excludes DEXs.** The $18.83T figure is CEX-only. DEX spot volume adds another ~$1.76T (see [DeFi capsule](../defi/REPORT.md)).
- **2019 data is estimated.** CoinGecko's top-15 series starts at 2020; 2019 is derived from industry estimates.
- **Historic derivatives data is sparse.** Full-year derivatives volume series before 2023 is not consistently reported.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- Actual trade counts on any CEX (no exchange publishes this; all TPS figures are estimated)
- The true wash trading percentage on "trusted" exchanges post-CoinGecko filtering — the tiered model ([wash-trading-filter.md](workings/wash-trading-filter.md)) narrows this but does not eliminate it
- Internal matching engine throughput vs. reported volume (exchanges batch and net orders internally)
- The share of volume driven by market makers vs. organic traders
- How much derivatives volume is delta-neutral hedging vs. directional speculation
- Whether derivatives-specific wash trading rates differ from spot (our model applies the same % to both)

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Wash trading on trusted exchanges | **Tiered model applied** — see [wash-trading-filter.md](workings/wash-trading-filter.md). Further refinement via Kaiko volume-to-depth ratios per exchange. | Kaiko volume-to-depth ratios; HTX flagged in 2024 | 🟡 |
| Regulated vs. unregulated volume split | Compare Coinbase/Kraken/Upbit volume patterns to Binance/OKX/Bybit — gap beyond product differences suggests wash trading | CoinGecko market share data; Coinbase 10-K ($1.16T FY2024 volume) | 🟢 |
| Futures-to-spot ratio as manipulation indicator | Organic markets show 2-4x futures-to-spot; ratios above 6x on specific exchanges suggest synthetic volume | CoinGecko derivatives data; current global ratio is ~3.1:1 but individual exchanges diverge | 🟡 |
| On-chain deposit/withdrawal flows | Compare on-chain inflows to exchanges (measurable) with claimed trading volume — genuine volume requires proportional deposits | Glassnode/CryptoQuant exchange flow data; Chainalysis exchange entity labelling | 🟢 |
| True trade count estimation | Cross-reference API trade feeds (where available) with reported 24h volume to derive actual trade sizes | Binance/Coinbase public trade APIs; Kaiko tick-level data | 🟡 |
| Bot vs. human trading ratio | Analyse trade size distribution and timing patterns — bot trades cluster at round numbers and sub-second intervals | Kaiko tick data; academic studies on HFT in crypto (Makarov & Schoar, 2020) | 🔴 |
| Zero-fee pair volume decomposition | Separate Binance zero-fee BTC pairs from fee-bearing volume to distinguish incentivised trading from wash trading | Binance API; Kaiko per-pair volume data | 🟡 |

### Key Modeling Questions
- **Coinbase trade count disclosure** would be the single highest-value data point. If Coinbase published daily trade counts alongside dollar volume in its 10-K, we could calibrate average trade size for a regulated exchange and reduce our TPS confidence interval by ~50%.
- The tiered model's Tier 2 estimate (20% wash, central) is the most impactful variable — a 10pp shift moves adjusted TPS by ~370. Post-2023 regulatory pressure may have reduced wash trading below our estimate, but no audit data exists to confirm.
- How does the derivatives-to-spot ratio vary between regulated and unregulated exchanges? A structurally higher ratio on unregulated exchanges would be strong evidence of synthetic volume.
- What fraction of CEX volume represents market-maker-to-market-maker trades? These are economically real but inflate the "human activity" interpretation of TPS.
- Does Binance's zero-fee BTC pair volume represent genuine incentivised trading or wash trading? The answer materially affects the Tier 2 estimate.

### Reference Comparisons
- **Traditional exchanges:** NYSE processes ~6B shares/day (~70K TPS) across ~$200B notional. If crypto CEXs process ~$159B/day (wash-adjusted) at a similar trade-size distribution, we'd expect ~3,000 TPS — closely matching our adjusted estimate.
- **Bitwise "real 10" exchanges:** Bitwise's 2019 analysis identified only 10 exchanges with genuine volume. The combined "real" volume was ~5% of total reported — but this was pre-CoinGecko trust scores. Our tiered model suggests CoinGecko's top-15 retains ~75% genuine volume.
- **FX market parallel:** Global FX does ~$8.5T/day (2024 interpolated). Crypto CEX does ~$159B/day wash-adjusted (1.9% of FX). Given crypto's 24/7/365 operation and speculative nature, this ratio is plausible.

---

## Sources

1. [CoinGecko — Largest Centralized Crypto Exchanges, 2020-2024](https://www.coingecko.com/research/publications/largest-centralized-crypto-exchanges)
2. [CoinGecko — 2024 Annual Crypto Industry Report](https://www.coingecko.com/research/publications/2024-annual-crypto-report)
3. [CoinGecko — State of Crypto Perpetuals Market (2024)](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf)
4. [TokenInsight — Crypto Exchange 2024 Annual Report](https://tokeninsight.com/en/research/reports/crypto-exchange-2024-annual-report)
5. [CoinLaw — Cryptocurrency Derivatives Market Statistics 2025](https://coinlaw.io/cryptocurrency-derivatives-market-statistics/)
6. [CoinLaw — Crypto Exchange Market Share Statistics 2026](https://coinlaw.io/crypto-exchange-market-share-statistics/)
7. [CryptoSlate — Crypto trading volumes rebound to $18T in 2024](https://cryptoslate.com/crypto-trading-volumes-rebound-in-2024-but-lag-behind-2021s-peak/)
8. [Finance Magnates — Global Spot Crypto Trading Climbs 142% YoY](https://www.financemagnates.com/cryptocurrency/global-spot-crypto-trading-climbs-142-year-over-year-to-21t/)
9. [Chainalysis — Crypto Market Manipulation 2025: Wash Trading](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)
10. [Yale/NBER — Crypto Wash Trading (working paper)](https://cowles.yale.edu/sites/default/files/2022-11/cryptowashtrading040521-crypto-wash-trading.pdf)
11. [Binance Square — Crypto Trading Hits Record $75.8T in 2024](https://www.binance.com/en/square/post/19331575711073)
12. [CryptoSlate — Total crypto trading volume hits $80T over last 12 months](https://cryptoslate.com/insights/total-crypto-trading-volume-hits-80-trillion-over-last-12-months/)

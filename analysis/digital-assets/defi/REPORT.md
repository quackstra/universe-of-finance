---
title: "DeFi (Decentralised Finance) — Report"
parent: Digital Assets
grand_parent: Explore
nav_order: 2
---

# DeFi (Decentralised Finance) — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Decentralised finance protocols processed approximately **$4.16 trillion** in trading volume across DEX spot ($1.76T) and DEX perpetuals ($2.4T) in 2024, with total value locked (TVL) reaching **$140 billion** by year-end ([DeFiLlama](https://defillama.com/), [CoinGecko](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf)). DeFi had ~21.7 million unique users at peak in September 2024, a 300% year-over-year increase. Uniswap remains the dominant DEX, but Solana-based DEXs (Raydium, Jupiter) surged dramatically. Critically, **all DeFi transactions are a subset of L1/L2 on-chain transactions** — they should not be added to the blockchain capsule totals.

## Scope

This analysis covers **decentralised, non-custodial financial protocols** operating on public blockchains. Included: DEX spot swaps (Uniswap, Raydium, PancakeSwap, etc.), DEX perpetual futures (Hyperliquid, dYdX, Jupiter), lending/borrowing (Aave, Compound, MakerDAO), and liquid staking (Lido, Rocket Pool). Excluded: centralised exchange trading (see [CEX capsule](../cex/REPORT.md)), centralised lending (BlockFi, Celsius — defunct), wrapped/bridged token issuance mechanics.

**Double-counting warning:** Every DeFi transaction is also an L1 or L2 blockchain transaction. A Uniswap swap on Arbitrum counts in both this capsule AND the [L1/L2 capsule](../blockchain-l1-l2/REPORT.md). Do not sum across capsules.

---

## Current State

### Trading Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| DEX spot volume (2024) | $1.76T | [DeFiLlama](https://defillama.com/dexs) / [CoinGecko](https://www.coingecko.com/research/publications/2024-annual-crypto-report) | 🟢 High |
| DEX perp volume (2024) | ~$2.4T | [CoinGecko Perps Report](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf) | 🟡 Medium |
| Combined DEX volume (2024) | ~$4.16T | Derived (spot + perps) | 🟡 Medium |
| DEX-to-CEX spot ratio | ~9.3% | $1.76T / $18.83T | 🟢 High |
| Peak daily DEX spot volume | $9.2B | Aug 4, 2024 ([CoinLaw](https://coinlaw.io/decentralized-finance-market-statistics/)) | 🟢 High |
| TVL (Dec 2024) | ~$140B | [DeFiLlama](https://defillama.com/) | 🟢 High |
| Open borrows (Q4 2024) | $19.1B | [CoinLaw](https://coinlaw.io/crypto-lending-and-borrowing-statistics/) | 🟡 Medium |
| Unique DeFi users (peak) | 21.7M | Sep 2024 ([CoinLaw](https://coinlaw.io/decentralized-finance-market-statistics/)) | 🟡 Medium |

### DEX Spot Volume by Chain (2024)

| Chain | Est. Annual DEX Volume | Share | Source | Confidence |
|-------|----------------------|-------|--------|------------|
| Solana | ~$969B | ~55% | [Solana Floor](https://solanafloor.com/news/solana-s-dex-volume-hits-trillion-dollar-mark-2025-in-numbers) | 🟡 Medium |
| Ethereum L1 | ~$350B | ~20% | DeFiLlama | 🟡 Medium |
| Arbitrum | ~$100B | ~6% | DeFiLlama | 🟡 Medium |
| Base | ~$80B | ~5% | DeFiLlama | 🟡 Medium |
| BNB Chain | ~$70B | ~4% | DeFiLlama | 🟡 Medium |
| Other chains | ~$190B | ~11% | DeFiLlama | 🔴 Low |

### Top DEX Protocols (Spot, 2024)

| Protocol | Chains | Est. Annual Volume | Notes |
|----------|--------|-------------------|-------|
| Uniswap (v2/v3/v4) | Ethereum, Arbitrum, Polygon, Base, etc. | ~$700B+ | Largest DEX by cumulative volume |
| Raydium | Solana | ~$300B+ | Memecoin trading hub |
| Jupiter | Solana | ~$200B+ | Solana DEX aggregator |
| PancakeSwap | BNB Chain, Ethereum | ~$80B+ | BSC leader |
| Orca | Solana | ~$60B+ | Concentrated liquidity on Solana |

### DEX Perpetuals (2024)

| Protocol | Est. Annual Volume | Share | Notes |
|----------|-------------------|-------|-------|
| Hyperliquid | ~$1.2T+ | ~50% | Dominant perp DEX by Q4 2024 |
| dYdX | ~$400B | ~17% | Fell to 3rd place |
| Jupiter Perps | ~$200B | ~8% | Solana-native |
| GMX | ~$100B | ~4% | Arbitrum-based |
| Others | ~$500B | ~21% | Various chains |

### DeFi Lending/Borrowing

| Metric | Value | Source |
|--------|-------|--------|
| Lending TVL | >$60B | [AInvest](https://www.ainvest.com/news/defi-lending-protocols-surpass-60-billion-total-locked-2507/) |
| Aave market share | ~50-62% | CoinLaw |
| Open borrows (Q4) | $19.1B | CoinLaw |
| Liquidations (2024) | Significant during Aug crash | Various |

---

## Historic Trend

### DeFi TVL and DEX Volume (2019-2024)

| Year | TVL (Dec) | DEX Spot Volume | Key Event | Confidence |
|------|-----------|----------------|-----------|------------|
| 2019 | ~$0.7B | ~$2B | Pre-DeFi summer | 🔴 Low |
| 2020 | ~$15B | ~$25B | DeFi summer, Uniswap v2 launch | 🟡 Medium |
| 2021 | ~$100B | ~$600B+ | DeFi mania, Uniswap v3, multi-chain | 🟡 Medium |
| 2022 | ~$40B | ~$500B | Bear market, Terra/Luna collapse, FTX | 🟡 Medium |
| 2023 | ~$54B | ~$648B | Recovery begins, Solana DeFi grows | 🟡 Medium |
| 2024 | ~$140B | ~$1.76T | Solana memecoin frenzy, perp DEX explosion | 🟢 High |

*Sources: DeFiLlama for TVL; CoinGecko for DEX volume.*

---

## Growth Rate Analysis

| Period | Metric | Growth | Context |
|--------|--------|--------|---------|
| 2023-2024 | DEX spot volume | +172% | Solana DEX explosion |
| 2023-2024 | TVL | +159% | Bull market recovery |
| 2020-2024 (4yr) | DEX spot volume | ~70x | From $25B to $1.76T |
| 2023-2024 | DEX perp volume | +132% | Hyperliquid emergence |
| 2023-2024 | Unique users | +300% | Memecoin retail influx |

DEX spot volume share vs CEX grew from ~7-10% at start of 2024 to over 20% by January 2025, indicating a structural shift toward non-custodial trading.

---

## Projections

### Baseline (DEX Share Grows Steadily)

**Assumptions:**
1. DEX-to-CEX ratio grows from ~10% to ~25% by 2030 (spot)
2. Perp DEX volume grows at 50% CAGR then decelerates
3. DeFi TVL follows crypto market cycles but ratchets higher each cycle
4. Institutional DeFi adoption begins (regulated pools, RWA tokenisation)

| Year | DEX Spot Volume | DEX Perp Volume | TVL (est.) |
|------|----------------|----------------|------------|
| 2026 | $3T | $6T | $200B |
| 2028 | $3.5T | $8T | $150B |
| 2030 | $7T | $15T | $400B |
| 2035 | $15T | $30T | $1T |

### High Growth (DeFi Eats Finance)

**Assumptions:**
1. DEX captures 50%+ of crypto trading by 2035
2. Real-world assets (bonds, equities) tokenised and traded on DEXs
3. DeFi lending rivals small banks in assets
4. AI agents trade autonomously on-chain

| Year | DEX Spot Volume | DEX Perp Volume | TVL (est.) |
|------|----------------|----------------|------------|
| 2026 | $5T | $10T | $300B |
| 2028 | $8T | $20T | $500B |
| 2030 | $20T | $50T | $1T |
| 2035 | $100T | $200T | $5T |

### Conservative (Speculation Fades)

**Assumptions:**
1. Memecoin activity collapses, taking Solana DEX volume with it
2. Regulatory action restricts DeFi access in major markets
3. Institutional adoption stalls

| Year | DEX Spot Volume | DEX Perp Volume | TVL (est.) |
|------|----------------|----------------|------------|
| 2026 | $1.5T | $3T | $100B |
| 2028 | $1T | $2T | $80B |
| 2030 | $2T | $4T | $120B |
| 2035 | $3T | $6T | $200B |

---

## Key Findings

1. **DEXs processed $1.76T in spot volume and $2.4T in perp volume in 2024** — combined $4.16T, a ~170% increase from 2023. DEX trading is approaching a meaningful share of CEX activity.

2. **Solana captured ~55% of DEX spot volume** in 2024, overtaking Ethereum for the first time. This was driven by the memecoin trading boom on platforms like Raydium and Jupiter.

3. **Hyperliquid dominated perp DEXs** with ~50% market share by Q4, displacing dYdX. The perp DEX market is growing faster than spot DEXs.

4. **DeFi TVL nearly tripled** from $54B to $140B in 2024. Aave controls ~50-62% of lending TVL. Open borrows reached $19.1B, nearly double centralised lending volume.

5. **All DeFi transactions are a subset of L1/L2 transactions.** A Uniswap swap on Ethereum counts as both a DeFi transaction and an Ethereum L1 transaction. This is the most important double-counting flag in the Digital Assets sector.

6. **DEX-to-CEX ratio is structurally increasing.** From ~3% in 2020 to ~10% in 2024 to ~20% by Jan 2025. The trend toward non-custodial trading is accelerating, driven by improved UX, lower fees on L2s, and post-FTX trust concerns.

---

## Data Quality & Limitations

- **DEX volume is high-confidence.** Unlike CEX data, DEX trades are on-chain and verifiable. DeFiLlama aggregates directly from smart contract events. However, MEV sandwich attacks and arbitrage bots inflate volume.
- **TVL is a flawed metric.** TVL counts the same dollar multiple times (deposit ETH → mint stETH → deposit stETH in Aave → borrow USDC → provide liquidity). Actual unique capital is much lower.
- **Perp DEX volume includes leverage.** Like CEX derivatives, notional volume overstates economic activity.
- **User count methodology varies.** "21.7M unique users" likely counts unique addresses, not unique humans (one person may use multiple wallets).
- **DeFi lending data is for open positions, not flow.** $19.1B in borrows is a stock metric, not annual flow.
- **Historic DEX volume before 2022 is less reliable.** DeFiLlama's coverage improved over time; earlier data may undercount smaller DEXs.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- The percentage of DEX volume generated by MEV bots (sandwich attacks + arbitrage) vs. organic human traders
- True unique user count (addresses != humans; sybil farming inflates DeFi user metrics)
- How much DEX volume is incentivised by liquidity mining rewards and would disappear without subsidies
- The real capital efficiency of DeFi (TVL is multi-counted via recursive lending/staking)
- Whether Hyperliquid's dominance in perp DEXs reflects genuine demand or concentrated market-making

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| MEV/bot volume as % of DEX trades | Analyse sandwich attack and arbitrage bot volume from MEV trackers; compare bot-attributed volume to total DEX volume | Sandwiched.me: $561.9M MEV volume in 16-month period on Solana alone; reverted txns peaked at 75.7% in Apr 2024; Flashbots data for Ethereum MEV | 🟡 |
| Unique users vs. transaction count ratio | Compare unique active addresses to transaction counts — a ratio below 1:10 suggests heavy bot/power-user concentration | DeFiLlama: 21.7M peak users vs. billions of annual transactions; Dune dashboards track unique traders per DEX | 🟢 |
| TVL-to-volume ratio as capital efficiency measure | Divide annual DEX volume by average TVL — higher ratios indicate more efficient capital use (or more speculative churn) | DeFi TVL ~$140B avg; DEX spot volume $1.76T → ~12.6x annual turnover. Compare to TradFi: NYSE market cap ~$28T, volume ~$50T → ~1.8x | 🟢 |
| Organic vs. incentivised volume | Track DEX volume changes when liquidity mining programs end — volume drops reveal the subsidy-dependent fraction | Historical data from Uniswap (post-UNI farming), SushiSwap rewards changes; Base/Optimism grant program timelines | 🟡 |
| Sybil/airdrop farming distortion | Compare pre-airdrop vs. post-airdrop activity on L2 DEXs (zkSync, Starknet, Arbitrum) to estimate farming-inflated volume | zkSync airdrop (Jun 2024) caused ~40-60% activity drop; Starknet similar pattern; Dune sybil detection dashboards | 🟡 |
| Perp DEX genuine demand | Analyse Hyperliquid's open interest relative to volume — a very high volume-to-OI ratio suggests wash trading or excessive churn | Hyperliquid dashboard shows OI vs. volume; compare to CEX perp exchanges for calibration | 🔴 |

### Key Modeling Questions
- If MEV bots account for 30-60% of DEX transaction count (not volume), what is the "organic human TPS" for DeFi? This would significantly reduce the activity attributed to genuine DeFi usage.
- The DEX-to-CEX ratio grew from ~3% to ~20% in 4 years. Is this structural (post-FTX trust shift) or cyclical (memecoin speculation on Solana)? If Solana memecoin activity normalises, does the ratio revert to ~10%?
- TVL's 12.6x annual turnover ratio is 7x higher than NYSE's. Does this indicate superior capital efficiency or speculative churn? Breaking down by protocol type (lending vs. DEX LP vs. liquid staking) would reveal the answer.
- How much of the $2.4T perp DEX volume is delta-neutral market making (economically hollow) vs. directional trading (economically meaningful)?

### Reference Comparisons
- **DEX vs. CEX spot volume:** DEXs did $1.76T vs. CEX $18.83T — a 9.3% ratio. If CEX volume is adjusted for wash trading (20-30% reduction), the ratio rises to ~12-13%, suggesting DEXs are more significant than headline numbers imply.
- **DeFi TVL vs. traditional bank deposits:** $140B TVL is equivalent to a mid-size US regional bank. The top 4 US banks hold ~$7T in deposits — DeFi is ~2% of that. But DeFi's growth rate (~159% YoY) far exceeds banking deposit growth (~5% YoY).
- **DEX capital efficiency:** Uniswap v3 concentrated liquidity achieves capital efficiency comparable to centralised order books on major pairs. Uniswap's TVL-to-volume ratio is ~50x annually vs. ~12.6x for DeFi overall — concentrated liquidity is transformative.
- **MEV as a tax on DeFi users:** If sandwich attacks extracted $370-500M from Solana users alone over 16 months, the annualised MEV tax is ~$280-375M — roughly 0.02% of DEX volume but significant for individual affected trades (5-10% slippage on sandwiched trades).

---

## Sources

1. [DeFiLlama — DEX Volume Rankings](https://defillama.com/dexs)
2. [DeFiLlama — DEX Volume by Chain](https://defillama.com/dexs/chains)
3. [DeFiLlama — Perp DEX Volume Rankings](https://defillama.com/perps)
4. [DeFiLlama — Total Value Locked Dashboard](https://defillama.com/)
5. [CoinGecko — 2024 Annual Crypto Industry Report](https://www.coingecko.com/research/publications/2024-annual-crypto-report)
6. [CoinGecko — State of Crypto Perpetuals Market (2024)](https://assets.coingecko.com/reports/2025/CoinGecko-State-of-Crypto-Perpetuals-Market.pdf)
7. [CoinLaw — Decentralized Finance Market Statistics 2025](https://coinlaw.io/decentralized-finance-market-statistics/)
8. [CoinLaw — Crypto Lending and Borrowing Statistics 2026](https://coinlaw.io/crypto-lending-and-borrowing-statistics/)
9. [Solana Floor — Solana's DEX Volume Hits Trillion Dollar Mark](https://solanafloor.com/news/solana-s-dex-volume-hits-trillion-dollar-mark-2025-in-numbers)
10. [AInvest — DeFi Lending Protocols Surpass $60B TVL](https://www.ainvest.com/news/defi-lending-protocols-surpass-60-billion-total-locked-2507/)
11. [The Block — DEX Volume Monthly](https://www.theblock.co/data/decentralized-finance/dex-non-custodial/dex-volume-monthly)
12. [The Block — Hyperliquid leads perp DEX futures at $285B](https://www.theblock.co/amp/post/333054/hyperliquid-leads-the-pack-as-dex-futures-hit-285-billion-in-2024)
13. [Focus on Business — TVL in DeFi soars 137% YoY to $129B](https://focusonbusiness.eu/en/news/total-value-locked-in-defi-soars-137-yoy-to-a-staggering-129-billion/6554)

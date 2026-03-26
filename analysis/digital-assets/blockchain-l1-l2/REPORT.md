# L1 & L2 Blockchain Transactions — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Public blockchains processed an estimated **25-30 billion on-chain transactions** in 2024, driven overwhelmingly by Solana's high-throughput architecture (~50-70M transactions/day) and the Ethereum L2 ecosystem (~14M+ transactions/day). This translates to roughly **800-950 average TPS** across all major chains combined. The headline number is deceptive, however: the majority of Solana transactions are lightweight operations (vote transactions, MEV bot activity), and high-value settlement remains concentrated on Ethereum and Bitcoin. On-chain transaction counts are growing exponentially as L2 rollups and high-throughput L1s reduce per-transaction costs toward zero.

## Scope

This analysis covers **on-chain transactions** settled on public, permissionless blockchains. Included: Bitcoin, Ethereum L1, Solana, BNB Chain, and major Ethereum L2 rollups (Base, Arbitrum, Optimism, zkSync, Starknet). Excluded: private/consortium blockchains, CEX internal transactions, sidechain bridges (counted at destination).

**Double-counting note:** DeFi transactions (see [DeFi capsule](../defi/REPORT.md)) and stablecoin transfers (see [Stablecoins capsule](../stablecoins/REPORT.md)) are **subsets** of L1/L2 transactions. A Uniswap swap on Ethereum L1 counts as one Ethereum transaction AND one DeFi transaction. Do not sum these capsules.

---

## Current State

### Transaction Volume by Chain (2024)

| Chain | Avg Daily Txns | Est. Annual Txns | Avg TPS | Peak TPS (observed) | Source | Confidence |
|-------|---------------|-----------------|---------|---------------------|--------|------------|
| Solana | ~50M (avg), 138M (peak Dec) | ~18B+ | ~580-1,600 | 4,000+ | [CryptoSlate](https://cryptoslate.com/70m-daily-transactions-143b-volume-how-solana-won-defis-throughput-race/) | 🟡 Medium |
| Base (L2) | ~8.8M (peak) | ~2B+ | ~50-100 | ~200+ | [CryptoRank](https://cryptorank.io/news/feed/4c92e-base-l2-transaction-momentum-2024) | 🟡 Medium |
| BNB Chain | ~3-4M | ~1.2B | ~35-46 | ~300 | BitInfoCharts | 🟡 Medium |
| Arbitrum (L2) | ~2-3M | ~900M | ~23-35 | ~100 | L2Beat | 🟡 Medium |
| Ethereum L1 | ~1.16M | ~425M | ~13.5 | ~22.8 | [Etherscan](https://etherscan.io/chart/tx) | 🟢 High |
| Bitcoin | ~500K | ~183M | ~5.8 | ~10.7 | [Blockchain.com](https://www.blockchain.com/charts/n-transactions) | 🟢 High |
| Optimism (L2) | ~1-2M | ~500M | ~12-23 | ~50 | L2Beat | 🟡 Medium |
| Other L2s | ~2-3M | ~800M | ~23-35 | varies | L2Beat | 🔴 Low |
| **Total (est.)** | **~70-90M** | **~25-30B** | **~800-1,000** | — | Aggregated | 🟡 Medium |

### Aggregate Metrics

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Est. combined avg TPS (all chains) | ~800-1,000 | Derived from daily totals | 🟡 Medium |
| Est. combined peak TPS | ~5,000+ | Solana peak + L2 peaks concurrent | 🔴 Low |
| Est. annual transactions (2024) | ~25-30B | Aggregated from chain data | 🟡 Medium |
| Bitcoin annual value transferred | ~$3.5T | Blockchain.com | 🟡 Medium |
| Ethereum L1 annual value transferred | ~$2.5T | Etherscan | 🟡 Medium |
| Solana annual value transferred | ~$400B+ | Messari | 🟡 Medium |

---

## Chain-by-Chain Analysis

### Bitcoin
- **Role:** Settlement layer, store of value transfers
- **Daily txns:** ~400K-800K (averaging ~500K in late 2024)
- **Theoretical max:** ~7 TPS (block size limit)
- **Actual avg TPS:** ~5.8
- **Notable 2024:** Ordinals/BRC-20 activity spiked transaction counts earlier in the year, then faded. Bitcoin reached 1 billion total historical transactions in 2024 ([Nasdaq](https://www.nasdaq.com/articles/bitcoin-network-tops-1-billion-in-total-transactions-processed)).

### Ethereum L1
- **Role:** Smart contract platform, DeFi hub, L2 settlement
- **Daily txns:** ~1.03-1.2M (average: 1,164,911)
- **Theoretical max:** ~15-30 TPS
- **Actual avg TPS:** ~13.5
- **Notable 2024:** Transaction count has been stable/declining on L1 as activity migrates to L2s. All-time high daily txns was 1.96M (Jan 2024). L1 is increasingly a settlement/data availability layer rather than an execution layer.

### Solana
- **Role:** High-throughput L1, DeFi, memecoin trading, NFTs
- **Daily txns:** ~50-70M average, peak 138M (Dec 2024)
- **Theoretical max:** ~65,000 TPS
- **Actual avg TPS:** ~580-1,600
- **Notable 2024:** Breakout year. Memecoin frenzy (pump.fun) and DeFi activity pushed Solana to the highest transaction count of any blockchain by a massive margin. Caveat: Solana counts vote transactions and failed transactions, which inflate the headline number. Excluding votes, "real" transactions are ~30-40% of total.

### Ethereum L2 Ecosystem
- **Combined daily txns:** ~14.3M+ (Base 8.8M + Arbitrum ~2.8M + Optimism ~1.5M + others)
- **Key trend:** Base emerged as the L2 transaction leader in late 2024, driven by Coinbase integration, AI agents (Virtuals Protocol), and low fees
- **L2 TVL:** >$58B locked across all L2s ([L2Beat](https://l2beat.com/scaling/tvs))
- **Notable:** Ethereum L2s processed a record 12.4M transactions in a single day in mid-2024 ([Cointelegraph](https://cointelegraph.com/news/ethereum-l2-ecosystem-processes-a-record-12-4-m-transactions-in-a-day))

### Radix
- **Role:** DeFi-focused L1 with asset-oriented programming model
- **Theoretical max:** 500,000+ TPS (Hyperscale test, Jan 2026 — 590 nodes, commodity hardware)
- **Actual daily txns:** Low (early-stage network, pre-mass-adoption)
- **Notable:** Radix's Cerberus consensus achieved >1M TPS in peer-reviewed testing. The Hyperscale public test (Jan 2026) sustained 500K TPS with peaks >700K TPS across 128 shards. Production mainnet activity remains nascent.

---

## Historic Trend

### Combined L1/L2 Estimated Annual Transactions

| Year | Est. Annual Txns | Key Driver | Confidence |
|------|-----------------|------------|------------|
| 2019 | ~1.5B | Bitcoin + Ethereum only | 🔴 Low |
| 2020 | ~2B | DeFi summer on Ethereum | 🔴 Low |
| 2021 | ~4B | Bull market, NFT boom, BSC growth | 🟡 Medium |
| 2022 | ~5B | L2 rollup launches, Solana growth | 🟡 Medium |
| 2023 | ~8B | L2 adoption accelerates, Solana recovery | 🟡 Medium |
| 2024 | ~25-30B | Solana memecoin frenzy, L2 explosion | 🟡 Medium |

*Note: 2024 represents a ~3x jump driven primarily by Solana's daily transaction count surging from ~20M to 50-138M.*

---

## Growth Rate Analysis

| Period | Growth | Context |
|--------|--------|---------|
| 2019-2024 (5yr) | ~17-20x | Massive structural growth from L2s and high-throughput L1s |
| 2023-2024 (1yr) | ~3x | Solana breakout + L2 scaling |
| Ethereum L1 (2023-2024) | +12% | Modest, as activity shifts to L2s |
| Bitcoin (2023-2024) | ~flat | Ordinals bump faded |

The growth is driven by **supply-side scaling**: as transaction costs drop (L2 fees <$0.01, Solana fees <$0.001), new use cases emerge (memecoin trading, AI agents, micro-payments) that were previously uneconomical.

---

## Projections

### Baseline (Scaling Continues)

**Assumptions:**
1. Ethereum L2 ecosystem grows to 50M+ combined daily txns by 2030
2. Solana stabilises at 50-100M daily txns as memecoin speculation cools
3. New high-throughput chains (Sui, Aptos, Monad) add meaningful volume
4. Bitcoin remains stable at ~500K-1M daily txns

| Year | Est. Annual Txns | Est. Avg TPS |
|------|-----------------|-------------|
| 2026 | ~40B | ~1,270 |
| 2028 | ~60B | ~1,900 |
| 2030 | ~100B | ~3,170 |
| 2035 | ~250B | ~7,930 |

### High Growth (Blockchain Goes Mainstream)

**Assumptions:**
1. Major apps (social media, gaming, payments) settle on-chain
2. L2 fees approach zero; transactions become "free" at the user level
3. AI agents generate billions of autonomous micro-transactions

| Year | Est. Annual Txns | Est. Avg TPS |
|------|-----------------|-------------|
| 2026 | ~60B | ~1,900 |
| 2028 | ~150B | ~4,760 |
| 2030 | ~500B | ~15,850 |
| 2035 | ~2T | ~63,400 |

### Conservative (Niche Remains)

**Assumptions:**
1. Crypto remains primarily speculative; no mainstream app breakout
2. Regulatory pressure caps growth in key markets
3. Transaction counts plateau as speculation fades

| Year | Est. Annual Txns | Est. Avg TPS |
|------|-----------------|-------------|
| 2026 | ~30B | ~950 |
| 2028 | ~35B | ~1,110 |
| 2030 | ~45B | ~1,430 |
| 2035 | ~60B | ~1,900 |

---

## Key Findings

1. **Solana dominates by transaction count.** With 50-138M daily transactions, Solana alone accounts for ~70% of all blockchain transactions — but most are low-value (memecoins, vote transactions, bots).

2. **Ethereum's execution is migrating to L2s.** Ethereum L1 daily transactions are flat at ~1.16M, while L2s collectively process 14M+ daily. L1 is becoming a settlement/DA layer.

3. **Transaction counts are exponentially correlated with cost.** As fees drop, volume explodes. Solana ($0.00025/tx) and L2s (<$0.01/tx) have orders of magnitude more transactions than Bitcoin ($1-5/tx) and Ethereum L1 ($1-20/tx).

4. **Quality varies enormously.** One Bitcoin transaction settling $100K has very different economic significance from one Solana vote transaction. Raw TPS comparisons across chains are misleading without value-weighting.

5. **Double-counting is pervasive in crypto.** DeFi transactions, stablecoin transfers, and NFT trades all count as L1/L2 transactions. The 25-30B annual figure includes all of these subcategories.

6. **Radix has the architecture but not yet the volume.** With 500K+ TPS demonstrated in testing, Radix has among the highest theoretical throughput of any network, but production adoption is still nascent.

---

## Data Quality & Limitations

- **Solana vote transaction inflation.** Solana counts validator vote transactions (~60% of total) in its headline number. "Real" user transactions are ~30-40% of reported total. We use total-transaction figures for consistency but note this caveat.
- **L2 data fragmentation.** L2Beat is the best aggregator, but dozens of smaller L2s/L3s are not tracked. Combined L2 figures are underestimates.
- **Historic data is estimated.** Pre-2022 combined L1/L2 figures are rough estimates. Chain-specific data exists but aggregation across all chains is not standardised.
- **No standard "transaction" definition.** Bitcoin counts UTXOs, Ethereum counts state transitions, Solana counts instructions. Cross-chain comparisons are inherently approximate.
- **Value transferred figures are rough.** On-chain value includes self-transfers, bridge movements, and other non-economic activity.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- The true number of "economically meaningful" transactions on Solana (vote txns, failed txns, and spam are bundled into headline numbers)
- What fraction of L2 transactions are MEV bots, sequencer overhead, or protocol-internal operations
- Whether L2 batch compression means posted L1 data understates true L2 activity (or overstates it via duplicate state roots)
- Cross-chain bridge transaction attribution — a single user transfer can generate 3-5 transactions across chains
- The economic value per transaction on high-throughput chains (Solana, Base) vs. settlement chains (Bitcoin, Ethereum L1)

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Solana vote txns vs. real txns | Filter using Solana's native vote/non-vote classification; further filter non-vote for failed txns and known bot programs | Solscan analytics; Dune `solana.vote_transactions` table; Helius MEV report data. Non-vote txns were ~30-40% of total historically, but hit 148M/day in Jan 2025 | 🟢 |
| Solana spam/MEV distortion | Analyse reverted transaction rate (peaked at 75.7% of non-vote txns in Apr 2024) and known MEV bot program IDs | Sandwiched.me analysed 8.5B trades / $1T DEX volume; Jito MEV data; Helius Solana MEV Report | 🟢 |
| Bitcoin inscriptions/Ordinals as % of total | Count OP_RETURN and Taproot witness transactions; compare fee-adjusted vs. raw tx counts | 69.6M cumulative inscriptions by Sep 2024 (31.9% growth in 9 months); Ordinals activity peaked Q1 2024 then faded | 🟡 |
| L2 sequencer data vs. posted batches | Compare L2Beat activity data (sequencer-reported) with L1 blob/calldata posts to validate L2 tx counts | L2Beat tracks both sequencer activity and L1 data posts; EIP-4844 blob data available on Etherscan | 🟡 |
| "Economic transactions" vs. all transactions | Value-weight transactions: multiply tx count by median transfer value per chain to get "economic TPS" | Messari/Artemis chain-level value transferred data; Bitcoin ~$7K/tx, Ethereum L1 ~$6K/tx, Solana ~$8/tx | 🟢 |
| L3/appchain undercounting | Survey emerging L3s (e.g., Degen Chain, Xai) not yet tracked by L2Beat | L2Beat covers ~30 major L2s but dozens of L3s are untracked; individual L3 explorers exist but no aggregator | 🔴 |

### Key Modeling Questions
- If we exclude Solana vote transactions AND failed transactions AND MEV bot reverts, what is the "genuine user TPS" for Solana? Early estimates suggest it could be 60-80% lower than headline — dropping Solana from ~580-1,600 TPS to ~120-500 TPS and combined blockchain TPS from ~800-1,000 to ~350-550.
- Should we define a "value-weighted TPS" metric? One Bitcoin transaction at $100K has more economic significance than 10,000 Solana memecoin swaps at $5 each. A value-weighted measure would dramatically reorder the chain rankings.
- What is the actual L2 transaction count growth rate net of airdrop farming? Many L2 transactions in 2024 were sybil accounts farming token airdrops (Base, zkSync, Starknet). Post-airdrop activity drops are the key signal.
- How many unique humans (not addresses) transact on-chain daily? Address-based counts overstate by 5-20x due to multi-wallet usage, bot accounts, and sybil activity.

### Reference Comparisons
- **SWIFT:** ~50M messages/day (~580 TPS), each representing a high-value interbank transfer. Bitcoin + Ethereum L1 combined (~1.66M txns/day, ~19 TPS) are the crypto equivalents — lower throughput but arguably comparable economic gravity per transaction.
- **Visa/Mastercard:** ~1.8B transactions/day (~21,000 TPS). Total blockchain TPS of ~800-1,000 is ~4-5% of card network throughput, but growing exponentially where card networks are flat.
- **Solana vs. Visa throughput claim:** Solana's ~580-1,600 TPS headline is often compared to Visa's ~1,700 TPS average. But after filtering votes, failures, and MEV, Solana's "real" TPS may be ~120-500 — below Visa rather than approaching it.
- **Ethereum L1 + L2 as a system:** Combined ~15M txns/day (~175 TPS). This is the more meaningful comparison unit for Ethereum's scaling strategy, not L1 alone.

---

## Sources

1. [Etherscan — Ethereum Daily Transactions Chart](https://etherscan.io/chart/tx)
2. [Blockchain.com — Bitcoin Confirmed Transactions Per Day](https://www.blockchain.com/charts/n-transactions)
3. [BitInfoCharts — Bitcoin/Ethereum/Solana Transaction Charts](https://bitinfocharts.com/)
4. [L2Beat — Scaling Activity Dashboard](https://l2beat.com/scaling/activity)
5. [CryptoSlate — 70M daily transactions: How Solana won DeFi's throughput race](https://cryptoslate.com/70m-daily-transactions-143b-volume-how-solana-won-defis-throughput-race/)
6. [CryptoSlate — Solana surpasses rivals with record 66.9M daily transactions](https://cryptoslate.com/insights/solana-surpasses-rivals-with-record-breaking-66-9-million-daily-transactions/)
7. [CryptoRank — Base keeps up L2 transaction momentum in 2024](https://cryptorank.io/news/feed/4c92e-base-l2-transaction-momentum-2024)
8. [Cointelegraph — Ethereum L2 ecosystem processes record 12.4M transactions in a day](https://cointelegraph.com/news/ethereum-l2-ecosystem-processes-a-record-12-4-m-transactions-in-a-day)
9. [Nasdaq — Bitcoin Network Tops 1 Billion Total Transactions](https://www.nasdaq.com/articles/bitcoin-network-tops-1-billion-in-total-transactions-processed)
10. [Chainspect — Fastest Blockchains by TPS (2026)](https://chainspect.app/dashboard)
11. [Everstake — Solana Staking Insights & Analysis: 2024 Annual Report](https://everstake.one/crypto-reports/solana-staking-insights-and-analysis-2024-annual-report)
12. [Radix Wiki — Transactions Per Second (TPS)](https://radix.wiki/contents/tech/core-concepts/transactions-per-second-tps)
13. [Staking Rewards — Radix: The DLT that Conquered 1.4M TPS](https://www.stakingrewards.com/journal/research/radix-the-dlt-that-conquered-1-4-million-tps-publicly)
14. [Statista — Bitcoin transactions per day 2009-2025](https://www.statista.com/statistics/730806/daily-number-of-bitcoin-transactions/)

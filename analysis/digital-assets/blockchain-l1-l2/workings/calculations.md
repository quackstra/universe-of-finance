# L1 & L2 Blockchain — Calculations & Methodology

## 1. Per-Chain Daily Transaction Estimates

### Bitcoin
- Source: Blockchain.com, BitInfoCharts
- Range in 2024: 400K-800K/day
- Average (late 2024): ~500K/day
- Annual: 500K x 365 = ~183M
- TPS: 500K / 86,400 = ~5.8

### Ethereum L1
- Source: Etherscan
- Average daily: 1,164,911 (2024 full year)
- Peak: 1,961,144 (Jan 14, 2024)
- Low: 965,098 (Oct 27, 2024)
- Annual: 1,165K x 365 = ~425M
- TPS: 1,165K / 86,400 = ~13.5

### Solana
- Source: CryptoSlate, Everstake, Dune
- Average daily (2024): ~50-70M (varies by period)
- Peak: 138M (Dec 17, 2024)
- Record before: 91M (Jun 2024)
- Using 50M avg: 50M x 365 = ~18.25B
- TPS: 50M / 86,400 = ~579 (low avg)
- TPS: 70M / 86,400 = ~810 (high avg)
- IMPORTANT: ~60% of Solana transactions are validator vote transactions
- "Real" user transactions: ~20-28M/day

### Base (L2)
- Source: CryptoRank, L2Beat
- Peak: 8.8M/day (late 2024)
- Average (H2 2024): ~5.5M/day
- Annual: ~2B

### Arbitrum (L2)
- Source: L2Beat
- Average: ~2.5-2.8M/day
- Annual: ~900M

### Optimism (L2)
- Source: L2Beat
- Average: ~1.5M/day
- Total historical: >550M (through late 2024)
- Annual 2024: ~500M+

## 2. Combined TPS Calculation

Sum of average daily transactions:
- Solana: 50M
- Base: 5.5M
- BNB: 3.5M
- Arbitrum: 2.5M
- Optimism: 1.5M
- Ethereum: 1.16M
- Bitcoin: 0.5M
- Others: ~3M
- **Total: ~67.7M/day (low est) to ~90M/day (high est)**

TPS = 75M / 86,400 = **~868 TPS** (midpoint)

## 3. Annual Transaction Count

75M/day x 365 = **~27.4 billion** (midpoint)
Range: 25-30 billion

## 4. Historic Estimates

These are rough approximations:
- 2019: Bitcoin ~125M + Ethereum ~250M + others ~125M = ~500M (but some emerging chains add more, est ~1.5B total with Tron, etc.)
- 2020: Similar base + DeFi summer spike on ETH + BSC launch = ~2B
- 2021: ETH at ~1.3M/day, BSC at ~5M/day, Solana emerging, Polygon = ~4B
- 2022: L2 rollups launch (Arbitrum, Optimism), Solana grows = ~5B
- 2023: Base launches, L2s grow, Solana recovers post-FTX = ~8B
- 2024: Solana 50-138M/day, L2s 14M+/day = ~25-30B

## 5. Projection Logic

Growth is primarily **supply-side driven**: cheaper transactions → more transactions.

Key inflection points:
- Ethereum danksharding (EIP-4844) → L2 fees drop 90% → more L2 txns
- Solana Firedancer upgrade → higher throughput ceiling
- New chains (Monad, Sei, Aptos) → additional capacity

Baseline assumes ~15% CAGR on current trajectory, moderating over time.
High growth assumes mainstream app adoption (social, gaming, payments on-chain).
Conservative assumes crypto remains speculative with no mainstream breakout.

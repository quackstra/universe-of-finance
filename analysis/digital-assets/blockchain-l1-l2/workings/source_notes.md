# L1 & L2 Blockchain — Source Notes

## Primary On-Chain Data Sources

### Bitcoin: Blockchain.com, BitInfoCharts
- Most reliable; data is directly from the Bitcoin blockchain
- Blockchain.com provides clean daily charts
- Confidence: 🟢 High

### Ethereum: Etherscan
- Gold standard for Ethereum L1 data
- Provides daily transaction counts, gas usage, contract interactions
- 2024 average: 1,164,911/day (verified from annual chart)
- Confidence: 🟢 High

### Solana: Dune Analytics, Solscan, Messari
- Multiple sources with somewhat different counting methods
- Vote transaction inclusion varies by source
- CryptoSlate/Everstake report total transactions (including votes)
- Dune dashboards can filter votes vs non-votes
- Confidence: 🟡 Medium (due to vote transaction ambiguity)

### L2 Ecosystem: L2Beat
- The authoritative source for Ethereum L2 data
- Tracks TVL, activity, and risk assessments for all major rollups
- Activity dashboard shows daily transactions per L2
- URL: https://l2beat.com/scaling/activity
- Confidence: 🟡 Medium (data depends on L2 team reporting)

## Data Gaps

1. **No aggregated all-chain dashboard exists** — we must sum chain-by-chain
2. **Tron is underrepresented** in our analysis — it's a major stablecoin chain with 3-5M daily txns
3. **Cosmos ecosystem** (Osmosis, etc.) is not tracked by L2Beat
4. **Non-EVM chains** (Near, Aptos, Sui) have less standardised reporting

## Cross-Referencing
- Etherscan Ethereum data matches BitInfoCharts data closely
- Bitcoin data is consistent across Blockchain.com and BitInfoCharts
- Solana figures vary: CryptoSlate reports 70M, Everstake says 138M peak, Dune shows ~50M avg
- We use the range (50-70M avg, 138M peak) to account for this variance

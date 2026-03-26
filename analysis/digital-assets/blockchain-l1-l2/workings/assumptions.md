# L1 & L2 Blockchain — Key Assumptions

## A1. Solana Vote Transaction Inclusion
- Solana counts ALL transactions including validator vote transactions (~60% of total)
- We include votes in headline figures for consistency with how Solana reports
- "Real" user transactions are ~30-40% of reported total
- This inflates Solana's TPS relative to chains that don't count consensus messages

## A2. Definition of "Transaction"
- There is no universal definition across chains
- Bitcoin: one transaction with potentially many UTXOs (inputs/outputs)
- Ethereum: one state transition (can include complex smart contract calls)
- Solana: one instruction (atomic unit; a swap may be multiple instructions)
- We count at each chain's native "transaction" unit for consistency

## A3. Double-Counting Within This Capsule
- We count each chain independently — no double-counting within L1/L2
- Exception: L2 batch submissions appear as L1 transactions. We count the L2 user transactions, not the L1 batch settlement transaction.
- Bridge transactions may count on both source and destination chains

## A4. Double-Counting With Other Capsules
- DeFi transactions (DEX swaps, lending, etc.) ARE counted within L1/L2 totals
- Stablecoin transfers ARE counted within L1/L2 totals
- CEX trades are NOT counted (off-chain)
- Do NOT sum L1/L2 + DeFi + Stablecoins for a sector total

## A5. "Others" Category
- Includes Tron, Avalanche, Polygon, Fantom, Cosmos chains, Near, Sui, Aptos, zkSync, Starknet
- Estimated at ~3M daily combined; likely an underestimate
- Tron alone may process 3-5M daily transactions (primarily USDT)

## A6. Value Transfer vs Transaction Count
- Transaction count and value transferred are weakly correlated
- Bitcoin has few transactions but high value per transaction (~$50K avg)
- Solana has many transactions but low value per transaction (<$10 avg)
- This capsule focuses on transaction count/TPS, not value

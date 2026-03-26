# DeFi — Key Assumptions

## A1. DEX Volume is On-Chain and Verifiable
- Unlike CEX volume, DEX trades settle on-chain via smart contracts
- DeFiLlama reads events directly from blockchain data
- This makes DEX volume data higher confidence than CEX data
- However, MEV bots and sandwich attacks inflate volume (est. 10-20% of DEX volume is bot-driven)

## A2. Double-Counting — The Critical Issue
- ALL DeFi transactions are L1/L2 transactions
- A Uniswap swap on Ethereum L1 = 1 DeFi transaction + 1 Ethereum L1 transaction
- A Raydium swap on Solana = 1 DeFi transaction + 1 Solana transaction
- Stablecoin transfers used within DeFi = overlap with stablecoins capsule
- CEX trading has ZERO overlap (off-chain settlement)

## A3. TVL Is a Stock Metric, Not a Flow Metric
- TVL = total capital locked at a point in time
- It does NOT measure throughput or transaction volume
- TVL can increase without any transactions (if ETH price rises, ETH-denominated TVL rises in USD)
- TVL double-counts: same dollar can be "locked" in multiple protocols via rehypothecation

## A4. Perp DEX Volume = Notional
- Same caveat as CEX derivatives: notional volume overstates economic activity
- A $100 trade with 50x leverage = $5,000 notional volume
- Spot DEX volume is a more honest measure of capital flow

## A5. User Count = Address Count
- "21.7M unique users" = unique wallet addresses
- One human often uses 2-10 wallets (privacy, strategy separation)
- True unique human users may be 5-10M
- Sybil activity (airdrop farming) inflates address counts further

## A6. Lending/Borrowing Is Not Counted as "Volume"
- We report lending TVL and open borrows as stock metrics
- We do NOT add lending flow to DEX trading volume
- The "DeFi volume" headline ($4.16T) = DEX spot + DEX perps only

## A7. Projection Methodology
- Baseline: DEX-to-CEX ratio continues growing from ~10% to ~25% by 2030
- High growth: DeFi captures traditional finance use cases (RWA, equities on-chain)
- Conservative: Memecoin boom fades, regulatory pressure
- All scenarios follow crypto's cyclical pattern (bull 2025-2026, bear 2027-2028)

# Stablecoins — Key Assumptions

## A1. Raw Volume vs Adjusted Volume
- The $27.6T figure is raw on-chain volume — every stablecoin movement on every chain
- Visa's adjusted figure ($5.7T) attempts to isolate genuine payment activity
- We report both, with the raw figure as the headline (consistent with how the industry reports)
- True economic activity is between the two: likely $5-15T

## A2. Transaction Count Estimation
- ~45M daily stablecoin transactions is sourced from analytics aggregators
- This includes all types: simple transfers, DEX swaps, lending deposits, bridge movements
- Not all "transactions" are P2P payments — many are DeFi interactions
- Confidence: 🟡 Medium

## A3. Double-Counting — The Critical Issue
- Stablecoin transfers ARE L1/L2 blockchain transactions
- A USDT transfer on Tron = 1 stablecoin transfer + 1 Tron transaction
- A stablecoin DEX swap = 1 stablecoin transfer + 1 DeFi transaction + 1 L1/L2 transaction
- Do NOT sum stablecoins + L1/L2 + DeFi for a sector total

## A4. CEX vs On-Chain
- CEX internal stablecoin transfers (trading pairs, deposits to other users) are OFF-CHAIN
- Only deposits to and withdrawals from CEXs appear on-chain
- The $27.6T figure is on-chain only; total stablecoin usage including CEX is higher

## A5. USDT Transparency
- Tether has faced scrutiny over reserves and reporting
- Transfer volume data is on-chain and verifiable regardless of reserve backing
- Market cap figures depend on Tether's attestations
- We treat transfer volume as reliable but note the reserve controversy

## A6. Chain Attribution
- Same stablecoin (e.g., USDT) exists on multiple chains
- Transfer volume is attributed to the chain where the transfer occurs
- Cross-chain bridge movements count on both source and destination chains
- This creates some double-counting in aggregate volume figures

## A7. Historic Data Quality
- 2022-2024: Good data from TRM Labs, Artemis, Visa
- 2020-2021: Estimated from available chain-specific data
- 2019: Very rough estimate
- Pre-2019: Essentially zero meaningful stablecoin activity

## A8. "Surpassing Visa" Context
- The $27.6T vs Visa+Mastercard comparison is technically accurate but misleading
- Visa processes ~773B transactions (count) vs ~45M x 365 = ~16B stablecoin transactions
- Stablecoins "surpass" Visa in VALUE but are ~50x fewer TRANSACTIONS
- Average stablecoin transfer ($1,680) is ~25x the average card transaction ($67)

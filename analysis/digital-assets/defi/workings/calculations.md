# DeFi — Calculations & Methodology

## 1. DEX Spot Volume

### Total 2024
- Source: DeFiLlama / CoinGecko 2024 Annual Report
- DEXs collectively processed over $1.76T in spot volume in 2024
- Up from $648B in 2023 (+172%)

### Chain Breakdown
- Solana: ~$969B (annual DEX volume from $42.1B in 2023 → $968.9B in 2024; ~23x growth)
- Ethereum L1: ~$350B (estimated from DeFiLlama chain breakdown)
- Arbitrum: ~$100B
- Base: ~$80B
- BNB Chain: ~$70B
- Others: ~$191B (residual to reach $1.76T)

### DEX-to-CEX Ratio
- Spot: $1.76T / $18.83T = 9.35%
- Including perps: $4.16T / $77.3T = 5.4%
- By Jan 2025, the DEX-to-CEX spot ratio reached ~20%

## 2. DEX Perpetual Futures Volume

### Total 2024
- Source: CoinGecko State of Crypto Perpetuals
- ~$2.4T cumulative perpetual trading volume in 2024
- Up 132% from 2023

### Protocol Breakdown
- Hyperliquid: ~50% of Q4 volume → est. ~$1.2T annual
- dYdX: fell to 3rd, behind Jupiter → est. ~$400B
- Jupiter Perps: Solana-native → est. ~$200B
- GMX: Arbitrum → est. ~$100B
- Others: ~$500B

## 3. TVL Trajectory

- Jan 2024: ~$54B
- Q1 2024: $93B
- Mid-Jun 2024: ~$105B
- Summer 2024: Dip
- Dec 2024: $140B
- Growth: +159% YoY

### TVL Double-Counting
TVL is notorious for double-counting:
1. Deposit 1 ETH to Lido → receive 1 stETH (TVL counts 1 ETH)
2. Deposit stETH to Aave → TVL counts stETH again
3. Borrow USDC against it → deposit to Uniswap LP
4. Same dollar is "locked" in 3 protocols simultaneously

True unique capital in DeFi is likely 40-60% of reported TVL.

## 4. DeFi Transaction Count Estimation

DeFi transactions are harder to count than volume because:
- A single swap = 1 transaction
- A complex yield farming strategy = 5-10 transactions (approve, deposit, stake, claim, compound)

Rough estimate:
- DEX swaps: If avg swap = $2,000, then $1.76T / $2,000 = ~880M swap transactions in 2024
- Lending: Borrows, repayments, liquidations → ~50-100M transactions
- Staking: Stakes, unstakes, claims → ~50M transactions
- Other DeFi: Bridges, yield, governance → ~100M transactions
- **Total DeFi-specific transactions: ~1-1.2B in 2024**
- This is ~4% of all L1/L2 transactions (27B)

## 5. Historic Volume Series

| Year | DEX Spot Volume | Source |
|------|----------------|--------|
| 2019 | ~$2B | Pre-AMM era (IDEX, 0x) |
| 2020 | ~$25B | Uniswap v2 launch (May 2020), DeFi summer |
| 2021 | ~$600B+ | Multi-chain expansion, Uniswap v3 |
| 2022 | ~$500B | Bear market, Terra/Luna collapse |
| 2023 | ~$648B | Recovery, Solana DeFi revival |
| 2024 | ~$1.76T | Solana memecoin frenzy, L2 growth |

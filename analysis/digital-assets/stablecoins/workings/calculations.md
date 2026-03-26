# Stablecoins — Calculations & Methodology

## 1. Annual Transfer Volume

### Raw Volume
- Source: CryptoSlate, citing CEX.IO/Bitget research
- Total 2024: $27.6 trillion
- USDT + USDC combined: $23T (90% increase from 2023)

### Adjusted Volume (Visa Method)
- Visa Onchain Analytics strips non-payment activity:
  - Removes: HFT bot activity, smart contract-to-contract routing, bridge relays, institutional treasury management
  - Keeps: Person-to-person, merchant payments, remittances, genuine commerce
- $2.5T in 12 months to May 2024
- Annualised to ~$5.7T for full 2024 (H2 was more active than H1)

### Interpretation
- Raw $27.6T overstates economic activity by ~5x
- Adjusted $5.7T is more meaningful but may undercount (Visa's methodology is conservative)
- True economic payment volume is likely $5-15T range

## 2. TPS Calculation

### Daily Transaction Estimate
- Source: World Metrics / Artemis aggregation
- ~45M daily stablecoin transactions across all chains
- This includes: transfers, DEX swaps involving stablecoins, lending deposits/withdrawals

### TPS
- 45,000,000 / 86,400 = **~520 TPS**

### Peak TPS
- During high-volatility days (market crashes, liquidation cascades), stablecoin activity spikes 3-4x
- Estimated peak: ~1,500-2,000 TPS

## 3. Market Share Calculations

### By Transfer Volume
- USDC: 70% of $27.6T = ~$19.3T
- USDT: 25% = ~$6.9T
- DAI/Others: 5% = ~$1.4T

### By Active Addresses
- USDT: 67% of ~1.5M daily addresses = ~1M USDT addresses
- USDC: 27% = ~405K
- Others: 6% = ~90K

### Interpretation
- USDC avg transfer: $19.3T / (405K x 365) = ~$131K avg
- USDT avg transfer: $6.9T / (1M x 365) = ~$19K avg
- This confirms USDC is institutional/large transfers; USDT is retail/P2P

## 4. Velocity Calculation

Velocity = Annual Transfer Volume / Market Cap
- 2024: $27.6T / $205B = 134.6x turnover
- 2023: $12T / $130B = 92.3x turnover
- Velocity increased ~46% YoY

This means each stablecoin dollar was transferred ~135 times in 2024.
(Adjusted velocity: $5.7T / $205B = ~28x — more comparable to traditional money velocity)

## 5. Historic Volume Series

| Year | Transfer Volume | Market Cap | Velocity | Source |
|------|----------------|-----------|----------|--------|
| 2019 | ~$0.2T | ~$5B | ~40x | Estimated |
| 2020 | ~$1T | ~$25B | ~40x | Estimated |
| 2021 | ~$5T | ~$140B | ~36x | Estimated |
| 2022 | ~$7T | ~$135B | ~52x | TRM Labs |
| 2023 | ~$12T | ~$130B | ~92x | TRM Labs |
| 2024 | $27.6T | ~$205B | ~135x | CryptoSlate |

## 6. Projection Methodology

Key drivers:
1. **Market cap growth** — new stablecoin issuance (regulated issuers, CBDC interop)
2. **Velocity growth** — more use cases = more transfers per dollar
3. **Chain expansion** — cheaper chains = more micro-transfers
4. **Regulatory impact** — clarity drives institutional adoption; restrictions could cap growth

Baseline: Market cap doubles to $500B by 2030; velocity continues rising.
High growth: Stablecoins become dominant digital payment rail globally.
Conservative: Regulation caps growth; CBDCs capture market share.

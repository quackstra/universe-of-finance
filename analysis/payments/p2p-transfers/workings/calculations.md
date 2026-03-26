# Peer-to-Peer Transfers — Calculations

## TPS Derivation

### Annual-to-TPS Formula
```
TPS = annual_transactions / (365 × 86,400)
TPS = annual_transactions / 31,536,000
```

### 2024 Aggregate

**Platform transaction counts:**

| Platform | Txns (B) | Value ($B) | Avg Txn Size | Data Quality |
|----------|---------|-----------|--------------|--------------|
| Zelle | 3.6 | $1,040 | $289 | Direct from EWS |
| Venmo | 2.3 (est.) | $280 | $122 (est.) | TPV from PayPal; count estimated |
| Cash App | 1.5 (est.) | $283 (inflows) | $189 | Inflows from Block; count estimated |
| PayPal P2P | 0.3 (est.) | $150 (est.) | $500 (est.) | Rough estimate |
| Non-US | 0.8 (est.) | $105 (est.) | $131 (est.) | Rough estimate |
| **Total** | **8.5** | **~$1,858** | **$219** | |

Note: Annual value in data.json uses $2.8T which includes Cash App total inflows ($283B) rather than pure P2P. The platform breakdown table above is more conservative.

```
TPS = 8,500,000,000 / 31,536,000 = 269.5 ≈ 270 TPS
```

### Venmo Transaction Count Estimate
- Q1 2024 TPV: $69B
- Annual TPV estimate: $69B × 4 = $276B → round to $280B
- Average Venmo transaction size (industry est.): ~$120
- Transaction count: $280B / $120 = 2.33B ≈ 2.3B

### Cash App Transaction Count Estimate
- Annual inflows: $282.9B
- Pure P2P estimated at ~60% of inflows: ~$170B
- Average P2P transaction (est.): ~$115
- P2P transaction count: ~$170B / $115 = 1.48B ≈ 1.5B
- (Note: if counting all inflow transactions, count would be higher)

### Zelle Average Transaction Size
```
$1,040,000,000,000 / 3,600,000,000 = $288.89 ≈ $289
```

## Historic Calculations

### Aggregate US P2P — Building Year by Year

| Year | Zelle ($B) | Venmo ($B) | Cash App ($B) | Other ($B) | Total ($B) |
|------|-----------|-----------|--------------|-----------|-----------|
| 2019 | $187 | $102 | $40 | $121 | $450 |
| 2020 | $307 | $159 | $75 | $139 | $680 |
| 2021 | $490 | $230 | $100 | $100 | $920 |
| 2022 | $629 | $244 | $128 | $149 | $1,150 |
| 2023 | $806 | $270 | $210 | $164 | $1,450 |
| 2024 | $1,040 | $280 | $283 | $147 | $1,750 |

### Transaction Count Estimates by Year

Using average transaction sizes that gradually increase over time:

| Year | Zelle Txns (B) | Venmo Txns (B) | Cash App Txns (B) | Other (B) | Total (B) |
|------|---------------|---------------|-------------------|----------|----------|
| 2019 | 0.74 | 0.9 | 0.4 | 0.66 | 2.7 |
| 2020 | 1.2 | 1.3 | 0.7 | 0.7 | 3.9 |
| 2021 | 1.8 | 1.7 | 0.9 | 0.7 | 5.1 |
| 2022 | 2.3 | 1.8 | 1.0 | 0.7 | 5.8 |
| 2023 | 2.9 | 2.1 | 1.3 | 0.7 | 7.0 |
| 2024 | 3.6 | 2.3 | 1.5 | 1.1 | 8.5 |

## Growth Rate Calculations

### US P2P 5-Year CAGR (Transactions)
```
CAGR = (7.7/2.1)^(1/5) - 1 = 3.667^0.2 - 1 = 1.297 - 1 = 29.7%
```
Wait — using 2.1B (US only 2019) to 7.7B (US only 2024):
```
CAGR = (7.7/2.1)^(1/5) - 1 ≈ 29.7%
```

Using global total:
```
CAGR = (8.5/2.7)^(1/5) - 1 = 3.148^0.2 - 1 = 1.258 - 1 = 25.8%
```

### Zelle 5-Year CAGR (Transactions)
```
CAGR = (3.6/0.74)^(1/5) - 1 = 4.865^0.2 - 1 = 1.372 - 1 = 37.2%
```

### Zelle 5-Year CAGR (Value)
```
CAGR = (1040/187)^(1/5) - 1 = 5.561^0.2 - 1 = 1.409 - 1 = 40.9%
```

### Cash App 5-Year CAGR (Value)
```
CAGR = (283/40)^(1/5) - 1 = 7.075^0.2 - 1 = 1.479 - 1 = 47.9%
```

## Projection Methodology

### Baseline: 12% declining to 6% by 2035
- US market maturing; Zelle growth slowing from 25% to ~10%
- Venmo essentially flat; Cash App still growing at ~15%
- Non-US P2P growing faster but from small base

Calculation for 2025:
```
8.5B × 1.12 = 9.52B ≈ 9.5B
```

For 2030 (avg ~10% CAGR 2025-2030):
```
9.5B × 1.10^5 = 15.3B ≈ 15.5B
```

For 2035 (avg ~6% CAGR 2030-2035):
```
15.5B × 1.06^5 = 20.7B
```

### High Growth: 16% declining to 10%
- Assumes P2P becomes primary bill-splitting and small business payment method
- Assumes international expansion of US platforms

### Conservative: 8% declining to 4%
- Assumes market saturation in US by 2027
- Assumes regulatory constraints (CFPB fraud rules on Zelle)

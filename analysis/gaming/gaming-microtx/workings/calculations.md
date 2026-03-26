# In-Game Microtransactions — Calculations

## 1. Annual Transaction Count (2024)

### Mobile IAP Transactions
```
Mobile IAP Revenue (2024): $81.0B (Sensor Tower)
Average Transaction Value:  $8.50 (see assumptions.md#A2)
Mobile Transactions = $81.0B / $8.50 = 9.53B transactions
```

### PC IAP Transactions
```
PC IAP Revenue (2024): ~$18.0B (estimated, see assumptions.md#A3)
Average Transaction Value:  $12.00 (see assumptions.md#A2)
PC Transactions = $18.0B / $12.00 = 1.50B transactions
```

### Console IAP Transactions
```
Console IAP Revenue (2024): ~$15.0B (estimated, see assumptions.md#A3)
Average Transaction Value:  $12.00 (see assumptions.md#A2)
Console Transactions = $15.0B / $12.00 = 1.25B transactions
```

### Total
```
Total Annual Transactions (2024) = 9.53B + 1.50B + 1.25B = 12.28B
Rounded: ~12.3B transactions
```

## 2. TPS Calculation (2024)

```
Seconds per year = 365.25 × 86,400 = 31,557,600
Average TPS = 12,280,000,000 / 31,557,600 = ~389 TPS
Peak TPS (est.) = 389 × 2.0 = ~778 TPS
```

## 3. Daily Volume
```
Daily transactions = 12,280,000,000 / 365.25 = ~33.6 million/day
```

## 4. Historical Transaction Estimates (2019-2024)

Revenue sources: Newzoo annual reports, Sensor Tower, SuperData (now Nielsen).
Transaction counts derived using same ATV methodology, adjusted for lower historical ATVs.

| Year | Est. Revenue ($B) | Est. ATV ($) | Est. Transactions (B) | Avg TPS | Notes |
|------|-------------------|-------------|----------------------|---------|-------|
| 2019 | 72 | 7.00 | 10.29 | 326 | Pre-COVID baseline; lower ATV due to more small mobile txns |
| 2020 | 94 | 7.50 | 12.53 | 397 | COVID boom (+30% revenue); ATV rose as engagement deepened |
| 2021 | 89 | 7.75 | 11.48 | 364 | Post-COVID correction in mobile (-5%) |
| 2022 | 86 | 8.00 | 10.75 | 341 | Continued correction, inflation impact (-3%) |
| 2023 | 92 | 8.25 | 11.15 | 354 | Stabilization (+5% revenue) |
| 2024 | 114 | 8.83 | 12.28* | 389 | Mobile rebound; uses platform-specific ATVs |

*2024 uses weighted ATV across platforms rather than single ATV.

### Revenue Derivation Notes
- 2019: Mobile $68B (Newzoo) × ~75% IAP + PC/console IAP ~$15B
- 2020: Mobile $86B (COVID surge) × ~75% IAP + PC/console IAP ~$20B
- 2021: Mobile $82B × ~75% IAP + PC/console IAP ~$20B
- 2022: Mobile $78B (post-COVID dip) × ~75% IAP + PC/console IAP ~$19B
- 2023: Mobile $78.5B × ~75% IAP + PC/console IAP ~$25B (live service growth)
- 2024: Mobile $81B (Sensor Tower) + PC $18B + Console $15B = $114B

## 5. Growth Rate Analysis

```
CAGR 2019-2024 (5yr, by transactions): (12.28/10.29)^(1/5) - 1 = 3.6%
CAGR 2019-2024 (5yr, by revenue):      (114/72)^(1/5) - 1   = 9.6%

Note: Revenue CAGR is much higher than transaction CAGR because ATV has been
rising (players spending more per transaction, not just more transactions).
```

## 6. Projection Models (2026-2035)

### Baseline (6% transaction CAGR)
Assumes mobile market matures, emerging market growth offsets developed market plateau.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 13.80 | 437 |
| 2028 | 15.51 | 491 |
| 2030 | 17.43 | 552 |
| 2035 | 23.32 | 739 |

### High Growth (9% transaction CAGR)
AI personalization, VR/AR platforms, deeper emerging market penetration.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 14.59 | 462 |
| 2028 | 17.34 | 550 |
| 2030 | 20.62 | 653 |
| 2035 | 31.72 | 1,005 |

### Conservative (3% transaction CAGR)
Regulatory crackdowns on loot boxes, player fatigue, economic headwinds.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 13.03 | 413 |
| 2028 | 13.83 | 438 |
| 2030 | 14.67 | 465 |
| 2035 | 17.01 | 539 |

## 7. Sensitivity Analysis

The largest source of uncertainty is the Average Transaction Value.

| ATV Assumption | Implied 2024 Transactions | Implied TPS |
|---------------|--------------------------|-------------|
| $5.00 (low) | 19.5B | 618 |
| $8.83 (base) | 12.3B | 389 |
| $12.00 (high) | 9.0B | 285 |
| $15.00 (very high) | 7.2B | 228 |

A ±40% swing in ATV produces a proportional inverse swing in transaction count.
This is the primary reason for the 🔴 Low confidence rating on transaction counts.

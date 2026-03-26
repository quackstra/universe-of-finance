# Digital Game Sales & Subscriptions — Calculations

## 1. Annual Transaction Count (2024)

### A. Full Game Purchases

```
Digital game sales revenue (excl. subs, excl. IAP): ~$52.0B
  - PC digital: $21.0B
  - Console digital: $28.5B
  - Mobile premium: $2.5B

Weighted average selling price (ASP):
  PC: $21.0B / $25 ASP = 840M transactions
  Console: $28.5B / $45 ASP = 633M transactions
  Mobile premium: $2.5B / $5 ASP = 500M transactions

Total game purchase transactions = 840M + 633M + 500M = 1,973M = ~1.97B
```

### B. DLC / Expansion Purchases

```
DLC market estimated at ~$12B within the $52B figure above
(already included in platform revenue figures)
DLC transactions at $15 avg = 800M transactions
Note: DLC is already counted in the platform revenue above;
these are a subset of the 1.97B, not additive.
```

Revised: The $52B includes DLC. Breaking it down:
```
Base game revenue: ~$40B
DLC revenue: ~$12B
Base game transactions: $40B / $30 ASP = 1,333M
DLC transactions: $12B / $15 ASP = 800M
Total game + DLC transactions = 2,133M = ~2.13B
```

### C. Subscription Transactions

```
Total subscribers across all services: ~140.2M
  (51.2M PS Plus + 35M Game Pass + 38M Nintendo + 13M EA Play + 3M Ubisoft+)

Average transactions per subscriber per year: 5.4
  (40% monthly × 12 + 60% annual × 1 = 5.4)

Subscription transactions = 140.2M × 5.4 = 757M = ~0.76B
```

### D. Total

```
Total Annual Transactions (2024) = 2.13B (game + DLC) + 0.76B (subscriptions) = 2.89B
Rounded: ~2.9B transactions
```

## 2. TPS Calculation (2024)

```
Seconds per year = 365.25 × 86,400 = 31,557,600
Average TPS = 2,890,000,000 / 31,557,600 = ~91.6 TPS
Peak TPS (est.) = 91.6 × 3.0 = ~275 TPS
```

Peak multiplier is higher (3.0x) than microtransactions because game sales spike
dramatically during seasonal sales (Steam Summer/Winter Sale, Black Friday,
holiday gifting season, major launch days).

## 3. Daily Volume
```
Daily transactions = 2,890,000,000 / 365.25 = ~7.9 million/day
```

## 4. Historical Transaction Estimates (2019-2024)

| Year | Est. Revenue ($B) | Est. Txns (B) | Avg TPS | Notes |
|------|-------------------|---------------|---------|-------|
| 2019 | 38.0 | 1.72 | 55 | Pre-COVID; lower digital share (~65% console) |
| 2020 | 47.5 | 2.28 | 72 | COVID boom; digital share jumped to 75%+ |
| 2021 | 43.7 | 2.15 | 68 | Post-COVID dip; fewer major releases |
| 2022 | 41.5 | 2.05 | 65 | Continued correction; inflation impact |
| 2023 | 45.0 | 2.30 | 73 | Recovery; Zelda TotK, Baldur's Gate 3, Starfield |
| 2024 | 60.2 | 2.89 | 92 | Strong year; digital share 84%+; subscription growth |

### Revenue Derivation
- 2019: Total market ~$144B; non-IAP digital ~26% = ~$38B
- 2020: Total ~$178B; non-IAP digital ~27% = ~$47.5B
- 2021: Total ~$176B; non-IAP digital ~25% = ~$43.7B
- 2022: Total ~$172B (est); non-IAP digital ~24% = ~$41.5B
- 2023: Total ~$177B; non-IAP digital ~25% = ~$45B
- 2024: Total ~$183B; non-IAP digital ~33% = ~$60.2B

### Transaction Count Derivation
Uses year-specific blended ASP (declining over time as digital sales increase
discount frequency and indie share grows):
- 2019: ASP ~$22 → 1.72B
- 2020: ASP ~$21 → 2.28B
- 2021: ASP ~$20 → 2.15B
- 2022: ASP ~$20 → 2.05B
- 2023: ASP ~$20 → 2.30B
- 2024: ASP ~$21 (slight uptick from subscription revenue) → 2.89B

Plus subscription transactions:
- 2019: ~60M total subscribers × 4.0 avg txns = 240M
- 2020: ~80M × 4.5 = 360M
- 2021: ~100M × 4.8 = 480M
- 2022: ~120M × 5.0 = 600M
- 2023: ~130M × 5.2 = 676M
- 2024: ~140M × 5.4 = 757M

## 5. Growth Rate Analysis

```
CAGR 2019-2024 (5yr, transactions): (2.89/1.72)^(1/5) - 1 = 10.9%
CAGR 2019-2024 (5yr, revenue):      (60.2/38.0)^(1/5) - 1 = 9.6%

Note: Transaction CAGR exceeds revenue CAGR because ASPs have been declining
(more indie titles, deeper discounts, subscription model) even as total
spending increases. Opposite pattern to microtransactions.
```

## 6. Projection Models (2026-2035)

### Baseline (5% Transaction CAGR)
Digital shift nearly complete; subscription growth moderates; steady new game releases.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 3.19 | 101 |
| 2028 | 3.51 | 111 |
| 2030 | 3.87 | 123 |
| 2035 | 4.94 | 157 |

### High Growth (8% Transaction CAGR)
Cloud gaming (GeForce NOW, Xbox Cloud) expands addressable market; emerging market
smartphone gaming drives premium app purchases; new subscription tiers.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 3.37 | 107 |
| 2028 | 3.93 | 125 |
| 2030 | 4.59 | 145 |
| 2035 | 6.74 | 214 |

### Conservative (2% Transaction CAGR)
Market saturation; subscription fatigue leads to churn; fewer blockbuster releases;
game preservation / backlog reduces new purchase frequency.

| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 3.01 | 95 |
| 2028 | 3.13 | 99 |
| 2030 | 3.25 | 103 |
| 2035 | 3.59 | 114 |

## 7. Sensitivity Analysis

### Game Purchase ASP Sensitivity

| ASP Assumption | Implied 2024 Game Txns | Total (+ subs) | TPS |
|---------------|----------------------|----------------|-----|
| $15 (low) | 3.47B | 4.22B | 134 |
| $21 (base blended) | 2.13B | 2.89B | 92 |
| $30 (high) | 1.73B | 2.49B | 79 |
| $40 (very high) | 1.30B | 2.06B | 65 |

### Subscription Split Sensitivity

| Monthly % | Txns per Sub/yr | Sub Txns (B) | Total |
|-----------|----------------|-------------|-------|
| 20% (mostly annual) | 3.2 | 0.45B | 2.58B |
| 40% (base) | 5.4 | 0.76B | 2.89B |
| 60% (mostly monthly) | 7.6 | 1.07B | 3.20B |
| 80% (mostly monthly) | 9.8 | 1.37B | 3.50B |

The monthly/annual split assumption has a meaningful impact (~±20% on total).

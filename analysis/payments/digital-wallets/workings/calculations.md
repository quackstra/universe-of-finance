# Digital Wallets & Mobile Payments — Calculations

## TPS Derivation

### Annual-to-TPS Formula
```
TPS = annual_transactions / (365 × 86,400)
TPS = annual_transactions / 31,536,000
```

### 2024 Aggregate Calculation

**Building the global aggregate (avoiding double-counting):**

| Platform | Annual Txns (B) | Notes |
|----------|----------------|-------|
| China mobile payments (all) | 280 | Includes Alipay + WeChat + others; PBOC aggregate |
| UPI (India) | 172 | NPCI official; includes Google Pay India |
| M-Pesa | 30 | Safaricom AR 2024 |
| Apple Pay (non-overlay est.) | 5 | ~25% of 20B total are non-card-rail (in-app, web) |
| Other wallets (Samsung, regional) | 133 | Residual estimate |
| **Total** | **620** | |

```
TPS = 620,000,000,000 / 31,536,000 = 19,660 TPS
```

### Peak TPS Estimate
- UPI peak month (Dec 2024): 16.73 billion txns / 31 days / 86,400 = ~6,250 TPS
- Alibaba Singles' Day 2024 peak: historically ~500,000 TPS for seconds, sustained ~50,000 TPS for hours
- Combined peak across all platforms: ~45,000 TPS (conservative, not all peak simultaneously)

### Daily Volume
```
620,000,000,000 / 365 = 1,698,630,137 ≈ 1.7 billion daily
```

## Platform-Specific Calculations

### UPI TPS
```
172,000,000,000 / 31,536,000 = 5,454 TPS average
```

### China Mobile TPS
```
280,000,000,000 / 31,536,000 = 8,879 TPS average
```

### M-Pesa TPS
```
30,000,000,000 / 31,536,000 = 951 TPS average
```

### Alipay Daily Check
- Reported: 120 million daily transactions
- Annual: 120,000,000 × 365 = 43,800,000,000 ≈ 44 billion
- TPS: 44,000,000,000 / 31,536,000 = 1,395 TPS

### WeChat Pay Estimate
- Reported: 1 billion daily transactions (industry est.), of which 450M from transit
- Annual: ~365 billion if taken at face value
- However, China total is 280B and Alipay is ~44B, leaving ~236B for WeChat + others
- WeChat Pay likely ~130-150B (55% of non-Alipay China mobile), using 130B conservatively
- TPS: 130,000,000,000 / 31,536,000 = 4,122 TPS

## Historic Aggregate Methodology

Built bottom-up for each year using:
1. UPI official NPCI data (high confidence)
2. China PBOC mobile payment counts (medium confidence)
3. M-Pesa Safaricom reports (high confidence)
4. Remainder allocated to Apple Pay, Google Pay (non-India), Samsung Pay, regional wallets

| Year | UPI | China | M-Pesa | Others (est.) | Total |
|------|-----|-------|--------|--------------|-------|
| 2019 | 12.5 | 101 | 12.6 | 54 | 180 |
| 2020 | 22.3 | 123 | 14.5 | 60 | 220 |
| 2021 | 46.0 | 178 | 18.3 | 68 | 310 |
| 2022 | 83.8 | 235 | 22.0 | 69 | 410 |
| 2023 | 117.6 | 260 | 25.5 | 87 | 490 |
| 2024 | 172.0 | 280 | 30.0 | 138 | 620 |

## Growth Rate Calculations

### 5-Year CAGR (2019-2024)
```
CAGR = (620/180)^(1/5) - 1 = 3.444^0.2 - 1 = 1.281 - 1 = 28.1%
```

### 2-Year CAGR (2022-2024)
```
CAGR = (620/410)^(1/2) - 1 = 1.512^0.5 - 1 = 1.229 - 1 = 22.9%
```

### UPI 5-Year CAGR
```
CAGR = (172/12.5)^(1/5) - 1 = 13.76^0.2 - 1 = 1.692 - 1 = 69.2%
```

### China 5-Year CAGR
```
CAGR = (280/101)^(1/5) - 1 = 2.772^0.2 - 1 = 1.226 - 1 = 22.6%
```

### M-Pesa 5-Year CAGR
```
CAGR = (30/12.6)^(1/5) - 1 = 2.381^0.2 - 1 = 1.192 - 1 = 19.2%
```

## Projection Methodology

### Baseline: 18% CAGR tapering to 12% by 2035
- 2025-2027: 18% CAGR (continued strong adoption in India, Africa, SE Asia)
- 2028-2030: 15% CAGR (market maturation in China, India nearing saturation)
- 2031-2035: 12% CAGR (global saturation, incremental growth from micropayments)

### High Growth: 22% tapering to 15%
- Assumes UPI-like adoption in SE Asia, Latin America, Africa
- Assumes continued 40%+ UPI growth through 2027

### Conservative: 14% tapering to 8%
- Assumes Chinese market stalls, UPI growth halves
- Assumes regulatory friction (antitrust) limits Western wallet growth

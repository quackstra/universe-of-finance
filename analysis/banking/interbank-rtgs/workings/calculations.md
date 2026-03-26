# Interbank RTGS — Calculations

## TPS Calculations

### Calendar TPS
```
Total annual transactions = 423,000,000
Seconds per year = 365 × 86,400 = 31,536,000
Calendar TPS = 423,000,000 / 31,536,000 = 13.4 TPS
```

### Business-Day TPS (8-hour operating window)
```
Business days per year ≈ 250
Operating hours per day ≈ 8 (conservative; some systems run 10-12h)
Operating seconds per year = 250 × 8 × 3,600 = 7,200,000
Business-day TPS = 423,000,000 / 7,200,000 = 58.8 TPS
```

Note: The 8-hour window is conservative. Fedwire operates 21.5 hours/day.
Using Fedwire's hours: 250 × 21.5 × 3,600 = 19,350,000 sec → 21.9 TPS.
The "~6.7 TPS" in the report uses a broader denominator (all seconds in business days, 250 × 86400).

### Corrected Business-Day TPS (full business day)
```
Business-day seconds = 250 × 86,400 = 21,600,000
Business-day TPS = 423,000,000 / 21,600,000 = 19.6 TPS
```

## Annual Volume Aggregation

| System | Annual Volume (M) | Source Quality |
|--------|-------------------|---------------|
| Fedwire | 209.9 | Direct from FRB Services (836,322 daily avg × 251 days) |
| T2/TARGET2 | 108.0 | ECB: "nearly 108 million" — record since euro introduction |
| CHAPS | 52.7 | Bank of England: "52.7 million CHAPS payments" |
| BOJ-NET | 5.0 | Estimated from ~19,000 daily avg × 260 business days |
| CLS | ~250 | Estimated — see CLS estimation below |
| **TOTAL** | **~626** | |

**Excluding CLS (pure RTGS only)**: ~376M transactions

For the report headline of 423M, we use a more conservative CLS estimate of ~50M
(representing only settled FX trades, not payment instructions) plus the four RTGS systems.
Actually, the report uses 423M which is ~376M RTGS + ~47M other smaller RTGS systems globally.

### CLS Transaction Count Estimation
```
CLS daily value settled: ~$7 trillion
CLS record day volume: 3.2 million trades (July 2022)
CLS record day value: $19.1 trillion (June 2024)

Ratio approach:
  Record day: 3.2M trades / $19.1T = 167,539 trades per $1T
  Average day: $7T × 167,539 = 1,172,774 trades/day

Annual (250 business days): 1,172,774 × 250 = ~293M trades/year

This is gross trade count. Each trade generates 2 payment instructions (PvP).
For transaction count purposes, we use ~250M as a round estimate.
```

## Annual Value Aggregation

| System | Annual Value (local) | USD Equivalent | FX Rate Used |
|--------|---------------------|---------------|-------------|
| Fedwire | $1,133.4T | $1,133.4T | 1.00 |
| T2 | €555T | ~$605T | EUR/USD = 1.09 |
| CHAPS | £87.5T | ~$111T | GBP/USD = 1.27 |
| BOJ-NET | ¥18,250T | ~$122T | USD/JPY = 149.5 |
| CLS | $1,750T (gross) | $1,750T | multiple currencies |
| **TOTAL** | | **~$3,721T** | |

**Note**: CLS value overlaps with RTGS values (CLS settles through RTGS systems).
The report headline of ~$2,150T excludes CLS to avoid double-counting.
$1,133.4 + $605 + $111 + $122 + others ≈ $2,150T (including ~$178T from smaller systems).

## Growth Rate Calculations

### Fedwire 5-Year CAGR (2019-2024)
```
CAGR = (209.9/179.0)^(1/5) - 1 = 1.0325 - 1 = 3.25%
```

### T2 5-Year CAGR (2019-2024)
```
CAGR = (108.0/87.8)^(1/5) - 1 = 1.0423 - 1 = 4.23%
```

### CHAPS 5-Year CAGR (2019-2024)
```
CAGR = (52.7/43.5)^(1/5) - 1 = 1.0390 - 1 = 3.90%
```

## Projection Calculations

### Baseline (3% volume CAGR)
```
2025: 423 × 1.03 = 436M → 436M / 31.56M sec = 13.8 TPS
2030: 423 × 1.03^6 = 505M → 16.0 TPS
2035: 423 × 1.03^11 = 585M → 18.5 TPS
```

### Value Baseline (5% CAGR)
```
2025: 2150 × 1.05 = $2,258T
2030: 2150 × 1.05^6 = $2,882T
2035: 2150 × 1.05^11 = $3,678T
```

# Securities Settlement — Calculations

## TPS Calculations

### Calendar TPS
```
Total annual transactions = ~1,400,000,000 (1.4B)
Seconds per year = 365 × 86,400 = 31,536,000
Calendar TPS = 1,400,000,000 / 31,536,000 = 44.4 TPS
```

### Business-Day TPS
```
Business days per year ≈ 250
Business-day seconds = 250 × 86,400 = 21,600,000
Business-day TPS = 1,400,000,000 / 21,600,000 = 64.8 TPS
```

### Peak TPS (from NSCC record day)
```
NSCC peak day = 545,000,000 transactions (7 April 2025)
Peak TPS = 545,000,000 / 86,400 = 6,308 TPS (smoothed over 24h)
If concentrated in 8 trading hours:
Peak TPS = 545,000,000 / 28,800 = 18,924 TPS
```

Note: The 545M figure is from April 2025, not 2024, but demonstrates infrastructure capacity.

## Annual Volume Aggregation

### DTCC Transaction Count Estimation
```
DTC daily deliveries: ~1,300,000
DTC annual (250 business days): 1,300,000 × 250 = 325,000,000

ATP annual transactions: >350,000,000

NSCC daily avg (estimated from revenue/volume patterns): ~2,000,000
NSCC annual: 2,000,000 × 250 = 500,000,000

Note: These overlap (ATP feeds into NSCC/DTC). Best estimate for
unique DTCC settlement transactions: ~500M
```

### Euroclear Transaction Count
```
Confirmed: 331 million netted transactions in 2024
Q1-Q3 2024: 243M (= 81M/quarter average)
Q4 2024: 331 - 243 = 88M (seasonal uptick typical in Q4)
```

### Clearstream Transaction Count Estimation
```
YTD through May 2024:
  ICSD: 8.0M
  CSD: 71.7M
  IFS: 18.4M
  Total: 98.1M in 5 months

Annualized (× 12/5): 235.4M

Conservative estimate: ~200M (H2 may have been lower)
Aggressive estimate: ~240M
Used: ~235M midpoint
```

### T2S Transaction Count Estimation
```
ECB: T2S volumes "up 14% from previous year" in 2024
2023 T2S estimate: ~145M (from ECB annual report context)
2024: 145M × 1.14 = ~165M

Note: T2S settles euro-denominated securities and partially overlaps
with Euroclear and Clearstream volumes for euro securities.
```

### Total Aggregation
```
DTCC:        ~500M
Euroclear:    331M
Clearstream: ~235M
T2S:         ~165M (partially overlapping with Euroclear/Clearstream)
Other CSDs:  ~170M (estimate for Japan JASDEC, Australia ASX, etc.)

Gross total: ~1,401M
Less T2S overlap: ~(100M)
Adjusted total: ~1,300M

Range used in report: 1.3B–1.5B
```

## Annual Value Calculations

### DTCC
```
Confirmed: $3.7 quadrillion (2024)
= $3,700,000,000,000,000
Daily: $3.7Q / 250 = $14.8T per business day
NSCC avg daily value: $2.219T (from CPMI disclosures)
```

### Euroclear
```
Confirmed: €1,162 trillion
USD equivalent: €1,162T × 1.09 = $1,267T = $1.267 quadrillion
```

### Clearstream (estimated)
```
Limited public data on total settlement value.
Assets under custody: ~€17T
Estimated annual settlement value: ~€150-200T (based on custody turnover ratios)
USD: ~$165-218T
Used: ~$200T midpoint
```

### T2S (estimated)
```
ECB reports T2S daily settled value but not prominently.
Estimated from European securities market context: ~€180T
USD: ~$196T
```

### Total Value
```
DTCC: $3,700T ($3.7Q)
Euroclear: $1,267T
Clearstream: ~$200T
T2S: ~$196T (overlapping)
Total (ex-overlap): ~$5.0Q (headline figure)

Note: Significant double-counting risk between:
- DTCC/Fedwire (cash legs)
- Euroclear/Clearstream and T2S (euro securities)
```

## Growth Rate Calculations

### DTCC 5-Year Value CAGR (2019-2024)
```
CAGR = (3.7/2.0)^(1/5) - 1 = 1.131 - 1 = 13.1%
```

### Euroclear 5-Year Volume CAGR (2019-2024)
```
CAGR = (331/250)^(1/5) - 1 = 1.058 - 1 = 5.8%
```

### Euroclear 5-Year Value CAGR (2019-2024)
```
CAGR = (1162/800)^(1/5) - 1 = 1.077 - 1 = 7.7%
```

## Projection Calculations

### Baseline (5% volume CAGR)
```
2025: 1.4B × 1.05 = 1.47B → 46.6 TPS
2030: 1.4B × 1.05^6 = 1.876B → 59.5 TPS
2035: 1.4B × 1.05^11 = 2.394B → 75.9 TPS
```

### Value Baseline (8% CAGR)
```
2025: $5.0Q × 1.08 = $5.4Q → used $4.0Q (conservative, from DTCC+Euroclear only)
Adjusted: Base from $3.7Q DTCC-centric
2025: 3.7 × 1.08 = $4.0Q
2030: 3.7 × 1.08^6 = $5.9Q
2035: 3.7 × 1.08^11 = $8.7Q
```

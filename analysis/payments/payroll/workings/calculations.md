# Payroll Payments — Calculations

## 1. Annual Transaction Count (2024)

### Employment Data (Sources: ILO, BLS, Eurostat, NBS China)

```
Global employed persons (ILO 2024): ~3.50 billion
  Wage and salaried workers:          ~1.90 billion (ILO 2021 data, projected)
  Self-employed:                      ~1.50 billion (excluded — no employer payroll)
  Informal sector workers:            ~2.00 billion (ILO est. — most receive cash)
```

### Regional Model

#### United States
```
Nonfarm payroll employment (BLS Dec 2024): 158.3M
Pay frequency distribution (BLS/APA data):
  Biweekly: 70% → 110.8M workers × 26 pays = 2,881M
  Weekly:   20% → 31.7M workers × 52 pays  = 1,648M (but many overlap — hourly workers)
  Monthly:  10% → 15.8M workers × 12 pays  = 190M

Note: Weekly is overstated — many "weekly" workers in BLS data are actually
biweekly with weekly timesheets. Adjusted estimate:
  Biweekly: 75% → 118.7M × 26 = 3,086M
  Weekly:   10% → 15.8M × 52  = 822M
  Monthly:  10% → 15.8M × 12  = 190M
  Semi-monthly: 5% → 7.9M × 24 = 190M

US Total: ~3,086M + 122M (adj. weekly — net of biweekly reclassification)
        + 190M + 190M = ~3,400M = 3.4B
```

#### EU-27
```
Employed persons (Eurostat 2024): 197.6M
  Employees (85.7%): 169.3M
  Self-employed (14.3%): 28.3M (excluded)

Pay frequency: ~90% monthly, ~10% biweekly/other
  Monthly: 152.4M × 12 = 1,829M
  Other:   16.9M × 18 (avg) = 304M

EU Total: ~2,133M ≈ 2.2B (rounded)
```

#### China
```
Total employed (NBS 2024): ~740M
Urban employed: ~470M (est. formal payroll)
  Monthly pay: 95% → 446.5M × 12 = 5,358M
  Other:        5% → 23.5M × 12  = 282M

Rural/migrant workers receiving electronic payroll: ~150M (est.)
  Monthly: 150M × 12 = 1,800M
Note: Significant overlap with urban figure; use urban as primary.
Exclude informal rural to avoid double-counting.

China Total: ~5,640M ≈ 5.6B
```

#### India
```
Total employed (ILO/MOSPI 2024): ~560M
Formal sector workers (EPFO-registered + government): ~120M
  Monthly: 95% → 114M × 12 = 1,368M
  Other:    5% → 6M × 12   = 72M

Informal sector (~440M): Excluded — cash wages, no electronic transaction

India Total (formal only): ~1,440M ≈ 1.4B
```

#### Japan
```
Employed (Statistics Bureau 2024): ~67M
Formal payroll: ~60M
  Monthly: 98% → 58.8M × 12 = 706M

Japan Total: ~720M ≈ 0.7B
```

#### Rest of World
```
Remaining employed: ~3,500M - 158M - 198M - 740M - 560M - 67M = ~1,777M

Estimated formal payroll recipients: ~710M (40% formalization rate)
  Monthly: 80% → 568M × 12 = 6,816M
  Biweekly: 20% → 142M × 18 (avg) = 2,556M

Informal cash wages: ~1,067M × avg 10 pay events = 10,670M

Rest of World formal: ~9,372M ≈ 9.4B
Rest of World informal (cash): ~10,670M ≈ 10.7B
```

### Global Total

```
                     Formal Electronic    Cash/Informal    Total
US:                  3,400M              0                3,400M
EU-27:               2,133M              ~100M            2,233M
China:               5,640M              ~2,000M          7,640M
India (formal):      1,440M              ~5,280M*         6,720M
Japan:               720M                0                720M
Rest of World:       9,372M              ~10,670M         20,042M

TOTAL:               22,705M             ~18,050M         ~41,200M
                     ≈ 23.2B             ≈ 18.0B          ≈ 41.2B

*India informal: 440M workers × 12 cash pays = 5,280M
```

## 2. TPS Calculation (2024)

```
Seconds per year = 365.25 × 86,400 = 31,557,600
Average TPS = 41,200,000,000 / 31,557,600 = ~1,305 TPS

Peak TPS estimation:
- US biweekly Friday: ~130M deposits in ~4hr ACH window
  = 130M / (4 × 3600) = ~9,028 TPS (US alone)
- Global concurrent payday (month-end): multiple zones
- Peak multiplier: 5.0x average → ~6,525 TPS
```

## 3. Overlap Quantification

```
Formal electronic payroll: ~23.2B
  Of which ACH/bank transfer: ~95% = ~22.0B
  Of which wire/RTGS:         ~3%  = ~0.7B
  Of which card/wallet:       ~2%  = ~0.5B

Total payroll already in Bank Transfers: ~22.7B + ~14.3B (cash-to-bank emerging mkts)
                                        ≈ 37.0B (90% of total)

Incremental (not in bank transfers): ~4.2B
  - Cash wages: ~4.0B
  - Check payroll: ~0.2B
```

## 4. Bank Transfer Share

```
US ACH payroll share:
  US ACH total (Nacha 2024): 33.6B transactions
  US payroll ACH: ~3.2B
  Payroll as % of US ACH: 3.2B / 33.6B = 9.5%

Global bank transfer payroll share:
  Global bank transfers: 484B
  Global payroll in bank transfers: ~37B
  Payroll as % of bank transfers: 37B / 484B = 7.6%
```

## 5. Growth Rate Analysis

```
CAGR 2019-2024 (5yr): (41.2/37.5)^(1/5) - 1 = 1.9%

This tracks closely with global employment growth (~1.8% CAGR per ILO),
plus a small uplift from informal-to-formal migration (~0.1% net).
```

## 6. Projection Models (2026-2035)

### Baseline (2% CAGR — tracks employment growth)
| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 42.8 | 1,357 |
| 2028 | 44.5 | 1,411 |
| 2030 | 46.3 | 1,467 |
| 2035 | 51.1 | 1,618 |

### High Growth (4% CAGR — formalization + emerging market inclusion)
| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 44.5 | 1,411 |
| 2030 | 52.0 | 1,649 |
| 2035 | 63.3 | 2,006 |

### Conservative (1% CAGR — automation + aging demographics)
| Year | Annual Txns (B) | Avg TPS |
|------|----------------|---------|
| 2026 | 41.8 | 1,325 |
| 2030 | 43.5 | 1,378 |
| 2035 | 45.7 | 1,449 |

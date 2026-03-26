# Tax & Government Payments — Calculations & Derivations

> All math shown step-by-step. Every input is tagged with source and confidence.

---

## 1. Annual Transaction Estimate

### 1a. Income Tax Payments (Personal + Corporate)

**Approach:** Estimate number of formal taxpayers globally x average filing frequency.

```
OECD countries: ~600M individual tax returns/year (estimated)
  - US: 161M returns (IRS 2024) — High confidence
  - EU: ~200M estimated across 27 member states
  - Japan: ~25M
  - Other OECD: ~60M
  - Corporate returns across OECD: ~50M estimated

Non-OECD countries: ~2.5B additional taxpayers (India ~100M ITR filers,
  China ~variable due to employer withholding, Brazil ~40M, etc.)
  Estimated formal filings: ~400M

Sub-total income tax: ~1B formal filing transactions
  + quarterly/monthly instalment payments: ~2B additional
Total income tax transactions: ~3B/year
```

**Confidence:** :red_circle: Low — assembled from fragments

### 1b. VAT/GST Remittances

**Approach:** Number of VAT-registered businesses x filing frequency.

```
Globally: ~175 countries have VAT/GST systems
Estimated VAT-registered businesses: ~300M worldwide
Average filing frequency: monthly (12x/year) in most jurisdictions,
  but many small businesses file quarterly (4x/year)

Weighted average: ~8 filings/year per registered business
Total VAT/GST remittance transactions: 300M × 8 = ~2.4B/year

Real-time digital reporting (India GST, EU ViDA) is increasing this
by fragmenting into per-invoice reporting — could add 2-3B by 2030.

Working figure: ~5B/year (including instalments and adjustments)
```

**Confidence:** :red_circle: Low

### 1c. Benefits Disbursements

**Approach:** Number of beneficiaries globally x payment frequency.

```
Social security/pension recipients:
  - US: 72M Social Security recipients × 12 months = 864M/year
  - EU: ~130M pension recipients × 12 = 1.56B/year
  - China: ~310M pension recipients × 12 = 3.72B/year
  - Japan: ~40M × 12 = 480M/year
  - India: ~300M recipients of various schemes × variable = ~2B/year
  - Rest of world: ~1B/year estimated

Unemployment benefits: ~50M recipients globally × avg 6 months = 300M/year
Welfare/assistance: ~500M recipients × variable = ~1B/year
Child/family benefits: ~200M recipients × 12 = 2.4B/year

Sub-total: ~12-13B transactions/year
Working figure: ~12B/year
```

**Confidence:** :red_circle: Low — wide error bars

### 1d. Customs & Excise

```
Global trade: ~25B customs declarations/year (WTO estimates ~50M
  shipments/day, but many are consolidated)
Duty payment transactions: ~2B/year
Excise payments: included in VAT estimates above

Working figure: ~2B/year
```

### 1e. Other Government Payments

```
Fines, fees, licences, permits, property tax:
Estimated: ~3B/year globally
```

### Total

```
Income tax:        ~3B
VAT/GST:           ~5B
Benefits:         ~12B
Customs/excise:    ~2B
Other:             ~3B
─────────────────────
Total:            ~25B transactions/year
```

**Confidence:** :red_circle: Low — this is an order-of-magnitude estimate

---

## 2. Average TPS Calculation

```
Seconds in a year = 365 × 86,400 = 31,536,000

Average TPS = 25 × 10⁹ / 31,536,000
            = 25,000,000,000 / 31,536,000
            = ~793 TPS
```

**Result: ~790 TPS average** :red_circle: Low

---

## 3. Peak TPS Estimation

Government payments are extremely bursty:

```
US Tax Day (April 15):
  - ~30M returns filed in final 2 weeks
  - Peak day: ~5M returns/filings
  - Peak TPS: 5M / 86,400 = ~58 TPS (US only, tax filings only)

US Social Security payment day (e.g., 2nd Wednesday):
  - ~24M payments in one day
  - Peak TPS: 24M / 86,400 = ~278 TPS

Combining all countries' tax deadlines and benefits payment days:
  Estimated global peak: ~5,000-10,000 TPS
  (Multiple countries' deadlines can overlap; benefits are distributed
   across different days reducing true simultaneous peak)
```

**Confidence:** :red_circle: Low

---

## 4. Projection Models

### Baseline Growth Rates

```
Transaction count CAGR: 3.5%
  Based on: population growth (1%) + formalisation (1.5%) +
  digitalisation splitting transactions (1%)

Year  | Annual Volume (B) | Avg TPS
2024  |  25.0             |  793
2026  |  26.8             |  850
2028  |  28.7             |  910
2030  |  31.5             | 1,000
2035  |  37.8             | 1,199
```

### High Growth (Digitalisation Accelerates)

```
Transaction count CAGR: 8%
  Driven by real-time tax reporting, UBI expansion, formalisation

Year  | Annual Volume (B) | Avg TPS
2026  |  28.4             |  900
2028  |  34.7             | 1,100
2030  |  44.2             | 1,401
2035  |  78.8             | 2,499
```

### Conservative

```
Transaction count CAGR: 1.5%
  Flat tax frequency, slow benefits growth

Year  | Annual Volume (B) | Avg TPS
2026  |  25.5             |  808
2028  |  26.5             |  840
2030  |  27.4             |  869
2035  |  30.0             |  951
```

---

## 5. Annual Value Estimation

```
Global GDP 2024: ~$110 trillion (IMF WEO)
Average govt spending: ~35% of GDP = ~$38.5T
  (Range: 18% Mexico to 56% France)

Of this, direct citizen-facing payments:
  - Tax collection (revenue): ~$18T (OECD avg tax-to-GDP 34.1%)
  - Benefits disbursements: ~$12-15T
  - Net citizen-facing flows: ~$25-30T

Note: Government revenue and expenditure are separate flows.
Total two-way government payment value: ~$25-30T
```

**Confidence:** :yellow_circle: Medium (GDP and tax ratios are well-sourced)

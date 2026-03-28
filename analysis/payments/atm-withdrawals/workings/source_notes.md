# ATM Withdrawals — Source Notes

## Key Sources and Their Limitations

### 1. BIS CPMI Retail Payment Statistics (Red Book)
- **What it provides**: ATM transaction volumes and values for ~25 CPMI member countries, standardized definitions
- **What it lacks**: Non-CPMI countries (most of Africa, smaller Asian markets)
- **Reliability**: High for covered countries
- **Lag**: Typically 12-18 months behind current year
- **Key insight**: BIS February 2024 commentary noted global ATM withdrawals declining ~3% by count while value per withdrawal rises

### 2. ECB Payment Statistics
- **What it provides**: Semi-annual ATM transaction data for all eurozone countries. Number of ATMs, withdrawal counts, values.
- **What it lacks**: Non-euro EU countries (Sweden, Denmark, Poland) reported separately
- **Reliability**: Very high — regulatory reporting requirement
- **Frequency**: Semi-annual (H1 2024 and H2 2024 both available)
- **Key data**: EU ATM count: 265,624 (end H2 2023), declining 0.4% annually

### 3. Federal Reserve Payments Study
- **What it provides**: Detailed US ATM withdrawal transaction counts and values
- **What it lacks**: Only published triennially — latest detailed data is 2021
- **Reliability**: Very high for the year it covers
- **Key data**: US ATM cash withdrawals declined from 5.1B (2018) to 3.7B (2021), -10.1% CAGR. Average withdrawal rose from $156 to $198.
- **Gap**: No 2024 data; must extrapolate

### 4. RBI ATM Statistics
- **What it provides**: Monthly ATM transaction counts by bank, region, and ATM type
- **What it lacks**: Clean annual totals (must aggregate monthly data)
- **Reliability**: High — regulatory reporting
- **Key data**: January 2025: 48.83 crore cash withdrawals (~489M/month). Declining from 57 crore in Jan 2023.

### 5. ATMIA
- **What it provides**: Industry-level statistics, installed base counts, operational benchmarks
- **What it lacks**: Detailed transaction volume data by region (proprietary reports)
- **Reliability**: Medium — industry association data, may have advocacy bias
- **Key data**: $157 average withdrawal, declining transactions per ATM, rising operational costs

### 6. Datos Insights (formerly RBR)
- **What it provides**: Global ATM market forecasts, installed base tracking, regional deployment trends
- **What it lacks**: Free data is limited; detailed reports are paywalled
- **Reliability**: Medium-high — independent research firm
- **Key insight**: Advanced terminals and emerging markets reshaping ATM landscape; Asia-Pacific decline driven by China

### 7. Sci-Tech Today / Electroiq ATM Statistics
- **What it provides**: Aggregated ATM statistics from multiple sources (86.7B total transactions, 3.22M ATMs)
- **What it lacks**: Primary source attribution is sometimes unclear
- **Reliability**: Medium — aggregator, useful for cross-checking
- **Key data**: Global ATM transactions totaled 86.7B (all types); 3.22M ATMs worldwide in 2024

## Data Gaps

| Gap | Impact | Mitigation |
|-----|--------|-----------|
| No single global ATM withdrawal count published | Must aggregate from regional sources | Top-down (86.7B × 57%) and bottom-up regional model converge at ~49B |
| US data is 3 years old (2021) | US estimate requires extrapolation | Moderate decline rate from -10.1% to -6% for 2021-2024 |
| China PBOC does not separate ATM withdrawals | Must estimate from ATM counts × per-ATM rates | Cross-check with Datos/BIS China data |
| African and SE Asian ATM data is sparse | Undercount possible for emerging markets | Used residual approach after accounting for major markets |
| Withdrawal vs. non-withdrawal split varies by source | 57-69% range creates uncertainty | Used 57% (conservative) for top-down; validated with bottom-up |

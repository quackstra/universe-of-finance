# Payroll Payments — Source Notes

## Key Sources and Their Limitations

### 1. ILO World Employment and Social Outlook (WESO)
- **What it provides**: Global and regional employment counts, formal/informal splits, employment-to-population ratios
- **What it lacks**: Pay frequency data, transaction counts, electronic vs. cash payment channel data
- **Reliability**: High for employment headcounts (based on national labor force surveys); medium for informal economy estimates
- **Last updated**: May 2024 (covers 2023 data with 2024 projections)

### 2. BLS Current Employment Statistics (CES)
- **What it provides**: US nonfarm payroll employment by industry, monthly
- **What it lacks**: Pay frequency distribution (must be sourced from American Payroll Association surveys)
- **Reliability**: Very high — gold standard for US employment data
- **Frequency**: Monthly

### 3. Eurostat Employment Statistics
- **What it provides**: EU-27 and member-state employment, employee vs. self-employed split
- **What it lacks**: Payroll transaction counts; pay frequency assumed from labor law norms
- **Reliability**: High
- **Note**: 2024 data shows 197.6M employed aged 20-64 at 75.8% employment rate — highest on record

### 4. ADP Global Payroll Survey 2024
- **What it provides**: Payroll industry trends, automation rates, pain points
- **What it lacks**: Total transaction volumes — ADP does not publish aggregate paycheck counts
- **Reliability**: Medium (survey-based, N=1,600 organizations)
- **Key stat**: ADP processes payroll for ~26M US workers per pay period

### 5. Nacha ACH Statistics
- **What it provides**: Total US ACH transaction volume and value, including payroll Direct Deposit share
- **What it lacks**: Granular payroll-specific breakdown (payroll is a subset of "Direct Deposit")
- **Reliability**: Very high — administrative data from the ACH network operator
- **2024 data**: 33.6B total ACH transactions, $86.2T value

### 6. NBS China / MOSPI India
- **What it provides**: National employment figures
- **What it lacks**: Payment channel data for payroll; formal/informal boundary is fuzzy in both countries
- **Reliability**: Medium — China data has well-known issues with classification of migrant workers; India EPFO data is reliable but covers only formal sector

## Data Gaps

| Gap | Impact | Mitigation |
|-----|--------|-----------|
| No global payroll transaction count exists | Entire estimate is model-derived | Cross-check: US ACH payroll share (9.5%) × global bank transfers should approximate |
| Pay frequency data is sparse outside US | Regional assumptions may be wrong | Used labor law norms + APA/CloudPay industry reports |
| Informal economy size is uncertain | Could be ±30% on cash wage estimate | Used ILO central estimate; flagged as low confidence |
| Gig economy boundary unclear | Growing grey area between payroll and P2P | Excluded; noted as open question |
| No peak TPS data for payroll processing | Peak multiplier is estimated | Used US ACH window mechanics as calibration |

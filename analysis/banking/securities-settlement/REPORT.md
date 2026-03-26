# Securities Settlement — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

**Category**: Banking > Securities Settlement
**Data Year**: 2024
**Last Updated**: 2026-03-26

---

## Executive Summary

Global securities settlement infrastructure processed an estimated **1.3–1.5 billion settlement transactions** in 2024, averaging **~41–48 TPS** (calendar), with a combined settled value of approximately **$3.7 quadrillion** (DTCC alone). The three pillars — DTCC (US), Euroclear (international/Belgium), and Clearstream (Germany/Luxembourg) — handle the post-trade processing for virtually all exchange-traded equities, bonds, and structured products in the developed world.

The defining event of 2024 was the **US move to T+1 settlement** (28 May 2024), compressing the settlement cycle from two business days to one. This increased operational intensity without necessarily changing annual transaction counts, but the infrastructure proved capable: NSCC processed a record peak of 545 million transactions in a single day in April 2025. Euroclear reached record settlement volumes with 331 million netted transactions for the full year.

**Critical taxonomy note**: Securities settlement is DOWNSTREAM of trading. Every equity trade, bond trade, or derivative exercise ultimately flows through settlement infrastructure. This capsule counts settlement-layer transactions only — it does not double-count the upstream trading activity covered in the equity-markets and ETD capsules.

---

## Scope

**Included:**
- DTCC subsidiaries: DTC (depository/settlement), NSCC (equities/corporate bonds clearing), FICC (government securities/MBS clearing)
- Euroclear group: Euroclear Bank (ICSD), Euroclear Belgium, France, Finland, Netherlands, Sweden, UK (CRESTCo)
- Clearstream: International CSD (ICSD), domestic CSD (Germany)
- TARGET2-Securities (T2S) — Eurosystem securities settlement platform
- CCP clearing that results in settlement (counted at the settlement leg)

**Excluded:**
- Trading/execution layer (covered in equity-markets, ETD capsules)
- Cash legs of DVP settlement (counted in interbank-rtgs capsule)
- OTC derivative clearing (covered in ETD/OTC derivatives capsule)
- Custody/safekeeping (asset servicing, not transaction processing)

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS (calendar) | ~41–48 | Calculated: 1.3–1.5B / 31.56M sec | 🟡 Medium |
| Peak TPS (est.) | ~6,300 | NSCC 545M peak day / 86,400 sec | 🟡 Medium |
| Daily volume (avg) | ~5.2–6.0M | Sum of system daily averages | 🟡 Medium |
| Annual volume (2024) | ~1.3–1.5B transactions | Aggregated from system reports | 🟡 Medium |
| Annual value (2024) | >$3.7 quadrillion | DTCC alone = $3.7Q; Euroclear adds €1,162T | 🟡 Medium |

**Note on TPS**: Securities settlement is batch-oriented during market hours. Unlike RTGS (continuous flow), settlement systems process in cycles. NSCC's Continuous Net Settlement (CNS) system nets throughout the day, with final settlement occurring end-of-day. The calendar TPS is a smoothed average; actual processing is bursty.

### System-by-System Breakdown

| System | Annual Volume (est.) | Annual Value | Avg Daily Txns | Assets Under Custody | Source | Confidence |
|--------|---------------------|-------------|----------------|---------------------|--------|------------|
| **DTCC** (DTC+NSCC+FICC) | ~500M+ | $3.7 quadrillion | ~1.3M (DTC alone) | $99T | [DTCC 2024 Annual Report](https://www.dtcc.com/annuals/2024/letters/cfo/) | 🟡 Medium |
| **Euroclear** (group) | ~331M | €1,162T (~$1,267T) | ~1.3M | >€40T | [Euroclear 2024 Results](https://www.euroclear.com/newsandinsights/en/press/2025/mr-05-euroclear-delivers-strong-results-in-2024.html) | 🟢 High |
| **Clearstream** (ICSD+CSD) | ~200M (est.) | €15T+ (est.) | ~800K (est.) | €17T+ | [Clearstream](https://www.clearstream.com/clearstream-en/about-clearstream) | 🟡 Medium |
| **T2S** (Eurosystem) | ~165M (est.) | €180T+ (est.) | ~660K | N/A | [ECB TARGET Services](https://www.ecb.europa.eu/press/targetservar/html/ecb.targetservar2024.en.html) | 🟡 Medium |

**DTCC detail**:
- DTC: Handles ~1.3 million delivery transactions per day. The money associated with these movements is accomplished through ~70 transfers via the Federal Reserve's National Settlement Service (NSS) each day.
- NSCC: Clears virtually all US broker-to-broker equity, corporate bond, and UIT transactions. Peak day record: 545M transactions (7 April 2025), up 33% from the prior record of 409M during the January 2021 meme stock event.
- FICC: Government Securities Division (GSD) clears US Treasury and agency debt. Mortgage-Backed Securities Division handles MBS settlement.
- ATP (Automated Trade Processing): Handles >350M transactions annually valued at >$142T.

**Euroclear detail**:
- 331 million netted transactions processed in 2024 (full year), valued at €1,162 trillion
- First 9 months of 2024: 243M transactions, €850T (up 5% YoY)
- Assets under custody exceeded €40 trillion for the first time
- Settlement volumes hit a new all-time high

**Clearstream detail**:
- Year-to-date through May 2024: ICSD 8.0M transactions, CSD 71.7M transactions, IFS 18.4M transactions (total: ~98.1M in 5 months)
- Annualized: ~235M transactions (though H2 may differ)
- Settlement instructions volume increased 25% in 2024; failed instructions declined 14%

**T2S detail**:
- Volumes peaked in 2024, up 14% from previous year, rebounding from two consecutive years of decline
- Part of the consolidated T2-T2S platform since March 2023

---

## Historic Trend

### DTCC Annual Settled Value ($ quadrillions)

| Year | Settled Value ($Q) | Revenue ($B) | Notes |
|------|-------------------|-------------|-------|
| 2019 | ~2.0 | 1.86 | Pre-pandemic baseline |
| 2020 | ~2.3 | 1.94 | COVID volatility spike |
| 2021 | ~2.5 | 2.02 | Meme stocks, record retail participation |
| 2022 | ~2.5 | 2.12 | Rate hiking cycle begins |
| 2023 | ~3.0 | 2.25 | Market recovery |
| 2024 | ~3.7 | 2.49 | T+1 transition, strong equity markets |

Source: [DTCC Annual Reports](https://www.dtcc.com/about/annual-report), [Wikipedia](https://en.wikipedia.org/wiki/Depository_Trust_%26_Clearing_Corporation)

### Euroclear Annual Transaction Volume (millions)

| Year | Transactions (M) | Value (€T) | Assets Under Custody (€T) |
|------|------------------|-----------|--------------------------|
| 2019 | ~250 | ~800 | ~31 |
| 2020 | ~265 | ~850 | ~33 |
| 2021 | ~280 | ~950 | ~37 |
| 2022 | ~290 | ~1,000 | ~35 |
| 2023 | ~310 | ~1,100 | ~37 |
| 2024 | 331 | 1,162 | >40 |

Source: [Euroclear Annual Results](https://www.euroclear.com/newsandinsights/en/press/2025/mr-05-euroclear-delivers-strong-results-in-2024.html)

Note: Pre-2024 Euroclear transaction volumes are estimates based on growth rate trends. The 2024 figure of 331M is confirmed.

---

## Growth Rate Analysis

| System | 5-Year CAGR (Volume) | 5-Year CAGR (Value) | Key Driver |
|--------|---------------------|--------------------|----|
| DTCC | ~6% (value) | ~13% (value) | T+1 transition, strong equity markets, record volumes |
| Euroclear | ~5.8% | ~7.7% | European market integration, T2S adoption |
| Clearstream | ~4% (est.) | ~5% (est.) | CSDR efficiency improvements |
| T2S | ~3% (est.) | ~4% (est.) | Gradual migration of European CSDs |

**Composite securities settlement 5-year volume CAGR**: ~5%
**Composite securities settlement 5-year value CAGR**: ~10%

The value CAGR significantly exceeds volume CAGR because:
1. Rising equity prices increase the notional value of each settlement
2. Government debt issuance has surged globally (higher fixed-income settlement values)
3. T+1 settlement doesn't change annual counts but concentrates activity

---

## Projections (through 2035)

### Baseline Scenario (5% volume CAGR, 8% value CAGR)

| Year | Annual Volume (B) | Avg TPS (calendar) | Annual Value ($Q) |
|------|-------------------|--------------------|--------------------|
| 2025 | 1.47 | 46.6 | 4.0 |
| 2026 | 1.54 | 48.8 | 4.3 |
| 2028 | 1.70 | 53.9 | 5.0 |
| 2030 | 1.87 | 59.3 | 5.9 |
| 2035 | 2.39 | 75.8 | 8.7 |

### High-Growth Scenario (8% volume CAGR)
Driven by: T+0/atomic settlement adoption, tokenized securities growth, emerging market CSD expansion, fractional share settlement.

| Year | Annual Volume (B) | Avg TPS (calendar) |
|------|-------------------|--------------------|
| 2030 | 2.06 | 65.3 |
| 2035 | 3.03 | 96.1 |

### Conservative Scenario (3% volume CAGR)
Driven by: Netting efficiency improvements reduce gross settlement counts, consolidation of European CSDs.

| Year | Annual Volume (B) | Avg TPS (calendar) |
|------|-------------------|--------------------|
| 2030 | 1.67 | 52.9 |
| 2035 | 1.93 | 61.2 |

---

## Key Findings

1. **$3.7 quadrillion processed by DTCC alone**: This is the largest single-institution value figure in global finance. DTCC's subsidiaries collectively process more value than any other financial market infrastructure.

2. **T+1 proved the plumbing works**: The US moved to T+1 on 28 May 2024 with no systemic issues. CLS settlement values increased post-T+1. Europe is evaluating a similar move (potentially 2027). The UK has signaled interest. T+0 (same-day or atomic settlement) remains a longer-term aspiration.

3. **NSCC peak capacity is extraordinary**: The 545M single-day record (April 2025) demonstrates that US clearing infrastructure can handle extreme stress events. This is >1,000x the daily average, showing massive headroom.

4. **Euroclear hit record highs across the board**: 331M transactions, €1,162T settled value, >€40T in custody — all records. European settlement infrastructure is scaling steadily.

5. **Settlement is downstream of trading**: Every equity trade, bond trade, and derivative exercise flows through these systems. The 1.3–1.5B settlement transactions are a compressed/netted version of the ~10B+ trades executed globally. Netting ratios typically run 5:1 to 10:1.

6. **Double-counting boundary**: The cash leg of DVP (delivery-versus-payment) settlement flows through RTGS systems and is counted in the interbank-rtgs capsule. This capsule counts the securities delivery leg only. There is inherent overlap in value terms — a $1M equity settlement appears as both a securities delivery (here) and a cash payment (RTGS).

---

## Data Quality & Limitations

- **DTCC**: Medium-high confidence on value ($3.7Q), lower confidence on transaction counts. DTCC publishes value data prominently but detailed transaction count breakdowns (by subsidiary, by asset class) require consulting CPMI-IOSCO quarterly disclosures.
- **Euroclear**: High confidence. Clear reporting of 331M transactions and €1,162T in 2024 press releases.
- **Clearstream**: Medium confidence. Monthly statistics published but complete annual totals require aggregation. Year-to-date figures through May 2024 extrapolated.
- **T2S**: Medium confidence. ECB reports growth rates (up 14% in 2024) but absolute transaction counts for T2S specifically are embedded in the broader TARGET Services reporting.
- **Overlap risk**: Euroclear and Clearstream both settle through T2S for euro-denominated securities. Some transactions may be counted by both the ICSD and T2S. We attempt to avoid double-counting by using netted transaction figures where available.
- **DTCC transaction count gap**: The biggest data limitation. We know DTCC processes >1.3M DTC deliveries/day and >350M ATP transactions/year, but the total annual settlement transaction count across all subsidiaries is not published as a single headline figure.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **DTCC total transaction count**: DTCC publishes value ($3.7Q) prominently but does not provide a single headline annual transaction count across all subsidiaries (DTC + NSCC + FICC + ATP). We estimate ~500M+ but this is assembled from partial disclosures.
- **CSD consolidation impact**: European CSDs are gradually consolidating onto T2S. How much of the apparent growth in T2S volumes is migration (from national CSDs) vs genuine new activity?
- **T+1 impact on fail rates**: The US moved to T+1 in May 2024; early data suggests fail rates initially spiked then normalised. The steady-state impact on settlement efficiency and transaction counts is still emerging.
- **Asian CSD volumes**: Japan (JASDEC), China (CSDC/CCDC), and India (NSDL/CDSL) are major settlement systems not covered in our estimates. Including them could add 500M-1B+ settlement transactions.
- **DLT settlement pilot volumes**: HKMA's Project Ensemble, BIS Project mBridge, and other DLT settlement pilots are live but volumes are not consistently reported.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| DTCC transaction count | Cross-reference: DTC daily deliveries (1.3M) x 250 days = 325M; add NSCC/FICC/ATP partial data | DTCC annual report, CPMI-IOSCO disclosures | :yellow_circle: |
| Asian CSD volumes (China CSDC) | China equity market daily turnover (~$100-150B/day) / avg trade size; apply netting ratio | Shanghai/Shenzhen exchange published trading data | :yellow_circle: |
| Asian CSD volumes (India NSDL/CDSL) | SEBI publishes depository statistics; CDSL processes ~80% of Indian equity settlements | SEBI Annual Report, CDSL monthly bulletins | :green_circle: |
| T+1 fail rate impact | DTCC/SIFMA T+1 After Action Report; compare pre/post fail rates; model steady-state volume impact | SIFMA T+1 report (published); DTCC settlement data | :green_circle: |
| CSD consolidation trend | Track number of CSDs on T2S over time (currently ~20); model remaining national CSD migration dates | ECB T2S participation list; CSDR implementation timeline | :yellow_circle: |
| DLT settlement pilot scale | BIS Innovation Hub reports; HKMA Ensemble disclosures; SIX Digital Exchange published volumes | BIS Annual Report, individual pilot disclosures | :red_circle: |

### Key Modeling Questions
- If Asian CSDs (China, Japan, India, Korea) were included, does global securities settlement volume reach 2.5-3.0 billion transactions? This would significantly change the TPS picture.
- What is the netting ratio trend? If NSCC netting becomes more efficient (currently ~5:1 to 10:1 trade-to-settlement), settlement transaction counts could decline even as trading volumes increase. Conversely, T+0/atomic settlement would eliminate netting, potentially multiplying settlement counts by 5-10x.
- How will tokenised securities (see RWA capsule) interact with traditional settlement? Will tokenised settlement be additive or substitutive?
- NSCC's 545M single-day peak vs ~2M daily average implies >250x headroom. Is this architecture genuine capacity or theoretical burst?

### Reference Comparisons
- **Trade-to-settlement ratio**: Comparing exchange-reported trade counts (~10B+ globally) to settlement counts (1.3-1.5B) gives a ~7:1 netting ratio. Monitoring this ratio over time reveals whether settlement is becoming more or less efficient.
- **BIS CPMI-IOSCO PFMI disclosures**: All systemically important CCPs and CSDs must publish quantitative disclosures quarterly. These are the most granular source for settlement transaction counts but are dispersed across individual institution websites.
- **Fractional share settlement**: The rise of fractional share trading (Robinhood, Trading 212) may increase settlement complexity without proportionally increasing settlement counts, as fractional positions are typically netted at the broker level before reaching DTCC.

---

## Sources

- [DTCC 2024 Annual Report](https://www.dtcc.com/annuals/2024/files/DTCC-Annual-Report-2024-Print.pdf)
- [DTCC Annual Report - CFO Letter](https://www.dtcc.com/annuals/2024/letters/cfo/)
- [DTCC Record Volumes (April 2025)](https://www.dtcc.com/news/2025/april/23/dtcc-processes-record-volumes-across-services-amid-market-volatility)
- [DTCC Wikipedia](https://en.wikipedia.org/wiki/Depository_Trust_%26_Clearing_Corporation)
- [Euroclear 2024 Results Press Release](https://www.euroclear.com/newsandinsights/en/press/2025/mr-05-euroclear-delivers-strong-results-in-2024.html)
- [Euroclear 2024 Annual Report](https://www.euroclear.com/newsandinsights/en/Format/Articles/euroclear-releases-2024-annual-reports.html)
- [Clearstream Settlement Efficiency 2024](https://www.clearstream.com/clearstream-en/newsroom/250131-4258778)
- [ECB TARGET Services Annual Report 2024](https://www.ecb.europa.eu/press/targetservar/html/ecb.targetservar2024.en.html)
- [SIFMA T+1 After Action Report](https://www.sifma.org/resources/guides-playbooks/t1-after-action-report)
- [DTCC $3.7 Quadrillion / Canton Network](https://finance.yahoo.com/news/dtcc-handles-3-7-quadrillion-162255289.html)
- [BIS CPMI Payment Statistics](https://www.bis.org/statistics/dataportal/payment_stats.htm)

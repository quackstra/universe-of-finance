# Tax & Government Payments — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Global government payment flows — encompassing tax collection, VAT/GST remittances, customs duties, and benefits disbursements — represent an estimated **~25 billion discrete payment transactions per year**, equivalent to roughly **~790 TPS** on average. While these flows are **massive by value** (an estimated **$25-30 trillion annually** across all levels of government worldwide), they are characterised by relatively low transaction frequency compared to consumer payment categories. The defining feature of government payments is extreme **seasonality**: tax filing deadlines create enormous spikes (the US IRS processes ~160 million returns, mostly within a 3-month window), while benefits disbursements follow rigid monthly cycles.

## Scope

This analysis covers four major subcategories of government-to-citizen and citizen-to-government payment flows:

1. **Income tax payments** — personal and corporate tax filings and remittances
2. **VAT/GST remittances** — consumption tax payments from businesses to governments
3. **Customs duties and excise** — trade-related government collections
4. **Benefits disbursements** — social security, welfare, pensions, unemployment, and other government-to-citizen transfers

Excluded: government procurement (B2G contracts), inter-governmental transfers, central bank operations, government bond issuance/redemption (covered in traditional finance).

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Avg TPS | ~790 | Derived from ~25B annual ([calculations](workings/calculations.md#1-annual-transaction-estimate)) | :red_circle: Low |
| Peak TPS (est.) | ~5,000-10,000 | Tax deadline spikes; benefits payment days | :red_circle: Low |
| Daily volume (avg) | ~68 million | Derived from annual total | :red_circle: Low |
| Annual volume (est.) | ~25 billion | Aggregated estimate ([calculations](workings/calculations.md#1-annual-transaction-estimate)) | :red_circle: Low |
| Annual value (est.) | ~$25-30 trillion | Global govt expenditure ~35% of $110T global GDP | :yellow_circle: Medium |
| Avg transaction value | ~$1,000-1,200 | Highly variable — taxes are large, benefits are moderate | :red_circle: Low |

### Subcategory Breakdown

| Subcategory | Est. Annual Txns (B) | Share | Avg Value | Confidence |
|-------------|---------------------|-------|-----------|------------|
| Benefits disbursements | ~12 | ~48% | ~$500-800 | :red_circle: Low |
| Income tax payments | ~3 | ~12% | ~$3,000-5,000 | :red_circle: Low |
| VAT/GST remittances | ~5 | ~20% | ~$1,500-3,000 | :red_circle: Low |
| Customs & excise | ~2 | ~8% | ~$2,000-5,000 | :red_circle: Low |
| Other govt payments | ~3 | ~12% | Variable | :red_circle: Low |

### Regional Breakdown

| Region | Share (by value) | Notes |
|--------|-----------------|-------|
| Europe | ~35% | High tax-to-GDP ratios (avg 34-45%), extensive welfare states |
| North America | ~25% | US alone: 161M individual returns, 72M Social Security recipients |
| Asia-Pacific | ~25% | China/India growing fast; lower tax-to-GDP but massive populations |
| Rest of World | ~15% | Significant informal economy reduces formal transaction counts |

---

## Historic Trend

### Government Revenue as % of GDP (OECD Average)

| Year | Tax-to-GDP (OECD avg) | Direction | Confidence |
|------|----------------------|-----------|------------|
| 2000 | 33.9% | — | :green_circle: High |
| 2005 | 33.4% | Down | :green_circle: High |
| 2010 | 32.0% | Down (GFC aftermath) | :green_circle: High |
| 2015 | 33.3% | Recovery | :green_circle: High |
| 2019 | 33.4% | Stable | :green_circle: High |
| 2020 | 33.5% | Slight increase (GDP fell faster than tax) | :green_circle: High |
| 2021 | 34.0% | Recovery | :green_circle: High |
| 2022 | 33.9% | Stable | :green_circle: High |
| 2023 | 33.8% | Stable | :green_circle: High |
| 2024 | 34.1% | Record high | :green_circle: High |

*Source: [OECD Revenue Statistics 2025](https://www.oecd.org/en/publications/2025/12/revenue-statistics-2025_07ca0a8e.html)*

**Key observations:**
- OECD tax-to-GDP reached a **record 34.1%** in 2024, driven by labour tax increases
- 33 out of 36 OECD countries saw nominal tax revenue increases in 2024
- The range is enormous: Mexico at 18.3% to Denmark at 45.2%
- Digitalisation of tax administration (e-filing, real-time reporting) is steadily increasing the formal transaction count even where underlying economic activity is flat

---

## Growth Rate Analysis

| Period | CAGR (Nominal Revenue) | Context |
|--------|----------------------|---------|
| 2015-2024 | ~4-5% | Slightly above GDP growth as tax bases broaden |
| Transaction count growth | ~3-4% | Driven by e-filing mandates, VAT digitalisation |
| Benefits disbursement growth | ~5-6% | Ageing populations expanding pension/healthcare rolls |

Government payment transaction counts grow more slowly than consumer payments because:
1. Tax payments are consolidated (one return per person/entity per year)
2. Benefits are monthly, not daily
3. Growth comes from population increase and formalisation, not frequency increase

---

## Projections

### Baseline (Steady State)

**Assumptions:**
1. Global GDP grows 2.5-3% annually; government spending maintains ~35% share
2. Digitalisation continues — real-time VAT reporting expands from EU to more jurisdictions
3. Benefits rolls grow 2-3% annually as populations age
4. No major tax reform changes transaction frequency

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 850 | 26.8 |
| 2028 | 920 | 29.0 |
| 2030 | 1,000 | 31.5 |
| 2035 | 1,200 | 37.8 |

### High Growth (Digitalisation Accelerates)

**Assumptions:**
1. Real-time digital tax reporting becomes global standard (fragmented payments replace annual lump sums)
2. Universal Basic Income pilots expand — adding 500M+ new monthly disbursement recipients by 2035
3. India, Africa formalise significantly — 1B+ new taxpayers enter formal system
4. Government payments move to instant payment rails (FedNow, Pix for govt)

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 900 | 28.4 |
| 2028 | 1,100 | 34.7 |
| 2030 | 1,400 | 44.2 |
| 2035 | 2,500 | 78.8 |

### Conservative (Status Quo)

**Assumptions:**
1. Tax transaction frequency stays flat — annual filing remains dominant
2. Benefits rolls grow slowly (1-2%) as retirement age increases offset ageing
3. Informal economy persists in developing nations
4. No major new disbursement programmes

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 810 | 25.5 |
| 2028 | 840 | 26.5 |
| 2030 | 870 | 27.4 |
| 2035 | 950 | 30.0 |

*Full projection tables: [workings/calculations.md](workings/calculations.md#4-projection-models)*

**2035 Range:** Government payments are projected to remain in the **950-2,500 TPS** range by 2035. The high-growth scenario depends heavily on structural changes (real-time tax, UBI) that would fundamentally alter transaction frequency.

---

## Key Findings

1. **Government payments are value-heavy, count-light.** At ~$25-30T annually, they rival consumer card payments in total value but process only ~1/30th the transaction count. The average government payment is 15-20x larger than the average card transaction.

2. **Extreme seasonality defines the category.** Tax deadlines create massive spikes — the US IRS processes the bulk of 161M returns in January-April. Benefits disbursements cluster on specific days (US Social Security pays on 2nd, 3rd, and 4th Wednesdays). Peak-to-average TPS ratios may exceed 10:1.

3. **Digitalisation is the primary growth driver for transaction counts.** Real-time VAT reporting (already live in parts of EU, Latin America, India) fragments what was one annual payment into monthly or even per-transaction reporting, multiplying formal transaction counts without changing underlying economic activity.

4. **Benefits disbursements are the high-count subcategory.** With ~72M US Social Security recipients alone receiving monthly payments, and similar programmes worldwide covering hundreds of millions, disbursements likely account for nearly half of all government payment transactions.

5. **The informal economy is the elephant in the room.** In developing nations, 30-60% of economic activity occurs outside formal tax systems. Formalisation could dramatically increase government payment transaction counts — India's GST rollout and Brazil's digital tax systems are early examples.

6. **Government payments are a lagging digitaliser.** While consumer payments digitised rapidly (contactless, mobile wallets), government payment systems are typically 5-10 years behind, still relying on batch processing, checks, and legacy infrastructure in many jurisdictions.

---

## Depth Research Update (Run 6, 2026-03-28)

> Full depth research: [workings/depth-research.md](workings/depth-research.md)

### Key Revisions

1. **US IRS Data Book FY2024 provides unprecedented detail**: 266M+ returns/forms processed, 4.6B information returns, $5.1T gross collections (first time >$5T), 219.9M e-filed. Derived US tax transaction count: ~680-690M/year (including employer withholding deposits).

2. **US benefits transactions derived from hard data**: 71M Social Security recipients x 12 = 852M; 42M SNAP x 12 = 504M; plus Medicare, unemployment, veterans, SSI = ~3.2B US benefits disbursements/year. Total US government payments: ~3.9B.

3. **India GSTN hard data**: 15.1M active GST registrations filing ~25 returns/year = ~362M GST filings. GSTR-3B compliance >95%. Combined with 7.4B+ DBT transactions, India government payments = ~8.7B/year.

4. **UK DWP**: Universal Credit recipients surged to 8.4M (Dec 2025), up from 7.36M a year earlier. Plus State Pension (12.5M) and other benefits. Total UK government payments: ~420-450M/year.

5. **Brazil Pix integration**: 63.4B total Pix transactions in 2024 (53% YoY growth), with government payments increasingly flowing through Pix rails. Brazil tax reform mandating Pix-to-invoice integration.

6. **Nacha ACH cross-validation**: 8.74B direct deposits in 2025 (includes payroll + Social Security + tax refunds). Government share (~30-35%) = 2.6-3.1B, consistent with the 3.9B US total from different methodology.

7. **Confidence revised from 50 to 60** (+10 points). The REPORT.md headline figure of ~25B is stale; the data.json bottom-up model of ~31.6B (now validated at ~32B) is the correct reference.

### Revised Current Metrics

| Metric | REPORT.md (stale) | data.json (validated) |
|--------|-------------------|----------------------|
| Annual transactions | ~25B | **~32B** (range: 28-38B) |
| Average TPS | ~790 | **~1,015** |

---

## Data Quality & Limitations

- **No single global dataset exists** for government payment transactions. This analysis is constructed from national statistics, OECD aggregate data, and estimation. Overall confidence is :red_circle: Low for transaction counts.
- **Value data is more reliable than count data.** Government expenditure as % of GDP is well-tracked by IMF/OECD/World Bank. Transaction counts are not systematically reported.
- **Definition ambiguity.** A "tax payment" could be one annual filing or thousands of withholding transactions by an employer. This analysis counts the citizen/entity-level transaction, not underlying employer withholdings.
- **Benefits disbursement counts** are estimated from recipient numbers x payment frequency. Actual disbursement transaction counts may differ due to batching, direct deposit consolidation, and multi-programme recipients.
- **Customs data** is particularly opaque — trade transaction counts depend on the granularity at which duties are assessed.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Most governments do not publish transaction counts.** Revenue and expenditure are well-tracked (IMF, OECD, World Bank), but the number of discrete payment transactions — tax payments received, benefit disbursements made — is rarely reported as a headline statistic.
- **Employer withholding granularity**: In most countries, employers remit income tax withholdings monthly or quarterly. Whether this counts as 1 transaction (per employer per period) or N transactions (per employee) varies by jurisdiction and is not standardised.
- **Developing country government payment volumes**: For ~100 countries (sub-Saharan Africa, parts of Asia, Central America), there is essentially no published data on government payment transaction counts.
- **Informal economy payments**: In countries where 30-60% of GDP is informal, the formal tax/benefits transaction count dramatically understates the true economic activity.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| US tax payment count | IRS: 161M individual returns + ~10M business returns + quarterly estimated payments (~40M) = ~250M tax payment transactions/year | IRS Filing Season Statistics (published weekly during season) | :green_circle: |
| US benefits disbursement count | 72M Social Security recipients x 12 payments + 42M SNAP recipients x 12 + 6M unemployment x ~6 months = ~1.5B/year | SSA Statistical Supplement; USDA SNAP data; DOL unemployment stats | :green_circle: |
| India JAM trinity as case study | India: 530M Jan Dhan accounts + 1.4B Aadhaar IDs + UPI integration. Track DBT (Direct Benefit Transfer) volume: 7.4B transactions in FY2023-24 (~$140B) | DBT Mission dashboard (public); RBI annual report | :green_circle: |
| EU VAT digitalisation impact | Real-time VAT reporting (ViDA proposal) fragments annual VAT payments into per-invoice reports. Estimate: ~100M EU businesses x 12 monthly filings = 1.2B vs ~100M annual filings today = 12x multiplier | European Commission ViDA impact assessment; Member state e-invoicing adoption data | :yellow_circle: |
| Government payroll as proxy | Global government employment ~90-100M (ILO estimate). At 12-26 pay periods/year = 1.1-2.6B payroll transactions | ILO government employment statistics; national civil service headcount data | :yellow_circle: |
| Developing country estimation | Take known tax-to-GDP ratio x GDP to get revenue. Divide by estimated average tax payment size ($500-2000 in developing countries) for transaction count. | OECD Revenue Statistics (36 countries); IMF GFS (180+ countries) | :red_circle: |

### Key Modeling Questions
- **Real-time VAT reporting is the biggest potential transaction multiplier.** The EU's ViDA (VAT in the Digital Age) proposal, if fully implemented, would require e-invoicing and real-time reporting across 27 member states. This could multiply EU government payment transactions by 5-10x without changing underlying economic activity. When will this take effect, and which countries will adopt it first?
- India's Direct Benefit Transfer programme processed 7.4 billion transactions in FY2023-24. If other large developing countries (Indonesia, Brazil, Nigeria) replicate India's JAM trinity model, how many additional government payment transactions would be created?
- What is the right level of granularity for "tax payment"? If every employer withholding remittance counts (rather than the consolidated monthly/quarterly payment), US tax transactions alone could increase from ~250M to ~2B+.
- How do check vs. electronic disbursement ratios affect transaction counts? The US Treasury still issues ~50M paper checks per year for government payments. As these convert to electronic, does the transaction count stay the same (format change) or increase (due to easier splitting)?

### Reference Comparisons
- **India as digitalisation benchmark**: India's DBT (Direct Benefit Transfer) programme is the world's most advanced government payment digitalisation effort. 7.4B DBT transactions in FY2023-24 across 313 schemes, touching ~800M beneficiaries. This provides a concrete case study for what happens when a large developing country digitises government payments.
- **US IRS as seasonal benchmark**: The IRS processes ~161M individual returns, with 80%+ filed January-April. This creates a predictable seasonal spike that can be used to calibrate peak-to-average ratios for government payment categories globally.
- **OECD tax-to-GDP as consistency check**: At a global average ~25% tax-to-GDP ratio and ~$110T global GDP, total tax revenue is ~$27.5T. At our estimated ~10B tax/VAT/customs transactions, the average tax transaction is ~$2,750 — plausible as a blend of small VAT remittances and large corporate tax payments.

---

## Sources

1. [OECD — Revenue Statistics 2025](https://www.oecd.org/en/publications/2025/12/revenue-statistics-2025_07ca0a8e.html)
2. [OECD — Tax Revenue Trends 1965-2024](https://www.oecd.org/en/publications/2025/12/revenue-statistics-2025_07ca0a8e/full-report/tax-revenue-trends-1965-2024_98c75833.html)
3. [OECD — Labour taxes drive revenues to record high in 2024](https://www.oecd.org/en/about/news/press-releases/2025/12/labour-taxes-drive-oecd-tax-revenues-to-record-high-in-2024.html)
4. [IMF — Government Expenditure % of GDP DataMapper](https://www.imf.org/external/datamapper/exp@FPP)
5. [IMF — Fiscal Monitor April 2024](https://www.imf.org/-/media/files/publications/fiscal-monitor/2024/april/english/ch1.pdf)
6. [US Social Security Administration — Annual Statistical Supplement 2024](https://www.ssa.gov/policy/docs/statcomps/supplement/2024/highlights.html)
7. [US Social Security Administration — Monthly Statistical Snapshot Feb 2026](https://www.ssa.gov/policy/docs/quickfacts/stat_snapshot/)
8. [US IRS — Filing Season Statistics](https://www.irs.gov/newsroom/filing-season-statistics-by-year)
9. [World Bank — Government Final Consumption Expenditure](https://data.worldbank.org/indicator/NE.CON.GOVT.CD)
10. [Our World in Data — Government Spending](https://ourworldindata.org/government-spending)
11. [Tax Foundation — OECD Tax Revenue by Country](https://taxfoundation.org/data/all/global/oecd-tax-revenue-by-country/)

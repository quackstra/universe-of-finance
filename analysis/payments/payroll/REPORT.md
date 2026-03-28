# Payroll Payments — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Global payroll — the disbursement of wages and salaries from employers to workers — generates an estimated **~41.2 billion transactions annually** in 2024, equivalent to an average of **~1,305 TPS**. This is derived from ILO data showing ~3.5 billion employed persons worldwide, multiplied by region-specific pay frequencies (biweekly in the US, monthly in the EU and most of Asia). **Payroll is overwhelmingly a subset of bank transfers** — approximately 85-90% of these transactions are already counted in the 484 billion bank transfer total as ACH/BACS/SEPA batch credits. The incremental, uncounted portion (~4.2B) consists of cash wage payments and check-based payroll in developing markets.

**Data quality is 🔴 Low for transaction counts** — no institution publishes a global payroll transaction count. The estimate is entirely model-derived from employment headcounts and pay frequency assumptions.

## Scope

This analysis covers:
- **Wage and salary disbursements** from employers to employees (formal sector)
- **All payment channels**: direct deposit (ACH/wire), check, cash wages
- **All employment types**: full-time, part-time, temporary, contract workers receiving regular pay

Excluded: self-employment income (no employer-to-worker transaction), gig economy per-task payments (counted in P2P/digital wallets), government benefit payments (separate category), pension disbursements.

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~1,305 | Derived from 41.2B annual ([calculations](workings/calculations.md#1-annual-transaction-count-2024)) | 🔴 Low |
| Peak TPS (est.) | ~6,500 | Estimated at 5.0x average (payday concentration) | 🔴 Low |
| Daily volume | ~112.9 million | Derived from annual total | 🔴 Low |
| Annual volume (2024) | ~41.2 billion | Employment × frequency model ([calculations](workings/calculations.md)) | 🔴 Low |
| Annual value (2024) | ~$32 trillion | ILO Global Wage Report (formal-sector wage bill) | 🟡 Medium |

### Regional Breakdown (2024)

| Region | Employed (M) | Formal Payroll (M) | Pay Frequency | Annual Payroll Txns (B) | Share |
|--------|-------------|-------------------|---------------|------------------------|-------|
| **United States** | 158.3 | ~150 | Biweekly (70%), weekly (20%), monthly (10%) | ~3.4 | 8.3% |
| **EU-27** | 197.6 | ~170 | Monthly (90%), biweekly (10%) | ~2.2 | 5.3% |
| **China** | ~740 | ~470 | Monthly (95%) | ~5.6 | 13.7% |
| **India** | ~560 | ~120 | Monthly (formal); cash (informal, excluded) | ~1.4 | 3.5% |
| **Japan** | ~67 | ~60 | Monthly (98%) | ~0.7 | 1.7% |
| **Rest of Asia-Pacific** | ~700 | ~300 | Monthly (80%), biweekly (20%) | ~4.2 | 10.2% |
| **Latin America** | ~290 | ~150 | Monthly (70%), biweekly (30%) | ~2.3 | 5.6% |
| **Africa** | ~460 | ~80 | Monthly (formal only) | ~1.0 | 2.4% |
| **Middle East** | ~70 | ~50 | Monthly (95%) | ~0.6 | 1.5% |
| **Rest of World** | ~260 | ~130 | Mixed | ~1.8 | 4.4% |
| **Sub-total (formal, electronic)** | | **~1,680** | | **~23.2** | **56.3%** |
| **Informal / cash wages** | | **~1,820** | | **~18.0** | **43.7%** |
| **GLOBAL TOTAL** | **~3,500** | **~3,500** | | **~41.2** | **100%** |

### Pay Frequency Distribution (Global)

| Frequency | Share of Workers | Annual Pays per Worker | Weighted Txns |
|-----------|-----------------|----------------------|---------------|
| Monthly | ~65% | 12 | ~27.3B |
| Biweekly | ~20% | 26 | ~18.2B (but subset is smaller total workers) |
| Weekly | ~5% | 52 | High frequency but small population |
| Semi-monthly | ~5% | 24 | Primarily US |
| Irregular/cash | ~5% | ~6-10 | Informal sector |

The US biweekly cycle drives a disproportionate share of global payroll transaction volume relative to its workforce size — 158M US workers generate ~3.4B annual payroll transactions due to 26 pay periods per year, compared to China's ~740M workers generating ~5.6B at 12 pay periods per year.

---

## Overlap with Bank Transfers

**Payroll is NOT an independent payment category — it is a subset of bank transfers.**

### Channel Decomposition

| Channel | Share of Payroll Txns | Overlap Category | Est. Txns (B) |
|---------|----------------------|------------------|---------------|
| ACH / Direct Deposit (US) | ~94% of US payroll | Bank Transfers (Batch/ACH) | ~3.2 |
| BACS (UK) | ~95% of UK payroll | Bank Transfers (Batch/ACH) | ~0.3 |
| SEPA Credit Transfer (EU) | ~92% of EU payroll | Bank Transfers (Batch/ACH) | ~2.0 |
| China domestic bank transfer | ~85% of China formal payroll | Bank Transfers | ~4.8 |
| Other electronic payroll | ~80-90% | Bank Transfers | ~18.7 |
| Cash wages | ~10% global average | Not counted elsewhere | ~4.0 |
| Check payroll (declining) | ~1% | Partially in bank transfers | ~0.2 |
| **TOTAL** | | | **~41.2** |

### Key Finding

**~37 billion (90%) of payroll transactions are already counted in the bank transfer total.** Only ~4.2 billion (primarily cash wages in developing markets) represent incremental transactions. For de-duplication purposes, payroll should be treated as an **analytic overlay** on bank transfers, not an additive category.

In the US specifically, ADP alone processes payroll for ~26 million workers per pay period. The total US ACH payroll volume (~3.2B transactions) represents roughly 9.5% of the 33.6B total US ACH transactions reported by Nacha for 2024.

---

## Historic Trend

| Year | Global Employed (B) | Est. Annual Payroll Txns (B) | Avg TPS | Notes |
|------|--------------------|-----------------------------|---------|-------|
| 2019 | 3.30 | 37.5 | 1,189 | Pre-COVID baseline |
| 2020 | 3.14 | 35.8 | 1,135 | COVID — ~5% global formal employment drop |
| 2021 | 3.25 | 37.2 | 1,179 | Partial recovery |
| 2022 | 3.38 | 39.1 | 1,239 | Recovery above 2019 |
| 2023 | 3.44 | 40.2 | 1,274 | Continued growth |
| 2024 | 3.50 | 41.2 | 1,305 | Current estimate |

*Source: ILO World Employment and Social Outlook; transaction counts derived.*

### Growth Rate Analysis

```
CAGR 2019-2024 (5yr): (41.2/37.5)^(1/5) - 1 = 1.9%
```

Payroll transaction growth tracks employment growth, which is slow and steady (~2% globally). Unlike card payments or real-time transfers, payroll volume cannot grow faster than workforce expansion unless pay frequencies increase (unlikely — the trend is toward monthly, not weekly).

---

## Projections

### Baseline (2% CAGR)
Tracks global employment growth; no major shift in pay frequency.

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,357 | 42.8 |
| 2028 | 1,411 | 44.5 |
| 2030 | 1,467 | 46.3 |
| 2035 | 1,618 | 51.1 |

### High Growth (4% CAGR)
Formalization of informal labor in India/Africa/SE Asia drives more workers onto payroll systems; gig economy workers move to W-2/formal contracts.

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,411 | 44.5 |
| 2030 | 1,649 | 52.0 |
| 2035 | 2,006 | 63.3 |

### Conservative (1% CAGR)
Automation reduces headcount; aging demographics in China/EU/Japan shrink workforce; gig economy grows (not counted as payroll).

| Year | Projected TPS | Annual Volume (B) |
|------|---------------|-------------------|
| 2026 | 1,325 | 41.8 |
| 2030 | 1,378 | 43.5 |
| 2035 | 1,449 | 45.7 |

---

## Key Findings

1. **Payroll is a massive but hidden payment flow.** At ~41.2B annual transactions, payroll generates more transaction volume than P2P transfers, remittances, and e-commerce combined — but it is invisible as an independent category because it flows through ACH/bank transfer rails.

2. **The US punches above its weight.** With only 4.5% of global workers, the US generates 8.3% of payroll transactions because of the biweekly pay cycle (26 pays/year vs. 12 for monthly-pay countries). This makes US ACH infrastructure disproportionately payroll-dependent.

3. **Informal labor is the blind spot.** ILO estimates ~2 billion informal workers globally. Their wages are paid in cash and are completely invisible to electronic payment systems. India alone has ~440M informal workers — roughly 80% of its workforce.

4. **Payroll is the most predictable payment category.** Unlike retail spending or P2P transfers, payroll volume is deterministic — it follows employment counts and calendar pay dates. This makes it the lowest-variance component of the bank transfer total.

5. **Peak TPS is extreme relative to average.** Payroll batches concentrate heavily on specific dates (1st and 15th, or biweekly Fridays). A single US payday Friday can see ~130M direct deposits processed in a 4-hour ACH window, generating burst rates 5-10x the daily average.

---

## Data Quality & Limitations

- **No direct data source exists.** There is no institution that counts global payroll transactions. This entire capsule is model-derived from employment statistics and pay frequency assumptions.
- **Informal economy exclusion.** The ILO estimates 58% of global employment is informal. Informal workers receiving cash wages generate real economic transactions but zero electronic payment events.
- **Pay frequency assumptions are coarse.** The biweekly/monthly split is based on US BLS, Eurostat, and regional norms — actual distributions within countries can vary significantly by industry and employer size.
- **Double-counting with bank transfers is near-total.** This capsule's primary value is analytical (sizing payroll as a share of bank transfers), not additive to the TPS total.
- **Gig economy boundary is fuzzy.** Uber drivers, DoorDash couriers, and similar gig workers receive per-task payments that look like payroll but are technically P2P or business-to-contractor transfers. These are excluded here but represent a growing grey area.

---

## Sources

1. [ILO — World Employment and Social Outlook 2024](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@dgreports/@inst/documents/publication/wcms_908142.pdf)
2. [ILOSTAT — Employment Statistics](https://ilostat.ilo.org/topics/employment/)
3. [BLS — Current Employment Statistics](https://www.bls.gov/ces/)
4. [Eurostat — Employment Annual Statistics 2024](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Employment_-_annual_statistics)
5. [ADP — Global Payroll Survey 2024](https://www.adp.com/-/media/adp/resourcehub/pdf/potential-payroll-survey-2024-us-en.pdf)
6. [Statista — Employment in China 2024](https://www.statista.com/topics/1317/employment-in-china/)
7. [Nacha — ACH Network Volume and Value Statistics](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
8. [CloudPay — Global Payroll Complexities and Trends 2024](https://www.cloudpay.com/blog/global-payroll-complexity-trends-by-region-2024/)

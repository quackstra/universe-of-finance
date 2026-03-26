# OTC Derivatives — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #7
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One bilateral OTC derivative contract execution (interest rate swap, CDS, equity swap, FX derivative, commodity swap, etc.)

---

## Executive Summary

The OTC derivatives market is the largest financial market in the world by notional outstanding — **$732 trillion at year-end 2024** according to BIS — yet it is paradoxically one of the **lowest-frequency markets by transaction count**. These are bespoke, bilateral contracts between sophisticated counterparties, typically executed in large notional sizes ($50M-$500M+ per trade for interest rate swaps).

We estimate approximately **40,000-60,000 OTC derivative trades per day** globally, yielding an average TPS of roughly **0.5-0.7**. This makes OTC derivatives the lowest-TPS category in the Universe of Finance despite being arguably the highest-value.

The 2025 BIS Triennial Survey revealed **OTC interest rate derivatives turnover surged to $7.9 trillion/day** (up 59% from 2022), driven by euro-denominated instruments and central bank policy divergence. However, this value is concentrated in relatively few, very large trades.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS (est.) | **~0.6** | 🔴 Low |
| Peak TPS (est.) | **~3** | 🔴 Low |
| Daily trade count (est.) | ~50,000 | 🔴 Low |
| Annual trade count (est.) | ~12.5M | 🟡 Medium |
| Notional outstanding (Dec 2024) | $732T | 🟢 High |
| Daily turnover — OTC IRD (Apr 2025) | $7.9T | 🟢 High |
| Daily turnover — OTC FX derivatives (Apr 2025) | $6.6T | 🟢 High |

**Methodology**: ISDA SwapsInfo reports ~2.9 million IRD trades in 2024 for US, EU, and UK markets. CDS adds ~317K trades. Adding other jurisdictions (Asia, EM) and other OTC derivative types (equity, commodity, FX derivatives) yields an estimated 12-13 million global OTC derivative trades per year. TPS = 12.5M / (252 x 10h x 3600) = ~1.4 during trading hours, or ~0.6 over a 24h day.

**Sources**: [ISDA SwapsInfo 2024 Review](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/), [BIS OTC Derivatives Statistics](https://www.bis.org/statistics/derstats.htm), [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25.htm)

---

## 2. Annual Volume (2024)

### 2.1 Trade Counts (ISDA SwapsInfo — US/EU/UK)

| Product | Annual Trades (2024) | YoY Change | Traded Notional | Source |
|---------|---------------------|------------|-----------------|--------|
| IRD — Total | ~2.9M | +8% (est.) | ~$400T | [ISDA](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/) |
| IRD — Q1 | 735.8K | -0.4% | $100.5T | ISDA Q1 2024 |
| IRD — H1 | 1.5M | +10.9% | $197.8T | ISDA H1 2024 |
| IRD — Q4 (US only) | 696.6K | +14.1% | $106.1T | ISDA Q4 2024 |
| Index CDS | 316.8K | -6.9% | $12.7T | ISDA FY 2024 |
| Single-name CDS | ~24K (est.) | — | ~$1.0T (est.) | Derived (7% of CDS notional) |
| **US/EU/UK Total** | **~3.2M** | — | **~$414T** | Composite |

### 2.2 Global Extrapolation

| Component | Est. Annual Trades | Notes |
|-----------|-------------------|-------|
| IRD (US/EU/UK reported) | 2.9M | ISDA SwapsInfo |
| IRD (rest of world, est. +35%) | 1.0M | Japan, Australia, HK, Singapore |
| CDS (global) | 0.4M | ISDA + non-reported markets |
| Equity derivatives (OTC) | 2.0M | Equity swaps, options — estimated |
| Commodity swaps (OTC) | 1.0M | Physical commodity hedging |
| FX derivatives (OTC, excl. spot) | 5.0M | Forwards, swaps, options (some overlap with FX category) |
| **Global Total (est.)** | **~12.3M** | — |

**Note on FX derivatives overlap**: FX forwards, swaps, and options are counted in the FX category. Some of these are also OTC derivatives. Per taxonomy, we include FX derivatives in the FX category and exclude them here to avoid double-counting. Excluding FX derivatives:

**OTC Derivatives (excl. FX): ~7.3M trades/year** = ~29K trades/day = **~0.3 TPS**
**OTC Derivatives (incl. FX derivatives): ~12.3M trades/year** = ~49K trades/day = **~0.6 TPS**

---

## 3. Notional Outstanding (BIS Semiannual)

| Date | Total Notional Outstanding | YoY Change | Source |
|------|---------------------------|------------|--------|
| Dec 2015 | $493T | — | [BIS](https://www.bis.org/statistics/derstats.htm) |
| Dec 2016 | $483T | -2.0% | BIS |
| Dec 2017 | $532T | +10.1% | BIS |
| Dec 2018 | $544T | +2.3% | BIS |
| Dec 2019 | $559T | +2.8% | BIS |
| Dec 2020 | $582T | +4.1% | BIS |
| Dec 2021 | $610T | +4.8% | BIS |
| Dec 2022 | $632T | +3.6% | BIS |
| Dec 2023 | $698T | +10.4% | BIS |
| Dec 2024 | $732T | +4.9% | [BIS/ISDA](https://www.isda.org/a/1rjgE/Key-Trends-in-the-Size-and-Composition-of-OTC-Derivatives-Markets-in-the-Second-Half-of-2024.pdf) |
| Jun 2025 | $846T | +16% vs Jun 2024 | [BIS](https://www.bis.org/publ/otc_hy2512.htm) |

### By Asset Class (Dec 2024)

| Asset Class | Notional Outstanding | Share | YoY Change |
|-------------|---------------------|-------|------------|
| Interest rate | $548.3T | 74.9% | +3.5% |
| FX | $130.1T | 17.8% | +10.2% |
| Credit (CDS) | $9.2T | 1.3% | +6.0% |
| Equity | $8.9T | 1.2% | +14.4% |
| Commodity | $2.4T | 0.3% | +9.3% |
| Other | $33.1T | 4.5% | — |
| **Total** | **$732.0T** | **100%** | **+4.9%** |

---

## 4. Daily Turnover (BIS Triennial Survey 2025)

| Asset Class | Daily Turnover (Apr 2025) | Change vs 2022 | Source |
|-------------|--------------------------|-----------------|--------|
| OTC Interest Rate Derivatives | $7.9T | +59% | [BIS](https://www.bis.org/statistics/rpfx25_ir.htm) |
| OTC FX Derivatives | $6.6T | +58% (est.) | [BIS](https://www.bis.org/statistics/rpfx25_fx.htm) |
| **Total OTC Derivatives** | **~$14.5T/day** | — | Composite |

**Key shift**: Euro-denominated IRD surged to $3.0T/day (from $1.6T in 2022), taking 38% share. USD contracts dropped to 31% share (from 46%) despite growing 7% to $2.4T/day.

---

## 5. Growth Rate Analysis

| Metric | Period | CAGR |
|--------|--------|------|
| Notional outstanding | 2015-2024 (9yr) | 4.5% |
| Notional outstanding | 2019-2024 (5yr) | 5.5% |
| IRD trade count (US/EU/UK) | 2023-2024 | ~8% |
| IRD daily turnover | 2022-2025 (3yr) | ~16.4% |
| CDS trade count | 2023-2024 | -6.9% |

---

## 6. Projections

### 6.1 Baseline (CAGR 5% on trade count)

| Year | Est. Annual Trades (M) | Est. TPS | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 12.3 | 0.6 | 732 |
| 2030 | 16.5 | 0.8 | 980 |
| 2035 | 21.1 | 1.0 | 1,250 |

### 6.2 High Growth (CAGR 8%)

| Year | Est. Annual Trades (M) | Est. TPS | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 12.3 | 0.6 | 732 |
| 2030 | 19.5 | 0.9 | 1,160 |
| 2035 | 28.7 | 1.4 | 1,700 |

### 6.3 Conservative (CAGR 2%)

| Year | Est. Annual Trades (M) | Est. TPS | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 12.3 | 0.6 | 732 |
| 2030 | 13.8 | 0.7 | 825 |
| 2035 | 15.3 | 0.7 | 910 |

**Scenario rationale**:
- **Baseline**: Steady growth driven by interest rate hedging demand, continued clearing mandate expansion. Trade counts grow modestly as compression and netting reduce ticket count while notional grows.
- **High Growth**: Electronic trading of OTC derivatives accelerates (SEF adoption), new participants enter, EM markets develop local currency swap markets.
- **Conservative**: Regulatory capital charges discourage OTC activity, migration to exchange-traded alternatives (e.g., futures replacing swaps), portfolio compression reduces gross notional and trade counts.

---

## 7. Key Findings

1. **OTC derivatives are the highest-VALUE, lowest-FREQUENCY financial market.** At ~0.6 TPS and $732T notional outstanding, each transaction represents an enormous economic commitment (average notional per trade: ~$60M for IRD).

2. **Interest rate derivatives dominate** at 75% of notional outstanding ($548T) and the majority of trade count. OIS (overnight index swaps) alone represent 70% of IRD traded notional.

3. **The 2025 BIS Triennial Survey shows OTC IRD turnover surged 59% to $7.9T/day**, driven by a near-doubling of euro-denominated contracts as ECB and Fed policy diverged.

4. **CDS volume is declining by trade count** (-6.9% YoY) even as notional grows, reflecting trade compression and portfolio optimization by dealers.

5. **Central clearing now dominates**: Over 70% of IRD trades are cleared through CCPs (LCH, CME Clearing), up from <30% pre-crisis. This has reduced bilateral credit risk but hasn't increased trade frequency.

6. **Double-counting note**: FX derivatives (forwards, swaps, options) are included in the FX category. We present OTC derivatives both including and excluding FX derivatives. For Universe of Finance aggregation, use the "excl. FX" figure (~7.3M trades/year) to avoid double-counting.

---

## 8. Data Quality & Limitations

- **Notional outstanding**: 🟢 High confidence — BIS semiannual survey is authoritative, based on reports from 65 major dealers.
- **Daily turnover**: 🟢 High confidence — BIS triennial survey is the gold standard.
- **Trade counts (US/EU/UK)**: 🟡 Medium — ISDA SwapsInfo aggregates DTCC SDR data. Covers major markets but not comprehensive.
- **Global trade count**: 🔴 Low — Requires extrapolation from US/EU/UK data to estimate Asia and EM markets.
- **Non-IRD/CDS trade counts**: 🔴 Low — Equity swaps, commodity swaps, and other OTC products have poor trade count visibility.
- **Gross credit exposure**: $3.0T at year-end 2024 (0.4% of notional), reflecting the heavily netted nature of the market.

---

## 9. Sources

1. [ISDA SwapsInfo — Full Year 2024 Review](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/)
2. [ISDA SwapsInfo — Full Year 2024 PDF](https://www.isda.org/a/jYNgE/SwapsInfo-Full-Year-2024-and-the-Fourth-Quarter-of-2024.pdf)
3. [ISDA — Key Trends in OTC Derivatives H2 2024](https://www.isda.org/a/1rjgE/Key-Trends-in-the-Size-and-Composition-of-OTC-Derivatives-Markets-in-the-Second-Half-of-2024.pdf)
4. [ISDA — Key Trends in OTC Derivatives H1 2024](https://www.isda.org/a/GpbgE/Key-Trends-in-the-Size-and-Composition-of-OTC-Derivatives-Markets-in-the-First-Half-of-2024.pdf)
5. [BIS — OTC Derivatives Statistics Overview](https://www.bis.org/statistics/derstats.htm)
6. [BIS — OTC Derivatives at end-June 2024](https://www.bis.org/publ/otc_hy2411.htm)
7. [BIS — OTC Derivatives at end-June 2025](https://www.bis.org/publ/otc_hy2512.htm)
8. [BIS — Triennial Survey 2025: OTC IRD Turnover](https://www.bis.org/statistics/rpfx25_ir.htm)
9. [BIS — Triennial Survey 2025 Press Release](https://www.bis.org/press/p250930.htm)
10. [ISDA — Reshaping the Global IRD Landscape (BIS 2025 analysis)](https://www.isda.org/2025/11/20/reshaping-the-global-ird-landscape-key-findings-from-the-2025-bis-triennial-survey/)

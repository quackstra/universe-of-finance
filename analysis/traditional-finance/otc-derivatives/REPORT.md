---
title: "OTC Derivatives — Report"
parent: Traditional Finance
grand_parent: Explore
nav_order: 6
---

# OTC Derivatives — Transaction Volume Analysis

> **Category**: Traditional Finance | **Priority**: #7
> **Last Updated**: 2026-03-26
> **Transaction Definition**: One bilateral OTC derivative contract execution (interest rate swap, CDS, equity swap, FX derivative, commodity swap, etc.)

---

## Executive Summary

The OTC derivatives market is the largest financial market in the world by notional outstanding — **$732 trillion at year-end 2024** according to BIS — yet it is paradoxically one of the **lowest-frequency markets by transaction count**. These are bespoke, bilateral contracts between sophisticated counterparties, typically executed in large notional sizes ($50M-$500M+ per trade for interest rate swaps).

**Revised estimate (Run 4 triangulation)**: A segmented model by derivative type yields **~4.7 million OTC derivative trades/year** (excluding FX derivatives), or **~18,700 trades/day**, for an average TPS of **~0.15** over 24h/365d. This is lower than the previous estimate of ~7.3M/~0.3 TPS because the earlier model overstated equity OTC and commodity OTC trade counts. Including FX derivatives: ~9.7M/year, ~0.31 TPS. The IRD and CDS components are well-anchored by ISDA SwapsInfo; equity and commodity OTC remain opaque.

The 2025 BIS Triennial Survey revealed **OTC interest rate derivatives turnover surged to $7.9 trillion/day** (up 59% from 2022), driven by euro-denominated instruments and central bank policy divergence. However, ISDA data shows trade count growth of +27.5% in H1 2025 vs H1 2024, indicating significant acceleration. However, this value is concentrated in relatively few, very large trades.

---

## 1. Current TPS (2024)

| Metric | Value | Confidence |
|--------|-------|------------|
| Average TPS — excl. FX derivatives | **~0.15** | 🟡 Medium |
| Average TPS — incl. FX derivatives | **~0.31** | 🔴 Low |
| Peak TPS (est.) | **~1.5** | 🔴 Low |
| Daily trade count — excl. FX (est.) | ~18,700 | 🟡 Medium |
| Annual trade count — excl. FX (est.) | ~4.7M | 🟡 Medium |
| Annual IRD trade count (US/EU/UK) | 2.7M | 🟢 High |
| Annual CDS trade count (index + single-name) | 525K | 🟢 High |
| Notional outstanding (Dec 2024) | $732T | 🟢 High |
| Daily turnover — OTC IRD (Apr 2025) | $7.9T | 🟢 High |
| Daily turnover — OTC FX derivatives (Apr 2025) | $6.6T | 🟢 High |

**Methodology**: Segmented model by derivative type. IRD: ISDA SwapsInfo 2.7M (US/EU/UK) + 0.4M (APAC/EM) = 3.1M. CDS: 525K (index + single-name, US/EU/UK) + 75K (RoW) = 0.6M. Equity OTC: 0.6M (estimated). Commodity OTC: 0.4M (estimated). Total excl. FX: 4.7M. FX derivatives (5M) excluded per taxonomy — counted in FX category. See [count triangulation](workings/count-triangulation.md) and [calculations](workings/calculations.md).

**Sources**: [ISDA SwapsInfo 2024](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/), [ISDA 2025](https://www.isda.org/2026/02/17/swapsinfo-full-year-2025-and-the-fourth-quarter-of-2025-review), [BIS OTC Derivatives Statistics](https://www.bis.org/statistics/derstats.htm), [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25.htm)

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

### 2.2 Global Extrapolation (Revised — Run 4 Triangulation)

| Component | Est. Annual Trades | Notes | Confidence |
|-----------|-------------------|-------|------------|
| IRD (US/EU/UK reported) | 2.7M | ISDA SwapsInfo FY 2024 (+8.2% YoY) | High |
| IRD (APAC: Japan, AU, SG, HK) | 0.32M | JSCC data + proportional scaling | Medium |
| IRD (EM/other) | 0.08M | Minimal bilateral unreported | Low |
| CDS — Index (US/EU/UK) | 0.317M | ISDA direct (-6.9% YoY) | High |
| CDS — Single-name (US/EU/UK) | 0.208M | ISDA direct (-16.6% YoY) | High |
| CDS — Rest of world | 0.075M | ~15% uplift | Low |
| Equity derivatives (OTC) | 0.6M | Equity swaps, TRS, variance swaps — estimated | Low |
| Commodity swaps (OTC) | 0.4M | Physical commodity hedging — estimated | Low |
| **Total (excl. FX)** | **~4.7M** | — | Medium |
| FX derivatives (OTC, excl. spot) | 5.0M | Forwards, swaps, options — EXCLUDED (in FX category) | Low |
| **Total (incl. FX)** | **~9.7M** | — | Low-Medium |

**Note on FX derivatives overlap**: FX forwards, swaps, and options are counted in the FX category. Per taxonomy, we exclude FX derivatives here to avoid double-counting.

**OTC Derivatives (excl. FX): ~4.7M trades/year** = ~18.7K trades/day = **~0.15 TPS** (24h/365d)
**OTC Derivatives (incl. FX derivatives): ~9.7M trades/year** = ~38.5K trades/day = **~0.31 TPS** (24h/365d)

**Why lower than previous estimate?** The prior model assumed 2.0M equity OTC and 1.0M commodity OTC trades. Triangulation against BIS notional data, proportional scaling, and available CCP data suggests these were overstated. These markets are dominated by very large institutional trades with low ticket counts. See [count-triangulation.md](workings/count-triangulation.md) for detailed methodology.

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

### 6.1 Baseline (CAGR 7% on trade count — excl. FX)

| Year | Est. Annual Trades (M) | Est. TPS (24h) | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 4.7 | 0.15 | 732 |
| 2030 | 6.9 | 0.22 | 980 |
| 2035 | 9.5 | 0.30 | 1,250 |

### 6.2 High Growth (CAGR 13% — in line with 2025 acceleration)

| Year | Est. Annual Trades (M) | Est. TPS (24h) | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 4.7 | 0.15 | 732 |
| 2030 | 10.1 | 0.32 | 1,160 |
| 2035 | 16.4 | 0.52 | 1,700 |

### 6.3 Conservative (CAGR 2%)

| Year | Est. Annual Trades (M) | Est. TPS (24h) | Notional Outstanding (est. $T) |
|------|-----------------------|----------|-------------------------------|
| 2024 | 4.7 | 0.15 | 732 |
| 2030 | 5.4 | 0.17 | 825 |
| 2035 | 6.0 | 0.19 | 910 |

**Scenario rationale**:
- **Baseline**: Steady growth driven by interest rate hedging demand, continued clearing mandate expansion. Trade counts grow modestly as compression and netting reduce ticket count while notional grows.
- **High Growth**: Electronic trading of OTC derivatives accelerates (SEF adoption), new participants enter, EM markets develop local currency swap markets.
- **Conservative**: Regulatory capital charges discourage OTC activity, migration to exchange-traded alternatives (e.g., futures replacing swaps), portfolio compression reduces gross notional and trade counts.

---

## 7. Key Findings

1. **OTC derivatives are the highest-VALUE, lowest-FREQUENCY financial market.** At ~0.15 TPS (excl. FX) and $732T notional outstanding, each transaction represents an enormous economic commitment (average notional per trade: ~$118M for IRD, even higher for commodity swaps).

2. **Interest rate derivatives dominate by trade count (~66% of total)** at 3.1M trades/year globally. ISDA SwapsInfo provides high-confidence data for US/EU/UK (2.7M); APAC adds ~0.4M anchored by JSCC data.

3. **The 2025 BIS Triennial Survey shows OTC IRD turnover surged 59% to $7.9T/day**, driven by a near-doubling of euro-denominated contracts as ECB and Fed policy diverged. ISDA H1 2025 data shows trade count up 27.5% — the acceleration is real and significant.

4. **CDS trade count is mixed**: Index CDS declined 6.9% in 2024 but rebounded 11.6% in 2025 (353.3K). Single-name CDS continues declining (-16.6% in 2024, -5.8% in 2025), reflecting compression and portfolio optimization.

5. **Equity and commodity OTC derivatives are the most opaque segments**: No public aggregate trade count data exists. Our estimates (0.6M and 0.4M respectively) are low-confidence extrapolations.

6. **Central clearing now dominates**: 76.9% of IRD by notional, 67.9% of CDS. SEF-traded IRD accounted for 77.3% of trade count in 2025. Electronic execution is growing but hasn't dramatically increased overall ticket count yet.

7. **Double-counting note**: FX derivatives are excluded from our primary figure (counted in FX category). For Universe of Finance aggregation, use ~4.7M trades/year (excl. FX).

---

## 8. Data Quality & Limitations

- **Notional outstanding**: 🟢 High confidence — BIS semiannual survey is authoritative, based on reports from 65 major dealers.
- **Daily turnover**: 🟢 High confidence — BIS triennial survey is the gold standard.
- **Trade counts (US/EU/UK)**: 🟡 Medium — ISDA SwapsInfo aggregates DTCC SDR data. Covers major markets but not comprehensive.
- **Global trade count**: 🔴 Low — Requires extrapolation from US/EU/UK data to estimate Asia and EM markets.
- **Non-IRD/CDS trade counts**: 🔴 Low — Equity swaps, commodity swaps, and other OTC products have poor trade count visibility.
- **Gross credit exposure**: $3.0T at year-end 2024 (0.4% of notional), reflecting the heavily netted nature of the market.

---

## Open Questions & Triangulation Opportunities

> **Run 4 update (2026-03-27)**: Detailed count triangulation completed. See [workings/count-triangulation.md](workings/count-triangulation.md) for the full segmented model, sensitivity analysis, and definition discussion.

### What We Can't Directly Observe
- **Equity OTC derivative trade count**: This is the single biggest gap. No public source aggregates global OTC equity swap/option trade counts. SEC SBSDR covers US security-based swaps, but aggregate statistics are not published accessibly. Our 0.6M estimate carries a wide range (0.3M-1.0M).
- **Commodity OTC derivative trade count**: Similar opacity. BIS notional ($2.4T outstanding) provides a ceiling anchor, but trade count depends heavily on average notional per trade.
- **Asia-Pacific OTC derivatives beyond Japan**: JSCC provides JPY IRS clearing data (record JPY 8,272T in 2024), but China, India, Korea, and other markets lack accessible English-language trade count reporting.
- **Impact of compression on reported trade counts**: TriOptima/OSTTRA compression cycles eliminate trades (e.g., 79% of eligible trades in a single commodities cycle). If we counted gross trades before compression, the total could be 2-5x higher.
- **True bilateral vs. cleared split by trade count**: BIS reports clearing rates by notional (76.9% for IRD, 67.9% for CDS), but clearing rates by trade count may differ.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| DTCC Trade Repository data | DTCC publishes weekly SDR data for CFTC-regulated swaps; aggregate for trade counts | [DTCC Repository OTC Data](https://www.dtcc.com/repository-otc-data) — weekly public dissemination | 🟡 Medium |
| Compression impact | Track TriOptima/OSTTRA compression cycle announcements; estimate trades eliminated per cycle | OSTTRA reports ~79% trade elimination in commodity cycles; LCH SwapClear compression data | 🟡 Medium |
| Central clearing % as opacity indicator | Higher clearing = more transparent trade count data; use clearing rate to bound observable vs. opaque trades | BIS: IRD 76.9% cleared, CDS 67.9% cleared; mandated currencies 98% cleared | 🟢 High |
| Asia-Pacific trade count | Use Japan JSCC clearing data + Australian ASIC trade repository reports as anchors for APAC estimate | JSCC publishes IRD clearing volumes; ASIC derivative trade repository data | 🟡 Medium |
| Equity swap trade count | SEC SBSDR data covers security-based swaps (equity + single-name CDS) in US | [SEC SBSDR](https://www.sec.gov/rules-regulations/staff-guidance/current-guidance/division-trading-markets-staff-guidance) public data | 🟡 Medium |

### Key Modeling Questions
- How many OTC derivative trades are "eliminated" annually by compression? If TriOptima eliminates 79% of eligible trades per cycle, and cycles run quarterly, the gross trade count before compression could be substantially higher than the net figure we observe.
- As the clearing mandate expands (particularly for Phase 6 entities), does trade count increase (more standardized = more trades) or decrease (compression + netting efficiencies)?
- The euro-denominated IRD surge to $3.0T/day (from $1.6T in 2022) — does this represent more trades or larger trades? ECB policy divergence could drive both.
- What is the "dark matter" of OTC derivatives? Non-reportable trades below de minimis thresholds and trades in non-mandatory jurisdictions could add 10-30% to observed counts.

### Reference Comparisons
- **ISDA SwapsInfo 2024**: US IRD Q4 trade count was 696.6K (+14.1% YoY) — acceleration in trade frequency signals electronification gains
- **CDS trade count declining**: 316.8K index CDS trades in 2024 (-6.9% YoY), even as notional grows — compression and portfolio optimization reduce ticket counts
- **BIS gross credit exposure**: $3.0T at year-end 2024 (0.4% of $732T notional) — demonstrates massive netting; the true economic exposure is 250× smaller than gross notional
- **Cleared share**: IRD 76.9% cleared ($445T), CDS 67.9% cleared ($6.1T) at H1 2024 ([BIS/CCP Global](https://ccp-global.org/sites/default/files/2025-02/INCENTIVES-FOR-CENTRAL-CLEARING-AND-THE-EVOLUTION-OF-OTC-DERIVATIVES-A-CCP12-REPORT_FINAL.pdf)); mandated currencies at 98% clearing rate
- **OSTTRA/TriOptima compression**: In a single commodities compression cycle, 79% of submitted eligible trades were fully terminated — illustrating how compression deflates trade count statistics

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

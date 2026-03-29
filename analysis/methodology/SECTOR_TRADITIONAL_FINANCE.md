---
title: "Sector: Traditional Finance"
parent: Methodology
grand_parent: Explore
nav_order: 3
---

# Sector Methodology: Traditional Finance

> How we measure trading activity across equity, fixed income, derivatives, FX, and commodity markets — 6 categories, ~13,373 TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

Traditional Finance measures **trading activity** — the execution of buy/sell orders for financial instruments on exchanges, OTC markets, and bilateral platforms. At ~13,373 TPS, TradFi accounts for **19% of global financial TPS**, making it the second-largest sector after Payments.

The sector is dominated by exchange-traded derivatives (9,505 TPS, 71% of sector), driven by the explosion of options trading in India and the structural growth of futures markets globally. Equity markets contribute 3,500 TPS, with the remaining categories (commodities, FX, fixed income, OTC derivatives) collectively adding ~374 TPS.

---

## 2. Sector-Specific Measurement Challenges

**Trade vs. order vs. settlement.** A single equity trade may generate 10-50 order messages (quotes, cancellations, modifications) before execution. We count **executed trades**, not order book activity. Settlement is counted separately in the Banking sector.

**OTC opacity.** OTC derivatives and fixed income are traded bilaterally, with no central order book. Transaction counts are inferred from post-trade reporting (TRACE for US bonds, DTCC for CDS) or from BIS surveys that publish notional values, not transaction counts.

**FX data staleness.** The definitive FX data source (BIS Triennial Survey) publishes every 3 years. Between surveys, we apply growth rates from SWIFT FX messaging data as a proxy, introducing compounding uncertainty.

**Dark pools and internalization.** An estimated 15-20% of US equity volume trades off-exchange (dark pools, ATS, systematic internalizers). These are harder to aggregate than lit exchange data.

**Exchange-traded derivatives growth.** ETD volume has been growing ~15%+ annually, driven largely by India's NSE (which now processes more options contracts than any other exchange). Historical growth rates may not persist, but they complicate year-over-year comparisons.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume | Confidence | Notes |
|---|----------|---------|--------------|------------|-------|
| 1 | Exchange-Traded Derivatives | 9,505 | 205.3B contracts | 88 (High) | FIA data; includes NSE options explosion |
| 2 | Equity Markets | 3,500 | 61.5B trades | 86 (High) | WFE + dark pool estimates |
| 3 | Commodities | 330 | 6.5B contracts | 74 (Medium-High) | FIA/CME/ICE data |
| 4 | Foreign Exchange | 40 | 882M trades | 58 (Medium) | BIS Triennial + growth projection |
| 5 | Fixed Income / Bond Markets | 3.6 | 112.9M trades | 60 (Medium-High) | TRACE + estimated global |
| 6 | OTC Derivatives | 0.17 | 5.3M contracts | 68 (Medium-High) | BIS notional → count conversion |

**Sector total: ~13,373 TPS** — no significant intra-sector overlaps.

---

## 4. Cross-Category Overlap Rules

### Overlap Analysis

TradFi has **no significant intra-sector overlaps.** Each category represents a distinct asset class traded on distinct infrastructure:

- ETD and OTC derivatives are mutually exclusive (exchange-traded vs. bilateral)
- Equity, fixed income, and commodities are distinct asset classes
- FX is independent of all other categories

The only potential overlap is commodity ETDs counted in both "Commodities" and "ETD". Our rule: commodity futures/options counted in Commodities only; ETD counts exclude commodity contracts. This avoids double-counting.

### Cross-Sector Overlap

TradFi trades generate downstream **settlement events** in the Banking sector (Securities Settlement, Interbank RTGS). Per UoF taxonomy rules, the trade and the settlement are separate transactions on different infrastructure:

```
┌──────────────────────────┐     ┌──────────────────────────┐
│    TRADFI SECTOR          │     │    BANKING SECTOR         │
│                           │     │                           │
│  Equity Trade: 1 trade   │────>│  CSD Settlement: 1 entry │
│  Bond Trade:   1 trade   │────>│  CSD Settlement: 1 entry │
│  ETD Contract: 1 trade   │────>│  CCP Clearing:  margined │
│  FX Trade:     1 trade   │────>│  CLS/RTGS: 1 settlement  │
│                           │     │                           │
│  Counted HERE             │     │  Counted HERE             │
│  (execution layer)        │     │  (settlement layer)       │
└──────────────────────────┘     └──────────────────────────┘

Both are real transactions. NOT deduplicated.
```

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
FIA Annual Survey   █████████░ █████████ █████████░  ████████░░
WFE Statistics      █████████░ █████████ █████████░  ███████░░░
BIS Triennial       ████████░░ ████░░░░░ ██████████  ██████░░░░
TRACE (US bonds)    ████░░░░░  █████████ █████████░  ██████████
CME/ICE Filings     ████░░░░░  █████████ █████████░  ██████████
ISDA Research       ██████░░░  ███████░░ ████████░░  ████░░░░░░
FINRA ATS Data      ███░░░░░░  █████████ █████████░  ████████░░
BIS OTC Stats       ██████░░░  ███████░░ ██████████  ███░░░░░░░
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Primary anchors):** FIA (ETD), WFE (equities), BIS (FX, OTC derivatives)
**Tier 2 (Cross-validation):** CME/ICE filings, TRACE, FINRA ATS data
**Tier 3 (Gap-filling):** ISDA research, academic studies, broker surveys

---

## 6. Sector Triangulation Approach

### Traditional Finance Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [Authority Data]      [Operator Sum]      [Value/Size]  │
│  FIA + WFE + BIS       Sum of exchange     Total value ÷ │
│  published stats       annual reports      avg trade size │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ 274.7B   │         │ 261B     │        │ 290B     │  │
│  │ annual   │         │ annual   │        │ annual   │  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ Method B undercounts  │                    │
│              │ by ~5% (misses small  │                    │
│              │ exchanges, dark       │                    │
│              │ pools). Method C      │                    │
│              │ overcounts by ~6%     │                    │
│              │ (avg trade size       │                    │
│              │ assumption too low).  │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ ~274B annual trades   │                    │
│              │ ~13,373 TPS           │                    │
│              │ Range: 12,000-15,000  │                    │
│              │ Confidence: 79/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## 7. Definition Standards

In Traditional Finance, a **transaction** is an **executed trade** — the point at which a buy order and sell order are matched and a binding agreement is formed.

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| Exchange-Traded Derivatives | Executed contract (matched on exchange) | Cancelled orders, quote updates, margin calls |
| Equity Markets | Executed trade (matched order) | Order submissions, cancellations, amendments |
| Commodities | Executed futures/options contract | Physical delivery events, warehouse receipts |
| Foreign Exchange | Completed FX deal (spot, forward, swap, option) | RFQ messages, price quotes |
| Fixed Income | Executed bond trade (primary or secondary) | Coupon payments, maturity events |
| OTC Derivatives | Confirmed bilateral contract | Novations, amendments, lifecycle events |

**Key distinction from Payments:** TradFi counts the **agreement to exchange**, not the movement of money. The money movement (settlement) is counted separately in the Banking sector.

---

## 8. Known Gaps & Future Work

- **FX transaction count.** The BIS Triennial Survey publishes daily turnover VALUE ($7.5T/day) but not transaction COUNT. Our 882M annual figure derives from value / average trade size, making it sensitive to the size assumption. Direct transaction count data from CLS or EBS would improve confidence.
- **OTC derivatives frequency.** At 0.17 TPS, this is the lowest-frequency category. The number is derived from BIS notional outstanding / average contract size / average tenor. Direct trade reporting repositories (DTCC, REGIS-TR) could provide better counts.
- **Dark pool coverage.** We estimate 15-20% of equity volume is off-exchange, but aggregating ATS/dark pool data globally is difficult. FINRA covers US; European SI data is fragmented.
- **India ETD explosion.** NSE options volume has grown 50%+ annually. Current data may understate 2025-2026 reality. Real-time FIA updates would help.
- **Bond market fragmentation.** TRACE covers US corporate bonds well, but government bond and non-US bond trading counts are poorly documented. The 112.9M annual figure has the widest uncertainty band in the sector.

---

*TradFi is the cleanest sector for methodology — distinct asset classes, well-established exchanges, and strong regulatory reporting. The main challenge is the opaque corners: OTC, dark pools, and FX.*

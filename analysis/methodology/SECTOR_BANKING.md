---
title: "Sector: Banking"
parent: Methodology
grand_parent: Explore
nav_order: 5
---

# Sector Methodology: Banking & Interbank

> How we measure settlement infrastructure throughput — 2 categories, ~92-98 TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

The Banking sector measures **settlement infrastructure** — the systems that discharge financial obligations between institutions. This includes Real-Time Gross Settlement (RTGS) systems that settle high-value interbank payments and Central Securities Depositories (CSDs) / Central Counterparties (CCPs) that settle trades from the Traditional Finance sector.

At ~92-98 TPS, Banking accounts for just **0.1% of global financial TPS** — but it underpins the entire financial system. Every card payment, stock trade, and bond transaction ultimately settles through one of these systems. The low TPS reflects extreme netting: millions of individual transactions are compressed into thousands of settlement entries.

---

## 2. Sector-Specific Measurement Challenges

**Netting compression.** CCP clearing compresses thousands of trades into a small number of settlement obligations. The netting ratio can be 100:1 or higher for liquid markets. We count **settlement instructions** (post-netting), not the underlying trades (which are counted in TradFi).

**RTGS system coverage.** The world has 80+ RTGS systems. Our initial Run 1 covered only 5 (Fedwire, TARGET2, CHAPS, BOJ-NET, CLS). Run 3 expanded to 13 systems, tripling the volume from ~423M to ~1,581M annual transactions. The remaining ~67 systems are estimated but add relatively small volumes.

**Settlement vs. trade boundary.** A stock trade counted in Equity Markets generates a settlement instruction counted in Securities Settlement. Per UoF rules, both are real transactions on different infrastructure — but this requires careful documentation to avoid confusion.

**Asia-Pacific CSD data.** US (DTCC) and EU (Euroclear, Clearstream) CSDs publish detailed settlement statistics. Asian CSDs (JASDEC, CCDC, HKMA CMU) have variable disclosure quality.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume | Confidence | Notes |
|---|----------|---------|--------------|------------|-------|
| 1 | Interbank Settlement (RTGS) | 50.1 | 1,581M transactions | 82 (High) | 13 RTGS systems |
| 2 | Securities Settlement | 41-48 | ~1,400M instructions | 74 (Medium-High) | CSDs + CCPs |

**Sector total: ~92-98 TPS**

---

## 4. Cross-Category Overlap Rules

### Overlap Analysis

The two Banking categories operate on **distinct infrastructure** with **no overlap**:

- **RTGS** settles cash obligations between banks (Fedwire: bank-to-bank fund transfers)
- **Securities Settlement** settles the delivery of securities against payment (DTCC: share delivery + cash payment)

Some securities settlements trigger RTGS movements (the cash leg of delivery-versus-payment), but these are separate system entries. No de-duplication needed within the sector.

### Cross-Sector Relationship

```
┌─────────────────────────────────────────────────────────┐
│  UPSTREAM: What generates settlement instructions         │
│                                                          │
│  Payments Sector          TradFi Sector                  │
│  ┌──────────────┐        ┌──────────────┐               │
│  │ 53,200 TPS   │        │ 13,373 TPS   │               │
│  │ card, bank,  │        │ equity, bond,│               │
│  │ wallet txns  │        │ derivative   │               │
│  └──────┬───────┘        └──────┬───────┘               │
│         │                       │                        │
│         │  Batch + Net          │  CCP + CSD             │
│         │  compression          │  netting               │
│         ▼                       ▼                        │
├─────────────────────────────────────────────────────────┤
│  BANKING SECTOR (settlement layer)                       │
│                                                          │
│  ┌──────────────┐        ┌──────────────┐               │
│  │ RTGS: 50 TPS │        │ Securities   │               │
│  │ (1,581M/yr)  │        │ Settlement:  │               │
│  │ High-value   │        │ 41-48 TPS    │               │
│  │ bank-to-bank │        │ (1,400M/yr)  │               │
│  └──────────────┘        └──────────────┘               │
│                                                          │
│  Compression ratio: ~700:1 (66,573 upstream TPS →        │
│                             ~95 settlement TPS)          │
└─────────────────────────────────────────────────────────┘
```

**Not deduplicated:** Settlement is a real, distinct transaction on dedicated infrastructure. The trade is one event; the settlement is another. Both are counted.

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Federal Reserve     ████░░░░░  █████████ ██████████  ██████████
(Fedwire stats)
ECB (T2 stats)      ████░░░░░  █████████ ██████████  █████████░
DTCC Annual Report  ████░░░░░  █████████ █████████░  ████████░░
Euroclear/          ████░░░░░  █████████ █████████░  ████████░░
Clearstream
BIS CPMI Red Book   ████████░░ █████░░░░ ██████████  ██████░░░░
CLS Group           ███░░░░░░  █████████ █████████░  █████████░
PBOC (CNAPS data)   ███░░░░░░  ████████░ █████████░  ████░░░░░░
RBI (India RTGS)    ███░░░░░░  █████████ █████████░  █████████░
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Primary anchors):** Central bank published statistics (Fedwire, TARGET2/T2, CHAPS, CNAPS-HVPS, India RTGS, BOJ-NET)
**Tier 2 (Cross-validation):** DTCC, Euroclear, Clearstream (CSD-level), CLS Group (FX settlement)
**Tier 3 (Gap-filling):** BIS CPMI Red Book (aggregated cross-country), smaller RTGS system annual reports

---

## 6. Sector Triangulation Approach

### Banking Sector Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [Central Bank Data]   [BIS CPMI Agg.]    [Netting      │
│  Sum of 13 RTGS        BIS Red Book       Ratio Model]  │
│  system annual         aggregated stats   TradFi trades  │
│  reports                                  ÷ est. ratio   │
│  ┌──────────┐         ┌──────────┐       ┌──────────┐   │
│  │ 1,581M   │         │ ~1,450M  │       │ ~1,600M  │   │
│  │ (RTGS)   │         │ (BIS     │       │ (implied │   │
│  │          │         │  subset) │       │  settle) │   │
│  └────┬─────┘         └────┬─────┘       └────┬─────┘   │
│       │                    │                   │         │
│       └────────────────────┼───────────────────┘         │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ BIS undercounts (only │                    │
│              │ CPMI members; misses  │                    │
│              │ ~8 of our 13 systems).│                    │
│              │ Netting model agrees  │                    │
│              │ within 5%.            │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ RTGS: 1,581M/yr       │                    │
│              │ Sec. Settle: ~1,400M  │                    │
│              │ Total: ~92-98 TPS     │                    │
│              │ Confidence: 78/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## 7. Definition Standards

In the Banking sector, a **transaction** is a **settlement instruction** — the final, irrevocable movement of funds or securities between institutional accounts.

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| Interbank RTGS | Individual payment order settled in the RTGS system | Queued but unsettled orders, liquidity management transfers |
| Securities Settlement | Settlement instruction (delivery-vs-payment or free-of-payment) | Matching/confirmation messages, fails (unsettled instructions) |

**Key distinction:** Banking counts at the **settlement** lifecycle point — the last step in the transaction chain. This produces the smallest numbers (due to netting) but represents the most definitive completion event.

### The 13 RTGS Systems Covered

| System | Country | Annual Volume (M) |
|--------|---------|-------------------|
| Fedwire | US | 210 |
| CNAPS-HVPS | China | 382 |
| India RTGS | India | 295 |
| TARGET2/T2 | EU | 108 |
| BOJ-NET | Japan | 20 |
| CHAPS | UK | 52.7 |
| CLS | Multi-currency FX | 300 |
| SARIE | Saudi Arabia | ~65 |
| BOK-Wire+ | South Korea | ~45 |
| RITS | Australia | ~40 |
| Lynx | Canada | ~35 |
| MEPS+ | Singapore | ~15 |
| BESP | Russia | ~13 |

---

## 8. Known Gaps & Future Work

- **Missing RTGS systems.** 67+ RTGS systems not yet individually counted (e.g., SAMOS in South Africa, SPEI in Mexico, RTGS-NG in Nigeria). These likely add 50-100M annual transactions.
- **CCP clearing counts.** CCP netting activity (LCH, CME Clearing, JSCC, Eurex Clearing) is partially captured in securities settlement but not fully disaggregated.
- **Cross-border settlement.** CLS (300M annual) covers multi-currency FX settlement, but non-CLS cross-border settlement (correspondent banking) is estimated. SWIFT messaging data could provide a better proxy.
- **Real-time securities settlement.** As markets move toward T+1 and eventually T+0, the settlement cycle shortens and the settlement-to-trade ratio may change. Current methodology assumes current netting ratios.
- **Digital asset settlement.** Blockchain-based settlement (tokenized securities on DLT) is emerging but currently negligible. As RWA tokenization grows, the boundary between Banking and Digital Assets settlement may blur.

---

*Banking is the foundation layer. Its low TPS belies its systemic importance — every other sector's transactions ultimately flow through settlement infrastructure. The methodology challenge is expanding coverage from 13 RTGS systems toward the full 80+.*

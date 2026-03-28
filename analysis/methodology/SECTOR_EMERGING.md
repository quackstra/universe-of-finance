# Sector Methodology: Emerging Transaction Types

> How we measure IoT payments, tokenized real-world assets, and AI agent transactions — 3 categories, ~637 TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

The Emerging sector measures **nascent transaction types** that do not fit neatly into traditional categories — machine-to-machine payments (IoT/M2M), tokenized real-world assets (RWA), and autonomous AI agent transactions. At ~637 TPS, Emerging accounts for **0.9% of global financial TPS**.

This sector spans the full maturity spectrum: IoT/M2M is already processing ~48.5B annual transactions (mature but poorly measured), RWA tokenization is early-stage with ~75M annual transactions, and AI agent transactions are pre-market at ~21M annual events. The measurement challenge varies accordingly — IoT requires triangulation across fragmented segments, while AI agents require projecting from near-zero base.

---

## 2. Sector-Specific Measurement Challenges

**IoT payment rail attribution.** The vast majority of IoT/M2M payments (70-80%) ride on existing card, bank, or wallet rails. A connected car paying a toll uses a linked credit card. A smart meter paying a utility bill uses a direct debit. Only 20-30% of IoT payments use genuinely new rails (embedded SIM payments, machine wallets, API micropayments).

**RWA on-chain subset.** Tokenized RWA transactions occur on blockchains and are therefore a subset of L1/L2 on-chain transactions (counted in Digital Assets). They are not additive. The RWA category exists as an analytical view to track this specific use case.

**AI agent immaturity.** At 0.66 TPS, AI agent transactions are barely measurable. The category is included for forward-looking completeness, not current significance. Most "data" is projections, not measurements.

**Definitional novelty.** What counts as an "IoT payment"? Is a smart TV auto-renewing a subscription an IoT payment or a recurring card payment? Is an AI agent calling a paid API an AI transaction or an API call? Boundary definitions are still being established.

**Projection vs. measurement.** For IoT and AI agents, much of the available data is market forecasts (Gartner, IDC, McKinsey) rather than actual measurements. We use forecasts only as cross-references, anchoring on observable data where possible.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume | Confidence | Notes |
|---|----------|---------|--------------|------------|-------|
| 1 | IoT & Machine-to-Machine Payments | 1,538 | ~48.5B | 67 (Medium-High) | Triangulated across 6 segments |
| 2 | Tokenised Real-World Assets | 2.4 | ~75M | 56 (Medium) | On-chain (subset of L1/L2) |
| 3 | AI Agent Transactions | 0.66 | ~21M | 34 (Low-Medium) | Pre-market category |

**Sector total: ~637 TPS** (using ~634 for IoT after rounding, +2.4 RWA, +0.66 AI)

---

## 4. Cross-Category Overlap Rules

### Intra-Sector

No overlap between the three categories. IoT is primarily fiat-rail, RWA is on-chain, and AI agents are a mix.

### Cross-Sector Overlap

```
┌─────────────────────────────────────────────────────────┐
│  EMERGING SECTOR: ~637 TPS                               │
│                                                          │
│  ┌────────────────┐  ┌────────────┐  ┌──────────────┐  │
│  │  IoT/M2M       │  │    RWA     │  │  AI Agents   │  │
│  │  ~1,538 TPS    │  │  2.4 TPS   │  │  0.66 TPS    │  │
│  │                │  │            │  │              │  │
│  │ 70-80% on     │  │ 100% on    │  │ ~60% on      │  │
│  │ card/bank     │  │ L1/L2      │  │ L1/L2 (x402) │  │
│  │ rails         │  │ (subset)   │  │ ~40% via API  │  │
│  └───────┬────────┘  └─────┬──────┘  └──────┬───────┘  │
│          │                 │                │           │
│          ▼                 ▼                ▼           │
│  ┌────────────────────────────────────────────────┐     │
│  │ Overlap Resolution:                            │     │
│  │                                                 │     │
│  │ IoT → Payments overlap: ~75% (~36.4B)           │     │
│  │        Incremental: ~25% (~12.1B) = ~384 TPS    │     │
│  │                                                 │     │
│  │ RWA → Digital Assets overlap: 100% (on-chain)   │     │
│  │        Incremental: 0 TPS                       │     │
│  │                                                 │     │
│  │ AI → Digital Assets overlap: ~60% (on-chain)    │     │
│  │       Incremental: ~40% = ~0.26 TPS             │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
│  Total incremental to Big Number: ~127-190 TPS           │
│  (IoT non-card portion only; RWA and AI negligible)      │
└─────────────────────────────────────────────────────────┘
```

**Decision:** In the payment infrastructure Big Number (~70,200), only the incremental IoT portion (~159 TPS) is added via the economic transaction method. RWA and AI agent transactions are subsets of existing sectors.

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
NPCI (FASTag/       ███░░░░░░  █████████ █████████░  ██████████
 NETC toll data)
E-ZPass/IBTTA       ███░░░░░░  ████████░ █████████░  ████████░░
(toll data)
GSMA IoT Reports    ████████░░ ████████░ ████████░░  ████░░░░░░
RWA.xyz / DeFiLlama ██████░░░░ ██████████ ███████░░░ ████████░░
(RWA on-chain)
Block explorers     ██████░░░░ ██████████ █████████░ ██████████
(AI agent txns)
Gartner/IDC         ████████░░ ███████░░ ████████░░  ███░░░░░░░
(IoT projections)
x402 protocol data  ██░░░░░░░░ ██████████ ██████░░░░ ████████░░
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Observable data):** Toll collection systems (NPCI FASTag, E-ZPass, European ETC), block explorers (RWA and AI agent on-chain activity)
**Tier 2 (Industry estimates):** GSMA IoT reports, RWA.xyz dashboards, DeFiLlama
**Tier 3 (Projections):** Gartner/IDC (IoT market sizing), academic papers, x402 protocol metrics

---

## 6. Sector Triangulation Approach

### IoT Triangulation Funnel (dominant category)

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES (IoT/M2M only)                 │
│                                                          │
│  Method A              Method B            Method C      │
│  [Segment Sum]         [Connected Device   [Industry     │
│  Toll + utility +      Count × Payment     Reports]      │
│  transit + vending     Frequency]          Gartner, IDC, │
│  + auto + industrial                       GSMA estimates │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ 48.5B    │         │ 42B      │        │ 55B      │  │
│  │ annual   │         │ annual   │        │ annual   │  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ Method B undercounts  │                    │
│              │ (not all connected    │                    │
│              │ devices make payments;│                    │
│              │ but those that do     │                    │
│              │ transact frequently). │                    │
│              │ Method C overcounts   │                    │
│              │ (includes projected   │                    │
│              │ rather than actual).  │                    │
│              │ Segment sum (A) is    │                    │
│              │ most grounded.        │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ ~48.5B annual txns    │                    │
│              │ ~1,538 TPS            │                    │
│              │ Range: 1,100-2,000    │                    │
│              │ Confidence: 67/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

### IoT Segment Breakdown

| Segment | Annual Txns (B) | Confidence | Primary Source |
|---------|----------------|------------|----------------|
| Toll collection | 18.5 | Medium-High | NPCI FASTag, E-ZPass, European ETC |
| Utility/smart meter payments | 12.0 | Medium | Utility company reports |
| Transit/ticketing | 8.0 | Medium | Contactless transit data |
| Vending/unattended | 4.5 | Low-Medium | Cantaloupe, USA Technologies |
| Connected vehicle | 3.0 | Low | Auto manufacturer estimates |
| Industrial IoT | 2.5 | Low | Industry estimates |

---

## 7. Definition Standards

In the Emerging sector, a **transaction** is defined per category:

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| IoT/M2M | Completed payment between/involving a machine/device | Telemetry data transmissions, device heartbeats, non-payment API calls |
| RWA Tokenisation | Confirmed on-chain transfer/trade of a tokenized real-world asset | Off-chain custody transfers, price oracle updates, governance votes |
| AI Agent Transactions | Completed payment by an autonomous agent for a service/resource | API calls without payment, agent-to-agent communication without value transfer |

**Key distinction:** IoT payments that use a linked credit card are counted here as IoT commerce events AND in Payments as card transactions. For the Big Number, only the incremental (non-card-rail) portion is added. RWA and AI agent transactions that occur on-chain are subsets of L1/L2 and are not added.

---

## 8. Known Gaps & Future Work

- **IoT payment rail granularity.** The 70-80% card/bank overlap is a rough estimate. A per-segment breakdown of payment methods would produce more precise de-duplication. Toll collection is primarily card-funded; utility payments are primarily direct debit; the overlap rates differ.
- **RWA platform coverage.** Only public blockchain RWA is tracked. Private tokenization platforms (JPMorgan Onyx, BNY Mellon, HSBC Orion) process tokenized asset transactions on permissioned ledgers that are not publicly visible.
- **AI agent trajectory.** At 0.66 TPS, this category is pre-market. The x402 protocol and emerging agent-commerce standards (A2A, MCP) may drive exponential growth. Quarterly monitoring is warranted to catch the inflection point.
- **Embedded finance boundary.** The taxonomy includes embedded payments, lending, and insurance under Emerging, but these categories have not yet been separately measured. They overlap heavily with Payments and Insurance sectors. Future runs should assess whether embedded finance warrants its own measurement track.
- **Machine wallet adoption.** As IoT devices get their own payment credentials (eSIM wallets, device-bound tokens), the overlap with card rails may decrease. Monitoring the shift from card-funded IoT to native machine payments is methodologically important.

---

*Emerging is the most forward-looking sector. IoT is already significant (~1,538 TPS before de-dup), while RWA and AI agents are at the base of their adoption S-curves. The methodology must balance current measurement rigor with readiness for rapid growth.*

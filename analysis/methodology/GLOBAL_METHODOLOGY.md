---
title: "Global Methodology"
parent: Methodology
grand_parent: Explore
nav_order: 1
---

# Universe of Finance — Global Methodology

> The master methodology document for measuring global financial transactions per second.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Mission Statement

The Universe of Finance (UoF) project measures the **total number of financial transactions processed globally per second**, across every instrument type, payment rail, and asset class. The goal is to produce a single, defensible, de-duplicated number — the "Big Number" — that represents the true throughput of the global financial system.

This is not a revenue study, a market capitalisation ranking, or a policy analysis. It is a **transaction count**: how many discrete financial events does the world produce per second?

The answer, as of March 2026: **approximately 70,700 TPS** (payment infrastructure basis) or **~71,200 TPS** (all economic events).

---

## 2. The Measurement Problem

Measuring global financial TPS is one of the hardest problems in financial data because:

**Inconsistent definitions.** A "transaction" means different things in different contexts. A card authorization, a clearing instruction, and a settlement entry are three distinct events triggered by a single consumer purchase. Different sources count at different lifecycle points, producing numbers that diverge by 3-15% for the same underlying activity.

**Overlapping categories.** A consumer buying shoes on Amazon via Apple Pay funded by a Visa card generates events in at least four categories (E-Commerce, Digital Wallets, Consumer Cards, Bank Settlement). Naive summation across categories produces a gross overcount of ~14%.

**Opaque markets.** China's mobile payment ecosystem (Alipay, WeChat Pay) processes an estimated 280 billion transactions annually, but detailed breakdowns are corporate-confidential. OTC derivatives markets are bilateral and unregistered. Cash economies are invisible to electronic counting.

**Geographic gaps.** The best data comes from jurisdictions with mandatory disclosure (US, EU, UK, Japan). For the other 180+ countries, estimates rely on GDP scaling, population proxies, and central bank reports of varying quality.

**Netting and batching.** A netting system that consolidates 1,000 payment instructions into 50 settlement obligations can be counted as either 1,000 or 50 transactions. Both are valid; conflating them is the error.

---

## 3. Our Approach: Triangulation-First

No single data source covers the global financial system. Our methodology uses **triangulation** — building multiple independent estimates for each category and reconciling the gap between them.

### Methodology Decision Tree

```
START: "How many [X] transactions happen annually?"
  │
  ├─ Is there a primary regulator/authority that publishes counts?
  │   ├─ YES → Use as anchor (e.g., Nilson Report for cards)
  │   │         └─ Cross-validate with operator filings
  │   └─ NO → Go to proxy estimation
  │
  ├─ Proxy Estimation
  │   ├─ Is total VALUE known?
  │   │   ├─ YES → Value ÷ avg transaction size = count
  │   │   │         └─ Sensitivity: avg txn size ±20% → count ±20%
  │   │   └─ NO → Go to bottom-up
  │   │
  │   └─ Bottom-Up
  │       ├─ Sum known operators (>50% coverage?)
  │       │   ├─ YES → Extrapolate remainder by market share
  │       │   └─ NO → Use population/GDP scaling from reference country
  │       │
  │       └─ Validate against top-down GDP ratio or per-capita benchmarks
  │
  └─ RECONCILE all methods
      ├─ Methods agree within 20%? → Confidence: HIGH
      ├─ Methods agree within 50%? → Confidence: MEDIUM
      └─ Methods disagree >50%?    → Confidence: LOW, investigate why
```

### Top-Down vs. Bottom-Up

**Top-down** starts from a macro anchor (global GDP, total consumer spending, total payment system throughput) and applies successive ratio filters to arrive at the category. It is best when macro data is reliable and the category is a well-defined fraction of a larger aggregate.

**Bottom-up** sums known operators, platforms, or systems and extrapolates for the uncovered tail. It is best when individual operators disclose transaction counts (e.g., Visa, Mastercard, UPI, individual exchanges).

The gap between top-down and bottom-up IS the finding. If they agree within 15%, we have a defensible estimate. If they diverge by 30%+, the divergence itself becomes the research question — it usually reveals a definitional mismatch, a coverage gap, or an overlap.

---

## 4. Transaction Definition Standard

### What Counts as a "Transaction"

For UoF purposes, a **transaction** is a single discrete financial event that represents either:
- A **payment**: money moving from one party to another
- A **trade**: an agreement to exchange financial instruments
- A **settlement**: the final discharge of an obligation between counterparties
- A **transfer**: the movement of a digital or financial asset between accounts

Each event is counted **once** at its canonical counting point, regardless of how many systems, messages, or intermediaries it passes through.

### The Three Lives of a Transaction

Every financial transaction has at least three lifecycle events. Which one we count depends on the category.

```
┌─────────────────────────────────────────────────────────────────┐
│                A SINGLE CONSUMER PURCHASE                       │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ AUTHORIZATION │    │   CLEARING   │    │  SETTLEMENT  │      │
│  │              │    │              │    │              │      │
│  │ Card tapped  │───>│ Instruction  │───>│ Funds move   │      │
│  │ at terminal  │    │ sent to      │    │ between      │      │
│  │              │    │ network      │    │ issuer and   │      │
│  │ Includes     │    │              │    │ acquirer     │      │
│  │ declines     │    │ ~97% of      │    │              │      │
│  │ (~3-5%)      │    │ auths        │    │ Netted:      │      │
│  │              │    │ proceed      │    │ 1000 txns →  │      │
│  │ Count: 100   │    │              │    │ 50 entries   │      │
│  │              │    │ Count: 97    │    │              │      │
│  │              │    │              │    │ Count: 50    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│                                                                 │
│  UoF Canonical Counting Points by Category:                     │
│  • Cards:           Clearing instruction (not auth, not settle) │
│  • Bank Transfers:  Initiated payment instruction               │
│  • Equity Markets:  Executed trade (matched order)              │
│  • Derivatives:     Executed contract                           │
│  • Digital Assets:  Confirmed on-chain transaction              │
│  • Settlement:      Settlement instruction (post-netting)       │
└─────────────────────────────────────────────────────────────────┘
```

### Why Clearing, Not Authorization or Settlement?

- **Authorization** overcounts by 3-5% because it includes declines and reversals
- **Settlement** undercounts by 50-95% because netting systems batch thousands of transactions into a few settlement entries
- **Clearing** best represents "one economic event" — the point at which a completed purchase enters the financial system as an obligation

For categories where clearing is not applicable (e.g., on-chain blockchain transactions), we count the **confirmed transaction** — the equivalent canonical event.

---

## 5. De-Duplication Framework

### Category Stack Diagram

Financial transactions exist in layers. Commerce layers sit on top of payment rails, which sit on top of settlement infrastructure. A single economic event can appear in multiple layers.

```
┌─────────────────────────────────────────────────────────┐
│ COMMERCE LAYERS (what people buy)                        │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│ │E-Commerce│ │  Gaming  │ │Government│ │Insurance │   │
│ │  57.5B   │ │  15.2B   │ │  31.6B   │ │   14B    │   │
│ │ 95% ↓    │ │ 70% ↓    │ │ 60% ↓    │ │ 90% ↓    │   │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
├─────────────────────────────────────────────────────────┤
│ CREDIT LAYERS (how purchases are financed)               │
│ ┌──────────┐                                             │
│ │   BNPL   │ 3.6× multiplier                            │
│ │  5.5B → 20B installment events                        │
│ └──────────┘                                             │
├─────────────────────────────────────────────────────────┤
│ PAYMENT RAILS (how money moves)                          │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│ │  Cards   │ │  Bank    │ │ Wallets  │ │   P2P    │   │
│ │  772.7B  │ │ Transfers│ │  620B    │ │  8.5B    │   │
│ │          │ │  484B    │ │          │ │          │   │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
├─────────────────────────────────────────────────────────┤
│ SETTLEMENT INFRASTRUCTURE (how it clears)                │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│ │   RTGS   │ │   CCP    │ │   CSD    │                 │
│ │  1,581M  │ │  netting │ │  1.4B    │                 │
│ └──────────┘ └──────────┘ └──────────┘                 │
└─────────────────────────────────────────────────────────┘
```

### Overlap Waterfall: Gross to Net TPS

```
Gross TPS (raw sum)    ████████████████████████████████  ~86,900
                       │
(-) UPI in both        ████████████████████████████████  ~81,450  -5,450 (172B counted twice)
    Wallets & Bank     │
(-) Card-rail wallets  ███████████████████████████████   ~80,180  -1,270 (40B Apple/Google/Samsung)
    (ApplePay etc.)    │
(-) E-Commerce on      ██████████████████████████████    ~78,500  -1,680 (95% rides on rails)
    existing rails     │
(-) P2P/Remittance     ██████████████████████████████    ~78,475  -25 (minor overlaps)
    overlaps           │
(-) Commerce layers    █████████████████████████████     ~70,741  -7,734 (gaming/govt/IoT
    on payment rails   │                                          on existing rails)
                        ▼
                       ════════════════════════════════
De-duplicated          █████████████████████████         ~70,741 TPS
```

### Overlap Rules

1. **Payment rails are base layers.** Cards (772.7B) and Bank Transfers (484B) are counted at face value. All other categories are measured for overlap against these base layers.

2. **Wallets de-duplicate against bank transfers and cards.** UPI (172B) is counted in Bank Transfers, not Wallets. Card-funded wallets (Apple Pay, Google Pay, Samsung Pay: ~40B) are subtracted from Wallets.

3. **Commerce layers de-duplicate against payment rails.** E-Commerce (95%), Gaming (70%), Government (60%), Insurance (90%), and IoT (75%) transactions ride on existing card/bank/wallet rails and are not added to the payment infrastructure total.

4. **BNPL is a credit layer.** The 5.5B BNPL purchases generate 20B installment events, but both the purchase and installments flow through card or bank rails. BNPL is not added to avoid double-counting.

5. **Settlement is downstream.** A stock trade counts in Equity Markets, and its resulting settlement counts in Securities Settlement. Both are real transactions on different infrastructure — they are NOT deduplicated against each other.

6. **Digital assets: on-chain is the base.** DeFi and Stablecoin transactions are subsets of L1/L2 on-chain transactions, not additive. CEX trades are off-chain and counted separately.

---

## 6. Confidence Scoring

Every category receives a confidence score from 0-100 based on four dimensions.

### Scoring Rubric

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Source Quality | 0-30 | Primary/regulatory data (25-30), industry reports (15-24), extrapolations (5-14), pure estimates (0-4) |
| Data Recency | 0-20 | <12 months (16-20), 1-2 years (10-15), 2-3 years (5-9), >3 years (0-4) |
| Triangulation | 0-25 | 3+ independent methods agree within 20% (20-25), 2 methods (10-19), single source (0-9) |
| Coverage | 0-25 | >90% market captured (20-25), 50-90% (10-19), <50% (0-9) |

### Source Confidence Matrix (Global Summary)

```
                    Source     Recency   Triang.    Coverage
                    ─────────  ────────  ─────────  ─────────
Consumer Cards      █████████░ █████████ ████████░░ ████████░░  91
ETD                 █████████░ █████████ ████████░░ ████████░░  88
Equity Markets      ████████░░ █████████ ████████░░ ████████░░  86
Interbank RTGS      ████████░░ █████████ ████████░░ ██████░░░░  82
Bank Transfers      ████████░░ ████████░ ████████░░ ██████░░░░  78
L1/L2 Blockchain    ███████░░░ █████████ ████████░░ ██████░░░░  76
Gov't Payments      █████░░░░░ ███████░░ ████░░░░░░ ████░░░░░░  50
Gaming Microtx      ███░░░░░░░ ████████░ ███░░░░░░░ ████░░░░░░  44
AI Agents           ██░░░░░░░░ ████████░ ██░░░░░░░░ ██░░░░░░░░  34
                    ─────────  ────────  ─────────  ─────────
```

### Confidence Bands

| Band | Score Range | Categories |
|------|------------|------------|
| High | 80-100 | Consumer Cards (91), ETD (88), Equity Markets (86), Interbank RTGS (82) |
| Medium-High | 60-79 | Bank Transfers (78), L1/L2 (76), Stablecoins (75), Securities Settlement (74), Commodities (74), and 7 others |
| Medium | 40-59 | Forex (58), Remittances (58), CEX (56), RWA (56), Game Sales (56), Gov't Payments (50), Microtx (44) |
| Low | 0-39 | AI Agents (34) |

**Median confidence across all 24 categories: 67/100** — solidly in the Medium-High band.

---

## 7. Limitations & Caveats

### What We Cannot Measure

- **Cash economies.** An estimated 18-20% of global consumer spending is cash-based. Cash transactions are invisible to electronic counting systems. This gap is largest in South Asia, Sub-Saharan Africa, and parts of Southeast Asia.

- **Informal transactions.** Hawala networks, informal lending circles, barter, and unrecorded person-to-person transfers are economically significant but unmeasurable.

- **Internal corporate transfers.** Intra-company fund movements, treasury management sweeps, and internal ledger entries are not counted. These are bookkeeping events, not market transactions.

- **On-us transactions.** When a payment stays within a single bank (payer and payee at the same institution), it may not appear in interbank clearing statistics. The Federal Reserve Payments Study estimates on-us transactions at 10-15% of total US non-cash payments.

### What We Intentionally Exclude

- **ATM balance inquiries** — information requests, not transactions (ATM cash withdrawals ARE counted)
- **Pre-authorizations** — temporary holds that do not represent completed purchases
- **Failed transactions** — declined cards, bounced checks, reverted on-chain transactions
- **Solana vote transactions** — consensus protocol events, not economic transactions (~35% of Solana's headline TPS)
- **MEV bot spam** — automated arbitrage transactions that inflate on-chain counts (~25% of Solana's non-vote TPS)
- **Message-level events** — a single ISO 20022 message may contain multiple transactions; we count transactions, not messages
- **Netting entries** — we count gross transactions (pre-netting), not the netted settlement obligations

### Structural Limitations

- **Data vintage.** Some categories rely on data that is 1-3 years old (notably BIS Triennial Survey for FX, published every 3 years). Growth rates are applied to forward-project, introducing compounding uncertainty.

- **Developed-market anchor bias.** The best data comes from the US, EU, UK, and Japan. Estimates for 180+ other countries rely on GDP/population scaling, which may not accurately reflect local financial system structure.

- **Definition harmonization.** Different central banks count the same instrument differently. The US Fed counts ACH "items" while the ECB counts SEPA "transactions" with different bundling rules, creating ~4% discrepancy for the same underlying flows.

- **Range, not point estimate.** The Big Number (~70,700 TPS) is a central estimate. The defensible range is **64,000-78,000 TPS** (payment infrastructure) or **65,000-80,000 TPS** (all economic events). Any single-number citation should be accompanied by this range.

---

*This methodology is versioned alongside the data. As category research improves, both the numbers and the methodology evolve together.*

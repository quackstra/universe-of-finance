---
title: "Sector: Digital Assets"
parent: Methodology
grand_parent: Explore
nav_order: 4
---

# Sector Methodology: Digital Assets

> How we measure cryptocurrency and blockchain transaction activity — 4 categories, ~3,515 de-duplicated TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

Digital Assets measures transaction activity across centralized crypto exchanges (off-chain), decentralized finance protocols (on-chain), stablecoin transfers, and base-layer blockchain transactions. At ~3,515 de-duplicated TPS, Digital Assets accounts for **5% of global financial TPS**.

The sector has a unique structural property: **DeFi and Stablecoins are subsets of L1/L2 on-chain transactions, not additive categories.** A Uniswap swap and a USDC transfer are both L1/L2 transactions. The correct de-duplication is CEX (off-chain, 3,100 TPS) + L1/L2 (on-chain, 415 TPS) = 3,515 TPS.

---

## 2. Sector-Specific Measurement Challenges

**Wash trading on CEX.** Centralized exchanges have historically inflated volume through wash trading. Estimates of fake volume range from 30% to 80% depending on methodology (Bitwise, Chainalysis, CoinGecko). Our 3,210 TPS figure applies a ~50% wash adjustment to reported volumes, which itself has ±30% uncertainty.

**Solana vote/spam filtering.** Solana's headline TPS (~4,000+) includes consensus vote transactions (~35% of total), failed transactions (~35% of non-vote), and MEV bot spam (~25% of successful non-vote). After filtering, Solana's genuine economic TPS is ~350-480. This filtering reduced the L1/L2 category from ~900 TPS to ~415 TPS.

**DeFi transaction definition.** A single DeFi operation can generate multiple on-chain transactions (approve + swap, or aggregator routing through 3 pools). We count confirmed on-chain transactions, not "DeFi operations," which means DeFi composability inflates the on-chain count relative to economic intent.

**Off-chain vs. on-chain boundary.** CEX trades are off-chain (internal ledger entries) and do not appear on any blockchain. Only deposits, withdrawals, and on-chain settlements touch L1/L2. This creates a clean boundary — CEX and L1/L2 do not overlap.

**Stablecoin noise.** Not all stablecoin transfers are "payments." Many are arbitrage, exchange rebalancing, or smart contract interactions. Filtering genuine payment-like transfers from noise is an unsolved problem.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume | Confidence | Overlap Status |
|---|----------|---------|--------------|------------|----------------|
| 1 | Centralised Crypto Exchanges | 3,210 | ~120B trades (wash-adjusted) | 56 (Medium) | Off-chain — no L1/L2 overlap |
| 2 | L1 & L2 Blockchain Transactions | 415 | ~13.1B txns | 76 (Medium-High) | Base on-chain layer |
| 3 | DeFi (Decentralised Finance) | *(subset)* | *(subset of L1/L2)* | 62 (Medium-High) | ~30-40% of L1/L2 |
| 4 | Stablecoins | 520 | *(subset of L1/L2)* | 75 (Medium-High) | ~15-25% of L1/L2 |

**De-duplicated sector total: ~3,515 TPS** (CEX 3,100 + L1/L2 415)

---

## 4. Cross-Category Overlap Rules

### Subset Structure

Digital Assets has a unique overlap structure: categories are not merely overlapping — they are **nested subsets**.

```
┌─────────────────────────────────────────────────────────┐
│  OFF-CHAIN (CEX)                                         │
│  ┌───────────────────────────────────────────┐          │
│  │ Centralised Exchange Trades               │          │
│  │ ~3,100 TPS (wash-adjusted)                │          │
│  │ Internal ledger entries — no blockchain    │          │
│  └───────────────────────────────────────────┘          │
│                                                          │
│  ON-CHAIN (L1/L2)                                        │
│  ┌───────────────────────────────────────────┐          │
│  │ L1 & L2 Blockchain Transactions           │          │
│  │ ~415 TPS (vote/spam filtered)             │          │
│  │                                            │          │
│  │  ┌─────────────┐  ┌──────────────┐        │          │
│  │  │    DeFi     │  │ Stablecoins  │        │          │
│  │  │  ~30-40%    │  │  ~15-25%     │        │          │
│  │  │  of L1/L2   │  │  of L1/L2    │        │          │
│  │  └─────────────┘  └──────────────┘        │          │
│  │                                            │          │
│  │  Remaining ~40-55%: native transfers,      │          │
│  │  NFT mints, bridge txns, other contracts   │          │
│  └───────────────────────────────────────────┘          │
│                                                          │
│  TOTAL: 3,100 + 415 = 3,515 TPS                         │
│  (DeFi and Stablecoins do NOT add — they are subsets)    │
└─────────────────────────────────────────────────────────┘
```

### Overlap Waterfall

```
Gross TPS (if naively summed)  ████████████████████████  ~4,145
                               │
(-) DeFi subset                ████████████████████████  ~4,145  -0
    (already in L1/L2)         │                         (DeFi TPS not additive)
                               │
(-) Stablecoin subset          ███████████████████████   ~3,625  -520
    (already in L1/L2)         │                         (Stablecoin TPS not additive)
                               │
(-) L1/L2 reclassified        ██████████████████████    ~3,515  -110
    (DeFi+Stable portion)      │                         (avoid counting L1/L2 twice)
                                ▼
                               ═══════════════════════
De-duplicated                  ██████████████████████    ~3,515 TPS
```

**Rule:** Count CEX + L1/L2. DeFi and Stablecoins are analytical views into the L1/L2 base, not separate transaction streams.

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Block Explorers     █████████░ ██████████ █████████░ ██████████
(Etherscan etc.)
DeFiLlama           ████████░░ ██████████ ████████░░ ████████░░
CoinGecko/CMC       ████████░░ ██████████ ██████░░░░ ███████░░░
L2Beat              ██████░░░░ ██████████ ████████░░ █████████░
Chainalysis         ██████░░░░ █████████░ ████████░░ ██████░░░░
Dune Analytics      ███████░░░ ██████████ ███████░░░ █████████░
Bitwise/Arca        ████░░░░░░ ████████░░ ███████░░░ ████░░░░░░
(wash studies)
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Primary anchors):** Block explorers (on-chain data is transparent and verifiable), DeFiLlama (DeFi protocol data)
**Tier 2 (Cross-validation):** L2Beat (L2 rollup data), CoinGecko/CoinMarketCap (CEX volumes), Dune Analytics (custom queries)
**Tier 3 (Adjustments):** Chainalysis (wash trading estimates), Bitwise (CEX volume integrity studies)

---

## 6. Sector Triangulation Approach

### Digital Assets Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [On-Chain Direct]     [Exchange Reports]  [Fee-Based]   │
│  Block explorer        Aggregate CEX       Total fees ÷  │
│  transaction counts    volume (adjusted)   avg fee =     │
│  + L2Beat rollup data                      implied txns  │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ 415 TPS  │         │ 3,100    │        │ 2,800-   │  │
│  │ on-chain │         │ TPS CEX  │        │ 3,400    │  │
│  │ (filtered│         │ (wash-   │        │ TPS CEX  │  │
│  │  L1/L2)  │         │ adjusted)│        │ (implied)│  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ On-chain is definitive│                    │
│              │ (verifiable).         │                    │
│              │ CEX Methods B & C     │                    │
│              │ agree within 10% —    │                    │
│              │ wash adjustment is    │                    │
│              │ the main uncertainty. │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ 3,515 TPS total       │                    │
│              │ Range: 2,500-4,500    │                    │
│              │ Confidence: 66/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

**On-chain (L1/L2):** High confidence (76/100). Block explorers provide verifiable, real-time data. The main uncertainty is Solana filtering methodology — different filter assumptions produce 350-480 TPS.

**Off-chain (CEX):** Medium confidence (56/100). The wash trading adjustment dominates uncertainty. A 30% wash assumption yields ~4,000 TPS; a 70% assumption yields ~2,000 TPS. Our central estimate uses ~50%.

---

## 7. Definition Standards

In Digital Assets, a **transaction** varies by context:

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| CEX | Executed trade (matched order on exchange order book) | Cancelled orders, open orders, internal transfers |
| L1/L2 Blockchain | Confirmed on-chain transaction (included in finalized block) | Failed/reverted transactions, vote transactions, pending mempool entries |
| DeFi | Confirmed on-chain contract interaction (swap, lend, stake) | Approval transactions counted separately, failed interactions |
| Stablecoins | Confirmed on-chain transfer of stablecoin tokens | Mint/burn (counted separately), zero-value transfers, smart contract internal moves |

**Key distinction:** On-chain data is uniquely transparent in finance — every transaction is publicly verifiable on the blockchain. This gives Digital Assets the highest potential data quality of any sector, offset by the noise-filtering challenge (vote txns, spam, wash trading).

---

## 8. Known Gaps & Future Work

- **CEX wash trading calibration.** The 50% wash adjustment is a rough central estimate. Per-exchange analysis using order book depth, bid-ask spread, and Benford's law tests would produce more defensible per-exchange adjustments.
- **L2 rollup aggregation.** L2Beat covers major rollups (Arbitrum, Optimism, Base, zkSync) but smaller L2s and app-chains are partially estimated. As L2 adoption grows, this gap widens.
- **Solana filter methodology.** Our vote/spam/MEV filtering reduced Solana from ~4,000 to ~350-480 TPS. The filter parameters (35% vote, 35% failed, 25% MEV) are based on sampled block analysis. Continuous monitoring would improve precision.
- **DeFi as subset measurement.** Stating DeFi as "30-40% of L1/L2" is approximate. Chain-specific analysis (Ethereum DeFi share vs. Solana DeFi share vs. Arbitrum DeFi share) would produce a more precise decomposition.
- **NFT and bridge transactions.** Currently included in L1/L2 but not broken out as separate analytical categories. As cross-chain activity grows, bridge transaction methodology may warrant its own category.
- **Stablecoin payment vs. speculation.** Not all stablecoin transfers are payments. Filtering genuine P2P/merchant transfers from arbitrage, rebalancing, and contract interactions would produce a "stablecoin payments TPS" distinct from "stablecoin activity TPS."

---

*Digital Assets is the most transparent sector (on-chain data) but also the noisiest (wash trading, spam, bot activity). The methodology challenge is filtering signal from noise, not finding data.*

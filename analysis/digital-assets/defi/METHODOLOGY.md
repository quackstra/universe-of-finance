---
title: "DeFi (Decentralised Finance) — Methodology"
parent: Digital Assets
grand_parent: Explore
nav_order: 102
---

# DeFi (Decentralised Finance) — Measurement Methodology

## Transaction Definition

- **What counts**: One on-chain interaction with a decentralised financial protocol — a DEX swap, lending deposit/withdrawal/borrow/repay, LP provision/removal, or perpetual futures trade settled on-chain
- **Counting point**: Smart contract execution included in a finalized block. Each DeFi interaction is an L1 or L2 blockchain transaction
- **Why this point**: DeFi transactions are smart contract events — they are on-chain and verifiable. DEX volume aggregators (DeFiLlama) count at the smart contract event level
- **Key ambiguities**:
  - **Multi-hop routing**: A single DEX swap may route through 2-5 liquidity pools (e.g., USDC → WETH → token via 2 Uniswap pools). This is 1 user transaction but generates 2+ swap events. DeFiLlama counts the volume at the final output level (not per-hop)
  - **MEV bot activity**: Sandwich attacks and arbitrage bots generate real on-chain transactions that inflate DEX volume. On Solana, sandwiched trades and MEV bots may account for 30-60% of DEX transaction COUNT. These are economically real (they extract value) but not "organic user" activity
  - **Lending lifecycle**: A single lending position generates multiple transactions: deposit, borrow, repay, withdraw, liquidation. Each is a separate DeFi transaction. A user maintaining a position for a year generates ~4-10 transactions per position
  - **TVL double-counting**: TVL is a stock metric, not a flow metric. Recursive borrowing (deposit ETH → mint stETH → deposit stETH in Aave → borrow USDC → LP in Uniswap) means the same dollar is counted 3-5x in TVL. TVL does NOT inform our transaction count

## Triangulation Approach

### Method A: DeFiLlama DEX Volume Aggregation

- **Source**: DeFiLlama DEX volume rankings — $1.76T spot DEX volume in 2024
- **Value**: At estimated average trade size of ~$500-1,500 → ~3.2-9.6M DEX trades/day → plus lending/staking transactions → total DeFi ~5-15M txns/day
- **Strengths**: DeFiLlama is the industry standard for DeFi data. Aggregates directly from smart contract events across 200+ protocols and 80+ chains
- **Weaknesses**: Reports VOLUME not transaction COUNT. Average trade size varies enormously (Solana memecoin: ~$50; Ethereum whale: ~$50K). No single source publishes global DeFi transaction counts

### Method B: Chain-Level DeFi Transaction Share

- **Source**: DeFi transactions as estimated percentage of total L1/L2 transactions per chain
- **Value**: If DeFi = ~40-50% of L1/L2 filtered transactions (~35.9M/day) → ~14-18M DeFi txns/day
- **Strengths**: Top-down cross-check using the L1/L2 total as ceiling
- **Weaknesses**: The DeFi share percentage is itself estimated. Solana's DeFi share is unclear because of memecoin/pump.fun activity (is this "DeFi" or "speculation"?)

### Method C: Protocol-Level Aggregation

- **Source**: Major protocol daily users × avg transactions per user. Uniswap ~500K daily unique traders, Aave ~50K daily users, Raydium ~200K daily traders, etc.
- **Value**: Cross-check for order-of-magnitude. ~1M daily unique DeFi users × ~5-10 transactions per active session → ~5-10M DeFi txns/day
- **Strengths**: Grounds the estimate in observable user behavior
- **Weaknesses**: "Unique users" = unique addresses (1 human may use 5+ wallets). Sybil farming inflated 2024 user counts on many L2s

```
┌─────────────────────────────────────────────────────────────┐
│           DeFi VOLUME vs COUNT ESTIMATION                     │
│                                                               │
│  DeFiLlama        Chain Share       Protocol Users            │
│  [volume-based]   [top-down %]      [bottom-up users]        │
│  ┌──────────┐    ┌──────────┐     ┌──────────┐              │
│  │$1.76T spot│    │~40-50% of│     │~1M daily │              │
│  │ + $2.4T  │    │ 35.9M/day│     │ unique   │              │
│  │ perps    │    │L1/L2 txns│     │ traders  │              │
│  │→ 5-15M/d│    │→14-18M/d │     │ × 5-10   │              │
│  └────┬─────┘    └────┬─────┘     └────┬─────┘              │
│       │               │                │                     │
│       └───────────────┼────────────────┘                     │
│                       ▼                                      │
│              ┌──────────────────┐                            │
│              │  CONVERGENCE     │                            │
│              │  ~10-15M DeFi    │                            │
│              │  txns/day        │                            │
│              │  (~120-175 TPS)  │                            │
│              │  Confidence: Low │                            │
│              └──────────────────┘                            │
│                                                               │
│  Note: No single source publishes a DeFi transaction count.  │
│  All approaches are estimates with wide uncertainty bands.    │
└─────────────────────────────────────────────────────────────┘
```

## Reconciliation

Three approaches converge on ~10-15M DeFi transactions/day (~120-175 TPS). This is consistent with DeFi representing ~40-50% of total on-chain activity. The volume-based approach gives the widest range because average trade size assumptions dominate. The chain-share approach provides the tightest bound but depends on an estimated DeFi percentage. The protocol-user approach is the most grounded but may undercount due to long-tail protocols.

Note: DeFi transaction count is NOT directly published by any source. This is one of the lowest-confidence estimates in the Digital Assets sector.

## Key Adjustments

### MEV/Bot Transaction Decomposition

```
DeFi Transaction Mix (Estimated)
═══════════════════════════════════════════════════

Total DeFi transactions/day:    ~12M (central estimate)
  │
  ├── Organic user swaps        ████████████       ~5M  (42%)
  │   Human-initiated DEX trades
  │
  ├── Arbitrage bots            █████████          ~3.5M (29%)
  │   Cross-DEX, cross-chain arbitrage
  │   (economically real — improve prices)
  │
  ├── MEV sandwich attacks      ███                ~1.5M (12%)
  │   Front-running user trades
  │   (parasitic but real on-chain activity)
  │
  ├── Lending/staking lifecycle ███                ~1.2M (10%)
  │   Deposits, borrows, repays,
  │   liquidations, staking/unstaking
  │
  └── Other (governance, etc.)  █                  ~0.8M  (7%)
      Votes, protocol upgrades,
      NFT-related DeFi

"Genuine human DeFi TPS" ≈ ~5M/day ≈ ~58 TPS
(vs ~12M total DeFi ≈ ~140 TPS)
```

The distinction between "organic user" and "bot" activity in DeFi is philosophically fraught. Arbitrage bots improve market efficiency and close price gaps — they perform a genuine economic function. Sandwich bots extract value parasitically but are real transactions. Our primary figure counts ALL DeFi transactions regardless of initiator, consistent with how traditional markets count HFT trades.

### DEX-to-CEX Ratio as Structural Metric

The DEX-to-CEX spot volume ratio grew from ~3% (2020) to ~10% (2024) to ~20% (Jan 2025). This structural shift is the most important trend in crypto market structure:

```
DEX Share of Crypto Spot Trading
═══════════════════════════════════════

2020  ██                                    ~3%
2021  ███                                   ~5%
2022  █████                                 ~7%
2023  ███████                               ~9%
2024  ████████████                          ~10%
2025  ████████████████████                  ~20%  (Jan 2025)
      ──────────────────────────────────────
      0%        10%        20%        30%

Drivers: FTX collapse trust shift, L2 fee reduction,
Solana memecoin boom, improved DEX UX (Jupiter, 1inch)
```

## Overlap Analysis

```
DeFi Overlap Map — Full Subset of L1/L2
═══════════════════════════════════════════════════

L1/L2 blockchain txns (filtered)  ██████████████████████  ~35.9M/day
  │
  │  CONTAINS:
  │
  ├── DeFi transactions (this)    █████████████           ~12M/day (33-50%)
  │     │
  │     ├── overlaps Stablecoins  ████████                ~30-40% of DeFi
  │     │   (USDC/USDT in swaps)                          involves stablecoins
  │     │
  │     └── overlaps CEX          ░ (none)                DEX ≠ CEX
  │
  ├── Non-DeFi on-chain           █████████               ~24M/day (50-67%)
  │   (simple transfers, NFTs,
  │    gaming, governance, spam)
  │
  └── Total L1/L2                 ██████████████████████  ~35.9M/day

CRITICAL: DeFi is a FULL SUBSET of L1/L2.
For Digital Assets sector totals:
  Sector total = L1/L2 (filtered) + CEX
  NOT: L1/L2 + DeFi + Stablecoins + CEX (would triple-count)
```

- **Full subset of L1/L2**: Every DeFi transaction is an on-chain transaction. DeFi ~= 33-50% of L1/L2 by count
- **Partial overlap with Stablecoins**: ~30-40% of DeFi transactions involve stablecoins (DEX swaps, lending)
- **Zero overlap with CEX**: DEX and CEX are mutually exclusive venues. A trade on Uniswap and a trade on Binance are never the same transaction

## Coverage Assessment

```
Protocol Type      Coverage  Source              Notes
─────────────────  ──────── ─────────────────── ──────────────────
DEX spot (major)   █████████ DeFiLlama           Uniswap, Raydium, etc.
DEX perps          ████████░ DeFiLlama perps     Hyperliquid, dYdX, Jupiter
Lending/borrowing  ████████░ DeFiLlama lending   Aave, Compound, MakerDAO
Liquid staking     ████████░ DeFiLlama staking   Lido, Rocket Pool
DEX aggregators    ███████░░ Various              Jupiter, 1inch, Paraswap
Long-tail DeFi     ████░░░░░ Partially tracked    Hundreds of small protocols
─────────────────  ──────── ─────────────────── ──────────────────
By volume: ~90% covered (top 20 protocols dominate)
By count: ~75% covered (long tail of micro-protocols)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
DeFiLlama (volume)  █████████  █████████ █████████░  ████████░░
CoinGecko DEX       ████████░  █████████ ████████░░  ██████░░░░
Protocol dashboards ██████░░░  █████████ ████████░░  ████████░░
Dune Analytics      ██████░░░  █████████ ██████░░░░  ██████████
MEV trackers        ████░░░░░  ████████░ ██████░░░░  ████████░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    72/100     90/100    78/100      76/100
```

- **Score**: 62/100
- **Key drivers of uncertainty**:
  - No source publishes DeFi transaction COUNTS — everything is derived from volume or estimated from chain data
  - MEV/bot share of DeFi transactions (30-60% by count?) is the single biggest unknown for "genuine user" TPS
  - Solana memecoin activity (pump.fun) may or may not be "DeFi" — definitional boundary is unclear
  - Sybil/airdrop farming inflated 2024 DeFi metrics (zkSync, Starknet saw 40-60% activity drops post-airdrop)
  - TVL (the most common DeFi metric) tells us nothing about transaction frequency — $140B TVL with 12M txns/day could also be $50B TVL with 12M txns/day
  - Perp DEX volume ($2.4T) is notional — leverage inflation distorts the economic significance
- **High-confidence elements**: DEX spot volume ($1.76T, on-chain verifiable); TVL ($140B, on-chain); DEX-to-CEX ratio (~10%); protocol market share

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: DeFi category created |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation with MEV decomposition |

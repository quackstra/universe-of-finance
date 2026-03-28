# L1 & L2 Blockchain Transactions — Measurement Methodology

## Transaction Definition

- **What counts**: One on-chain transaction settled on a public, permissionless blockchain. The unit varies by architecture:
  - **Bitcoin**: One UTXO transaction (may contain multiple inputs/outputs)
  - **Ethereum/EVM**: One state transition triggered by an EOA or contract
  - **Solana**: One transaction (may contain multiple instructions)
- **Counting point**: Inclusion in a finalized block (Bitcoin: 1 confirmation; Ethereum: finalized slot; Solana: confirmed slot)
- **Why this point**: On-chain data is immutable and verifiable. Block explorers and indexers provide exact counts. This is the one category where the raw data is mathematically provable
- **Key ambiguities**:
  - **Solana vote transactions**: Solana's consensus mechanism requires validators to submit vote transactions (~60% of total). These are protocol overhead, not user activity. Including votes: ~60M/day; excluding votes: ~24M/day. Our filtered estimate removes votes, failed txns, and MEV spam
  - **Failed/reverted transactions**: Ethereum and Solana count failed transactions in their totals. On Solana, revert rates peaked at 75.7% of non-vote txns (Apr 2024). Failed transactions consume resources but have no economic effect
  - **Internal transactions**: Ethereum contract-to-contract calls generate internal transactions NOT counted in the headline tx count (only the initiating EOA transaction counts)
  - **L2 batch compression**: L2 rollups batch hundreds of transactions into a single L1 data post. We count the L2 transactions (not the L1 batch posts)

## Triangulation Approach

### Method A: Chain-by-Chain Block Explorer Aggregation

- **Source**: Etherscan (Ethereum), Blockchain.com (Bitcoin), Solscan (Solana), L2Beat (rollups), BitInfoCharts (BNB Chain)
- **Value**: ~70-90M/day raw (25-30B/year); ~35.9M/day filtered (13.1B/year)
- **Strengths**: On-chain data is verifiable and immutable. Block explorers provide exact daily counts
- **Weaknesses**: Each chain counts differently (UTXO vs account model vs instruction model). Aggregation is manual. Smaller chains/L2s may be undercounted

### Method B: Solana-Filtered Model (Run 3)

- **Source**: Solana raw ~60M/day → remove votes (~60%) → remove failed (~30% of remaining) → remove MEV bots (~15% of remaining) → ~13-24M "genuine user" txns/day
- **Value**: Reduces combined TPS from ~800-1,000 (raw) to ~350-480 (filtered)
- **Strengths**: Uses Solana's native vote/non-vote classification + reverted tx rate data + Jito/Helius MEV reports
- **Weaknesses**: MEV bot identification is probabilistic (program ID matching). The boundary between "bot" and "user" is fuzzy — arbitrage bots perform a genuine economic function

### Method C: Value-Weighted Cross-Check

- **Source**: Bitcoin ~$3.5T annual value, Ethereum L1 ~$2.5T, Solana ~$400B+
- **Value**: Economic significance per transaction varies 1000x+ across chains. Bitcoin: ~$7K/tx; Ethereum L1: ~$6K/tx; Solana: ~$8/tx
- **Strengths**: Provides economic grounding — prevents overweighting high-count, low-value chains
- **Weaknesses**: Value transferred includes self-transfers, bridge movements, and treasury operations

```
┌─────────────────────────────────────────────────────────────┐
│         SOLANA VOTE/SPAM FILTER PIPELINE                      │
│                                                               │
│  Solana raw transactions: ~60M/day                            │
│  ┌──────────────────────────────────────────────────┐        │
│  │ ████████████████████████████████████████████████  │ 60M    │
│  └───────────────────────┬──────────────────────────┘        │
│                          ▼                                    │
│  ┌──────────────────────────────────────────────────┐        │
│  │ FILTER 1: Remove Vote Transactions (~60%)         │        │
│  │ Validator consensus votes = protocol overhead     │        │
│  │ ████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░  │ →24M   │
│  └───────────────────────┬──────────────────────────┘        │
│                          ▼                                    │
│  ┌──────────────────────────────────────────────────┐        │
│  │ FILTER 2: Remove Failed/Reverted (~30% of rem.)   │        │
│  │ Peak: 75.7% revert rate in Apr 2024               │        │
│  │ Average: ~30% of non-vote fail                    │        │
│  │ ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │ →17M   │
│  └───────────────────────┬──────────────────────────┘        │
│                          ▼                                    │
│  ┌──────────────────────────────────────────────────┐        │
│  │ FILTER 3: Remove MEV Bots (~15% of remainder)     │        │
│  │ Sandwich attacks, arb bots (Jito/Helius data)     │        │
│  │ ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │ →14M   │
│  └───────────────────────┬──────────────────────────┘        │
│                          ▼                                    │
│  ┌──────────────────────────────────────────────────┐        │
│  │ FILTERED SOLANA: ~13-24M genuine txns/day         │        │
│  │ (central estimate: ~14M)                          │        │
│  │ ████████████                                      │        │
│  └──────────────────────────────────────────────────┘        │
│                                                               │
│  Combined filtered TPS (all chains):                          │
│  Solana ~162 + Ethereum L1 ~13.5 + L2s ~166 + BTC ~5.8       │
│  + BNB ~40 + others ~28 = ~415 TPS                           │
│  Range: 350-480 TPS                                           │
└─────────────────────────────────────────────────────────────┘
```

## Reconciliation

Raw blockchain data provides exact transaction counts — the question is what to count. The raw aggregate (~800-1,000 TPS) is verifiable but misleading because it includes Solana vote transactions, failed transactions, and MEV bot activity that inflate the number by ~2x. The filtered estimate (~415 TPS, range 350-480) removes these non-economic transactions and is used as the primary figure. The filter methodology is documented in workings/solana-filter.md.

## Key Adjustments

### Cross-Architecture Normalization

Different blockchain architectures count transactions differently:

| Chain | Architecture | What is "1 transaction" | Inflation factor |
|-------|-------------|------------------------|------------------|
| Bitcoin | UTXO | 1 UTXO spend (may consolidate inputs/outputs) | 1x (conservative) |
| Ethereum | Account | 1 state transition from EOA | 1x (standard) |
| Solana | Transaction + Instructions | 1 tx may contain multiple instructions | 1-5x vs ETH equivalent |
| L2 Rollups | Varies | 1 L2 tx = 1 state transition (posted in batches to L1) | 1x per L2 tx |

Solana's instruction model means a single "transaction" can perform 5+ operations that would each be separate transactions on Ethereum. This makes raw cross-chain comparison misleading. We count at the transaction level (not instruction level) for consistency.

### L2 Counting Convention

L2 rollups batch transactions for L1 submission. We count:
- Each individual L2 transaction (at the sequencer level) = 1 transaction
- NOT the L1 batch post (which is 1 L1 transaction containing 100-1000+ L2 txns)
- L2 transactions are NOT additive to L1 — they are separate, though the L1 batch post IS counted in the L1 total

## Overlap Analysis

```
L1/L2 Blockchain — Superset Relationship
═══════════════════════════════════════════════════

L1/L2 on-chain transactions   ██████████████████████  13.1B/year
  │                                                    (filtered)
  │
  │  CONTAINS as subsets:
  │
  ├── DeFi transactions        ████████████            est. ~40-50%
  │   (DEX swaps, lending,                             of L1/L2 by count
  │    LP actions)
  │
  ├── Stablecoin transfers     ██████████              est. ~30-40%
  │   (USDT, USDC on-chain                            of L1/L2 by count
  │    movements)
  │
  └── Native transfers         ████                    est. ~15-25%
      (ETH/BTC/SOL sends,                             simple value transfer
       NFT transfers, etc.)

CRITICAL: DeFi + Stablecoins are SUBSETS, not additive.
A Uniswap USDC→ETH swap counts as:
  - 1 L1/L2 transaction (here)
  - 1 DeFi transaction (DeFi capsule)
  - 1 stablecoin transfer (Stablecoins capsule)
DO NOT SUM ACROSS CAPSULES.
```

- **DeFi and Stablecoins are full subsets**: Every DeFi transaction and every stablecoin transfer is an L1 or L2 blockchain transaction. The Digital Assets sector total = L1/L2 + CEX (no double-count because CEX is off-chain)
- **CEX is NOT a subset**: CEX trades are off-chain. Zero overlap
- **Cross-chain bridge transactions**: A bridge transfer generates transactions on BOTH the source and destination chains. This means one economic transfer = 2+ on-chain transactions. We count each chain's transactions separately (no deduplication)

## Coverage Assessment

```
Chain               Coverage  Source           Notes
─────────────────── ──────── ──────────────── ──────────────────
Bitcoin             █████████ Blockchain.com   Exact, immutable
Ethereum L1         █████████ Etherscan        Exact, immutable
Solana              ████████░ Solscan/Helius   Vote filtering needed
Base (L2)           ████████░ L2Beat/Basescan  Sequencer data
Arbitrum (L2)       ████████░ L2Beat/Arbiscan  Sequencer data
BNB Chain           ████████░ BscScan          Some spam inflation
Optimism (L2)       ████████░ L2Beat           Sequencer data
Other L2s/L3s       ████░░░░░ L2Beat partial   Dozens untracked
Alt L1s (Sui, etc.) ███░░░░░░ Individual       Fragmented coverage
─────────────────── ──────── ──────────────── ──────────────────
By volume: ~90% of transactions on tracked chains
By chain count: ~60% of chains tracked (long tail untracked)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Etherscan/Bitcoin   █████████  █████████ ██████████  ██████████
L2Beat              ████████░  █████████ █████████░  ████████░░
Solscan/Helius      ████████░  █████████ ████████░░  ████████░░
BitInfoCharts       ██████░░░  █████████ ██████░░░░  ██████░░░░
Chain-specific      ████░░░░░  █████████ ████████░░  ██████░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    78/100     92/100    84/100      82/100
```

- **Score**: 76/100
- **Key drivers of uncertainty**:
  - Solana vote/failed/MEV filtering is the single biggest methodological choice — it reduces Solana's contribution by ~75% and combined TPS by ~50%
  - "What is a meaningful transaction?" is inherently subjective. Bitcoin's ~500K high-value txns/day and Solana's 60M mixed-quality txns/day are not comparable units
  - L2/L3 fragmentation means dozens of small rollups are untracked
  - Cross-chain bridge double-counting inflates totals by an unmeasured amount
  - Historic data (pre-2022) is rough — no standardized cross-chain aggregator existed
- **High-confidence elements**: Bitcoin and Ethereum L1 counts are mathematically exact and publicly verifiable. On-chain data is the most transparent in all of finance

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: L1/L2 category created |
| 2026-03-27 | Solana filter | Run 3: Vote/failed/MEV filtering; TPS revised from ~800-1000 to ~415 |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

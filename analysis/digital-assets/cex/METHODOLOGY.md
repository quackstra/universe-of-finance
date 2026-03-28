# Centralised Crypto Exchanges (CEX) — Measurement Methodology

## Transaction Definition

- **What counts**: One matched trade on a centralised exchange order book — a buy order matched against a sell order for any crypto asset (spot or derivative)
- **Counting point**: Internal matching engine execution. CEX trades are off-chain — they occur on the exchange's internal database, NOT on any blockchain
- **Why this point**: CEX order matching is the crypto equivalent of an exchange trade execution. Unlike on-chain data, CEX trade counts are NOT directly verifiable
- **Key ambiguities**:
  - **No exchange publishes trade counts**: This is the fundamental measurement problem. All CEXs report dollar VOLUME, not trade COUNT. Our entire TPS estimate is derived from volume / assumed average trade size
  - **Wash trading**: Artificial volume inflates reported numbers. Even after CoinGecko trust-score filtering, an estimated 15-45% of volume on individual exchanges may be wash-traded
  - **Derivatives notional**: A 100x leveraged perpetual futures trade on $100 collateral registers as $10,000 in volume. Derivatives volume ($58.5T) is notional, not economic
  - **Zero-fee pair inflation**: Binance's zero-fee BTC pairs generate volume that may be genuine incentivised trading OR wash trading. This ambiguity alone affects ~15% of total spot volume

## Triangulation Approach

### Method A: Volume / Average Trade Size (Raw)

- **Source**: CoinGecko — $77.3T combined annual volume (spot $18.83T + derivatives $58.5T)
- **Value**: $77.3T / 365 days / $605 avg trade size ≈ ~350M trades/day ≈ ~4,050 TPS (unadjusted)
- **Strengths**: Uses industry-standard volume data from CoinGecko's top-15 "trusted" exchanges
- **Weaknesses**: Average trade size ($605) is assumed from Coinbase trade data extrapolation; actual sizes vary dramatically by exchange and product

### Method B: Tiered Wash Trading Model

- **Source**: Academic research (NBER/Yale, CEPR), industry reports (Bitwise, Kaiko, Forbes/BTI), regulatory data
- **Value**: 25% blended wash trading reduction → ~3,040 TPS (range: 2,685-3,275)
- **Methodology**: Exchanges segmented into 3 tiers:
  - Tier 1 (Regulated: Coinbase, Kraken, Upbit): 15% of volume, 3.5% wash
  - Tier 2 (Semi-regulated: Binance, OKX, Bybit): 55% of volume, 20% wash
  - Tier 3 (Lower-tier: HTX, KuCoin, Gate.io): 30% of volume, 45% wash
- **Strengths**: Principled per-tier adjustment based on regulatory status. Narrows confidence interval from 1,250-wide to 590-wide
- **Weaknesses**: Tier-level percentages are themselves uncertain. Tier 2 (especially Binance at 39% spot share) is the most impactful variable

### Method C: Regional Wash Trading Model (Primary)

- **Source**: Geographic decomposition using Chainalysis Geography Report, regional regulatory data, and per-region wash estimates
- **Value**: 20.6% blended wash trading reduction → ~3,210 TPS (range: 2,890-3,450)
- **Methodology**: 8 geographic regions with region-specific wash rates based on regulatory environment

```
┌───────────────────────────────────────────────────────────┐
│            CEX WASH TRADING FILTER PIPELINE                 │
│                                                             │
│  REPORTED VOLUME                                            │
│  $77.3T combined ($18.83T spot + $58.5T derivatives)        │
│  ┌──────────────────────────────────────────────────┐      │
│  │ Reported ~4,050 TPS (unadjusted)                  │      │
│  └───────────────────────┬──────────────────────────┘      │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────┐      │
│  │ STEP 1: CoinGecko Trust Filter (pre-applied)      │      │
│  │ Removes worst-offender exchanges from top-15 list │      │
│  │ Estimated effect: already removes ~30-50%          │      │
│  │ of total global crypto volume                      │      │
│  └───────────────────────┬──────────────────────────┘      │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────┐      │
│  │ STEP 2: Regional Wash Model                       │      │
│  │                                                    │      │
│  │ US (8%): 2% wash          ████████████████████    │      │
│  │ Korea (7%): 5% wash       ████████████████████    │      │
│  │ Japan/SG/HK (6%): 3%     ████████████████████    │      │
│  │ Europe (10%): 5% wash     ████████████████████    │      │
│  │ China offshore (25%): 35% █████████████░░░░░░░    │      │
│  │ ME/Africa (15%): 30%      ██████████████░░░░░░    │      │
│  │ LatAm (10%): 15% wash    ██████████████████░░    │      │
│  │ SEA/Oceania (12%): 20%   ████████████████░░░░    │      │
│  │ Other (7%): 35% wash     █████████████░░░░░░░    │      │
│  │                                                    │      │
│  │ Blended: 20.6% reduction                          │      │
│  └───────────────────────┬──────────────────────────┘      │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────┐      │
│  │ STEP 3: Cross-Check with Tier Model               │      │
│  │ Tier model gives 25% blended → 3,040 TPS         │      │
│  │ Regional model gives 20.6% → 3,210 TPS           │      │
│  │ Convergence within ~170 TPS (5%)                  │      │
│  └───────────────────────┬──────────────────────────┘      │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────┐      │
│  │ FINAL: ~3,210 TPS (regional model primary)        │      │
│  │ Range: 2,890 - 3,450 TPS                          │      │
│  │ Confidence: Medium-Low                             │      │
│  └──────────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────────┘
```

## Reconciliation

The regional model (3,210 TPS) and tier model (3,040 TPS) converge within ~5%, providing increased confidence in the ~3,000-3,200 range. The regional model is preferred because it decomposes by geography (where regulatory environment drives wash trading incentives) rather than by exchange tier (which is more subjective). Both models agree that the unadjusted ~4,050 TPS overstates genuine activity by 20-25%.

## Key Adjustments

### Wash Trading Research Summary

| Study | Year | Finding | Relevance |
|-------|------|---------|-----------|
| Bitwise SEC Filing | 2019 | 95% of unregulated volume is suspect | Calibrates Tier 3 |
| NBER/Yale (Cong et al.) | 2022 | 70%+ on unregulated exchanges | Academic benchmark |
| CEPR (Kocenda et al.) | 2024 | 53.4% on "unregulated Tier 1" | Calibrates Tier 2 |
| Forbes/BTI | 2022 | 51% of Bitcoin volume fake | Cross-check |
| Kaiko | 2024 | HTX flagged; algorithmic patterns | Exchange-specific evidence |
| Chainalysis | 2025 | $2.57B DEX wash (0.035%) | DEX comparison |

### Sensitivity: Tier 2 Wash Trading (Binance Effect)

Binance holds 39% of spot market share. Moving Tier 2 wash estimate by 10 percentage points shifts the entire adjusted TPS by ~370:

```
Tier 2 wash = 10%  →  adjusted TPS ≈ 3,410
Tier 2 wash = 20%  →  adjusted TPS ≈ 3,040  (central)
Tier 2 wash = 30%  →  adjusted TPS ≈ 2,670
```

This single variable dominates the uncertainty. Post-2023 regulatory pressure (Binance $4.3B DOJ settlement) may have reduced wash trading, but no post-settlement audit data exists.

## Overlap Analysis

```
CEX Overlap with Other Digital Assets Categories
═══════════════════════════════════════════════════

CEX trades                   ██████████████████████  ~3,210 TPS
  │
  │  CEX trades are OFF-CHAIN
  │  (internal order book matching)
  │
  │  ZERO overlap with:
  ├── L1/L2 blockchain txns   (on-chain only)
  ├── DeFi transactions        (smart contract only)
  └── Stablecoin transfers     (on-chain only)

Only overlap: deposits/withdrawals
  CEX deposit = 1 on-chain tx (counted in L1/L2)
  CEX withdrawal = 1 on-chain tx (counted in L1/L2)
  But the CEX TRADE itself is off-chain → no double-count
```

- **Zero double-counting with L1/L2**: CEX order book matches are settled on internal databases, not blockchains. This is the cleanest boundary in the Digital Assets sector
- **Deposits/withdrawals**: User deposits and exchange withdrawals touch the blockchain and appear in L1/L2 counts. But these are custodial transfers, not trades — they are NOT counted as CEX trades

## Coverage Assessment

```
Exchange Tier       Coverage  Source              Notes
─────────────────── ──────── ─────────────────── ──────────────────
Tier 1 (regulated)  █████████ 10-K filings        Coinbase audited
Tier 2 (semi-reg)   ████████░ CoinGecko trust     Post-settlement data
Tier 3 (lower-tier) ██████░░░ CoinGecko trust     Wash trading uncertain
Excluded exchanges  ░░░░░░░░░ Not in top-15       Likely >50% fake
─────────────────── ──────── ─────────────────── ──────────────────
Volume coverage: ~85-90% of "trusted" global volume
Trade count: 0% directly observed (no exchange publishes counts)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
CoinGecko Volume    ████████░  █████████ ████████░░  ████████░░
Coinbase 10-K       ███░░░░░░  █████████ ██████████  ████████░░
Wash Trading Lit.   ████████░  ██████░░░ ████████░░  ████░░░░░░
Kaiko Market Data   ████████░  █████████ ████████░░  ██████████
Regional Reg Data   ██████░░░  ████████░ ████████░░  ████░░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    68/100     86/100    78/100      72/100
```

- **Score**: 56/100
- **Key drivers of uncertainty**:
  - No exchange publishes trade counts — the entire TPS figure is derived from volume / assumed trade size
  - Wash trading estimates span 15-45% per tier/region, creating a wide uncertainty band
  - China offshore segment (25% of volume, 35% wash) is the primary uncertainty driver
  - Derivatives volume is notional — leverage inflation means $58.5T derivatives may represent far less economic activity
  - Crypto volumes are radically cyclical (7x range in 5 years) — any snapshot is cycle-dependent
- **One data point that would transform confidence**: If Coinbase published daily trade counts alongside dollar volume in its 10-K, we could calibrate average trade size for a regulated exchange and reduce the confidence interval by ~50%

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: CEX category created |
| 2026-03-27 | Tiered wash model | Run 4: Three-tier wash trading filter |
| 2026-03-28 | Regional wash model | Run 5: Geographic decomposition; primary model changed |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

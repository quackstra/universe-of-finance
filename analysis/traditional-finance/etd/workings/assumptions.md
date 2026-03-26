# Exchange-Traded Derivatives — Assumptions

> All assumptions documented with rationale and sensitivity notes.

## Definition Assumptions

| # | Assumption | Rationale | Impact if Wrong |
|---|-----------|-----------|-----------------|
| A1 | "Transaction" = one contract traded | FIA and WFE both count contracts; this is the industry standard | If counting individual legs of spreads, volume would be ~1.3-1.5x higher |
| A2 | Exchange-traded only; excludes OTC | Clear regulatory distinction; ETD = standardised, centrally cleared | OTC derivatives are 5-10x larger by notional; not comparable by volume |
| A3 | Includes all asset classes | Equity, IR, FX, commodity, ETF, crypto (if on regulated exchange) | Some sources exclude crypto ETD; impact <0.5% of total |
| A4 | FIA as primary volume source over WFE | FIA covers 85 exchanges (broader); WFE limited to members | Using WFE would reduce 2024 total by ~12% (180B vs 205B) |

## TPS Calculation Assumptions

| # | Assumption | Value Used | Range | Sensitivity |
|---|-----------|------------|-------|-------------|
| T1 | Trading days per year | 252 | 250-255 | ±1% on TPS |
| T2 | Effective global trading hours per day | 21.6h | 16-24h | ±20% on TPS |
| T3 | Volume distributed evenly across trading hours | Uniform | Reality: concentrated around opens/closes | Peak TPS could be 2-3x higher during opening hours |
| T4 | Peak-to-average ratio | 6x | 4-10x | ±40% on peak TPS estimate |
| T5 | India expiry-day volume concentration | 3-6x normal | Based on FIA reporting | Higher concentration = higher peak TPS |

## Historical Data Assumptions

| # | Assumption | Impact |
|---|-----------|--------|
| H1 | 2022 total derived from Statista (futures 29.32B + options 54.53B = 83.85B) | FIA's own report may differ slightly; ±5% |
| H2 | Pre-2020 futures/options split not available from FIA summaries | Cannot compute instrument-level CAGR for full 10yr period |
| H3 | FIA methodology consistent across 2015-2024 | FIA added exchanges over time; early years may undercount slightly |

## Notional Value Assumptions

| # | Assumption | Value | Rationale |
|---|-----------|-------|-----------|
| N1 | BIS covers only IR + FX ETD notional | $12.83T/day | BIS explicitly states this scope |
| N2 | Average notional per equity ETD contract | ~$1,500 | Weighted: India ~$1K (small lots), US ~$10K, Europe ~$5K; India dominates volume |
| N3 | Average notional per commodity ETD contract | ~$25,000 | Blended across energy ($50K+), metals ($30K), agriculture ($10K) |
| N4 | Trading days for annual notional conversion | 255 | Slightly higher than equity markets due to commodity exchanges |

## Projection Assumptions

### Baseline (12% CAGR)

| # | Assumption | Rationale |
|---|-----------|-----------|
| B1 | India options growth decelerates from ~60% to ~15% | SEBI lot-size increases (Nov 2024), weekly expiry restrictions already biting |
| B2 | Futures grow at ~5% globally | Consistent with 2020-2024 CAGR of ~2.5%, plus emerging market growth |
| B3 | No major new markets open for derivatives | Conservative: no China liberalization, no major African exchanges |
| B4 | Crypto ETD remains <1% of total | CME crypto volumes growing but from tiny base |
| B5 | Options/futures mix stabilizes at ~85/15 | Current level sustained as India growth moderates |

### High-Growth (18% CAGR)

| # | Assumption | Rationale |
|---|-----------|-----------|
| G1 | Retail derivatives access expands to 10+ new markets | SE Asia (Vietnam, Philippines), Africa (Kenya, Nigeria), LatAm (Mexico, Colombia) |
| G2 | Crypto ETD grows to 3-5% of total by 2035 | Bitcoin/Ethereum ETF options on Cboe/Nasdaq; potential Solana, other assets |
| G3 | ETF options maintain 25%+ annual growth | US ETF options explosion continues; spreads to Europe and APAC |
| G4 | No global regulatory clampdown | Regulators accept derivatives growth as legitimate hedging/price discovery |
| G5 | AI/algorithmic trading increases velocity | More strategies, more frequent rebalancing |

### Conservative (5% CAGR)

| # | Assumption | Rationale |
|---|-----------|-----------|
| C1 | India volume drops 30-50% from SEBI interventions | Lot size increases, transaction taxes, position limits reduce retail speculation |
| C2 | China maintains restrictions on retail derivatives | No liberalization of equity/commodity options for retail |
| C3 | US introduces financial transaction tax | Repeatedly proposed in Congress; would reduce HFT/algo volume |
| C4 | European MiFID III adds derivatives constraints | Position limits, reporting burden increases cost of trading |
| C5 | Crypto derivatives face regulatory hostility | SEC/CFTC turf wars delay or prevent new crypto ETD listings |

## Double-Counting and Overlap Notes

| Risk | Mitigation |
|------|-----------|
| A single trade can appear on both sides (buyer + seller) | FIA counts single-sided volume (one contract = one count), which is industry standard |
| CME block trades may be counted differently | FIA includes all trade types; no special treatment needed |
| Index options on expiry may generate equity trades | Those equity trades are in "cash equity" category, not derivatives |
| ETF options overlap with equity category | WFE separates ETF derivatives as distinct asset class (~4% of total) |
| Crypto ETD on CME vs unregulated venues | Only CME/Cboe crypto derivatives count as ETD; Binance/Deribit are not included |

## Key Uncertainties

1. **India regulatory trajectory**: SEBI's Nov 2024 lot-size changes are the single largest risk factor. If weekly expiry restrictions and transaction taxes escalate, global volume growth could stall or reverse.

2. **FIA vs WFE gap**: The 25B contract difference (~12%) creates uncertainty in the "true" total. FIA is preferred but neither is wrong — they simply measure different universes.

3. **Notional value for equity ETD**: The BIS gap (no equity/commodity ETD notional) means our total notional estimate carries significant uncertainty. The $262T equity estimate could be $100T-$500T depending on assumptions about average contract size.

4. **Peak TPS**: Without exchange-level microsecond data, the peak TPS is necessarily speculative. NSE's matching engine capacity (~500K orders/second) is a technical upper bound, but actual TPS is lower.

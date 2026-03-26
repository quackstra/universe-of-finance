# OTC Derivatives — TPS Calculations

## Trade Count Estimation

### Reported Data: ISDA SwapsInfo (US/EU/UK)

**Interest Rate Derivatives (IRD)**:
- Q1 2024: 735,800 trades ($100.5T notional)
- H1 2024: 1,500,000 trades ($197.8T notional)
- Q4 2024 (US only): 696,600 trades ($106.1T notional)
- Full Year 2024 estimate: ~2.9M trades (~$400T notional)

Average notional per IRD trade: $400T / 2.9M = **~$138M per trade** (US/EU/UK)

**Credit Default Swaps (CDS)**:
- Index CDS: 316,800 trades ($12.7T notional), -6.9% YoY
- Single-name CDS: est. ~24,000 trades (~$1T notional) — 7% of CDS notional
- Total CDS: ~341,000 trades

### Global Extrapolation

ISDA SwapsInfo covers US, EU, and UK markets. These represent the majority of OTC derivatives activity but not all.

**IRD**:
- US/EU/UK: ~2.9M trades (ISDA reported)
- Japan: ~8% of global IRD market → ~0.25M trades
- Australia/NZ: ~3% → ~0.10M trades
- Hong Kong/Singapore: ~5% → ~0.17M trades
- Other (Canada, EM): ~4% → ~0.13M trades
- **Global IRD: ~3.55M trades**
- Note: Some double-counting may occur as cross-border trades are reported in multiple jurisdictions
- Adjusted estimate: **~3.2M global IRD trades**

**CDS**:
- US/EU/UK covers vast majority of CDS activity (~90%)
- Global CDS: 341K / 0.90 = **~380K trades**

**Equity Derivatives (OTC)**:
- Equity swaps, variance swaps, OTC equity options
- No comprehensive trade count data
- Estimated from notional outstanding ($8.9T) and average trade size (~$25M)
- With ~5-year average duration and portfolio turnover: ~2M trades/year estimate
- **Estimated: ~2.0M trades/year**

**Commodity Swaps (OTC)**:
- Small notional ($2.4T outstanding) but active hedging market
- Estimated: ~1.0M trades/year (commodity trading houses execute ~200K-400K each)
- **Estimated: ~1.0M trades/year**

**FX Derivatives (OTC, excl. spot)**:
- Forwards, swaps, options: covered primarily in FX category
- If included: ~5.0M trades/year (from FX capsule: ~750M total FX of which ~40% are derivatives by count)
- **For reference only — attributed to FX category**

### Global Total

| Product | Annual Trades (M) |
|---------|-------------------|
| IRD | 3.2 |
| CDS | 0.4 |
| Equity OTC | 2.0 |
| Commodity swaps | 1.0 |
| Other OTC | 0.7 |
| **Subtotal (excl. FX derivs)** | **7.3** |
| FX derivatives (for reference) | 5.0 |
| **Total (incl. FX derivs)** | **12.3** |

## TPS Calculation

### Including FX Derivatives
Daily trades: 12,300,000 / 252 = ~48,800/day
TPS (24h): 48,800 / 86,400 = **~0.56 TPS**
TPS (10h effective trading day): 48,800 / 36,000 = **~1.36 TPS**

### Excluding FX Derivatives
Daily trades: 7,300,000 / 252 = ~29,000/day
TPS (24h): 29,000 / 86,400 = **~0.34 TPS**
TPS (10h): 29,000 / 36,000 = **~0.81 TPS**

### Central Estimate: **~0.6 TPS** (incl. FX derivs, 24h basis)

## Peak TPS

Peak activity: central bank announcement days, quarter-end roll dates
Peak concentration: ~5x average during peak hours
Peak TPS: ~3 TPS

## Notional Per Trade Analysis

| Product | Annual Trades (est.) | Annual Notional (est.) | Avg Notional/Trade |
|---------|---------------------|----------------------|-------------------|
| IRD (US/EU/UK) | 2.9M | $400T | $138M |
| Index CDS | 317K | $12.7T | $40M |
| Equity OTC | 2.0M | ~$50T turnover | ~$25M |
| Commodity swaps | 1.0M | ~$15T turnover | ~$15M |

OTC derivatives have by far the highest average transaction value in the Universe of Finance.

## Confidence Assessment

- Notional outstanding: 🟢 High — BIS semiannual survey is authoritative
- Daily turnover (BIS triennial): 🟢 High — gold standard
- IRD/CDS trade count (US/EU/UK): 🟡 Medium — ISDA SwapsInfo is reliable for covered markets
- Global trade count total: 🔴 Low — requires extrapolation for non-reported markets and asset classes
- TPS: 🔴 Low — derived from estimated global trade counts

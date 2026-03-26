# CEX — Calculations & Methodology

## 1. Annual Volume Derivation

### Spot Volume
- Source: CoinGecko 2024 Annual Report — top 15 CEXs
- Total: $18.83 trillion (2024)

### Derivatives Volume
- Source: CoinGecko State of Crypto Perpetuals — top 10 CEXs
- Perpetuals: $58.5 trillion (2024)
- Note: This is notional volume. A 100x leveraged $100 position = $10,000 notional.

### Combined
- $18.83T + $58.5T = ~$77.3T

## 2. TPS Estimation Methodology

CEXs do not publish trade counts. We estimate as follows:

### Average Trade Size Assumptions
- Spot average trade: ~$500 (mix of retail $50-200 and institutional $10K+)
- Derivatives average trade: ~$2,000 (higher due to leverage mechanics)

### Daily Trade Count Estimate
- Spot: $18.83T / 365 / $500 = ~103M trades/day
- Derivatives: $58.5T / 365 / $2,000 = ~80M trades/day
- Combined: ~183M-400M trades/day (wide range due to trade size uncertainty)
- Midpoint: ~300M trades/day

### TPS
- 300M / 86,400 = ~3,472 TPS
- Range: 2,100 - 4,600 TPS
- Reported midpoint: ~4,000 TPS

### Peak TPS
- During extreme volatility (BTC flash crash, ETF launch day), volume can spike 3-5x
- Estimated peak: ~12,000-20,000 TPS
- Reported: ~15,000 TPS

## 3. Historic Spot Volume Series

| Year | Spot Volume (T) | Source |
|------|----------------|--------|
| 2019 | ~$3.5 | Industry estimate (CoinGecko series starts 2020) |
| 2020 | $3.78 | CoinGecko |
| 2021 | $25.21 | CoinGecko (all-time high) |
| 2022 | ~$14.0 | CoinGecko (estimated, FTX collapse year) |
| 2023 | $8.05 | CoinGecko |
| 2024 | $18.83 | CoinGecko |

## 4. Wash Trading Adjustment

Research estimates on unregulated exchanges:
- 50-70% of reported volume may be wash trading (Yale/NBER study)
- CoinGecko top-15 applies trust scoring, reducing but not eliminating wash trades
- Conservative "real" volume estimate: 60-80% of reported = $11.3T-$15.1T spot

We report CoinGecko figures as-is but flag the wash trading concern prominently.

## 5. Projection Methodology

Crypto volumes are **cyclical**, driven by ~4-year Bitcoin halving cycles:
- Halving: Apr 2024 → Bull phase: 2024-2025 → Peak: 2025-2026 → Bear: 2027-2028
- Next halving: ~Apr 2028 → Next bull: 2028-2029

Baseline projections follow this cycle pattern with a rising secular trend (institutional adoption, ETFs, regulatory frameworks).

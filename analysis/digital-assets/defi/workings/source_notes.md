# DeFi — Source Notes

## Primary Sources

### DeFiLlama
- The gold standard for DeFi data
- Aggregates TVL, DEX volume, lending, yield data across 200+ chains
- Open-source methodology; reads directly from smart contracts
- DEX volume page: https://defillama.com/dexs
- Perp DEX page: https://defillama.com/perps
- Confidence: 🟢 High for volume; 🟡 Medium for TVL (double-counting issues)

### CoinGecko Reports
- Annual crypto report provides DEX vs CEX volume comparisons
- Perpetuals report provides comprehensive derivatives data
- More narrative/analysis than raw data
- Confidence: 🟢 High

### CoinLaw
- Aggregates statistics from multiple sources
- Good for DeFi market overview statistics (users, TVL, trends)
- Less granular than DeFiLlama for protocol-level data
- Confidence: 🟡 Medium

## Data Gaps

1. **DeFi transaction count** — no standard source tracks total DeFi transaction count across all protocols. Our estimate (~1B) is derived from volume / avg trade size.
2. **Lending flow** — we have stock data (TVL, open borrows) but not annual flow data (total borrowed and repaid in 2024).
3. **Yield farming volume** — yield strategies involve many small transactions; no aggregated data exists.
4. **Pre-2020 DeFi** — essentially zero meaningful data; DeFi was negligible before Uniswap v2 (May 2020).

## Cross-Validation
- DeFiLlama $1.76T spot aligns with CoinGecko's $1.76T figure
- CoinGecko perps report ($2.4T) aligns with dYdX's ecosystem report figure
- TVL figures consistent between DeFiLlama ($140B) and industry reporting ($129B-$140B range)

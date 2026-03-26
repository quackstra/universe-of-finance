# CEX — Key Assumptions

## A1. Trade Count Estimation
- Average spot trade size: $500
- Average derivatives trade size: $2,000
- These are rough midpoints. Retail trades skew $50-200; institutional/bot trades skew $5K-50K.
- Confidence: 🔴 Low

## A2. Derivatives = Notional Volume
- Derivatives volume is reported as notional (face value), not collateral posted
- A trader depositing $1,000 with 50x leverage generates $50,000 in notional volume per trade
- Economic significance is much lower than headline notional figures suggest
- Spot volume is a more honest measure of actual capital changing hands

## A3. Wash Trading Caveat
- CoinGecko's top-15 data is already filtered by trust score
- But even "trusted" exchanges may have 10-20% artificial volume from market makers
- Unregulated exchanges (not in top 15) may have 50-70% wash volume
- We do NOT adjust reported figures but flag this limitation

## A4. Zero On-Chain Overlap
- CEX internal order matching happens on private databases
- On-chain activity (deposits, withdrawals) is a tiny fraction of trade volume
- This means CEX volume has ZERO overlap with the L1/L2 blockchain capsule
- Users depositing to and withdrawing from CEXs do appear on-chain, but the trades themselves do not

## A5. Projection Cyclicality
- Crypto is NOT a monotonically growing market (unlike card payments or bank transfers)
- Projections must account for bull/bear cycles
- Baseline uses halving cycle timing: peak years alternate with trough years
- Long-term secular trend is upward due to institutional adoption

## A6. Top-15 Coverage
- CoinGecko top-15 captures ~85-90% of legitimate CEX spot volume
- Hundreds of smaller exchanges exist but many have questionable volume
- We use top-15 as representative of the market

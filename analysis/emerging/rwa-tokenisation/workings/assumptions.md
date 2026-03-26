# Tokenised Real-World Assets — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. RWA.xyz as Primary TVL Source
**Assumption:** RWA.xyz's tracking of on-chain tokenised assets (excluding stablecoins) is the most comprehensive available.
**Reasoning:** RWA.xyz is the industry-standard tracker for tokenised real-world assets, similar to DeFiLlama for broader DeFi.
**Risk:** May miss smaller protocols, private chain deployments, or regional platforms. Likely undercounts total TVL by 10-20%.

### A2. Stablecoin Exclusion
**Assumption:** Stablecoins (USDT, USDC, DAI, etc.) are excluded from RWA TVL figures despite technically being tokenised real-world assets (backed by treasuries, deposits).
**Reasoning:** Stablecoins are covered in a separate Universe of Finance category. Including them would add ~$150B+ and distort the RWA analysis.
**Risk:** Some overlap exists — e.g., USDC backing includes Treasury bills that overlap with "tokenised treasuries." We accept this as a known limitation.

### A3. Mid-2025 Data Snapshot
**Assumption:** TVL and protocol data is based on mid-2025 figures (approximately June-July 2025).
**Reasoning:** This is the most recent comprehensive data available from RWA trackers and industry reports.
**Risk:** Market is growing rapidly; figures could be 20-30% higher by end of 2025.

---

## Transaction Count Assumptions

### A4. Transaction-to-TVL Ratio
**Assumption:** RWA protocols generate approximately 2,000-4,000 on-chain transactions per $1M of TVL per year.
**Reasoning:** RWA tokens are primarily buy-and-hold (Treasury tokens, private credit) with limited secondary trading. This is lower than DeFi lending protocols (~5,000-10,000 txns/$1M) but higher than simple token storage. The ratio includes minting, redemption, transfers, DeFi interactions, and governance.
**Risk:** Could be significantly higher if secondary markets develop, or lower if most holders simply buy and hold. The 2x range (2,000-4,000) reflects this uncertainty.

### A5. Transaction Definition
**Assumption:** We count all on-chain transactions interacting with RWA protocol contracts — including mints, redeems, transfers, approvals, yield claims, and DeFi composability actions.
**Reasoning:** This is consistent with how blockchain explorers count transactions.
**Risk:** Multi-step transactions (approve + deposit) may inflate counts. Conversely, batched operations (institutional mints) may undercount.

---

## Projection Assumptions

### A6. Baseline TVL Trajectory ($500B by 2030, $2T by 2035)
**Assumption:** TVL follows the lower end of industry projections, reflecting steady institutional adoption without regulatory breakthrough or crisis.
**Reasoning:** Industry consensus ranges from $3.5T (21.co baseline) to $30T (BCG/Standard Chartered bull case) by 2030. Our baseline of $500B is deliberately conservative — below even the most cautious institutional forecast — because:
  1. Current TVL is $24B; reaching $500B requires ~85% CAGR for 5 years, which is aggressive but below recent growth rates
  2. Regulatory uncertainty could slow adoption significantly
  3. Infrastructure challenges (custody, interoperability, oracles) are non-trivial
**Risk:** If any major exchange (NYSE, LSE) tokenises settlement, this could be dramatically too low.

### A7. High Growth TVL ($5T by 2030, $16T by 2035)
**Assumption:** Major financial infrastructure begins migrating to tokenised rails.
**Reasoning:** This aligns with BCG's mid-range projection. Requires: US regulatory clarity, institutional custody standards, cross-chain interoperability.
**Risk:** Regulatory failure or a major hack/exploit of a large RWA protocol could set back adoption by 3-5 years.

### A8. Conservative TVL ($100B by 2030, $500B by 2035)
**Assumption:** Tokenisation remains niche — primarily Treasury tokens and private credit for crypto-native users.
**Reasoning:** Traditional finance continues to operate on legacy rails. Regulatory barriers prevent broad institutional adoption. RWA tokens remain a crypto-native DeFi primitive, not a TradFi replacement.
**Risk:** This may be too pessimistic if BlackRock and other TradFi giants continue aggressively expanding their tokenised offerings.

### A9. Transaction Ratio Growth
**Assumption:** The transaction-to-TVL ratio increases over time (from ~2,000 to ~5,000-10,000 txns/$1M by 2035).
**Reasoning:** As tokenised assets develop liquid secondary markets and deeper DeFi integration, each dollar of TVL generates more transactions. Early stages are mint-and-hold; mature stages include trading, lending, derivatives.
**Risk:** If RWA tokens remain primarily institutional buy-and-hold instruments, the ratio may stay flat or decrease.

---

## Market Structure Assumptions

### A10. Private Credit Dominance Is Temporary
**Assumption:** Private credit's 61% TVL share will decline as treasuries, real estate, and equities tokenise.
**Reasoning:** Private credit was the earliest RWA use case because it has no liquid traditional market to compete with — tokenisation genuinely improved access. As treasuries and equities (which DO have liquid markets) tokenise, they will overtake private credit by TVL.
**Risk:** Private credit may retain dominance if regulatory barriers prevent equity/bond tokenisation.

### A11. Multi-Chain Future
**Assumption:** Tokenised RWAs will be distributed across multiple chains (Ethereum, Solana, Avalanche, Stellar, Base, etc.).
**Reasoning:** Different protocols and institutions are choosing different chains. No single chain will capture all RWA activity.
**Risk:** Chain fragmentation could reduce composability and secondary market liquidity, suppressing transaction counts.

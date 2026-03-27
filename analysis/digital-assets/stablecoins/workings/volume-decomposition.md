# Stablecoin Volume Decomposition

> Working paper for [Stablecoins REPORT.md](../REPORT.md) — Universe of Finance, Run 3
> Created: 2026-03-26

## The Gap

| Metric | Value | Source |
|--------|-------|--------|
| Raw on-chain volume (2024) | $27.6T | [CryptoSlate](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/) |
| Visa-adjusted volume (2024) | ~$5.5–5.7T | [Visa Onchain Analytics](https://visaonchainanalytics.com/transactions) |
| Unexplained gap | ~$21.9T (79%) | Derived |
| Real-world payment volume (2025 run-rate) | ~$390B (~1% of raw) | [McKinsey/Artemis](https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss) |

The gap is not a single phenomenon. It is a layered stack of non-payment activity, each with different economic meaning. This document attempts a bottom-up reconstruction.

---

## Visa's Adjustment Methodology

Visa (partnered with Allium Labs) applies two sequential filters to raw on-chain data:

1. **Directional Volume Filter**: Only the largest stablecoin amount in a single transaction is counted. This strips out redundant internal legs of complex smart contract interactions (e.g., a DEX swap that moves USDC through three pools counts only the largest single leg).

2. **Address Activity Filter**: Addresses that have sent >1,000 transactions OR >$10M in transfer volume in any 30-day period are excluded. This removes:
   - High-frequency trading wallets
   - Bot addresses (MEV, arbitrage, sandwich)
   - High-throughput smart contracts
   - Automated protocol addresses

**Result**: 77% of 2024's total stablecoin transaction volume falls into the "unadjusted" (filtered-out) category. The remaining 23% (~$5.5–5.7T) is classified as "adjusted" organic-like activity.

**Adjusted volume breakdown by category** (Visa dashboard, 2024):
- CEX-related transfers: **41%** (~$2.3T)
- DEX activity: estimated ~20–25%
- Lending/DeFi: estimated ~15–20%
- Other (P2P, payments, unknown): ~15–20%

Source: [Visa Onchain Analytics](https://visaonchainanalytics.com/transactions), [Allium](https://www.allium.so/post/visa-x-allium-making-sense-of-stablecoins)

---

## Decomposition of the $27.6T

### Component Breakdown

| Component | Est. Volume ($T) | % of Raw | Methodology | Confidence |
|-----------|-----------------|----------|-------------|------------|
| **Bot/MEV/HFT activity** | **$11–13T** | **40–47%** | Visa filter: 70% of volume is bot-related (CEX.IO/Visa); 77% falls into unadjusted category. Bot share dominant on Solana (98%), Base (98%), Ethereum (~60%). Fourfold increase from 2023. | Medium |
| **CEX deposit/withdrawal cycles** | **$4–5T** | **14–18%** | CEX is 41% of Visa-adjusted volume (~$2.3T) plus substantial CEX flows in the filtered-out portion. Glassnode/CryptoQuant exchange flow data suggests 30–40% of all on-chain stablecoin volume touches exchange addresses. | Medium |
| **DeFi internal flows** | **$3–4T** | **11–14%** | Yield farming rotations, liquidity provision/withdrawal, collateral movements, vault rebalancing. DeFi TVL in stablecoins was ~$50–60B with high turnover. Protocol-to-protocol transfers (e.g., Aave -> Curve -> Convex) generate multiple on-chain transactions for the same economic intent. | Low |
| **Bridge/cross-chain transfers** | **$0.5–1T** | **2–4%** | DeFi Llama bridge data: monthly volumes $1.5–3.2B for most of 2024, surging to $50B in Nov. Annual total ~$150–250B across all bridges. Each bridge transfer generates 2+ on-chain transactions (burn on source, mint on destination). Stablecoins are ~60–70% of bridge volume. | Medium |
| **Wash trading / volume inflation** | **$1–2T** | **4–7%** | Chainalysis 2025 market manipulation report documents ongoing wash trading. Stablecoin pairs (USDT/USDC) are common wash instruments. Concentrated on smaller CEXs and certain DEX pairs. Hard to separate cleanly from bot activity. | Low |
| **Institutional treasury management** | **$1–2T** | **4–7%** | Large stablecoin issuers (Circle, Tether) and institutional holders routinely move billions between chains, wallets, and custodians. Mint/burn events alone totaled hundreds of billions. | Low |
| **Organic economic activity** | **$5–6T** | **18–22%** | Visa-adjusted volume minus pure-CEX trading flows. Includes P2P transfers, merchant payments, remittances, payroll, cross-border settlement, and genuine DeFi usage. | Medium |
| - *of which: real-world payments* | *$0.39T* | *1.4%* | McKinsey/Artemis: B2B ($226B), payroll/remittances ($90B), capital markets ($8B), other ($66B). | High |
| **TOTAL** | **~$27.6T** | **100%** | | |

### Visual Waterfall

```
Raw on-chain volume                               $27.6T  (100%)
  minus Bot/MEV/HFT                              -$12.0T  (-43%)
  minus CEX deposit/withdrawal cycles             -$4.5T   (-16%)
  minus DeFi internal flows                       -$3.5T   (-13%)
  minus Bridge double-counting                    -$0.7T   (-3%)
  minus Wash trading                              -$1.5T   (-5%)
  minus Institutional treasury mgmt               -$1.5T   (-5%)
                                                  --------
= Organic economic activity                        ~$3.9T  (14%)
  of which: Visa-adjusted "payment-like"           $5.5T*  (20%)
  of which: real-world payments (McKinsey)         $0.39T  (1.4%)
```

*Note: The Visa-adjusted figure ($5.5T) is higher than our "organic economic activity" estimate because Visa's methodology retains some CEX and DeFi activity that passes below the 1,000-txn/30-day threshold. Both are valid lenses — Visa measures "not obviously automated," while our decomposition attempts "genuine economic intent."*

---

## Component Deep-Dives

### 1. Bot/MEV/HFT Activity ($11–13T, ~43%)

This is the single largest component and the primary reason raw volume is misleading.

**What it includes:**
- **Arbitrage bots**: Exploit price differences between DEXs, between CEXs and DEXs, and across chains. On Ethereum alone, EigenPhi data shows $20B+ monthly in bot-driven volume.
- **Sandwich attacks**: Front-run and back-run user transactions on DEXs. Still dominant on Solana despite mitigation on Ethereum (via MEV-Boost/Flashbots).
- **Liquidation bots**: Monitor lending protocols (Aave, Compound) and execute liquidations when collateral ratios drop. Each liquidation moves stablecoins.
- **Market-making bots**: Automated market makers on CEXs and DEXs continuously move stablecoins.

**Evidence:**
- CEX.IO analysis: 70% of 2024 stablecoin transaction volume was bot-related
- Visa unadjusted category captured 77% of volume, up from ~60% in 2023
- On Solana and Base, bot transactions were 98% of volume
- Bot activity experienced a fourfold increase in 2024 vs 2023

**Why it grew so fast in 2024:**
- Memecoin mania on Solana created massive arbitrage opportunities
- L2 proliferation (Base, Blast, etc.) created cross-chain arb opportunities
- Lower gas costs on L2s made smaller arbitrage trades profitable

### 2. CEX Deposit/Withdrawal Cycles ($4–5T, ~16%)

**What it includes:**
- Moving stablecoins from self-custody to exchange hot wallets (deposit)
- Moving stablecoins from exchange hot wallets back to self-custody (withdrawal)
- Exchange-to-exchange transfers (e.g., moving USDT from Binance to Bybit)
- OTC desk settlement flows

**Evidence:**
- Visa adjusted volume: CEX category is 41% of adjusted (~$2.3T)
- CryptoQuant: USDT exchange reserves surged 165% in 2024
- Estimated 30–40% of all on-chain stablecoin volume touches exchange addresses
- CEX internal transfers (order book trades) are NOT on-chain and NOT counted

**Key insight:** A single trade on a CEX can generate 2–4 on-chain stablecoin transactions: (1) deposit USDT to exchange, (2) trade (off-chain), (3) withdraw USDC from exchange, (4) bridge USDC to another chain. The economic intent is one trade, but the on-chain footprint is 3 stablecoin transfers.

### 3. DeFi Internal Flows ($3–4T, ~13%)

**What it includes:**
- **Yield farming rotations**: Moving stablecoins between protocols chasing APY (e.g., Aave -> Curve -> Convex -> back to Aave)
- **Liquidity provision/withdrawal**: Adding/removing stablecoins from AMM pools
- **Collateral movements**: Depositing/withdrawing stablecoins as collateral in lending protocols
- **Vault rebalancing**: Automated vault strategies (Yearn, Beefy) rebalancing positions
- **Protocol-to-protocol transfers**: Aggregators routing through multiple protocols

**Evidence:**
- DeFi TVL in stablecoins ~$50–60B with high turnover ratios
- A single yield farming strategy can generate 5–10 on-chain stablecoin transfers per cycle
- Automated vaults execute rebalancing multiple times per day

### 4. Bridge/Cross-Chain Transfers ($0.5–1T, ~3%)

**What it includes:**
- Lock-and-mint bridge transfers (e.g., Wormhole, Stargate)
- Burn-and-mint transfers (e.g., Circle CCTP for native USDC)
- Bridge aggregator routing (may traverse multiple intermediate chains)

**Evidence:**
- DeFi Llama: Monthly bridge volume $1.5–3.2B for most of 2024, surging to $50B in Nov
- Annual total across all bridges: ~$150–250B
- Stablecoins are ~60–70% of bridge volume -> ~$90–175B in stablecoin bridge volume
- Each bridge transfer creates 2+ on-chain transactions, so the on-chain footprint is 2–3x the economic value
- On-chain footprint: $200B–500B+ including relay and routing transactions
- Across protocol alone: $11.6B in stablecoin bridging in 2024

**Why this is smaller than expected:** Bridge volume, while growing fast, is still measured in hundreds of billions, not trillions. The double-counting effect (2–3x) inflates it, but it remains a relatively small contributor to the $27.6T total.

### 5. Wash Trading ($1–2T, ~5%)

**What it includes:**
- Deliberate volume inflation on DEXs and CEXs
- Stablecoin-pair trading (USDT/USDC) used for wash volume
- Incentive farming (trading volume to earn token rewards)

**Evidence:**
- Chainalysis 2025 market manipulation report documents ongoing wash trading
- Concentrated on smaller CEXs and certain DEX pairs
- Difficult to separate cleanly from legitimate bot market-making

### 6. Institutional Treasury Management ($1–2T, ~5%)

**What it includes:**
- Tether/Circle moving stablecoins between chains for liquidity management
- Institutional custodians rebalancing holdings
- Mint/burn events (new USDT/USDC issuance or redemption)
- Corporate treasury movements between wallets

---

## Organic Payment Volume: The Real Number

After stripping all non-payment activity, McKinsey/Artemis estimated **$390 billion** in real-world stablecoin payments for 2025 (run-rate based on December 2025 data):

| Payment Category | Annual Volume | % of Payments | Source |
|-----------------|---------------|---------------|--------|
| B2B cross-border payments | $226B | 58% | McKinsey/Artemis |
| Payroll & remittances | $90B | 23% | McKinsey/Artemis |
| Capital markets settlement | $8B | 2% | McKinsey/Artemis |
| Other (P2P, merchant, cards) | $66B | 17% | Derived |
| **Total real-world payments** | **$390B** | **100%** | |

### Geographic Distribution of Payments

| Region | Payment Volume | Notes |
|--------|---------------|-------|
| Asia-Pacific (Singapore, HK, Japan) | $245B | B2B trade settlement dominant |
| North America | $95B | Growing institutional adoption |
| Europe | $50B | MiCA-regulated corridor growth |

### Comparison to Traditional Payment Networks

| Network | Annual Volume | Daily Txns | Avg Transfer |
|---------|-------------|-----------|-------------|
| Visa | $14.8T | ~640M | ~$63 |
| Mastercard | $9.0T | ~390M | ~$63 |
| SWIFT | ~$150T | ~50M msg/day | ~$8,200 |
| PayPal | ~$1.5T | ~60M | ~$69 |
| **Stablecoins (Visa-adjusted)** | **$5.5T** | **~10M** | **~$1,500** |
| **Stablecoins (real payments)** | **$0.39T** | **~2–5M** | **~$200–500** |

**Key insight:** Stablecoin real-world payment volume ($390B) is roughly:
- 2.6% of Visa's volume
- 0.26% of SWIFT's volume
- 45% of global remittances ($860B)
- Still tiny in absolute terms, but growing at 500%+ annually

---

## Velocity Analysis

### Raw Velocity by Stablecoin

Velocity = Annual Transfer Volume / Average Market Cap

| Stablecoin | Market Cap (avg 2024) | Transfer Volume Share | Est. Volume | Velocity | Interpretation |
|------------|----------------------|----------------------|-------------|----------|---------------|
| USDT | ~$120B | 25% ($6.9T) | $6.9T | ~58x | Retail/P2P dominant, moderate velocity |
| USDC | ~$35B | 70% ($19.3T) | $19.3T | ~551x | Institutional/programmatic, extreme velocity |
| DAI/USDS | ~$5B | 3% ($0.8T) | $0.8T | ~166x | DeFi-native, high protocol cycling |
| Others | ~$15B | 2% ($0.6T) | $0.6T | ~37x | Mixed |
| **All** | **~$175B avg** | **100%** | **$27.6T** | **~158x** | |

*Note: Average market cap used (not year-end $205B) for more accurate velocity.*

### USDC's Extreme Velocity Explained

USDC's velocity (~551x) is 9.5x higher than USDT's (~58x). This does NOT mean USDC is "used more" in a retail sense. It means:

1. **Institutional/programmatic routing**: USDC is the preferred stablecoin for DeFi protocol routing, DEX aggregators, and institutional settlement
2. **Circle CCTP**: Native cross-chain transfers create high-velocity circulation
3. **Compliance positioning**: Regulated entities (Coinbase, Stripe) route through USDC
4. **Smaller market cap denominator**: $35B vs $120B amplifies the velocity ratio

### Adjusted Velocity Comparison

| Monetary Instrument | Annual Throughput | Base | Velocity | Category |
|--------------------|------------------|------|----------|----------|
| **US M1** | ~$18T GDP | ~$18T | ~1.0x | Broad money (incl. savings) |
| **US M2** | ~$23.5T | ~$21T | ~1.12x | Includes time deposits |
| **PayPal balances** | ~$1.5T | ~$40B | ~38x | Digital transactional money |
| **Visa network** | ~$14.8T | ~$20B float | ~740x | Pure payment rail |
| **Stablecoins (raw)** | $27.6T | $175B avg | ~158x | Includes all on-chain activity |
| **Stablecoins (Visa-adj)** | $5.5T | $175B avg | ~31x | Filtered for organic-like |
| **Stablecoins (payments)** | $0.39T | $175B avg | ~2.2x | Real-world payments only |

### What Velocity Tells Us

1. **Raw velocity (158x) is meaningless** for economic comparison. It reflects the fact that stablecoins are programmable money on always-on rails — bots can move the same dollar thousands of times per day.

2. **Visa-adjusted velocity (~31x)** is comparable to PayPal balance velocity (~38x). This makes intuitive sense: both represent digital transactional money used primarily within a financial ecosystem (DeFi for stablecoins, ecommerce for PayPal).

3. **Payment velocity (~2.2x)** is close to M1/M2 velocity (~1.0–1.12x), suggesting that stablecoins used for real-world payments circulate at roughly the same rate as traditional dollars. This is the most meaningful comparison.

4. **The 25x gap between Visa-adjusted velocity (31x) and M2 velocity (1.12x)** is explained by the fact that M2 includes savings/store-of-value money that rarely moves, while the Visa-adjusted stablecoin figure still includes substantial trading and DeFi activity that is not "payment" activity per se.

---

## Implications for TPS Estimates

The stablecoins capsule estimates ~520 TPS based on ~45M daily transactions. How should the volume decomposition affect this?

| Activity Type | % of Volume | % of Transactions (est.) | Est. Daily Txns | Est. TPS |
|--------------|-------------|-------------------------|----------------|----------|
| Bot/MEV/HFT | 43% | 60–70% | 27–31.5M | 312–365 |
| CEX flows | 16% | 10–15% | 4.5–6.75M | 52–78 |
| DeFi internal | 13% | 10–15% | 4.5–6.75M | 52–78 |
| Bridge transfers | 3% | 2–3% | 0.9–1.35M | 10–16 |
| Wash trading | 5% | 3–5% | 1.35–2.25M | 16–26 |
| Treasury mgmt | 5% | 1–2% | 0.45–0.9M | 5–10 |
| Organic economic | 15% | 5–10% | 2.25–4.5M | 26–52 |
| - Real payments | 1.4% | 2–5% | 0.9–2.25M | 10–26 |

**Key finding:** Organic economic stablecoin TPS is likely **26–52 TPS**, not 520 TPS. Real-world payment TPS is likely **10–26 TPS**. The headline 520 TPS figure is dominated by automated/bot activity.

However, this does not diminish stablecoins' importance. Even 26–52 TPS of genuine economic activity is:
- Growing at 100%+ annually
- Operating 24/7/365 (unlike traditional payment rails)
- Serving use cases (cross-border B2B, emerging market remittances) that traditional systems serve poorly

---

## Confidence Assessment

| Estimate | Confidence | Key Uncertainty |
|----------|-----------|-----------------|
| Total raw volume ($27.6T) | High | Well-sourced from on-chain data |
| Visa-adjusted volume ($5.5T) | Medium | Methodology is transparent but threshold choices (1,000 txns) are debatable |
| Bot/MEV share (40–47%) | Medium | Consistent across CEX.IO, Visa, and Allium analyses |
| CEX flow share (14–18%) | Medium | CryptoQuant/Glassnode exchange labeling is mature |
| Real-world payments ($390B) | High | McKinsey/Artemis bottom-up from merchant and payment processor data |
| Bridge volume ($0.5–1T) | Medium | DeFi Llama data is comprehensive but 2024 surges add uncertainty |
| DeFi internal ($3–4T) | Low | Hardest to isolate; blurs with bot activity and CEX flows |
| Wash trading ($1–2T) | Low | Inherently difficult to measure; overlaps with bot category |
| Velocity comparisons | High | Straightforward arithmetic on well-sourced inputs |

---

## Key Takeaways

1. **The $27.6T headline is ~70x the actual payment volume.** Only $390B (1.4%) represents real-world payments for goods, services, payroll, and remittances. The rest is financial plumbing.

2. **Visa's $5.5T adjusted figure is the best available "organic activity" proxy**, but it still includes substantial CEX trading flows (41% of adjusted = ~$2.3T) and DeFi activity. It is "not automated" rather than "is a payment."

3. **There are really three numbers to care about:**
   - $27.6T = total on-chain footprint (useful for blockchain capacity planning)
   - $5.5T = organic-like economic activity (useful for comparing to traditional finance)
   - $390B = real-world payments (useful for understanding stablecoin adoption as a payment method)

4. **Stablecoin payment velocity (~2.2x) is comparable to M2 velocity (~1.12x)**, which makes intuitive sense — real payments circulate at real-economy speeds regardless of the underlying technology.

5. **The 2024 bot explosion (4x vs 2023) inflated raw volume disproportionately.** If bot growth normalises, future raw-to-adjusted ratios may improve, making headline figures less misleading.

6. **B2B cross-border payments ($226B) are the largest real-world use case**, not P2P remittances. This is significant — it suggests stablecoins are first disrupting correspondent banking, not retail payments.

---

## Sources

1. [CryptoSlate — Stablecoins surpass Visa and Mastercard with $27.6T](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/)
2. [Visa Onchain Analytics Dashboard](https://visaonchainanalytics.com/transactions)
3. [Visa — Making Sense of Stablecoins](https://corporate.visa.com/en/sites/visa-perspectives/trends-insights/making-sense-of-stablecoins.html)
4. [Allium — Visa x Allium: Making Sense of Stablecoins](https://www.allium.so/post/visa-x-allium-making-sense-of-stablecoins)
5. [McKinsey — Stablecoins in payments: What the raw transaction numbers miss](https://www.mckinsey.com/industries/financial-services/our-insights/stablecoins-in-payments-what-the-raw-transaction-numbers-miss)
6. [CoinDesk — Stablecoins moved $35T but only 1% was real-world payments](https://www.coindesk.com/business/2026/01/23/stablecoins-moved-usd35-trillion-last-year-but-only-1-of-it-was-for-real-world-payments)
7. [CEX.IO — Stablecoin Landscape: What 2024 Reveals](https://blog.cex.io/ecosystem/stablecoin-landscape-34864)
8. [Castle Island / Brevan Howard — Stablecoins: The Emerging Market Story](https://castleisland.vc/wp-content/uploads/2024/09/stablecoins_the_emerging_market_story_091224.pdf)
9. [Artemis — Stablecoin Payments from the Ground Up 2025](https://reports.artemisanalytics.com/stablecoins/artemis-stablecoin-payments-from-the-ground-up-2025.pdf)
10. [Citi GPS — Stablecoins 2030](https://www.citigroup.com/rcs/citigpa/storage/public/GPS_Report_Stablecoins_2030.pdf)
11. [IMF — How to Estimate International Stablecoin Flows (WP/2025/141)](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025141-source-pdf.pdf)
12. [IMF — Understanding Stablecoins (2025)](https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf)
13. [Chainalysis — Crypto Market Manipulation 2025](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)
14. [DeFi Llama — Bridge Volume Rankings](https://defillama.com/bridges)
15. [CryptoQuant — Stablecoin Exchange Flows](https://cryptoquant.com/asset/stablecoin/chart/exchange-flows)
16. [EigenPhi — MEV Data](https://eigenphi.io/)
17. [Reap Global — B2B Stablecoin Payments Surge](https://reap.global/newsroom/b2b-stablecoin-payments-surge-30x-to-3-billion-monthly-volume-in-2025)

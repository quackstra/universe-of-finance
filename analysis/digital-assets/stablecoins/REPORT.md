# Stablecoins — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Stablecoins settled **$27.6 trillion** in on-chain transfer volume in 2024, surpassing the combined transaction volume of Visa and Mastercard by 7.68% ([CryptoSlate](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/)). With an estimated **~45 million daily transactions** across all chains, stablecoins operate at roughly **~520 TPS**. USDC overtook USDT in transfer volume (70% share) despite USDT dominating by market cap and active addresses. Solana became the leading chain for stablecoin activity, overtaking Tron and Ethereum. Stablecoins are emerging as the crypto sector's most compelling use case for real-world payments and cross-border settlement.

## Scope

This analysis covers **fiat-pegged stablecoins** transacted on public blockchains. Included: USDT (Tether), USDC (Circle), DAI/USDS (MakerDAO/Sky), FDUSD, PYUSD, TUSD, and other USD-pegged tokens. Transfers, mint/burn events, and smart contract interactions (DEX swaps involving stablecoins, lending deposits) are counted. Excluded: algorithmic stablecoins (most collapsed), non-USD stablecoins (EUROC, etc. — negligible volume), CEX internal stablecoin transfers.

**Double-counting warning:** Stablecoin transfers are a **subset** of L1/L2 blockchain transactions. A USDT transfer on Ethereum counts in both this capsule AND the [L1/L2 capsule](../blockchain-l1-l2/REPORT.md). Many stablecoin transactions also overlap with [DeFi](../defi/REPORT.md) (e.g., stablecoins swapped on DEXs, deposited in lending protocols). Do not sum across capsules.

---

## Current State

### Transfer Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Annual transfer volume (2024) | $27.6T | [CryptoSlate](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/) | 🟢 High |
| Adjusted annual volume (Visa method) | ~$5.7T | [Visa Onchain Analytics](https://visaonchainanalytics.com/transactions) | 🟡 Medium |
| Est. daily transactions | ~45M | [World Metrics / Artemis](https://worldmetrics.org/stablecoin-statistics/) | 🟡 Medium |
| Est. average TPS | ~520 | Derived: 45M / 86,400 | 🟡 Medium |
| USDT daily active addresses | ~1.5M | [Artemis](https://app.artemisanalytics.com/stablecoins) | 🟡 Medium |
| Total stablecoin market cap (Dec 2024) | ~$205B | CoinGecko | 🟢 High |
| Avg transfer value (unadjusted) | ~$1,680 | $27.6T / (45M x 365) | 🔴 Low |

### Volume: Raw vs Adjusted

The $27.6T headline figure includes all on-chain movements: bot activity, arbitrage, smart contract routing, institutional treasury management, and duplicate counting across bridges. Visa's Onchain Analytics Dashboard strips out:
- High-frequency trading activity
- Institutional treasury movements
- Smart contract-to-contract transfers
- Bridge relay transactions

After adjustment, Visa estimated **~$2.5T in payment-like activity** over 12 months to May 2024. Extrapolating to full year 2024 suggests **~$5.7T in adjusted payment volume** — still enormous, but ~80% lower than the raw figure.

### Stablecoin Market Share

| Stablecoin | Market Cap (Dec 2024) | Transfer Volume Share | Active Address Share | Source |
|------------|----------------------|----------------------|---------------------|--------|
| USDT (Tether) | ~$140B | ~25% | ~67% | [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report) |
| USDC (Circle) | ~$45B | ~70% | ~27% | TRM Labs |
| DAI/USDS | ~$5B | ~3% | ~3% | Estimated |
| Others (FDUSD, PYUSD, TUSD) | ~$15B | ~2% | ~3% | Estimated |

**Key insight:** USDC dominates by transfer volume (70%) but USDT dominates by market cap ($140B) and active addresses (67%). This suggests USDC is used for larger, institutional/commercial transfers while USDT is used for more frequent, smaller transfers — particularly in emerging markets.

### Chain Distribution (2024)

| Chain | Role | Notes |
|-------|------|-------|
| Solana | #1 by activity (Jan 2024+) | Overtook Tron and Ethereum for stablecoin transfers |
| Tron | Major USDT chain | Dominates emerging market P2P transfers; low fees |
| Ethereum L1 | High-value settlement | Large transfers; institutional usage |
| Arbitrum/Base | Growing L2 usage | Low fees attracting DeFi stablecoin activity |
| BNB Chain | Moderate activity | BSC-native stablecoin usage |

---

## Historic Trend

### Stablecoin Transfer Volume (2019-2024)

| Year | Annual Transfer Volume | Market Cap (Dec) | Key Event | Confidence |
|------|----------------------|-----------------|-----------|------------|
| 2019 | ~$0.2T | ~$5B | USDT dominance, early Ethereum | 🔴 Low |
| 2020 | ~$1T | ~$25B | DeFi summer drives stablecoin demand | 🔴 Low |
| 2021 | ~$5T | ~$140B | USDC growth, multi-chain expansion | 🟡 Medium |
| 2022 | ~$7T | ~$135B | Bear market flight to stability; UST collapse | 🟡 Medium |
| 2023 | ~$12T | ~$130B | USDT on Tron grows; USDC recovers | 🟡 Medium |
| 2024 | $27.6T | ~$205B | Record year; USDC overtakes USDT in volume | 🟢 High |

*Sources: CryptoSlate, TRM Labs, Bloomberg, Artemis.*

---

## Growth Rate Analysis

| Period | Growth | Context |
|--------|--------|---------|
| 2023-2024 | +130% | Bull market + real-world payment adoption |
| 2020-2024 (4yr) | ~28x | From $1T to $27.6T |
| Market cap 2020-2024 | ~8x | From $25B to $205B |

Stablecoin transfer volume is growing faster than market cap, indicating increasing **velocity** — each stablecoin dollar is being transferred more frequently. This suggests genuine usage growth, not just supply inflation.

---

## Projections

### Baseline (Payment Use Case Matures)

**Assumptions:**
1. Stablecoins become a standard cross-border payment rail (competing with SWIFT/wires)
2. Regulatory frameworks (US stablecoin bill, MiCA) provide clarity, enabling institutional adoption
3. Market cap grows to $500B by 2030; velocity continues increasing
4. Major payment companies (Stripe, PayPal) integrate stablecoins at scale

| Year | Annual Transfer Volume | Market Cap (est.) | Daily Txns (est.) |
|------|----------------------|------------------|------------------|
| 2026 | $50T | $350B | ~80M |
| 2028 | $60T | $400B | ~100M |
| 2030 | $100T | $500B | ~150M |
| 2035 | $200T | $1T | ~300M |

### High Growth (Stablecoins Replace Cash)

**Assumptions:**
1. Stablecoins become dominant payment method in emerging markets
2. Tokenised deposits and CBDC interoperability expand the market
3. AI agents use stablecoins for autonomous micro-payments
4. Market cap exceeds $2T

| Year | Annual Transfer Volume | Market Cap (est.) | Daily Txns (est.) |
|------|----------------------|------------------|------------------|
| 2026 | $80T | $500B | ~120M |
| 2028 | $150T | $800B | ~200M |
| 2030 | $300T | $1.5T | ~400M |
| 2035 | $1,000T | $3T | ~1B |

### Conservative (Regulatory Headwinds)

**Assumptions:**
1. US regulation restricts non-bank stablecoin issuance
2. CBDCs capture the regulated payment use case
3. Crypto bear market reduces DeFi-driven stablecoin usage
4. Growth decelerates to 15-20% CAGR

| Year | Annual Transfer Volume | Market Cap (est.) | Daily Txns (est.) |
|------|----------------------|------------------|------------------|
| 2026 | $35T | $250B | ~55M |
| 2028 | $30T | $220B | ~50M |
| 2030 | $45T | $300B | ~70M |
| 2035 | $70T | $500B | ~100M |

---

## Key Findings

1. **Stablecoins settled $27.6T in 2024 — more than Visa and Mastercard combined.** This is the headline statistic, but it must be heavily caveated: the raw figure includes bot activity, bridge routing, and institutional treasury management. Visa's adjusted figure is ~$5.7T, still substantial.

2. **USDC dominates volume; USDT dominates usage.** USDC handles 70% of transfer volume (large, institutional transfers) while USDT has 67% of active addresses (retail, emerging market, P2P). This bifurcation reflects USDC's institutional/compliance positioning vs USDT's grassroots adoption.

3. **Stablecoins are the "killer app" of crypto for real-world utility.** Cross-border payments, remittances, dollarisation in emerging markets, and treasury management are genuine non-speculative use cases growing rapidly.

4. **Velocity is increasing faster than supply.** The 130% volume growth in 2024 outpaced the ~58% market cap growth, meaning each stablecoin dollar is being used more frequently — a strong signal of organic adoption.

5. **All stablecoin transactions are a subset of L1/L2 transactions.** A USDT transfer on Tron counts as both a stablecoin transfer and a Tron blockchain transaction. Many stablecoin transactions also overlap with DeFi activity.

6. **Solana is the new stablecoin activity leader** by transaction count, overtaking Tron and Ethereum in early 2024. This reflects lower fees and the memecoin/DeFi activity driving stablecoin demand on Solana.

---

## Data Quality & Limitations

- **Raw vs adjusted volume.** The $27.6T figure is raw on-chain volume. Visa's adjusted $5.7T is more representative of economic activity, but the adjustment methodology is opaque. The "true" payment volume is likely somewhere between $5.7T and $27.6T.
- **Transaction count is estimated.** Unlike transfer volume (well-tracked), the number of daily stablecoin transactions is reported inconsistently. Our ~45M/day figure is an estimate from Artemis/World Metrics.
- **Market cap is reliable.** Total stablecoin supply is on-chain and verifiable. USDT on Tron, USDC on Ethereum — these are auditable smart contract balances.
- **Chain attribution.** Stablecoins exist on multiple chains (USDT on Ethereum, Tron, Solana, etc.). Attributing activity to chains requires chain-specific analytics.
- **Historic volume before 2022 is rough.** Cross-chain stablecoin tracking was less mature; earlier figures are estimates.
- **USDT transparency concerns.** Tether's reserves and reporting have been questioned, though this affects market cap confidence more than transfer volume data.

---

## Sources

1. [CryptoSlate — Stablecoins surpass Visa and Mastercard with $27.6T transfer volume in 2024](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/)
2. [Bloomberg — Stablecoin Transactions Rose to Record $33T (incl. early 2025)](https://www.bloomberg.com/news/articles/2026-01-08/stablecoin-transactions-rose-to-record-33-trillion-led-by-usdc)
3. [TRM Labs — 2025 Crypto Adoption and Stablecoin Usage Report](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report)
4. [Visa Onchain Analytics Dashboard — Transactions](https://visaonchainanalytics.com/transactions)
5. [Visa — Making Sense of Stablecoins](https://corporate.visa.com/en/sites/visa-perspectives/trends-insights/making-sense-of-stablecoins.html)
6. [Artemis Terminal — Stablecoins Dashboard](https://app.artemisanalytics.com/stablecoins)
7. [Artemis — Stablecoin Payments from the Ground Up 2025](https://reports.artemisanalytics.com/stablecoins/artemis-stablecoin-payments-from-the-ground-up-2025.pdf)
8. [McKinsey — Stablecoins: Payments infrastructure for modern finance](https://www.mckinsey.com/industries/financial-services/our-insights/the-stable-door-opens-how-tokenized-cash-enables-next-gen-payments)
9. [CEX.IO Blog — Stablecoin Landscape: What 2024 Reveals](https://blog.cex.io/ecosystem/stablecoin-landscape-34864)
10. [World Metrics — Stablecoin Statistics 2026](https://worldmetrics.org/stablecoin-statistics/)
11. [IMF — Crypto-Assets Monitor](https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/Crypto%20Assets%20Monitor.pdf)
12. [BVNK & Cebr — The Decade of Digital Dollars 2024](https://bvnk.com/report/decade-of-digital-dollars)

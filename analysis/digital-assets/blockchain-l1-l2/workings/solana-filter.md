# Solana Vote Transaction Filter & L1/L2 TPS Revision

> Working paper for [L1/L2 Blockchain Transactions](../REPORT.md) capsule.
> Created: 2026-03-26 | Run 3 Research Elf

---

## The Problem

Solana's headline transaction count (~50-138M daily, ~18B+ annually in 2024) includes three categories of inflated activity that do not represent genuine economic transactions:

1. **Vote transactions** — validator consensus messages submitted every slot (~400ms). These are protocol overhead, not user activity.
2. **Failed transactions** — transactions that consume compute but revert. On Solana, failed transactions are still recorded on-chain and counted.
3. **MEV bot spam** — arbitrage and sandwich bots that submit thousands of transactions per block, most of which fail intentionally as part of their strategy.

Without filtering these, Solana appears to process ~580-1,600 TPS. After filtering, genuine user TPS drops dramatically. This distortion cascades into global L1/L2 TPS estimates, since Solana accounts for ~70% of all blockchain transactions by count.

---

## Solana Transaction Breakdown

### Vote vs. Non-Vote Transactions

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| Total daily txns (avg) | ~50-70M | 2024 avg | Solscan, SolanaCompass | 🟡 Medium |
| Total daily txns (peak) | 138M | Dec 2024 | CryptoSlate | 🟢 High |
| Non-vote daily txns (avg) | ~30-50M | 2024 avg | Dune `solana.vote_transactions` | 🟡 Medium |
| Non-vote daily txns (peak) | 148M | 30 Jan 2026 | KuCoin/SolanaCompass | 🟢 High |
| Vote txn share (historic) | ~60-70% of total | Pre-2025 | Solscan analytics, Dune | 🟡 Medium |
| Vote txn share (late 2025+) | ~30-40% of total | Late 2025-2026 | The Block, Everstake | 🟡 Medium |
| Vote txns daily (peak era) | ~300K validator-submitted | 2023 (2,500 validators) | The Block | 🟡 Medium |
| Vote txns daily (current) | ~170K validator-submitted | Mar 2026 (~800 validators) | The Block | 🟡 Medium |

**Key shift:** Vote transaction share has declined from ~60-70% historically to ~30-40% as of late 2025. This is driven by two forces:
1. **Validator count collapse**: from ~2,500 validators (early 2023) to <800 (Mar 2026), a 65%+ decline. Fewer validators = fewer vote transactions.
2. **Non-vote transaction surge**: genuine activity (DeFi, memecoins, AI agents) has pushed non-vote txns from ~20M/day to 50-100M/day.

### Failed Transaction Rate

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| Non-vote failure rate (peak) | 75.7% | Apr 2024 | Cointelegraph, BeInCrypto | 🟢 High |
| Non-vote failure rate (avg 2024) | ~40-50% | 2024 | Helius MEV Report | 🟡 Medium |
| Non-vote failure rate (current) | ~30-40% | Early 2026 | Estimated from trend | 🔴 Low |
| Failed arb txns as % of all non-vote | >50% | 2024 | Helius | 🟡 Medium |

### MEV Bot Activity

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| MEV bot blockspace consumption | ~40% | 2025 | Flashbots / AInvest | 🟡 Medium |
| MEV bot fee contribution | ~7% of total fees | 2025 | Flashbots | 🟡 Medium |
| Sandwich bot revenue | $370-500M | 16 months to Jan 2026 | Helius MEV Report | 🟡 Medium |
| Jito validator stake share | 92% | Early 2025 | Everstake | 🟢 High |
| Single bot: 11M txns / 30 days | 99.95% failure rate | Late 2024 | Bitget | 🟡 Medium |

---

## Adjusted Solana TPS

### Filtering Methodology

We apply three sequential filters to Solana's headline TPS:

| Filter | Removal Rate | Rationale |
|--------|-------------|-----------|
| **1. Remove vote transactions** | 30-40% of total (2026); 60-70% (pre-2025) | Validator consensus overhead, not user activity |
| **2. Remove failed non-vote txns** | 30-50% of remaining | Reverted txns consume compute but produce no economic outcome |
| **3. Remove identified MEV spam** | ~20-30% of successful non-vote | Bot-generated txns with no end-user economic intent |

### Calculation (2024 average baseline)

| Step | Daily Txns | TPS | Notes |
|------|-----------|-----|-------|
| **Headline total** | ~60M | ~694 | Reported average |
| After vote filter (60% removal) | ~24M | ~278 | Non-vote only |
| After failed txn filter (45% failure) | ~13.2M | ~153 | Successful non-vote only |
| After MEV spam filter (25% removal) | ~9.9M | ~115 | Genuine user transactions |

### Calculation (late 2025 / early 2026 baseline)

| Step | Daily Txns | TPS | Notes |
|------|-----------|-----|-------|
| **Headline total** | ~100M | ~1,157 | Higher activity, fewer validators |
| After vote filter (35% removal) | ~65M | ~752 | Non-vote only |
| After failed txn filter (35% failure) | ~42M | ~489 | Successful non-vote only |
| After MEV spam filter (25% removal) | ~31.5M | ~365 | Genuine user transactions |

### Summary: Solana TPS Range

| Metric | 2024 Avg | Late 2025+ | Source |
|--------|---------|-----------|--------|
| Headline TPS | ~694 | ~1,157 | Solscan |
| Non-vote TPS | ~278 | ~752 | Dune/SolanaCompass |
| Successful non-vote TPS | ~153 | ~489 | Derived |
| "Genuine user" TPS (est.) | ~115 | ~365 | Derived (speculative) |
| **Reduction from headline** | **~83%** | **~68%** | — |

The "genuine user" TPS is the most speculative figure because defining MEV spam vs. legitimate arbitrage is subjective. The non-vote successful TPS (~153-489) is the most defensible adjusted metric.

---

## Other Chain Adjustments

### Bitcoin: Ordinals/Inscriptions

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| Inscription share of txns (peak) | 73.2% | 13 Jan 2024 | Glassnode, academic papers | 🟢 High |
| Cumulative inscriptions | 69.6M | Sep 2024 | Bitcoin Ordinals Statistics | 🟢 High |
| Inscription share (2024 avg) | ~15-25% | 2024 full year | Estimated; peaked Q1, faded H2 | 🟡 Medium |
| Blockspace utilization pre-inscriptions | ~40% | Pre-2023 | Glassnode | 🟢 High |
| Blockspace utilization with inscriptions | ~80% | 2024 peak | Glassnode | 🟢 High |

**Adjustment:** Bitcoin inscriptions are economically meaningful (they pay fees, occupy blockspace) but represent a different transaction class than monetary transfers. For a "monetary transfer TPS" metric, removing inscriptions would reduce Bitcoin's ~5.8 TPS to ~4.3-4.9 TPS (2024 average). However, inscriptions faded significantly in H2 2024, so the adjustment is modest by year-end.

### Ethereum L1: MEV/Bot Activity

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| Flashbots Protect share of txns | ~3% | 2024-2025 | Flashbots | 🟢 High |
| Estimated MEV bot txns (L1) | ~10-15% | 2024 | Flashbots research | 🟡 Medium |
| MEV bot gas consumption | Higher than txn share | Ongoing | EigenPhi | 🟡 Medium |

**Adjustment:** Ethereum L1 MEV activity is less distortionary than Solana because: (a) Ethereum's fee market (EIP-1559) discourages spam; (b) Flashbots MEV-Boost channels most MEV through builder auctions rather than on-chain spam; (c) failed transactions are less common on Ethereum L1. A ~10-15% reduction for MEV bots would take Ethereum L1 from ~13.5 TPS to ~11.5-12.2 TPS.

### Ethereum L2s: Bot/Spam Activity

| Metric | Value | Period | Source | Confidence |
|--------|-------|--------|--------|------------|
| MEV spam on OP-Stack rollups | >50% of gas | 2024-2025 | Flashbots | 🟡 Medium |
| Base: 2 bots account for | >80% of spam txns | Nov 2024-Feb 2025 | Flashbots | 🟡 Medium |
| Base: 11M gas/s added, consumed by bots | ~100% of added capacity | Nov 2024-Feb 2025 | Flashbots | 🟢 High |
| Airdrop farming (sybil) share | ~20-40% (pre-airdrop) | 2024 | Estimated from post-airdrop drops | 🔴 Low |

**Adjustment:** L2 spam is a significant but harder-to-quantify problem. The ~14M+ daily L2 transactions likely include 30-50% bot/spam activity. Adjusted L2 daily genuine transactions may be ~7-10M rather than ~14M+.

---

## Revised Global L1/L2 TPS

### Original Estimates (from REPORT.md)

| Chain / Group | Daily Txns | TPS | Annual Txns |
|---------------|-----------|-----|-------------|
| Solana | ~60M | ~694 | ~18B+ |
| Ethereum L2s | ~14M+ | ~162 | ~4.2B+ |
| BNB Chain | ~3.5M | ~41 | ~1.2B |
| Ethereum L1 | ~1.16M | ~13.5 | ~425M |
| Bitcoin | ~500K | ~5.8 | ~183M |
| Other | ~5M | ~58 | ~1.8B+ |
| **Total** | **~84M** | **~974** | **~25.8B** |

### Adjusted Estimates (vote/spam/bot filtered)

| Chain / Group | Original TPS | Adjustment | Adjusted TPS | Adjusted Daily Txns |
|---------------|-------------|------------|-------------|---------------------|
| Solana | ~694 | -75% (votes + failures + MEV) | ~153-278 | ~13-24M |
| Ethereum L2s | ~162 | -35% (MEV bots + sybils) | ~105 | ~9.1M |
| BNB Chain | ~41 | -15% (bots, conservative) | ~35 | ~3.0M |
| Ethereum L1 | ~13.5 | -12% (MEV bots) | ~12 | ~1.0M |
| Bitcoin | ~5.8 | -20% (inscriptions, 2024 avg) | ~4.6 | ~400K |
| Other | ~58 | -20% (est.) | ~46 | ~4.0M |
| **Total** | **~974** | **~63% reduction** | **~356-481** | **~30.5-41.5M** |

### Key Takeaway

| Metric | Original | Adjusted | Change |
|--------|---------|---------|--------|
| Combined avg TPS | ~800-1,000 | ~350-480 | -52% to -56% |
| Solana share of total | ~70% | ~43-58% | Still dominant but less so |
| Annual transactions | ~25-30B | ~11-15B | Roughly halved |
| Solana "Visa comparison" | ~694 TPS vs Visa ~1,700 | ~153-278 TPS | Well below Visa |

**The adjusted global blockchain TPS of ~350-480 is roughly 1.7-2.3% of Visa/Mastercard combined throughput (~21,000 TPS), compared to the headline ~4.6% figure. This is a more honest comparison.**

---

## Methodological Notes

1. **Vote transaction filtering** is the most defensible adjustment. Solana's own explorer (Solscan) and analytics tools (SolanaCompass, Dune) separate vote from non-vote transactions natively.

2. **Failed transaction filtering** is well-supported. Solana records failed transactions on-chain, unlike most other chains where failed transactions are dropped from the canonical count. The ~40-50% failure rate is documented by multiple sources.

3. **MEV/bot filtering** is the most subjective. Some MEV activity (e.g., DEX arbitrage that improves price efficiency) arguably represents genuine economic activity. Our 20-30% estimate for "pure spam" is conservative.

4. **Inscriptions on Bitcoin** are debatable. They are paid-for blockspace usage, economically real, but not monetary transfers. We present the adjustment but acknowledge inscriptions have legitimate value.

5. **L2 adjustments** are the least confident. Data on L2 bot activity is fragmented and rapidly changing as L2s implement anti-spam measures.

---

## Sources

- [Solana Compass Statistics](https://solanacompass.com/statistics) — real-time vote/non-vote TPS breakdown
- [Solscan Analytics](https://solscan.io/analytics) — vote vs non-vote transaction charts
- [Dune: Solana Daily TPS (Non-Vote)](https://dune.com/queries/1454081)
- [Dune: Solana Non-Vote Transactions per day](https://dune.com/queries/400051)
- [The Block: Solana validator count falls, vote transactions drop 40%](https://www.theblock.co/post/387108/solana-validator-count-below-800-vote-transactions-drop-40)
- [KuCoin: Solana Daily Non-Vote Transactions Hit 148 Million](https://www.kucoin.com/news/articles/solana-daily-non-vote-transactions-hit-148-million-milestones-and-challenges-for-high-performance-blockchains)
- [Helius: Solana MEV Report](https://www.helius.dev/blog/solana-mev-report)
- [BeInCrypto: Meme Coins Push Solana to Limit — 77% Failed Transactions](https://beincrypto.com/meme-coin-solana-transaction-failure/)
- [Cointelegraph: Solana struggles — 75% of user txns failing](https://cointelegraph.com/news/solana-struggling-record-seventy-five-percent-trasnactions-fail-memecoin-mania)
- [Flashbots / AInvest: MEV Spam Consumes 40% of Solana Blockspace, 50% of Ethereum L2s](https://www.ainvest.com/news/mev-spam-consumes-40-solana-blockspace-50-ethereum-l2s-2506/)
- [Bitget: Solana Faces Scrutiny Over Transaction Metrics Inflated by Bot Activity](https://www.bitget.com/news/detail/12560604951556)
- [AMBCrypto: Solana 3.3K TPS — masking weak protocol revenue?](https://ambcrypto.com/solana-is-3-3k-tps-strength-masking-sols-weak-protocol-revenue/)
- [Everstake: Solana Staking Insights — First Half 2025](https://everstake.one/crypto-reports/solana-staking-insights-and-analysis-first-half-of-2025)
- [Chainspect: Solana TPS](https://chainspect.app/chain/solana)
- [Glassnode: Ordinal Theory and the Rise of Inscriptions](https://insights.glassnode.com/ordinal-theory-and-the-rise-of-inscriptions/)
- [Social Capital Markets: Bitcoin Ordinals Statistics 2024](https://socialcapitalmarkets.net/crypto-trading/bitcoin-ordinals-statistics/)
- [Flashbots: MEV bots clogging blockchains faster than networks can scale](https://www.theblock.co/post/358512/mev-bots-are-clogging-blockchains-faster-than-networks-can-scale-says-flashbots)

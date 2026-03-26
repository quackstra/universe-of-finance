# Last Session Notes — 2026-03-26

## Capsules Produced: 24 (across 2 sessions)

First session (interrupted by rate limit): 5 capsules
Second session (resumed): 19 capsules

## Categories Researched

### Payments (6)
- **consumer-cards**: Full capsule — 24,501 avg TPS, 772.7B annual txns. Visa/UnionPay/Mastercard triopoly.
- **digital-wallets**: Full capsule — 19,660 avg TPS, 620B annual txns. UPI is the global champion at 172B txns/year.
- **bank-transfers**: Full capsule — 15,338 avg TPS, 484B annual txns. Real-time payments growing fast.
- **ecommerce**: Full capsule — ~1,800 avg TPS, ~57.5B annual txns. Heavy overlap with card payments.
- **p2p-transfers**: Full capsule — 270 avg TPS, 8.5B annual txns. Zelle hit $1T in 2024.
- **remittances**: Full capsule — 57 avg TPS, 1.8B annual txns. Value data is strong but txn counts are a data gap.

### Traditional Finance (6)
- **etd**: Full capsule — ~9,500 avg TPS, 205.3B contracts. 6th consecutive annual record, +51% YoY.
- **equity-markets**: Full capsule — ~3,500 avg TPS (trading hours), 61.5B trades. India +74.3% YoY surge.
- **commodities**: Full capsule — ~330 avg TPS, ~10.4B contracts. CME, ICE, LME dominate.
- **forex**: Full capsule — ~35 avg TPS, ~750M trades. $9.6T daily turnover but low txn count.
- **fixed-income**: Full capsule — ~7 avg TPS (cash bonds), ~220M trades. Bonds rarely trade.
- **otc-derivatives**: Full capsule — ~0.6 avg TPS, ~15M trades. Lowest TPS despite $665T notional.

### Digital Assets (4)
- **cex**: Full capsule — ~4,000 avg TPS (est.), $77.3T combined volume. Wash trading flagged.
- **blockchain-l1-l2**: Full capsule — ~900 avg TPS, ~27B on-chain txns. Solana dominates by count.
- **defi**: Full capsule — $4.16T DEX volume. Subset of L1/L2. DEX-to-CEX ratio growing.
- **stablecoins**: Full capsule — ~520 avg TPS, $27.6T raw volume. Subset of L1/L2.

### Banking (2)
- **interbank-rtgs**: Full capsule — 13.4 avg TPS, 423M txns, $2,150T value. CLS is the hidden giant.
- **securities-settlement**: Full capsule — ~41-48 avg TPS, ~1.3-1.5B txns, $3.7 quadrillion (DTCC alone).

### Gaming (2)
- **gaming-microtx**: Full capsule — ~389 avg TPS, ~12.3B txns, $114B. Mobile dominates.
- **gaming-sales**: Full capsule — ~92 avg TPS, ~2.9B txns, $60.2B. Digital 84-96%.

### Government (1)
- **government-payments**: Full capsule — ~793 avg TPS, ~25B txns. Benefits disbursements dominate count.

### Emerging (3)
- **iot-m2m**: Full capsule — ~634 avg TPS, ~20B txns. Already large but invisible.
- **rwa-tokenisation**: Full capsule — ~2.4 avg TPS, ~75M txns. $24B TVL, growing fast.
- **ai-agents**: Full capsule — ~0.66 avg TPS. Most speculative category. x402 data available.

## Key Findings
- **Consumer cards + digital wallets + bank transfers account for ~80% of global financial TPS**
- The "Big Number" first-pass estimate is ~76,000 TPS across non-overlapping categories
- Double-counting between digital wallets and card payments is the biggest methodological challenge
- Value and count rankings diverge dramatically (forex is massive by value, tiny by count)
- UPI (India) alone processes more transactions than all global equity markets combined

## Taxonomy Changes
- No changes to TAXONOMY.md needed — all 24 categories fit well
- Potential future addition: "Insurance Premiums" (not currently tracked)
- Potential future addition: "Payroll Payments" (currently lumped into bank transfers)

## Issues Found in Prior Research
- None (first research pass)

## Unfinished Work
- data.json schemas vary across agents — need normalisation pass
- Some capsules have more detailed projections than others
- Historic data for many categories only goes back to 2019 (protocol requests deeper historics for inside-out expansion)
- Double-counting quantification needed: how much of digital wallets is truly incremental vs. card-rail overlap?

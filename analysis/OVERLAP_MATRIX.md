# Universe of Finance — Global Overlap Matrix & De-Duplicated TPS

> Cross-category overlap analysis for accurate total global financial TPS.
> **Last Updated**: 2026-03-27 (Run 3 reconciliation)

## The Big Number (De-Duplicated)

**Estimated Global Financial TPS: ~70,700** (non-overlapping, all sectors)

This is derived by summing de-duplicated TPS across all 7 sectors, accounting for
overlaps within payments, subsets within digital assets, and the settlement-vs-trading
boundary in banking.

---

## Sector-by-Sector De-Duplication

### 1. Payments — ~53,200 TPS (de-duplicated)

See [payments/OVERLAP_ANALYSIS.md](payments/OVERLAP_ANALYSIS.md) for full methodology.

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| Consumer Cards | 24,501 | 24,501 | Base layer |
| Bank Transfers | 15,338 | 15,338 | Base layer (includes UPI) |
| Digital Wallets | 19,660 | 12,930 | Minus UPI (in bank transfers) and card-rail wallets |
| E-Commerce | 1,800 | 143 | ~95% overlay on cards/wallets/bank |
| P2P Transfers | 270 | 254 | Minor wallet overlap |
| Remittances | 57 | 32 | Minor bank/P2P overlap |
| **Payments Total** | **61,626** | **53,198** | **14% overcount in raw sum** |

### 2. Traditional Finance — ~13,400 TPS

No significant intra-sector overlaps. ETD and OTC derivatives are distinct markets
(exchange-traded vs. bilateral). Forex is independent of equity/bond trading.

| Category | TPS | Notes |
|----------|-----|-------|
| Exchange-Traded Derivatives | 9,500 | Independent — futures/options on exchanges |
| Equity Markets | 3,500 | Independent — stock trades |
| Commodities | 330 | Independent — commodity futures |
| Foreign Exchange | 35 | Independent — currency trades (high-value, low-count) |
| Fixed Income (cash bonds) | 7 | Independent — bond trades |
| OTC Derivatives | 0.6 | Independent — bilateral contracts |
| **TradFi Total** | **~13,373** | **No intra-sector overlaps** |

**Cross-sector overlap with Payments**: Minimal. TradFi transactions settle through
banking infrastructure (RTGS, CSD) but are counted separately per taxonomy rules.
The settlement is downstream, not a duplicate of the trade.

### 3. Digital Assets — ~3,515 TPS (de-duplicated)

Critical overlap: DeFi and Stablecoins are *subsets* of L1/L2 on-chain transactions.
CEX trades are off-chain (no overlap with L1/L2).

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| CEX (wash-adjusted) | 3,100 | 3,100 | Off-chain, no L1/L2 overlap |
| L1/L2 Blockchain | 415 | 0 | *Subsumed — DeFi + Stablecoins + other on-chain ARE L1/L2* |
| DeFi | *(subset)* | *(included in L1/L2)* | ~30-40% of L1/L2 transactions |
| Stablecoins | *(subset)* | *(included in L1/L2)* | ~15-25% of L1/L2 transactions |
| **Digital Assets Total** | — | **~3,515** | **CEX + L1/L2 (which contains DeFi + stablecoins)** |

The correct de-duplication is: CEX (off-chain, 3,100 TPS) + L1/L2 (on-chain, 415 TPS) = **3,515 TPS**.
DeFi and Stablecoins don't add because they're subsets of L1/L2.

**Run 3 revision**: L1/L2 TPS revised from ~900 to ~415 (range: 350-480) after filtering
Solana vote transactions (~35% of total), failed transactions (~35% of non-vote), and
MEV bot spam (~25% of successful non-vote). See `digital-assets/blockchain-l1-l2/workings/solana-filter.md`.

### 4. Banking — ~92-98 TPS (de-duplicated)

| Category | TPS | Notes |
|----------|-----|-------|
| Securities Settlement | 41-48 | Downstream of equity/bond/derivative trades |
| Interbank RTGS | 50.1 | Settlement of high-value payments (13 systems) |
| **Banking Total** | **~92-98** |

**Run 3 revision**: Interbank RTGS expanded from 5 systems (Fedwire, T2, CHAPS, BOJ-NET, CLS)
to 13 systems, adding CNAPS-HVPS (China), India RTGS, SARIE (Saudi Arabia), BOK-Wire+,
RITS (Australia), Lynx (Canada), MEPS+ (Singapore), and Russia BESP. Annual volume tripled
from ~423M to ~1,581M transactions. See `banking/interbank-rtgs/workings/missing-systems.md`. |

**Cross-sector note**: Banking transactions are the settlement layer for TradFi and
Payments. Per taxonomy double-counting rules, a stock trade counts as ONE trade
(in Equity Markets) and the resulting settlement counts separately (in Securities
Settlement). Both are real transactions on different infrastructure.

### 5. Gaming — ~481 TPS

| Category | TPS | Notes |
|----------|-----|-------|
| Microtransactions | 389 | ~65-75% paid via card rails (overlap with Payments) |
| Game Sales | 92 | ~70-80% paid via card rails |
| **Gaming Total** | **~481** | |

**Cross-sector overlap with Payments**: Gaming purchases (~10-11.5B/year) are paid
via cards/wallets/bank transfers. These payment transactions are ALREADY counted in
the Payments sector. Gaming counts the **commerce events**, not the payment flows.
For pure TPS aggregation, gaming should be treated as a commerce layer (like e-commerce)
unless we want to count the economic activity rather than payment infrastructure throughput.

**Decision**: Exclude gaming from the "payment TPS" total but include in the
"economic transaction TPS" total.

### 6. Government — ~1,002 TPS

| Category | TPS | Notes |
|----------|-----|-------|
| Government Payments | 1,002 | Tax receipts + benefits disbursements (bottom-up model) |
| **Government Total** | **~1,002** | |

**Run 3 revision**: Bottom-up model across US (5.09B txns), India (8.19B), EU (5.84B),
and tiered RoW extrapolation yields ~31.6B annual transactions (up from ~25B). India's
JAM-enabled DBT platform alone accounts for 7.4B transactions. Confidence upgraded from
Low to Medium. See `government/government-payments/workings/bottom-up-model.md`.

**Cross-sector overlap with Payments**: Benefits disbursements flow through ACH/bank
transfers; tax payments through cards/bank transfers. Like gaming and e-commerce,
government payments are economic events paid via existing payment rails.

**Decision**: Partially overlapping with bank transfers. Estimate ~60% of government
payment transactions are already counted in bank transfers (ACH disbursements).
Incremental: ~401 TPS.

### 7. Emerging — ~637 TPS

| Category | TPS | Notes |
|----------|-----|-------|
| IoT/M2M | 634 | Most ride on card/bank rails |
| RWA Tokenisation | 2.4 | On-chain (subset of L1/L2) |
| AI Agents | 0.66 | Mostly on-chain (x402) |
| **Emerging Total** | **~637** | |

**Cross-sector overlap**: IoT payments (~70-80%) ride on existing card/bank rails.
RWA and AI agent transactions are on-chain (subset of L1/L2). Incremental emerging
TPS: ~127-190 (IoT non-card portion only).

---

## De-Duplicated Global Total

### Method A: Payment Infrastructure TPS (what rails actually process)

This counts only the throughput on payment/settlement infrastructure, avoiding
double-counting commerce layers (e-commerce, gaming, government, IoT) that ride
on those rails.

| Sector | De-Dup TPS | Notes |
|--------|-----------|-------|
| Payments (de-dup) | 53,200 | Cards + Bank Transfers + incremental Wallets |
| Traditional Finance | 13,373 | Trading activity on exchanges/OTC |
| Digital Assets | 3,515 | CEX (off-chain) + L1/L2 (on-chain, vote/spam filtered) |
| Banking/Settlement | 95 | RTGS (13 systems) + Securities Settlement |
| **Total** | **~70,200** | |

### Method B: Economic Transaction TPS (all unique economic events)

This counts every unique economic event once, regardless of payment rail.
Includes commerce layers but de-duplicates payment overlaps.

| Sector | De-Dup TPS | Notes |
|--------|-----------|-------|
| Payments (de-dup) | 53,200 | |
| Traditional Finance | 13,373 | |
| Digital Assets | 3,515 | |
| Banking/Settlement | 95 | |
| Gaming (incremental) | 481 | Commerce events (payment already in Payments) |
| Government (incremental) | 401 | ~40% not in bank transfers |
| IoT/M2M (incremental) | 159 | ~25% not on existing rails |
| RWA + AI Agents | 3 | On-chain but tiny |
| **Total** | **~71,200** | |

### The Range

| Metric | Low Estimate | Central | High Estimate |
|--------|-------------|---------|---------------|
| Payment Infrastructure TPS | 64,000 | 70,200 | 78,000 |
| Economic Transaction TPS | 65,000 | 71,200 | 80,000 |

The ~1,000 TPS gap between Method A and Method B reflects commerce layers
(gaming, government, IoT) that generate real economic events but whose
payment flows are already counted in the Payments sector.

### Programmatic Validation

`tools/big_number.py` computes **~70,741 TPS** de-duplicated. This sits between
Method A (~70,200) and Method B (~71,200) because the script includes government
and IoT incremental contributions but excludes gaming, RWA, and AI agents. The
~500 TPS gap between the script and Method A is the government (401 TPS) and
IoT (159 TPS) incrementals minus rounding differences. All three figures are
internally consistent.

---

## Key Insights

1. **Payments dominate**: 76% of global financial TPS is payment transactions
   (cards, bank transfers, wallets). Trading, settlement, and everything else is 24%.

2. **The overlap problem is smaller than feared**: Raw sum across all 24 categories
   would yield ~81,000+ TPS. De-duplication reduces this by ~13% to ~70,200.
   The biggest single overlap is UPI (172B transactions in both wallets and bank transfers).

3. **E-commerce is NOT a payment category**: It's a commerce layer. 95% of e-commerce
   payment flows are already counted in cards/wallets/bank transfers. Same applies
   to gaming and government payments.

4. **Digital assets are smaller than headline numbers suggest**: At ~3,515 TPS
   (after Solana vote/spam filtering), crypto (CEX + on-chain) is ~5% of global
   financial TPS. Solana's headline ~900 TPS drops to ~350-480 after removing vote
   transactions, failed transactions, and MEV spam.

5. **TradFi trading is surprisingly large**: At ~13,400 TPS, trading (especially
   derivatives at 9,500 TPS) is a bigger transaction generator than most people realise.
   ETD volume has been growing ~15%+ annually.

6. **Interbank settlement is larger than previously captured**: Expanding from 5 to 13
   RTGS systems tripled the count from ~423M to ~1,581M annual transactions. China's
   CNAPS-HVPS (382M) and India's RTGS (295M) are both larger than any Western system
   except Fedwire.

7. **Government payments are higher than top-down estimates**: Bottom-up modelling
   reveals ~31.6B annual transactions (up from ~25B), driven by India's DBT platform
   (7.4B transactions across 1,206+ schemes) and EU social security contributions.

---

*This analysis will be refined as individual capsule data improves. Key uncertainties:
China digital wallet volume (±50B), CEX wash trading adjustment (±30%), and
IoT payment rail attribution.*

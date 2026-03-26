# Universe of Finance — Global Overlap Matrix & De-Duplicated TPS

> Cross-category overlap analysis for accurate total global financial TPS.
> **Last Updated**: 2026-03-26 (Run 2)

## The Big Number (De-Duplicated)

**Estimated Global Financial TPS: ~68,000** (non-overlapping, all sectors)

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

### 3. Digital Assets — ~3,100 TPS (de-duplicated)

Critical overlap: DeFi and Stablecoins are *subsets* of L1/L2 on-chain transactions.
CEX trades are off-chain (no overlap with L1/L2).

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| CEX (wash-adjusted) | 3,100 | 3,100 | Off-chain, no L1/L2 overlap |
| L1/L2 Blockchain | 900 | 0 | *Subsumed — DeFi + Stablecoins + other on-chain ARE L1/L2* |
| DeFi | *(subset)* | *(included in L1/L2)* | ~30-40% of L1/L2 transactions |
| Stablecoins | *(subset)* | *(included in L1/L2)* | ~15-25% of L1/L2 transactions |
| **Digital Assets Total** | — | **~4,000** | **CEX + L1/L2 (which contains DeFi + stablecoins)** |

Wait — the correct de-duplication is: CEX (off-chain, 3,100 TPS) + L1/L2 (on-chain, 900 TPS) = **4,000 TPS**.
DeFi and Stablecoins don't add because they're subsets of L1/L2.

### 4. Banking — ~55 TPS (de-duplicated)

| Category | TPS | Notes |
|----------|-----|-------|
| Securities Settlement | 41-48 | Downstream of equity/bond/derivative trades |
| Interbank RTGS | 13.4 | Settlement of high-value payments |
| **Banking Total** | **~55-61** | |

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

### 6. Government — ~793 TPS

| Category | TPS | Notes |
|----------|-----|-------|
| Government Payments | 793 | Tax receipts + benefits disbursements |
| **Government Total** | **~793** | |

**Cross-sector overlap with Payments**: Benefits disbursements flow through ACH/bank
transfers; tax payments through cards/bank transfers. Like gaming and e-commerce,
government payments are economic events paid via existing payment rails.

**Decision**: Partially overlapping with bank transfers. Estimate ~60% of government
payment transactions are already counted in bank transfers (ACH disbursements).
Incremental: ~317 TPS.

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
| Digital Assets | 4,000 | CEX (off-chain) + L1/L2 (on-chain) |
| Banking/Settlement | 55 | RTGS + Securities Settlement |
| **Total** | **~70,600** | |

### Method B: Economic Transaction TPS (all unique economic events)

This counts every unique economic event once, regardless of payment rail.
Includes commerce layers but de-duplicates payment overlaps.

| Sector | De-Dup TPS | Notes |
|--------|-----------|-------|
| Payments (de-dup) | 53,200 | |
| Traditional Finance | 13,373 | |
| Digital Assets | 4,000 | |
| Banking/Settlement | 55 | |
| Gaming (incremental) | 481 | Commerce events (payment already in Payments) |
| Government (incremental) | 317 | ~40% not in bank transfers |
| IoT/M2M (incremental) | 150 | ~25% not on existing rails |
| RWA + AI Agents | 3 | On-chain but tiny |
| **Total** | **~71,600** | |

### The Range

| Metric | Low Estimate | Central | High Estimate |
|--------|-------------|---------|---------------|
| Payment Infrastructure TPS | 65,000 | 70,600 | 78,000 |
| Economic Transaction TPS | 66,000 | 71,600 | 80,000 |

The ~5,000 TPS gap between Method A and Method B reflects commerce layers
(gaming, government, IoT) that generate real economic events but whose
payment flows are already counted in the Payments sector.

---

## Key Insights

1. **Payments dominate**: 75% of global financial TPS is payment transactions
   (cards, bank transfers, wallets). Trading, settlement, and everything else is 25%.

2. **The overlap problem is smaller than feared**: Raw sum across all 24 categories
   would yield ~82,000+ TPS. De-duplication reduces this by ~13-15% to ~70,600.
   The biggest single overlap is UPI (172B transactions in both wallets and bank transfers).

3. **E-commerce is NOT a payment category**: It's a commerce layer. 95% of e-commerce
   payment flows are already counted in cards/wallets/bank transfers. Same applies
   to gaming and government payments.

4. **Digital assets are small but unique**: At ~4,000 TPS, crypto (CEX + on-chain)
   is ~6% of global financial TPS. But it operates on entirely different infrastructure
   with zero overlap to traditional payment rails.

5. **TradFi trading is surprisingly large**: At ~13,400 TPS, trading (especially
   derivatives at 9,500 TPS) is a bigger transaction generator than most people realise.
   ETD volume has been growing ~15%+ annually.

---

*This analysis will be refined as individual capsule data improves. Key uncertainties:
China digital wallet volume (±50B), CEX wash trading adjustment (±30%), and
IoT payment rail attribution.*

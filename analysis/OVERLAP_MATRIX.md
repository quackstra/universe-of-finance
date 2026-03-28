# Universe of Finance — Global Overlap Matrix & De-Duplicated TPS

> Cross-category overlap analysis for accurate total global financial TPS.
> **Last Updated**: 2026-03-28 (Run 6 — full 29-category reconciliation)

## The Big Number (De-Duplicated)

**Estimated Global Financial TPS: ~73,750** (non-overlapping, all 29 categories)

This is derived by summing de-duplicated TPS across all 7 sectors, accounting for
overlaps within payments, subsets within digital assets, and the settlement-vs-trading
boundary in banking.

---

## Sector-by-Sector De-Duplication

### 1. Payments — ~55,690 TPS (de-duplicated)

See [payments/OVERLAP_ANALYSIS.md](payments/OVERLAP_ANALYSIS.md) for full methodology.

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| Consumer Cards | 24,501 | 24,501 | Base layer |
| Bank Transfers | 15,338 | 15,338 | Base layer (includes UPI) |
| Digital Wallets | 19,660 | 12,938 | Minus UPI (in bank transfers) and card-rail wallets |
| ATM Withdrawals | 1,557 | 1,557 | **Zero overlap** — cash-out, unique event type |
| BNPL | 634 | 460 | 100% infra overlap, but 3.6x multiplier → ~460 TPS incremental |
| Bill Payments | 3,012 | 301 | ~90% via direct debit/card-on-file rails |
| E-Commerce | 1,823 | 91 | ~95% overlay on cards/wallets/bank |
| P2P Transfers | 270 | 270 | Minor wallet overlap |
| Payroll | 1,305 | 131 | ~90% is ACH/BACS/SEPA batch (in bank transfers) |
| Insurance Premiums | 444 | 44 | ~90% via card/direct debit rails |
| Remittances | 57 | 57 | Minor bank/P2P overlap |
| **Payments Total** | **68,601** | **55,688** | **19% overcount in raw sum** |

### 2. Traditional Finance — ~13,473 TPS

No significant intra-sector overlaps. ETD and OTC derivatives are distinct markets
(exchange-traded vs. bilateral). Forex is independent of equity/bond trading.

| Category | TPS | Notes |
|----------|-----|-------|
| Exchange-Traded Derivatives | 9,505 | Independent — futures/options on exchanges |
| Equity Markets | 3,500 | Independent — stock trades |
| Commodities | 330 | Independent — commodity futures |
| Foreign Exchange | 127 | **Revised Run 5**: incl. ~8M retail trades/day (was ~35 institutional-only) |
| Fixed Income (incl. repo) | 10.5 | **Revised Run 5**: incl. 219M repo transactions (was ~3.6 cash-only) |
| OTC Derivatives | 0.2 | Independent — bilateral contracts |
| **TradFi Total** | **~13,473** | **No intra-sector overlaps** |

**Cross-sector overlap with Payments**: Minimal. TradFi transactions settle through
banking infrastructure (RTGS, CSD) but are counted separately per taxonomy rules.
The settlement is downstream, not a duplicate of the trade.

### 3. Digital Assets — ~3,625 TPS (de-duplicated)

Critical overlap: DeFi and Stablecoins are *subsets* of L1/L2 on-chain transactions.
CEX trades are off-chain (no overlap with L1/L2).

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| CEX (wash-adjusted) | 3,210 | 3,210 | Off-chain, no L1/L2 overlap. **Run 5**: revised from 3,040 |
| L1/L2 Blockchain | 415 | 415 | On-chain (DeFi + Stablecoins are subsets, not additive) |
| DeFi | *(subset)* | *(included in L1/L2)* | ~30-40% of L1/L2 transactions |
| Stablecoins | *(subset)* | *(included in L1/L2)* | ~15-25% of L1/L2 transactions |
| **Digital Assets Total** | — | **~3,625** | **CEX + L1/L2 (which contains DeFi + stablecoins)** |

The correct de-duplication is: CEX (off-chain, 3,210 TPS) + L1/L2 (on-chain, 415 TPS) = **3,625 TPS**.
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

### 5. Gaming — ~88 TPS (incremental)

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| Microtransactions | 389 | 70 | 82% on card/wallet rails → ~18% incremental |
| Game Sales | 92 | 18 | 84% on card/wallet rails → ~16% incremental |
| **Gaming Total** | **~481** | **~88** | |

**Cross-sector overlap with Payments**: Gaming purchases (~15.2B/year) are paid
via cards/wallets/bank transfers. These payment transactions are ALREADY counted in
the Payments sector. Gaming counts the **commerce events**, not the payment flows.

**Run 6 revision**: Instead of fully excluding gaming, we now count the ~18% of
gaming transactions that use non-card/non-wallet rails (gift cards, platform credit,
direct carrier billing, crypto). This gives ~88 TPS incremental.

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

### 7. Emerging — ~385 TPS (incremental)

| Category | Raw TPS | De-Dup TPS | Notes |
|----------|---------|------------|-------|
| IoT/M2M | 1,538 | 385 | **Run 5**: revised from ~634 to ~1,538; 75% on card/bank rails |
| RWA Tokenisation | 2.4 | 0 | On-chain (subset of L1/L2) |
| AI Agents | 0.66 | 0 | Mostly on-chain (x402, subset of L1/L2) |
| **Emerging Total** | **~1,541** | **~385** | |

**Cross-sector overlap**: IoT payments (~75%) ride on existing card/bank rails.
RWA and AI agent transactions are on-chain (subset of L1/L2). Incremental emerging
TPS: ~385 (IoT non-card portion only).

---

## De-Duplicated Global Total

### Method A: Payment Infrastructure TPS (what rails actually process)

This counts only the throughput on payment/settlement infrastructure, avoiding
double-counting commerce layers (e-commerce, gaming, government, IoT) that ride
on those rails.

| Sector | De-Dup TPS | Notes |
|--------|-----------|-------|
| Payments (de-dup) | 55,690 | Cards + Bank Transfers + incremental Wallets + ATM + BNPL incremental + Bill/Payroll/Insurance incrementals |
| Traditional Finance | 13,473 | Trading activity on exchanges/OTC (revised forex + fixed income) |
| Digital Assets | 3,625 | CEX (off-chain, wash-adjusted) + L1/L2 (on-chain, vote/spam filtered) |
| Banking/Settlement | 94 | RTGS (13 systems) + Securities Settlement |
| **Total** | **~72,880** | |

### Method B: Economic Transaction TPS (all unique economic events)

This counts every unique economic event once, regardless of payment rail.
Includes commerce layers but de-duplicates payment overlaps.

| Sector | De-Dup TPS | Notes |
|--------|-----------|-------|
| Payments (de-dup) | 55,690 | |
| Traditional Finance | 13,473 | |
| Digital Assets | 3,625 | |
| Banking/Settlement | 94 | |
| Gaming (incremental) | 88 | ~18% not on card/wallet rails |
| Government (incremental) | 401 | ~40% not in bank transfers |
| IoT/M2M (incremental) | 385 | ~25% not on existing rails |
| RWA + AI Agents | 3 | On-chain but tiny |
| **Total** | **~73,760** | |

### The Range

| Metric | Low Estimate | Central | High Estimate |
|--------|-------------|---------|---------------|
| Payment Infrastructure TPS | 66,000 | 72,900 | 82,000 |
| Economic Transaction TPS | 67,000 | 73,750 | 83,000 |

The ~870 TPS gap between Method A and Method B reflects commerce/activity layers
(gaming, government, IoT) that generate real economic events but whose
payment flows are already counted in the Payments sector.

### Programmatic Validation

`tools/big_number.py` computes **~73,753 TPS** de-duplicated across all 29 categories.
This aligns with Method B (~73,760) because the script now includes all incremental
contributions: gaming (88), government (401), IoT (385), plus the 5 new payment
categories with deductions. All three figures are internally consistent.

### Run 6 vs Run 3 Reconciliation

| Change | Impact |
|--------|--------|
| 5 new payment categories (ATM, bills, payroll, insurance, BNPL) | +2,493 TPS (after deductions) |
| Gaming: exclude → incremental | +88 TPS |
| Forex: institutional → incl. retail | +87 TPS |
| Fixed income: cash → incl. repo | +6.9 TPS |
| CEX wash adjustment: 3,040 → 3,210 | +110 TPS (already in Run 5) |
| IoT: 634 → 1,538 (×0.25) | +226 TPS (already in Run 5) |
| **Net change from Run 3 (~70,741)** | **+~3,012 TPS → ~73,753** |

---

## New Category Overlap Details (Run 6)

### Gaming Overlap

- **Raw TPS**: ~481 (microtx 389 + sales 92)
- **Overlap**: 82% of gaming transactions settle on card/wallet rails
- **Incremental**: ~88 TPS (gift cards, platform credit, carrier billing, crypto)
- **Rationale**: Gaming is a commerce layer like e-commerce. Most purchases use
  cards (40-50%), digital wallets (25-30%), or bank transfers (5-10%). The ~18%
  incremental comes from platform-specific payment methods not captured elsewhere.

### Insurance Premium Overlap

- **Raw TPS**: ~444 (14B annual premium payments)
- **Overlap**: 90% flows via card auto-pay or direct debit/ACH
- **Incremental**: ~44 TPS (~1.4B transactions via cash/agent collections)
- **Rationale**: Most insurance premiums are recurring payments on existing rails.
  Cash premium collection (common in India, Africa) is the only incremental portion.

### BNPL Overlap

- **Raw TPS**: ~634 (installment-level, 20B events/year)
- **Overlap**: 100% infrastructure overlap — every installment settles via card or bank
- **Incremental**: ~460 TPS (~14.5B net new payment events)
- **Rationale**: BNPL is unique — it has complete infrastructure overlap but creates
  genuine new transaction events. A single purchase becomes 3-4 installment payments
  on the underlying rail. The 5.5B purchases would have been 5.5B card transactions
  anyway; the ~14.5B additional installment events (20B - 5.5B) are net new TPS on
  the payment infrastructure.

### Bill Payments Overlap

- **Raw TPS**: ~3,012 (95B annual bill payments)
- **Overlap**: 90% flows via direct debit, card-on-file, or mobile money
- **Incremental**: ~301 TPS (~9.5B cash/check bill payments)
- **Rationale**: Utility bills, telecom, and digital subscriptions are overwhelmingly
  paid via automated channels already counted in bank transfers (direct debit) or
  consumer cards (card-on-file). Cash bill payments at agent networks (common in
  emerging markets) are the incremental portion.

### Payroll Overlap

- **Raw TPS**: ~1,305 (41.2B annual payroll disbursements)
- **Overlap**: 90% is ACH/BACS/SEPA batch transfers already in bank transfers
- **Incremental**: ~131 TPS (~4.2B cash wages and check payroll)
- **Rationale**: Formal-sector payroll is essentially a subset of bank transfers.
  The ~10% incremental represents cash wages (informal sector, emerging markets)
  and remaining check payroll (declining in developed markets).

### ATM Withdrawals (Zero Overlap)

- **Raw TPS**: ~1,557 (49.1B annual cash withdrawals)
- **Overlap**: 0% — ATM withdrawals are cash-out events, not payments
- **Incremental**: ~1,557 TPS (full count)
- **Rationale**: ATM cash withdrawals create a unique transaction type not captured
  anywhere else. They use card rails for authentication but the transaction itself is
  a cash disbursement. When the consumer later spends that cash, the spending is
  untracked. Card network statistics exclude ATM withdrawals from purchase counts.

---

## Key Insights

1. **Payments dominate**: 75% of global financial TPS is payment transactions
   (cards, bank transfers, wallets, ATM, bills, payroll, BNPL, insurance). Trading, settlement, and everything else is 25%.

2. **The overlap problem is material but manageable**: Raw sum across all 29 categories
   yields ~89,300 TPS. De-duplication reduces this by ~17% to ~73,750.
   The biggest single overlap is UPI (172B transactions in both wallets and bank transfers).

3. **ATM withdrawals are a significant overlooked category**: At ~1,557 TPS with zero
   overlap, ATM cash-outs are the third-largest payment category by TPS and are
   entirely incremental to the total.

4. **BNPL creates genuine new infrastructure load**: Despite 100% infrastructure overlap,
   the 3.6x installment multiplier generates ~14.5B net new payment events (~460 TPS).
   This is a rare case where overlap does not mean deduction.

5. **Bill payments are massive but mostly captured**: At ~95B annual transactions (~3,012 TPS),
   bill payments are a huge category but ~90% flows through direct debit and card-on-file
   rails already counted elsewhere.

6. **Digital assets are smaller than headline numbers suggest**: At ~3,625 TPS
   (after Solana vote/spam filtering and CEX wash adjustment), crypto is ~5% of global
   financial TPS.

7. **TradFi trading is surprisingly large**: At ~13,473 TPS, trading (especially
   derivatives at 9,505 TPS) is a bigger transaction generator than most people realise.
   Forex revised upward to ~127 TPS (from ~35) with retail inclusion; fixed income
   revised to ~10.5 TPS (from ~3.6) with repo inclusion.

8. **IoT is growing fast**: Revised from ~634 to ~1,538 TPS in Run 5, with toll
   collection and vending machines as the dominant segments. After 75% rail overlap
   deduction, contributes ~385 TPS incremental.

---

*This analysis will be refined as individual capsule data improves. Key uncertainties:
China digital wallet volume (±50B), CEX wash trading adjustment (±30%),
bill payment cash/digital split (±10%), and IoT payment rail attribution.*

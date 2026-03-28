# Digital Game Sales & Subscriptions — Payment Overlap Analysis

> Quantifies how digital game purchases and subscription payments overlap with other
> payment categories in the Universe of Finance taxonomy.

## 1. The Core Question

When a consumer buys a $60 game on Steam or renews their $15/month Game Pass subscription,
that payment uses an existing payment rail (card, wallet, bank transfer). Is this transaction
already counted in another capsule?

**Yes — almost entirely.** Game sales and subscription payments are commerce transactions
that flow through existing payment infrastructure.

## 2. Payment Channel Decomposition

### Full Game Purchases (~2.13B transactions, $52B revenue)

#### PC Digital Games (~840M transactions, $21B)

| Payment Method | Share | Est. Txns (M) | Also Counted In |
|----------------|-------|--------------|-----------------|
| Card-on-file (Steam, Epic, GOG) | ~55% | ~462 | Consumer Cards |
| PayPal | ~18% | ~151 | Digital Wallets |
| Platform wallet (Steam Wallet) | ~10% | ~84 | Counted at wallet top-up |
| Bank transfer / iDEAL / Sofort | ~8% | ~67 | Bank Transfers |
| Gift cards | ~5% | ~42 | Counted at original purchase |
| Other | ~4% | ~34 | Various |

#### Console Digital Games (~633M transactions, $28.5B)

| Payment Method | Share | Est. Txns (M) | Also Counted In |
|----------------|-------|--------------|-----------------|
| Card-on-file | ~72% | ~456 | Consumer Cards |
| PayPal | ~10% | ~63 | Digital Wallets |
| Platform wallet / store credit | ~8% | ~51 | Counted at wallet top-up |
| Gift cards (PSN/Xbox/Nintendo) | ~8% | ~51 | Counted at original purchase |
| Other | ~2% | ~13 | Various |

#### Mobile Premium Games (~500M transactions, $2.5B)

| Payment Method | Share | Est. Txns (M) | Also Counted In |
|----------------|-------|--------------|-----------------|
| Card-on-file | ~55% | ~275 | Consumer Cards |
| Apple Pay / Google Pay | ~15% | ~75 | Digital Wallets + Cards |
| Carrier billing | ~12% | ~60 | None — telecom rails |
| PayPal / wallet | ~8% | ~40 | Digital Wallets |
| Gift cards | ~5% | ~25 | Counted at original purchase |
| Bank transfer | ~3% | ~15 | Bank Transfers |
| Other | ~2% | ~10 | Various |

### Subscription Renewals (~0.76B transactions, $8.2B)

| Payment Method | Share | Est. Txns (M) | Also Counted In |
|----------------|-------|--------------|-----------------|
| Card-on-file (recurring charge) | ~75% | ~570 | Consumer Cards |
| PayPal (recurring) | ~12% | ~91 | Digital Wallets |
| Platform wallet / balance | ~5% | ~38 | Counted at wallet top-up |
| Gift cards / prepaid codes | ~5% | ~38 | Counted at original purchase |
| Bank transfer / direct debit | ~3% | ~23 | Bank Transfers |

## 3. Aggregate Overlap Summary

| Payment Rail | Game Purchases (M) | Subscriptions (M) | Total (M) | % of 2.89B |
|-------------|-------------------|-------------------|-----------|------------|
| **Card rails (direct)** | 1,193 | 570 | **1,763** | **61.0%** |
| **Card rails (via wallet)** | 75 | 0 | **75** | **2.6%** |
| **Digital wallets (non-card)** | 254 | 91 | **345** | **11.9%** |
| **Carrier billing** | 60 | 0 | **60** | **2.1%** |
| **Gift cards / store credit** | 118 | 38 | **156** | **5.4%** |
| **Bank transfer** | 82 | 23 | **105** | **3.6%** |
| **Platform wallet (pre-funded)** | 135 | 38 | **173** | **6.0%** |
| **Other** | 57 | 0 | **57** | **2.0%** |
| **TOTAL** | **2,130** | **760** | **2,890** | **100%** |

## 4. Overlap with Consumer Cards

**Total game sales/subs on card rails: 1,763M (direct) + 75M (via wallet) = 1,838M**

This represents **63.6%** of all digital game sales and subscription transactions.

These ~1.84B transactions are already included in the 772.7B consumer card total.
Game sales represent **0.24%** of all card transactions — negligible at the card network level.

## 5. Overlap with Digital Wallets

**Total via wallets: 75M (card-funded) + 345M (non-card) = 420M**

Of these:
- 75M are Apple Pay/Google Pay on card rails (triple-counted: game sales + wallets + cards)
- 345M are PayPal/non-card wallets (double-counted: game sales + wallets)

## 6. Incremental (Truly Unique) Transactions

| Source | Txns (M) | Why Incremental |
|--------|----------|-----------------|
| Carrier billing | 60 | Telecom rails |
| Gift card redemptions | 156 | Original purchase counted, redemption is new |
| Platform wallet spend | 173 | Top-up counted, in-store spend is internal |
| Other | 57 | Regional/crypto methods |
| **TOTAL INCREMENTAL** | **~446M** | **15.4% of game sales transactions** |

**Key finding: ~84.6% of digital game sale and subscription transactions (2.44B) are already counted in Consumer Cards, Digital Wallets, or Bank Transfers.** Only ~446M (~15%) are truly incremental.

## 7. Combined Gaming Overlap (Microtransactions + Sales)

| Category | Annual Txns (B) | On Card Rails | On Wallet Rails | On Bank Rails | Incremental |
|----------|----------------|---------------|-----------------|---------------|-------------|
| Microtransactions | 12.28 | 8.45 (68.8%) | 2.55 (20.8%) | 0.41 (3.3%) | 2.32 (18.9%) |
| Game Sales + Subs | 2.89 | 1.84 (63.6%) | 0.42 (14.5%) | 0.11 (3.6%) | 0.45 (15.4%) |
| **COMBINED** | **15.17** | **10.29 (67.8%)** | **2.97 (19.6%)** | **0.52 (3.4%)** | **2.77 (18.3%)** |

**Of the combined 15.2B annual gaming transactions, approximately 10.3B (68%) flow through card rails and are already counted in Consumer Cards.** Only 2.8B (~18%) are truly incremental to the global payment transaction total.

## 8. Update to data.json Overlap Fields

The existing `data.json` overlap section should be updated from:
```json
"overlap_note": "70-80% of digital game sales settle on card rails"
```
to:
```json
"overlap_note": "63.6% of digital game sales settle on card rails (1.84B of 2.89B). An additional 11.9% flow through non-card digital wallets, 3.6% through bank transfers. Only ~15% (446M) are truly incremental — primarily gift card redemptions, carrier billing, and platform wallet spend."
```

## 9. Implications for De-Duplication

When aggregating the Universe of Finance TPS total:
- **Gaming microtransactions** contribute ~2.32B incremental transactions (~74 TPS)
- **Gaming sales/subs** contribute ~446M incremental transactions (~14 TPS)
- **Combined gaming increment**: ~2.77B transactions (~88 TPS)
- **Total gaming raw**: 15.17B transactions (~481 TPS)
- **Double-counted**: ~12.4B transactions (~393 TPS) already in cards/wallets/bank transfers

This is consistent with the broader pattern: **gaming is a commerce layer, not a payment layer**. Like e-commerce, the vast majority of gaming transactions flow through existing payment infrastructure.

# Gaming Microtransactions — Payment Overlap Analysis

> Quantifies how gaming microtransaction purchases overlap with other payment categories
> in the Universe of Finance taxonomy.

## 1. The Core Question

When a player buys 1,000 V-Bucks on their iPhone, three things happen:
1. Apple charges their card-on-file (Visa/MC) via the App Store
2. Apple processes the transaction through its payment system
3. Epic receives the revenue minus Apple's 30% commission

Is this one transaction or three? For our purposes, **it is one consumer payment transaction** — the player-to-platform purchase. But that single transaction may already be counted in:
- **Consumer Cards** (if paid by credit/debit card)
- **Digital Wallets** (if paid via Apple Pay, Google Pay, or PayPal)
- **Bank Transfers** (if paid via carrier billing that settles as direct debit, or open banking)

## 2. Payment Channel Decomposition

### Mobile IAP (~9.53B transactions, $81B revenue)

| Payment Method | Share of Mobile IAP Value | Est. Txns (B) | Also Counted In |
|----------------|--------------------------|---------------|-----------------|
| Card-on-file (credit/debit) | ~55% | ~5.24 | Consumer Cards |
| Apple Pay / Google Pay | ~15% | ~1.43 | Digital Wallets + Consumer Cards (wallet on card rails) |
| Carrier billing (DCB) | ~12% | ~1.14 | None — unique to telecom rails |
| PayPal / platform balance | ~8% | ~0.76 | Partially in Digital Wallets |
| Gift cards / store credit | ~5% | ~0.48 | Counted at original gift card purchase (prepaid/cards) |
| Bank transfer / open banking | ~3% | ~0.29 | Bank Transfers |
| Other (crypto, regional methods) | ~2% | ~0.19 | Various |

**Sources for payment method split:**
- Xsolla industry data: cards remain dominant for game payments globally (~55-60%)
- J.P. Morgan Payments in Gaming: digital wallets growing but card-on-file still standard
- Carrier billing: ~12% of mobile IAP (higher in SE Asia, lower in US/EU)
- Regional variation is significant: China ~80% wallet, US ~70% card, SE Asia ~30% carrier billing

### PC IAP (~1.50B transactions, $18B revenue)

| Payment Method | Share | Est. Txns (B) | Also Counted In |
|----------------|-------|---------------|-----------------|
| Card-on-file (Steam, Epic, direct) | ~60% | ~0.90 | Consumer Cards |
| PayPal | ~15% | ~0.23 | Digital Wallets |
| Platform wallet (Steam Wallet) | ~12% | ~0.18 | Counted at wallet top-up (card/bank) |
| Bank transfer / iDEAL / Sofort | ~8% | ~0.12 | Bank Transfers |
| Gift cards / prepaid | ~3% | ~0.05 | Counted at original purchase |
| Other | ~2% | ~0.02 | Various |

### Console IAP (~1.25B transactions, $15B revenue)

| Payment Method | Share | Est. Txns (B) | Also Counted In |
|----------------|-------|---------------|-----------------|
| Card-on-file (PS Store, Xbox, Nintendo) | ~70% | ~0.88 | Consumer Cards |
| PayPal | ~10% | ~0.13 | Digital Wallets |
| Platform wallet / store credit | ~10% | ~0.13 | Counted at wallet top-up |
| Gift cards (PSN, Xbox, Nintendo eShop) | ~8% | ~0.10 | Counted at original purchase |
| Other | ~2% | ~0.03 | Various |

## 3. Aggregate Overlap Summary

| Payment Rail | Mobile IAP (B) | PC IAP (B) | Console IAP (B) | Total (B) | % of 12.28B |
|-------------|---------------|------------|-----------------|-----------|-------------|
| **Card rails (direct)** | 5.24 | 0.90 | 0.88 | **7.02** | **57.2%** |
| **Card rails (via wallet)** | 1.43 | 0.00 | 0.00 | **1.43** | **11.6%** |
| **Digital wallets (non-card)** | 0.76 | 0.23 | 0.13 | **1.12** | **9.1%** |
| **Carrier billing** | 1.14 | 0.00 | 0.00 | **1.14** | **9.3%** |
| **Gift cards / store credit** | 0.48 | 0.05 | 0.10 | **0.63** | **5.1%** |
| **Bank transfer** | 0.29 | 0.12 | 0.00 | **0.41** | **3.3%** |
| **Platform wallet (funded earlier)** | 0.00 | 0.18 | 0.13 | **0.31** | **2.5%** |
| **Other** | 0.19 | 0.02 | 0.03 | **0.24** | **1.9%** |
| **TOTAL** | **9.53** | **1.50** | **1.25** | **12.28** | **100%** |

## 4. Overlap with Consumer Cards

**Total microtransactions on card rails: 7.02B (direct) + 1.43B (via wallet) = 8.45B**

This represents **68.8%** of all gaming microtransactions.

However, not all of these are double-counted in our Consumer Cards capsule:
- The 772.73B card figure from Nilson counts **all** card network purchase transactions, which includes gaming purchases
- So yes, **~8.45B gaming microtransactions are already counted in the 772.7B consumer card total**
- This is 1.1% of all card transactions — small but non-trivial

## 5. Overlap with Digital Wallets

**Total microtransactions via wallets: 1.43B (card-funded) + 1.12B (non-card) = 2.55B**

Of these:
- 1.43B are Apple Pay/Google Pay on card rails → counted in both Wallets and Cards
- 1.12B are PayPal/platform balance → counted in Wallets only
- Total wallet overlap: **2.55B** (20.8% of gaming microtransactions)

## 6. Incremental (Truly Unique) Gaming Microtransactions

Transactions NOT counted in any other payment category:

| Source | Txns (B) | Why Incremental |
|--------|----------|-----------------|
| Carrier billing (DCB) | 1.14 | Telecom rails — not cards, wallets, or bank transfers |
| Gift cards / store credit | 0.63 | The gift card purchase was counted, but the redemption is a new transaction |
| Platform wallet spend (pre-funded) | 0.31 | Steam Wallet / PSN balance spend — the top-up was counted, the in-game spend is internal |
| Other | 0.24 | Crypto, regional methods |
| **TOTAL INCREMENTAL** | **~2.32B** | **18.9% of gaming microtransactions** |

**Key finding: ~81% of gaming microtransactions (10.0B) are already counted in Consumer Cards, Digital Wallets, or Bank Transfers.** Only ~2.3B (~19%) are truly incremental.

## 7. Update to data.json Overlap Fields

The existing `data.json` overlap section should be updated from:
```json
"overlap_note": "65-75% of microtransactions settle on card rails"
```
to:
```json
"overlap_note": "68.8% of microtransactions settle on card rails (8.45B of 12.28B). An additional 9.1% flow through non-card digital wallets, 3.3% through bank transfers. Only ~19% (2.3B) are truly incremental — primarily carrier billing and gift card redemptions."
```

## 8. Regional Variation

The payment mix varies dramatically by region:

| Region | Card % | Wallet % | Carrier % | Other % |
|--------|--------|----------|-----------|---------|
| US/Canada | ~70% | ~15% | ~5% | ~10% |
| EU/UK | ~60% | ~20% | ~8% | ~12% |
| Japan | ~40% | ~25% | ~20% | ~15% |
| South Korea | ~50% | ~30% | ~10% | ~10% |
| China | ~10% | ~80% | ~2% | ~8% |
| SE Asia | ~25% | ~35% | ~30% | ~10% |
| Latin America | ~45% | ~20% | ~15% | ~20% |

China's dominance of mobile IAP revenue (~35% of global) means that the global card overlap is lower than US-centric intuition suggests. Alipay and WeChat Pay process ~80% of Chinese gaming IAP, and these are NOT on card rails.

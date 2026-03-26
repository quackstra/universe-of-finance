# Payment Category Overlap Analysis

> Part of the [Universe of Finance](../../README.md) project.
> **Last Updated**: 2026-03-26

## Purpose

The Universe of Finance counts six payment categories independently. Several of these categories overlap — a single consumer purchase can appear in multiple categories simultaneously (e.g., an Amazon order paid via Apple Pay funded by a Visa card touches E-Commerce, Digital Wallets, and Consumer Cards). This document quantifies those overlaps to enable accurate de-duplication when aggregating total global payment TPS.

---

## A) Digital Wallets <> Consumer Cards

### The Core Problem

Digital wallets like Apple Pay, Google Pay, and Samsung Pay are predominantly **convenience layers** over existing card rails. From the card network's perspective, an Apple Pay tap is simply a Visa or Mastercard contactless transaction. Both the wallet platform and the card network count it.

### Card-Rail vs. Independent Wallet Transactions

| Wallet Type | Est. 2024 Txns (B) | Rides on Card Rails? | Incremental to Cards? |
|-------------|---------------------|---------------------|-----------------------|
| **UPI (India)** | 172 | No — bank-to-bank A2A | Yes |
| **China mobile (Alipay/WeChat)** | 280 | No — linked to bank accounts, not card networks | Yes |
| **M-Pesa / mobile money (Africa)** | ~82 (GSMA: 108B global, ~82B Africa) | No — mobile money ledger | Yes |
| **Other mobile money (non-Africa)** | ~26 | No | Yes |
| **Apple Pay** | ~24 (est. 2024) | ~95%+ on Visa/MC rails | ~5% incremental (transit, in-app non-card) |
| **Google Pay (non-UPI)** | ~5 (est.) | ~90%+ on Visa/MC rails | ~10% incremental |
| **Samsung Pay** | ~3 (est.) | ~95%+ on Visa/MC rails | Minimal |
| **PayPal mobile wallet** | ~5 | ~60% card-funded, ~40% bank/balance | ~40% incremental |
| **Other regional wallets** | ~3 | Mixed | ~50% incremental |

### Quantification

**Total digital wallet transactions (2024):** ~620 billion

| Segment | Txns (B) | Card-Rail Overlap | Incremental (non-card) |
|---------|----------|-------------------|----------------------|
| UPI | 172 | 0 | 172 |
| China mobile | 280 | ~5 (UnionPay NFC subset) | ~275 |
| M-Pesa + African mobile money | 82 | 0 | 82 |
| Other mobile money (GSMA non-Africa) | 26 | 0 | 26 |
| Apple Pay | 24 | ~23 | ~1 |
| Google Pay (non-UPI) | 5 | ~4.5 | ~0.5 |
| Samsung Pay | 3 | ~2.9 | ~0.1 |
| PayPal mobile | 5 | ~3 | ~2 |
| Other regional | 3 | ~1.5 | ~1.5 |
| **TOTAL** | **~620** | **~40** | **~560** |

### Key Finding

**Of the ~620B digital wallet transactions, approximately 560B (~90%) are INCREMENTAL to the 773B card transactions.** Only ~40B (~6.5%) are double-counted with card networks.

This is because the world's largest wallet ecosystems — UPI (172B), China mobile payments (280B), and African mobile money (82B) — operate on **independent, non-card rails**. The card-rail overlap is concentrated in Apple Pay, Google Pay, and Samsung Pay, which are large in Western markets but small globally.

**The double-counting risk is lower than intuition suggests.** While nearly 100% of Apple Pay/Google Pay/Samsung Pay transactions in Western markets ride on Visa/Mastercard rails, these platforms collectively represent only ~32B of 620B total wallet transactions (~5%). The global wallet story is overwhelmingly UPI + China + mobile money, none of which use card rails.

---

## B) E-Commerce <> Cards / Bank Transfers / Wallets

### Payment Method Breakdown for E-Commerce (2024)

Source: [Worldpay Global Payments Report 2025](https://worldpay.com/en/global-payments-report)

| Payment Method | Share of E-Commerce Value | Est. E-Commerce Txns (B) | Also Counted In |
|----------------|--------------------------|-------------------------|-----------------|
| Digital Wallets | 53% | ~30.5 | Digital Wallets |
| Credit Cards | 20% | ~11.5 | Consumer Cards |
| Debit Cards | 12% | ~6.9 | Consumer Cards |
| Bank Transfer (A2A) | 7% | ~4.0 | Bank Transfers |
| BNPL | 5% | ~2.9 | (Partially in Cards — BNPL providers often use card rails for merchant payout) |
| Cash on Delivery | 2% | ~1.2 | Not counted elsewhere |
| Other | 1% | ~0.5 | Various |
| **TOTAL** | **100%** | **~57.5** | |

### Overlap Quantification

Every e-commerce transaction is paid for by *some* payment method. Therefore:

- **~18.4B e-commerce txns** (32%) are already counted in Consumer Cards (credit + debit)
- **~30.5B e-commerce txns** (53%) are already counted in Digital Wallets
  - Of those, ~65% are funded by cards (per Worldpay: 65% of Americans fund wallets with cards) — so ~20B are *also* in Consumer Cards via wallet-funded card charges
- **~4.0B e-commerce txns** (7%) are already counted in Bank Transfers
- **~1.2B e-commerce txns** (2%) are cash-on-delivery — genuinely unique to this category
- **~2.9B e-commerce txns** (5%) are BNPL — partially unique (BNPL providers like Klarna/Afterpay settle with merchants via card networks or bank transfers)

### Non-Overlapping E-Commerce Portion

**Truly incremental e-commerce transactions (not counted in any other payment category): ~4-6B** — primarily cash-on-delivery, some BNPL, and residual "other" methods.

**E-commerce is almost entirely an overlay category.** The 57.5B e-commerce transactions are real commerce events, but 90%+ of the underlying payment flows are already captured in Cards, Wallets, or Bank Transfers. For TPS aggregation, e-commerce should be treated as a **commerce layer**, not a payment layer.

---

## C) Bank Transfers Breakdown

### By Transfer Type (2024)

| Subcategory | Annual Volume (B) | Share by Volume | Annual Value ($T) | Share by Value |
|-------------|------------------|-----------------|-------------------|----------------|
| **Real-Time Payments** | 378 | 78.1% | ~106 | 4.3% |
| **Batch/ACH** | 106 | 21.9% | ~505 | 20.4% |
| **RTGS/Wire** | 0.4 | 0.08% | ~1,860 | 75.3% |
| **TOTAL** | **484** | **100%** | **~$2,471T** | **100%** |

### Real-Time Payments Detail

| System | Country | 2024 Volume (B) | Launch Year | Notes |
|--------|---------|-----------------|-------------|-------|
| UPI | India | 172 (NPCI: up from 131B in calendar 2024 to 172B fiscal year basis) | 2016 | Also counted in Digital Wallets |
| PIX | Brazil | ~65-69 | 2020 | ~52% YoY growth; BCB data |
| PromptPay | Thailand | ~18 (est.) | 2017 | |
| Faster Payments | UK | 5.1 | 2008 | |
| SEPA Instant | EU | ~5.0 | 2017 | Growing fast under EU Instant Payments Regulation |
| Nigeria NIP | Nigeria | ~7.9 | 2011 | |
| FedNow | US | 0.0015 | 2023 | Negligible volume so far |
| Other RTP systems (80+ countries) | Various | ~105 | Various | ACI estimates 266B global in 2023; 42% growth |

### Batch/ACH Detail

| System | Country | 2024 Volume (B) | 2024 Value ($T) |
|--------|---------|-----------------|-----------------|
| US ACH (Nacha) | US | 33.6 | $86.2 |
| SEPA Credit Transfers | EU | ~32 | ~$238 (EUR 220T) |
| BACS | UK | ~7.5 | ~$6.5T |
| Other national ACH | Various | ~33 | ~$174 |

### RTGS/Wire Detail

| System | Country | 2024 Volume (M) | 2024 Value ($T) |
|--------|---------|-----------------|-----------------|
| Fedwire | US | 210 | $1,133 |
| TARGET2/T2 | EU | 108 | ~$600 |
| CHAPS | UK | 52.7 | ~$127 |
| BOJ-NET | Japan | ~20 (est.) | ~$100 (est.) |
| Other RTGS | Various | ~10 | ~$200 (est.) |

### Key Overlap: UPI in Both Bank Transfers and Digital Wallets

UPI's 172B transactions are counted in **both** Bank Transfers (as real-time A2A payments) and Digital Wallets (as mobile wallet transactions via PhonePe/GPay/Paytm). This is the single largest overlap in the entire payments taxonomy — **172 billion transactions** appear in two categories.

**Resolution:** UPI is fundamentally a bank transfer rail. The wallet apps (PhonePe, Google Pay, Paytm) are front-ends, not independent payment systems. For de-duplication, UPI should be counted once in Bank Transfers, and Digital Wallets should subtract UPI volume from its total, leaving ~448B incremental wallet transactions.

---

## D) Overlap Summary Matrix

| Category Pair | Overlapping Txns (B) | Nature of Overlap |
|---------------|---------------------|-------------------|
| Digital Wallets <> Consumer Cards | ~40 | Apple Pay/Google Pay/Samsung Pay on card rails |
| Digital Wallets <> Bank Transfers | ~172 | UPI counted in both |
| E-Commerce <> Consumer Cards | ~18.4 (direct) + ~20 (via wallets) | Card-paid e-commerce orders |
| E-Commerce <> Digital Wallets | ~30.5 | Wallet-paid e-commerce orders |
| E-Commerce <> Bank Transfers | ~4.0 | A2A-paid e-commerce orders |
| P2P Transfers <> Digital Wallets | ~0.5 | PayPal/Cash App wallet overlap |
| Remittances <> Bank Transfers | ~0.7 | Bank wire remittances |
| Remittances <> P2P Transfers | ~0.1 | Cross-border P2P overlap |

### De-Duplicated Global Payment TPS (2024)

| Category | Raw Annual Txns (B) | Subtract Overlaps (B) | De-Duplicated Txns (B) | Avg TPS |
|----------|---------------------|-----------------------|----------------------|---------|
| Consumer Cards | 773 | 0 (base layer) | 773 | 24,500 |
| Digital Wallets | 620 | -172 (UPI) -40 (card-rail) | 408 | 12,930 |
| Bank Transfers | 484 | 0 (base layer; includes UPI) | 484 | 15,340 |
| E-Commerce | 57.5 | -53 (paid via cards/wallets/bank) | 4.5 | 143 |
| P2P Transfers | 8.5 | -0.5 (wallet overlap) | 8.0 | 254 |
| Remittances | 1.8 | -0.8 (bank/P2P overlap) | 1.0 | 32 |
| **Raw Sum** | **1,944.8** | | | |
| **De-Duplicated Sum** | | | **1,678.5** | **53,199** |

**The raw sum overstates global payment transactions by ~14%.** After de-duplication, the global payment system processes approximately **1,679 billion unique transactions per year**, or **~53,200 TPS average**.

The two dominant base layers are:
1. **Consumer Cards** (773B) — the legacy electronic payment backbone
2. **Bank Transfers** (484B) — increasingly dominated by real-time payments

Together they account for 75% of all unique payment transactions. Digital wallets add another 408B incremental transactions (24%), primarily from China's mobile payment ecosystem and African mobile money. E-Commerce, P2P, and Remittances add minimal incremental volume because their payment flows are captured in the base layers.

---

## Methodology Notes

1. All transaction counts are 2024 estimates. Sources: Nilson Report (cards), NPCI (UPI), ACI Worldwide (RTP), Worldpay GPR (e-commerce payment mix), GSMA (mobile money), Statista/PBOC (China), Safaricom (M-Pesa).
2. "Incremental" means a transaction that would not be counted in any other payment category.
3. Card-rail overlap for Apple Pay/Google Pay/Samsung Pay estimated at 95% based on the fact that these wallets require a linked card in most markets and almost all transactions are tokenized card payments.
4. UPI allocation: counted in Bank Transfers as the primary category (it is an A2A real-time payment system), subtracted from Digital Wallets.
5. E-commerce payment method shares from Worldpay GPR 2025, which covers $6.33T in retail e-commerce GMV.
6. The 65% card-funding rate for wallets is US-specific (Worldpay); global rate may be lower due to China/India bank-account-linked wallets.

---

## Sources

1. [Worldpay Global Payments Report 2025](https://worldpay.com/en/global-payments-report)
2. [Nilson Report — Global Network Card Results 2024](https://nilsonreport.com/articles/global-network-card-results-worldwide-2024/)
3. [NPCI UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics)
4. [ACI Worldwide — Prime Time for Real-Time 2024](https://www.aciworldwide.com/real-time-payments-report)
5. [GSMA — State of the Industry Report on Mobile Money 2025](https://www.gsma.com/sotir/)
6. [PBOC Payment System Report 2024](http://www.pbc.gov.cn/en/3688247/3688978/3709143/5649949/2025040114593718714.pdf)
7. [Statista — China Mobile Payment Transactions 2024](https://www.statista.com/statistics/244538/number-of-mobile-payment-transactions-in-china/)
8. [Capital One Shopping — Apple Pay Statistics 2026](https://capitaloneshopping.com/research/apple-pay-statistics/)
9. [CoinLaw — Samsung Pay Statistics 2025](https://coinlaw.io/samsung-pay-statistics/)
10. [BCB — PIX Statistics](https://www.bcb.gov.br/en)
11. [Safaricom Annual Report 2024](https://www.safaricom.co.ke/annualreport_2024/)
12. [Nacha — ACH Network Volume and Value Statistics](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
13. [Federal Reserve Services — Fedwire Annual Statistics](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html)

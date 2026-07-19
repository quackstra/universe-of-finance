# Middle East Deep Dive — Calculations & Derivations

> Run 13 (2026-07-19). Full audit trail for every number in REPORT.md and data.json.
> Constant used: SECONDS_PER_YEAR = 31,536,000.

## Saudi Arabia

### mada card TPS
- 2024 volume: **8.9B transactions** ([WhiteSight](https://whitesight.net/how-saudi-arabia-engineered-a-digital-payments-boom/))
- TPS = 8,900,000,000 / 31,536,000 = **282.2 TPS**

### sarie instant TPS
- 2024 volume: **593M transactions**, 50% CAGR since 2021 launch ([ClearingPost](https://clearingpost.com/insights/saudi-arabia-payment-infrastructure-guide-sarie-mada-sadad/))
- TPS = 593,000,000 / 31,536,000 = **18.8 TPS**
- Cross-check: >100M/month by 2025 → 1.2B/yr run-rate → ~38 TPS (2025 trajectory, not 2024 figure)

### SADAD bill payments TPS
- 2024 volume: ~364M (conservative) to ~500M+ (broad) ([PaymentBrief](https://paymentbrief.com/articles/saudi-arabia-mada-sarie-payment-stack/))
- Using ~500M: TPS = 500,000,000 / 31,536,000 = **15.9 TPS**

### Blended non-cash retail (headline figure used)
- 2024: **12.6B non-cash retail transactions**, 79% of all retail ([mada](https://www.mada.com.sa/en))
- TPS = 12,600,000,000 / 31,536,000 = **399.5 TPS**
- This is the headline Saudi figure (includes mada + Visa/MC credit + wallets + instant).
  The individual rails above are components; we do NOT sum them on top of 12.6B (would
  double-count).

## UAE

### Card TPS (estimated from value)
- 2024 card value: **Dh511.4B** (+13.3% YoY) ([Khaleej Times](https://www.khaleejtimes.com/business/uae-card-transactions-set-to-surge-to-dh5655-billion))
- Dh511.4B ≈ $139.2B (at Dh3.6725/$)
- Assume avg ticket ~$27 (UAE skews high vs global ~$22): $139.2B / $27 ≈ **5.15B txns**
- TPS = 5,150,000,000 / 31,536,000 = **163 TPS** → rounded to ~150 TPS (conservative, avg
  ticket may be higher → fewer txns). Confidence 🟡.

### Aani instant TPS
- ~25,000 P2P transfers/day ([CBUAE](https://www.centralbank.ae/en/news-and-publications/news-and-insights/press-release/aani-delivers-a-transformational-leap-in-the-uae-s-digital-payments-landscape-12-5-million-users-and-instant-transfers-in-3-seconds/))
- 25,000/day / 86,400 s = **0.29 TPS**. Nascent but 6x YoY growth.

### Outward remittance TPS
- 2024 outflow: **AED 183B (~$50B)** ([Khaleej Times](https://www.khaleejtimes.com/business/remittance-boom-uae-leads-gcc-as-india-hits-record-1294b-in-2024))
- Assume avg remittance ~$415 (typical Gulf→South Asia corridor): $50B / $415 ≈ 120M txns
- TPS = 120,000,000 / 31,536,000 = **3.8 TPS**
- **Note the value density**: 3.8 TPS carrying $50B/yr = ~$415/txn, but the *aggregate*
  makes UAE the #2-3 global remittance origin. This is the value-not-count signature.

### UAE total ≈ 150 + 0.3 + 3.8 ≈ **~155 TPS**

## Qatar
- Fawran: 5.5M txns in 14 months (from Mar 2024) → ~4.7M/yr → 0.15 TPS ([Lightspark](https://www.lightspark.com/knowledge/instant-payments-qatar))
- Cards: GDP ~$220B, ~3M pop, affluent. Estimate ~1B card txns/yr → ~32 TPS
- **Qatar ≈ ~35 TPS** (🔴, card count estimated)

## Kuwait
- KNET dominant: ~80% of online, ~5M cards, ~80% debit ([Tap](https://blog.tap.company/local-payment-methods-middle-east/))
- Estimate ~1.4B txns/yr (GDP $160B, high card penetration): → ~45 TPS
- **Kuwait ≈ ~45 TPS** (🔴, KNET does not publish counts)

## Bahrain
- BenefitPay: **421M txns 2024** (+22%), Fawri+ ~410M ([FCCIB](https://www.fccib.net/news/n/news/benefitpay-transactions-surge-by-22pc-in-2024.html))
- 421M / 31,536,000 = **13.4 TPS** from BenefitPay alone
- Plus other card/RTGS ~7 TPS → **Bahrain ≈ ~20 TPS** (🟡)
- Per-capita intensity: 421M / 1.5M pop = 281 instant txns per person/yr — among world's highest

## Oman
- ~5M pop, OmanNet. Estimate ~470M txns/yr → **~15 TPS** (🔴)

## Israel
- ~9.8M pop, developed. High card usage (~3.5B card txns/yr est) + TASE
- Estimate **~100 TPS** (🟡). Often analyzed separately from Gulf.

## Levant (Jordan, Lebanon, Iraq)
- Largely cash. Jordan JoMoPay growing; Lebanon dollarized crisis; Iraq Qi Card gov rails
- Combined estimate **~30 TPS** (🔴)

## Regional Capital Markets
- Tadawul ADV ~$1.5B, ~$3T cap, 239 listings ([Saudi Exchange](https://www.saudiexchange.sa/wps/portal/tadawul/home/))
- Combined regional exchanges (Tadawul/ADX/DFM/QSE/Boursa Kuwait/TASE): est. 500-800k trades/day
- 650,000/day / 86,400 = **~7.5 TPS → ~8 TPS** (🟡)

## Interbank RTGS
- High value, low count. Oil settlement + wholesale. Est. **~3 TPS** but ~6% of global RTGS
  count share and higher value share (~5x count share).

## Regional Total
```
Saudi Arabia           399.5
UAE                    155.0
Kuwait                  45.0
Qatar                   35.0
Bahrain                 20.0
Oman                    15.0
Israel                 100.0
Levant                  30.0
Capital markets          8.0
Interbank RTGS           3.0
--------------------------------
GROSS                  810.5
De-dup (instant/remittance overlaps netted, ~10 TPS): ~800 TPS
```

- **~800 TPS / 73,720 global = 1.085% ≈ 1.1%**
- Per-capita: 800 / 260M = 3.08 TPS per million people (vs Africa 2.0/million — GCC more
  digitized per person, but far fewer people)

## Sovereign Wealth (value, not count)
- ADIA ~$1.1T + PIF ~$925B + KIA ~$800B + QIA ~$530B + Mubadala ~$330B + ADQ ~$250B
  = **~$3.94T** (call it ~$4-5T with smaller funds) ([SWF Institute](https://www.swfinstitute.org/))
- Transaction count: negligible (perhaps single-digit large transactions per day per fund)
- Illustrative: if the 6 funds collectively execute ~50 large transactions/day →
  50/86,400 = 0.0006 TPS, moving ~$4-5T in AUM. **Value-per-transaction in the billions.**
- Contrast: African mobile money = 43.5B txns/yr moving $832B → ~$19/txn.
  The two regions differ in value-per-transaction by a factor of **~100 million×**.

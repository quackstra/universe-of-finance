---
title: "Scenarios"
---

# Macro Scenario Stress Tests — How the Big Number Shifts

> Modelling the ~70,700 TPS Big Number under three macro stress scenarios.

**Author**: Market Research Analyst + Emerging Tech Forecaster (Run 5)
**Last Updated**: 2026-03-28

---

## Baseline: The Big Number

**De-duplicated Global Financial TPS: ~70,700** (payment infrastructure) / **~71,200** (all economic events)

| Sector | De-Dup TPS | Share |
|--------|-----------|-------|
| Payments | 53,200 | 75.2% |
| Traditional Finance | 13,373 | 18.9% |
| Digital Assets | 3,515 | 5.0% |
| Banking/Settlement | 95 | 0.1% |
| Incremental (Gov/IoT) | ~560 | 0.8% |

---

## Scenario 1: Recession (2008-Style Global Financial Crisis)

### Assumptions

Based on observed 2008–2009 data and academic literature on payment behaviour during recessions:

| Category | Direction | Magnitude | Basis |
|----------|-----------|-----------|-------|
| Consumer Cards | DOWN | -10% to -15% | Consumer spending fell ~12% in 2008-09; transaction counts dropped less than spend value (consumers shift to smaller purchases) |
| Digital Wallets | DOWN | -5% to -10% | Wallets are more discretionary; but also include utility payments that persist |
| Bank Transfers | DOWN | -5% | Corporate payments decline, but payroll/rent persist; ACH is resilient |
| E-Commerce | DOWN | -5% to -8% | E-commerce is more resilient than brick-and-mortar, partially offsets |
| P2P Transfers | DOWN | -8% | Less discretionary spending |
| Remittances | DOWN | -5% to -10% | Migrant worker employment affected; but corridor demand is inelastic |
| ETD | UP | +30% to +50% | Hedging demand surges; VIX derivatives explode. 2008 ETD volume rose ~40% |
| Equity Markets | UP | +40% to +80% | Volatility drives massive trading volumes. 2008 volume surged |
| Commodities | UP | +20% | Flight to gold, oil volatility |
| Forex | UP | +30% | Currency volatility, safe-haven flows |
| Fixed Income | UP | +50% | Flight to quality (Treasuries), repo market stress |
| OTC Derivatives | UP | +100% | CDS trading explodes in credit crises |
| CEX | MIXED | -10% to +20% | 2008 pre-dates crypto; by analogy, risk assets sell off but trading volume rises |
| L1/L2 Blockchain | FLAT | ±10% | On-chain activity mildly affected |
| Government Payments | UP | +20% to +30% | Unemployment benefits, stimulus disbursements surge |
| Gaming | DOWN | -5% | Discretionary spending, but gaming is recession-resilient |
| IoT/M2M | DOWN | -3% | Tolling drops with less commuting; utility payments persist |

### Recession Big Number Estimate

| Sector | Baseline TPS | Recession TPS | Change |
|--------|-------------|---------------|--------|
| Payments (de-dup) | 53,200 | 46,800 | -12% |
| Traditional Finance | 13,373 | 19,400 | +45% |
| Digital Assets | 3,515 | 3,515 | ±0% |
| Banking/Settlement | 95 | 130 | +37% |
| Incremental (Gov/IoT) | 560 | 680 | +21% |
| **Total** | **~70,700** | **~70,500** | **-0.3%** |

### Analysis

**The Big Number barely moves in a recession.** The decline in consumer payments (-6,400 TPS) is almost exactly offset by the surge in trading activity (+6,000 TPS) and increased government disbursements. This makes intuitive sense: recessions shift economic activity from consumption to risk management, but the total volume of financial transactions remains remarkably stable.

The *composition* changes dramatically:
- Payments share drops from 75% to 66%
- TradFi share jumps from 19% to 28%
- Government share doubles

**Historical precedent**: Global non-cash payment volumes grew even through 2008-09 (BIS Red Book data), though growth slowed from ~10% to ~3%. Total financial message traffic (SWIFT) barely dipped.

**Range**: 66,000 – 75,000 TPS (low = severe recession with crypto winter; high = volatile recession with trading boom)

---

## Scenario 2: Pandemic (2020-Style Global Lockdown)

### Assumptions

Based on observed 2020–2021 data:

| Category | Direction | Magnitude | Basis |
|----------|-----------|-----------|-------|
| Consumer Cards | DOWN then UP | -15% (Q2 2020), +10% (2021) | Physical POS cratered; e-commerce surged. Net: ~-5% annualised first year |
| Digital Wallets | UP | +25% to +40% | Massive shift to contactless/digital. India UPI grew 73% in 2020 despite lockdowns |
| Bank Transfers | UP | +10% to +15% | Government disbursements via ACH explode; corporate payments persist remotely |
| E-Commerce | UP | +30% to +50% | 3-5 year acceleration of e-commerce adoption compressed into months |
| P2P Transfers | UP | +20% to +30% | Venmo/Cash App surged as in-person cash exchange stopped |
| Remittances | DOWN then UP | -5% to +5% | Initial shock (-20% in Q2 2020), then rapid recovery |
| ETD | UP | +30% to +40% | 2020 set ETD records; COVID volatility was tradeable |
| Equity Markets | UP | +50% to +80% | Retail investing boom (Robinhood), volatility. 2020 US equity volumes +55% |
| Commodities | UP | +15% | Oil volatility (negative prices!), gold safe haven |
| Forex | UP | +10% | Moderate increase from central bank divergence |
| Fixed Income | UP | +30% | Central bank buying, flight to quality |
| OTC Derivatives | UP | +20% | Hedging demand |
| CEX | UP | +100% to +200% | 2020-21 crypto bull run; DeFi summer; NFT mania |
| L1/L2 Blockchain | UP | +200% to +500% | DeFi summer 2020 + NFT boom 2021. Ethereum gas fees skyrocketed |
| Government Payments | UP | +50% to +100% | Stimulus checks: US alone disbursed 476M payments in 3 rounds. UK furlough scheme. India DBT surge |
| Gaming | UP | +20% to +30% | Lockdown gaming boom; mobile gaming up 45% |
| IoT/M2M | DOWN then UP | -10% then +15% | Tolling crashed (lockdowns), but EV charging and smart home purchases surged |

### Pandemic Big Number Estimate

| Sector | Baseline TPS | Pandemic TPS (Year 1) | Pandemic TPS (Year 2) | Change (Y1) |
|--------|-------------|----------------------|----------------------|-------------|
| Payments (de-dup) | 53,200 | 56,900 | 62,500 | +7% |
| Traditional Finance | 13,373 | 18,700 | 16,700 | +40% |
| Digital Assets | 3,515 | 7,000 | 10,500 | +99% |
| Banking/Settlement | 95 | 120 | 110 | +26% |
| Incremental (Gov/IoT) | 560 | 1,000 | 700 | +79% |
| **Total** | **~70,700** | **~83,700** | **~90,500** | **+18%** |

### Analysis

**A pandemic INCREASES the Big Number by 18-28%.** Unlike a recession (which redistributes activity), a pandemic genuinely creates *new* transaction volume:

1. **Cash-to-digital migration** — Physical cash usage cratered ~30% in 2020. Those transactions moved to cards and digital wallets, increasing the *counted* digital TPS (cash transactions are invisible to our measurement)
2. **Government disbursement explosion** — The US alone processed 476M stimulus payments. India's DBT disbursed record volumes. UK, EU, and others all created new payment flows
3. **Retail investing boom** — Robinhood added 3M users in Q1 2020 alone. Global equity trading volumes hit records
4. **Crypto/DeFi supercycle** — The 2020-21 crypto bull run was partially pandemic-driven (stimulus money, stay-at-home speculation)
5. **E-commerce structural shift** — E-commerce penetration jumped 3-5 years forward permanently

**The pandemic effect is NOT temporary for payments.** Post-COVID, card transaction volumes never returned to pre-COVID growth trajectories — they shifted permanently higher. The Big Number likely ratcheted up ~10-15% permanently from pandemic-era behavioural changes.

**Range**: 78,000 – 95,000 TPS (Year 1); 85,000 – 105,000 TPS (Year 2, as digital adoption compounds)

---

## Scenario 3: Crypto Winter (2022-Style Extended Bear Market)

### Assumptions

Based on observed 2022–2023 data:

| Category | Direction | Magnitude | Basis |
|----------|-----------|-----------|-------|
| CEX | DOWN | -60% to -80% | Spot volume fell ~65% from 2021 peak to 2022 trough (CoinGecko data) |
| L1/L2 Blockchain | DOWN | -40% to -60% | On-chain activity dropped ~50% from peak. Ethereum gas fees fell 80%+ |
| DeFi | DOWN | -60% to -80% | TVL fell from $180B to $39B. DEX volumes cratered |
| Stablecoins | DOWN | -10% to -20% | Surprisingly resilient — stablecoin market cap fell only ~15% vs crypto overall -60%. Transfer volumes declined modestly as stablecoins became the "flight to safety" within crypto |
| Consumer Cards | FLAT | ±0% | Zero correlation with crypto markets |
| Digital Wallets | FLAT | ±0% | Zero correlation |
| Bank Transfers | FLAT | ±0% | Zero correlation |
| ETD | FLAT | ±0% | Crypto ETD is <2% of total ETD volume |
| Equity Markets | FLAT | ±0% to -2% | Minor sentiment correlation; crypto-adjacent stocks affected (COIN, MSTR) but negligible market-wide |
| Government | FLAT | ±0% | Zero correlation |
| Gaming | FLAT to DOWN | -1% to -3% | Web3 gaming collapsed but was never material to total gaming volume |
| IoT/M2M | FLAT | ±0% | Zero correlation |

### Crypto Winter Big Number Estimate

| Sector | Baseline TPS | Crypto Winter TPS | Change |
|--------|-------------|-------------------|--------|
| Payments (de-dup) | 53,200 | 53,200 | ±0% |
| Traditional Finance | 13,373 | 13,373 | ±0% |
| Digital Assets | 3,515 | 1,350 | -62% |
| Banking/Settlement | 95 | 95 | ±0% |
| Incremental (Gov/IoT) | 560 | 560 | ±0% |
| **Total** | **~70,700** | **~68,600** | **-3.0%** |

### Digital Assets Breakdown

| Sub-category | Baseline TPS | Crypto Winter TPS | Change |
|--------------|-------------|-------------------|--------|
| CEX (wash-adjusted) | 3,040 | 910 | -70% |
| L1/L2 Blockchain | 415 | 190 | -54% |
| DeFi | *(subset)* | *(subset)* | -70% |
| Stablecoins | *(subset)* | *(subset)* | -15% |
| **Digital Assets Total** | **3,515** | **~1,350** | **-62%** |

### Analysis

**A crypto winter has negligible impact on the Big Number.** Digital assets represent ~5% of de-duplicated global financial TPS. Even a severe 62% decline in crypto activity only reduces the total by ~2,165 TPS — a 3.0% change that's well within the uncertainty range of the Big Number itself (64,000–80,000 TPS).

**This confirms the structural insight**: Crypto, despite enormous media attention and significant value volumes ($77T+ in 2024 CEX volume), is a transaction *count* minnow relative to payments and traditional finance. Card networks alone process ~7x more transactions per second than the entire crypto ecosystem.

**Stablecoin resilience is notable**: During the 2022 crypto winter, stablecoin transfer volumes proved far more resilient than speculative trading volumes. This suggests stablecoins are developing genuine payment utility independent of crypto speculation. A stablecoin-heavy crypto winter (where speculation dies but stablecoin payments persist) would reduce the impact to <2%.

**Range**: 67,500 – 69,500 TPS

---

## Summary: Big Number Under Stress

| Scenario | Big Number | Change vs Baseline | Key Driver |
|----------|-----------|-------------------|------------|
| **Baseline (2024)** | ~70,700 | — | — |
| **Recession (2008-style)** | ~70,500 | -0.3% | Payment decline offset by trading surge |
| **Pandemic (2020-style, Year 1)** | ~83,700 | +18% | Cash-to-digital shift + stimulus + trading boom |
| **Pandemic (2020-style, Year 2)** | ~90,500 | +28% | Structural digital acceleration |
| **Crypto Winter** | ~68,600 | -3.0% | Crypto is 5% of TPS; rest unaffected |

### Visual Ranges

```
Baseline:       |==========|                           ~70,700 TPS
                     ^
Recession:      |=========|                            ~66,000 - 75,000 TPS
                    ^
Pandemic Y1:         |============|                    ~78,000 - 95,000 TPS
                          ^
Pandemic Y2:            |==============|               ~85,000 - 105,000 TPS
                              ^
Crypto Winter:  |=========|                            ~67,500 - 69,500 TPS
                   ^
```

### Key Takeaways

1. **The Big Number is remarkably resilient.** It barely moves in a recession because payments and trading are inversely correlated. When people stop buying, traders start hedging.

2. **Pandemics are the biggest TPS accelerator** — not because of crisis trading (which helps) but because they force structural migration from cash/physical to digital/card channels, permanently increasing the measured digital TPS.

3. **Crypto's macro impact is overstated.** A total crypto collapse barely dents the Big Number. The ~$100T in annual crypto volume is impressive but spread across relatively few high-value transactions compared to ~770B annual card swipes.

4. **The "floor" for the Big Number is ~65,000 TPS** — even in the worst combined scenario (severe recession + crypto winter), payments infrastructure maintains a baseline load that doesn't significantly decline.

5. **The "ceiling" (non-crisis) is ~90,000-100,000 TPS** within a few years, driven by structural trends: real-time payment adoption (India, Brazil leading), digital wallet penetration (China, SE Asia), and e-commerce growth converting cash transactions to digital.

---

*These scenarios use directional estimates based on historical precedent (2008, 2020, 2022). Actual outcomes would depend on crisis severity, geographic distribution, and policy response. All estimates carry Low to Medium confidence.*

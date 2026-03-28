# Growth Analysis: Cross-Sector Trends 2015-2025

> Comparative analysis of growth rates, structural trends, and regime changes
> across all 24 categories in the Universe of Finance.

**Generated**: 2026-03-28
**Companion files**: `TIMESERIES.md` (summary tables), `data.json` (machine-readable)

---

## 1. Growth Rate Comparison by Sector

### Sector-Level CAGRs (2015-2025, weighted by 2025 TPS)

| Sector | 2015 TPS | 2025 TPS | CAGR | Dominant Driver |
|--------|----------|----------|------|-----------------|
| Payments | ~9,561 | ~69,632 | 22.0% | RTP adoption (UPI/PIX) + digital wallet expansion |
| Digital Assets | ~37 | ~5,430 | 64.7% | CEX scale + L1/L2 throughput gains |
| Traditional Finance | ~2,351 | ~11,858 | 17.5% | ETD explosion (India options) |
| Banking | ~13 | ~60 | 16.6% | Securities settlement scope expansion |
| Gaming | ~240 | ~512 | 7.8% | Mobile gaming maturation |
| Government | ~700 | ~1,002 | 3.6% | Slow digitization |
| Emerging | ~400 | ~1,541 | 14.4% | IoT tolling/metering growth |

**Takeaway**: Digital assets grew fastest by percentage but from a tiny base. Payments dominate absolute volume and still grew >20% CAGR. Traditional finance's growth was almost entirely driven by one subcategory (ETD) -- without India's options explosion, TradFi CAGR would be ~4%.

### The "Quiet Giant" Problem

Traditional finance categories (equity, bonds, FX, commodities, OTC derivatives) account for an enormous share of *value* transacted but a tiny share of *transaction count*:

| Metric | Payments | Traditional Finance |
|--------|----------|-------------------|
| Share of global TPS (2025) | ~80% | ~14% |
| Share of global value (2025) | ~$35T | ~$250T+ |
| Avg transaction size | ~$50-500 | ~$50K-5M |

This asymmetry explains why payments infrastructure gets the most engineering investment -- it is the throughput bottleneck, not the value bottleneck.

---

## 2. Structural Trends

### Trend 1: The Digitization Wave (2015-2025)

Three overlapping waves of digitization:

**Wave 1 (2015-2018): Card penetration deepens**
- Consumer cards grew from 227B to 346B txns (+53%)
- Contactless adoption accelerated in UK, Australia, Canada
- China's UnionPay scaled domestic card usage

**Wave 2 (2018-2022): Mobile-first payments emerge**
- UPI: 2.7B (2017) -> 46B (2021) in India
- WeChat Pay/Alipay saturated China's mobile commerce
- M-Pesa expanded across East Africa
- Digital wallets grew from ~117B to ~410B txns

**Wave 3 (2022-2025): Real-time payments go global**
- PIX: 0 -> 66B txns in Brazil (2020-2024)
- SEPA Instant: +72% YoY in Europe
- FedNow launched in US (2023) -- still tiny but growing 2000%/yr
- RTP combined: 50B (2018) -> 553B (2025 est.)

### Trend 2: The Derivatives Explosion

Exchange-traded derivatives grew from 24.8B to 300B contracts in 10 years:

```
2015: 24.8B  (flat since 2010)
2019: 34.5B  (+39% in 4 years)
2020: 46.8B  (COVID volatility)
2023: 137.3B (India retail options)
2025: ~300B  (India dominates)
```

This is almost entirely an India story. NSE went from a minor exchange to the world's largest by contract count, driven by:
- Zero-day options (0DTE) regulation that enabled weekly expiries
- Mobile trading apps (Zerodha, Groww) bringing retail to derivatives
- Low per-contract costs enabling high-frequency retail speculation

**Without India's ETD explosion, global TPS growth would be ~30% lower.**

### Trend 3: Blockchain's Throughput Revolution

Total L1/L2 blockchain TPS: 7 (2015) -> 1,100 (2025) = 157x

Phase breakdown:
- **2015-2017**: Bitcoin-era (3-7 TPS ceiling, block size debates)
- **2017-2019**: Ethereum enables smart contracts but 15 TPS ceiling
- **2020-2022**: Alt-L1s (BSC, Solana, Avalanche) push to 100+ TPS
- **2023-2025**: L2 rollups + Solana's throughput gains push to 1000+ TPS

The narrative arc: blockchains went from "can't scale" to "scaling faster than payments" in one decade. But only ~5% of on-chain transactions are economically meaningful payments; the rest is MEV, spam, failed txns, and protocol overhead.

### Trend 4: Stablecoins as a Payment Rail

The stablecoin trajectory is unique -- it grew through every crypto bear market:

| Year | Est. Stablecoin TPS | Crypto Market Sentiment |
|------|--------------------|-----------------------|
| 2019 | 5 | Bear |
| 2020 | 20 | Early bull |
| 2021 | 80 | Peak bull |
| 2022 | 150 | Deep bear (UST collapse) |
| 2023 | 300 | Recovery |
| 2024 | 520 | Bull |
| 2025 | 700 | Bull |

Stablecoins are the one crypto category that behaves like payments infrastructure rather than speculative assets. Transfer value ($27.6T in 2024) now exceeds Visa and Mastercard combined.

---

## 3. COVID Impact Analysis (2020)

### Categories That Surged

| Category | 2019 TPS | 2020 TPS | Change | Mechanism |
|----------|----------|----------|--------|-----------|
| P2P Transfers | 86 | 124 | +44% | Stimulus splitting, rent sharing |
| Equity Markets | 1,205 | 1,649 | +37% | Retail trading boom, volatility |
| ETD | 1,093 | 1,483 | +36% | Hedging demand, volatility premium |
| Gaming Sales | 55 | 72 | +33% | Lockdown entertainment |
| E-Commerce | 1,062 | 1,282 | +21% | Forced digital shift |
| Gaming Microtx | 326 | 397 | +22% | Engagement hours up |
| Bank Transfers (RTP) | 2,378 | 3,330 | +40% | Digital-first necessity |

### Categories That Dipped

| Category | 2019 TPS | 2020 TPS | Change | Mechanism |
|----------|----------|----------|--------|-----------|
| Consumer Cards | 12,620 | 12,049 | -4.5% | Travel, dining, physical retail collapse |
| IoT/M2M | 850 | 900 | +5.9% | Toll collection down, offset by smart meters |
| FX | 33 | 34 | +3% | Reduced cross-border commerce |

### COVID's Lasting Legacy

The categories that surged in 2020 mostly stayed elevated. E-commerce, digital wallets, and RTP did not revert to pre-COVID trends -- they established a permanently higher baseline. Consumer cards recovered by 2021 and then accelerated. The "digital shift" was a one-way door.

One exception: **gaming microtransactions** had a COVID peak in 2020 (397 TPS) that they only matched again in 2024 (389 TPS). The COVID gaming bump was largely a time-availability effect that reversed.

---

## 4. Projection Confidence: Did Past Growth Rates Predict Correctly?

For categories where we can compare early projections vs. actuals:

### Consumer Cards
- **2019 projection for 2024** (at 2015-2019 CAGR of ~15%): ~800B txns
- **2024 actual**: 773B txns
- **Verdict**: Close -- COVID dip in 2020 and subsequent acceleration roughly canceled out

### Bank Transfers (RTP)
- **2020 projection for 2025** (at 2018-2020 CAGR of ~45%): ~750B txns
- **2025 estimate**: 553B txns
- **Verdict**: Overshot -- growth rate decelerated from 45% to ~30% as largest systems (UPI, PIX) matured

### ETD
- **2019 projection for 2024** (at 2015-2019 CAGR of ~8%): ~50B contracts
- **2024 actual**: 205B contracts
- **Verdict**: Massively undershot -- India options were unpredictable regime change

### Blockchain L1/L2
- **2021 projection for 2025** (at 2019-2021 CAGR of ~63%): ~28B txns
- **2025 estimate**: 35B txns
- **Verdict**: Slightly overshot -- Solana and L2 exceeded expectations

### Key Lessons for Forward Projections

1. **Mature categories (cards, FX, government)**: CAGR-based projections work well. Low volatility, predictable drivers.
2. **Adoption S-curve categories (RTP, wallets)**: Early CAGR overpredicts because growth rates decelerate as penetration increases.
3. **Regime-change categories (ETD, crypto)**: Historical CAGR is useless. Single policy decisions (India 0DTE options) or technology breakthroughs (Solana throughput) can cause 5-10x deviations.
4. **Nascent categories (AI agents, RWA)**: Any projection is essentially science fiction. The 2020-2025 trajectory of stablecoins (zero to $700 TPS) shows how fast new categories can emerge.

---

## 5. Power Law Distribution

Financial transaction TPS follows a power law. Plotting 2025 TPS on a log scale:

```
10^4+ : Consumer Cards (26,700), Digital Wallets (23,150), Bank Transfers (17,519)
10^3+ : ETD (9,505), CEX (3,500), Equity (2,067), E-Commerce (1,907)
        IoT (1,538), L1/L2 (1,100), Gov't (1,002), Stablecoins (700)
10^2+ : Gaming Microtx (415), P2P (301), Commodities (240), DeFi (130)
        Gaming Sales (97)
10^1+ : Remittances (61), Sec Settlement (47), FX (42), RTGS (14)
10^0+ : Fixed Income (3.8), RWA (2.4), AI Agents (0.66), OTC Derivs (0.16)
```

The top 3 categories (cards, wallets, RTP) represent 77% of all TPS. The bottom 10 categories combined represent <1%. This extreme concentration means that the "global TPS" number is overwhelmingly driven by consumer retail payments.

---

## 6. Cross-Cutting Observations

### The Value-Count Inversion
- **Highest TPS, lowest value/txn**: Consumer cards ($67 avg), digital wallets ($25 avg)
- **Lowest TPS, highest value/txn**: RTGS ($3.5M avg), OTC derivatives ($155M avg notional)
- The financial system has two fundamentally different throughput problems: mass retail (billions of small txns) and wholesale (millions of huge txns)

### The Overlay Problem
Modern payment flows create counting headaches:
- A consumer pays $50 at a store using Apple Pay (NFC) -> Visa (card rail) -> issuing bank (ACH settlement)
- This is ONE economic transaction but counts in: digital wallets, consumer cards, and bank transfers
- Our dedup factor (0.75 in 2025) tries to account for this, but it is a rough estimate

### The India Effect
India now appears in the top contributors for:
- **ETD**: NSE is #1 globally by contract count
- **Bank Transfers**: UPI is 46% of global RTP volume
- **Equity Markets**: NSE/BSE are #1/#7 by trade count
- **Digital Wallets**: UPI is simultaneously a wallet, RTP, and P2P system

India's financial digitization (driven by Aadhaar + UPI + NPCI policy) is arguably the single largest structural shift in global financial TPS in this decade.

### The "TPS Per Capita" View
Rough estimates:
- **US**: ~25B annual financial txns / 330M people = ~76 txns/person/year (cards dominate)
- **India**: ~200B+ annual financial txns / 1.4B people = ~143 txns/person/year (UPI dominate)
- **China**: ~300B+ annual financial txns / 1.4B people = ~214 txns/person/year (WeChat/Alipay)

China and India have higher per-capita digital financial transaction rates than the US, driven by mobile-first payment systems that bypassed card infrastructure.

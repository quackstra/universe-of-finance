# Peak TPS Analysis — Coordinated Global Maximum

> What happens when multiple categories hit peak load simultaneously?

**Author**: Emerging Tech Forecaster + Market Research Analyst (Run 5)
**Last Updated**: 2026-03-28

---

## 1. Per-Category Peak TPS (from REPORT.md data)

| Category | Avg TPS | Peak TPS | Peak Trigger | Confidence |
|----------|---------|----------|--------------|------------|
| Consumer Cards | 24,501 | 50,000–65,000 | Black Friday, Singles' Day, Christmas Eve | Low |
| Digital Wallets | 19,660 | ~45,000 | Singles' Day (Alipay) + UPI month-end | Medium |
| Bank Transfers | 15,338 | 25,000–30,000 | Month-end payroll + real-time payment spikes | Low |
| E-Commerce | ~1,800 | 600,000–1,000,000 | Singles' Day (Alibaba 583K orders/sec record) | Low |
| ETD | 9,505 | ~57,000 | Indian expiry days, triple witching | Low |
| Equity Markets | 3,500 | ~80,000 | Flash crash, circuit-breaker days, VIX spike | Low |
| CEX (wash-adjusted) | 3,040 | ~15,000 | Crypto crash/rally (FTX collapse, BTC halving) | Low |
| Government Payments | ~1,002 | 5,000–10,000 | Tax deadline day, benefits disbursement day | Low |
| L1/L2 Blockchain | 415 | ~5,000 | Major DeFi event, NFT mint, airdrop | Low |
| Stablecoins | ~520 | ~2,000 | De-peg panic, exchange withdrawal run | Low |
| IoT/M2M | ~1,538 | ~4,500 | Rush hour tolling (global concurrent) | Low |
| Gaming Microtx | ~389 | ~778 | Holiday sales, new release launch | Low |
| P2P Transfers | 270 | ~600 | US holiday weekends | Low |
| Securities Settlement | ~44 | ~6,300 | NSCC peak day (options expiry settlement) | Medium |
| Interbank RTGS | ~50 | ~130 | Cross-timezone concurrent settlement | Low |
| Commodities | ~330 | ~1,650 | Commodity shock day (OPEC decision, crop report) | Low |
| Forex | ~40 | ~160 | Central bank surprise (SNB floor removal type event) | Low |
| Remittances | 57 | ~100 | Eid, Christmas corridor peaks | Low |
| Fixed Income | ~7 | ~50 | Flight-to-quality day, Treasury auction settlement | Low |
| OTC Derivatives | ~0.15 | ~1.5 | Margin call cascades | Low |
| Game Sales | ~92 | ~275 | Steam Summer Sale, Black Friday digital | Low |
| RWA Tokenisation | ~2.4 | ~15 | Major fund launch | Low |
| AI Agents | ~0.66 | ~8.5 | Peak period (Dec 2025) | Medium |

---

## 2. Calendar Co-Occurrence Analysis

### Scenario A: Black Friday (Late November, US)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| Consumer Cards | 2.5x | ~61,250 | Highest card volume day globally |
| Digital Wallets | 1.5x | ~29,500 | Strong in US/EU; China not aligned |
| Bank Transfers | 1.2x | ~18,400 | Month-end payroll coincidence possible |
| E-Commerce | 5x+ | ~9,100 | Major e-commerce peak (but settles on card/bank rails) |
| Equity Markets | 0.5x (US closed) | ~1,750 | Half-day after Thanksgiving; Asia/EU normal |
| ETD | 0.7x | ~6,650 | US closed, lower global volume |
| CEX | 1.0x | ~3,040 | Crypto uncorrelated with retail shopping |
| Gaming | 2.5x | ~973 | Game sales peak |
| Government | 0.8x | ~802 | Not a government payment date |
| IoT/M2M | 1.3x | ~2,000 | Holiday travel tolling |
| **Total (de-dup)** | | **~95,000** | Cards, wallets, bank transfers dominate |

**Key insight**: Black Friday is the global payments peak but NOT a trading peak. US equity markets are closed. The peak is concentrated in payment infrastructure.

### Scenario B: Quarter-End (Last Business Day of March/June/Sept/Dec)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| Consumer Cards | 1.3x | ~31,850 | Above average but not peak |
| Digital Wallets | 1.2x | ~23,590 | Month-end spending patterns |
| Bank Transfers | 2.0x | ~30,680 | Payroll + corporate settlement + tax deadlines |
| ETD | 3.0x | ~28,500 | Triple/quadruple witching (options/futures expiry) |
| Equity Markets | 2.0x | ~7,000 | Window dressing, rebalancing |
| Securities Settlement | 3.0x | ~132 | Massive settlement backlog from expiry |
| RTGS | 2.0x | ~100 | Corporate payment deadlines |
| Government | 1.5x | ~1,503 | Quarter-end tax remittances |
| Commodities | 1.5x | ~495 | Contract rollovers |
| CEX | 1.0x | ~3,040 | Uncorrelated |
| **Total (de-dup)** | | **~105,000** | Trading + payments co-peak |

**Key insight**: Quarter-end is the most dangerous co-occurrence for infrastructure stress. Both payment systems AND trading venues hit peak simultaneously. Triple witching alone can push ETD to 3-6x normal volume.

### Scenario C: US Tax Deadline Day (April 15)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| Bank Transfers | 1.8x | ~27,600 | IRS estimated payments, corporate tax, ACH surge |
| Government | 5.0x | ~5,010 | 160M tax returns peak; IRS refund disbursement overlap |
| Consumer Cards | 1.1x | ~26,950 | Normal+ (some pay taxes on cards) |
| Digital Wallets | 1.0x | ~19,660 | Normal |
| Equity Markets | 1.2x | ~4,200 | Tax-loss harvesting/rebalancing |
| ETD | 1.0x | ~9,505 | Normal |
| CEX | 1.0x | ~3,040 | Tax selling possible |
| **Total (de-dup)** | | **~78,000** | Bank transfers + government dominate the delta |

### Scenario D: Chinese New Year / Singles' Day (November 11)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| Digital Wallets | 2.3x | ~45,000 | Alipay/WeChat red envelopes + purchases |
| Consumer Cards | 1.2x | ~29,400 | China UnionPay elevated; global normal |
| E-Commerce | 10x+ | ~18,230 | Singles' Day — Alibaba 583K orders/sec peak |
| Remittances | 1.5x | ~86 | Corridor spikes (SEA, East Asia) |
| Bank Transfers | 1.0x | ~15,338 | Normal globally |
| ETD | 1.0x | ~9,505 | Normal |
| CEX | 1.0x | ~3,040 | Normal |
| **Total (de-dup)** | | **~85,000** | Asia digital payment dominance |

**Note**: E-commerce peak TPS is enormous (583K+ orders/sec) but these are *commerce events*, not unique payment transactions. Each order settles on card/wallet/bank rails already counted above.

### Scenario E: Crypto Black Swan (Terra/LUNA collapse, FTX type event)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| CEX | 4.0x | ~12,160 | Exchange rush, liquidation cascades |
| L1/L2 Blockchain | 5.0x | ~2,075 | On-chain panic (DEX swaps, bridge withdrawals) |
| Stablecoins | 4.0x | ~2,080 | Flight to/from stablecoins |
| DeFi | 5.0x | *(subset of L1/L2)* | Liquidation cascades |
| Consumer Cards | 1.0x | ~24,501 | Unaffected |
| Bank Transfers | 1.0x | ~15,338 | Unaffected |
| ETD | 1.1x | ~10,456 | Crypto futures on CME elevated |
| **Total (de-dup)** | | **~75,000** | Crypto adds ~12K TPS on top of normal base |

**Key insight**: Even the worst crypto crash adds relatively little to global peak TPS because crypto's share of the total (~5%) limits its impact on the Big Number.

### Scenario F: Flash Crash + Volatility Cascade (2010-style or worse)

| Category | Peak multiplier | Est. TPS | Notes |
|----------|----------------|----------|-------|
| Equity Markets | 5.0x+ | ~80,000 | Circuit breakers, algo trading surge |
| ETD | 6.0x | ~57,000 | Hedging frenzy, VIX futures explode |
| Consumer Cards | 1.0x | ~24,501 | Normal |
| Bank Transfers | 1.0x | ~15,338 | Normal |
| Digital Wallets | 1.0x | ~19,660 | Normal |
| RTGS | 2.0x | ~100 | Margin calls require RTGS settlement |
| Securities Settlement | 2.0x | ~88 | Settlement backlog |
| CEX | 2.0x | ~6,080 | Crypto follows equity panic |
| Forex | 3.0x | ~120 | Safe-haven flows |
| Commodities | 2.0x | ~660 | Gold flight |
| **Total (de-dup)** | | **~170,000+** | Trading surge dominates |

**Key insight**: A flash crash is the scenario that most amplifies global TPS because equity markets and ETD together can surge to 137,000 TPS — nearly double the entire normal Big Number — while payments continue at their normal ~53,000 TPS base.

---

## 3. Estimated Coordinated Global Peak TPS

### The "Perfect Storm" Calendar Day

**December 31, Quarter-End + Year-End + Elevated Consumer Spending**

The highest plausible simultaneous load occurs when payment peaks and trading peaks co-occur:

| Component | Peak TPS | Basis |
|-----------|----------|-------|
| Consumer Cards | ~40,000 | Year-end elevated (not Black Friday peak) |
| Digital Wallets | ~30,000 | Year-end elevated |
| Bank Transfers | ~30,000 | Corporate year-end settlement + payroll |
| ETD | ~28,000 | Year-end expiry, contract rolls |
| Equity Markets | ~7,000 | Window dressing, year-end rebalancing |
| CEX | ~4,500 | Year-end crypto rally common |
| Government | ~3,000 | Year-end tax payments |
| IoT/M2M | ~2,000 | Holiday travel tolling |
| Gaming | ~800 | Holiday sales |
| Other (forex, commodities, etc.) | ~1,500 | Elevated |
| **Coordinated Peak** | **~147,000** | **2.1x average Big Number** |

### The "True Worst Case" — Volatility Event on a Busy Day

If a flash crash occurs on a quarter-end when consumer payments are already elevated:

| Component | Peak TPS | Basis |
|-----------|----------|-------|
| Equity Markets | ~80,000 | Circuit breakers, algo chaos |
| ETD | ~57,000 | Max observed multiplier on expiry day |
| Consumer Cards | ~35,000 | Quarter-end elevated |
| Bank Transfers | ~27,000 | Month-end elevated |
| Digital Wallets | ~25,000 | Slightly elevated |
| CEX | ~12,000 | Crypto follows equity panic |
| L1/L2 | ~5,000 | On-chain panic |
| Government | ~2,000 | Normal |
| All other categories | ~3,000 | Mixed |
| **Absolute Peak** | **~246,000** | **3.5x average Big Number** |

### Confidence Assessment

| Estimate | TPS | Confidence | Notes |
|----------|-----|------------|-------|
| Normal state (Big Number) | ~70,700 | Medium | Well-validated across 24 categories |
| Typical busy day | ~90,000–100,000 | Medium | Any major holiday or month-end |
| Quarter-end co-peak | ~120,000–150,000 | Low | Requires payment + trading alignment |
| Absolute worst case | ~200,000–250,000 | Very Low | Flash crash on busy day; modeled, never observed |

---

## 4. Comparison with Benchmark Systems

### Visa's Claimed Capacity: 65,000 TPS

- Visa's VisaNet has a **stated capacity** of 65,000 TPS (some sources say 83,000 TPS)
- Visa currently processes ~24,500 TPS average, peaking at ~50,000–65,000 on Black Friday
- **Implication**: Visa alone handles ~35% of global average financial TPS and could theoretically handle ~92% of it at peak capacity
- Visa's capacity headroom: ~1.3–2.7x their peak observed load

### Solana's Claimed Throughput: 65,000 TPS (theoretical)

- Solana's theoretical maximum is ~65,000 TPS
- Actual observed peak: ~4,000+ TPS (including vote transactions)
- After vote/spam filtering: ~350–480 meaningful TPS (average), ~2,000–2,500 peak
- **Implication**: Solana's claimed throughput (~65,000 TPS) would handle the current Big Number but has never demonstrated even 10% of that in real financial transaction throughput
- Gap between claim and reality: ~25–185x depending on what you count

### Comparison Table

| System | Claimed Capacity | Actual Peak | Utilisation | Could Handle Big Number? |
|--------|-----------------|-------------|-------------|--------------------------|
| VisaNet | 65,000–83,000 TPS | ~50,000–65,000 TPS | ~30–80% | Average yes, peak no |
| Solana | ~65,000 TPS (theoretical) | ~4,000 TPS (raw), ~2,500 (filtered) | ~4–6% | No (at current real throughput) |
| Ethereum L1 | ~15–30 TPS | ~15 TPS | ~50–100% | No |
| Ethereum + L2s | ~2,000+ TPS (aggregate) | ~500–800 TPS | ~25–40% | No |
| UPI (NPCI) | ~100,000 TPS (target) | ~11,250 TPS | ~11% | Average possibly, peak no |
| PIX (Brazil) | ~40,000 TPS (capacity) | ~3,500 TPS | ~9% | No at current capacity |
| FedNow | ~500,000 msg/sec (target) | early ramp-up | <1% | Designed for it, not tested |

### Key Takeaway

No single system can handle the global coordinated peak. The reason global finance works is that it runs on **hundreds of independent systems across dozens of time zones** that never all peak simultaneously. The ~70,700 average TPS is spread across:

- 6+ card networks (Visa, Mastercard, UnionPay, Amex, JCB, domestic schemes)
- 50+ real-time payment systems (UPI, PIX, FedNow, FPS, TIPS, etc.)
- 80+ equity exchanges
- 30+ derivative exchanges
- 13+ RTGS systems
- 100+ CEX platforms
- Dozens of L1/L2 blockchains

The distributed nature of global finance is not a bug — it's the architecture that makes ~70,700 TPS possible without any single point of failure.

---

*This analysis uses peak multipliers from individual REPORT.md files. Most peak estimates carry Low confidence — they are modeled from averages and seasonal patterns, not observed concurrent peak measurements. The coordinated peak estimates should be treated as order-of-magnitude guides, not precise predictions.*

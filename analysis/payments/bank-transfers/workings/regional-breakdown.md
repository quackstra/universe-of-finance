# Bank Transfers -- Regional/System Breakdown (2024)

> Workings file for the [Bank Transfers](../REPORT.md) capsule.
> Last updated: 2026-03-27

---

## Methodology

The 484B total annual bank transfer transactions (2024) is decomposed into individual payment systems using:

1. **Direct operator disclosures** -- NPCI (UPI), Nacha (US ACH), ECB (SEPA), Pay.UK (Faster Payments), BCB (PIX), PBOC (CNAPS/CIPS), Federal Reserve (Fedwire, FedNow)
2. **Industry benchmarks** -- ACI Worldwide Prime Time Report 2024 for global real-time payments
3. **Central bank reports** -- PBOC Payment System Report 2024, Bank of England, BOJ

The 484B total breaks down as: ~378B real-time + ~106B batch/ACH + ~0.4B RTGS/wire. This workings file decomposes each segment by individual system.

---

## Data Sources

| Source | Citation | Accessed |
|--------|----------|----------|
| ACI Worldwide | [Prime Time for Real-Time 2024](https://www.aciworldwide.com/real-time-payments-report) -- 266.2B RTP in 2023, ~42% growth | 2026-03-26 |
| NPCI | [UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics) -- 172.2B txns (CY2024) | 2026-03-27 |
| BCB (Brazil) | [PIX Statistics](https://www.bcb.gov.br/en) -- 63-69B txns (2024), ~52% YoY growth | 2026-03-27 |
| Nacha | [ACH Volume & Value](https://www.nacha.org/content/ach-network-volume-and-value-statistics) -- 33.6B txns, $86.2T | 2026-03-26 |
| ECB | [Payments Statistics H2 2024](https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2024h2~5ada0087d2.en.html) -- ~32B credit transfers | 2026-03-27 |
| Pay.UK | [FPS Statistics](https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/) -- 5.09B txns, GBP 4.2T | 2026-03-27 |
| Federal Reserve | [FedNow Volume](https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats) -- 1.5M txns, $38.2B | 2026-03-27 |
| Federal Reserve | [Fedwire Annual Stats](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) -- 210M txns, $1,133T | 2026-03-26 |
| PBOC | [Payment System Report 2024](http://www.pbc.gov.cn/en/3688247/3688978/3709143/5649949/2025040114593718714.pdf) -- 357.2B consumer txns | 2026-03-27 |
| CIPS | [Introduction](https://www.cips.com.cn/en/about_us/about_cips/introduction/index.html) -- 8.2M txns, RMB 175.5T | 2026-03-27 |
| NIBSS (Nigeria) | [NIP 2024](https://www.vanguardngr.com/2025/01/nigerias-instant-payment-transactions-hit-n1-07-quadrillion-in-2024-nibss/) -- 11.2B txns | 2026-03-27 |
| Statista / PromptPay | [Thailand PromptPay](https://www.statista.com/statistics/1131100/thailand-volume-of-promptpay-transactions/) -- ~24.3B txns (2024) | 2026-03-27 |
| AusPayPlus | [NPP Statistics](https://www.auspayplus.com.au/solutions/npp) -- 1.6B txns, A$1.99T | 2026-03-27 |
| ECB | [TARGET2 Facts](https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html) -- 108M txns (record) | 2026-03-26 |
| BOE | [CHAPS Annual Report](https://www.bankofengland.co.uk/report/2025/rtgs-and-chaps-annual-report-2024-25) -- 52.7M txns | 2026-03-26 |

---

## Breakdown Table -- Real-Time Payment Systems (2024)

| System | Country | Annual Txns (B) | Annual Value | YoY Growth | Share of Global RTP | Confidence |
|--------|---------|----------------|-------------|------------|-------------------|------------|
| **UPI** | India | 172.2 | ~$2.5T (INR 247T) | +46% | 45.6% | High |
| **PIX** | Brazil | ~66.0 | ~$5.0T (est.) | +52% | 17.5% | High |
| **PromptPay** | Thailand | ~24.3 | — | +22% (est.) | 6.4% | Medium |
| **China IBPS/mobile** | China | ~20.0 (est.) | — | — | 5.3% | Low |
| **SEPA Instant** | EU | ~5.0 | — | +72% (daily vol) | 1.3% | Medium |
| **UK Faster Payments** | UK | 5.09 | GBP 4.2T | ~5% | 1.3% | High |
| **Nigeria NIP** | Nigeria | 11.2 | NGN 1.07Q (~$700B) | +15.5% | 3.0% | High |
| **South Korea** | S. Korea | ~10.0 (est.) | — | +15% (est.) | 2.6% | Low |
| **US RTP (TCH)** | US | ~0.5 (est.) | — | ~50% (est.) | 0.1% | Low |
| **FedNow** | US | 0.0015 | $38.2B | +2,000% (from tiny base) | 0.0004% | High |
| **Australia NPP** | Australia | 1.6 | A$1.99T | +23% | 0.4% | High |
| **Japan Zengin (instant)** | Japan | ~2.0 (est.) | — | — | 0.5% | Low |
| **Other RTP systems** | Various | ~60.1 (est.) | — | — | 15.9% | Low |
| **TOTAL Real-Time** | | **~378** | | | **100%** | Medium |

**Note on China**: China's real-time payment landscape is complex. PBOC reports 357.2B consumer payment transactions, but the vast majority flow through Alipay/WeChat Pay (counted under Digital Wallets) rather than traditional bank-to-bank rails. The ~20B figure here represents bank-initiated instant transfers via IBPS (Internet Banking Payment System) and similar channels, excluding wallet-mediated flows.

---

## Breakdown Table -- Batch/ACH Systems (2024)

| System | Country | Annual Txns (B) | Annual Value | YoY Growth | Confidence |
|--------|---------|----------------|-------------|------------|------------|
| **US ACH (Nacha)** | US | 33.6 | $86.2T | +6.7% | High |
| **SEPA Credit Transfers** (non-instant) | EU | ~27.0 (est.) | ~EUR 210T | +5% (est.) | Medium |
| **SEPA Direct Debits** | EU | ~24.0 (est.) | ~EUR 15T | +4% (est.) | Medium |
| **UK Bacs** | UK | ~7.5 (est.) | — | -2% (est.) | Medium |
| **Japan Zengin** (batch) | Japan | ~2.2 (est.) | — | — | Low |
| **Australia BECS** | Australia | ~3.0 (est.) | — | declining | Medium |
| **Other ACH/batch** | Various | ~8.7 (est.) | — | — | Low |
| **TOTAL Batch/ACH** | | **~106** | | | Medium |

**Note**: SEPA totals (~32B credit transfers total) include both instant and non-instant. The ~5B SEPA Instant is counted under real-time above; the ~27B remainder here. SEPA Direct Debits are a separate scheme.

---

## Breakdown Table -- RTGS/Wire Systems (2024)

| System | Country | Annual Txns (M) | Annual Value | Avg Txn Size | Confidence |
|--------|---------|----------------|-------------|-------------|------------|
| **Fedwire** | US | 210 | $1,133T | $5.4M | High |
| **TARGET2/T2** | EU | 108 | ~$600T (EUR 556T) | ~$5.6M | High |
| **CHAPS** | UK | 52.7 | ~$150T (est.) | ~$2.8M | High |
| **CIPS** | China | 8.2 | $24.5T (RMB 175.5T) | $2.98M | High |
| **BOJ-NET** | Japan | ~15 (est.) | ~$200T (est.) | ~$13M | Low |
| **Other RTGS** | Various | ~6 (est.) | ~$150T (est.) | varies | Low |
| **TOTAL RTGS** | | **~400** | **~$2,258T** | | Medium |

---

## Reconciliation

| Segment | Our Sum (B) | REPORT.md Total (B) | Gap |
|---------|------------|--------------------|----|
| Real-time payments | 378 | 378 | 0 |
| Batch/ACH | 106 | 106 | 0 |
| RTGS/Wire | 0.4 | 0.4 | 0 |
| **TOTAL** | **~484.4** | **~484** | **~0.4 (0.08%)** |

### Sum of known systems vs. total

| Segment | Known Systems Sum | Segment Total | Unattributed |
|---------|------------------|--------------|-------------|
| Real-time | ~317.9B | 378B | ~60.1B (15.9%) |
| Batch/ACH | ~106B | 106B | ~8.7B (8.2%) |
| RTGS | ~394M | 400M | ~6M |

The **60.1B unattributed real-time transactions** likely include:
- **China domestic mobile** (not captured in IBPS -- Alipay/WeChat P2P bank transfers): ~15-25B
- **Indonesia, Philippines, Malaysia, Vietnam** real-time systems: ~10-15B combined
- **Mexico SPEI/CoDi**: ~3-5B
- **Saudi Arabia (SARIE), UAE (IPP), other Middle East**: ~2-3B
- **Other African systems** (Ghana GhIPSS, Kenya PesaLink, etc.): ~2-3B
- **Various smaller systems** in 80+ countries with live RTP: ~10-15B

---

## The Real-Time Payments Revolution -- Growth Comparison

| System | Launch Year | Time to 1B txns | Time to 10B txns | 2024 Volume (B) | Population Served |
|--------|------------|----------------|-------------------|-----------------|-------------------|
| UPI | 2016 | ~2.5 years | ~4 years | 172.2 | 1.4B |
| PIX | 2020 | ~1 year | ~2 years | ~66 | 215M |
| PromptPay | 2017 | ~3 years | ~5 years | ~24.3 | 72M |
| UK FPS | 2008 | ~3 years | never (5.1B total) | 5.09 | 67M |
| Nigeria NIP | 2011 | ~6 years | ~12 years | 11.2 | 220M |
| FedNow | 2023 | not yet | not yet | 0.0015 | 330M |

**Per-capita real-time transactions (2024)**:

| Country | RTP Txns/Person/Year | System |
|---------|---------------------|--------|
| Thailand | ~337 | PromptPay |
| Brazil | ~307 | PIX |
| India | ~123 | UPI |
| UK | ~76 | Faster Payments |
| Nigeria | ~51 | NIP |
| Australia | ~62 | NPP |
| US | ~0.005 | FedNow |

Thailand leads on per-capita real-time usage, followed closely by Brazil. The US is effectively at zero for real-time bank transfers -- a striking contrast given its economic development.

---

## Key Trends

1. **UPI and PIX together are 63% of global real-time volume.** Two systems, in two countries, processing 238B of 378B global real-time transactions. Both launched within the last 8 years.

2. **The US real-time gap is extraordinary.** FedNow processed 1.5 million transactions in 2024 -- approximately what UPI processes every 5 seconds. Even including TCH's RTP network (~500M est.), the US real-time volume is ~0.1% of India's.

3. **SEPA Instant is accelerating fast.** Daily volumes grew 72% in 2024 vs. 2023, driven by the EU Instant Payments Regulation mandating SEPA Instant adoption. This is the most significant regulatory catalyst for real-time payments in the developed world.

4. **Nigeria's NIP is Africa's real-time champion.** At 11.2B transactions, Nigeria processes more real-time payments than the UK, EU, and US combined. This is largely driven by the mobile money operator ecosystem (OPay, PalmPay, Moniepoint).

5. **RTGS value dwarfs everything.** Fedwire alone moved $1,133 trillion -- roughly 45x US GDP. The average Fedwire transfer ($5.4M) is 180,000x the average UPI payment (~$30). These are fundamentally different products under the "bank transfer" umbrella.

6. **China's payment system is uniquely fragmented.** With 357.2B consumer transactions via PBOC rails, 280B mobile payments, and an unclear boundary between bank-initiated and wallet-initiated flows, China's true bank transfer volume is the hardest to isolate in the entire dataset.

---

## Open Questions

1. **What is China's true bank-to-bank transfer volume?** PBOC reports 357.2B consumer payment transactions, but Alipay/WeChat Pay dominate. Isolating pure bank-transfer flows (excluding wallet-mediated) requires PBOC sub-categorization that is not publicly available in English.

2. **Will FedNow follow PIX's trajectory?** PIX went from 0 to 65B in 4 years. FedNow is at 1.5M after 18 months. The US banking structure (fragmented, legacy-heavy) suggests a slower curve, but Same Day ACH (1.2B, +45.3% YoY) shows demand exists.

3. **How should SEPA be counted?** SEPA Credit Transfers (~32B total) include both instant (~5B) and standard (~27B). The standard transfers settle in D+1, not "real-time" -- but they are electronic bank transfers. Our methodology counts standard SEPA under batch/ACH and SEPA Instant under real-time.

4. **Thailand's PromptPay volume precision**: The ~24.3B figure comes from Statista; the ACI report suggests ~18B for 2023. With 22% growth that would be ~22B, not 24.3B. The gap may reflect different counting methodologies (interbank vs. total including on-us).

5. **What percentage of UPI transactions are commercial vs. micro-tests?** NPCI data shows P2M (person-to-merchant) was ~59% of UPI volume in Dec 2024. But even P2P includes genuine transfers. The "frivolous transaction" share is likely <5% but unquantified.

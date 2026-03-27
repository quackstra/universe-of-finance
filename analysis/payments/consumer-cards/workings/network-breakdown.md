# Consumer Cards -- Network Breakdown (2024)

> Workings file for the [Consumer Card Payments](../REPORT.md) capsule.
> Last updated: 2026-03-27

---

## Methodology

The 772.73B total annual purchase transactions (2024, Nilson Report) is decomposed into individual card networks using a combination of:

1. **Direct disclosures** -- Visa 10-K (FY2024, Sep year-end), Mastercard 10-K (FY2024, Dec year-end), American Express annual report
2. **Derived estimates** -- UnionPay from PBOC consumer payment data + CoinLaw industry estimates; JCB from industry reports; Discover from Nilson/Capital One Shopping
3. **Domestic-only networks** -- RuPay (NPCI data), Elo (Brazilian card association estimates), Mir (Russian Central Bank / TAdviser)

"Branded transactions" = all transactions carrying the network's brand, regardless of who processes them. "Switched/processed transactions" = transactions routed through the network's own infrastructure. The Nilson 772.73B figure uses branded transaction counts for the six global networks.

---

## Data Sources

| Source | Citation | Accessed |
|--------|----------|----------|
| Nilson Report | Global Network Card Results Worldwide 2024 | 2026-03-26 |
| Visa 10-K FY2024 | [SEC Filing](https://s1.q4cdn.com/050606653/files/doc_financials/2024/ar/2ddc584c-441d-475b-8a97-630dad75db94.pdf) -- 303B branded, 233.8B processed | 2026-03-26 |
| Visa Q4 FY2024 Operational Data | [Earnings Release](https://s1.q4cdn.com/050606653/files/doc_financials/2024/q4/Q4-2024-Earnings-Release_vF.pdf) | 2026-03-26 |
| Mastercard 10-K FY2024 | [SEC Filing](https://www.sec.gov/Archives/edgar/data/1141391/000114139125000011/ma-20241231.htm) -- 159.4B switched txns (+11% YoY) | 2026-03-26 |
| Mastercard Earnings Review | [FY2024](https://www.mastercard.com/global/en/news-and-trends/stories/2025/earnings-review-2024-and-the-road-ahead.html) -- ~185B total branded | 2026-03-26 |
| American Express Annual Report 2024 | [PDF](https://s26.q4cdn.com/747928648/files/doc_financials/2024/ar/v2/American-Express-2024-Annual-Report.pdf) -- $1,551B billed business, 83.6M cards | 2026-03-26 |
| CoinLaw | [UnionPay Statistics 2025](https://coinlaw.io/unionpay-statistics/) -- 228B txns (2023), 8.96B cards | 2026-03-26 |
| PBOC Payment System Report 2024 | [Q4 2024](https://www.pbc.gov.cn/en/3688247/3688978/3709143/5649949/2025040114593718714.pdf) -- 357.2B consumer payment txns | 2026-03-27 |
| CoinLaw | [JCB Card Statistics 2025](https://coinlaw.io/jcb-card-statistics/) -- $410B+ volume (2025), 160M cardholders | 2026-03-27 |
| Capital One Shopping | [Credit Card Market Share 2025](https://capitaloneshopping.com/research/credit-card-market-share-statistics/) | 2026-03-26 |
| Nilson / GlobeNewsWire | [US networks >$10T in 2024](https://www.globenewswire.com/news-release/2025/02/25/3032247/0/en/Amex-Discover-Mastercard-and-Visa-Card-Spending-Exceeded-10-Trillion-in-2024.html) | 2026-03-26 |
| NPCI | [RuPay Statistics](https://coinlaw.io/rupay-statistics/) -- 18% India credit card market share | 2026-03-27 |
| TAdviser | [Mir Payment System](https://tadviser.com/index.php/Product:World_(payment_system)) -- 475M cards, 66.7% domestic share | 2026-03-27 |
| Elo / Rebill | [Elo Brazil](https://www.rebill.com/en/blog/what-is-elo) -- 14-20% Brazil market share, 120M+ cards | 2026-03-27 |

---

## Breakdown Table -- Global Card Networks (2024)

### Tier 1: The Six Global Networks (Nilson-counted)

| Network | Annual Txns (B) | Market Share | YoY Growth | Avg Txn Value | Confidence | Notes |
|---------|----------------|-------------|------------|---------------|------------|-------|
| **Visa** | 303.0 (branded) | 39.2% | ~10% | ~$58 | High | 233.8B processed by VisaNet; 69.2B processed by third parties on Visa rails |
| **UnionPay** | ~247.0 (est.) | 32.0% | ~8% (est.) | ~$68 (est.) | Medium | 228B in 2023 (CoinLaw); ~8% growth applied. 95%+ domestic China. |
| **Mastercard** | ~185.0 (branded) | 23.9% | ~11% | ~$62 | High | 159.4B switched (+11% YoY); ~185B total branded (est. from ratio) |
| **American Express** | ~15.0 (est.) | 1.9% | ~8% | ~$103 | Medium | $1,551B billed / ~$103 avg = ~15B txns. 83.6M cards. Highest avg txn. |
| **JCB** | ~11.0 (est.) | 1.4% | ~10% | ~$37 | Low | $410B volume (2025) / ~$37 avg. 160M cardholders. Japan-centric. |
| **Discover/Diners** | ~8.6 (est.) | 1.1% | ~-2% | ~$26 | Low | $225B volume / ~$26 avg. Declining slightly before Capital One merger. |
| **SUBTOTAL (6 networks)** | **~769.6** | **99.6%** | | | | |

### Tier 2: Major Domestic-Only Networks (not in Nilson 772.7B total)

| Network | Country | Annual Txns (B) | YoY Growth | Confidence | Notes |
|---------|---------|----------------|------------|------------|-------|
| **RuPay** | India | ~12.0 (est.) | ~30%+ | Medium | 18% of India credit card market; ~360M+ debit cards (PMJDY). NPCI data suggests 8.5B (FY2024) growing rapidly. Estimated 12B calendar 2024. |
| **Mir** | Russia | ~15.0 (est.) | ~15% | Low | 475M cards issued; 66.7% domestic transaction share. ~50M interbank txns/day. Estimated from daily clearing volume. |
| **Elo** | Brazil | ~5.0 (est.) | ~8% | Low | 14-20% of Brazil card market. 120M+ cards. No public transaction count. |
| **BC Card** | South Korea | ~4.0 (est.) | ~5% | Low | Major domestic network; limited English-language data. |
| **Other domestic** | Various | ~10.0 (est.) | varies | Low | TROY (Turkey), Verve (Nigeria), Bancontact (Belgium), etc. |
| **SUBTOTAL (domestic)** | | **~46.0** | | | Not included in Nilson 772.7B |

---

## Reconciliation

| Item | Volume (B) |
|------|-----------|
| Nilson Report 2024 total (6 global networks) | 772.73 |
| Our sum of 6 global networks | 769.6 |
| **Gap** | **3.13 (~0.4%)** |

**Gap explanation**: The 3.1B gap is well within estimation error for UnionPay and JCB, both of which are derived figures. Nilson may also include a small amount of co-branded or multi-network transactions. The reconciliation is strong -- within 0.4% of the reported total.

### Domestic networks and double-counting

The domestic-only networks (~46B) are **excluded** from the 772.73B Nilson figure. However, there is potential overlap:
- **RuPay-Discover alliance**: Some RuPay international transactions may route over Discover's network and be counted in Discover's total
- **Elo-Discover alliance**: Similarly, Elo has a co-badge arrangement with Discover for international acceptance
- **UnionPay domestic**: Nearly all of UnionPay's 247B transactions are China-domestic, but they ARE included in the Nilson global count as UnionPay is classified as a global network

**Adjusted global total including domestic networks**: ~772.7B (Nilson) + ~46B (domestic-only) = **~819B total card transactions worldwide** (2024).

---

## Debit vs. Credit Split (Where Available)

| Network | Debit Share (by count) | Credit Share (by count) | Prepaid | Source |
|---------|----------------------|------------------------|---------|--------|
| Visa | ~57% | ~35% | ~8% | Visa FY2024: debit $6.02T / credit $5.31T (value); count ratio skews further to debit |
| Mastercard | ~55% | ~38% | ~7% | Similar ratio to Visa; MC 10-K disclosures |
| UnionPay | ~75% (est.) | ~20% (est.) | ~5% | China heavily debit-dominated |
| American Express | ~0% | ~100% | ~0% | Amex is credit/charge only |
| JCB | ~15% (est.) | ~80% (est.) | ~5% | Japan market skews credit |
| Discover | ~45% (est.) | ~55% | ~0% | PULSE debit network + Discover credit |
| **Global weighted** | **~55%** | **~37%** | **~8%** | Consistent with REPORT.md |

---

## Key Trends

1. **Visa's branded vs. processed gap is widening.** Of 303B branded transactions, only 233.8B (77%) are processed by VisaNet. The 69.2B processed by third parties represents a growing segment of co-branded and regional processing arrangements.

2. **UnionPay is the great unknown.** As the #2 network by count, UnionPay's opacity is a significant data quality issue. The PBOC reports 357.2B consumer payment transactions in 2024, of which UnionPay card transactions are a subset (the remainder being mobile/QR payments via Alipay/WeChat Pay that bypass card rails).

3. **Mastercard is closing the gap on Visa in growth rate.** Mastercard's switched transactions grew 11% vs. Visa's 10% in 2024. At these rates, the gap narrows slowly but meaningfully over a decade.

4. **American Express has the highest average transaction value** (~$103 vs. ~$58 for Visa), reflecting its premium/corporate positioning. But at only 15B transactions on 83.6M cards, its per-card utilization (~180 txns/card/year) far exceeds other networks.

5. **Domestic networks are a hidden 6% of global card transactions.** RuPay (India), Mir (Russia), and Elo (Brazil) together process ~32B transactions that are invisible in standard global card statistics. RuPay is the fastest-growing, driven by India's push for domestic payment independence.

6. **Discover/Diners is the only declining network**, with volume slipping ~2% YoY as the Capital One acquisition creates uncertainty. Post-merger, Discover's network may see renewed investment or gradual absorption.

---

## Growth Rates by Network

| Network | 3-Year CAGR (2021-2024) | 5-Year CAGR (2019-2024) | Trend |
|---------|------------------------|------------------------|-------|
| Visa | ~12% | ~17% | Steady; post-COVID normalizing |
| UnionPay | ~8% (est.) | ~10% (est.) | Slowing; China mobile payments competing |
| Mastercard | ~13% | ~18% | Slightly outpacing Visa |
| American Express | ~9% | ~11% | Premium segment resilient |
| JCB | ~10% (est.) | ~8% (est.) | Japan cashless push driving growth |
| Discover | ~2% | ~5% | Stagnating; pre-merger uncertainty |
| RuPay | ~35%+ | ~40%+ | Hypergrowth; India govt backing |
| Mir | ~15% | N/A (2022 surge) | Post-sanctions capture of Russian market |

---

## Open Questions

1. **What is UnionPay's actual 2024 transaction count?** The 247B figure is extrapolated from 2023's 228B at ~8% growth. PBOC's 357.2B consumer payment transactions minus estimated mobile-only payments (~110B) gives ~247B as a cross-check, but this is circular reasoning if UnionPay = PBOC minus mobile.

2. **How many RuPay transactions are counted by Discover?** The RuPay-Discover co-badge arrangement means some international RuPay transactions route over Discover rails. Could be 100M-500M transactions -- small but relevant to Discover's total.

3. **Will Mir expand beyond Russia?** Currently used in ~12 countries (CIS states, Turkey, Vietnam). If sanctions persist, Mir could become a significant regional network. Current international volume is negligible.

4. **JCB transaction count precision**: JCB does not publish transaction counts in English-language reports. The ~11B estimate is derived from $410B volume / ~$37 average transaction, which is a rough proxy. Could be 8B-14B.

5. **What happens to domestic networks as digital wallets grow?** In China, Alipay/WeChat Pay bypass UnionPay for many transactions. In India, UPI competes with RuPay for debit transactions. The boundary between "card network" and "payment rail" is blurring.

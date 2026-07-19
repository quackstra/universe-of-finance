---
title: "Middle East"
parent: "Deep Dives"
layout: default
nav_order: 10
---

# Middle East Deep Dive — Regional TPS Analysis

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-07-19 (Run 13)

---

## Executive Summary

The Middle East is the **structural inverse of Africa**. Where Africa is defined by an
enormous *count* of tiny mobile-money transactions (43B+ per year, often under $1),
the Middle East is defined by a modest count of **extraordinarily high-value**
transactions: oil settlements, sovereign wealth flows, luxury real estate, and the
world's second- and third-largest remittance outflows.

We estimate the region (GCC core + Israel + Levant, **excluding** Egypt — covered under
[Africa](../africa/REPORT.md) — and Turkey) contributes approximately **~800
de-duplicated TPS**, roughly **1.1% of the global ~73,720 TPS**. That share understates
the region's importance: measured by transaction *value*, the Middle East punches far
above 1.1%, because its per-transaction ticket size is among the highest on Earth.

Three forces define the region:

1. **State-engineered digitization**: Saudi Arabia's Vision 2030 turned a cash economy
   into a digital one in under a decade. Electronic payments hit **79% of retail
   transactions in 2024**, up from 70% in 2023 — **12.6 billion non-cash retail
   transactions** ([SAMA / Saudi Payments](https://www.mada.com.sa/en)). The UAE
   launched its instant-payment rail **Aani** in October 2023; it grew **sixfold
   year-on-year** and now serves 12.5M users
   ([CBUAE](https://www.centralbank.ae/en/news-and-publications/news-and-insights/press-release/aani-delivers-a-transformational-leap-in-the-uae-s-digital-payments-landscape-12-5-million-users-and-instant-transfers-in-3-seconds/)).

2. **The remittance super-corridor**: The UAE sent **AED 183 billion (~$50B)** abroad in
   2024 and Saudi Arabia is the world's #2–#3 remittance source. Together the Gulf is
   the single largest *origin* of migrant remittances on the planet — a value story that
   dwarfs its transaction count
   ([Khaleej Times](https://www.khaleejtimes.com/business/remittance-boom-uae-leads-gcc-as-india-hits-record-1294b-in-2024)).

3. **Sovereign wealth as a transaction class**: GCC sovereign wealth funds (PIF, ADIA,
   KIA, QIA, Mubadala, ADQ) hold **~$4–5 trillion**. Their transaction *count* is
   negligible, but individual tickets run into billions. This is the purest example in
   the Universe of Finance of **value decoupled from count** — the mirror image of
   African mobile money.

The Middle East is the only region where a single wire transfer can move more value than
an entire African country's annual mobile-money volume, and where the dominant "fintech"
innovation — instant sovereign-backed rails — was **built top-down by central banks**,
not bottom-up by startups.

---

## The Region's Share Across Categories

```
Category                 ME TPS   Global TPS    ME Share
================================================================
Consumer Cards            ~500     24,501         2.0%   |
Bank Transfers            ~130     15,338         0.8%
Digital Wallets            ~95     19,660         0.5%
Bill Payments (SADAD+)     ~30      3,012         1.0%   |
Remittances (outbound)    ~7.5        57*        13.2%   |||||||  <- outsized
Equity Markets              ~8      3,500         0.2%
Interbank RTGS              ~3         50         6.0%   ||||
================================================================
* Remittances global TPS = 57 (net); ME is the world's largest ORIGIN by value.
  ME's share of global remittance VALUE is ~25-30%, far above its 13% count share.
```

**Reading this table**: the Middle East's transaction *count* share is small
(~1.1% blended), but two rows — **Remittances** and **Interbank RTGS** — punch far above
weight. Both are high-value, low-count rails. This is the fingerprint of the region.

---

## Country Breakdown

### Saudi Arabia — The Digitization Engine (~400 TPS)

Saudi Arabia is the largest transaction-count contributor in the region, driven by a
deliberate state program to displace cash.

| Rail | 2024 Volume | TPS | Source |
|------|-------------|-----|--------|
| **mada** (national card scheme) | 8.9B txns | ~282 | [WhiteSight](https://whitesight.net/how-saudi-arabia-engineered-a-digital-payments-boom/) |
| **sarie** (instant payments) | 593M txns | ~18.8 | [ClearingPost](https://clearingpost.com/insights/saudi-arabia-payment-infrastructure-guide-sarie-mada-sadad/) |
| **SADAD** (bill payments) | ~500M txns | ~15.9 | [PaymentBrief](https://paymentbrief.com/articles/saudi-arabia-mada-sarie-payment-stack/) |
| **All non-cash retail (blended)** | **12.6B txns** | **~399.5** | [mada](https://www.mada.com.sa/en) |

sarie (launched early 2021) grew at a **50% CAGR** to 593M transactions and exceeded
**100M/month** in 2025 — one of the fastest instant-payment ramps globally. mada
e-commerce alone reached **SR197.4B ($52.6B)** in 2024, +25.8% YoY. Electronic payments
now cover **79% of retail**, a figure most G7 economies took decades to reach.
**Confidence: 🟢 (SAMA/Saudi Payments publish systematically).**

### UAE — The Value Hub (~155 TPS)

The UAE is the region's financial and remittance capital. Its transaction *count* is
smaller than Saudi's, but its *value density* and cross-border role are higher.

| Rail | 2024 Metric | TPS | Notes |
|------|-------------|-----|-------|
| **Card payments** | Dh511.4B value (+13.3% YoY) | ~150 | POS = 80.7% of market; 82% contactless |
| **Aani** (instant, launched Oct 2023) | ~25k P2P/day, 12.5M users | ~0.3 | 6× YoY growth; 74 institutions connected |
| **Outward remittances** | AED 183B (~$50B) | ~3.8 | World's #2–#3 remittance origin |

Card *value* (Dh511.4B ≈ $139B) is high because average ticket sizes in the UAE are among
the world's largest. Aani is still nascent by count but growing faster than any rail in
the region. **Confidence: 🟡 (value data strong; transaction counts estimated from value
÷ avg ticket).**

### Qatar — Fawran's Fast Start (~35 TPS)

Qatar Central Bank launched **Fawran** in March 2024. It processed **QR 10.1B (~$2.8B)**
and **5.5M transactions** in its first 14 months
([Lightspark](https://www.lightspark.com/knowledge/instant-payments-qatar)). Card usage
dominates day-to-day retail in a wealthy, small (~3M) population. **Confidence: 🔴 (card
counts estimated; Fawran data early).**

### Kuwait — KNET Monopoly (~45 TPS)

**KNET** is the near-universal debit rail: **~80% of online transactions** run on KNET,
and ~80% of the ~5M issued cards are KNET debit
([Tap](https://blog.tap.company/local-payment-methods-middle-east/)). Kuwait remains
comparatively cash-heavy for a high-income state. **Confidence: 🔴 (KNET does not publish
annual counts; estimated from card base and GDP).**

### Bahrain — BenefitPay Breakout (~20 TPS)

Bahrain's **BenefitPay** app surged **+22%** to **421M transactions** in 2024, with
Fawri+ instant transfers reaching ~410M
([FCCIB](https://www.fccib.net/news/n/news/benefitpay-transactions-surge-by-22pc-in-2024.html)).
For a population of ~1.5M, that is one of the highest per-capita instant-payment
intensities in the world. **Confidence: 🟡 (Benefit publishes headline figures).**

### Oman & the Levant (~45 TPS combined)

Oman (~5M) is digitizing via the mobile payment switch and OmanNet, estimated ~15 TPS.
Israel (~9.8M, developed economy, high card usage + TASE) contributes an estimated ~100
TPS but is often analyzed separately from the Gulf. Jordan (JoMoPay), Lebanon (cash/dollar
crisis economy), and Iraq (largely cash + Qi Card government rails) add an estimated ~30
TPS combined. **Confidence: 🔴.**

---

## The Signature Insight: Value Without Count

The Middle East's defining characteristic is that its **share of global transaction value
vastly exceeds its share of transaction count.** Three structural reasons:

### 1. Sovereign Wealth Funds (~$4–5T AUM, near-zero count)

| Fund | Country | AUM (est.) |
|------|---------|-----------|
| ADIA | UAE (Abu Dhabi) | ~$1.1T |
| PIF | Saudi Arabia | ~$925B |
| KIA | Kuwait | ~$800B |
| QIA | Qatar | ~$530B |
| Mubadala | UAE (Abu Dhabi) | ~$330B |
| ADQ | UAE (Abu Dhabi) | ~$250B |

Combined **~$4–5 trillion**. A single PIF allocation or ADIA rebalancing can move
billions in one transaction. These flows are almost invisible in TPS terms (perhaps a few
transactions per day) yet represent value equal to years of an entire region's retail
payments. **This is the exact inverse of African mobile money** — there, billions of
transactions each move under a dollar. ([SWF Institute](https://www.swfinstitute.org/))

### 2. Oil & Commodity Settlement

Gulf oil exports (~18M barrels/day from GCC) settle in large, infrequent wholesale
transactions — often via interbank RTGS and correspondent USD rails. High value, low
count. This is why the region's **Interbank RTGS share (~6%) is 5× its count share.**

### 3. The Remittance Super-Corridor

The UAE ($50B) and Saudi Arabia (comparable) form the world's largest remittance *origin*.
Migrant workers (~28M in the GCC, roughly half the population) send home to India,
Pakistan, the Philippines, Egypt, and Bangladesh. India alone received **$129.4B** in
2024, much of it Gulf-sourced. By *count* these are ~7–8 TPS regionally; by *value* the
region originates ~25–30% of the world's formal remittance flow.

---

## Cross-Border & CBDC: Project mBridge

The UAE and Saudi Arabia are both participants in **Project mBridge**, the multi-CBDC
cross-border settlement platform (with China, Thailand, and Hong Kong). mBridge moved
past its minimum-viable-product stage in 2024 and represents the region's bet on
**bypassing correspondent banking** for high-value cross-border settlement. For the
Universe of Finance this is a category to watch: it sits at the intersection of the new
[CBDC category (7.3)](../../../TAXONOMY.md) and Interbank RTGS, and its whole design
premise is *high-value, low-count* — the regional signature again.
([BIS — mBridge](https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm))

---

## Islamic Finance Note

A meaningful share of regional transactions run through **Shariah-compliant**
instruments — sukuk (Islamic bonds), takaful (Islamic insurance), and murabaha financing.
These do not create a distinct *transaction rail* (they settle on the same card, RTGS, and
securities infrastructure) but they do shape *composition*: sukuk issuance and secondary
trading feed the Fixed Income category, and takaful feeds
[Insurance Premiums](../../../payments/insurance-premiums/REPORT.md). No double-count
adjustment is required — flagged here for completeness.

---

## Regional Total & De-Duplication

| Component | Gross TPS | Notes |
|-----------|-----------|-------|
| Saudi Arabia (blended retail) | ~400 | 12.6B non-cash retail |
| UAE | ~155 | Cards + Aani + remittance origin |
| Kuwait | ~45 | KNET-dominated |
| Qatar | ~35 | Cards + Fawran |
| Bahrain | ~20 | BenefitPay-led |
| Oman | ~15 | OmanNet |
| Israel | ~100 | Cards + TASE |
| Levant (Jordan/Lebanon/Iraq) | ~30 | Largely cash |
| Regional capital markets | ~8 | Tadawul/ADX/DFM/QSE/TASE |
| Interbank RTGS | ~3 | High value, low count |
| **Gross** | **~811** | Before overlap netting |
| **De-duplicated regional total** | **~800** | Instant/remittance overlaps netted |

**~800 TPS ≈ 1.1% of the global ~73,720 TPS.** Every number here is already *inside* the
global category totals (Saudi mada is part of global Consumer Cards, etc.) — this deep
dive slices the global figure by geography, it does not add to it.

---

## Key Findings

1. **The Middle East is Africa inverted.** Africa: many tiny transactions, low value.
   Middle East: few transactions, extreme value. The two regions bracket the entire
   count-vs-value spectrum of global finance.

2. **Digitization here was engineered top-down.** Unlike Kenya (M-Pesa, bottom-up) or the
   US (card networks, market-driven), Gulf instant-payment rails — sarie, Aani, Fawran,
   Fawri+ — were built by **central banks** as sovereign infrastructure. This produced
   the fastest national cash-to-digital transitions ever recorded (Saudi: 70%→79% retail
   electronic in one year).

3. **The Gulf is the world's remittance heart.** UAE + Saudi Arabia originate the largest
   share of global migrant remittances by value. This is a ~$100B+ annual outflow on a
   transaction count of only ~7–8 TPS — the highest value-per-transaction of any consumer
   payment rail in the Universe.

4. **Sovereign wealth is a hidden transaction class.** ~$4–5T in GCC SWF AUM transacts in
   billions-per-ticket, near-zero count. Invisible in TPS, enormous in value — the purest
   value/count decoupling we have catalogued.

5. **mBridge makes the region a CBDC frontier.** UAE and Saudi participation in the
   multi-CBDC bridge positions the Gulf to pioneer high-value cross-border settlement
   outside correspondent banking — a natural fit for its low-count, high-value profile.

6. **Confidence is bifurcated.** Saudi data is excellent (🟢); UAE value data is strong
   but counts are estimated (🟡); smaller Gulf states and the Levant are largely
   estimated (🔴) because their switches (KNET, OmanNet) do not publish annual counts.

---

## Sources

1. [WhiteSight — How Saudi Arabia Engineered a Digital Payments Boom](https://whitesight.net/how-saudi-arabia-engineered-a-digital-payments-boom/)
2. [ClearingPost — Saudi Arabia Payment Infrastructure Guide (SARIE, sarie, mada, SADAD)](https://clearingpost.com/insights/saudi-arabia-payment-infrastructure-guide-sarie-mada-sadad/)
3. [PaymentBrief — Saudi Arabia Mada, SARIE & STC Pay](https://paymentbrief.com/articles/saudi-arabia-mada-sarie-payment-stack/)
4. [mada — National Payment Scheme](https://www.mada.com.sa/en)
5. [Arab News — Saudi e-commerce Mada card sales hit $53bn in 2024](https://www.arabnews.com/node/2589350/business-economy)
6. [CBUAE — Aani: 12.5M Users, Instant Transfers in 3 Seconds](https://www.centralbank.ae/en/news-and-publications/news-and-insights/press-release/aani-delivers-a-transformational-leap-in-the-uae-s-digital-payments-landscape-12-5-million-users-and-instant-transfers-in-3-seconds/)
7. [CBUAE — Al Etihad Payments launches Aani](https://www.centralbank.ae/en/news-and-publications/news-and-insights/press-release/al-etihad-payments-launches-aani-an-instant-payments-platform-for-digital-transactions-in-the-uae/)
8. [Khaleej Times — Remittance boom: UAE leads GCC as India hits record $129.4b in 2024](https://www.khaleejtimes.com/business/remittance-boom-uae-leads-gcc-as-india-hits-record-1294b-in-2024)
9. [Khaleej Times — UAE card transactions set to surge to Dh565.5 billion](https://www.khaleejtimes.com/business/uae-card-transactions-set-to-surge-to-dh5655-billion)
10. [Lightspark — Instant Payments Qatar (Fawran)](https://www.lightspark.com/knowledge/instant-payments-qatar)
11. [FCCIB — BenefitPay transactions surge by 22pc in 2024](https://www.fccib.net/news/n/news/benefitpay-transactions-surge-by-22pc-in-2024.html)
12. [Tap — Accepting local payment methods: mada, KNET, Benefit](https://blog.tap.company/local-payment-methods-middle-east/)
13. [Qatar Central Bank — FAWRAN instant payment service](https://www.qcb.gov.qa/en/News/Pages/19feb24.aspx)
14. [SWF Institute — Sovereign Wealth Fund Rankings](https://www.swfinstitute.org/)
15. [BIS — Project mBridge (multi-CBDC bridge)](https://www.bis.org/about/bisih/topics/cbdc/mcbdc_bridge.htm)
16. [Saudi Exchange (Tadawul)](https://www.saudiexchange.sa/wps/portal/tadawul/home/)
17. [PaymentsCMI — UAE Remittances Market Data](https://paymentscmi.com/insights/united-arab-emirates-remittances-market-data-overview/)

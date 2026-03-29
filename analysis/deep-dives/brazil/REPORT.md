---
title: "Brazil"
parent: Deep Dives
grand_parent: Explore
---

# Brazil Deep Dive — Country-Level TPS Analysis

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-03-29

---

## Executive Summary

Brazil is Latin America's financial powerhouse and a top-10 contributor to global
financial TPS. With an estimated **~4,680 de-duplicated TPS** across all categories,
Brazil contributes roughly **6.3% of the global ~73,750 TPS** — a meaningful
overweight for an economy that represents ~2.1% of global GDP.

Brazil's significance spans three intersecting stories:

1. **Pix**: Brazil's instant payment system processed **68.7 billion transactions**
   in CY2024 — making it the world's #2 real-time payment system behind India's UPI.
   Pix reached this scale in just 4 years (launched November 2020), faster than UPI's
   trajectory. Over **170 million consumers** (93% of adults) use Pix.

2. **B3 Derivatives**: B3 is the **#2 derivatives exchange globally** by contract
   volume (~9.5B contracts in CY2024), and the dominant exchange in Latin America.
   Latin America traded 9.96 billion ETD contracts in 2024, with B3 accounting for
   the vast majority.

3. **Cards + Boleto**: Despite Pix's rise, Brazil maintains a large card ecosystem
   (~46B annual card transactions) and the unique Boleto Bancario payment slip system,
   creating a layered payment landscape unlike any other emerging market.

Brazil is the only country that simultaneously operates a top-3 real-time payment
system AND a top-3 derivatives exchange.

---

## Brazil's Share Across Categories

```
Category               Brazil TPS  Global TPS   Brazil Share
================================================================
Bank Transfers          2,179       15,338         14.2%  |||||||
ETD (Derivatives)         541        9,505          5.7%  ||
Consumer Cards          1,459       24,501          6.0%  |||
Bill Payments             190        3,012          6.3%  |||
Digital Wallets*        2,179       19,660         11.1%  |||||
Equity Markets             57        3,500          1.6%  |
Gov't Payments            101        1,002         10.1%  |||||
ATM Withdrawals           127        1,557          8.2%  ||||
Interbank RTGS              2           50          4.0%  ||
CEX (Crypto)               10        3,210          0.3%
Gaming (MTX)               12          389          3.1%  |
Commodities                 3          330          0.9%
================================================================
* Digital Wallets figure is gross (Pix); de-duplicated into Bank Transfers
```

---

## Brazil vs World — Comparison Table

| Metric | Brazil | World | Brazil's Share |
|--------|--------|-------|----------------|
| De-duplicated TPS | ~4,680 | ~73,750 | **6.3%** |
| Real-time payment txns (2024) | 68.7B (Pix) | 378B | **18.2%** |
| ETD contracts traded (2024) | ~9.5B | 205.3B | **4.6%** |
| Card transactions (2024) | ~46B | ~773B | **6.0%** |
| Government payment txns | ~3.2B | ~32B | **10.0%** |
| GDP | $2.2T | $110T | **2.0%** |
| Population | 213M | 8.1B | **2.6%** |

Brazil generates **3x its GDP-weight** in global financial TPS. The
transaction-to-GDP ratio is among the highest in the Americas, driven by
Pix micropayments and a mature card ecosystem.

---

## Category-by-Category Analysis

### 1. Pix — The World's #2 Real-Time Payment System

| Metric | Value | Source |
|--------|-------|--------|
| CY2024 volume | 68.7 billion txns | [Global Finance](https://gfmag.com/transaction-banking/pix-becomes-brazils-top-transaction-method/) |
| CY2024 value | ~R$17 trillion (~$5T) | [EBANX](https://insights.ebanx.com/en/five-years-on-pix-approaches-8-monthly-transactions/) |
| Monthly trajectory (2025) | ~7.9 billion txns/month | EBANX |
| Daily record | 252.1 million txns (Dec 20, 2024) | BCB |
| YoY growth (CY2024) | +52% by volume | Global Finance |
| Active users | 170 million+ (93% of adults) | EBANX |
| Average transaction | ~R$250 (~$45) | Derived |
| Global RTP share | **18.2%** of all real-time payments | Derived |
| 5-year CAGR (2020-2024) | **202%** | EBANX |
| P2B share of volume | 44% (overtook P2P at 43%) | EBANX |

**The growth curve rivals UPI.** Pix launched in November 2020 and processed
68.7 billion transactions by CY2024 — reaching 8 billion monthly transactions
faster than India's UPI (5 years vs UPI's 6 years 8 months). At current
trajectories, Pix will process **~95 billion transactions in CY2025**.

```
Year    Pix Txns (B)    Global RTP Share
2020         0.45            0.4%
2021         8.87            5.3%
2022        24.0            10.2%
2023        41.9            15.7%
2024        68.7            18.2%
2025E       ~95             ~22%
```

**Market structure**: Unlike UPI's two-app dominance (PhonePe + Google Pay = 85%),
Pix is integrated directly into every bank's app. The big five banks (Itau,
Bradesco, Banco do Brasil, Santander, Caixa) plus fintechs (Nubank, Inter,
PicPay) all provide native Pix access. No single app dominates.

**Comparison to UPI**: Both are central-bank-mandated, account-to-account,
zero-cost instant payment rails. Key differences:
- UPI uses a central switch (NPCI); Pix uses direct settlement via BCB's SPI
- Pix average ticket (~R$250/$45) is higher than UPI (~$17)
- UPI has 3x Pix volume but Pix grew faster in its first 4 years
- Pix has 93% adult adoption vs UPI's ~45% population penetration

**De-duplication note**: Like UPI, Pix is architecturally a bank transfer rail
(account-to-account). It appears in both Digital Wallets and Bank Transfers
categories. For de-duplication, it is classified under Bank Transfers.

---

### 2. Consumer Cards — Latin America's Largest Card Market

| Metric | Value | Source |
|--------|-------|--------|
| Q3 2024 card txns (quarterly) | 11.5 billion | [ABECS](https://rankingslatam.com/blogs/industry-news/brazil-payment-cards-market-trends-and-performance-insights-2024-09-overview-1) |
| CY2024 card txns (annualized) | ~46 billion | ABECS / Derived |
| Credit card txns (Q3 2024) | 5.0 billion (quarterly) | ABECS |
| Debit card txns (Q3 2024) | 4.1 billion (quarterly) | ABECS |
| Prepaid card txns (Q3 2024) | 2.4 billion (quarterly) | ABECS |
| Card market share: Mastercard | 51% | [Statista](https://www.statista.com/statistics/1312242/biggest-card-schemes-in-brazil/) |
| Card market share: Visa | 31% | Statista |
| Card market share: Elo | 14% | Statista |
| Contactless share | 61.1% of card payments (H1 2024) | ABECS |
| Credit card YoY growth | +13.1% (Q3 2024) | ABECS |
| Debit card YoY growth | -2.5% (Q3 2024) | ABECS |

**Brazil has a mature card ecosystem** — at ~46 billion annual card transactions,
it accounts for ~6% of global card volume. This is a dramatically different profile
from India (0.8% of global cards) because Brazil went through a full card adoption
cycle before Pix arrived.

**Elo — Brazil's domestic card brand**: Created in 2011 by Banco do Brasil,
Bradesco, and Caixa, Elo has reached 14% market share and is accepted at
essentially all merchants. It competes directly with Visa and Mastercard on
domestic transactions. Brazilian domestic card labels collectively hold ~10%
of the market.

**Pix impact on cards**: Debit cards are declining (-2.5% YoY in Q3 2024) as Pix
absorbs low-value point-of-sale transactions. Credit cards continue growing (+13.1%)
because installment payments ("parcelamento") remain a deeply embedded consumer
behavior in Brazil — merchants offer 2-12x interest-free installments on credit
cards, a feature Pix is only beginning to replicate.

---

### 3. B3 — Latin America's Dominant Exchange

#### Derivatives

| Metric | Value | Source |
|--------|-------|--------|
| CY2023 contracts | 8.3 billion | [FIA](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023) |
| CY2024 contracts (est.) | ~9.5 billion | FIA / B3 data (36% Dec YoY growth) |
| LatAm ETD volume (2024) | 9.96 billion | [FIA](https://www.fia.org/fia/articles/etd-volume-december-2024) |
| B3 share of LatAm ETD | **~95%** | Derived |
| B3 global rank | **#2** by contract volume | FIA |
| Open interest (end 2023) | 203.6 million contracts (+61.5% YoY) | FIA |
| Key products | Interest rate futures (DI), FX futures, equity index options | B3 |

**B3 is the #2 derivatives exchange globally**, behind only NSE India. Its
product mix is fundamentally different from NSE — where India is dominated by
equity index options, B3's largest product is interest rate futures (DI
contracts), reflecting Brazil's historically high and volatile interest rate
environment (Selic at 14.25% as of early 2025).

#### Equities

| Metric | Value | Source |
|--------|-------|--------|
| Dec 2024 equity ADTV | R$29.0 billion ($4.8B) | [Rio Times](https://www.riotimesonline.com/b3-stock-exchange-sees-20-6-jump-in-december-trading-volume/) |
| CY2024 equity ADTV change | -3.8% YoY (cash equities) | B3 IR |
| Individual investors | 5.26 million | B3 |
| BDR ADTV growth (2024) | +47% | B3 IR |
| ETF ADTV growth (2024) | +16% | B3 IR |
| B3 market cap | ~$0.8 trillion | B3 |
| Annual equity trades (est.) | ~1.8 billion | Derived from ADTV |

B3's equity market is smaller than India's by trade count (~1.8B vs ~18B) but
handles larger average trade sizes. The 2024 monetary tightening cycle reduced
risk appetite, leading to a 3.8% decline in cash equity ADTV. However, BDRs
(Brazilian Depositary Receipts for foreign stocks) surged 47%, indicating
growing international diversification among Brazilian investors.

---

### 4. Boleto Bancario — Brazil's Unique Payment Slip System

| Metric | Value | Source |
|--------|-------|--------|
| E-commerce volume (2024) | ~$27 billion | [PCMI](https://paymentscmi.com/insights/payments-ecommerce-trends-brazil-2024/) |
| E-commerce share | 8-10% of online sales | PCMI |
| Total annual txns (est.) | ~4-5 billion | Derived from BCB data |
| Trend | Declining, displaced by Pix | Multiple sources |

**Boleto Bancario is unique to Brazil** — a payment slip system where consumers
receive a barcode-based document and can pay it at any bank, ATM, lottery house,
or via internet banking. It served as the primary non-cash payment method for
decades before Pix.

Boleto remains important for:
- **Bill payments**: Utilities, rent, taxes, and government fees
- **E-commerce**: 8-10% of online purchases (declining from ~20% pre-Pix)
- **Unbanked population**: Can be paid in cash at lottery houses

Pix is rapidly absorbing Boleto's use cases. The same barcode infrastructure
is being integrated with Pix for seamless payment, but Boleto as a standalone
method is in structural decline.

---

### 5. Government Payments — Bolsa Familia and Beyond

| Metric | Value | Source |
|--------|-------|--------|
| Bolsa Familia beneficiaries | 20.8 million families (55.1M people) | [Policy Basket](https://policybasket.endhungerandpoverty.org/index.php/Brazil:_Bolsa_Fam%C3%ADlia) |
| Bolsa Familia annual disbursement | ~$32 billion (~R$168 billion) | World Bank / CEPAL |
| Bolsa Familia monthly transfers | ~R$14 billion | CEPAL |
| Minimum monthly payment | R$600/family | BCB |
| Annual government payment txns (est.) | ~3.2 billion | Derived |
| Coverage | ~25% of population | Policy Basket |

**Bolsa Familia is the world's largest conditional cash transfer program**,
reaching 55.1 million people (~25% of Brazil's population). At ~$32 billion
annually, it dwarfs India's DBT in per-capita terms though India's DBT reaches
more absolute beneficiaries.

Government payment transactions include:
- **Bolsa Familia**: ~249 million monthly disbursements (20.8M families x 12 months)
- **INSS pensions**: ~37 million beneficiaries, monthly payments
- **FGTS withdrawals**: Workers' severance fund, periodic disbursements
- **Tax refunds and government salaries**: Federal, state, and municipal

Combined, these generate an estimated ~3.2 billion annual government payment
transactions.

---

### 6. STR/Selic — Brazil's RTGS and Securities Settlement

| Metric | Value | Source |
|--------|-------|--------|
| STR annual value (2024) | R$13.68 trillion | [BCB](https://www.bcb.gov.br/en) |
| STR function | Real-time gross settlement | BCB |
| Selic system | Government securities settlement | BCB |
| Annual RTGS txns (est.) | ~60 million | Derived |

**STR (Sistema de Transferencia de Reservas)** is Brazil's RTGS system,
operated by BCB. It handles high-value interbank settlements. The Selic system
settles government securities (the name also applies to Brazil's benchmark
interest rate).

**TED (Transferencia Eletronica Disponivel)**: Brazil's large-value wire
transfer system, which runs through STR. TED handles ~65 million transactions
per month (~780M/year), moving R$3.3-3.9 trillion monthly. TED volume has
stabilized as Pix absorbs smaller transfers, but TED remains critical for
high-value corporate payments.

---

### 7. Drex — Brazil's CBDC (Digital Real)

| Metric | Value | Source |
|--------|-------|--------|
| Status | Pilot phase (Phase 2) | [BCB](https://www.bcb.gov.br/en) |
| Expected launch | Late 2025 / H1 2026 | CoinTelegraph / BCB |
| Pilot participants | Major banks, Visa, Mastercard, Microsoft | BCB |
| Use cases tested | 13 themes including tokenized securities, trade finance | BCB |
| Current TPS contribution | **Zero** (pilot only) | — |

**Drex is notable for its ambition**: Rather than simply creating a digital
currency, BCB is building a programmable money platform for tokenized assets,
DeFi-inspired use cases, and automated financial contracts. Phase 2 explores
13 themes including tokenized real estate, liquidity pools for government
securities, and international trade finance.

**Privacy challenge**: BCB postponed the original timeline after determining
that tested privacy solutions lacked "necessary maturity." The blockchain-
inspired component was ultimately scaled back due to high maintenance costs
and unresolved privacy issues. This makes Drex's trajectory uncertain —
it may launch as a more conventional wholesale CBDC rather than the
ambitious DeFi platform originally envisioned.

**TPS implication**: Drex has zero current TPS contribution. If launched at
scale with tokenized asset settlement, it could add meaningful volume, but
this is speculative. Not included in current estimates.

---

### 8. ATM Withdrawals — Cash Still Matters

| Metric | Value | Source |
|--------|-------|--------|
| Annual withdrawals (2024 est.) | ~4.0 billion | [ReportLinker](https://www.reportlinker.com/dataset/5ad11e5a2afe7aced9c8e9c38a9c8bf3f16b83bd) |
| ATMs in Brazil | ~178,000 | IMARC / ATMIA |
| CAGR (2018-2023) | +2.92% | ReportLinker |
| Forecast CAGR (2024-2028) | +0.99% | ReportLinker |

Despite Pix's dominance, Brazil still has ~4 billion ATM withdrawals per year.
Cash usage persists in the informal economy, street markets, and among the ~7%
of adults who don't use Pix. Growth is flattening as digital payments
absorb more use cases.

---

### 9. Digital Assets — Latin America's Crypto Hub

| Metric | Value | Source |
|--------|-------|--------|
| Crypto trading volume (Jan-May 2024) | $6 billion (BRL denominated) | [Chainalysis](https://newsletter.brazilcrypto.io/p/210-brazil-crypto-volumes-at-319) |
| Total crypto flows (2024-25) | $319 billion | Chainalysis |
| Market share: Binance | 79% | Chainalysis |
| Mercado Bitcoin users | 1.5 million+ | CoinMarketCap |
| Stablecoin share of trades | ~50% | Chainalysis |
| Global ranking | **#7** by fiat trade volume | Chainalysis |

Brazil is Latin America's largest crypto market and 7th globally by fiat
currency trade volume. Unlike India's punitive 30% tax, Brazil has a more
moderate regulatory framework. The BCB is actively developing crypto
regulation, and Drex's DeFi ambitions suggest openness to tokenized finance.

**Stablecoin dominance**: Nearly half of all crypto trades in Brazil involve
stablecoins (primarily USDT), reflecting demand for dollar-denominated savings
in a historically inflation-prone economy.

---

### 10. Gaming — The Mobile Giant of LatAm

| Metric | Value | Source |
|--------|-------|--------|
| Gaming market size (2025) | $5.64 billion | [IMARC](https://www.imarcgroup.com/brazil-gaming-market) |
| Mobile gaming share | 52.8% of revenue | IMARC |
| Mobile game downloads (2024) | 3.5 billion | [Tenjin](https://tenjin.com/blog/the-state-of-mobile-gaming-in-brazil-2025-data-trends-and-market-analysis/) |
| IAP share of revenue | 61.3% | IMARC |
| Global IAP ranking | #5 Android, #10 iOS | Tenjin |
| Average daily play time | 5+ hours | Tenjin |

Brazil is the largest gaming market in Latin America. With 3.5 billion mobile
game downloads in 2024 and IAP generating 61.3% of revenue, gaming
microtransactions are a growing contributor. Brazil ranks 5th globally for
Android in-app purchases.

---

## The Pix Effect — Brazil's Structural Transformation

### How Pix Reshaped Brazil's Payment Landscape

Pix's impact on Brazil mirrors UPI's impact on India, but with a key
difference: Brazil had a mature card ecosystem before Pix arrived. The
result is displacement rather than leapfrogging.

```
Payment Method    Pre-Pix (2019)    Post-Pix (2024)    Change
================================================================
Cash                 55%              ~15%              -40pp
Credit Card          20%               18%               -2pp
Debit Card           15%               10%               -5pp
Pix                   0%               47%              +47pp
Boleto                8%                5%               -3pp
TED/DOC               2%               <1%               -2pp
```

**Pix didn't just replace cash — it compressed the entire payment stack.**
Cash fell from 55% to ~15%. Debit cards lost 5 percentage points. Boleto
lost 3 points. TED/DOC became nearly irrelevant for consumer payments.
Only credit cards held relatively steady, protected by the installment
payment culture.

### The Installment Paradox

Brazil has a unique financial behavior: **parcelamento** (installment
payments). Consumers routinely split purchases into 2-12 interest-free
monthly installments on credit cards. This is so embedded in Brazilian
culture that prices are often quoted as "12x de R$50" rather than "R$600."

This protects credit cards from Pix displacement — until Pix Credit
(launching 2025-26) offers equivalent installment functionality. When that
happens, credit cards may face the same compression that debit cards
experienced.

### Pix vs UPI — The Two Giants Compared

```
Metric                     Pix (Brazil)         UPI (India)
================================================================
Launch year                2020                  2016
Year to 8B monthly txns    ~5 years             ~6.7 years
CY2024 annual txns         68.7B                172.0B
Adult adoption             93%                   ~45%
Avg transaction            ~$45                  ~$17
Zero merchant fee          Yes                   Yes
Architecture               Direct (SPI)          Switch (NPCI)
Operator                   BCB (central bank)    NPCI (non-profit)
```

Both systems prove that government-mandated, zero-cost instant payment
rails can achieve massive adoption. Brazil's higher per-capita adoption
(93% vs ~45%) reflects its smaller, more urbanized population and higher
smartphone penetration.

---

## The Transaction-to-GDP Anomaly

Brazil generates **3x its GDP-weight** in financial transaction volume:

```
Country         GDP Share    TPS Share    Ratio
India             3.5%        17.4%       5.0x
Brazil            2.0%         6.3%       3.2x
China            17.5%        ~20%        1.1x
United States    25.5%        ~25%        1.0x
Europe (EU)      16.5%        ~18%        1.1x
```

Brazil's overweight is driven by:

1. **Pix micropayments**: The average Pix transaction is ~$45, generating
   more transactions per dollar of economic activity than card-dominated
   economies.
2. **Card + Pix layering**: Brazil uniquely has both a mature card ecosystem
   AND a massive instant payment system, creating parallel transaction flows.
3. **Derivatives market depth**: B3's interest rate derivatives reflect
   Brazil's complex monetary environment (high rates, inflation history).
4. **Social transfer scale**: Bolsa Familia alone generates ~250 million
   annual disbursements to 25% of the population.

---

## Risks and Vulnerabilities

### 1. Pix Concentration Risk
Pix now handles 47% of all financial transactions. Any disruption to the
SPI (Pix's settlement infrastructure) would paralyze Brazilian commerce.
BCB has invested heavily in redundancy, but the concentration is unprecedented.

### 2. Monetary Policy Impact on B3
B3's derivatives volume is heavily correlated with interest rate volatility.
If Brazil achieves sustained low inflation and stable rates (historically
unusual), DI futures volume could decline significantly.

### 3. Credit Card Disruption
When Pix Credit (installment payments via Pix) launches, it could rapidly
erode credit card volume. This would reduce Brazil's total card TPS while
increasing Pix TPS — a category shift rather than net growth.

### 4. Drex Uncertainty
BCB's ambitious CBDC vision has been scaled back due to privacy and cost
concerns. If Drex launches as a limited wholesale system rather than a
retail platform, its TPS contribution will be negligible.

### 5. Informal Economy
Despite Pix's 93% adult adoption, Brazil's informal economy remains
significant (~40% of employment). Cash transactions in favelas, street
markets, and informal services are largely unmeasured.

---

## Key Takeaways

1. **Brazil is 6.3% of global financial TPS on 2.0% of global GDP** — a 3.2x
   overweight driven by Pix adoption, a mature card market, and B3 derivatives.

2. **Pix is the world's #2 real-time payment system**, processing 68.7B
   transactions in CY2024 with 93% adult adoption. It reached 8B monthly
   transactions faster than India's UPI.

3. **B3 is the #2 derivatives exchange globally** and accounts for ~95% of
   Latin American ETD volume. Its interest rate futures reflect Brazil's
   unique monetary environment.

4. **Brazil is the only country with both a top-3 RTP system AND a top-3
   derivatives exchange**, making it a uniquely diversified contributor to
   global TPS.

5. **Unlike India, Brazil didn't skip cards** — it has ~46B annual card
   transactions alongside Pix, creating a layered payment ecosystem. The
   installment culture (parcelamento) protects credit cards from immediate
   Pix displacement.

6. **Bolsa Familia is the world's largest conditional cash transfer program**
   by per-capita disbursement, reaching 25% of the population with ~$32B
   annually.

7. **Drex (CBDC) is ambitious but uncertain** — privacy and cost challenges
   have scaled back the original DeFi-inspired vision. Watch for the H1 2026
   launch timeline.

---

## Sources

1. [Global Finance — Pix Becomes Brazil's Top Transaction Method](https://gfmag.com/transaction-banking/pix-becomes-brazils-top-transaction-method/)
2. [EBANX — Pix Approaches 8 Billion Monthly Transactions](https://insights.ebanx.com/en/five-years-on-pix-approaches-8-monthly-transactions/)
3. [BusinessWire — Pix Transactions Exceed 6 Billion Monthly](https://www.businesswire.com/news/home/20250121148825/en/Pix-Transactions-Exceed-6-Billion-Monthly)
4. [FIA — Global Futures and Options Volume 2023](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023)
5. [FIA — ETD Volume December 2024](https://www.fia.org/fia/articles/etd-volume-december-2024)
6. [FIA — 2024 Annual ETD Volume Review](https://www.fia.org/fia/articles/2024-annual-etd-volume-review)
7. [ABECS / Rankings LatAm — Brazil Payment Cards Q3 2024](https://rankingslatam.com/blogs/industry-news/brazil-payment-cards-market-trends-and-performance-insights-2024-09-overview-1)
8. [Statista — Card Scheme Market Share Brazil](https://www.statista.com/statistics/1312242/biggest-card-schemes-in-brazil/)
9. [PCMI — Payment and Ecommerce Trends in Brazil 2024](https://paymentscmi.com/insights/payments-ecommerce-trends-brazil-2024/)
10. [Rio Times — B3 Stock Exchange December 2024](https://www.riotimesonline.com/b3-stock-exchange-sees-20-6-jump-in-december-trading-volume/)
11. [Policy Basket — Bolsa Familia](https://policybasket.endhungerandpoverty.org/index.php/Brazil:_Bolsa_Fam%C3%ADlia)
12. [BCB — Banco Central do Brasil](https://www.bcb.gov.br/en)
13. [Chainalysis — Brazil Crypto Volumes](https://newsletter.brazilcrypto.io/p/210-brazil-crypto-volumes-at-319)
14. [IMARC — Brazil Gaming Market](https://www.imarcgroup.com/brazil-gaming-market)
15. [Tenjin — State of Mobile Gaming in Brazil 2025](https://tenjin.com/blog/the-state-of-mobile-gaming-in-brazil-2025-data-trends-and-market-analysis/)
16. [ReportLinker — ATM Cash Withdrawals Brazil](https://www.reportlinker.com/dataset/5ad11e5a2afe7aced9c8e9c38a9c8bf3f16b83bd)
17. [WFE — FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-fy24-market-data-americas-region-leading-global-markets-despite-lowest-level-ipos-worldwide-last-5-years)
18. [BCB — SPI 2024 Annual Report](https://www.bcb.gov.br/content/financialstability/spi_annual_reports/SPI_2024.pdf)
19. [CoinTelegraph — Brazil Drex CBDC DeFi](https://cointelegraph.com/news/brazil-decentralized-finance-digital-real-cbdc)
20. [PagBrasil — Brazilian Domestic Card Labels Market Share](https://www.pagbrasil.com/blog/news/brazilian-domestic-card-labels-market-share/)

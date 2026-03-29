---
title: "Africa"
parent: "Deep Dives"
layout: default
nav_order: 8
---

# Africa Deep Dive — Continental TPS Analysis

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-03-29

---

## Executive Summary

Africa is the mobile money capital of the world and the most structurally distinct
financial ecosystem in the Universe of Finance. With an estimated **~2,870
de-duplicated TPS** across all categories, Africa contributes roughly **3.9% of the
global ~73,750 TPS** — modest in absolute terms, but remarkable given that Africa
represents only ~3.1% of global GDP and has the youngest, fastest-growing population
on Earth.

Africa's significance is defined by three forces:

1. **Mobile money**: Africa invented mobile money (M-Pesa, Kenya, 2007) and remains
   its global epicenter. GSMA reports **$832 billion** in mobile money transactions
   across Sub-Saharan Africa in 2023, with **1.75 billion registered accounts** and
   **12 million+ agents** — humans serving as the continent's ATM network. Mobile
   money works on feature phones, not smartphones — a critical distinction from
   digital wallets elsewhere.

2. **Nigeria's fintech explosion**: Africa's largest economy processed **5+ billion
   NIP (Nigeria Instant Payment)** transactions in 2023. A wave of fintechs —
   Flutterwave, Paystack, OPay, PalmPay — has built parallel payment infrastructure
   alongside the banks, serving 200+ million people in a country where 40% of adults
   were unbanked a decade ago.

3. **The informal economy**: 40-60% of GDP across much of Africa operates outside
   formal financial infrastructure. Cash, barter, and informal credit networks are
   not captured in any dataset. This makes Africa the largest blind spot in the
   Universe of Finance — our confidence score reflects this structural uncertainty.

Africa is the only continent where mobile money agents outnumber ATMs by 50:1,
where a $0.50 airtime transfer is a routine financial transaction, and where the
dominant payment rail runs on USSD menus, not apps.

---

## Africa's Share Across Categories

```
Category               Africa TPS  Global TPS   Africa Share
================================================================
Bank Transfers          1,380       15,338          9.0%  ||||
Digital Wallets*        1,380       19,660          7.0%  |||
Consumer Cards            285       24,501          1.2%  |
Bill Payments             210        3,012          7.0%  |||
ATM Withdrawals           175        1,557         11.2%  |||||
Gov't Payments            135        1,002         13.5%  ||||||
Equity Markets             18        3,500          0.5%
ETD (Derivatives)          11        9,505          0.1%
Interbank RTGS              1           50          2.0%  |
CEX (Crypto)              340        3,210         10.6%  |||||
Gaming (MTX)                8          389          2.1%  |
Commodities                 5          330          1.5%  |
================================================================
* Digital Wallets figure is gross (mobile money); de-duplicated into Bank Transfers
```

---

## Africa vs World — Comparison Table

| Metric | Africa | World | Africa's Share |
|--------|--------|-------|----------------|
| De-duplicated TPS | ~2,870 | ~73,750 | **3.9%** |
| Mobile money accounts (2023) | 1.75B registered | ~1.95B global | **~90%** |
| Mobile money txn value (2023) | $832B | ~$1.4T global | **~59%** |
| Mobile money agents | 12M+ | ~14M global | **~86%** |
| Card transactions (2024) | ~9B | ~773B | **1.2%** |
| P2P crypto volume (2023) | Highest adoption rate | — | **#1 globally** |
| GDP | $3.4T | $110T | **3.1%** |
| Population | 1.45B | 8.1B | **17.9%** |

Africa generates **1.3x its GDP-weight** in global financial TPS. The modest
overweight is entirely driven by mobile money transaction volumes. Formal capital
markets are underdeveloped relative to population. The real story is what is
*not* measured — the informal economy could double Africa's true transaction count.

---

## Category-by-Category Analysis

### 1. Mobile Money — Africa's Defining Financial Innovation

| Metric | Value | Source |
|--------|-------|--------|
| Registered accounts (SSA, 2023) | 1.75 billion | [GSMA State of the Industry 2024](https://www.gsma.com/mobilemoneymetrics/) |
| Active accounts (90-day, SSA) | ~400 million | GSMA |
| Transaction value (SSA, 2023) | $832 billion | GSMA |
| Transaction volume (SSA, 2023) | ~45 billion | GSMA / Derived |
| Mobile money agents (SSA) | 12 million+ | GSMA |
| Agent-to-ATM ratio | ~50:1 | Derived |
| Countries with mobile money | 50+ across Africa | GSMA |
| M-Pesa active users (Kenya) | 35 million+ | Safaricom |
| M-Pesa annual value (Kenya) | $300 billion+ | Safaricom |
| Average transaction value | ~$18 | Derived |

**Mobile money is not a digital wallet.** This is the most important conceptual
distinction for understanding Africa's financial infrastructure. M-Pesa and its
equivalents run on **USSD menus** (Unstructured Supplementary Service Data) — the
`*xxx#` codes that work on any phone, including $15 feature phones with no data
connection. There is no app. No smartphone required. No internet needed.

```
How M-Pesa Works (User Experience)
================================================================
1. Dial *334# on any phone (Kenya)
2. Select "Send Money"
3. Enter recipient phone number
4. Enter amount (e.g., KES 500 / ~$3.80)
5. Enter PIN
6. Transaction confirmed via SMS
================================================================
Total time: ~30 seconds. Works on a Nokia 1100.
```

**The agent network is the infrastructure.** Africa has 12 million+ mobile money
agents — small shop owners, kiosk operators, and market vendors who convert cash
to mobile money and vice versa. They are human ATMs. In rural Kenya, the nearest
bank branch may be 50 km away, but an M-Pesa agent is within 1 km.

```
Year    Mobile Money Txn Value (SSA, $B)    Registered Accounts (M)
====================================================================
2012           35                              140
2014           85                              300
2016          175                              500
2018          310                              750
2020          490                            1,000
2022          700                            1,400
2023          832                            1,750
```

**Market structure by country (mobile money value, 2023)**:
- **Kenya**: ~$300B+ (M-Pesa dominance, 35M+ active users)
- **Ghana**: ~$110B (MTN MoMo, Vodafone Cash, AirtelTigo)
- **Tanzania**: ~$85B (M-Pesa, Tigo Pesa, Airtel Money)
- **Uganda**: ~$55B (MTN MoMo, Airtel Money)
- **Francophone West Africa**: ~$95B (Orange Money, MTN, Wave)
- **Rest of SSA**: ~$87B+

**De-duplication note**: Mobile money is architecturally a stored-value account
system, not a bank transfer rail. However, mobile money-to-bank transfers and
bank-to-mobile money top-ups create overlap. For de-duplication, mobile money is
classified under Bank Transfers (similar treatment to UPI and Pix), as it represents
account-to-account value transfer regardless of the underlying technology.

---

### 2. Nigeria — Africa's Payment Powerhouse

| Metric | Value | Source |
|--------|-------|--------|
| NIP transactions (2023) | 5+ billion | [NIBSS](https://nibss-plc.com.ng/) |
| NIP transaction value (2023) | NGN 420+ trillion (~$500B) | NIBSS |
| NIP daily peak | ~20 million transactions | NIBSS |
| Active bank accounts | 150+ million | CBN |
| Fintech users | 100+ million | Industry estimates |
| eNaira (CBDC) wallets | ~13 million (low activity) | CBN |
| Banked adults (2023) | ~64% (up from ~40% in 2014) | EFInA |

**NIP (NIBSS Instant Payment)** is Nigeria's real-time payment system, operated
by Nigeria Inter-Bank Settlement System (NIBSS). It is Africa's largest instant
payment platform by volume, processing over 5 billion transactions in 2023.

**The fintech wave**: Nigeria's payment landscape has been transformed by fintechs:
- **OPay**: Backed by Opera, 35M+ monthly active users, processes ~80% of
  Nigeria's POS transactions
- **Paystack**: Acquired by Stripe (2020, $200M), powers online payments
- **Flutterwave**: $3B+ valuation, cross-border payments across Africa
- **PalmPay**: Chinese-backed, 30M+ users, targeting the unbanked
- **Moniepoint**: Business payments, 1M+ merchant terminals

These fintechs collectively process more retail transactions than traditional banks.

**eNaira — Africa's first CBDC**: Launched October 2021, the eNaira has ~13 million
wallets but low active usage. Adoption has been tepid — Nigerians prefer the
existing NIP/fintech ecosystem. The eNaira is a cautionary tale for CBDCs in
markets with already-functional instant payment systems.

---

### 3. South Africa — Africa's TradFi Hub

| Metric | Value | Source |
|--------|-------|--------|
| JSE market cap | ~$1.0 trillion | [JSE](https://www.jse.co.za/) |
| JSE daily equity trades | ~350,000 | JSE |
| JSE annual equity trades (est.) | ~88 million | Derived (252 trading days) |
| JSE derivatives contracts (annual) | ~120 million | JSE / FIA |
| PayShap transactions (2024) | Growing (launched 2023) | SARB |
| Card transactions (annual) | ~4.5 billion | BankservAfrica |
| EFT transactions (annual) | ~3.5 billion | BankservAfrica |
| ATM withdrawals (annual) | ~1.5 billion | BankservAfrica |
| Population | 62 million | Stats SA |

**JSE (Johannesburg Stock Exchange)** is Africa's largest and most sophisticated
exchange. At ~$1 trillion market cap, it dwarfs every other African exchange
combined. JSE offers equities, bonds, derivatives (equity index futures/options,
commodity derivatives, currency derivatives), and ETFs.

**PayShap**: South Africa's real-time low-value payment system, launched March 2023.
Built on ISO 20022 messaging standards, PayShap enables instant interbank transfers
using proxy identifiers (phone numbers, email). It is the South African equivalent
of Pix or UPI but is still in early adoption.

**South Africa's card market** is the most developed in Africa — ~4.5 billion annual
card transactions across Visa, Mastercard, and domestic schemes. Contactless
adoption is growing rapidly, driven by FNB, Standard Bank, Nedbank, and Absa.

**Dual economy challenge**: South Africa has both sophisticated formal financial
infrastructure (comparable to developed markets) and a large informal economy.
The formal/informal split creates measurement challenges — formal transaction data
is reliable, but ~30% of economic activity occurs outside tracked systems.

---

### 4. East Africa — The Mobile Money Heartland

| Metric | Value | Source |
|--------|-------|--------|
| Kenya M-Pesa active users | 35 million+ | Safaricom |
| Kenya M-Pesa txn value (2024) | $300 billion+ | Safaricom |
| Tanzania mobile money accounts | 40+ million | GSMA |
| Tanzania mobile money value | ~$85B annually | GSMA |
| Rwanda mobile money penetration | ~80% of adults | National Bank of Rwanda |
| Uganda mobile money accounts | 35+ million | Bank of Uganda |
| EAC total mobile money value | ~$500B+ | Derived |

**Kenya is where it all started.** M-Pesa launched in March 2007 — nearly a decade
before UPI (2016) and 13 years before Pix (2020). It proved that mobile phones
could serve as financial infrastructure in the absence of traditional banking.

The East African Community (EAC) — Kenya, Tanzania, Uganda, Rwanda, Burundi,
South Sudan, DRC — is the global epicenter of mobile money. Key characteristics:

- **Interoperability progress**: M-Pesa-to-Airtel Money transfers now work in
  several markets, though cross-border interoperability remains limited
- **Merchant payments growing**: Mobile money for retail purchases (pay-bill,
  till numbers) expanding beyond P2P transfers
- **Savings and credit**: M-Shwari (Kenya), MoKash (Uganda) layer savings and
  microloans on top of mobile money rails
- **Government integration**: Tax payments, utility bills, and government fees
  payable via mobile money in Kenya, Tanzania, Rwanda

---

### 5. Consumer Cards — Small but Growing

| Metric | Value | Source |
|--------|-------|--------|
| Africa card transactions (2024 est.) | ~9 billion | Visa / Mastercard Africa reports |
| South Africa share | ~50% (~4.5B) | BankservAfrica |
| Nigeria card transactions | ~2.5 billion | NIBSS |
| Egypt card transactions | ~800 million | CBE |
| Kenya card transactions | ~400 million | CBK |
| Rest of Africa | ~800 million | Derived |
| Card penetration (SSA avg) | ~5-8% of adults | World Bank Findex |

Africa's card market is small relative to global volumes — ~9 billion transactions
represents just 1.2% of the global ~773 billion. Cards are concentrated in South
Africa (which has a developed-market card ecosystem) and Nigeria (where debit cards
are common for ATM and POS use).

**Why cards are less relevant in Africa**:
- Mobile money bypassed cards for most of the population
- Card acceptance infrastructure (POS terminals) is sparse outside major cities
- Card fees are high relative to mobile money (which is often free for P2P)
- Feature phone users (still the majority in many markets) cannot use card-linked apps

**Growth drivers**: Visa and Mastercard are investing heavily in Africa — Visa's
2024 strategy explicitly targets 15 African markets for card expansion. Virtual
cards (linked to mobile wallets) and QR-code payments may create a hybrid
card-mobile money ecosystem.

---

### 6. Capital Markets — Early Stage but Growing

#### Equity Markets

| Metric | Value | Source |
|--------|-------|--------|
| JSE market cap | ~$1.0T | JSE |
| NGX (Nigeria) market cap | ~$55B | NGX |
| NSE Kenya market cap | ~$20B | NSE Kenya |
| EGX (Egypt) market cap | ~$45B | EGX |
| BRVM (West Africa) market cap | ~$15B | BRVM |
| Combined African exchange market cap | ~$1.4T | ASEA |
| Africa share of global equity market cap | **~1.3%** | WFE |
| Combined annual equity trades (est.) | ~560 million | Derived |

Africa's equity markets are dominated by the JSE, which accounts for ~70% of the
continent's total market capitalization. Outside South Africa, markets are
characterized by low liquidity, few listed companies, and limited retail
participation.

**BRVM (Bourse Regionale des Valeurs Mobilieres)** is notable as the world's only
exchange serving 8 countries — the francophone West African Economic and Monetary
Union (WAEMU: Benin, Burkina Faso, Cote d'Ivoire, Guinea-Bissau, Mali, Niger,
Senegal, Togo). Despite its innovative regional model, BRVM has low liquidity
and a market cap of only ~$15 billion.

#### Derivatives

African derivatives markets are minimal outside South Africa. JSE derivatives
(~120 million contracts annually) are the only meaningful volume. Nigeria's FMDQ
handles some OTC derivatives (FX forwards), but exchange-traded derivatives are
negligible elsewhere on the continent.

---

### 7. Cross-Border Payments — PAPSS and the AfCFTA Vision

| Metric | Value | Source |
|--------|-------|--------|
| Intra-African trade (2023) | ~15% of total trade | AfCFTA Secretariat |
| Remittances to SSA (2024) | ~$54 billion | World Bank |
| Average remittance cost to SSA | 7.9% (highest globally) | World Bank |
| PAPSS launch | January 2022 | Afreximbank |
| PAPSS participating central banks | 12+ | PAPSS |
| PAPSS transactions processed | Growing from low base | PAPSS |

**PAPSS (Pan-African Payment and Settlement System)** is potentially the most
important financial infrastructure development in Africa. Launched in January 2022
by the African Export-Import Bank (Afreximbank), PAPSS enables instant cross-border
payments in local currencies — eliminating the need to route through USD/EUR
correspondent banks.

Before PAPSS, a payment from Kenya (KES) to Nigeria (NGN) would typically:
1. Convert KES to USD at a Kenyan bank
2. Route through a US correspondent bank
3. Convert USD to NGN at a Nigerian bank
4. Settle in 3-5 business days, with 5-10% in fees

PAPSS enables direct KES-to-NGN settlement in seconds, at a fraction of the cost.

**AfCFTA (African Continental Free Trade Area)** — the world's largest free trade
area by member states (54 countries, 1.4B people) — relies on PAPSS to make
intra-African trade practical. Currently, only ~15% of African trade is
intra-continental (vs. ~60% in Europe, ~40% in Asia). The combination of AfCFTA
tariff reduction and PAPSS payment infrastructure could dramatically increase
cross-border transaction volumes.

**Remittance corridor fees**: Sub-Saharan Africa has the highest remittance costs
globally at 7.9% average (World Bank Q1 2024). For context, the global average is
6.2%, and the SDG target is 3%. High corridor fees drive crypto adoption for
cross-border transfers (see Section 9).

---

### 8. Government Payments — Cash Transfer Programs

| Metric | Value | Source |
|--------|-------|--------|
| Kenya Inua Jamii beneficiaries | ~1.1 million | Government of Kenya |
| South Africa social grants | ~18 million recipients | SASSA |
| South Africa grant value | ZAR 250B+ annually (~$14B) | SASSA |
| Nigeria social register | ~25 million households | NASSCO |
| Ethiopia PSNP beneficiaries | ~8 million | World Bank |
| Rwanda VUP beneficiaries | ~250,000 households | Government of Rwanda |
| Combined annual govt payment txns (est.) | ~4.25 billion | Derived |
| Africa share of global govt payments | **~13.5%** | Derived |

Africa's government payment landscape is shaped by large-scale social protection
programs, many supported by World Bank and development partners:

- **South Africa**: The most developed social grant system in Africa — SASSA
  (South African Social Security Agency) distributes grants to ~18 million
  recipients monthly, including old age pensions, child support grants, and
  disability grants. SASSA payments are increasingly made via bank accounts
  and SASSA cards, reducing cash distribution.

- **Nigeria**: The National Social Safety Net Program targets 25+ million
  households, with conditional cash transfers expanding. Distribution via
  mobile money and agent banking is growing.

- **Ethiopia**: The Productive Safety Net Programme (PSNP) serves ~8 million
  beneficiaries with cash and food transfers.

- **Kenya**: Inua Jamii (National Safety Net Programme) covers ~1.1 million
  elderly, disabled, and orphan beneficiaries via M-Pesa disbursement.

Mobile money has transformed government payment delivery across Africa —
disbursements that previously required physical cash distribution at government
offices can now be sent directly to mobile money wallets.

---

### 9. Digital Assets — Africa's P2P Crypto Hub

| Metric | Value | Source |
|--------|-------|--------|
| P2P crypto adoption rate | **Highest globally** | Chainalysis 2023 Geography of Crypto |
| Nigeria crypto users | ~30 million | Triple-A / Industry estimates |
| South Africa crypto users | ~6 million | Triple-A |
| Kenya crypto users | ~5 million | Triple-A |
| SSA crypto value received (2022-23) | ~$117 billion | Chainalysis |
| P2P share of volume | ~60%+ (vs. ~35% globally) | Chainalysis |
| Top use case | Remittances / FX hedging | Chainalysis |

**Africa has the highest P2P crypto adoption rate globally** (Chainalysis 2023).
This is not speculation-driven — it is utility-driven:

1. **Remittance cost arbitrage**: Sending $200 from the US to Nigeria via
   traditional channels costs $16-30 (8-15%). Via crypto P2P, it costs $2-5.
   At $54B in annual remittances to SSA, the savings potential is enormous.

2. **Currency devaluation hedge**: The Nigerian naira lost ~70% against the USD
   between 2022-2024. Nigerians use USDT and USDC as dollar-denominated savings
   vehicles, accessible via P2P platforms.

3. **Cross-border business payments**: African merchants importing goods from
   China use crypto to bypass SWIFT correspondent banking costs and delays.

4. **Banking access**: In countries with capital controls (Nigeria, Ethiopia),
   crypto provides an alternative rails for international value transfer.

**Regulatory landscape varies wildly**:
- **South Africa**: Regulated (FSCA licensing of crypto asset service providers)
- **Nigeria**: Hostile, then pragmatic (SEC framework emerging after initial bans)
- **Kenya**: Unregulated but tolerated
- **Central African Republic**: Briefly adopted Bitcoin as legal tender (2022),
  then reversed course
- **Most countries**: No clear framework

**P2P dominance**: Africa's crypto market is structurally different from other
regions. ~60%+ of volume is P2P (vs. ~35% globally), reflecting limited CEX
access and a culture of informal person-to-person finance that mirrors the
mobile money agent model.

---

### 10. ATM Withdrawals — The Cash-Mobile Money Bridge

| Metric | Value | Source |
|--------|-------|--------|
| Africa ATM withdrawals (2024 est.) | ~5.5 billion | ATMIA / RBR |
| ATMs in Africa | ~230,000 | ATMIA |
| South Africa ATMs | ~70,000 | SABRIC |
| Nigeria ATMs | ~20,000 | CBN |
| ATM-to-population ratio | 1 per 6,300 (vs. 1 per 700 globally) | Derived |
| Mobile money agents | 12,000,000+ | GSMA |
| Agent-to-ATM ratio | **~52:1** | Derived |

The agent-to-ATM ratio tells the story of Africa's financial infrastructure: there
are 52 mobile money agents for every ATM. In rural East and West Africa, agents
have almost entirely replaced ATMs as the cash access point.

ATM withdrawals remain significant in South Africa (~1.5B annually) and Nigeria
(~1.5B) where formal banking infrastructure exists. Elsewhere, the "cash-out"
function is served by mobile money agents — a user sends mobile money to an
agent and receives physical cash, or vice versa for "cash-in."

**This creates a measurement challenge**: Agent cash-in/cash-out transactions are
counted in mobile money volumes, not ATM volumes. The functional equivalent of
an ATM withdrawal in rural Kenya is an M-Pesa cash-out at an agent — but it shows
up in a completely different data category.

---

### 11. Gaming — Mobile-First, Low ARPU

| Metric | Value | Source |
|--------|-------|--------|
| Africa gaming revenue (2025 est.) | ~$2.0 billion | Newzoo / Statista |
| Mobile gaming share | ~75% | Newzoo |
| Nigeria gaming market | ~$600 million | Industry estimates |
| South Africa gaming market | ~$550 million | Industry estimates |
| Egypt gaming market | ~$350 million | Industry estimates |
| Kenya gaming market | ~$120 million | Industry estimates |
| IAP transactions (est.) | ~250 million | Derived |

Africa's gaming market is mobile-dominated and low-ARPU (average revenue per user).
Free-to-play mobile games with microtransactions are the dominant model. Console
and PC gaming are niche due to hardware costs and power reliability. Sports betting
platforms (Betway, SportPesa, Bet9ja) blur the line between gaming and gambling and
are a significant transaction generator, particularly in Nigeria and Kenya.

---

## The Mobile Money Effect — Africa's Structural Transformation

### How Mobile Money Rewired African Finance

Mobile money did not replace existing financial infrastructure in Africa — it *was*
the first financial infrastructure for hundreds of millions of people. Unlike Pix
(which replaced cards and cash in Brazil) or UPI (which replaced cash in India),
M-Pesa created a financial system where none existed.

```
Financial Access in Kenya (% of adults)
================================================================
Year    Formal Banking    Mobile Money Only    Excluded
2006        19%                0%                58%
2009        23%               28%                33%
2013        29%               33%                25%
2016        42%               41%                17%
2019        44%               43%                11%
2023        48%               44%                 8%
================================================================
Source: FinAccess Surveys / Central Bank of Kenya
```

**Key insight**: Mobile money did not cannibalize banking — it grew *alongside* it.
The "Excluded" population dropped from 58% to 8%, and most of that inclusion came
through mobile money, not banks. Kenya now has 92% financial inclusion — comparable
to developed economies — achieved primarily through a telecoms company (Safaricom),
not the banking sector.

### The Agent Banking Model

Africa's agent banking model is unique globally and poorly understood outside the
continent. The model works as follows:

```
Traditional Banking Model (developed world):
  Customer → Bank Branch → Electronic System → Settlement

Africa's Agent Model:
  Customer → Mobile Money Agent (corner shop) → Telco Platform → Settlement
  Customer → Agent Bank (market stall) → Bank Core System → Settlement
```

Agents are individual entrepreneurs who hold float (cash + mobile money balance)
and provide cash-in/cash-out services for a small commission. They require:
- A mobile phone
- Cash float (~$200-500)
- A registered mobile money account
- Basic training (~2 hours)

This model achieves financial infrastructure coverage at **1/100th the cost** of
bank branch networks. A bank branch in Kenya costs ~$500K to build and $200K/year
to operate. An M-Pesa agent costs $0 in infrastructure (they use their own phone
and shop) and earns revenue from commissions.

### Interoperability — The Remaining Challenge

Africa's mobile money ecosystem is fragmented across operators, countries, and
currencies. Key interoperability gaps:

1. **Operator-to-operator**: M-Pesa to Airtel Money transfers are now possible in
   several markets but still carry friction and fees
2. **Mobile money-to-bank**: Transfers between mobile wallets and bank accounts
   work but are not seamless in most markets
3. **Cross-border**: Sending mobile money across borders remains difficult despite
   PAPSS and bilateral agreements
4. **Currency**: Africa has 42 currencies — each cross-border transfer involves
   FX conversion, often at unfavorable rates

PAPSS (Section 7) addresses cross-border interoperability at the central bank
level. Domestic interoperability is improving market by market, with regulators
increasingly mandating open access to mobile money platforms.

---

## The Informal Economy — Africa's Unmeasured Majority

Africa has the largest informal economy relative to GDP of any continent. This is
the single biggest source of uncertainty in our TPS estimates:

```
Informal Economy as % of GDP (selected countries)
================================================================
Nigeria                    53%
Tanzania                   58%
Kenya                      34%
Ghana                      42%
Ethiopia                   38%
South Africa               28%
Egypt                      36%
DRC                        88%
================================================================
Source: IMF / World Bank Shadow Economy estimates
```

**What the informal economy means for TPS measurement**:

- A market trader in Lagos who sells goods for cash, mobile money, or informal
  credit generates transactions that are partially visible (mobile money) and
  partially invisible (cash, credit)
- Informal savings groups (chamas in Kenya, esusu in Nigeria, stokvels in South
  Africa) collectively hold billions of dollars but generate no formally tracked
  transactions
- Cross-border informal trade (estimated at 30-40% of intra-African trade) is
  entirely unmeasured

**Our estimate adjustment**: We apply a conservative 15-20% uplift to measured
mobile money volumes to account for mobile money transactions within informal
economies that are captured in GSMA data but whose economic activity is not
reflected in GDP. We do *not* attempt to estimate purely cash-based informal
transactions, as they are untraceable.

---

## Africa vs Other Emerging Markets

```
Metric                    Africa      India       Brazil      China
====================================================================
Population                1.45B       1.44B       213M        1.42B
GDP                       $3.4T       $3.9T       $2.2T       $19.3T
De-duplicated TPS         ~2,870      ~12,850     ~4,680      ~14,750
TPS per capita            0.002       0.009       0.022       0.010
Dominant payment rail     Mobile $    UPI         Pix         Alipay/WePay
Rail technology           USSD        App/QR      App/QR      App/QR
Smartphone required       No          Yes         Yes         Yes
Financial inclusion       ~55%        ~80%        ~96%        ~95%
Informal economy          40-60%      ~50%        ~40%        ~13%
Capital markets TPS       ~30         ~6,950      ~600        ~3,500
====================================================================
```

**Africa's unique position**: Lowest TPS per capita, but the only major economy
where the dominant payment rail works without a smartphone. Africa is 10-15 years
behind India and Brazil in formal financial digitization but has built a functional
alternative infrastructure on feature phones and human agents.

---

## Risks and Vulnerabilities

### 1. Fragmentation
54 countries, 42 currencies, hundreds of mobile money operators, dozens of
regulatory frameworks. Africa is not one market — it is 54 markets loosely
connected. PAPSS and AfCFTA aim to reduce fragmentation, but progress is slow.

### 2. Telco Concentration
Mobile money markets are often dominated by a single telco (Safaricom in Kenya,
MTN in Ghana/Uganda). Regulatory pressure for interoperability and competition
is growing, but telco leverage over financial infrastructure raises systemic risk.

### 3. Currency Volatility
Nigerian naira, Egyptian pound, and Ghanaian cedi have all experienced severe
devaluations (50-70%) in recent years. Currency instability drives crypto adoption
but also makes formal financial data unreliable in USD terms.

### 4. Infrastructure Gaps
Power reliability, internet connectivity, and physical infrastructure remain
constraints. Mobile money works on 2G networks, but more advanced fintech services
(app-based payments, crypto exchanges) require smartphones and data connectivity
that are still scarce in rural areas.

### 5. Regulatory Uncertainty
Several countries have reversed course on fintech regulation (Nigeria's crypto
ban/unban, CAR's Bitcoin legal tender reversal). Regulatory unpredictability
deters investment and creates compliance costs for cross-border operators.

### 6. Data Quality
Africa has the weakest financial data infrastructure of any continent. Many
central banks publish limited or delayed statistics. Mobile money data is good
(GSMA collects systematically), but card, equity, and banking data are patchy.

---

## Key Takeaways

1. **Africa is 3.9% of global financial TPS on 3.1% of global GDP** — a modest
   overweight driven entirely by mobile money volumes. Formal capital markets
   contribute very little.

2. **Africa is the mobile money capital of the world**: ~90% of global registered
   mobile money accounts, ~59% of global mobile money transaction value, and ~86%
   of global mobile money agents are in Sub-Saharan Africa.

3. **Mobile money is not a digital wallet** — it works on feature phones via USSD
   menus with no smartphone or internet required. This is a fundamentally different
   technology from UPI, Pix, Alipay, or Apple Pay.

4. **Nigeria's NIP processes 5B+ transactions annually**, making it Africa's largest
   instant payment system. Nigerian fintechs (OPay, Paystack, Flutterwave) have
   built parallel infrastructure alongside traditional banks.

5. **Africa has the highest P2P crypto adoption globally**, driven by remittance
   cost arbitrage (7.9% average fees to SSA) and currency devaluation hedging.
   This is utility, not speculation.

6. **PAPSS could be transformative** — enabling instant cross-border payments in
   local currencies across 54 countries. Combined with AfCFTA, it could materially
   increase intra-African trade and transaction volumes.

7. **The informal economy is the elephant in the room**: 40-60% of GDP in most
   African countries operates outside formal financial infrastructure. Our
   confidence score of 58 reflects this structural measurement gap.

8. **Africa is the only continent where human agents outnumber ATMs 50:1** — the
   agent banking model achieves financial infrastructure coverage at 1/100th the
   cost of traditional bank branches.

---

## Sources

1. [GSMA — State of the Industry Report on Mobile Money 2024](https://www.gsma.com/mobilemoneymetrics/)
2. [GSMA — Mobile Money Metrics](https://www.gsma.com/mobilemoneymetrics/)
3. [Safaricom — M-Pesa Statistics](https://www.safaricom.co.ke/about/media-centre)
4. [NIBSS — Nigeria Instant Payment Statistics](https://nibss-plc.com.ng/)
5. [CBN — Central Bank of Nigeria](https://www.cbn.gov.ng/)
6. [JSE — Johannesburg Stock Exchange](https://www.jse.co.za/)
7. [BankservAfrica — Payment Statistics](https://www.bankservafrica.com/)
8. [SARB — South African Reserve Bank](https://www.resbank.co.za/)
9. [Chainalysis — Geography of Cryptocurrency Report 2023](https://www.chainalysis.com/blog/2023-global-crypto-adoption-index/)
10. [World Bank — Remittance Prices Worldwide](https://remittanceprices.worldbank.org/)
11. [PAPSS — Pan-African Payment and Settlement System](https://papss.com/)
12. [AfCFTA Secretariat](https://au-afcfta.org/)
13. [Afreximbank — PAPSS Launch](https://www.afreximbank.com/)
14. [World Bank — Global Findex Database 2021](https://www.worldbank.org/en/publication/globalfindex)
15. [CBK — Central Bank of Kenya FinAccess Surveys](https://www.centralbank.go.ke/)
16. [IMF — Shadow Economy Estimates](https://www.imf.org/en/Publications)
17. [ASEA — African Securities Exchanges Association](https://african-exchanges.org/)
18. [NGX — Nigerian Exchange Group](https://ngxgroup.com/)
19. [SASSA — South African Social Security Agency](https://www.sassa.gov.za/)
20. [Triple-A — Crypto Ownership Data](https://triple-a.io/crypto-ownership/)

# India Deep Dive — Country-Level TPS Analysis

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-03-28

---

## Executive Summary

India is the single most important country in the Universe of Finance by transaction
count. With an estimated **~12,850 de-duplicated TPS** across all categories, India
contributes roughly **17.4% of the global ~73,750 TPS** — a staggering figure for an
economy that represents only ~3.5% of global GDP.

India's dominance spans three categories simultaneously:

1. **Real-time payments**: UPI processed **172 billion transactions** in CY2024
   (228.3B in CY2025) — more than all US electronic payments combined. It is the
   world's largest real-time payment system, accounting for **49% of all global
   real-time transactions** ([IMF](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569)).

2. **Exchange-traded derivatives**: NSE India is the world's largest derivatives
   exchange by contract volume. India accounts for **~62% of global ETD volume**,
   driven by the explosion in equity index options.

3. **Equity markets**: NSE is #3 globally by trade count at **18 billion equity
   trades** in 2024 (+74.3% YoY), representing **29.3% of global equity trades**
   on just 4% of global market cap.

No other country dominates three top-10 categories simultaneously.

---

## India's Share Across Categories

```
Category               India TPS   Global TPS   India Share
================================================================
ETD (Derivatives)       5,890        9,505         62.0%  ||||||||||||||||||||||||||||||||
Bank Transfers          5,630       15,338         36.7%  ||||||||||||||||||
Equity Markets          1,024        3,500         29.3%  ||||||||||||||
Gov't Payments            276        1,002         27.5%  |||||||||||||
Digital Wallets*        5,454       19,660         27.7%  |||||||||||||
ATM Withdrawals           190        1,557         12.2%  ||||||
Commodities                32          330          9.7%  ||||
Gaming (MTX)               25          389          6.4%  |||
Bill Payments              95        3,012          3.2%  |
Consumer Cards            197       24,501          0.8%
Interbank RTGS              9           50         19.0%  |||||||||
CEX (Crypto)                8        3,210          0.2%
================================================================
* Digital Wallets figure is gross (UPI); de-duplicated into Bank Transfers
```

---

## India vs World — Comparison Table

| Metric | India | World | India's Share |
|--------|-------|-------|---------------|
| De-duplicated TPS | ~12,850 | ~73,750 | **17.4%** |
| Real-time payment txns (2024) | 172B (UPI) | 378B | **45.5%** |
| ETD contracts traded (2024) | ~127.5B | 205.3B | **62.1%** |
| Equity trades (2024) | ~18B | ~61.5B | **29.3%** |
| Government payment txns | ~8.7B | ~32B | **27.2%** |
| Card transactions (2024) | ~6.2B | ~773B | **0.8%** |
| Demat/brokerage accounts | 500M+ | ~800M (est.) | **~63%** |
| Real-time payments per capita | 123/year | 48/year (avg) | **2.6x global avg** |
| GDP | $3.9T | $110T | **3.5%** |
| Population | 1.44B | 8.1B | **17.8%** |

India generates **5x its GDP-weight** in global financial TPS. The transaction-to-GDP
ratio is the highest of any major economy.

---

## Category-by-Category Analysis

### 1. UPI — The World's Largest Payment System

| Metric | Value | Source |
|--------|-------|--------|
| CY2024 volume | 172.0 billion txns | [NPCI](https://www.npci.org.in/product/upi/product-statistics) |
| CY2025 volume | 228.3 billion txns | [NPCI](https://www.npci.org.in/product/upi/product-statistics) |
| CY2024 value | ~Rs 247 lakh crore (~$2.9T) | [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569) |
| Monthly peak (Jan 2026) | 21.7 billion txns | [NPCI](https://www.npci.org.in/product/upi/product-statistics) |
| YoY growth (CY2024) | +57% by volume | NPCI |
| Average transaction | ~$17 (Rs 1,435) | Derived |
| Global RTP share | **49%** of all real-time payments | [IMF](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569) |
| Per-capita UPI txns | ~123/year | Derived |
| 5-year CAGR (2019-2024) | **89.4%** | NPCI |

**The growth curve is extraordinary.** UPI went from 18 million transactions in its
2016 launch year to 172 billion in CY2024 — a **7,285x increase in 7 years**.
By CY2025, it crossed 228 billion. At current trajectories, UPI will process
**300+ billion transactions in CY2026**, likely overtaking China's entire mobile
payment ecosystem by volume.

**Market structure**: PhonePe (48.4%) and Google Pay (36.9%) together handle 85.3% of
UPI volume. Paytm, CRED, and bank apps split the remainder.

**De-duplication note**: UPI is architecturally a bank transfer rail (account-to-account
via NPCI switch). It appears in both Digital Wallets and Bank Transfers categories.
For de-duplication, it is classified under Bank Transfers, and subtracted from Digital
Wallets.

#### Other NPCI Payment Systems

| System | CY2024 Volume | Notes |
|--------|---------------|-------|
| NEFT | 9.27B txns | Tripled from 2.6B (2019); batch transfers |
| IMPS | ~4.9B txns | Real-time interbank; declining as UPI absorbs use cases |
| NACH | ~6.5B txns (est.) | Automated clearing (recurring mandates, ECS replacement) |
| AEPS | ~1.0B txns (est.) | Aadhaar-enabled; rural financial inclusion |
| BBPS | Growing rapidly | Centralized bill payment; onboarding new billers |
| FASTag | ~4.5B txns (est.) | Electronic toll collection |

**Combined NPCI ecosystem**: ~200B+ transactions in CY2024 across all platforms.
NPCI processed nearly **230 billion transactions** across all platforms in FY2024-25.

---

### 2. Exchange-Traded Derivatives — The India Effect

| Metric | Value | Source |
|--------|-------|--------|
| NSE contracts (CY2023) | 84.8 billion | [FIA](https://www.fia.org/fia/articles/global-futures-and-options-volume-hits-record-137-billion-contracts-2023) |
| NSE contracts (CY2024 est.) | ~130B+ | FIA / NSE data |
| BSE contracts (FY2024-25) | ~20B+ | BSE / [Religare](https://www.religareonline.com/blog/nse-equity-derivatives-vs-bse-equity-derivatives/) |
| MCX ADT (FY2024-25) | Rs 2.19 lakh crore (+101% YoY) | [MCX](https://www.mcxindia.com) |
| India share of global ETD | **~62%** | FIA |
| NSE global rank | **#1** by contract volume | FIA |
| MCX global rank | **#3** in commodity options | FIA |
| Options share of India ETD | **~90%+** | FIA |

**The "India Effect" explained**: Between 2019 and 2024, global ETD volume grew from
34.5B to 205.3B contracts — a 6x increase. Nearly **all** of this growth came from
India. Futures volume globally remained flat at ~28-29B contracts. The entire increase
was in options, driven by Indian equity index options on NSE.

**What caused it**:
1. Weekly expiry contracts (multiplied trading opportunities)
2. Mobile trading apps (Zerodha, Groww, Angel One) bringing millions of retail traders
3. Small lot sizes ($500-1,500 per contract) making options accessible
4. Zero/low brokerage models reducing friction
5. 500M+ demat accounts creating a massive retail base

**SEBI regulatory risk**: India's concentration creates fragility. A single SEBI
decision (lot-size increases, weekly expiry restrictions) could move the global ETD
number by 20-30% overnight. SEBI has already begun tightening: lot-size increases
and margin requirements were introduced in late 2024.

**The TPS implication**: India alone adds **~5,890 TPS** to the ETD category.
Without India, global ETD would be ~3,600 TPS — comparable to 2019 levels.
India took ETD from **~800 TPS (2015) to ~9,500 TPS (2024)**.

---

### 3. Equity Markets — 29% of Global Trades on 4% of Market Cap

| Metric | Value | Source |
|--------|-------|--------|
| NSE equity trades (2024) | ~18.0 billion | [WFE](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024) |
| NSE global rank by trade count | **#3** | WFE |
| YoY trade growth (2024) | **+74.3%** | WFE |
| NSE market cap | $5.13 trillion | NSE |
| Demat accounts | 500M+ (CDSL + NSDL) | CDSL/NSDL |
| Demat account growth | ~15M/month | CDSL/NSDL |
| India share of global equity trades | **29.3%** | WFE |
| India share of global equity market cap | **~4%** | WFE |

The ratio of trade share to market cap share is **7.3x** — India trades far more
frequently per dollar of market cap than any other major market. This reflects:

- Massive retail participation (500M+ demat accounts vs. China's ~200M brokerage accounts)
- Mobile-first trading (Zerodha has 16M+ users)
- Small average trade sizes (~$300-500 vs. US ~$1,730)
- High day-trading activity among retail participants

**BSE context**: BSE (Asia's oldest exchange, est. 1875) adds further volume,
particularly in the derivatives segment where BSE has been growing rapidly. Combined
NSE + BSE, India likely accounts for **~30%+ of global equity trade count**.

---

### 4. Government Payments — The JAM Trinity

| Metric | Value | Source |
|--------|-------|--------|
| DBT transactions (FY2023-24) | 7.4 billion | [DBT Bharat](https://dbtbharat.gov.in/) |
| DBT schemes | 320+ (up from 28 in 2013-14) | [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2123192) |
| DBT beneficiaries | 176 crore (1.76B) | PIB |
| DBT cumulative savings | Rs 3.48 lakh crore | PIB |
| DBT funds transferred (FY2023-24) | Rs 6.91 lakh crore | PIB |
| GST active taxpayers | 15.3 million | [PIB](https://www.pib.gov.in/PressNoteDetails.aspx?id=154789) |
| GST cumulative returns filed | 164.4 crore (1.64B) | GSTN |
| GST collection (FY2024-25) | Rs 22.08 lakh crore (record) | GSTN |
| GST annual filings | ~362 million (15.1M taxpayers x ~24 returns) | GSTN |
| India share of global govt payments | **27.2%** | Derived |

**The JAM Trinity** (Jan Dhan + Aadhaar + Mobile) is the world's most advanced
government payment digitization infrastructure:

- **530M Jan Dhan bank accounts** — financial inclusion at scale
- **1.4B Aadhaar biometric IDs** — universal identity
- **UPI** — instant payment rail connecting identity to bank accounts

This infrastructure enables direct-to-beneficiary transfers that bypass
intermediaries, reducing corruption and leakage. DBT has saved Rs 3.48 lakh crore
(~$40B) through elimination of ghost beneficiaries and duplicate payments.

**GST digitization**: India's Goods and Services Tax (launched July 2017) is one of
the world's most digitized consumption tax systems. 15.3M active taxpayers file
~24 returns per year through the GST portal, with compliance consistently above 95%.
The GSTN processes Rs 22+ lakh crore in annual collections.

---

### 5. Consumer Cards — Surprisingly Small

| Metric | Value | Source |
|--------|-------|--------|
| Credit card txns (CY2024) | 4.47 billion | [RBI](https://www.rbi.org.in/Scripts/ATMView.aspx) |
| Debit card txns (CY2024) | 1.74 billion (declining) | RBI |
| Total card txns | ~6.21 billion | RBI |
| Credit card 5yr CAGR | 16.5% (volume) | RBI |
| Debit card trend | -19% CAGR (2019-2024) | RBI |
| RuPay cards issued | 700M+ | [CoinLaw](https://coinlaw.io/rupay-statistics/) |
| RuPay credit card market share | 18% | RuPay / NPCI |
| India share of global card txns | **0.8%** | Derived |

India's card market is paradoxically tiny relative to its payment volume. At ~6.2B
card transactions, India accounts for less than 1% of the global 773B card
transactions. The reason: **UPI has leapfrogged cards entirely**.

Where developed countries went cash -> cards -> mobile wallets, India went
cash -> UPI directly, skipping the card era for most of the population. Debit card
transactions are declining at 19% annually as consumers shift to UPI. Credit cards
are growing (16.5% CAGR) but from a small base.

**RuPay's role**: India's domestic card network (RuPay) has issued 700M+ cards,
primarily debit cards under the Jan Dhan financial inclusion programme. RuPay now
processes more credit card transactions by volume than Visa or Mastercard in India,
largely through UPI-linked credit card payments.

---

### 6. ATM Withdrawals — The Cash Paradox

| Metric | Value | Source |
|--------|-------|--------|
| Annual withdrawals (2024) | ~6.0 billion | [RBI](https://www.rbi.org.in/Scripts/ATMView.aspx) |
| ATMs in India | ~215,000 | RBI / ATMIA |
| Average withdrawal | ~$40 (Rs 3,300) | RBI |
| YoY change (count) | -5% | RBI |
| YoY change (value) | +5.5% | RBI |
| India share of global ATM txns | **12.2%** | Derived |

Despite UPI processing 172B transactions, India still has ~6B ATM withdrawals per year.
Cash remains sticky for rural transactions, daily-wage workers, and small vendors who
haven't adopted UPI. Notably, while the number of withdrawals is declining, the value
per withdrawal is growing — people make fewer but larger cash withdrawals.

India's ATM withdrawals are zero-overlap with electronic payments: these are
cash-out events where the subsequent spending is untraceable.

---

### 7. Digital Assets — Regulatory Headwinds

| Metric | Value | Source |
|--------|-------|--------|
| Crypto exchange market size | $1.61B (2024) | [IMARC](https://www.imarcgroup.com/india-cryptocurrency-exchange-market) |
| Top exchanges | Bitbns (79%), WazirX (11%), CoinDCX (7%) | CoinGecko |
| Combined user base | ~30M+ | Exchange reports |
| Tax regime | 30% capital gains + 1% TDS | India Finance Act 2022 |
| India share of global CEX | **~0.2%** | Derived |

India's crypto market has been severely suppressed by the punitive tax regime
introduced in 2022 (30% flat tax on gains with no loss offset, plus 1% TDS on every
transfer). This caused trading volumes to collapse by ~90% from 2021 peaks. The
WazirX hack ($235M stolen, July 2024) further damaged confidence.

Despite this, India has ~30M+ registered crypto users and the market is projected
to grow to $15.7B by 2033 (IMARC). If the tax regime were rationalized, India could
become a significant crypto market given its young, tech-savvy population and mobile
payment adoption.

---

### 8. Gaming — Mobile-First Market

| Metric | Value | Source |
|--------|-------|--------|
| Mobile gaming market | $3.02B (2024) | [IMARC](https://www.imarcgroup.com/india-mobile-gaming-market) |
| Game downloads (FY2024-25) | 8.45 billion | Sensor Tower |
| Paying gamers | 148 million | Industry reports |
| IAP revenue | ~$400M | Sensor Tower |
| ARPPU | $25-30 (up from $2-5) | Industry reports |
| In-game purchase share | 63.5% of gaming revenue | IMARC |

India is the world's largest mobile game market by downloads (8.45B in FY2024-25).
However, monetization lags developed markets — IAP revenue of ~$400M is modest
compared to China ($30B+) or the US ($15B+). The gap is closing: ARPPU has risen
sharply from $2-5 to $25-30, and in-app purchases are set to overtake ad revenue
by FY2030.

---

### 9. Commodities — MCX Dominance

| Metric | Value | Source |
|--------|-------|--------|
| MCX market share (India) | 97.84% | MCX |
| MCX ADT (FY2024-25) | Rs 2.19 lakh crore (+101% YoY) | [MCX](https://www.mcxindia.com) |
| MCX global rank | #3 in commodity options | FIA |
| Key products | Gold, silver, crude oil, natural gas, base metals | MCX |
| Single-day record | Rs 23.13 lakh crore (Nov 2025) | MCX |

MCX is a near-monopoly in Indian commodity derivatives (97.84% market share).
It trades bullion, energy, base metals, and recently launched India's first
electricity futures (July 2025). MCX's 101% YoY ADT growth reflects both
increased participation and the addition of new products.

---

### 10. Banking Infrastructure — RTGS and CCIL

| Metric | Value | Source |
|--------|-------|--------|
| RTGS transactions (CY2024) | 295.3 million | [RBI](https://rbidocs.rbi.org.in/rdocs/Publications/PDFs/PSR270120251BEE95CF47F2426B9740075D405FA070.PDF) |
| RTGS value (CY2024) | Rs 1,938 lakh crore | RBI |
| RTGS minimum | Rs 2 lakh ($2,400) | RBI |
| CCIL forex clearing (Dec 2024) | Rs 99.2 lakh crore (record) | [CCIL](https://www.ccilindia.com/) |
| NEFT transactions (CY2024) | 9.27 billion | RBI |
| NEFT value (CY2024) | Rs 432.8 lakh crore | RBI |

India's RTGS system handles high-value interbank settlement (minimum Rs 2 lakh per
transaction). CCIL clears government securities, forex, and money market instruments.
NEFT (batch transfers, now 24x7) has tripled in volume since 2019, processing
9.27 billion transactions in CY2024.

---

## The India Effect — A Structural Transformation

### How India Reshaped Global Transaction Volumes

India's impact on the Universe of Finance is not incremental — it is structural.
Three phenomena, all occurring simultaneously, have fundamentally altered global
transaction counts:

**1. The UPI Revolution (2016-present)**

UPI is the most dramatic growth curve in the history of financial infrastructure:

```
Year    UPI Txns (B)    Global RTP Share
2017         0.018            0.02%
2018         0.915            0.9%
2019         5.35             6.3%
2020        12.52            10.6%
2021        22.33            13.4%
2022        45.96            19.6%
2023        83.71            31.4%
2024       131.13            34.7%
2025       228.30            ~42%
```

UPI went from irrelevant to processing more transactions than Visa globally
in under 8 years. Key enablers: free merchant acceptance, zero MDR policy,
Aadhaar identity layer, and 600M+ smartphone users.

**2. The Derivatives Explosion (2019-present)**

India took global ETD from ~25B contracts (flat for a decade) to ~205B in
five years. This was entirely driven by equity index options on NSE:

```
Year    India ETD (B)    Global ETD (B)    India Share
2015        ~3                24.8             12%
2019        ~8                34.5             23%
2022       ~50                83.9             60%
2023       ~90               137.3             66%
2024      ~130               205.3             63%
```

India transformed ETD from a ~800 TPS category to a ~9,500 TPS category.

**3. The Retail Equity Boom (2020-present)**

India's demat account count exploded from ~40M (2019) to 500M+ (2025),
creating the world's largest retail investor base. This drove equity trade
counts up 74% in a single year (2024), making NSE the #3 exchange globally.

### The Transaction-to-GDP Anomaly

India generates **5x its GDP-weight** in financial transaction volume:

```
Country         GDP Share    TPS Share    Ratio
India             3.5%        17.4%       5.0x
China            17.5%        ~20%        1.1x
United States    25.5%        ~25%        1.0x
Europe (EU)      16.5%        ~18%        1.1x
```

This anomaly is driven by:

1. **Micropayments**: India's average UPI transaction is $17 (vs. US card avg $67).
   The same economic activity generates more transactions at lower average value.
2. **Zero-cost infrastructure**: UPI has zero merchant fees, encouraging adoption
   for even Rs 10 ($0.12) transactions.
3. **Derivatives accessibility**: NSE options at $500-1,500 per contract vs.
   CME at $100,000-200,000 — same market in different granularity.
4. **Population + smartphones**: 1.44B people x 600M+ smartphones = massive base.

---

## Digital Infrastructure Stack

India's transaction volume is built on a unique public digital infrastructure
stack that no other country has replicated at scale:

```
Layer 4: Applications
  PhonePe | Google Pay | Paytm | Zerodha | Groww | Angel One | CRED

Layer 3: Payment Rails
  UPI | IMPS | NEFT | RTGS | NACH | BBPS | FASTag | AEPS

Layer 2: Identity + Accounts
  Aadhaar (1.4B IDs) | Jan Dhan (530M accounts) | Demat (500M accounts)

Layer 1: NPCI Switch + RBI Infrastructure
  National Payments Corporation of India | Reserve Bank of India
  Clearing Corporation of India (CCIL) | NSE | BSE | MCX
```

The **India Stack** (Aadhaar + UPI + eKYC + DigiLocker) is a government-built
public good that private applications build on top of. This is structurally
different from the US model (private rails like Visa/Mastercard) or China's
model (private platforms like Alipay/WeChat Pay that became quasi-public).

---

## Risks and Vulnerabilities

### 1. Concentration Risk
A single SEBI decision on derivatives lot sizes could move the global ETD number
by 20-30% overnight. India's regulatory decisions now have global-scale impact.

### 2. UPI Sustainability
UPI operates on a zero-MDR model for most transactions. NPCI is profitable
(Rs 1,134 crore surplus in FY24), but the long-term sustainability of free
merchant payments at 230B+ transactions/year is an open question.

### 3. Quality vs. Quantity
Many Indian transactions are low-value (UPI avg $17, options contracts $500-1,500).
A $17 UPI tea payment and a $5.4M Fedwire transfer both count as "one transaction"
in TPS terms. India's TPS share overstates its economic significance relative
to GDP share.

### 4. Crypto Suppression
India's 30% crypto tax has effectively killed domestic crypto trading. If this
were rationalized, India could add significant CEX volume given its demographics.

### 5. Cash Persistence
Despite UPI dominance, India still has ~6B ATM withdrawals/year. Cash-to-digital
conversion is incomplete, particularly in rural areas and the informal economy.

---

## Key Takeaways

1. **India is 17.4% of global financial TPS on 3.5% of global GDP** — a 5x
   overweight driven by micropayments, free infrastructure, and retail
   participation.

2. **UPI is the world's largest payment system by transaction count**, processing
   more transactions than Visa, Mastercard, or China's mobile payment systems.
   It grew 7,285x in 7 years.

3. **India single-handedly transformed ETD from ~800 to ~9,500 TPS** through the
   retail options explosion on NSE. Remove India and ETD reverts to 2015 levels.

4. **The JAM Trinity (Jan Dhan + Aadhaar + Mobile) is the most successful
   financial inclusion programme in history**, enabling 7.4B+ annual DBT
   transactions reaching 1.76B beneficiaries.

5. **India skipped the card era**. At 0.8% of global card transactions, India
   went directly from cash to UPI, creating a fundamentally different payment
   landscape than any developed economy.

6. **Three categories would look dramatically different without India**:
   Bank Transfers (36.7% India share), ETD (62.1%), and Equity Markets (29.3%).
   India's removal would reduce the global Big Number by ~12,850 TPS (17.4%).

---

## Sources

1. [NPCI UPI Product Statistics](https://www.npci.org.in/product/upi/product-statistics)
2. [PIB — UPI as World's Largest Real-Time Payment System (IMF)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569)
3. [GrabOn — UPI Statistics 2016-2025](https://www.grabon.in/indulge/tech/upi-statistics/)
4. [DemandSage — UPI Market Share & Growth 2026](https://www.demandsage.com/upi-statistics/)
5. [FIA — 2024 Annual ETD Volume Review](https://www.fia.org/fia/articles/2024-annual-etd-volume-review)
6. [FIA — Meteoric Rise of India's Equity Derivatives](https://www.fia.org/marketvoice/articles/explainer-meteoric-rise-indias-equity-derivatives-volume)
7. [FIA — Premium Turnover in Indian Options Hits $150B](https://www.fia.org/marketvoice/articles/premium-turnover-indian-options-hits-150-billion)
8. [WFE FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)
9. [RBI Payment System Report H2 2024](https://rbidocs.rbi.org.in/rdocs/Publications/PDFs/PSR270120251BEE95CF47F2426B9740075D405FA070.PDF)
10. [Business Standard — Digital payments 99.7% of volume in 2024](https://www.business-standard.com/industry/news/digital-payments-make-up-99-7-of-transaction-volume-in-2024-rbi-report-125102301064_1.html)
11. [DBT Bharat Portal](https://dbtbharat.gov.in/)
12. [PIB — India's DBT Boosting Welfare Efficiency](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2123192)
13. [PIB — GST @ 8 Years Report](https://www.pib.gov.in/PressNoteDetails.aspx?id=154789)
14. [ClearTax — GST Collection Monthly Trends 2025](https://cleartax.in/s/gst-collection)
15. [OECD Revenue Statistics 2025](https://www.oecd.org/en/publications/2025/12/revenue-statistics-2025_07ca0a8e.html)
16. [RBI — Bankwise ATM/POS/Card Statistics](https://www.rbi.org.in/Scripts/ATMView.aspx)
17. [CoinLaw — RuPay Statistics 2026](https://coinlaw.io/rupay-statistics/)
18. [TechCrunch — India's Digital Payments Strategy Cutting Out Visa and Mastercard](https://techcrunch.com/2025/01/09/india-rupay-upi-payment-push-is-cutting-out-visa-and-mastercard/)
19. [MCX India](https://www.mcxindia.com)
20. [CCIL — The Clearing Corporation of India](https://www.ccilindia.com/)
21. [NSE India](https://www.nseindia.com/)
22. [IMARC — India Cryptocurrency Exchange Market](https://www.imarcgroup.com/india-cryptocurrency-exchange-market)
23. [IMARC — India Mobile Gaming Market](https://www.imarcgroup.com/india-mobile-gaming-market)
24. [Sensor Tower — India Mobile Game Insights 2025](https://sensortower.com/blog/india-mobile-game-insights-2025)
25. [CoinGecko — Top India Crypto Exchanges](https://www.coingecko.com/research/publications/india-crypto-exchanges)
26. [Factly — UPI Leads Volumes, RTGS Leads Values](https://factly.in/upi-leads-volumes-rtgs-leads-values-as-digital-payments-mature/)

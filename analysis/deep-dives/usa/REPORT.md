# USA Deep Dive — Country-Level TPS Analysis

> Part of the [Universe of Finance](../../../README.md) project.
> **Last Updated**: 2026-03-29

---

## Executive Summary

The United States is the single most important country in the Universe of Finance by
*economic weight* of transactions. With an estimated **~18,200 de-duplicated TPS** across
all categories, the USA contributes roughly **24.7% of the global ~73,750 TPS** — closely
matching its ~25.5% share of global GDP. This stands in stark contrast to India, which
generates 5x its GDP weight in transactions.

The USA's dominance is concentrated in three structural pillars:

1. **Consumer card payments**: The USA is the world's #1 card market. An estimated
   **~159 billion card transactions** in 2024 represent **20.6% of global card volume**
   ([Payments Dive / Nilson](https://www.paymentsdive.com/news/credit-card-us-market-payments-outpaced-by-other-world-regions/740595/)).
   US card spend exceeded **$10 trillion** for the first time
   ([GlobeNewsWire / Nilson](https://www.globenewswire.com/news-release/2025/02/25/3032247/0/en/Amex-Discover-Mastercard-and-Visa-Card-Spending-Exceeded-10-Trillion-in-2024.html)).

2. **Capital markets infrastructure**: NYSE + NASDAQ are the world's two largest
   exchanges by market cap ($50T+ combined). The US runs the deepest fixed income
   market (Treasury ADV crossed **$1 trillion** in 2024), the dominant derivatives
   complex (CME Group: 26.5M contracts/day ADV), and one side of **88% of all FX
   trades** involves the US dollar.

3. **Wholesale settlement**: Fedwire moved **$1,133 trillion** in 2024 — more than
   any other RTGS system on Earth. CHIPS settles **~$1.8 trillion per day**. Together
   they are the backbone of global dollar settlement.

Where India dominates by *transaction count* (micropayments, retail derivatives), the
USA dominates by *transaction value* and *systemic importance*. A Fedwire transfer
averaging $5.4 million and a UPI tea payment averaging $17 both count as "one
transaction" — but the economic gravity is vastly different.

---

## USA's Share Across Categories

```
Category               USA TPS    Global TPS   USA Share
================================================================
Consumer Cards          5,040       24,501        20.6%  ||||||||||
Bank Transfers (ACH)    1,116       15,338         7.3%  |||
Bill Payments             633        3,012        21.0%  ||||||||||
Digital Wallets           633       19,660         3.2%  |
P2P Transfers             244          270        90.6%  |||||||||||||||||||||||||||||||||||||||||||||
E-Commerce                380        1,823        20.8%  ||||||||||
BNPL                       49          175        28.0%  ||||||||||||||
Payroll                   108        1,305         8.3%  ||||
Equity Markets            540        3,500        15.4%  |||||||
ETD (Derivatives)         600        9,505         6.3%  |||
Commodities               178          330        53.9%  |||||||||||||||||||||||||||
Forex*                     16           40        40.0%  ||||||||||||||||||||
Fixed Income               74          105        70.5%  |||||||||||||||||||||||||||||||||||
OTC Derivatives*            2            5        40.0%  ||||||||||||||||||||
Interbank RTGS              7           13        50.0%  |||||||||||||||||||||||||
CEX (Crypto)              149        3,040         4.9%  ||
Gov't Payments            191          790        24.2%  ||||||||||||
ATM Withdrawals           238        1,557        15.3%  |||||||
================================================================
* Attributed via USD share of market, not geographic execution
```

---

## USA vs India — Comparison Table

| Metric | USA | India | Ratio |
|--------|-----|-------|-------|
| De-duplicated TPS | ~18,200 | ~12,850 | **1.4x** |
| Share of global TPS | 24.7% | 17.4% | 1.4x |
| GDP | $28.8T | $3.9T | 7.4x |
| GDP share | 25.5% | 3.5% | 7.3x |
| TPS-to-GDP ratio | 1.0x | 5.0x | India 5x |
| Card transactions (2024) | ~159B | ~6.2B | **25.6x** |
| Real-time payments (2024) | ~1.5M (FedNow) | 172B (UPI) | India 115,000x |
| ETD contracts (2024) | ~6.7B | ~130B+ | India 19x |
| Equity trades (2024) | ~9.5B | ~18.0B | India 1.9x |
| Treasury/Govt bond ADV | $1,055B | — | US dominant |
| Fedwire daily value | $4.5T | — | Unmatched |
| RTGS annual value | $1,133T | ~Rs 1,938L cr (~$232T) | US 4.9x |
| Avg card transaction | ~$63 | ~$17 (UPI) | US 3.7x |
| Population | 335M | 1,440M | India 4.3x |
| Transactions per capita | ~174/day | ~32/day | US 5.4x |

**The structural difference**: The USA processes *fewer* transactions than India in high-volume
categories (real-time payments, derivatives, equity trades) but vastly more in card payments
and vastly higher *value* across all wholesale categories. The USA is the world's financial
plumbing; India is the world's financial volume leader.

---

## Category-by-Category Analysis

### 1. Consumer Cards — The World's #1 Card Market

| Metric | Value | Source |
|--------|-------|--------|
| US card transactions (2024) | ~159 billion | [Payments Dive / Nilson](https://www.paymentsdive.com/news/credit-card-us-market-payments-outpaced-by-other-world-regions/740595/) |
| US card spend (2024) | $10+ trillion | [GlobeNewsWire / Nilson](https://www.globenewswire.com/news-release/2025/02/25/3032247/0/en/Amex-Discover-Mastercard-and-Visa-Card-Spending-Exceeded-10-Trillion-in-2024.html) |
| Share of global card transactions | 20.6% | Payments Dive / Nilson |
| Merchant processing fees (2024) | $187.2 billion | [Nilson Report](https://nilsonreport.com/articles/merchant-processing-fees-in-the-united-states-2024/) |
| Cards per capita | ~480 transactions/year | Derived |
| Credit share | ~35% of consumer payments | [Federal Reserve Payments Study](https://www.federalreserve.gov/paymentsystems/2024-November-The-Federal-Reserve-Payments-Study.htm) |
| Debit share | ~30% of consumer payments | Federal Reserve Payments Study |
| GP card transactions (2022, Fed) | 153.3 billion | Federal Reserve Payments Study |
| US card growth (10yr, 2014-2024) | +111% | Payments Dive |

The USA averages ~480 card transactions per person per year — 2.7x the EU average (~180).
This reflects the deeply embedded card culture: rewards programs, universal merchant acceptance,
and the absence of a free real-time payment alternative (FedNow is nascent). The US card market
grew 111% over the past decade while the Middle East & Africa region saw nearly 10x growth.

**Network breakdown (US)**:
- **Visa**: ~60% of US purchase volume
- **Mastercard**: ~25%
- **American Express**: ~10% (higher-value transactions)
- **Discover**: ~5%

**Key structural point**: Unlike India (which leapfrogged cards via UPI) or China (which
leapfrogged via Alipay/WeChat Pay), the USA *is* the card economy. Cards are the default
for everything from $2 coffee to $50K business procurement. This creates a ~5,040 TPS
contribution — the USA's single largest category.

---

### 2. Bank Transfers — ACH, Fedwire, and FedNow

| Metric | Value | Source |
|--------|-------|--------|
| ACH transactions (2025) | 35.2 billion | [Nacha](https://www.nacha.org/news/nachas-top-50-ach-originators-and-receivers-2025-now-available-total-ach-payment-volume-2025) |
| ACH transactions (2024) | 33.6 billion | [Nacha](https://www.nacha.org/content/ach-network-volume-and-value-statistics) |
| ACH value (2025) | $93 trillion | Nacha |
| ACH value (2024) | $86.2 trillion | Nacha |
| ACH including off-network (2025) | 42.1 billion | Nacha |
| Same Day ACH (2025) | 1.4 billion, $3.9T | Nacha |
| Same Day ACH growth | +16.7% YoY | Nacha |
| B2B ACH (2025) | 8.1 billion (+9.9% YoY) | [PYMNTS](https://www.pymnts.com/news/b2b-payments/2026/b2b-volume-on-ach-network-increased-9-9-in-2025/) |
| Fedwire transactions (2024) | 209.9 million | [FRB Services](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) |
| Fedwire value (2024) | $1,133 trillion | FRB Services |
| Fedwire daily avg | 836,322 txns, $4.5T | FRB Services |
| CHIPS daily | ~500,000 txns, $1.8T | [CHIPS/Wikipedia](https://en.wikipedia.org/wiki/Clearing_House_Interbank_Payments_System) |
| FedNow (Jan-Aug 2024) | 414,827 txns total | [FRB Services](https://www.frbservices.org/resources/financial-services/fednow/quarterly-volume-value-stats) |
| US share of global bank transfers | ~7.3% (by count) | Derived (35.2B / 484B) |

**The ACH paradox**: US ACH processes 35.2 billion transactions — more than the UK, EU SEPA,
and most other developed-market batch systems. But this is dwarfed by India's UPI (228B in 2025)
and Brazil's PIX (~63B). The US share of global bank transfers by *count* is just 7.3%, despite
being the world's largest economy. By *value*, however, ACH's $93T + Fedwire's $1,133T make
the US the dominant bank transfer economy.

**FedNow's slow start**: FedNow processed just 414,827 transactions in its first 8 months of
2024 — about 0.00031% of what India's UPI handles. The US real-time payment adoption is
67,000x lower than Thailand's PromptPay per capita. This is the single biggest gap in
US payment infrastructure.

**Same Day ACH as bridge**: Same Day ACH (1.4B transactions in 2025, +16.7%) is filling the
gap that FedNow was designed for. It processes 4x more transactions than FedNow and is growing
rapidly, potentially cannibalizing FedNow's addressable market.

---

### 3. Digital Wallets — Apple Pay Dominance

| Metric | Value | Source |
|--------|-------|--------|
| Apple Pay transactions (est.) | ~20 billion (2023) | [Electroiq](https://electroiq.com/stats/apple-pay-statistics/) |
| Google Pay (non-UPI, US) | ~2-3 billion (est.) | Industry estimates |
| Samsung Pay | ~1 billion (est.) | Industry estimates |
| Total US wallet transactions | ~20 billion (est.) | Derived |
| Wallet share of US POS | Growing rapidly | Various |

**Critical caveat**: Apple Pay, Google Pay, and Samsung Pay in the US are **overlay
transactions** — they ride on Visa/Mastercard rails. Every Apple Pay tap is also a card
transaction already counted in Consumer Cards. For de-duplication, US wallet transactions
are largely excluded from the USA TPS total (only non-card-rail wallet transactions count).

The US wallet market is structurally different from India (UPI is a native bank rail) or
China (Alipay/WeChat Pay are native mobile platforms). In the US, wallets are a UX layer
on top of cards, not a replacement for them.

---

### 4. P2P Transfers — Zelle, Venmo, Cash App

| Metric | Value | Source |
|--------|-------|--------|
| Zelle (2024) | 3.6B txns, $1.04T | [CNBC](https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html) |
| Venmo (2024 est.) | ~2.3B txns, ~$280B | [BusinessOfApps](https://www.businessofapps.com/data/venmo-statistics/) |
| Cash App (2024 est.) | ~1.5B txns, ~$283B | [BusinessOfApps](https://www.businessofapps.com/data/cash-app-statistics/) |
| PayPal P2P (non-Venmo) | ~0.3B txns (est.) | Estimated |
| US P2P total | ~7.7B txns, ~$1.75T | Composite |
| US share of global P2P | ~90.6% | Derived (7.7B / 8.5B global) |

The US utterly dominates the P2P transfers category, accounting for **over 90%** of global
dedicated P2P volume (excluding UPI and WeChat/Alipay P2P which are classified under Digital
Wallets). Zelle crossed $1 trillion in annual payments in 2024 — a milestone that took
11 years to achieve. Zelle's 5-year CAGR is 37% by transactions and 41% by value.

**Zelle vs UPI**: Zelle processed 3.6B transactions in 2024. UPI processed 228B in 2025.
The comparison is instructive: Zelle is bank-to-bank P2P only (no merchant payments), while
UPI is universal. But Zelle's average transfer ($289) dwarfs UPI's average ($17), reflecting
the US pattern of fewer, larger transactions.

---

### 5. Equity Markets — NYSE + NASDAQ

| Metric | Value | Source |
|--------|-------|--------|
| US equity ADV (shares, 2024) | 12.2 billion shares | [Nasdaq](https://www.nasdaq.com/articles/top-trading-trends-2024) |
| NYSE ADV | ~1.54B shares, $80.6B | [NYSE](https://www.nyse.com/trade/us-equity-volumes) |
| NASDAQ-listed ADV | ~5.0B trades (est.) | Derived from exchange data |
| NYSE-listed ADV | ~4.5B trades (est.) | Derived from exchange data |
| Total US equity trades (2024) | ~9.5B (est.) | Derived |
| US share of global equity trades | ~15.4% | Derived (9.5B / 61.5B) |
| Off-exchange share | 47% of TCV | [Cboe](https://ir.cboe.com/news/news-details/2025/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2024/default.aspx) |
| NYSE + NASDAQ market cap | $50T+ combined | NYSE / Nasdaq |
| Options ADV (2024) | 47.3M contracts | [Nasdaq](https://www.nasdaq.com/articles/top-trading-trends-2024) |
| ETF share of equity volume | 19.6% | Nasdaq |
| Retail share | 17.9% | Nasdaq |
| Avg trade size (US) | ~$1,730 | Derived |

The US equity market is structurally different from India's. NYSE + NASDAQ have the
largest combined market cap in the world ($50T+), but India's NSE generates ~1.9x more
equity trades by count on ~1/10 the market cap. US average trade size (~$1,730) is
~3.5x India's (~$500), reflecting institutional dominance vs. India's retail army.

**The dark pool phenomenon**: Nearly half (47%) of US equity volume now trades off-exchange
in dark pools and internalizers — the highest in the world. This is both a sign of market
sophistication (institutional block trading) and a regulatory concern (price discovery).

---

### 6. Exchange-Traded Derivatives — CME, Cboe, ICE

| Metric | Value | Source |
|--------|-------|--------|
| CME Group ADV (2024) | 26.5M contracts (record) | [CME Group](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html) |
| CME annual volume (2024) | ~6.7B contracts | Derived (26.5M x 252 days) |
| CME Interest Rate ADV | 13.7M (record, +10%) | CME Group |
| CME Treasury futures ADV | 8.1M (record) | CME Group |
| CME SOFR futures ADV | 5.2M (record) | CME Group |
| CME Metals ADV | Record (+23% YoY) | CME Group |
| CME Agriculture ADV | Record (+13% YoY) | CME Group |
| CME FX ADV | Record (+8% YoY) | CME Group |
| CME Bitcoin futures ADV | 19,000 (+56%) | CME Group |
| Cboe options volume (2024) | 3.8B contracts | [Cboe](https://ir.cboe.com/news/news-details/2025/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2024/default.aspx) |
| Cboe SPX options | 784.2M contracts | Cboe |
| Cboe VIX options | 209.2M contracts | Cboe |
| ICE commodity contracts (2024) | 1.2B (record) | [ICE](https://ir.theice.com/press/news-details/2025/ICE-Announces-That-a-Record-2-Billion-Contracts-Traded-in-2024/default.aspx) |
| US share of global ETD | ~6.3% (by contract count) | Derived (13B / 205B) |
| US share of global ETD (by notional) | ~45-50% (est.) | CME dominates IR notional |

**The notional vs. count paradox**: The US accounts for just ~6.3% of global ETD by
*contract count* (India dominates at 62%), but an estimated ~45-50% by *notional value*.
A single CME Treasury future ($100,000-$200,000 face) carries 100-200x the notional of an
NSE Nifty option ($1,000-$2,000). The US ETD market is institutional, high-value, and
globally systemic. India's is retail, high-frequency, and domestically concentrated.

CME Group alone is the world's leading derivatives marketplace by notional. Interest rate
products (13.7M ADV) underpin global rate setting (SOFR, Treasury curve). CME crypto
derivatives (Bitcoin futures ADV +56%) reflect the post-regulation US crypto landscape.

---

### 7. Commodities — CME/NYMEX, ICE, COMEX

| Metric | Value | Source |
|--------|-------|--------|
| CME commodity segments (2024) | ~3.5B contracts (est.) | CME Group (energy, metals, agriculture) |
| ICE commodity volume (2024) | 1.2B contracts (record) | ICE |
| ICE oil futures | 655M (Brent: 346M record) | ICE |
| US share of global commodity ETD | ~53.9% (est.) | Derived |

The US dominates global commodity derivatives through CME/NYMEX (energy, agriculture) and
COMEX (precious metals). ICE is the benchmark for global oil pricing (Brent crude = 75% of
internationally traded crude). CME agriculture and metals ADV both hit records in 2024.
The US is the pricing centre for the world's physical commodity markets.

---

### 8. Foreign Exchange — The Dollar's Dominance

| Metric | Value | Source |
|--------|-------|--------|
| USD share of all FX trades | 88% (one side) | [BIS Triennial Survey 2025](https://www.bis.org/statistics/rpfx25_fx.htm) |
| Global FX daily turnover (2025) | $9.6 trillion | BIS |
| US-attributed FX share (est.) | ~40% | NY Fed FX Committee data |
| CME FX futures ADV (2024) | ~1.0-1.2M contracts (record) | CME Group |

The US dollar is involved in **88% of all FX transactions** (BIS 2025). This means the
US financial system — through its banks, the Fed, and dollar-denominated instruments — is
a counterparty or reference point for nearly every FX trade on Earth. The NY Fed FX
Committee covers 21 major dealers that handle the bulk of US-located FX activity.

FX attribution to the US is complex: a EUR/USD trade between a London bank and a Singapore
hedge fund involves the dollar but may execute in neither the US nor on US infrastructure.
We attribute ~40% of institutional FX TPS to the US based on NY Fed share data and the
dollar's reserve currency role.

---

### 9. Fixed Income — The Deepest Bond Market

| Metric | Value | Source |
|--------|-------|--------|
| US Treasury ADV (2024) | $1,055B (first time >$1T) | [SIFMA](https://www.sifma.org/research/statistics/us-treasury-securities-statistics) |
| US Corporate Bond ADV | $57.9B (+11.5% YoY) | [SIFMA](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics) |
| TRACE annual trades (2024) | ~52M | [FINRA TRACE](https://www.finra.org/finra-data/fixed-income) |
| MSRB muni trades (2024) | 14.5M (record) | [MSRB](https://www.msrb.org/sites/default/files/2025-01/MSRB-2024-Municipal-Market-Year-in-Review.pdf) |
| MSRB muni trades (2025) | 17.6M (+22% YoY) | MSRB |
| US share of global fixed income trades | ~70.5% | Derived |
| US Treasury outstanding | $36T+ | US Treasury |
| Global bond outstanding | $145T | SIFMA |

The US Treasury market is the deepest, most liquid fixed income market in the world.
ADV crossed $1 trillion for the first time in 2024. The US accounts for approximately
**70%** of global cash bond trade count — TRACE (52M corporate/agency trades) and MSRB
(14.5M municipal trades) provide hard transaction count data that no other country matches.

Municipal bonds are a uniquely American phenomenon — the $4T muni market serves as the
primary funding mechanism for state and local government infrastructure. The 14.5M annual
MSRB trades make it one of the highest-confidence data points in fixed income.

---

### 10. OTC Derivatives — Major Dealer Banks

| Metric | Value | Source |
|--------|-------|--------|
| US share of ISDA-reported IRD trades | ~40-45% | [ISDA SwapsInfo](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/) |
| IRD Q4 2024 (US only) | 696,600 trades | ISDA |
| Major US dealer banks | JPMorgan, Goldman Sachs, Citigroup, Bank of America, Morgan Stanley | — |
| US share of global OTC derivatives notional | ~35-40% (est.) | BIS / Derived |

The US is home to 4 of the world's 5 largest OTC derivatives dealers (JPMorgan, Goldman
Sachs, Citigroup, Bank of America). ISDA SwapsInfo shows the US handling ~40-45% of
reported IRD trade counts. The OTC market is low-frequency (~0.15 TPS globally) but
massive in notional ($732T outstanding).

---

### 11. Digital Assets — Post-Regulation Clarity

| Metric | Value | Source |
|--------|-------|--------|
| Coinbase trading volume (2024) | ~$1T+ | [BusinessOfApps](https://www.businessofapps.com/data/coinbase-statistics/) |
| Kraken trading volume (2024) | $665B | [Daily Hodl](https://dailyhodl.com/2025/01/31/us-based-crypto-exchange-kraken-reports-huge-boosts-in-revenue-and-trading-volume-in-2024/) |
| US exchanges combined | ~$1.7T (est.) | Derived |
| US share of global CEX volume | ~4.9% (est.) | Derived ($1.7T / $77.3T adjusted) |
| CME crypto derivatives | Bitcoin ADV +56%, 19K contracts | CME Group |
| Stablecoins (USDC) | 70% of stablecoin transfer volume | [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report) |

The US crypto market is small by global CEX volume (~4.9%) because the major global
exchanges (Binance, Bybit, OKX) operate primarily outside US jurisdiction. However,
the US has outsized *structural* influence:

- **USDC** (Circle, US-regulated) accounts for 70% of stablecoin transfer volume
- **CME** is the world's largest regulated crypto derivatives venue
- **Coinbase** is the largest US exchange and a publicly traded company
- Post-2024 regulatory clarity (SEC/CFTC framework) is attracting institutional capital

The Ethereum ecosystem was largely US-originated, and US-based developers remain central
to DeFi protocol development.

---

### 12. Banking Infrastructure — Fedwire, CHIPS, FedNow

| Metric | Value | Source |
|--------|-------|--------|
| Fedwire (2024) | 209.9M txns, $1,133T | [FRB Services](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) |
| Fedwire avg transfer | $5.4M | FRB Services |
| Fedwire daily avg | 836,322 txns, $4.5T | FRB Services |
| CHIPS daily | ~500K txns, $1.8T | CHIPS |
| CHIPS annual (est.) | ~126M txns, ~$454T | Derived (252 business days) |
| FedNow (Jan-Aug 2024) | 414,827 txns total | [FRB Services](https://www.frbservices.org/resources/financial-services/fednow/quarterly-volume-value-stats) |
| FedNow participants | ~1,000 financial institutions | FRB Services |
| US share of global RTGS | ~50% (by value) | Derived |

Fedwire is the backbone of the US (and global) dollar settlement system. At $1,133T
annually, it processes more value than any other payment system on Earth. Combined with
CHIPS ($454T est.), the US RTGS complex handles over $1,587T — roughly **73%** of global
RTGS value across the 5 major systems.

**FedNow's challenge**: With just ~415K transactions in 8 months, FedNow is in its infancy.
For comparison, India's UPI processed 228B in 2025. The US real-time payments gap is the most
significant structural weakness in the world's largest economy's payment infrastructure. Same
Day ACH (1.4B transactions in 2025) is growing faster and may become the de facto US
real-time rail.

---

### 13. Government Payments — IRS, Social Security, Federal Payroll

| Metric | Value | Source |
|--------|-------|--------|
| IRS e-filed returns (FY2024) | 219.9M (all forms) | [IRS](https://www.irs.gov/newsroom/filing-season-statistics-by-year) |
| Individual returns (FY2024) | 161.1M total, 147.1M e-filed | IRS |
| E-file rate (2025 season) | ~96% | IRS |
| Social Security beneficiaries | 71.6M people | [SSA](https://www.ssa.gov/policy/docs/chartbooks/fast_facts/2024/fast_facts24.html) |
| OASDI benefits paid (CY2023) | $1,379B | SSA |
| SSI recipients | 7.4M people | SSA |
| Monthly SS disbursements | ~72M payments/month | Derived |
| Annual SS disbursements | ~864M payments/year | Derived |
| Federal civilian payroll | ~2.1M employees | OPM |
| Military payroll | ~1.3M active duty | DoD |
| Total US govt payment txns (est.) | ~6.0B/year | Composite |
| US share of global govt payments | ~24% (by value) | Derived |

The US government payment complex generates an estimated ~6B transactions annually:
- Social Security/SSI: ~864M monthly disbursements
- IRS refunds: ~111M refunds issued in FY2024
- IRS e-file submissions: ~220M
- Medicare/Medicaid payments: ~1.5B claims processed
- Federal/military payroll: ~86M paychecks/year
- State unemployment, SNAP, other benefits: ~2B+ (est.)

---

### 14. Payroll — ADP and the US Pay Cycle

| Metric | Value | Source |
|--------|-------|--------|
| US employed | 158.3M | BLS |
| Formal payroll workers | ~150M | Derived |
| Biweekly pay (70%) | 105M workers x 26 = 2.73B | — |
| Weekly pay (20%) | 30M workers x 52 = 1.56B | — |
| Monthly pay (10%) | 15M workers x 12 = 0.18B | — |
| Total US payroll transactions | ~3.4B/year | — |
| ADP coverage | 26M+ employees, 500K+ companies | [ADP](https://www.adp.com/) |
| US share of global payroll | 8.3% | Derived |

The US is unique among major economies in its biweekly pay cycle (70% of workers vs. monthly
in most of the world). This means US payroll generates ~2.2x more transactions per worker than
a monthly-pay country. ADP alone processes payroll for 26M+ employees — roughly 1 in 6 private
sector workers.

---

### 15. ATM Withdrawals — Declining but Significant

| Metric | Value | Source |
|--------|-------|--------|
| US ATM withdrawals (2024) | ~7.5B | BIS / ATM Industry Association |
| US ATMs | ~470,000 | ATMIA |
| YoY change | -6% | Derived |
| Avg withdrawal | $198 | Industry average |
| US share of global ATM txns | 15.3% | Derived |

US ATM withdrawals are declining at ~6% annually as card and digital payments substitute.
The US has ~470K ATMs — the most of any country — but usage per ATM is dropping. The average
US withdrawal ($198) is among the highest globally, reflecting infrequent but larger
cash-out events.

---

## The USD as Global Reserve Currency

The US dollar's role as the world's reserve currency inflates America's share across
several categories beyond what domestic activity alone would justify:

```
Category          USD Effect on US TPS Attribution
══════════════════════════════════════════════════════════
Forex             USD is one side of 88% of all FX trades
Fixed Income      US Treasuries are the global "risk-free" asset
OTC Derivatives   ~60% of IRD notional is USD-denominated
Interbank RTGS    Fedwire settles global dollar obligations
Stablecoins       USDC + USDT are 99%+ USD-pegged
Trade Finance     ~40% of global trade invoiced in USD
```

If we strip the reserve currency effect and count only *domestic* US economic activity,
the USA's estimated TPS drops from ~18,200 to roughly ~14,000-15,000 — still the world's
largest, but closer to its GDP weight.

---

## The Real-Time Payments Gap

The most striking structural weakness in US payments is the near-total absence of
real-time payments:

```
Country       RTP System    Annual Txns (2024)    Per Capita
═══════════════════════════════════════════════════════════════
Thailand      PromptPay     ~72B                  337/year
Brazil        PIX           ~63B                  307/year
India         UPI           172B                  123/year
UK            FPS           5.1B                  76/year
Australia     NPP           1.7B                  62/year
Nigeria       NIP           11.2B                 51/year
USA           FedNow        ~1.5M                 0.005/year
═══════════════════════════════════════════════════════════════
```

The US is 67,000x behind Thailand in per-capita real-time payments. This gap exists
because:
1. **Card dominance**: Cards are deeply embedded; there is no consumer pain point
2. **Bank incentives**: Banks earn interchange on cards; RTP cannibalizes that revenue
3. **Fragmented adoption**: FedNow requires bank-by-bank integration (only ~1,000 of 4,000+ banks)
4. **Same Day ACH fills the gap**: 1.4B transactions in 2025 at "good enough" speed
5. **No government mandate**: Unlike India (UPI), Brazil (PIX), or EU (SEPA Instant regulation)

---

## USA vs India — Structural Comparison

| Dimension | USA | India |
|-----------|-----|-------|
| **Payment model** | Card-centric (Visa/MC) | Bank-rail (UPI) |
| **Avg transaction value** | $63 (cards) | $17 (UPI) |
| **Merchant acceptance cost** | 2-3% interchange | 0% (UPI) |
| **Identity infrastructure** | SSN (fragmented) | Aadhaar (universal biometric) |
| **Real-time payments** | FedNow (~0 adoption) | UPI (228B txns/year) |
| **Capital markets** | Deepest in world (by value) | Largest by trade count |
| **ETD model** | Institutional, high-notional | Retail, high-frequency |
| **Wholesale settlement** | Fedwire $1,133T | RTGS Rs 1,938L cr |
| **Crypto regulatory stance** | Post-clarity (SEC/CFTC) | Punitive (30% tax + 1% TDS) |
| **TPS-to-GDP ratio** | 1.0x (proportional) | 5.0x (massively overweight) |

The fundamental insight: **the USA and India are complementary extremes**. The USA
processes the world's highest-value transactions at moderate frequency. India processes
the world's highest-frequency transactions at low value. Together, they illustrate why
TPS alone is an incomplete measure of financial activity — value per transaction matters.

---

## Risks and Vulnerabilities

### 1. Real-Time Payments Deficit
The US is the only major economy without meaningful real-time payment adoption. If FedNow
fails to gain traction, the US risks being left behind as the global payment standard
shifts to account-to-account instant transfers.

### 2. Card Interchange Dependency
The $187B merchant processing fee ecosystem creates powerful incumbency. Any regulatory
move (Durbin 2.0, credit card interchange caps) could disrupt both bank revenue and
card network economics.

### 3. Off-Exchange Equity Concentration
With 47% of equity volume trading off-exchange, price discovery increasingly happens in
dark pools rather than lit markets. SEC scrutiny is growing.

### 4. Treasury Market Fragility
The $36T+ Treasury market is systemically critical. The October 2023 basis trade volatility
and March 2020 Treasury market dysfunction showed that even the world's most liquid market
can seize under stress.

### 5. RTGS Single Point of Failure
Fedwire processes $4.5T/day. Any prolonged outage would cascade across global dollar
markets instantly.

---

## Key Takeaways

1. **The USA is 24.7% of global financial TPS on 25.5% of global GDP** — roughly
   proportional, unlike India's 5x overweight. This proportionality reflects the US
   pattern of fewer, larger transactions.

2. **The US is the world's #1 card market** with ~159B transactions (20.6% of global),
   generating ~5,040 TPS. Cards are the backbone of US consumer payments.

3. **US capital markets are the deepest in the world by value**: Treasury ADV >$1T,
   Fedwire $1,133T/year, CME 26.5M contracts/day. The US sets global benchmarks for
   rates, commodities, and equity pricing.

4. **The dollar's reserve currency status inflates US attribution** across FX (88%),
   fixed income, OTC derivatives, and stablecoins. Strip this effect and US domestic
   TPS is ~14,000-15,000.

5. **The real-time payments gap is the USA's biggest structural weakness**. FedNow
   at ~0.005 transactions per capita per year vs. Thailand's 337 and India's 123.
   The US is 67,000x behind the global leaders.

6. **USA + India together account for ~42% of global TPS** on ~29% of GDP. They
   represent opposite extremes: the US dominates value, India dominates volume.

---

## Sources

1. [Nilson Report — Global Network Card Results Worldwide 2024](https://nilsonreport.com/articles/global-network-card-results-worldwide-2024/)
2. [Payments Dive — US card market share 2024](https://www.paymentsdive.com/news/credit-card-us-market-payments-outpaced-by-other-world-regions/740595/)
3. [GlobeNewsWire / Nilson — US card spend exceeded $10T](https://www.globenewswire.com/news-release/2025/02/25/3032247/0/en/Amex-Discover-Mastercard-and-Visa-Card-Spending-Exceeded-10-Trillion-in-2024.html)
4. [Federal Reserve Payments Study (Nov 2024)](https://www.federalreserve.gov/paymentsystems/2024-November-The-Federal-Reserve-Payments-Study.htm)
5. [Nacha — ACH Network Volume and Value Statistics](https://www.nacha.org/content/ach-network-volume-and-value-statistics)
6. [Nacha — Top 50 ACH Originators 2025, Total Volume Exceeded 42B](https://www.nacha.org/news/nachas-top-50-ach-originators-and-receivers-2025-now-available-total-ach-payment-volume-2025)
7. [Nacha — Same Day ACH and B2B Growth 2025](https://www.nacha.org/news/same-day-ach-and-business-business-payments-propel-ach-network-volume-growth-2025)
8. [FRB Services — Fedwire Annual Statistics](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html)
9. [FRB Services — FedNow Quarterly Statistics](https://www.frbservices.org/resources/financial-services/fednow/quarterly-volume-value-stats)
10. [CME Group — Record 2024 ADV of 26.5M Contracts](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html)
11. [Cboe — Full Year 2024 Trading Volume](https://ir.cboe.com/news/news-details/2025/Cboe-Global-Markets-Reports-Trading-Volume-for-December-and-Full-Year-2024/default.aspx)
12. [ICE — Record 2B Contracts in 2024](https://ir.theice.com/press/news-details/2025/ICE-Announces-That-a-Record-2-Billion-Contracts-Traded-in-2024/default.aspx)
13. [BIS Triennial FX Survey 2025](https://www.bis.org/statistics/rpfx25_fx.htm)
14. [SIFMA — US Treasury Securities Statistics](https://www.sifma.org/research/statistics/us-treasury-securities-statistics)
15. [SIFMA — US Corporate Bonds Statistics](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics)
16. [FINRA — TRACE Fixed Income Data](https://www.finra.org/finra-data/fixed-income)
17. [MSRB — 2024 Municipal Market Year in Review](https://www.msrb.org/sites/default/files/2025-01/MSRB-2024-Municipal-Market-Year-in-Review.pdf)
18. [ISDA SwapsInfo — Full Year 2024](https://www.isda.org/2025/02/20/swapsinfo-full-year-2024-and-the-fourth-quarter-of-2024/)
19. [CNBC — Zelle Payments Top $1 Trillion in 2024](https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html)
20. [IRS — Filing Season Statistics by Year](https://www.irs.gov/newsroom/filing-season-statistics-by-year)
21. [SSA — Fast Facts & Figures About Social Security 2024](https://www.ssa.gov/policy/docs/chartbooks/fast_facts/2024/fast_facts24.html)
22. [Nasdaq — Top Trading Trends 2024](https://www.nasdaq.com/articles/top-trading-trends-2024)
23. [NYSE — US Equity Daily Volumes](https://www.nyse.com/trade/us-equity-volumes)
24. [WFE — FY 2024 Market Highlights](https://www.world-exchanges.org/our-work/articles/wfe-market-highlights-fy-2024)
25. [BusinessOfApps — Coinbase Statistics](https://www.businessofapps.com/data/coinbase-statistics/)
26. [Daily Hodl — Kraken 2024 Revenue and Volume](https://dailyhodl.com/2025/01/31/us-based-crypto-exchange-kraken-reports-huge-boosts-in-revenue-and-trading-volume-in-2024/)
27. [Nilson Report — Merchant Processing Fees US 2024](https://nilsonreport.com/articles/merchant-processing-fees-in-the-united-states-2024/)
28. [CLS Group — 2024 Annual Report](https://www.cls-group.com/about/annual-report-2024/)
29. [ADP — Payroll Data and Employment Report](https://www.adp.com/)
30. [PYMNTS — B2B ACH Volume +9.9% in 2025](https://www.pymnts.com/news/b2b-payments/2026/b2b-volume-on-ach-network-increased-9-9-in-2025/)

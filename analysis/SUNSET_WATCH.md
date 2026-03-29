---
title: "Sunset Watch"
---

# Universe of Finance — Sunset Watch

> Tracking financial transaction categories and subcategories in structural
> decline. These are the slow deaths of the financial system — transactions
> types being displaced by digital alternatives, regulatory changes, or
> technological obsolescence.
>
> **Last Updated**: 2026-03-28

---

## The Sunset Timeline

```
Category               2024 Volume    CAGR     Projected     Year Hits
                       (annual)                Negligibility  <1% of Peak
═══════════════════════════════════════════════════════════════════════════
ATM Withdrawals        49.1B txns     -3.5%    ~2055-2060    ~2090+
Cheque/Check Payments  ~5.5B txns     -7.0%    ~2035-2038    ~2045
Cash-on-Delivery       ~3.0B txns     -8.0%    ~2032-2035    ~2040
SWIFT MT Messages      ~4.5B msgs     -40%*    ~2026 (cutoff) Nov 2025**
Physical Trading Floors ~0.5B txns    -12%     ~2030-2032    ~2038
Traveler's Cheques     ~0.01B txns    -15%     ~2028         Already <1%
═══════════════════════════════════════════════════════════════════════════
* SWIFT MT decline is a forced migration, not organic decline
** MT messages officially discontinued November 22, 2025
```

### Decline Trajectory (ASCII Chart)

```
Volume (indexed to peak = 100)

100 |*                                           Peak
 90 | *.                                         .
 80 |  *..                                       . ATM Withdrawals
 70 |    *...                                    .   (slow fade)
 60 |      *....                                 .
 50 |         *......                            .
 40 |              *.........                    .
 30 |                    *..............         .
 20 |                              *..........  .
 10 |                                        *...
  0 |____________________________________________*___
    2016  2020  2025  2030  2035  2040  2045  2050


100 |*                                           Peak
 90 | *                                          .
 80 |  *                                         . Cheque Payments
 70 |   **                                       .   (steep decline)
 60 |     **                                     .
 50 |       ***                                  .
 40 |          ***                               .
 30 |             ****                           .
 20 |                 *****                      .
 10 |                      *******               .
  0 |_____________________________***************____
    2015  2020  2025  2030  2035  2040  2045


100 |*
 90 | .                                          SWIFT MT Messages
 80 | .                                            (cliff event)
 70 | .
 60 | .
 50 | .
 40 |  .
 30 |   .
 20 |    ..
 10 |      ...
  0 |_________*  ← Nov 22, 2025: mandatory cutover
    2023  2024  2025  2026
```

---

## Category 1: ATM Withdrawals

**Status: Confirmed declining | Captured in taxonomy | -3.0 to -3.5% CAGR**

See [payments/atm-withdrawals/REPORT.md](payments/atm-withdrawals/REPORT.md) for
full analysis.

### Trajectory

| Metric | Value |
|--------|-------|
| Peak | ~63B transactions (2016-2017) |
| Current (2024) | ~49.1B transactions |
| Decline from peak | -22% over 8 years |
| CAGR (2016-2024) | -3.0% |
| Pre-COVID trend CAGR | -3.3% |

### What's Replacing It

- **Digital wallets** (Alipay, WeChat Pay, UPI, PIX) — direct cash replacement
- **Contactless card payments** — reduced need for cash in developed markets
- **Real-time payments** (FedNow, Faster Payments, UPI) — P2P transfers replace
  cash for splitting bills, small payments
- **CBDCs** (e-CNY, potential others) — digital cash by central banks

### Regional Variation

```
Region            2024 CAGR    Trajectory
──────────────── ──────────── ──────────────────────────────
China              -8%         Fastest decline (Alipay/WeChat)
US                 -6%         Accelerating since COVID
UK                 -6%         Contactless dominance
EU                 -4%         Varies by country (Germany sticky)
Japan              -3%         Cash culture resilient
Africa             +5%         STILL GROWING (financial inclusion)
Latin America      -2%         Moderate decline, cash still important
India              -5%         UPI displacing cash rapidly
```

### Negligibility Estimate

ATM withdrawals are declining but persistent. Even at -4% CAGR:
- **2030**: ~38B transactions (still massive)
- **2040**: ~25B transactions
- **2050**: ~17B transactions
- Hits <1% of peak (~630M): **Never in our lifetime** — cash infrastructure
  will persist in some form well beyond 2060

### Impact on the Big Number

- Current contribution: **~1,557 TPS** (de-duplicated, zero overlap)
- At -4% CAGR: loses ~62 TPS per year
- By 2030: ~1,218 TPS
- By 2040: ~820 TPS
- Net impact: **-340 TPS by 2030** (modest — other categories grow faster)

---

## Category 2: Cheque/Check Payments

**Status: Steep decline | NOT explicitly captured in taxonomy | Hidden in Bank Transfers**

### Trajectory

| Metric | Value |
|--------|-------|
| Peak (US) | ~42B checks (2000) |
| Current US (2024) | ~3.0B checks (Federal Reserve processed) |
| Current UK (2024) | ~253M cheques (~135M consumer + ~118M business) |
| Global estimate (2024) | ~5.5B checks/cheques |
| Decline rate (US, 10yr) | -6.3% CAGR (Fed: -50% over decade) |
| Decline rate (UK) | -8% CAGR |

### Key Data Points

- **US Federal Reserve**: In 2024, Reserve Banks processed nearly **3.0 billion
  commercial checks** — nearly 50% less than 5.7 billion a decade ago. Volume
  declined >6% annually on average. [Source: [Federal Register](https://www.federalregister.gov/documents/2025/12/09/2025-22272/request-for-information-and-comment-on-the-future-of-the-federal-reserve-banks-check-services)]
- **US consumers**: Only **7% of consumers** paid by check in 2024, down from 19%
  in 2020. [Source: [Federal Reserve Bank of Atlanta](https://www.empower.com/the-currency/money/fed-takes-closer-look-check-services-news)]
- **US businesses**: Check volumes fell from 59% of business payments (2024) to
  below 50% (2025). **77% of businesses** still using checks plan to go fully
  digital within 1-3 years. [Source: [Citizens Bank](https://www.citizensbank.com/corporate-finance/insights/end-of-paper-checks.aspx)]
- **UK**: Cheque payments declined from 2.8% of non-cash transactions (2014) to
  0.8% (2024). [Source: [UK Finance](https://www.ukfinance.org.uk/system/files/2024-07/Summary%20UK%20Payment%20Markets%202024.pdf)]
- **Fed action**: In December 2025, the Federal Reserve issued a Request for
  Information on the future of its check services, signaling possible service
  reduction. [Source: [Payments Dive](https://www.paymentsdive.com/news/fed-proposes-reduced-check-services/807294/)]

### What's Replacing It

- **ACH/BACS direct debit** — for recurring bill payments
- **Real-time payments** (FedNow, Faster Payments) — for one-off transfers
- **Digital invoicing and AP automation** — for B2B payments
- **Zelle/Venmo** — for personal payments that once used checks

### Where It Lives in Our Taxonomy

Checks are **not a standalone category** — they are hidden within:
- **Bank Transfers** (ACH/BACS subcategory) — checks clear through the same
  clearing houses
- **Bill Payments** — many check payments are bill payments
- **Payroll** — some payroll still uses checks (declining rapidly)

This means check decline does not directly reduce any single TPS category but
contributes to the gradual shift within bank transfers from paper to electronic.

### Negligibility Estimate

```
US check trajectory at -7% CAGR:
  2024: ~3.0B
  2028: ~2.2B
  2030: ~1.9B
  2035: ~1.3B
  2040: ~0.9B
  Hits <1% of peak (420M): ~2038-2040

Global estimate:
  2024: ~5.5B
  2030: ~3.5B
  2035: ~2.3B
  Negligibility (<500M): ~2040-2045
```

### Impact on the Big Number

- Checks are already counted within bank transfers (~484B annual)
- At ~5.5B checks globally, they represent **~1.1% of bank transfers**
- Their decline is offset by ACH/real-time payment growth
- **Net impact on Big Number: Zero** — the transactions migrate from checks to
  electronic, staying in the same category

---

## Category 3: Cash-on-Delivery (COD)

**Status: Declining in most markets | NOT explicitly captured | Hidden in E-Commerce and Payments**

### Trajectory

| Metric | Value |
|--------|-------|
| Global COD share of e-commerce (2020) | ~15-20% |
| Global COD share of e-commerce (2024) | ~8-10% |
| Estimated global COD transactions (2024) | ~3.0B |
| Decline rate | -8% CAGR (as digital payments displace) |

### Key Data Points

- Traditional payment methods (cards + COD) projected to account for **<33% of
  global e-commerce** transaction value by 2025. [Source: [FIS / Worldpay](https://www.fisglobal.com/about-us/media-room/press-release/2022/global-e-commerce-market-projected-to-grow-55-percent-by-2025-fis-study-finds)]
- Digital payments now account for **54% of all global payments** (2025).
- **Food delivery COD** specifically generated $93.3B revenue in 2024, but this is
  a value figure, not a transaction count. Asia Pacific dominates COD in food
  delivery. [Source: [Grand View Research](https://www.grandviewresearch.com/horizon/statistics/online-food-delivery-market/payment-method/cash-on-delivery/global)]

### Regional Variation

```
Region            COD Share    Trend
──────────────── ──────────── ──────────────────────────────
India              30-40%      Declining rapidly (UPI)
Southeast Asia     25-35%      Declining (GrabPay, ShopeePay)
Middle East        20-30%      Declining (local wallets)
Africa             40-50%      Persistent (low card penetration)
Europe             <5%         Already negligible
US                 <2%         Essentially zero
China              <3%         Nearly eliminated (Alipay/WeChat)
Latin America      10-15%      Declining (PIX, Mercado Pago)
```

### What's Replacing It

- **Digital wallets** (UPI, GrabPay, ShopeePay, M-Pesa)
- **BNPL** (Klarna, Afterpay equivalents in each market)
- **Mobile money** (M-Pesa, MTN MoMo) — particularly in Africa
- **Cash-on-pickup** → **digital payment at pickup** hybrid models

### Where It Lives in Our Taxonomy

COD is split across:
- **E-Commerce** (the commerce event)
- **No payment category** (the cash exchange at delivery is untracked — like
  ATM-withdrawn cash being spent)

COD actually creates a **gap** in our taxonomy: the commerce event is counted in
e-commerce, but the payment event (cash handover) is not captured in any
electronic payment category. As COD declines, those transactions migrate TO
cards/wallets/bank transfers, which INCREASES electronic payment TPS.

### Negligibility Estimate

```
Global COD transactions at -8% CAGR:
  2024: ~3.0B
  2028: ~2.2B
  2030: ~1.7B
  2035: ~0.9B
  Negligibility (<300M): ~2038-2040
```

### Impact on the Big Number

- COD decline actually **INCREASES** the Big Number over time because cash
  payments migrate to electronic rails
- Estimated migration: ~200M transactions/year shift from untracked cash to
  tracked electronic payments
- **Net impact: +6 TPS/year** as COD converts to digital (small but positive)

---

## Category 4: SWIFT MT Messages

**Status: Forced migration (NOT organic decline) | Deadline: November 22, 2025**

### Trajectory

| Metric | Value |
|--------|-------|
| Annual SWIFT messages (all types, 2024) | ~12.7B |
| In-scope MT payment messages | ~4.5B |
| Migration deadline | November 22, 2025 |
| Post-deadline MT volume | ~0 (mandatory cutover) |
| Replacement: MX (ISO 20022) messages | 1:1 replacement |

### Key Data Points

- **March 20, 2023**: Official start of the industry-wide transition from MT to
  MX messaging (ISO 20022 / CBPR+ schema).
  [Source: [J.P. Morgan](https://www.jpmorgan.com/insights/payments/fx-cross-border/iso-20022-migration)]
- **November 22, 2025**: End of "coexistence" period. All cross-border payments
  must use MX format exclusively. MT payment and cash messages retired.
  [Source: [Swift](https://www.swift.com/standards/iso-20022/iso-20022-financial-institutions-focus-payments-instructions)]
- **87% of high-value payment systems** migrated to ISO 20022 by end of 2025.
  [Source: [BNY](https://www.bny.com/assets/corporate/documents/pdf/iso-20022-end-of-co-existence_-may-2025-final.pdf)]
- Co-existence allowed both MT and MX from March 2023 to November 2025.

### What's Replacing It

- **MX messages (ISO 20022)** — direct 1:1 replacement with richer data fields
- Same SWIFT network, same transaction volumes, different message format
- Key benefit: structured data enables better compliance, richer remittance info

### Where It Lives in Our Taxonomy

SWIFT messages are counted within **Bank Transfers** (specifically the "SWIFT
messages" subcategory under 2.3). This is a **format migration, not a volume
decline**. The same cross-border payments continue to flow — just in a new
message format.

### Negligibility Estimate

```
MT message volume:
  2023: ~4.5B (pre-migration)
  2024: ~3.0B (coexistence period)
  2025 (Nov): ~0 (mandatory cutoff)
  2026+: 0

MX message volume:
  2023: ~0.5B
  2024: ~1.5B
  2025 (Nov): ~4.5B (absorbed all MT)
  2026+: Growing with cross-border payment growth
```

### Impact on the Big Number

- **Net impact: ZERO.** This is a format migration, not a volume change.
- Every MT message that disappears is replaced by an MX message.
- The number of cross-border payment transactions is unchanged.
- However, ISO 20022 may enable new transaction types (richer data,
  more granular reporting) that could slightly increase message counts
  over time.

---

## Category 5: Physical Trading Floors

**Status: Near-obsolete | Declining since ~2000 | Captured implicitly in Equity/ETD**

### Trajectory

| Metric | Value |
|--------|-------|
| Peak floor trading share (1990s) | ~80-90% of volume |
| Current floor trading share (2024) | ~2-5% of total volume |
| Electronic trading share (2024) | ~95-98% |
| Algorithmic execution (US equities, 2023) | 44% of buy-side flow |
| Remaining physical floors | NYSE, CME (limited), CBOE, a few options exchanges |

### Key Data Points

- Electronic platforms captured **44% of buy-side US equity order flow** in 2023,
  up from 42% in 2022. Algorithmic trading: **37% of volume** (up from 35%).
  [Source: [Coalition Greenwich](https://www.greenwich.com/press-release/electronic-platforms-capture-growing-share-us-equity-trading-volume)]
- **NYSE** operates a hybrid model — floor brokers handle ~2-3% of total NYSE
  volume, primarily for opening/closing auctions and large blocks.
- In March 2020, NYSE temporarily closed its floor entirely and went all-electronic
  — markets functioned normally, proving floor is non-essential.
  [Source: [TechCrunch](https://techcrunch.com/2020/03/18/nyse-will-temporarily-close-its-trading-floor-and-move-to-electronic-trading-only/)]
- Interestingly, **MIAX Sapphire** opened a NEW options trading floor in September
  2025 — a rare counter-trend driven by regulatory advantages for floor-based
  options market-making.
- Academic research (2025) found floor brokers "skew stock market prices" —
  questioning their continued role.
  [Source: [UVA Law](https://www.law.virginia.edu/news/202511/professor-finds-floor-brokers-skew-stock-market-prices)]

### What's Replacing It

- **Electronic matching engines** (NYSE Arca, NASDAQ, CME Globex)
- **Algorithmic trading / smart order routing**
- **Dark pools and ATS** (Alternative Trading Systems)
- **DMA (Direct Market Access)** for institutional traders

### Where It Lives in Our Taxonomy

Physical floor trades are counted within:
- **Equity Markets** (stock trades, regardless of execution venue)
- **Exchange-Traded Derivatives** (futures/options floor vs screen)

The transaction happens whether it's executed on a floor or electronically —
the taxonomy counts the trade, not the venue.

### Negligibility Estimate

```
Floor trading share of total equity/ETD volume:
  2000: ~80%
  2010: ~20%
  2020: ~5%
  2024: ~2-3%
  2028: ~1-2% (residual for auctions, large blocks)
  2030: ~0.5-1%
  Hits <1% of its historical self: ~2028-2032
```

### Impact on the Big Number

- **Net impact: ZERO.** Floor trading is a venue, not a transaction type.
- Whether a trade executes on a floor or electronically, it is one trade.
- Floor closure shifts execution venue, not transaction count.
- If anything, electronic trading enables MORE transactions (smaller tick sizes,
  higher frequency) so the migration is slightly ADDITIVE.

---

## Category 6: Traveler's Cheques

**Status: Effectively dead | NOT in taxonomy | Negligible volume**

### Trajectory

| Metric | Value |
|--------|-------|
| Peak (1990s) | ~$50B value, ~200M transactions |
| Current (2024) | ~$1-2B value, ~10M transactions |
| Decline rate | -15% CAGR (accelerating) |
| Already <1% of peak? | **Yes — since ~2018** |

### What Killed It

- International debit/credit cards with no foreign transaction fees
- Currency exchange apps (Wise, Revolut, Xe)
- ATM networks worldwide accepting international cards
- Mobile wallets accepted globally (Apple Pay, Google Pay)
- American Express discontinued traveler's cheques in 2020

### Where It Lives in Our Taxonomy

Nowhere. Traveler's cheques are too small to warrant a subcategory. At ~10M
transactions annually, they represent **~0.3 TPS** — statistical noise.

### Impact on the Big Number

- **Net impact: ZERO.** Already negligible. Not worth tracking.

---

## The Sunset Honor Roll (Emerging Declines to Watch)

These subcategories are not yet in confirmed decline but show early warning signs:

### Fax-Based Trade Confirmations
- Still used in OTC derivatives for trade confirms
- Being displaced by electronic matching (MarkitWire, TradeWeb)
- Current volume: Unknown but probably <100M annual
- Expected obsolescence: 2028-2030

### Physical Commodity Delivery Tickets
- Paper-based delivery notices for physical commodity settlement
- Being digitized by commodity exchanges globally
- Current volume: Unknown, very small
- Expected obsolescence: 2030-2035

### Manual Wire Transfer Requests
- Walk-in bank wire transfers with paper forms
- Being displaced by online banking wire initiation
- Still common in some developing markets
- Declining at estimated -5% CAGR

### Magnetic Stripe Card Transactions
- EMV chip has replaced mag stripe in most markets
- US was the last major market to migrate (~2015-2020)
- Some markets still use mag stripe for ATMs
- Expected negligibility: 2028-2030 for in-store, 2035 for ATMs

### Money Orders
- US Postal Service and Western Union money orders
- Being displaced by digital payment apps
- ~$25B value annually in US, declining ~5% per year
- Still relevant for unbanked populations

---

## Aggregate Impact on the Big Number

### What Declines Mean for the Total

```
Category              2024 TPS    2030 TPS    Change    Net Impact
                      (current)   (projected)
──────────────────── ──────────── ────────── ────────── ──────────
ATM Withdrawals       1,557       1,218       -339      -339 TPS
Checks (in bank xfr)  174         110         -64       0 (stays in bank xfr)
COD (to digital)       95          53         -42       +42 TPS (migrates to digital)
SWIFT MT → MX        ~143          0         -143       0 (format change only)
Physical floors       ~75          30         -45       0 (venue change only)
Traveler's cheques     0.3         0.1        -0.2      0
──────────────────── ──────────── ────────── ────────── ──────────
TOTAL IMPACT                                            -297 TPS by 2030
```

### The Sunset Paradox

Most "declining" categories have **zero net impact** on the Big Number because:

1. **Format migrations** (SWIFT MT→MX): Same transactions, new format
2. **Venue migrations** (floor→electronic): Same trades, new venue
3. **Rail migrations** (checks→ACH, COD→digital): Same economic events, new
   payment rail — and often MORE transaction events on the new rail

**ATM withdrawals are the ONLY truly declining transaction type** — where the
decline represents a genuine reduction in financial transaction events. Every
other "decline" is actually a migration that preserves or increases total TPS.

### The Real Story

```
Gross decline in sunset categories (2024→2030):     ~-630 TPS
Offset by format/venue/rail migrations:             ~+333 TPS
                                                    ──────────
Net decline:                                        ~-297 TPS

Meanwhile, growing categories add:
  Digital wallets:  +3,490 TPS (2024→2030 at baseline)
  Consumer cards:   +4,738 TPS
  Bank transfers:   +2,000 TPS (estimated)
  ETD:              +1,000 TPS (estimated)
                    ──────────
Net growth:         +11,228 TPS

Ratio: Growth outpaces decline by ~38:1
```

The sunset categories are a footnote. The Big Number is driven entirely by
growth in digital payments, card adoption, and derivatives trading. Even if
every declining category hit zero tomorrow, the Big Number would barely notice.

---

## Methodology Notes

- **CAGR calculations** use the standard compound annual growth rate formula:
  (End/Start)^(1/Years) - 1
- **Negligibility** is defined as <1% of historical peak volume
- **"Hidden in"** categories refer to transactions that are counted within a
  parent category in our taxonomy but are identifiable as a distinct declining
  subcategory
- **Net impact** accounts for migration effects: if a declining format is replaced
  1:1 by a new format, the net impact on total TPS is zero
- Transaction counts for checks and COD are estimates with low confidence
  (no single authoritative global source)

---

## Sources

1. [Federal Register — Future of Federal Reserve Check Services (Dec 2025)](https://www.federalregister.gov/documents/2025/12/09/2025-22272/request-for-information-and-comment-on-the-future-of-the-federal-reserve-banks-check-services)
2. [Payments Dive — Fed proposes reduced check services](https://www.paymentsdive.com/news/fed-proposes-reduced-check-services/807294/)
3. [Citizens Bank — Declining Paper Checks](https://www.citizensbank.com/corporate-finance/insights/end-of-paper-checks.aspx)
4. [Vixio — A Sharp Decline: Cheque Usage in Britain](https://www.vixio.com/insights/pc-sharp-decline-cheque-usage-britain)
5. [UK Finance — UK Payment Markets Summary 2024](https://www.ukfinance.org.uk/system/files/2024-07/Summary%20UK%20Payment%20Markets%202024.pdf)
6. [J.P. Morgan — ISO 20022 Migration](https://www.jpmorgan.com/insights/payments/fx-cross-border/iso-20022-migration)
7. [Swift — ISO 20022 for Financial Institutions](https://www.swift.com/standards/iso-20022/iso-20022-financial-institutions-focus-payments-instructions)
8. [BNY — ISO 20022 End of Co-Existence (May 2025)](https://www.bny.com/assets/corporate/documents/pdf/iso-20022-end-of-co-existence_-may-2025-final.pdf)
9. [Coalition Greenwich — Electronic Platforms Capture Growing Share of US Equity Trading](https://www.greenwich.com/press-release/electronic-platforms-capture-growing-share-us-equity-trading-volume)
10. [TechCrunch — NYSE Temporarily Closes Trading Floor (March 2020)](https://techcrunch.com/2020/03/18/nyse-will-temporarily-close-its-trading-floor-and-move-to-electronic-trading-only/)
11. [CoinLaw — ATM Usage Decline Statistics 2025](https://coinlaw.io/atm-usage-decline-statistics/)
12. [CoinLaw — Cashless Society Adoption Statistics 2025](https://coinlaw.io/cashless-society-adoption-statistics/)
13. [OECD — Safeguarding Consumers' Access to Cash (March 2025)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/safeguarding-consumers-access-to-cash-in-the-digital-economy_d6048c25/189970b4-en.pdf)
14. [FIS / Worldpay — Global E-Commerce Report](https://www.fisglobal.com/about-us/media-room/press-release/2022/global-e-commerce-market-projected-to-grow-55-percent-by-2025-fis-study-finds)
15. [Grand View Research — Cash on Delivery in Online Food Delivery](https://www.grandviewresearch.com/horizon/statistics/online-food-delivery-market/payment-method/cash-on-delivery/global)
16. [UVA Law — Floor Brokers Skew Stock Market Prices (2025)](https://www.law.virginia.edu/news/202511/professor-finds-floor-brokers-skew-stock-market-prices)

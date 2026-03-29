---
title: "TTR Valuation"
parent: "Total Tokenizable Resources"
layout: default
nav_order: 1
---

# TTR Valuation: The Total Addressable Market for Tokenization

> Every asset on Earth that can be represented as a digital token has a value.
> The sum of those values — the Total Tokenizable Resources (TTR) — is the
> ceiling for the tokenization revolution. This document estimates that ceiling.

*A standalone analysis from the Universe of Finance project. March 2026.*

---

## 1. The Headline Number

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   TOTAL TOKENIZABLE RESOURCES (TTR)                                  ║
║   ═════════════════════════════════                                   ║
║                                                                      ║
║   Conservative (tangible + financial):     ~$890 TRILLION             ║
║   Broad (including rights & intangibles):  ~$980 TRILLION             ║
║   Maximum (including derivatives notional): ~$1.6 QUADRILLION         ║
║                                                                      ║
║   Current RWA tokenization (on-chain):     ~$20 BILLION               ║
║   Tokenization penetration:                ~0.002%                    ║
║                                                                      ║
║   The gap between what IS tokenized and what COULD be tokenized       ║
║   is five orders of magnitude.                                        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

The three-tier estimate reflects a genuine measurement choice. Derivatives
notional value ($630T) represents contractual exposure, not underlying assets
— including it nearly doubles the number. We present all three because
different use cases warrant different denominators. A stablecoin project
cares about the conservative figure; a DeFi protocol building perpetual
futures cares about the maximum.

---

## 2. Financial Assets (~$495 Trillion)

The most liquid and immediately tokenizable category. Much of this already
exists in digital form — the "tokenization" is re-platforming from closed
ledgers to programmable, composable, globally accessible ones.

### 2.1 Detailed Breakdown

| Asset Class | Estimated Value | Primary Source | Confidence |
|-------------|---------------:|----------------|:----------:|
| Global M2 money supply | $105.0T | IMF IFS database, central bank aggregates (2024) | High |
| Global equity market cap | $115.0T | WFE Annual Statistics (Dec 2024) | High |
| Global bond market (outstanding) | $130.0T | ICMA/BIS Quarterly Review (Q3 2024) | High |
| Derivatives (notional outstanding) | $632.0T | BIS OTC Derivatives Statistics (H1 2024) | High |
| Bank deposits (global) | $82.0T | BIS banking statistics, central bank data | Medium |
| Insurance industry assets (AUM) | $40.0T | Swiss Re sigma, OECD Global Insurance Stats | Medium |
| Pension fund assets | $56.0T | OECD Pension Markets in Focus (2024) | Medium |
| Sovereign wealth fund assets | $12.0T | SWF Institute Global Rankings (2024) | Medium |
| Private equity & VC (AUM) | $14.0T | Preqin Global Alternatives Report (2024) | Medium |
| Hedge fund assets | $4.5T | HFR Global Hedge Fund Report (2024) | Medium |
| **Subtotal (excl. derivatives)** | **$558.5T** | | |
| **Subtotal (incl. derivatives)** | **$1,190.5T** | | |

**Why derivatives get their own line.** The $632T in derivatives notional
is not additive to the equity and bond markets — it is *derived* from them.
A $100M interest rate swap does not represent $100M of new value; it
represents exposure to the movement of $100M in underlying bonds. Including
derivatives in the TTR is defensible if you are measuring "total contractual
value that could live on a programmable ledger" but misleading if you are
measuring "total underlying wealth."

We use **$495T** as the financial assets subtotal throughout this document:
$558.5T minus derivatives, minus ~$63T in double-counting between M2 and
bank deposits (deposits are a component of M2).

### 2.2 What "Tokenized" Means for Each

| Asset Class | Current State | Tokenized State | MEST Impact |
|-------------|--------------|-----------------|-------------|
| M2 / Cash | Central bank digital ledgers, commercial bank entries | Stablecoins (USDC, USDT) or CBDCs | 7 MESTs to 2 (see MEST Advantage) |
| Equities | CSD-held, broker-intermediated, T+1 settlement | Security tokens with atomic DvP | 10 MESTs to 2 |
| Bonds | OTC-dominant, bilateral clearing, T+2 | On-chain fixed income (Franklin Templeton FOBXX) | 8 MESTs to 2-3 |
| Deposits | Siloed bank ledgers, slow interbank transfer | Tokenized deposits (JPM Onyx, Partior) | 5 MESTs to 2 |
| Insurance | Paper-heavy, slow claims, no secondary market | Parametric smart contracts, tradeable policies | 6 MESTs to 2-3 |
| Pension/SWF | Illiquid, long lock-up, opaque fees | Fractional tokenized fund units | 5 MESTs to 2 |
| Private equity | Illiquid, high minimums, no price discovery | Fractional tokens, secondary DEX trading | 5 MESTs to 2-3 |

---

## 3. Real Assets (~$510 Trillion)

Physical assets are harder to tokenize than financial ones — you need a
legal framework connecting the token to the physical thing. But the total
value dwarfs financial markets.

### 3.1 Detailed Breakdown

| Asset Class | Estimated Value | Primary Source | Confidence |
|-------------|---------------:|----------------|:----------:|
| Global real estate | $380.0T | Savills Global Real Estate Report (2024) | High |
| Agricultural land | $30.0T | FAO/World Bank, Savills farmland index | Medium |
| Infrastructure (built) | $50.0T | McKinsey Global Infrastructure Outlook, G20 GIH | Low-Med |
| Gold (above-ground) | $15.8T | World Gold Council (212,582 tonnes at ~$2,400/oz, mid-2025) | High |
| Other precious metals | $1.2T | Silver Institute, Johnson Matthey PGM reports | Medium |
| Vehicles in operation | $16.5T | OICA (~1.5B vehicles, avg ~$11,000 depreciated value) | Low |
| Art & collectibles | $2.0T | Deloitte Art & Finance Report (2024) | Low |
| Commodities in storage/transit | $8.0T | IEA (oil/gas), USDA (grains), LME (metals) | Low |
| Timber & forestry assets | $4.0T | FAO Global Forest Resources Assessment | Low |
| **Subtotal** | **~$507.5T** | | |

### 3.2 The Real Estate Dominance

Real estate alone is **$380 trillion** — larger than all global equity and
bond markets combined. This single category accounts for ~40% of the entire
TTR (conservative basis).

```
    Composition of Global Real Estate ($380T)
    ══════════════════════════════════════════

    Residential       ████████████████████████████████████   $260T  (68%)
    Commercial        ██████████████                         $70T   (18%)
    Agricultural      █████                                  $30T   (8%)
    Industrial        ████                                   $20T   (5%)

    Of $380T total:
    - OECD countries: ~$280T (74%)
    - China:          ~$60T  (16%)
    - Rest of world:  ~$40T  (10%)
```

Real estate is also the category with the widest gap between tokenizability
and actual tokenization. The reasons are structural:

1. **Legal heterogeneity.** Property law is jurisdictional. A tokenized deed
   in Wyoming means nothing in France. There is no global property standard.
2. **Custody problem.** Financial tokens are self-custodied. Real estate
   tokens need a legal entity (SPV, trust, DAO) to hold the physical asset.
3. **Illiquidity is a feature.** Homeowners do not want their house to be
   traded on a 24/7 market. Price stability matters for shelter.
4. **Title systems.** Only ~30% of the world's land is formally registered
   (World Bank). You cannot tokenize what you cannot prove ownership of.

### 3.3 Vehicles: A Surprising Category

The world has approximately **1.47 billion vehicles** in operation (OICA 2024).
At an average depreciated value of ~$11,000 per vehicle, that is ~$16.5T in
mobile assets — larger than all above-ground gold.

Vehicle tokenization is already emerging:
- **Vehicle history tokens** (Carfax-on-chain concepts)
- **Fleet financing** (tokenized vehicle portfolios as ABS)
- **Autonomous vehicle revenue sharing** (fractional ownership of self-driving fleets)

---

## 4. Rights & Claims (~$85 Trillion)

This category is the most speculative and the most transformative. These are
assets that are hard to trade today because they lack standardized
representations — exactly the problem tokenization solves.

### 4.1 Detailed Breakdown

| Asset Class | Estimated Value | Primary Source | Confidence |
|-------------|---------------:|----------------|:----------:|
| Intellectual property (global) | $65.0T | Ocean Tomo Intangible Asset Study (S&P 500 alone = $21T; global extrapolation) | Low |
| Carbon credit market (projected 2030) | $1.0T | BloombergNEF, TSVCM projections | Low |
| Spectrum licenses (cumulative allocated) | $3.0T | ITU/FCC auction data, GSMA extrapolation | Low |
| Water rights | $3.0T | WRI Aqueduct, OECD water pricing studies | Low |
| Mining & mineral rights | $8.0T | S&P Global Market Intelligence, USGS | Low-Med |
| Insurance policies (as tradeable assets) | $5.0T | Life settlement market extrapolation (LISA, Conning) | Low |
| **Subtotal** | **~$85.0T** | | |

### 4.2 Intellectual Property: The Sleeping Giant

Global IP is valued at roughly **$65 trillion** — but this number is deeply
uncertain. Ocean Tomo's analysis found that intangible assets represent 90%
of S&P 500 market cap (~$21T in 2024). Extrapolating to global equity
markets and privately held IP is speculative but directionally correct.

The tokenizable surface of IP:

| IP Type | Global Count | Tokenization Use Case |
|---------|-------------|----------------------|
| Active patents | ~16M (WIPO 2024) | Licensing revenue streams, fractional R&D funding |
| Registered trademarks | ~73M (WIPO 2024) | Brand licensing, franchise tokens |
| Copyrights | Uncountable (automatic upon creation) | Royalty streams (music, publishing, software) |
| Trade secrets | Unmeasurable | N/A — secrecy is the value |

Music royalties are the furthest along: platforms like Royal and Anotherblock
have tokenized royalty streams from artists, allowing fans to own fractional
rights to songs. The global music royalty market ($43B in 2024, IFPI) is a
natural fit — small, high-frequency payment streams distributed to many
rights holders.

### 4.3 Carbon Credits: Tokenization as Market-Maker

The voluntary carbon market was ~$2B in 2024 but is projected to reach
$250B-$1T by 2030-2050 (BloombergNEF, TSVCM). The market's biggest problem
is fragmentation — no standardized registry, no price transparency, no
secondary liquidity. Tokenization directly addresses all three:

- **Toucan Protocol** tokenized 22M+ tonnes of carbon credits (2022-2024)
- **KlimaDAO** created on-chain carbon demand and price discovery
- **Verra and Gold Standard** are exploring blockchain-native registries

---

## 5. Digital Native Assets (~$5 Trillion)

Assets that were born digital — many already operate on or near
blockchain infrastructure.

### 5.1 Detailed Breakdown

| Asset Class | Estimated Value | Primary Source | Confidence |
|-------------|---------------:|----------------|:----------:|
| Cryptocurrency (total market cap) | $2.8T | CoinGecko (March 2026) | High |
| Domain names (~370M registered) | $0.05T | Verisign Domain Brief, GoDaddy aftermarket data | Medium |
| In-game items & virtual economies | $0.06T | Newzoo, Niko Partners ($60B+ market) | Low-Med |
| NFTs & digital art (total market) | $0.03T | NonFungible/DappRadar aggregate | Low |
| Digital advertising inventory (annual) | $0.7T | eMarketer/IAB Global Ad Spend (2024) | Medium |
| SaaS & cloud subscriptions (annual ARR) | $0.8T | Gartner/Synergy Research Group | Medium |
| Data as an asset class | $0.5T | Theoretical — McKinsey data valuation frameworks | Very Low |
| **Subtotal** | **~$5.0T** | | |

### 5.2 Data: The Unpriced Category

Data is the most philosophically interesting TTR category. It is clearly
valuable — the world's five most valuable companies are data companies. But
data has no standard unit, no market price, and no ownership framework that
would enable tokenization.

Attempts to price data:
- **McKinsey (2022):** US health data alone worth $300B-$600B/year if shared optimally
- **European Commission (2023):** EU data economy valued at EUR 829B (~4.9% of GDP)
- **World Bank:** Low-income countries could gain 1-2% GDP from better data markets

We include $0.5T as a placeholder — it is almost certainly a vast undercount
but there is no reliable methodology.

---

## 6. Government Records & Registrations

Not all tokenizable resources are "assets" in the financial sense. Government
records represent a massive surface of attestable claims that benefit from
blockchain properties (immutability, auditability, portability).

| Record Type | Global Count | Tokenization Use Case |
|-------------|-------------|----------------------|
| Land titles | ~1.4B residential + commercial (World Bank) | On-chain deed registry, instant title verification |
| Vehicle registrations | ~1.47B (OICA) | Transfer-of-title, lien tracking |
| Business registrations | ~400M SMEs globally (IFC) | Verifiable corporate identity, cap table management |
| Professional licenses | ~500M estimated (medical, legal, engineering) | Credential verification, cross-border recognition |
| Birth/death certificates | ~140M births/year (UN) | Identity foundation layer |
| Passport/ID records | ~5B adults globally | Self-sovereign identity (SSI) |

These are not included in the TTR valuation because they are not "assets"
with market value — but they represent the *infrastructure layer* on which
tokenized assets gain their legal force. A tokenized property deed is only
as good as the land registry that backs it.

---

## 7. The TTR Composition

### 7.1 Summary Table

| Category | Value | % of TTR (Conservative) |
|----------|------:|:-----------------------:|
| Real Assets | $507.5T | 57.0% |
| Financial Assets | $495.0T | 55.6% |
| Rights & Claims | $85.0T | 9.5% |
| Digital Native | $5.0T | 0.6% |
| **Conservative TTR** | **~$890T** | |
| *Less double-counting (financial assets backed by real assets)* | *-$200T* | |
| **Adjusted TTR** | **~$690T** | |
| Derivatives notional (additive exposure) | +$632T | |
| **Maximum TTR** | **~$1.6 Quadrillion** | |

**The double-counting problem.** A significant portion of financial assets
(mortgages, REITs, commodity futures) are *claims on* real assets. Adding
$380T in real estate and $130T in bonds (many of which are mortgage-backed)
overstates the TTR. We estimate ~$200T in overlap — primarily
mortgage-backed securities, commodity derivatives, and real estate
investment trusts. The adjusted TTR of ~$690T is likely the most honest
single number.

### 7.2 Composition Chart

```
    TTR Composition by Category (~$890T conservative)
    ══════════════════════════════════════════════════

    Real Estate         ████████████████████████████████████████████   $380T  43%
    Bonds               ██████████████████                             $130T  15%
    Equities            ███████████████                                $115T  13%
    M2 Money Supply     █████████████                                  $105T  12%
    Deposits            ██████████                                     $82T    9%
    IP & Rights         █████                                          $65T    7%
    Pension/SWF/PE      ████                                           $82T    9%
    Infrastructure      ███                                            $50T    6%
    Ag. Land            ██                                             $30T    3%
    Gold                █                                              $16T    2%
    Other               █                                              $35T    4%
    Digital Native      ▌                                              $5T    <1%

    Note: Bars are approximate. Percentages sum to >100% due to
    double-counting across categories.
```

---

## 8. Tokenization Penetration by Category

How much of each category is already tokenized? The answer is: almost nothing.

### 8.1 Current State (March 2026)

| Category | Total Value | Tokenized Value | Penetration | Key Projects |
|----------|----------:|----------------:|:-----------:|--------------|
| Stablecoins (M2 proxy) | $105T | $170B | 0.16% | USDT, USDC, PYUSD |
| Tokenized Treasuries | $130T | $3.5B | 0.003% | BUIDL, FOBXX, OUSG |
| Tokenized equities | $115T | $0.5B | 0.0004% | Securitize, INX |
| Tokenized real estate | $380T | $4.0B | 0.001% | RealT, Lofty, Propy |
| Tokenized commodities | $8T | $1.5B | 0.02% | PAXG, Tether Gold |
| Carbon credits on-chain | $1T (proj.) | $0.3B | 0.03% | Toucan, KlimaDAO |
| NFTs / digital art | $0.03T | $8B (peak was $40B) | ~26% | OpenSea, Blur |
| In-game items (on-chain) | $0.06T | $2B | ~3% | Axie, Immutable X |
| **Aggregate** | **~$890T** | **~$20B** | **~0.002%** | |

```
    Tokenization Penetration — Log Scale
    ═════════════════════════════════════

    100%  ┤
          │
     10%  ┤                                                    ● NFTs (~26%)
          │
      1%  ┤                                        ● In-game (~3%)
          │
    0.1%  ┤  ● Stablecoins (0.16%)
          │
   0.01%  ┤                ● Commodities (0.02%)
          │                     ● Carbon (0.03%)
  0.001%  ┤         ● Real estate (0.001%)    ● Treasuries (0.003%)
          │
 0.0001%  ┤                          ● Equities (0.0004%)
          │
          └────────────────────────────────────────────────────
            Financial   Real    Rights   Digital
```

### 8.2 The Penetration Paradox

The categories with the highest penetration (NFTs, in-game items) have the
smallest total addressable markets. The categories with the largest TAMs
(real estate, bonds, equities) have negligible penetration. This is not
surprising — tokenization started with digitally native assets that needed
no legal bridge to the physical world.

The next wave — already underway with BlackRock BUIDL and Franklin Templeton
FOBXX — is tokenizing financial assets that already exist as database entries.
The hardest wave — real estate, IP, natural resources — requires legal
infrastructure that does not yet exist in most jurisdictions.

---

## 9. Tokenization Difficulty Matrix

Not all assets are equally tokenizable. Value and difficulty are independent
dimensions.

```
    Tokenization Difficulty Matrix
    ══════════════════════════════

                          DIFFICULTY
              Low                              High
         ┌─────────────────────┬─────────────────────┐
         │                     │                     │
         │   SWEET SPOT        │   HARD PRIZES       │
    H    │                     │                     │
    i    │   Bonds ($130T)     │   Real Estate       │
    g    │   Equities ($115T)  │     ($380T)         │
    h    │   Deposits ($82T)   │   IP ($65T)         │
         │   M2/Cash ($105T)   │   Ag. Land ($30T)   │
    V    │   Pensions ($56T)   │   Infrastructure    │
    A    │                     │     ($50T)          │
    L    ├─────────────────────┼─────────────────────┤
    U    │                     │                     │
    E    │   QUICK WINS        │   NOT WORTH IT      │
         │                     │   (yet)             │
    L    │   Stablecoins       │   Water rights ($3T)│
    o    │   Gold tokens       │   Spectrum ($3T)    │
    w    │   Carbon credits    │   Vehicles ($16T)   │
         │   Domain names      │   Data ($0.5T)      │
         │   In-game items     │   Art ($2T)         │
         │                     │                     │
         └─────────────────────┴─────────────────────┘

    LOW DIFFICULTY: asset is already digital, standard unit exists,
    legal framework clear, custody is simple.

    HIGH DIFFICULTY: physical custody needed, legal jurisdiction varies,
    no standard unit, regulatory uncertainty.
```

### 9.1 Difficulty Drivers

| Difficulty Factor | Description | Most Affected Categories |
|-------------------|-------------|--------------------------|
| **Legal heterogeneity** | Property law varies by jurisdiction; no global standard | Real estate, land, water rights |
| **Custody bridge** | Need a legal entity to link token to physical asset | Real estate, vehicles, commodities |
| **Valuation opacity** | No public market price; appraisal-dependent | IP, art, infrastructure, data |
| **Regulatory uncertainty** | Unclear if tokenized version is a "security" | Equities, deposits, insurance |
| **Fragmentation** | No standard unit; each instance is unique | Art, patents, land parcels |
| **Counterparty requirement** | Need ongoing real-world performance | Insurance policies, carbon credits |

### 9.2 Tokenization Readiness Score

A composite score (0-100) based on: legal clarity (25%), digital maturity
(25%), standardization (25%), and market demand (25%).

| Category | Legal | Digital | Standard | Demand | **Score** |
|----------|:-----:|:-------:|:--------:|:------:|:---------:|
| Money / stablecoins | 18 | 25 | 25 | 25 | **93** |
| Government bonds | 22 | 25 | 23 | 22 | **92** |
| Listed equities | 20 | 25 | 23 | 20 | **88** |
| Gold / precious metals | 22 | 20 | 25 | 18 | **85** |
| Corporate bonds | 18 | 22 | 20 | 20 | **80** |
| Bank deposits | 15 | 25 | 20 | 18 | **78** |
| Carbon credits | 12 | 20 | 18 | 22 | **72** |
| Private equity/VC | 12 | 20 | 15 | 22 | **69** |
| Insurance products | 10 | 18 | 15 | 15 | **58** |
| Commercial real estate | 10 | 15 | 12 | 20 | **57** |
| Residential real estate | 8 | 12 | 12 | 18 | **50** |
| Intellectual property | 5 | 15 | 8 | 18 | **46** |
| Agricultural land | 5 | 8 | 10 | 12 | **35** |
| Water rights | 3 | 5 | 5 | 10 | **23** |
| Data | 2 | 15 | 3 | 15 | **35** |

---

## 10. Growth Projections: RWA Tokenization

### 10.1 Industry Projections

Multiple credible sources have published RWA tokenization forecasts:

| Source | Projection | Timeframe |
|--------|-----------|-----------|
| Boston Consulting Group | $16T in tokenized assets | By 2030 |
| BlackRock (Larry Fink) | "Next generation for markets" | Multi-decade |
| Citigroup | $4-5T in tokenized securities | By 2030 |
| McKinsey | $2T (excl. stablecoins/deposits) | By 2030 |
| Standard Chartered | $30T | By 2034 |
| Roland Berger | $10T | By 2030 |

The range ($2T to $30T by 2030) reflects fundamentally different assumptions
about regulatory speed and institutional adoption. We use **$5-10T by 2030**
as a base case — roughly in line with the BCG midpoint adjusted for
regulatory friction.

### 10.2 Growth Rate Analysis

```
    RWA Tokenization Growth Trajectory
    ═══════════════════════════════════

    Value
    (log)
    $100T ┤                                                    ╱
          │                                                 ╱
    $10T  ┤                                           ╱╱╱╱
          │                                     ╱╱╱╱╱
    $1T   ┤                               ╱╱╱╱
          │                          ╱╱╱╱╱
    $100B ┤                    ╱╱╱╱╱
          │              ╱╱╱╱╱
    $10B  ┤         ●╱╱╱╱
          │       ● (today: ~$20B)
    $1B   ┤     ●
          │   ●
    $100M ┤ ●
          └──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──
           2020 21 22 23 24 25 26 27 28 29 2030

    Historical CAGR (2020-2025): ~119%
    Projected CAGR (2025-2030): ~200% (to reach ~$5-10T)
    Required CAGR for BCG ($16T): ~250%
```

### 10.3 What's Driving the Growth

**Institutional entry (2024-2026):**
- BlackRock BUIDL: $2.9B AUM — largest tokenized fund
- Franklin Templeton FOBXX: $700M+ on-chain money market fund
- JPM Onyx: tokenized repo and intraday liquidity
- Citibank: tokenized deposits pilot with institutional clients
- HSBC Orion: tokenized gold and green bonds

**Regulatory catalysts:**
- EU MiCA (2024-2025): legal framework for crypto-assets
- US stablecoin legislation (2025-2026): bipartisan momentum
- Singapore MAS Project Guardian: multi-asset tokenization sandbox
- Hong Kong SFC: tokenized fund distribution framework
- Switzerland DLT Act: fully operational tokenized securities framework

**Infrastructure maturation:**
- Ethereum EIP-3643 (T-REX) for compliant security tokens
- Chainlink CCIP for cross-chain settlement
- SWIFT experiments with tokenized asset interoperability
- DTCC exploring blockchain-native settlement

---

## 11. Revenue Opportunity

If tokenization captures even a fraction of the management and transaction
fees currently charged on traditional assets, the revenue opportunity is
enormous.

### 11.1 Fee Compression Model

| Metric | Traditional | Tokenized | Compression |
|--------|------------|-----------|:-----------:|
| Equity trading fees | 5-50 bps | 1-5 bps | 80-90% |
| Bond settlement cost | $50-200/trade | <$1/trade | 95%+ |
| Real estate transaction cost | 5-6% of value | 1-2% (projected) | 60-70% |
| Cross-border remittance | 6-7% of value | <1% | 85%+ |
| Fund management fees | 50-200 bps | 10-50 bps | 50-75% |
| Private equity admin | 200+ bps | 50-100 bps | 50-75% |

### 11.2 Revenue at Scale

Assuming tokenization reaches $5-10T by 2030:

```
    Revenue Model: Tokenization Platform Fees
    ══════════════════════════════════════════

    CONSERVATIVE ($5T tokenized, low fee capture)
    ──────────────────────────────────────────────
    Issuance fees (10 bps one-time):           $5B
    Annual management fees (5 bps):            $2.5B/yr
    Trading fees (2 bps on 100% turnover):     $10B/yr
    Settlement savings captured (10%):         $5B/yr
    ────────────────────────────────────────
    Total annual revenue pool:                 ~$17.5B/yr

    BASE CASE ($10T tokenized, moderate fee capture)
    ─────────────────────────────────────────────────
    Issuance fees (10 bps one-time):           $10B
    Annual management fees (5 bps):            $5B/yr
    Trading fees (2 bps on 150% turnover):     $30B/yr
    Settlement savings captured (15%):         $15B/yr
    ────────────────────────────────────────
    Total annual revenue pool:                 ~$50B/yr

    AGGRESSIVE ($50T tokenized by 2035)
    ────────────────────────────────────
    Total annual revenue pool:                 ~$200B/yr
```

### 11.3 Who Captures the Value?

The tokenization value chain has distinct layers, each with different
competitive dynamics:

| Layer | Description | Likely Winners | Rev Share |
|-------|-------------|---------------|:---------:|
| **Blockchain infrastructure** | Settlement layer (Ethereum, Solana, Radix) | Network token holders | 5-10% |
| **Issuance platforms** | Token creation, compliance wrapping | Securitize, Tokeny, Fireblocks | 15-20% |
| **Custody & wallets** | Institutional-grade key management | Fireblocks, Anchorage, Ledger | 10-15% |
| **Trading venues** | Secondary market liquidity | tZERO, INX, DEXs | 20-25% |
| **Oracles & data** | Price feeds, proof of reserves | Chainlink, Pyth | 5-10% |
| **Traditional finance** | Distribution, client relationships | BlackRock, JPM, Goldman | 25-35% |

Traditional finance captures the largest share because they own the
distribution. BlackRock's BUIDL did not succeed because of its blockchain
infrastructure — it succeeded because BlackRock clients trust BlackRock.
The blockchain is the plumbing; the brand is the moat.

---

## 12. The MEST Connection

The TTR Valuation and the MEST Advantage are companion analyses. Together
they answer two questions:

1. **TTR:** How much value *could* move to tokenized infrastructure? (~$690T-$890T)
2. **MEST:** How much cheaper would it be to *run* that infrastructure? ($150-250B/year savings)

### 12.1 MEST Savings as a Function of TTR Penetration

| TTR Penetration | Tokenized Value | Est. MEST Savings | Savings as % of Traditional Cost |
|:--------------:|----------------:|------------------:|:-------------------------------:|
| 0.002% (today) | $20B | Negligible | ~0% |
| 0.5% | $4.5T | $2-4B/yr | ~0.5-1% |
| 1% | $9T | $5-10B/yr | ~1.5-3% |
| 5% | $45T | $30-50B/yr | ~8-14% |
| 10% | $90T | $60-100B/yr | ~17-28% |
| 50% | $450T | $150-250B/yr | ~40-70% |
| 100% (theoretical) | $890T | $200-300B/yr | ~55-85% |

The relationship is not linear because high-value, high-MEST categories
(OTC derivatives, equities) will tokenize before low-value, low-MEST
categories (bill payments, payroll). Each percentage point of TTR
penetration captures more MEST savings at the start of the curve.

### 12.2 The Flywheel

```
    The TTR-MEST Flywheel
    ═════════════════════

    ┌──────────────────┐
    │  More assets      │
    │  tokenized (TTR↑) │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  More on-chain    │
    │  liquidity        │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  Lower MEST       │──────────────┐
    │  multipliers      │              │
    └────────┬─────────┘              │
             │                         │
             ▼                         ▼
    ┌──────────────────┐     ┌──────────────────┐
    │  Lower cost per   │     │  Better price     │
    │  transaction      │     │  discovery         │
    └────────┬─────────┘     └────────┬─────────┘
             │                         │
             └──────────┬──────────────┘
                        │
                        ▼
             ┌──────────────────┐
             │  More demand to   │
             │  tokenize (TTR↑)  │
             └──────────────────┘
```

---

## 13. Confidence Assessment

This analysis spans five orders of magnitude in confidence — from IMF
monetary statistics (highly reliable) to data valuation (speculative).

| Tier | Categories | Combined Value | Confidence |
|------|-----------|---------------:|:----------:|
| **Tier 1: Published, audited** | M2, equities, bonds, derivatives, gold | $1,128T | High (70-90) |
| **Tier 2: Industry estimates** | Real estate, deposits, insurance, pensions, vehicles | $574T | Medium (40-65) |
| **Tier 3: Extrapolations** | IP, infrastructure, ag land, commodities | $157T | Low (20-45) |
| **Tier 4: Speculative** | Carbon, water, spectrum, data | $7T | Very Low (10-25) |

The TTR number is dominated by Tier 1 and 2 data. Even if Tier 3 and 4 are
off by 50%, the TTR changes by less than 10%.

---

## 14. Key Takeaways

1. **The total addressable market for tokenization is ~$690T-$890T** (adjusted
   for double-counting) or up to ~$1.6 quadrillion including derivatives
   notional exposure.

2. **Current penetration is ~0.002%.** The RWA tokenization market (~$20B) is
   a rounding error on the total addressable market. This is either a sign
   of massive upside or a sign that tokenization faces structural barriers
   that market size cannot overcome. Both are partially true.

3. **Real estate ($380T) is the largest single category** but also one of the
   hardest to tokenize due to legal heterogeneity and custody challenges.
   Financial assets ($495T) are larger in aggregate and significantly easier.

4. **The sweet spot is financial assets with high MEST multipliers.** Bonds
   ($130T, 8 MESTs), equities ($115T, 10 MESTs), and deposits ($82T, 5 MESTs)
   are already digital, legally standardized, and would benefit most from
   MEST compression. This is exactly where BlackRock, Franklin Templeton,
   and JPMorgan are building.

5. **$5-10T tokenized by 2030 is plausible** based on institutional momentum
   and regulatory clarity, implying a ~$17-50B annual revenue opportunity for
   the tokenization value chain.

6. **At 5% TTR penetration (~$45T), annual MEST savings reach $30-50B/year**
   — enough to fundamentally reshape financial infrastructure economics.

7. **Traditional finance will capture the largest share of tokenization
   revenue** through distribution and client relationships. The blockchain
   layer is necessary but not sufficient — trust and regulation are the
   binding constraints.

---

## Methodology Notes

**Financial asset values** are sourced from the IMF International Financial
Statistics database, BIS Quarterly Review (Q3 2024), World Federation of
Exchanges annual statistics, and OECD institutional investor databases.
Where possible, we use end-of-period values for consistency.

**Real asset values** rely on Savills' triennial "The Total Value of Global
Real Estate" report (most recent: 2024), supplemented by FAO land statistics,
OICA vehicle production data, and World Gold Council quarterly reports. Real
estate values are particularly volatile — the $380T figure assumes 2024
market conditions.

**IP valuation** uses the Ocean Tomo methodology (market cap minus tangible
book value = intangible value). This is a ceiling estimate — not all
intangible value is tokenizable IP. The $65T figure includes brand value,
customer relationships, and organizational capital that cannot be separated
into tradeable tokens.

**Tokenization penetration** is measured by summing on-chain RWA values
reported by rwa.xyz, DefiLlama RWA dashboard, and individual project
disclosures (BlackRock BUIDL, Franklin Templeton FOBXX, Securitize, RealT).
Stablecoin market cap is excluded from the RWA figure in some analyses but
included here as a tokenized representation of M2.

**Growth projections** synthesize published forecasts from BCG, McKinsey,
Citigroup, and Standard Chartered, adjusted for observed regulatory
timelines. Our base case ($5-10T by 2030) is below the BCG/Standard
Chartered projections but above McKinsey's conservative estimate.

**MEST savings estimates** are derived from the MEST Advantage analysis
(see `MEST_ADVANTAGE.md`), applying per-category compression ratios to the
tokenized asset mix.

**Limitations.** (1) Asset values are point-in-time estimates subject to
market conditions. (2) Double-counting between categories (e.g., MBS in both
bonds and real estate) is estimated, not precisely measured. (3) "Tokenizable"
does not mean "will be tokenized" — legal, political, and practical barriers
may permanently prevent tokenization of some categories. (4) Revenue
projections assume fee structures that do not yet exist at scale.

**Data sources:**
- IMF International Financial Statistics (2024)
- BIS Quarterly Review (Q3 2024) — OTC derivatives, banking statistics
- World Federation of Exchanges (WFE) Annual Statistics (2024)
- ICMA Bond Market Size Report (2024)
- Savills "The Total Value of Global Real Estate" (2024)
- World Gold Council Quarterly Report (Q1 2025)
- OICA World Vehicles in Use Statistics (2024)
- WIPO IP Statistics Data Center (2024)
- Ocean Tomo Intangible Asset Market Value Study (2024)
- rwa.xyz — Real-time RWA tokenization tracker
- BlackRock BUIDL disclosures (2025)
- BCG "Relevance of On-Chain Asset Tokenization" (2024)
- McKinsey "From Ripples to Waves: Tokenized Assets" (2024)
- Citigroup "Money, Tokens, and Games" (2024)
- Standard Chartered/Synpulse "Tokenisation Report" (2024)

---

*This analysis was produced as part of Universe of Finance Run 11.
March 2026.*

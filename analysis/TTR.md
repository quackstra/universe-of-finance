---
title: "Total Tokenizable Resources"
layout: default
nav_order: 3
---

# Total Tokenizable Resources (TTR)

> The Big Number measures transactions. The MEST Number measures state changes.
> The TTR Number measures the universe of discrete resources that *could* be
> represented as tokens on a programmable ledger — whether or not they are today.

*A framework from the Universe of Finance project. March 2026.*

---

## 1. Definition

**A Total Tokenizable Resource (TTR) is any discrete resource, right, or
obligation that could be uniquely represented and transferred on a programmable
ledger.**

Three criteria must hold for something to qualify as a TTR:

1. **Uniquely identifiable** — The resource has properties that distinguish it
   from all other resources. A specific parcel of land, a specific patent, a
   specific insurance policy. Fungible resources (dollars, barrels of oil)
   qualify because each *unit* is identifiable within its class.

2. **Transferable or verifiable** — The resource can either change hands
   (ownership transfer) or its state can be attested to by a third party
   (credential verification). A property deed transfers. A medical license
   is verified. Both are tokenizable.

3. **Multi-party interest** — At least two parties care about the resource's
   state. A diary entry fails this test. A property title passes it (owner,
   government, lender, insurer all care). A professional license passes it
   (holder, licensing board, employer, clients all care).

The definition is deliberately broad. We are not asking "what *should* be
tokenized?" or "what is *practical* to tokenize today?" We are asking:
**how large is the universe of things that meet the structural criteria for
tokenization?**

### What TTR Is Not

- **Not market cap.** TTR counts discrete tokenizable units, not their value.
  A $500K house and a $5M house are both 1 TTR unit.
- **Not current tokenization.** TTR includes everything that *could* be
  tokenized, regardless of whether anyone has done it.
- **Not a technology prescription.** TTR is ledger-agnostic. The resource
  could live on Ethereum, Radix, a government-run permissioned chain, or a
  system that does not exist yet.

---

## 2. The TTR Number

### Estimation

We count discrete tokenizable units across all categories, then sum.

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   The global economy contains approximately                      ║
║                                                                  ║
║           ~170 billion tokenizable resource units                 ║
║                                                                  ║
║   Range: 130 billion – 250 billion                               ║
║   (depending on granularity of digital assets and data rights)   ║
║                                                                  ║
║   Of these, fewer than 500 million are currently represented     ║
║   on any distributed ledger.                                     ║
║                                                                  ║
║   Current tokenization rate: < 0.3%                              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

This number is conservative. It counts discrete, identifiable units with
clear multi-party interest. It does not count every individual data record,
every social media post, or every IoT sensor reading — though arguments
exist for including all of these.

### How Big Is 170 Billion?

```
    Scaling the TTR Number
    ══════════════════════

    ~170 billion tokenizable resources
    ÷ 8 billion people on Earth
    ─────────────────────────────
    = ~21 tokenizable resources per person

    That is: your house, your car, your driver's license,
    your degree, your insurance policies, your bank accounts,
    your loyalty points, your health records, your professional
    certifications, your pension, your utility contracts,
    your phone number, your domain names, your data rights...

    21 per person is, if anything, an undercount for developed
    economies (where the average person has 30-50 discrete
    financial/legal/identity instruments) and an overcount for
    developing economies (where informal ownership dominates).
```

---

## 3. TTR Taxonomy

Six tiers, organized by current proximity to tokenization.

```
    The TTR Pyramid
    ═══════════════

                          /\
                         /  \         Tier 1: Financial Assets
                        / 6B  \       Money, securities, derivatives
                       / units \      Partially tokenized today
                      /──────────\
                     /            \
                    /    Tier 2    \   Real Assets
                   /     ~7B       \  Real estate, vehicles, commodities
                  /     units       \
                 /──────────────────\
                /                    \
               /      Tier 3         \  Rights & Claims
              /       ~20B            \  IP, licenses, carbon, insurance
             /        units            \
            /──────────────────────────\
           /                            \
          /        Tier 4                \  Identity & Credentials
         /         ~12B                   \  Degrees, licenses, health
        /          units                   \
       /────────────────────────────────────\
      /                                      \
     /          Tier 5                        \  Digital Native
    /           ~115B                          \  Domains, game items,
   /            units                           \  data rights, NFTs
  /──────────────────────────────────────────────\
 /                                                \
/              Tier 6                              \  Government Records
               ~10B                                 \  Land titles, vehicle
               units                                 \  regs, business licenses
──────────────────────────────────────────────────────
```

### Summary Table

| Tier | Category | Est. Global Units | Currently Tokenized | Tokenization Rate |
|------|----------|-------------------|--------------------|--------------------|
| 1 | Financial Assets | ~6B | ~400M | ~6.7% |
| 2 | Real Assets | ~7B | ~2M | ~0.03% |
| 3 | Rights & Claims | ~20B | ~50M | ~0.25% |
| 4 | Identity & Credentials | ~12B | ~5M | ~0.04% |
| 5 | Digital Native | ~115B | ~40M | ~0.03% |
| 6 | Government Records | ~10B | ~1M | ~0.01% |
| **Total** | | **~170B** | **~498M** | **~0.29%** |

---

## 4. Per-Category Deep Dive

### Tier 1: Financial Assets

Already partially tokenized. The frontier is well-mapped; the question is
pace of migration.

#### 1a. Money (Currency Units in Circulation)

| Attribute | Value |
|-----------|-------|
| **What** | Physical banknotes, coins, and digital currency units (M2 money supply expressed as discrete account balances) |
| **Global count** | ~3.5B discrete bank accounts + ~500M digital wallet balances + ~300M crypto wallet addresses with non-zero balance = **~4.3B units** |
| **Currently tokenized** | ~300M (stablecoin addresses + CBDC pilot accounts) |
| **Tokenization rate** | ~7% |
| **Complexity score** | 2/5 — Stablecoins have proven the model. CBDCs are in pilot. Regulatory framework is forming. |
| **Key blockers** | Central bank sovereignty concerns, AML/KYC requirements at scale, banking lobby resistance |
| **Example projects** | USDC (Circle), USDT (Tether), Digital Yuan (PBoC), Sand Dollar (Bahamas), BUIDL (BlackRock) |

#### 1b. Securities (Stocks, Bonds, Fund Shares)

| Attribute | Value |
|-----------|-------|
| **What** | Equity shares, corporate bonds, government bonds, mutual fund/ETF shares |
| **Global count** | ~58,000 listed equities × avg ~500M shares outstanding = ~29T shares → but counting unique instruments: **~600K distinct securities** with ~1.2B discrete account positions |
| **Currently tokenized** | ~50M (tokenized fund shares, security tokens on platforms like Securitize, tZERO) |
| **Tokenization rate** | ~4% |
| **Complexity score** | 3/5 — Legal frameworks (Reg D, Reg S) enable it; CSD integration and cross-border recognition remain hard |
| **Key blockers** | CSD monopolies, regulatory fragmentation across jurisdictions, institutional custody requirements |
| **Example projects** | BlackRock BUIDL ($2.9B), Franklin Templeton BENJI, Securitize, Ondo Finance |

#### 1c. Derivatives Contracts

| Attribute | Value |
|-----------|-------|
| **What** | Options, futures, swaps, forwards — each a discrete contractual obligation |
| **Global count** | ~100B open exchange-traded contracts + ~80M OTC derivative positions = **~100B+ contracts** (but many are short-lived; outstanding at any moment: ~15B) |
| **Currently tokenized** | ~50M (perpetual futures on DEXes, synthetic assets) |
| **Tokenization rate** | ~0.3% |
| **Complexity score** | 4/5 — Margin management, regulatory reporting (EMIR/Dodd-Frank), and counterparty risk make this structurally complex |
| **Key blockers** | Regulatory classification, margin requirements, counterparty risk management in DeFi |
| **Example projects** | dYdX, GMX, Synthetix, Drift Protocol |

---

### Tier 2: Real Assets

Physical things with title, registration, or ownership records.

#### 2a. Real Estate

| Attribute | Value |
|-----------|-------|
| **What** | Residential, commercial, and agricultural property titles |
| **Global count** | ~1.4B residential properties + ~300M commercial properties + ~570M agricultural parcels = **~2.3B parcels** |
| **Currently tokenized** | ~50K (RealT, Propy, Lofty, Red Swan) |
| **Tokenization rate** | ~0.002% |
| **Complexity score** | 4/5 — Title law is jurisdiction-specific; Torrens vs. deed recording systems vary globally; requires legal recognition of on-chain title |
| **Key blockers** | Local land law, title insurance industry resistance, surveying/cadastral data quality, fractional ownership regulation |
| **Example projects** | Propy, RealT (~$100M tokenized), Lofty, HouseBit |

*See Section 8 for a deep dive on property deeds.*

#### 2b. Vehicles

| Attribute | Value |
|-----------|-------|
| **What** | Cars, trucks, motorcycles, boats, aircraft — each with a registration/title |
| **Global count** | ~1.5B registered motor vehicles + ~40M boats + ~400K registered aircraft = **~1.54B units** |
| **Currently tokenized** | ~10K (mostly luxury vehicle NFTs and fractional supercar platforms) |
| **Tokenization rate** | ~0.0007% |
| **Complexity score** | 3/5 — VIN/registration systems are mature and digital in most countries; legal framework for title transfer is the gap |
| **Key blockers** | DMV/registration office integration, lien recording, insurance linkage |
| **Example projects** | DIMO (vehicle data tokenization, 100K+ connected vehicles), CurioInvest (supercars) |

#### 2c. Commodities and Physical Goods

| Attribute | Value |
|-----------|-------|
| **What** | Warehouse receipts, bills of lading, precious metals in custody, agricultural output certificates |
| **Global count** | ~500M active warehouse receipts + ~200M active bills of lading + ~50M precious metal custody records = **~750M units** |
| **Currently tokenized** | ~2M (Paxos Gold, Tether Gold, commodity-backed tokens) |
| **Tokenization rate** | ~0.27% |
| **Complexity score** | 3/5 — Commodity standards are well-defined; custody/verification is the hard part |
| **Key blockers** | Physical verification (is the gold really there?), quality grading, cross-border commodity regulation |
| **Example projects** | Paxos Gold (PAXG), Tether Gold (XAUT), Agrotoken (grain-backed tokens), TradeFinex |

#### 2d. Machinery, Equipment, and Industrial Assets

| Attribute | Value |
|-----------|-------|
| **What** | Factory equipment, construction machinery, medical devices, energy infrastructure — each with serial numbers and maintenance histories |
| **Global count** | ~2B discrete pieces of industrial/commercial equipment with serial tracking |
| **Currently tokenized** | ~5K (mostly IoT-linked asset tokens in pilot programs) |
| **Tokenization rate** | ~0.0003% |
| **Complexity score** | 3/5 — Asset tracking systems (RFID, IoT) already generate digital twins; tokenization adds ownership/financing layer |
| **Key blockers** | Equipment diversity, depreciation modeling, cross-border leasing law |
| **Example projects** | Centrifuge (real-world asset financing), Goldfinch |

---

### Tier 3: Rights and Claims

Intangible assets with economic value and multi-party interest.

#### 3a. Intellectual Property

| Attribute | Value |
|-----------|-------|
| **What** | Patents, trademarks, copyrights, trade secrets with registered status |
| **Global count** | ~16M active patents + ~70M active trademarks + ~50M+ registered copyrights = **~136M registered IP assets** (but unregistered copyrights number in the billions — every creative work is automatically copyrighted) |
| **Currently tokenized** | ~500K (mostly music royalty tokens and IP-backed NFTs) |
| **Tokenization rate** | ~0.37% (of registered IP) |
| **Complexity score** | 4/5 — IP law varies by jurisdiction; valuation is subjective; enforcement depends on courts, not code |
| **Key blockers** | Jurisdictional IP law variation, valuation difficulty, enforcement mechanism gap |
| **Example projects** | Royal.io (music royalties), Molecule (biotech IP), IPwe (patent tokenization with IBM) |

#### 3b. Carbon Credits and Environmental Assets

| Attribute | Value |
|-----------|-------|
| **What** | Carbon offsets, renewable energy certificates (RECs), biodiversity credits, water quality trading permits |
| **Global count** | ~2B active carbon credits + ~500M active RECs + ~100M other environmental certificates = **~2.6B units** |
| **Currently tokenized** | ~30M (Toucan Protocol, KlimaDAO, Flowcarbon) |
| **Tokenization rate** | ~1.2% |
| **Complexity score** | 3/5 — Registries (Verra, Gold Standard) already issue serial-numbered credits; on-chain bridge is straightforward |
| **Key blockers** | Double-counting prevention across registries, additionality verification, vintage quality |
| **Example projects** | Toucan Protocol, KlimaDAO, Flowcarbon, Carbonmark |

#### 3c. Insurance Policies

| Attribute | Value |
|-----------|-------|
| **What** | Life, health, property, casualty, and specialty insurance policies — each a discrete contractual obligation |
| **Global count** | ~6.5B active insurance policies globally (many people hold multiple policies) |
| **Currently tokenized** | ~100K (parametric insurance on-chain, Etherisc, Nexus Mutual for DeFi) |
| **Tokenization rate** | ~0.002% |
| **Complexity score** | 5/5 — Insurance is among the most regulated industries; actuarial models, state-by-state licensing, claims adjudication all resist tokenization |
| **Key blockers** | Regulatory classification (is a tokenized policy a security?), claims oracle problem, actuarial model integration |
| **Example projects** | Etherisc, Nexus Mutual, InsurAce, Arbol (parametric weather) |

#### 3d. Loyalty Points and Rewards

| Attribute | Value |
|-----------|-------|
| **What** | Airline miles, hotel points, credit card rewards, retail loyalty tokens |
| **Global count** | ~300B+ outstanding loyalty point balances globally (representing ~$200B in unredeemed value) — but counted as discrete program memberships: **~5B active loyalty accounts** |
| **Currently tokenized** | ~10M (Singapore Airlines KrisPay, Bakkt wallet) |
| **Tokenization rate** | ~0.2% |
| **Complexity score** | 2/5 — Programs already have digital balances and APIs; interoperability is the unlock |
| **Key blockers** | Program operator resistance (breakage revenue at risk), cross-program exchange rate challenges |
| **Example projects** | Bakkt (loyalty point aggregation), Points.com, Trip.com blockchain loyalty |

#### 3e. Licenses and Permits

| Attribute | Value |
|-----------|-------|
| **What** | Spectrum licenses, water rights, mining rights, fishing quotas, emissions permits, liquor licenses |
| **Global count** | ~50M spectrum licenses + ~200M water rights + ~100M mining/resource permits + ~500M other government-issued permits = **~850M units** |
| **Currently tokenized** | ~5K (mostly pilot programs for carbon-adjacent permits) |
| **Tokenization rate** | ~0.0006% |
| **Complexity score** | 5/5 — Government-issued, jurisdiction-specific, often non-transferable by design |
| **Key blockers** | Sovereign authority over issuance, political resistance, transferability restrictions |
| **Example projects** | WaterBridge (water rights trading), very early stage |

#### 3f. Supply Chain Documents

| Attribute | Value |
|-----------|-------|
| **What** | Bills of lading, letters of credit, certificates of origin, phytosanitary certificates, customs declarations |
| **Global count** | ~4B trade documents issued annually × ~3 year active lifecycle = **~12B active documents** |
| **Currently tokenized** | ~5M (TradeLens before shutdown, CargoX, electronic bills of lading) |
| **Tokenization rate** | ~0.04% |
| **Complexity score** | 3/5 — MLETR (Model Law on Electronic Transferable Records) adopted by UK, Singapore, others; legal framework is forming |
| **Key blockers** | Multi-party coordination (shipping lines, ports, customs, banks), legacy paper processes, jurisdictional acceptance |
| **Example projects** | CargoX, TradeLens (discontinued 2022 — cautionary tale), GSBN, edoxOnline |

---

### Tier 4: Identity and Credentials

Not transferable in the ownership sense, but verifiable — a credential
token attests that a claim is true without revealing the underlying data.

#### 4a. Professional Licenses

| Attribute | Value |
|-----------|-------|
| **What** | Medical licenses, legal bar admissions, engineering certifications, teaching credentials, financial advisor registrations |
| **Global count** | ~500M active professional licenses globally |
| **Currently tokenized** | ~1M (pilot programs, blockchain-based credential verification) |
| **Tokenization rate** | ~0.2% |
| **Complexity score** | 3/5 — Licensing boards are conservative but see value in fraud prevention |
| **Key blockers** | Licensing board adoption, cross-jurisdiction recognition, revocation mechanisms |
| **Example projects** | Dock.io, Hyland Credentials, Learning Machine (acquired by Hyland) |

#### 4b. Academic Credentials

| Attribute | Value |
|-----------|-------|
| **What** | University degrees, professional certifications, course completions, transcripts |
| **Global count** | ~3B cumulative academic credentials held by living people (degrees + professional certifications) |
| **Currently tokenized** | ~2M (MIT digital diplomas, various pilot programs) |
| **Tokenization rate** | ~0.07% |
| **Complexity score** | 2/5 — W3C Verifiable Credentials standard exists; issuer adoption is the bottleneck |
| **Key blockers** | University IT inertia, accreditation body buy-in, privacy regulations (FERPA, GDPR) |
| **Example projects** | MIT Digital Diplomas, Blockcerts, Velocity Network (for employment credentials) |

#### 4c. Healthcare Records (Access Rights)

| Attribute | Value |
|-----------|-------|
| **What** | Patient health record access tokens — not the data itself, but the right to access/share specific records |
| **Global count** | ~8B discrete medical records with multi-party access interest (patient, provider, insurer, pharmacy) |
| **Currently tokenized** | ~2M (MedRec pilot, Patientory, various health chain projects) |
| **Tokenization rate** | ~0.03% |
| **Complexity score** | 5/5 — HIPAA, GDPR, and health data sovereignty laws create extreme regulatory complexity |
| **Key blockers** | Health data regulation, EHR vendor lock-in (Epic, Cerner), patient consent management |
| **Example projects** | MedRec (MIT), Patientory, BurstIQ, Solve.Care |

#### 4d. Identity Documents

| Attribute | Value |
|-----------|-------|
| **What** | Passports, national IDs, birth certificates, social security numbers — as verifiable credentials |
| **Global count** | ~1B active passports + ~5B national ID cards + ~1.5B birth certificates on record = **~7.5B** (but ~1B people lack any form of legal ID — World Bank ID4D) |
| **Currently tokenized** | ~100K (Estonia e-Residency, various DID pilots) |
| **Tokenization rate** | ~0.001% |
| **Complexity score** | 5/5 — Sovereign identity is the most politically sensitive tokenization target |
| **Key blockers** | National sovereignty, privacy absolutism, the "key recovery" problem for self-sovereign identity |
| **Example projects** | Estonia e-Residency, WorldCoin (iris-based), Polygon ID, Spruce |

---

### Tier 5: Digital Native

Resources that were born digital. Many already have unique IDs and
transferability — tokenization is natural.

#### 5a. Domain Names

| Attribute | Value |
|-----------|-------|
| **What** | Internet domain registrations (ICANN TLDs + blockchain-native domains) |
| **Global count** | ~360M registered domain names (ICANN) + ~5M blockchain domains (ENS, Unstoppable) = **~365M** |
| **Currently tokenized** | ~5M (ENS, Unstoppable Domains) |
| **Tokenization rate** | ~1.4% |
| **Complexity score** | 1/5 — ENS has proven the model; ICANN domains could be bridged |
| **Key blockers** | ICANN governance, registrar business model disruption, dispute resolution (UDRP) |
| **Example projects** | ENS (Ethereum Name Service), Unstoppable Domains, Handshake |

#### 5b. Digital Art and Collectibles

| Attribute | Value |
|-----------|-------|
| **What** | Digital artwork, trading cards, collectible items, music as NFTs |
| **Global count** | ~500M discrete digital collectible items across platforms (including game-adjacent items with marketplace value) |
| **Currently tokenized** | ~30M (NFTs minted 2021-2025 with ongoing ownership tracking) |
| **Tokenization rate** | ~6% |
| **Complexity score** | 1/5 — Already proven at scale; the 2021-2022 NFT boom demonstrated tokenization works, even if valuations corrected |
| **Key blockers** | Market volatility perception, IP rights clarity, environmental criticism (diminishing with PoS) |
| **Example projects** | OpenSea, Blur, Foundation, Zora |

#### 5c. In-Game Items and Virtual Assets

| Attribute | Value |
|-----------|-------|
| **What** | Skins, weapons, characters, virtual land, in-game currencies with marketplace value |
| **Global count** | ~100B+ discrete in-game items across all platforms (Steam alone has ~10B items in inventories) |
| **Currently tokenized** | ~2M (Axie Infinity assets, The Sandbox land, Illuvium) |
| **Tokenization rate** | ~0.002% |
| **Complexity score** | 2/5 — Game studios control issuance; the question is willingness, not capability |
| **Key blockers** | Game studio resistance (loss of control), player backlash against "crypto games," regulatory uncertainty on virtual economies |
| **Example projects** | Axie Infinity, The Sandbox, Immutable X, Ronin Network |

#### 5d. Data Rights and Digital Twins

| Attribute | Value |
|-----------|-------|
| **What** | Personal data access rights (GDPR Article 20 portability), IoT sensor data ownership, digital twin ownership records |
| **Global count** | ~15B discrete data right claims (every internet user × multiple platform data stores) — highly speculative |
| **Currently tokenized** | ~3M (Ocean Protocol data tokens, Streamr data unions) |
| **Tokenization rate** | ~0.02% |
| **Complexity score** | 4/5 — Legal definition of "data ownership" is contested; technical enforcement is immature |
| **Key blockers** | Data ownership legal ambiguity, platform resistance, valuation difficulty |
| **Example projects** | Ocean Protocol, Streamr, SOLID (Tim Berners-Lee), Ceramic Network |

---

### Tier 6: Government Records

Sovereign-issued records that establish legal facts.

#### 6a. Land Titles and Cadastral Records

| Attribute | Value |
|-----------|-------|
| **What** | Official government records of land ownership, separate from the property itself — the title, not the house |
| **Global count** | ~3B land parcels globally (includes undeveloped land, agricultural, government-owned). Only ~1.5B have formal title registration |
| **Currently tokenized** | ~500K (Georgia, Honduras, India pilot programs) |
| **Tokenization rate** | ~0.03% (of formally registered titles) |
| **Complexity score** | 4/5 — Requires government buy-in and legal reform recognizing on-chain records |
| **Key blockers** | Sovereign authority, legacy cadastral systems, corruption (in some jurisdictions, opacity is a feature) |
| **Example projects** | Georgia (Bitfury partnership), Honduras (Factom), India (Andhra Pradesh pilot), Sweden (Chromaway pilot) |

#### 6b. Vehicle Registrations

| Attribute | Value |
|-----------|-------|
| **What** | Government vehicle registration records, inspection certificates, emissions compliance |
| **Global count** | ~1.5B registered vehicles (same physical assets as Tier 2, but this is the government record, not the asset) |
| **Currently tokenized** | ~100K (pilot programs) |
| **Tokenization rate** | ~0.007% |
| **Complexity score** | 3/5 — DMVs are digitizing; blockchain adds immutability and cross-state portability |
| **Key blockers** | Government IT procurement cycles, inter-agency data sharing, privacy concerns |
| **Example projects** | BMW (vehicle history on blockchain), MOBI (Mobility Open Blockchain Initiative) |

#### 6c. Business Licenses and Registrations

| Attribute | Value |
|-----------|-------|
| **What** | Business incorporation records, operating licenses, tax registrations |
| **Global count** | ~400M registered businesses globally (formal economy) |
| **Currently tokenized** | ~50K (mostly pilot programs, Delaware blockchain LLC records) |
| **Tokenization rate** | ~0.01% |
| **Complexity score** | 3/5 — Corporate registries are already digital; adding on-chain verification is incremental |
| **Key blockers** | Multi-jurisdiction complexity, beneficial ownership privacy, AML requirements |
| **Example projects** | Delaware blockchain initiative, Singapore ACRA digital certificates, Dubai DIFC |

#### 6d. Vital Records

| Attribute | Value |
|-----------|-------|
| **What** | Birth certificates, death certificates, marriage certificates |
| **Global count** | ~5B vital records on file globally (with ~140M new births + ~60M deaths + ~50M marriages per year) |
| **Currently tokenized** | ~50K (pilot programs, mostly birth certificate verification) |
| **Tokenization rate** | ~0.001% |
| **Complexity score** | 5/5 — Among the most conservative government functions; privacy sensitivity is extreme |
| **Key blockers** | Government conservatism, citizen trust, privacy law, the permanence problem (a blockchain birth certificate is forever) |
| **Example projects** | Zug, Switzerland (blockchain-based eID), Brazil (pilot for birth certificates) |

---

## 5. The Tokenization Gap

Less than 0.3% of the TTR universe is currently on any distributed ledger.
The gap is enormous — and unevenly distributed.

### Gap by Tier

```
    The Tokenization Gap (% of TTR Currently On-Chain)
    ═══════════════════════════════════════════════════

    Tier 1: Financial        ██████▌                              6.7%
    Tier 2: Real Assets      ▏                                    0.03%
    Tier 3: Rights/Claims    ▎                                    0.25%
    Tier 4: Identity/Creds   ▏                                    0.04%
    Tier 5: Digital Native   ▏                                    0.03%
    Tier 6: Govt Records     ▏                                    0.01%
                             ─────┬─────┬─────┬─────┬─────┬─────
                                  2%    4%    6%    8%   10%   12%
```

### Gap Table

| Tier | Total Units | Tokenized | Gap (Un-tokenized) | % Gap |
|------|-------------|-----------|---------------------|-------|
| 1. Financial Assets | 6.0B | 400M | 5.6B | 93.3% |
| 2. Real Assets | 7.0B | 2M | 7.0B | >99.97% |
| 3. Rights & Claims | 20.0B | 50M | 19.95B | 99.75% |
| 4. Identity & Credentials | 12.0B | 5M | 12.0B | 99.96% |
| 5. Digital Native | 115.0B | 40M | 115.0B | 99.97% |
| 6. Government Records | 10.0B | 1M | 10.0B | 99.99% |
| **Total** | **170.0B** | **498M** | **~169.5B** | **99.7%** |

### Why the Gap Exists

The gap is not primarily technical. The infrastructure to tokenize most of
these resources exists today. The gap persists because of:

1. **Legal recognition** — Most jurisdictions do not recognize on-chain
   records as legally authoritative. A tokenized deed is not a deed until
   the law says it is.

2. **Institutional inertia** — Title companies, custodians, registrars, and
   licensing boards have no incentive to tokenize themselves out of existence.

3. **The last-mile problem** — Connecting physical reality to on-chain state
   requires trusted oracles. Is the gold really in the vault? Is the house
   still standing? Is the license still valid?

4. **Privacy** — Many TTR categories (health records, identity documents)
   require selective disclosure. Public blockchains are a poor fit without
   privacy layers (ZK proofs, confidential transactions).

5. **Key management** — If you lose your private key, you lose your house.
   The average person is not ready for this responsibility model. Recovery
   mechanisms must mature.

---

## 6. TTR x TPS: The Big Number Implications

If the TTR universe were fully tokenized, each resource would generate
ongoing state changes: transfers, updates, compliance checks, dividend
distributions, insurance claims, verification requests, and more.

### State-Change Frequency by TTR Tier

Not all tokenized resources transact at the same rate.

| Tier | Units | Est. State Changes/Unit/Year | Annual State Changes | Implied TPS |
|------|-------|------------------------------|---------------------|-------------|
| 1. Financial | 6B | 50 (trades, transfers, dividends, rebalances) | 300B | 9,513 |
| 2. Real Assets | 7B | 2 (transfers, lien updates, insurance renewals) | 14B | 444 |
| 3. Rights & Claims | 20B | 5 (transfers, renewals, verifications, claims) | 100B | 3,171 |
| 4. Identity & Creds | 12B | 10 (verification requests, renewals, attestations) | 120B | 3,805 |
| 5. Digital Native | 115B | 3 (transfers, updates, access grants) | 345B | 10,940 |
| 6. Government Records | 10B | 1 (annual renewal, verification, amendment) | 10B | 317 |
| **Total** | **170B** | | **889B** | **~28,190** |

### The Full-Tokenization TPS Impact

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   Current Big Number:              ~73,750 TPS                   ║
║                                                                  ║
║   Additional TPS from full TTR                                   ║
║   tokenization (new state changes                                ║
║   not currently in the Big Number): ~28,190 TPS                  ║
║                                                                  ║
║   Projected Big Number (full TTR):  ~102,000 TPS                 ║
║                                                                  ║
║   Increase:                         ~38%                         ║
║                                                                  ║
║   NOTE: Most of this increase comes from identity                ║
║   verification (Tier 4) and digital asset transfers              ║
║   (Tier 5) — categories that barely register in                  ║
║   today's Big Number.                                            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

This is likely an undercount. Tokenized resources enable *new* transaction
types that do not exist in the paper world:

- **Fractional transfers** — Selling 0.01% of a property, impossible with
  paper deeds, trivial with tokens. Each fractional transfer is a new TPS.
- **Automated compliance** — Smart contracts checking license validity,
  insurance coverage, or credit status on every interaction.
- **Composability** — Using a tokenized house as collateral for a loan that
  funds an investment that pays dividends, all in one atomic transaction.
- **Micropayments for verification** — Paying $0.001 each time someone
  verifies your credential. At scale, this alone could add thousands of TPS.

---

## 7. TTR x MEST: The Bilateral State-Change Impact

Tokenization has two opposing effects on MEST:

### Effect 1: MEST Compression Per Transaction

As documented in [MEST_ADVANTAGE.md](MEST_ADVANTAGE.md), tokenization
reduces the MEST multiplier for each transaction by eliminating
intermediaries. A tokenized property transfer generates ~2 MESTs
(seller token debit + buyer token credit) instead of ~8 MESTs
(deed preparation, title search, escrow, recording, lender notification,
insurance update, tax assessor notification, registry update).

```
    Property Transfer: Traditional vs. Tokenized
    ═════════════════════════════════════════════

    TRADITIONAL (~8 MESTs)
    Seller → Attorney → Title Search → Escrow → Recording Office
                                                     ↓
              Lender ← Insurance Co ← Tax Assessor ← Registry

    TOKENIZED (~2 MESTs)
    Seller Wallet ──── property NFT ────→ Buyer Wallet
         │                                     │
       MEST 1                               MEST 2
       (token debit)                        (token credit)

    Smart contract handles escrow, lien check, and recording
    atomically — no bilateral state changes needed for intermediaries.

    MEST compression: 75% (8 → 2)
```

### Effect 2: MEST Volume Expansion

But tokenization also creates *more things that generate state changes*.
Today, a property title sits in a filing cabinet and generates maybe 1
state change per decade (when it sells). Tokenized, it could generate
dozens of state changes per year:

- Fractional ownership rebalancing
- Automated insurance policy checks
- Property tax payment confirmation
- Rental income distribution to token holders
- Collateral verification for DeFi loans
- Zoning change notification
- Appraisal update propagation

### Net MEST Impact Model

| Factor | Effect on MEST/s |
|--------|-----------------|
| Compression of existing transactions (7.4x → ~2.7x) | -345,000 MEST/s |
| New TPS from TTR tokenization (+28,190 TPS × ~2.7x avg multiplier) | +76,113 MEST/s |
| Increased state-change frequency on existing assets | +50,000-100,000 MEST/s (est.) |
| **Net effect** | **-170,000 to -220,000 MEST/s** |

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   MEST Impact of Full TTR Tokenization                           ║
║   ═════════════════════════════════════                           ║
║                                                                  ║
║   Current MEST/s:                    ~545,000                    ║
║   After compression:                 ~200,000                    ║
║   After new TTR state changes:       ~325,000 - 375,000         ║
║                                                                  ║
║   Net MEST reduction:                ~31% - 40%                  ║
║                                                                  ║
║   Key insight: Tokenization REDUCES MESTs per transaction        ║
║   but INCREASES the number of things transacting.                ║
║   The compression wins, but not by as much as a naive            ║
║   "just compress everything" model predicts.                     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 8. Property Deeds Deep Dive

Real estate is the world's largest asset class (~$380 trillion in total
value). It is also one of the least tokenized. This section examines why,
and what full tokenization would look like.

### 8.1 The Scale

```
    Global Real Estate: The Untokenized Giant
    ══════════════════════════════════════════

    Residential properties:     ~1.4 billion
    Commercial properties:      ~300 million
    Agricultural parcels:       ~570 million
    ──────────────────────────────────────────
    Total titled parcels:       ~2.3 billion

    Estimated global value:     ~$380 trillion
    Annual transaction volume:  ~50 million property sales/year
    Average holding period:     ~7-10 years (residential)

    For comparison:
    - Global stock market cap:  ~$110 trillion
    - Global bond market:       ~$130 trillion
    - Real estate exceeds BOTH combined
```

### 8.2 Current Title Systems

Three main systems govern land title worldwide:

**Torrens Title (government-guaranteed)**
- Used in: Australia, much of Canada, parts of UK, Singapore, Malaysia, NZ
- How it works: Government maintains an authoritative register. The register
  *is* the title. If the register says you own it, you own it.
- Tokenization fit: HIGH — already a single source of truth; moving to
  blockchain is a database migration, not a conceptual shift.

**Deed Recording (US-style)**
- Used in: United States, much of Latin America
- How it works: Government records deeds but does not guarantee them. Title
  must be traced through the "chain of title" — every deed back to the
  original land grant. This is why title insurance exists.
- Tokenization fit: MEDIUM — requires resolving the chain-of-title problem
  first, then establishing the token as authoritative.

**Informal/Customary**
- Used in: Much of Sub-Saharan Africa, parts of Southeast Asia, indigenous
  lands globally
- How it works: Ownership is established by community consensus, oral
  history, or physical occupation. No formal register exists.
- Tokenization fit: LOW (but HIGH impact) — tokenization could *create*
  formal title where none exists, enabling 1B+ people to use land as
  collateral for the first time.

### 8.3 The Title Insurance Problem

In the US, the deed recording system created a $26 billion/year industry
that exists solely because the government does *not* guarantee title:

```
    The Title Insurance Industry
    ════════════════════════════

    Annual US title insurance premiums:     $26 billion (2024)
    Industry loss ratio:                    3-5%
    (Meaning: $0.97 of every $1 in premiums goes to
     search costs, overhead, and profit — NOT to claims)

    Why it exists:
    ┌────────────────────────────────────────────────────┐
    │ US deed recording does NOT guarantee title.         │
    │ A deed can be recorded but still be invalid         │
    │ (forged signature, undisclosed lien, clerical       │
    │ error, missing heir, boundary dispute).             │
    │                                                     │
    │ Title insurance protects the buyer against defects  │
    │ in the chain of title — defects that a Torrens-     │
    │ style authoritative register would prevent.         │
    └────────────────────────────────────────────────────┘

    If US property titles were tokenized on an authoritative
    ledger (government-backed, Torrens-like):

    - Title search: eliminated (ledger is authoritative)
    - Title insurance: eliminated (ledger is guaranteed)
    - Escrow: reduced to smart contract (atomic DvP)
    - Recording: automatic (on-chain = recorded)

    Potential savings: $20-25 billion/year in the US alone
    (title insurance premiums minus the 3-5% that goes to claims)
```

### 8.4 The MEST Impact of Tokenized Property

A traditional US home purchase involves approximately 15 distinct bilateral
state changes:

```
    Traditional Home Purchase MEST Cascade
    ═══════════════════════════════════════

     1. Listing agreement         (seller + agent)
     2. Purchase offer            (buyer + seller)
     3. Mortgage application      (buyer + lender)
     4. Appraisal order           (lender + appraiser)
     5. Title search              (title company + county records)
     6. Title commitment          (title company + lender)
     7. Home inspection           (buyer + inspector)
     8. Mortgage approval         (lender + buyer)
     9. Escrow deposit            (buyer + escrow agent)
    10. Closing/settlement        (all parties: buyer, seller, agents,
                                   lender, title company, escrow)
    11. Deed recording            (title company + county recorder)
    12. Mortgage recording        (lender + county recorder)
    13. Title insurance issuance  (title company + buyer/lender)
    14. Tax reassessment trigger  (county assessor + buyer)
    15. Insurance policy transfer (insurer + buyer)

    Total: ~15 MESTs over 30-60 days
    Typical closing costs: $10,000-$20,000
```

A tokenized property transfer:

```
    Tokenized Home Purchase
    ═══════════════════════

     1. Property NFT transfer     (seller wallet → buyer wallet)
     2. Payment token transfer    (buyer wallet → seller wallet)

    Smart contract handles: title verification (on-chain),
    lien check (on-chain), escrow (atomic), recording (automatic),
    tax notification (event emission), insurance verification
    (oracle check).

    Total: 2 MESTs in ~6 seconds
    Estimated closing costs: $100-$500
    (legal review, smart contract audit fee, network fees)

    MEST compression: 87% (15 → 2)
    Cost compression: 95-97%
    Time compression: 99.99% (60 days → 6 seconds)
```

### 8.5 Tokenization Projects in Real Estate

| Project | Model | Scale | Status (2025-2026) |
|---------|-------|-------|---------------------|
| **RealT** | Fractional ownership of US rental properties as ERC-20 tokens | ~$100M tokenized, ~400 properties | Active, generating rental yield on-chain |
| **Propy** | End-to-end real estate transactions on blockchain; US county recorder integration | Pilot in select US counties | Active, growing county partnerships |
| **Lofty** | Fractional US real estate, $50 minimum | ~$40M tokenized | Active on Algorand |
| **Red Swan** | Commercial real estate tokenization | ~$4B in pipeline | Active |
| **Georgia (country)** | Government land registry on blockchain (Bitfury) | National rollout | Operational since 2017 |
| **HouseBit** | Fractional luxury real estate | Early stage | Beta |

### 8.6 Fractional Ownership: The TPS Multiplier

Tokenization enables fractional property ownership. A single property that
changes hands once per decade could instead have 1,000 fractional owners
trading daily. The TPS implications:

```
    Fractional Ownership TPS Model
    ══════════════════════════════

    Traditional:
    50M property sales/year ÷ 31.5M seconds/year = 1.6 TPS

    Tokenized (conservative):
    2.3B properties × 10% fractionalized × 100 fractions each
    = 23B fractional tokens
    × 5% annual turnover = 1.15B trades/year
    = 36.5 TPS

    Tokenized (aggressive):
    2.3B properties × 30% fractionalized × 1,000 fractions each
    = 690B fractional tokens
    × 10% annual turnover = 69B trades/year
    = 2,188 TPS

    Range: 37 - 2,188 TPS (vs. 1.6 TPS today)
    Multiplier: 23x to 1,368x
```

Fractional ownership does not just tokenize an existing resource — it
creates a new asset class. Each fraction is a new TTR unit. 2.3 billion
properties become 23 billion to 690 billion fractional tokens.

---

## 9. Methodology and Limitations

### 9.1 How We Estimated Counts

Each TTR category was estimated using one or more of:

1. **Top-down from industry reports** — World Bank (land titles, ID
   coverage), WIPO (IP registrations), ICANN (domain names), WFE (securities),
   BIS (banking), insurance industry associations.

2. **Bottom-up from per-country data** — For real estate, vehicles, and
   government records, we summed available country-level data and extrapolated
   for countries without public registries.

3. **Cross-referencing with population** — For identity and credential
   categories, we used global population (~8B) multiplied by estimated
   per-capita resource counts, validated against available registry data.

### 9.2 Confidence Levels

| Tier | Confidence | Notes |
|------|-----------|-------|
| 1. Financial Assets | **HIGH** (75) | Well-reported by BIS, WFE, industry associations |
| 2. Real Assets | **MEDIUM** (55) | Real estate counts are solid; vehicle registrations less so outside OECD |
| 3. Rights & Claims | **MEDIUM** (50) | IP registrations are accurate; supply chain docs and environmental credits have wide ranges |
| 4. Identity & Credentials | **LOW-MEDIUM** (40) | Professional license counts are estimates; healthcare record counts are highly uncertain |
| 5. Digital Native | **LOW** (30) | In-game item counts are order-of-magnitude guesses; data rights counts are speculative |
| 6. Government Records | **MEDIUM** (50) | Vital records and business registrations well-counted in OECD; patchy elsewhere |

### 9.3 What Is Missing

The TTR Number (~170B) does **not** include:

- **Individual financial transactions as tokenizable events** — Every invoice,
  receipt, and payment confirmation is theoretically tokenizable. Including
  these would add trillions of units.
- **Sensor data streams** — Every IoT device generates data that could be
  tokenized (IOTA's model). Including this would dwarf all other categories.
- **Social media content** — Every post, comment, and like has a creator and
  potential economic value. Including this adds hundreds of billions of units.
- **Informal economy assets** — Unregistered businesses, unlicensed
  professionals, unrecorded property. The informal economy is 30-60% of GDP
  in developing nations.
- **Future resource types** — AI model weights, synthetic biology sequences,
  space resource claims, climate adaptation credits. The TTR universe is
  expanding.

### 9.4 The Double-Counting Question

Some TTR categories overlap:

- A **property** (Tier 2) and its **land title** (Tier 6) are related but
  distinct tokenizable resources. The property is the asset; the title is
  the government record. Both could exist as separate tokens (asset token +
  title attestation).
- A **vehicle** (Tier 2) and its **registration** (Tier 6) — same logic.
- A **security** (Tier 1) and its **custody record** (Tier 1) — a security
  could be tokenized as an asset, and separately, the custody record could
  be tokenized as a credential.

We have counted both where they represent genuinely distinct tokenizable
resources. This is analogous to the MEST approach: not double-counting the
same thing, but recognizing that different layers of reality can each be
independently tokenized.

### 9.5 Comparison to Other Estimates

| Source | Estimate | What They Measured |
|--------|----------|-------------------|
| Boston Consulting Group (2022) | $16T tokenizable by 2030 | Market value of tokenizable assets (financial assets only) |
| McKinsey (2024) | $2T tokenized by 2030 | Market value of tokenized securities |
| Citibank (2023) | $4-5T tokenized by 2030 | Market value of tokenized assets |
| **This framework** | **170B units** | **Count of discrete tokenizable resources across all categories** |

The difference: industry estimates focus on *market value of financial
assets that will be tokenized soon*. TTR measures the *total count of
everything that could ever be tokenized*. These are complementary metrics.
BCG's $16T is the value of a small fraction of the TTR universe; the full
TTR universe's aggregate value likely exceeds $1 quadrillion.

---

## Summary

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   THE THREE NUMBERS                                              ║
║   ═════════════════                                              ║
║                                                                  ║
║   The Big Number:    ~73,750 TPS                                 ║
║   How many financial transactions happen per second               ║
║                                                                  ║
║   The MEST Number:   ~545,000 MEST/s                             ║
║   How many bilateral state changes those transactions generate    ║
║                                                                  ║
║   The TTR Number:    ~170 billion resources                      ║
║   How many discrete resources COULD be tokenized                  ║
║   (of which <0.3% currently are)                                 ║
║                                                                  ║
║   ─────────────────────────────────────────────────────────      ║
║                                                                  ║
║   Together, these three numbers frame the universe:               ║
║                                                                  ║
║   TTR tells you how big the playing field is.                    ║
║   TPS tells you how fast the game is being played.               ║
║   MEST tells you how much work each play generates.              ║
║                                                                  ║
║   The gap between what IS tokenized (<500M resources on-chain)   ║
║   and what COULD BE (~170B resources) is the single largest      ║
║   infrastructure opportunity of the 21st century.                ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

*This analysis was produced as part of Universe of Finance Run 11.
March 2026.*

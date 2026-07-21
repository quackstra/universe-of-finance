---
title: "Recruiter Overview"
parent: SLE Profiles
grand_parent: Explore
nav_order: 100
---

# Intergalactic Recruiter — Soul Less Employee Framework

> "The right question, asked by the right mind, with the right tools."

## What This Is

The Intergalactic Recruiter maintains a roster of **Soul Less Employees (SLEs)** — expert personas grounded in real job descriptions from the world's top financial data organizations. Each SLE embodies the mental models, tools, data sources, and analytical instincts of a specific domain expert.

When an Elf is dispatched to research a category, it consults this framework to determine **which expert(s) would be best at answering that specific question**, then adopts their perspective.

## Why It Works

A payments economist at the BIS and a crypto forensics analyst at Chainalysis approach "how many transactions happen daily?" from completely different angles — different data sources, different definitions of "transaction," different biases. By explicitly adopting the right persona, we:

1. **Ask better questions** — each SLE knows what to ask and where to look
2. **Avoid blind spots** — every SLE has documented biases that the Elf compensates for
3. **Triangulate naturally** — multi-SLE dispatch forces cross-validation between perspectives
4. **Ground in reality** — personas are built from real job descriptions, not abstract archetypes

---

## The Roster

| # | Slug | Role Title | Primary Sectors | Confidence Impact |
|---|------|-----------|----------------|-------------------|
| 1 | `payments-network-analyst` | Payment Network Data Analyst | Payments | High — covers #1 TPS category |
| 2 | `central-bank-economist` | Central Bank Payments Economist | Payments, Banking | High — covers #3 and #5 TPS categories |
| 3 | `market-microstructure-analyst` | Exchange & Market Structure Analyst | Traditional Finance | Medium — covers ETD, equities |
| 4 | `post-trade-specialist` | Post-Trade & Settlement Specialist | Banking, Traditional Finance | Medium — covers settlement, clearing |
| 5 | `fixed-income-specialist` | Fixed Income & Money Market Specialist | Traditional Finance | High — lowest-confidence TradFi |
| 6 | `forex-specialist` | Foreign Exchange Market Analyst | Traditional Finance | High — genuinely opaque category |
| 7 | `crypto-forensics-analyst` | Crypto Analytics & Forensics Specialist | Digital Assets | High — wash trading is the key uncertainty |
| 8 | `digital-wallets-analyst` | Digital Payments & Wallet Analyst | Payments | High — covers #2 TPS category |
| 9 | `market-research-analyst` | Payments & Commerce Market Researcher | Cross-cutting | Critical — overlap analysis arbiter |
| 10 | `government-statistician` | Government Finance & Public Sector Statistician | Government | Medium — single-category specialist |
| 11 | `gaming-economy-analyst` | Gaming & Virtual Economy Analyst | Gaming | Low — well-sized but niche |
| 12 | `emerging-tech-forecaster` | Emerging Tech & Machine Economy Forecaster | Emerging | High — lowest-confidence categories |
| 13 | `rwa-tokenisation-analyst` | Real-World Asset Tokenisation Analyst | Digital Assets, Traditional Finance | Medium — fastest-growing niche |
| 14 | `market-sizing-specialist` | Market Sizing & TAM Methodology Lead | **Cross-cutting (methodology)** | Critical — every category needs sizing |
| 15 | `measurement-standards-expert` | Financial Data Standards Specialist | **Cross-cutting (methodology)** | Critical — definition consistency across all categories |
| 16 | `statistical-methodologist` | Economic Measurement Methodologist | **Cross-cutting (methodology)** | Critical — confidence intervals and extrapolation for all estimates |
| 17 | `transaction-lifecycle-analyst` | Transaction Lifecycle & MEST Analyst | **Cross-cutting (MEST analysis)** | Critical — MEST multiplier estimation for all categories |
| 18 | `forensic-accountant` | Forensic Accountant & Financial Investigator | **Cross-cutting (opacity)** | Critical — opaque market volume estimation via proxy chains and fee-income analysis |
| 19 | `shadow-economy-economist` | Shadow Economy Economist & Illicit Finance Researcher | **Cross-cutting (opacity)** | Critical — informal sector sizing via MIMIC, currency demand, and trade misinvoicing |
| 20 | `academic-payments-economist` | Academic & Research Economist (Money, Payments & FMI) | **Cross-cutting (academia)** | High — grounds volume estimates in payment-demand theory and the peer-reviewed literature |
| 21 | `national-accounts-statistician` | National Accounts & Flow-of-Funds Statistician | **Cross-cutting (government)** | Critical — macro-consistency check: reconciles transaction totals against national financial accounts |
| 22 | `cbdc-digital-currency-researcher` | CBDC & Digital Currency Researcher | Digital Assets / Emerging | High — the flagged future category; retail/wholesale CBDC and tokenised settlement |

---

## Dispatch Matrix

### Category → SLE Routing

| Category | Primary SLE | Secondary SLE(s) |
|----------|-------------|-------------------|
| **Payments** | | |
| Consumer Cards | `payments-network-analyst` | `market-research-analyst` |
| Digital Wallets | `digital-wallets-analyst` | `payments-network-analyst`, `market-research-analyst` |
| Bank Transfers | `central-bank-economist` | `payments-network-analyst` |
| E-Commerce | `market-research-analyst` | `payments-network-analyst`, `digital-wallets-analyst` |
| P2P Transfers | `digital-wallets-analyst` | `central-bank-economist` |
| Remittances | `central-bank-economist` | `digital-wallets-analyst` |
| **Traditional Finance** | | |
| Equity Markets | `market-microstructure-analyst` | `post-trade-specialist` |
| ETD (Derivatives) | `market-microstructure-analyst` | `fixed-income-specialist` |
| Commodities | `market-microstructure-analyst` | `emerging-tech-forecaster` |
| Forex | `forex-specialist` | `central-bank-economist` |
| Fixed Income | `fixed-income-specialist` | `post-trade-specialist` |
| OTC Derivatives | `fixed-income-specialist` | `forex-specialist` |
| **Digital Assets** | | |
| CEX | `crypto-forensics-analyst` | `market-research-analyst` |
| DeFi | `crypto-forensics-analyst` | `rwa-tokenisation-analyst` |
| Stablecoins | `crypto-forensics-analyst` | `central-bank-economist` |
| L1/L2 Blockchain | `crypto-forensics-analyst` | `emerging-tech-forecaster` |
| **Banking** | | |
| Interbank RTGS | `central-bank-economist` | `post-trade-specialist` |
| Securities Settlement | `post-trade-specialist` | `market-microstructure-analyst` |
| **Gaming** | | |
| In-Game Microtransactions | `gaming-economy-analyst` | `market-research-analyst` |
| Game Sales | `gaming-economy-analyst` | `market-research-analyst` |
| **Government** | | |
| Government Payments | `government-statistician` | `central-bank-economist` |
| **Emerging** | | |
| IoT & M2M | `emerging-tech-forecaster` | `payments-network-analyst` |
| AI Agent Transactions | `emerging-tech-forecaster` | `crypto-forensics-analyst` |
| RWA Tokenisation | `rwa-tokenisation-analyst` | `fixed-income-specialist` |

### Cross-Cutting Methodology SLEs

The following three SLEs are **methodology specialists**, not category specialists. They are available as secondary SLEs for ANY category when the question involves their area of expertise. They do not replace category-specific SLEs — they augment them.

| Methodology SLE | Trigger | Role When Deployed |
|----------------|---------|-------------------|
| `market-sizing-specialist` | Any "size the market" or "what's the TAM?" question | Provides TAM/SAM/SOM framework, top-down vs. bottom-up reconciliation, proxy variable selection. Works alongside category primary to ensure sizing methodology is rigorous |
| `measurement-standards-expert` | Any "what counts as a transaction?" or "are these numbers comparable?" question | Provides transaction lifecycle mapping, double-counting rules, definitional alignment across sources. Ensures the category primary's count is based on a consistent, explicit definition |
| `statistical-methodologist` | Any "how confident are we?" or "how do we extrapolate from 60% coverage?" question | Provides confidence intervals, imputation methodology, coverage gap modeling, uncertainty quantification. Ensures the final estimate has a defensible uncertainty statement |

These three SLEs can be deployed individually or as a panel (see Methodology Review Protocol below).

### Opacity & Shadow Economy Dispatch (NEW — Run 12)

The following two SLEs are **opacity specialists** — forensic and economic researchers who estimate transaction volumes where conventional data sources fail. They are deployed when a category has low transparency, self-reported data of questionable reliability, or significant informal/shadow economy components.

| Opacity SLE | Trigger | Role When Deployed |
|------------|---------|-------------------|
| `forensic-accountant` | Any "the reported number doesn't add up" or "how do we verify opaque data?" question. Also: China, HFT, proprietary trading, off-balance-sheet vehicles, any category where fee income can proxy for transaction volume | Uses proxy chains (fee income → implied volume, settlement throughput → implied trades, regulatory filings → cross-reference). Applies Benford's Law, round-trip detection, and jurisdictional opacity gradients. Produces a triangulated estimate with explicit opacity discount |
| `shadow-economy-economist` | Any "how much activity is informal/unreported?" or "what's the shadow economy component?" question. Also: informal remittances, cash economy, underground banking, developing country opacity, HFT volume estimation | Uses MIMIC models, currency demand gaps, electricity consumption proxies, and trade misinvoicing analysis. Converts shadow economy GDP to transaction counts via sector-specific velocity. Produces a range estimate with ±20-30% inherent uncertainty |

**Key principle**: These SLEs deploy alongside category primaries, not in place of them. The category SLE provides the "official" estimate; the opacity SLEs estimate what's missing.

**Dispatch rules for opaque categories**:

| Category | Opacity SLE Assignment | Why |
|----------|----------------------|-----|
| Digital Wallets (China) | `forensic-accountant` | Ant/Tencent corporate-confidential data; PBOC aggregates need forensic decomposition |
| Foreign Exchange | `forensic-accountant` + `shadow-economy-economist` | BIS triennial = snapshot; daily transaction count is derived; informal FX in emerging markets |
| OTC Derivatives | `forensic-accountant` | Bilateral contracts; BIS notional outstanding ≠ transaction count; ISDA data gaps |
| Centralised Crypto Exchanges | `forensic-accountant` | Wash trading discount; offshore exchange opacity |
| Informal Remittances | `shadow-economy-economist` | Hawala, fei-qian, underground banking — entirely outside formal reporting |
| Cash Economy (new) | `shadow-economy-economist` | Currency demand method; formalization shock analysis |
| HFT / Dark Pools (new) | `forensic-accountant` + `market-microstructure-analyst` | Order flow internalization; FINRA ATS data; SEC Rule 605 |
| China (country-level) | `forensic-accountant` + `shadow-economy-economist` | Both formal opacity (corporate-confidential) and shadow banking |
| Private Credit / PE | `forensic-accountant` | No exchange reporting; fund-level transaction counts from AUM × turnover |

### Academia & Government Deepening (NEW — Run 14)

The following three SLEs deepen the roster's **academic** and **government-statistics**
pillars, which were previously thin relative to industry/consultancy sources. They
are cross-cutting: available as secondary SLEs for any category when their lens applies.

| SLE | Trigger | Role When Deployed |
|-----|---------|--------------------|
| `academic-payments-economist` | Any "what's the behavioural driver?" or "what does the literature say?" question. Also: card interchange / two-sided markets, cash-vs-digital substitution, velocity | Grounds a category estimate in a theory of payment demand and the peer-reviewed/working-paper literature. Challenges numbers that have no behavioural model behind them |
| `national-accounts-statistician` | Any "does this reconcile with the macro data?" or "how does this map to the financial accounts?" question. Also: sectoral decomposition, stock-flow consistency, gross-vs-net | Runs the macro-consistency check — reconciles aggregate transaction/value totals against flow-of-funds and SNA financial accounts. The definitional bridge between "payment" and "SNA financial transaction" |
| `cbdc-digital-currency-researcher` | Any CBDC, e-CNY, digital-euro, tokenised-deposit, or wholesale-settlement-DLT question | Estimates the emerging CBDC category, separating pilot from steady-state and cannibalisation from net-new. Fulfils the roster's own flagged need for a dedicated CBDC SLE |

**Key principle**: `academic-payments-economist` and `national-accounts-statistician`
are validation/grounding SLEs — they rarely lead a category but sharpen and sanity-check
its estimate. `cbdc-digital-currency-researcher` is a category primary for CBDC and a
secondary for stablecoins, bank transfers, and securities settlement (its migration targets).

### MEST Analysis Dispatch

**MEST = Mutual Economic State Transition**: any change to a holding of economically valuable assets where more than one party has a material interest in the record or accounting of that change and its result.

The `transaction-lifecycle-analyst` SLE is a **cross-cutting MEST specialist** that applies to ALL categories. Every transaction in the Big Number generates multiple MESTs downstream — the MEST Number captures the full cascade of bilateral state changes across the economy.

| When to Deploy | How to Deploy | What It Produces |
|---------------|---------------|-----------------|
| **MEST multiplier estimation** — for any category, estimate how many bilateral state transitions each transaction generates | Deploy `transaction-lifecycle-analyst` as secondary SLE alongside the category primary. The category SLE provides the transaction count; the lifecycle analyst maps the downstream cascade | A MEST multiplier range (e.g., "8-12x for equity trades") with documented lifecycle stages and party enumeration |
| **MEST-aware research runs** — when building or updating a category capsule | Add `transaction-lifecycle-analyst` to the SLE panel after the primary research is complete. The lifecycle analyst reads the capsule and adds a "MEST Analysis" section | A MEST section appended to the capsule: base multiplier, exception amplifier, regulatory tail, and total MEST estimate for the category |
| **Global MEST aggregation** — when computing the total MEST Number across all categories | Deploy `transaction-lifecycle-analyst` as lead, with `measurement-standards-expert` (for definition consistency) and `statistical-methodologist` (for confidence intervals) as secondary | The MEST Number: total bilateral state transitions per second across the global financial system, with uncertainty bounds |
| **Cross-category MEST comparison** — when comparing the operational intensity of different transaction types | Deploy `transaction-lifecycle-analyst` as lead with relevant category primaries | Comparative MEST multiplier table showing which categories generate the most downstream state changes per originating transaction |

**Key principle**: The `transaction-lifecycle-analyst` never replaces the category primary SLE. It always works alongside them. The category SLE knows the transaction count and market structure; the lifecycle analyst knows what happens after the trigger event and how many bilateral state changes cascade from it.

### Question-Type Routing

| Question Archetype | Lead SLE | Supporting SLE(s) |
|-------------------|----------|-------------------|
| "What is the transaction count for X?" | Category primary (see above) | Category secondary |
| "What % of volume is artificial/inflated?" | `crypto-forensics-analyst` | `market-research-analyst` |
| "How will X grow by 2030?" | `emerging-tech-forecaster` (emerging) / `market-research-analyst` (established) | Category primary |
| "What's the overlap between X and Y?" | `market-research-analyst` | Both category primaries |
| "What data sources exist for X?" | Category primary | `market-research-analyst` |
| "How does settlement/clearing work?" | `post-trade-specialist` | Category primary |
| "What's the regulatory outlook?" | `central-bank-economist` (payments/banking) / `government-statistician` (fiscal) | Category primary |
| "What's the real number behind opaque data?" | `forensic-accountant` | Category primary, `shadow-economy-economist` |
| "How much informal/shadow activity is there?" | `shadow-economy-economist` | `forensic-accountant`, Category primary |
| "Is this self-reported data reliable?" | `forensic-accountant` | Category primary, `statistical-methodologist` |
| "What's the underground/informal version of this?" | `shadow-economy-economist` | `forensic-accountant`, Category primary |
| "How does this compare across regions?" | `market-research-analyst` | Category primary |
| "How big is this market? What's the TAM?" | `market-sizing-specialist` | Category primary, `market-research-analyst` |
| "What counts as a transaction in X?" | `measurement-standards-expert` | Category primary |
| "How confident are we in this estimate?" | `statistical-methodologist` | Category primary, `market-sizing-specialist` |
| "How do we extrapolate from partial data?" | `statistical-methodologist` | `market-sizing-specialist`, Category primary |
| "Are these two numbers measuring the same thing?" | `measurement-standards-expert` | `statistical-methodologist` |
| "What's the methodology behind this number?" | `measurement-standards-expert` | `statistical-methodologist`, Category primary |
| "How many MESTs does this transaction generate?" | `transaction-lifecycle-analyst` | Category primary, `measurement-standards-expert` |
| "What's the MEST multiplier for this category?" | `transaction-lifecycle-analyst` | Category primary, `statistical-methodologist` |
| "What happens after the transaction is initiated?" | `transaction-lifecycle-analyst` | Category primary, `post-trade-specialist` |

---

## Multi-SLE Protocol

When a research question requires multiple SLEs:

1. **Lead expert frames the question** — the primary SLE defines what "transaction" means, which data sources are authoritative, and what the expected range is
2. **Secondary expert(s) provide specific inputs** — they contribute data points, alternative methodologies, or challenge assumptions from their domain
3. **Market Research Analyst arbitrates** — when lead and secondary disagree, the market-research-analyst resolves using cross-source triangulation
4. **Blind spots are cross-checked** — each SLE's documented biases are explicitly reviewed against the findings

## Methodology Review Protocol

When a category estimate is high-stakes (feeds into the headline UoF total) or low-confidence (score below 50), deploy the three methodology SLEs as a **Methodology Review Panel**. This is the measurement equivalent of a code review — the category specialist produces the estimate, and the panel stress-tests it.

### When to Convene the Panel

- **Mandatory**: Any category contributing >5% of the global TPS total (currently: Consumer Cards, Digital Wallets, Bank Transfers)
- **Mandatory**: Any category with confidence score below 50 after the primary research run
- **Recommended**: Any category where top-down and bottom-up estimates diverge by >25%
- **Recommended**: Any cross-category aggregation (e.g., "total global financial TPS") where double-counting risk is high
- **On request**: When a category SLE flags uncertainty about definitions, methodology, or data quality

### Panel Review Sequence

1. **`measurement-standards-expert` goes first** — Reviews the definition of "transaction" used by the category SLE. Checks: Is the counting point explicit (authorization vs. clearing vs. settlement)? Are double-counting rules stated? Are sources using consistent definitions? If not, the expert harmonizes definitions before any numbers are discussed

2. **`market-sizing-specialist` goes second** — Reviews the sizing methodology. Checks: Was both a top-down and bottom-up approach used? How large is the reconciliation gap? Are proxy variables documented with fidelity estimates? Is the growth rate decomposed into drivers or just a naked CAGR? If the methodology has gaps, the specialist identifies them and proposes fixes

3. **`statistical-methodologist` goes third** — Reviews the uncertainty quantification. Checks: What is the coverage fraction (what % of the market is directly observed)? How was the unobserved portion estimated? Is the confidence interval realistic (accounts for coverage error, not just sampling error)? Are imputation methods appropriate for the missing data pattern? The methodologist produces the final uncertainty statement

### Panel Output

The panel produces a **Methodology Review Note** appended to the research capsule, containing:

- **Definition audit**: Is "transaction" consistently defined? (Pass/Fail with notes)
- **Methodology audit**: Top-down/bottom-up reconciliation quality (Pass/Conditional/Fail)
- **Uncertainty audit**: Confidence interval realism (Pass/Conditional/Fail)
- **Revised confidence score**: Panel-adjusted confidence score (may be higher or lower than initial)
- **Action items**: Specific data collection or methodology improvements needed for the next run

A "Conditional" on any audit means the estimate is publishable with caveats. A "Fail" means the estimate needs rework before inclusion in the UoF total.

## When to Add a New SLE

Add a new SLE when:
- A new taxonomy category is added that doesn't map to any existing SLE's competencies
- An existing SLE covers too many disparate categories (>5 primary assignments)
- A confidence score stays below 40 after two research runs and the current SLE's tools/data sources are exhausted
- A major new data source emerges that requires specialized expertise to interpret (e.g., CBDC transaction data would need a dedicated SLE)

## Integration with Elf Pipeline

```
Scout → Architect → [RECRUITER dispatch] → Elf (with SLE persona) → Publish
                           ↓
                    Read SOUL.md for:
                    - Activation phrase (prepend to research prompt)
                    - Data sources (prioritized lookup order)
                    - Mental models (analytical lens)
                    - Blind spots (explicit bias check)
```

The Elf reads the primary SLE's SOUL.md and adopts that persona's perspective. For multi-SLE questions, it reads both and synthesizes. The SLE's "Blind Spots" section acts as a built-in adversarial check.

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
| "What's the real number behind opaque data?" | Category primary (triangulation lead) | `market-research-analyst` + nearest adjacent SLE |
| "How does this compare across regions?" | `market-research-analyst` | Category primary |

---

## Multi-SLE Protocol

When a research question requires multiple SLEs:

1. **Lead expert frames the question** — the primary SLE defines what "transaction" means, which data sources are authoritative, and what the expected range is
2. **Secondary expert(s) provide specific inputs** — they contribute data points, alternative methodologies, or challenge assumptions from their domain
3. **Market Research Analyst arbitrates** — when lead and secondary disagree, the market-research-analyst resolves using cross-source triangulation
4. **Blind spots are cross-checked** — each SLE's documented biases are explicitly reviewed against the findings

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

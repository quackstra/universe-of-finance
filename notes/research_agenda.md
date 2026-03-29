# Research Agenda — Next Run (Run 10)

> Updated 2026-03-29 after completing Run 9 (MEST Advantage + Brazil/EU + panel review + site polish).

## Status: Run 9 Complete

MEST Advantage paper published (DLT compression thesis). Brazil deep dive (Pix #2, 6.3% global TPS).
EU deep dive (18.2% global TPS, TIPS +402% YoY). Top-3 methodology panel review completed.
Confidence uplift: ATM 52→58, Insurance 52→57, Payroll 53→59. About page and cross-cutting index added.
5 country/region deep dives now complete (India, China, USA, Brazil, EU).

## What Run 10 Should Target

### Tier 1: Publication & Polish

1. **Executive Summary** — One-page findings document with Big Number, MEST Number, key charts.
   Target audience: financial regulators, infrastructure builders, DLT skeptics.
   Should stand alone as a shareable PDF.

2. **Data Dictionary** — Document every field in the data.json schema. Machine-readable.
   Powers future API/dashboard work.

3. **Methodology Paper** — Formal write-up of triangulation-first approach, MEST framework,
   overlap de-duplication rules. Citable format.

### Tier 2: New Deep Dives

4. **Japan deep dive** — 3rd largest economy, unique payment culture (cash-heavy but
   rapidly digitizing), JPX derivatives, JGB market, PayPay adoption.

5. **UK deep dive** — Faster Payments pioneer, CHAPS/BACS, FCA regulatory data,
   London as FX/derivatives hub. Strong data availability.

6. **Africa deep dive** — M-Pesa as original mobile money, fragmented but growing.
   Kenya, Nigeria, South Africa. Mobile money ≠ digital wallet distinction.

### Tier 3: MEST Extensions

7. **MEST by country** — Apply multipliers to all 5 deep-dive countries.
   India's MEST advantage (simpler UPI stack = lower multiplier).
   Create MEST leaderboard by country.

8. **MEST cost modeling** — Extend MEST Advantage paper with real cost data.
   Visa interchange + scheme fees per MEST vs. on-chain gas per MEST.
   Build the cost-per-MEST comparison table.

9. **MEST regulatory load** — Quantify how regulation drives MEST growth.
   KYC/AML reporting creates MESTs. MiCA vs. no-regulation MEST differential.

### Tier 4: Confidence & Data Quality

10. **AI Agent Transactions** (conf: 34) — Still the weakest. Consider splitting into
    "measured" (x402, Stripe agent billing) vs. "projected" tiers.

11. **In-Game Microtransactions** (conf: 44) — Publishers report revenue not counts.
    Epic Games Store + Roblox quarterly reports may yield transaction counts.

12. **Bill Payments** (conf: 48) — No single global source. Bottom-up from:
    utility connections (IEA), telecom subs (GSMA), streaming subs (platforms).

### Tier 5: Interactive Dashboard Updates

13. **Dashboard v2** — Add Brazil and EU to country spotlight cards.
    Add MEST Advantage visualization (compression waterfall chart).
    Add version history link in footer.

14. **Payment Stack Visualization** — Show how commerce layers stack on payment rails.
    Interactive Sankey or waterfall showing overlap flows.

15. **Category Explorer** — Click any category → see methodology, data sources,
    confidence breakdown, time-series chart, MEST cascade.

## Data Sources to Investigate

- **Epic Games Store / Roblox 10-K** — Microtransaction counts
- **JPX Annual Report** — Japan derivatives + equity volumes
- **Bank of Japan Payment Statistics** — Japan payment infrastructure
- **PayPay investor materials** — Japan mobile payments adoption
- **FCA Payment Statistics** — UK payment volumes
- **BACS/Faster Payments annual data** — UK real-time payments
- **Central Bank of Kenya** — M-Pesa transaction data
- **CBN (Nigeria)** — NIP instant payment volumes
- **SARB (South Africa)** — Payment system statistics
- **Visa/Mastercard 10-K** — Per-MEST cost derivation

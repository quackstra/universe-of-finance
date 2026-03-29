# Research Agenda — Next Run (Run 8)

> Updated 2026-03-29 after completing Run 7 (MEST framework + deep dives + confidence uplift).

## Status: Run 7 Complete

MEST framework established (~545K/s, 7.4× Big Number). India deep dive (17.4% of global TPS).
China opacity mapped (±6K TPS uncertainty). Sunset Watch built. Bottom 5 confidence scores
improved (bill payments +12 to 60, payroll +5 to 53, microtx +5 to 60, govt +5 to 65, AI agents +4 to 42).
17 SLEs operational including MEST-specialized transaction lifecycle analyst.

## What Run 8 Should Target

### Tier 1: MEST Deep Dives

1. **MEST multiplier validation** — The current multipliers are modeled. Validate against real clearing/settlement data:
   - Visa VisaNet processing stats (auth + clearing + settlement legs per transaction)
   - DTCC settlement-to-trade ratios
   - CLS daily settlement counts vs. FX trade counts
   - On-chain transaction traces (DeFi composability = observable MEST cascades)

2. **MEST by country** — Apply MEST multipliers to India and China deep dives. India's MEST advantage (simpler UPI stack = lower multiplier per txn). China's potential MEST hidden volume.

3. **MEST time-series** — Has the MEST multiplier changed over time? Real-time settlement (UPI, FedNow) reduces MESTs vs. batch (ACH). Crypto eliminates intermediary MESTs. Trend: is the world getting more or less MEST-intensive?

### Tier 2: Confidence Uplift (remaining sub-50 categories)

4. **AI Agent Transactions** (conf: 42) — Still the weakest. Need to decide: keep in Big Number as "pre-market" or create a separate "Emerging/Speculative" tier?

5. **Payroll** (conf: 53) — ADP processes 1 in 6 US private-sector paychecks. Their 10-K has run counts. Expand with Paychex, Gusto (combined: ~50% of US market).

6. **ATM Withdrawals** (conf: 52) — ATMIA global data. RBI publishes detailed India ATM stats. ECB Blue Book for Europe.

7. **Insurance Premiums** (conf: 52) — Swiss Re sigma gives premium VALUE. Need transaction COUNT from IRDAI (India), NAIC (US), EIOPA (EU).

### Tier 3: New Deep Dives

8. **USA deep dive** — India is 17.4% of TPS; what's the US? Card-heavy, ACH-heavy, dominant in TradFi. Build the mirror of the India capsule.

9. **Brazil deep dive** — Pix is the #2 real-time payment system globally. Brazil's market structure is unique (high banking concentration + Pix disruption).

10. **EU deep dive** — SEPA unification, PSD2/PSD3 impact, TARGET2 volumes. Fragmented but well-documented.

### Tier 4: The Payment Stack Visualization

11. **Payment Stack diagram** — Show how commerce-layer categories (e-commerce, gaming, insurance, BNPL, bills) stack on top of payment-rail categories (cards, bank transfers, wallets). Quantify each layer. This is the key visual for explaining overlaps.

12. **MEST Cascade Visualizer** — Interactive or detailed static version showing how a single transaction in each category cascades through the financial system.

### Tier 5: Publication Preparation

13. **Executive summary** — One-page findings document with both Big Number and MEST Number.

14. **Methodology paper** — Formal write-up leveraging 29 METHODOLOGY.md files + MEST framework.

15. **Data dictionary** — Document every field in data.json schema.

## Data Sources to Investigate

- **Visa VisaNet stats** — Auth + clearing + settlement counts for MEST validation
- **DTCC Annual Report** — Settlement-to-trade ratios
- **CLS Settlement Statistics** — FX MEST validation
- **ADP 10-K / Paychex 10-K** — Payroll run counts
- **ATMIA Global ATM Market** — ATM transaction trends
- **Swiss Re sigma + IRDAI** — Insurance transaction counts
- **Pix statistics (BCB)** — Brazil real-time payments
- **ECB Blue Book** — EU payment statistics
- **Federal Reserve Payments Study** — US payments landscape

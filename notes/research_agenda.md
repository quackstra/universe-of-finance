# Research Agenda — Next Run (Run 7)

> Updated 2026-03-28 after completing Run 6 (methodology overhaul + measurement SLEs + reconciliation).

## Status: Run 6 Complete

29 categories with full METHODOLOGY.md files including triangulation visuals. 16 SLEs (13 domain + 3 methodology). Big Number reconciled to ~73,750 TPS. Global + 7 sector methodology docs complete. Depth research on 4 weakest categories done.

## What Run 7 Should Target

### Tier 1: Confidence Uplift (weakest categories still below 50)

1. **AI Agent Transactions** (conf: 34) — Still the weakest. Need primary data from x402 protocol, Stripe agent billing API, actual measured volumes rather than projections. Consider whether this category should be flagged as "pre-market" and excluded from the Big Number.

2. **Payroll** (conf: 35) — ADP processes ~1 in 6 US private-sector paychecks. Their quarterly reports + BLS data could anchor a much better US estimate. Expand internationally via ILO + Eurostat.

3. **In-Game Microtransactions** (conf: 44) — Apple/Google app store review data could provide hard platform transaction counts. Sensor Tower or data.ai as alternatives.

4. **Bill Payments** (conf: 48) — India BBPS is a goldmine (centralized, publishes stats). UK BACS Direct Debit gives excellent UK data. EU SEPA DD volumes are BIS-published.

5. **Tax & Government Payments** (conf: 50) — India GST portal, US IRS e-file statistics, UK HMRC self-assessment filing counts. Bottom-up from tax authority digital stats.

### Tier 2: Cross-Category Deep Dives

6. **India deep dive** — India appears in nearly every category's top list. Build a country-level capsule showing India's contribution across all categories (UPI, NSE, RuPay, GST, BBPS).

7. **China opacity report** — Quantify what we don't know about China across all categories. Extend the digital wallets China model to other sectors.

8. **Declining categories analysis** — ATM is declining at -3% CAGR. Are others? Check/cheque payments, cash-on-delivery, traditional wire transfers. Build a "sunset watch" list.

### Tier 3: Methodology Review Panel Deployment

9. **Panel review of top 3 TPS contributors** — Consumer Cards, Digital Wallets, Bank Transfers account for ~80% of global TPS. Deploy the full 3-SLE Methodology Review Panel for each. These are mandatory per the panel protocol.

10. **Panel review of categories below conf:50** — Mandatory per protocol. AI agents, payroll, in-game microtx, bill payments need formal panel review.

### Tier 4: Presentation & Tooling

11. **Update charts.py** — Add time-series chart, peak TPS calendar heatmap, overlap Sankey diagram.

12. **Interactive dashboard** — Web-based Big Number visualization with drill-down capability.

13. **Automated pipeline** — Single script that runs big_number + confidence_score + data_freshness + validate_schema.

14. **Category comparison tool** — Side-by-side comparison of any two categories.

### Tier 5: Publication

15. **Executive summary** — One-page findings summary suitable for external sharing.

16. **Methodology paper** — Formal write-up leveraging the new METHODOLOGY.md files and visual template.

17. **Data dictionary** — Document every field in data.json schema for downstream consumers.

## Data Sources to Investigate

- **x402 Protocol Metrics** — AI agent transaction data
- **India BBPS** — Bharat Bill Payment System (centralized bill payment data)
- **Apple App Store / Google Play Console** — In-app purchase statistics
- **India GST Portal** — Tax transaction data
- **ADP Quarterly Reports** — Payroll transaction volumes
- **UK BACS/FPS Statistics** — Direct debit and faster payment data
- **Sensor Tower / data.ai** — Mobile gaming transaction analytics
- **ILO ILOSTAT** — Global employment data for payroll modeling

# Research Agenda — Next Run (Run 6)

> Updated 2026-03-28 after completing Run 5 (new categories + time-series + peak/scenarios).

## Status: Run 5 Complete

29 categories (5 new). Time-series 2015-2025 built. Peak TPS and scenario analysis done.
Repo deep dive, CEX regional model, retail forex aggregation, equity OTC model complete.
Gaming overlap quantified (82% already counted). Intergalactic Recruiter operational.

## What Run 6 Should Target

### Tier 1: Reconciliation & Big Number Update (CRITICAL)

1. **Re-run big_number.py with 29 categories** — Current Big Number (~70,741) is based on 24 categories. Need to add 5 new categories with proper overlap deductions. Also incorporate: revised repo (+135M txns), revised CEX wash (20.6%), revised retail FX (8M/day), revised equity OTC (1.2M).

2. **Update OVERLAP_MATRIX.md** — Add gaming overlap quantification (82%), new category overlaps (insurance 90%, BNPL 100% infrastructure, bill payments 90%, payroll 90%, ATM 0%).

3. **Update README.md** — Expand to 29-category leaderboard. Update Big Number.

4. **Update TAXONOMY.md** — Add 5 new categories formally.

5. **Re-run confidence_score.py** — Score the 5 new categories and refresh all 29.

### Tier 2: Depth on Weakest Categories

6. **AI Agent Transactions** (confidence 34) — x402 protocol data, Stripe agent billing, OpenAI function calling volume estimates. This is the most speculative category.

7. **In-Game Microtransactions** (confidence 44) — Publisher-level data mining. Apple/Google app store review data could help.

8. **Tax & Government Payments** (confidence 50) — India GST portal data, US IRS e-file statistics, UK self-assessment data. Bottom-up from tax authority digital stats.

9. **Payroll** (confidence 35) — ADP quarterly reports, Paychex data, UK RTI/PAYE data, EU payroll provider data.

10. **Bill Payments** (confidence 48) — India BBPS is a goldmine (centralized bill payment data). UK BACS Direct Debit stats. EU SEPA DD volumes.

### Tier 3: Cross-Category Analysis

11. **The Payment Stack visualization** — Show how commerce-layer categories (e-commerce, gaming, insurance, BNPL, bills) stack on top of payment-rail categories (cards, bank transfers, wallets). Quantify each layer.

12. **India deep dive** — India appears in nearly every category's top list. Build a country-level capsule showing India's contribution to global TPS across all categories.

13. **China opacity report** — Quantify what we don't know about China across all categories. Extend the digital wallets China model to other categories.

14. **Declining categories analysis** — ATM withdrawals are declining. Are any others? Fixed income cash bond trading? Check/cheque payments? Build a "sunset watch" list.

### Tier 4: Presentation & Tooling

15. **Update charts.py** — Add time-series chart, peak TPS calendar heatmap, overlap Sankey diagram.

16. **Interactive dashboard** — Web-based Big Number visualization with drill-down.

17. **Automated pipeline** — Script that runs big_number + confidence_score + data_freshness + validate_schema in one command.

18. **Category comparison tool** — Given two categories, show side-by-side: TPS, value, growth rate, confidence, overlap.

### Tier 5: Publication Preparation

19. **Executive summary** — One-page summary of all findings suitable for external sharing.

20. **Methodology paper** — Formal write-up of the measurement methodology, overlap deduction approach, and confidence scoring.

21. **Data dictionary** — Document every field in data.json schema for downstream consumers.

## Data Sources to Investigate

- **x402 Protocol Metrics** — AI agent transaction data (for AI agents category)
- **India BBPS** — Bharat Bill Payment System (centralized bill payment data)
- **Apple App Store / Google Play Console** — In-app purchase statistics
- **India GST Portal** — Tax transaction data
- **ADP Quarterly Reports** — Payroll transaction volumes
- **UK BACS/FPS Statistics** — Direct debit and faster payment data

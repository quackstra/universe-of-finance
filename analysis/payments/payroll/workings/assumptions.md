# Payroll Payments — Assumptions

## A1. Employment Data

- **Global employment (2024)**: ~3.50 billion (ILO WESO 2024). This includes all employed persons aged 15+.
- **Wage and salaried workers**: ~1.90 billion globally (ILO 2021 projection). The remainder are self-employed, contributing family workers, or informal.
- **US nonfarm payroll**: 158.3M (BLS CES, December 2024)
- **EU-27 employed**: 197.6M (Eurostat, 2024 annual), of which 85.7% are employees
- **China urban employed**: ~470M estimated (NBS does not publish a clean payroll count; derived from urban employment statistics)
- **India formal sector**: ~120M based on EPFO registered workers + central/state government employees. The 440M informal workforce is excluded from electronic payroll counts.

## A2. Pay Frequency by Region

| Region | Primary Frequency | Source |
|--------|-------------------|--------|
| US | Biweekly (26/yr) — 70-75% of workers | APA / BLS |
| EU | Monthly (12/yr) — ~90% | Standard across EU labor law |
| UK | Monthly (12/yr) — ~85% | HMRC / BACS data |
| China | Monthly (12/yr) — ~95% | Standard; some factories weekly |
| India (formal) | Monthly (12/yr) — ~95% | Labor law mandates monthly |
| Japan | Monthly (12/yr) — ~98% | Standard |
| Latin America | Monthly (70%) / Biweekly (30%) | Mixed by country |
| Africa (formal) | Monthly — ~90% | Standard for formal sector |

## A3. Formal vs. Informal Split

- ILO estimates **58% of global employment is informal** (Women and Men in the Informal Economy, 2018, updated 2023)
- Informal workers are assumed to receive cash wages that do not generate electronic payment transactions
- However, cash wages are still counted as "payroll transactions" in this model for completeness — they represent real economic events even if invisible to payment systems

## A4. Cash Wage Treatment

Cash wages are counted in the total (41.2B) but flagged as non-overlapping with bank transfers. This is the only portion (~4.2B) that is incremental to the bank transfer category.

## A5. Self-Employment Exclusion

Self-employed individuals (~1.5B globally) do not receive payroll transactions from an employer. Their income comes from customers/clients and is captured in other payment categories (cards, bank transfers, cash).

## A6. Gig Economy Treatment

Gig workers (Uber, DoorDash, Deliveroo, etc.) receive per-task or weekly batch payments that resemble payroll but are technically contractor payments. These are **excluded** from this model and are partially captured in P2P transfers or bank transfers. Estimated ~100-200M gig workers globally.

## A7. Seasonality and Peak TPS

Payroll is the most calendar-driven payment category:
- **US**: ~70% of employers pay biweekly on Fridays. On a typical payday Friday, ~130M direct deposits are processed in a 4-hour ACH window.
- **EU/Asia month-end**: Last business day of month sees concentrated salary deposits.
- **13th-month pay**: Common in Philippines, Brazil, Netherlands — creates December spike.
- Peak multiplier set at **5.0x** average TPS due to extreme concentration.

## A8. Value Estimation

The $32T global wage bill estimate comes from ILO Global Wage Report data. This covers formal-sector wages only. Adding informal cash wages would increase the total but these are inherently unmeasurable at global scale.

Average payroll transaction value: $32T / 41.2B = ~$777 per transaction
- US average: ~$2,200 (biweekly gross, pre-tax withholdings)
- EU average: ~$2,800 (monthly net)
- China average: ~$1,100 (monthly, urban)
- India formal: ~$350 (monthly, formal sector)
- Global weighted: ~$777 reflects the downward pull of emerging market wages

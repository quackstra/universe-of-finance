# ATM Withdrawals — Assumptions

## A1. Withdrawal vs. Total ATM Transaction Split

The widely-cited "86.7 billion global ATM transactions" includes all ATM interactions:
- Cash withdrawals: ~57-60% (our focus)
- Balance inquiries: ~20-25%
- Deposits: ~8-10%
- Mini-statements: ~3-5%
- Bill payments / transfers: ~3-5%

We use **57% as the withdrawal share** for the top-down calibration, giving ~49.4B.
This is conservative — ATMIA has stated withdrawal share as high as 69% of "transaction revenue," but that metric weights by value rather than count.

## A2. Regional ATM Count Data

| Region | ATMs (2024) | Source |
|--------|-------------|--------|
| Global total | ~3.12M | Sci-Tech Today / World Bank (declining from 3.22M in 2023) |
| China | ~700K | Datos Insights (down from 1.1M in 2018) |
| US | ~470K | ATMIA (includes IAD ATMs) |
| EU-27 | ~266K | ECB (end of H2 2023, declining 0.4%/year) |
| India | ~215K | RBI |
| Japan | ~180K | BIS |
| Brazil | ~120K | BCB |

## A3. Transactions Per ATM

Global average: ~15,700 withdrawals per ATM per year (2024), down from ~18,500 at peak (2016).

This masks huge variation:
- India: ~27,900/ATM/year (high density, high usage)
- EU: ~28,200/ATM/year (moderate)
- US: ~6,600/ATM/year (very low — many lightly used IAD ATMs)
- China: ~17,100/ATM/year (declining rapidly)

## A4. US ATM Withdrawal Decline Rate

The Federal Reserve reported a -10.1% annual decline from 2018 to 2021 (5.1B to 3.7B).
We moderate this to -6% for 2021-2024, reflecting:
- Post-COVID cash usage partially rebounded
- Remaining ATM users are sticky (rural, unbanked, cash-preference)
- Mobile wallet adoption rate in US is slower than EU/Asia

This gives ~3.1B for US in 2024.

## A5. Average Withdrawal Value

The $157 figure from ATMIA is likely US-weighted. Our volume-weighted model suggests ~$99 globally. We report the ATMIA figure with the caveat that true global average is likely $100-160.

Key regional values:
- US $198 (up from $156 in 2018 — people withdraw more per trip as frequency drops)
- EU ~$140 (ECB data)
- India ~$40 (RBI; but rising 5% annually as larger withdrawals replace small ones)
- China ~$90 (declining usage but moderate per-withdrawal amounts)

## A6. Peak TPS Multiplier

ATM usage is less concentrated than payroll but still has patterns:
- Weekend peaks (payday + pre-leisure spending)
- Holiday eves (Diwali, Chinese New Year, Christmas Eve)
- Month-end clusters in monthly-pay economies

Peak multiplier: **2.0x average** — more spread out than payroll (5x) but more concentrated than card spending (2.5x).

## A7. COVID Impact Model

COVID lockdowns reduced ATM usage ~26% in 2020 (range: -20% US to -30% India).
Recovery was incomplete — 2023 was still ~19% below 2016 peak.
We assume COVID permanently shifted ~10-15% of ATM usage to digital channels, compounding the pre-existing digital displacement trend.

## A8. Emerging Market Growth

Africa and parts of South/Southeast Asia are still net-positive for ATM deployment:
- Egypt: major bank ATM rollout ongoing
- Uzbekistan: 1,000+ new ATMs in 2024
- Nigeria: financial inclusion driving growth despite mobile money

However, this growth is small relative to the developed-market decline.
Net global effect is still negative.

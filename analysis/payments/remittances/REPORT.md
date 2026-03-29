---
title: "Remittances — Report"
parent: Payments
grand_parent: Explore
nav_order: 6
---

# Remittances — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Global cross-border remittances reached an estimated **$905 billion in 2024**, with flows to low- and middle-income countries (LMICs) accounting for **$685 billion**. The transaction count is far harder to pin down — remittance providers generally report values, not counts. Based on available data from Western Union (~300 million annual transactions), Wise (~125 million), and extrapolation across the broader market, we estimate **~1.8 billion cross-border personal transfer transactions in 2024**, yielding approximately **57 TPS**. This makes remittances one of the lowest-TPS categories in the Payments sector by volume, but one of the highest by average transaction value (~$500).

The remittance market is undergoing a structural shift from cash-based agent networks (Western Union, MoneyGram) to digital-first platforms (Wise, Remitly, WorldRemit), with digital channels now handling over 50% of flows in many corridors.

## Scope

**Included:**
- Cross-border personal money transfers (worker remittances)
- Formal channels: banks, money transfer operators (MTOs), digital remittance platforms
- All corridors globally (South-North, South-South, North-South)

**Excluded:**
- Domestic P2P transfers (covered in P2P Transfers)
- Business-to-business cross-border payments (covered in B2B/Wholesale)
- Informal/hawala transfers (untracked by definition)
- Crypto remittances (estimated <2% of total; data unreliable)

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~57 | Derived from annual volume estimate | 🔴 Low |
| Peak TPS (est.) | ~100 | Holiday corridors (Eid, Christmas, Diwali) | 🔴 Low |
| Daily volume | ~4.9 million | Derived from annual | 🔴 Low |
| Annual volume (2024) | ~1.8 billion txns (est.) | Extrapolated from provider data | 🔴 Low |
| Annual value (2024) | $905 billion | [World Bank](https://blogs.worldbank.org/en/peoplemove/in-2024--remittance-flows-to-low--and-middle-income-countries-ar) | 🟢 High |
| Avg transaction size | ~$500 | Derived: $905B / 1.8B txns | 🟡 Medium |
| Avg cost (% of $200 txn) | 6.35% | [World Bank RPW](https://remittanceprices.worldbank.org/) | 🟢 High |

### Top Recipient Countries (2024)

| Country | Inflows ($B) | Source | Confidence |
|---------|-------------|--------|------------|
| India | $129 | World Bank | 🟢 High |
| Mexico | $68 | World Bank / Banxico | 🟢 High |
| China | $48 | World Bank | 🟡 Medium |
| Philippines | $40 | World Bank / BSP | 🟢 High |
| Pakistan | $33 | World Bank / SBP | 🟢 High |
| Bangladesh | $25 | World Bank | 🟡 Medium |
| Egypt | $24 | World Bank | 🟡 Medium |
| Nigeria | $20 | World Bank | 🟡 Medium |

### Provider Market Share (Estimated 2024)

| Provider | Est. Annual Txns (M) | Est. Annual Value ($B) | Channel | Confidence |
|----------|---------------------|----------------------|---------|------------|
| Western Union | ~300 | ~$135 | Agent + digital | 🟡 Medium |
| Wise | ~125 | ~$145 | Digital | 🟡 Medium |
| MoneyGram | ~100 | ~$50 | Agent + digital | 🔴 Low |
| Remitly | ~50 | ~$50 | Digital | 🔴 Low |
| WorldRemit | ~30 | ~$15 | Digital | 🔴 Low |
| Banks | ~400 | ~$300 | Bank wire | 🔴 Low |
| Other MTOs | ~795 | ~$210 | Mixed | 🔴 Low |
| **Total** | **~1,800** | **~$905** | | |

---

## Historic Trend

### Global Remittance Flows (Value)

| Year | Global Total ($B) | To LMICs ($B) | YoY Growth | Source |
|------|-------------------|---------------|------------|--------|
| 2019 | $715 | $549 | +2.7% | World Bank |
| 2020 | $717 | $556 | +0.3% | World Bank |
| 2021 | $791 | $605 | +10.3% | World Bank |
| 2022 | $831 | $626 | +5.1% | World Bank |
| 2023 | $865 | $656 | +4.1% | World Bank |
| 2024 | $905 | $685 | +4.6% | World Bank (est.) |

### Estimated Transaction Count (Global)

| Year | Est. Txns (billions) | Est. Avg Txn Size | Avg TPS | Confidence |
|------|---------------------|-------------------|---------|------------|
| 2019 | 1.30 | $550 | 41 | 🔴 Low |
| 2020 | 1.35 | $531 | 43 | 🔴 Low |
| 2021 | 1.45 | $546 | 46 | 🔴 Low |
| 2022 | 1.55 | $536 | 49 | 🔴 Low |
| 2023 | 1.65 | $524 | 52 | 🔴 Low |
| 2024 | 1.80 | $503 | 57 | 🔴 Low |

Note: Transaction count estimates assume declining average transaction size over time as digital channels enable smaller, more frequent transfers. This is a well-documented trend — digital remittance average transaction sizes are $200-300 vs. $500+ for traditional MTOs.

---

## Growth Rate Analysis

| Period | CAGR (Value) | CAGR (Est. Transactions) | Notes |
|--------|-------------|------------------------|-------|
| 2019-2024 (5yr) | 4.8% | 6.7% | Volume growing faster than value (smaller txns) |
| 2022-2024 (2yr) | 4.3% | 7.7% | Digital adoption accelerating txn count |
| COVID period 2020-2021 | 10.3% | 7.4% | Stimulus payments boosted sender capacity |

### Digital vs. Traditional
- Digital remittances are growing at ~20-25% CAGR (by value)
- Traditional agent-based remittances are declining at ~3-5% CAGR
- Digital share of total: ~15% in 2019 → ~40% in 2024 (estimated)

---

## Projections

### Baseline (4.5% value CAGR, 7% txn CAGR — digital shift continues)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($B) |
|------|----------------------|---------|-------------------|
| 2025 | 1.93 | 61 | $946 |
| 2027 | 2.20 | 70 | $1,034 |
| 2030 | 2.70 | 86 | $1,180 |
| 2035 | 3.78 | 120 | $1,475 |

### High Growth (6% value CAGR, 10% txn CAGR — rapid digitization)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($B) |
|------|----------------------|---------|-------------------|
| 2025 | 1.98 | 63 | $959 |
| 2027 | 2.40 | 76 | $1,078 |
| 2030 | 3.19 | 101 | $1,284 |
| 2035 | 5.14 | 163 | $1,718 |

### Conservative (3% value CAGR, 5% txn CAGR — regulatory friction)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($B) |
|------|----------------------|---------|-------------------|
| 2025 | 1.89 | 60 | $932 |
| 2027 | 2.08 | 66 | $989 |
| 2030 | 2.41 | 76 | $1,081 |
| 2035 | 3.08 | 98 | $1,253 |

---

## Key Findings

1. **Remittances are a value story, not a volume story.** At ~57 TPS, this is orders of magnitude below card networks or digital wallets. But the $905B annual value exceeds all foreign direct investment to LMICs and all official development aid combined.

2. **Transaction counts are the biggest data gap** in remittance research. The World Bank, which is the gold standard for remittance data, tracks values but not transaction counts. Our 1.8B estimate is derived from provider data and should be treated with low confidence.

3. **Digital is eating traditional.** Western Union's Q4 2024 results show digital transactions growing while overall transactions are flat-to-declining. Wise processes ~$145B at ~0.6% margin vs. Western Union's ~$135B at ~3%. The cost compression is real.

4. **Average transaction size is falling**, from ~$550 in 2019 to ~$500 in 2024 (estimated). Digital platforms enable smaller, more frequent transfers ($200-300 average) vs. traditional MTOs ($500+). This means transaction counts are growing faster than values.

5. **India is the remittance superpower**, receiving $129B in 2024 — nearly double the #2 recipient (Mexico, $68B). The US-India and Gulf-India corridors alone account for ~$80B.

6. **The G20's 3% cost target remains unmet.** The global average remittance cost is 6.35% for a $200 transfer (Q4 2024). Sub-Saharan Africa remains the most expensive corridor at ~7.9%. Digital channels average ~4.3%.

---

## Data Quality & Limitations

- **Value data is reliable (World Bank)** — The $905B figure comes from balance-of-payments data compiled by the World Bank's KNOMAD team. This is the global standard.
- **Transaction count is estimated** — No global authority tracks the number of remittance transactions. Our 1.8B figure is built bottom-up from provider disclosures and market share assumptions. Confidence is low.
- **Informal flows are excluded** — Hawala networks, hand-carried cash, and crypto remittances are not captured. The World Bank estimates true flows could be 50% larger than official figures.
- **Provider data is uneven** — Western Union (public) reports quarterly transactions. Wise (public) reports volume and revenue. MoneyGram (private since 2023) has limited recent disclosure.
- **Double-counting risk with P2P** — Some platforms (e.g., PayPal, Cash App) enable cross-border transfers that may be counted in both P2P and Remittances depending on the sender's intent.
- **"Remittance" definition varies** — Some sources include all personal cross-border transfers; others only count worker remittances (compensation of employees abroad). We use the broader definition.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Global remittance transaction count.** The World Bank tracks value ($905B) but not transaction count. Our 1.8B estimate is the weakest figure in the entire payments taxonomy — built from provider extrapolations with low confidence.
- **Informal/hawala transfer volume.** The World Bank estimates informal flows could be 50% of formal flows, which would imply true remittances of ~$1.35T and ~2.7B transactions. This is fundamentally unobservable.
- **Average transaction size by corridor.** The global average (~$500) masks enormous variation: US-Mexico average is ~$390 (Banxico data), Gulf-India is ~$250, while UK-Nigeria may be ~$800+. Corridor-level data is sparse.
- **Digital vs. traditional share by transaction count.** Digital is ~40% by value, but digital transactions are smaller ($200-300 avg) vs. traditional ($500+). By count, digital may already be >50%.
- **MoneyGram data post-privatization.** Since going private in 2023 (acquired by Madison Dearborn), MoneyGram no longer files public financials. Its ~$50B volume and ~100M transaction estimates are increasingly stale.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Global transaction count | Method 1: $905B / $500 avg = 1.81B. Method 2: Sum known providers (WU 300M + Wise 125M + banks 400M + others 975M). Method 3: Use corridor-level data from World Bank RPW to build bottom-up count. | World Bank RPW (200+ corridors); WU quarterly reports; Wise annual report | 🔴 |
| Informal flows | Compare official BoP remittance data with household survey data on received transfers. The gap = informal. IMF has done this for select corridors (India, Philippines, Pakistan). | IMF household surveys; World Bank bilateral estimates; Dilip Ratha research papers | 🔴 |
| Average txn size by corridor | Banxico publishes US-Mexico average ($390). SBP publishes Pakistan inflow data. RBI publishes India corridor data. Assemble 10-15 major corridors to build weighted global average. | Banxico monthly remittance data; SBP monthly stats; RBI Annual Report; BSP (Philippines) OFW stats | 🟡 |
| Digital share by count | Wise (125M txns, ~$145B value, $1,160 avg) is 100% digital. WU digital is ~40% of transactions. Remitly/WorldRemit are 100% digital. Weight by market share. | Wise annual report; WU quarterly: digital ~40% of C2C transactions; Remitly S-1 (2021) | 🟡 |
| Cost reduction trajectory | World Bank RPW publishes quarterly average cost by corridor. Extrapolate cost decline rate to estimate when 3% G20 target is reached. | World Bank RPW: 6.35% global average; Sub-Saharan Africa 7.9%; South Asia 4.3% | 🟢 |

### Key Modeling Questions
- The World Bank's $905B figure is derived from balance-of-payments data (central bank reporting). This captures formal bank and MTO flows but may miss digital-native platforms that route through novel corridors (e.g., Wise's multi-currency accounts, crypto-bridged remittances). Is the $905B an undercount?
- If digital remittance average transaction size ($250) continues converging toward P2P averages ($120-290), do remittances become indistinguishable from cross-border P2P transfers? At what point does the category boundary dissolve?
- Western Union's strategic pivot from agent networks to digital: if WU's agent revenue declines faster than digital grows, could there be a net reduction in formal remittance volume as senders shift to informal digital channels (WhatsApp-mediated hawala, crypto)?
- SWIFT gpi (global payments innovation) is reducing cross-border bank transfer costs. If bank wire remittances become competitive with MTOs at the <$1,000 level, could banks recapture remittance share?

### Reference Comparisons
- **India's inflows by channel:** India receives $129B in remittances. RBI data shows ~75% arrives via bank wire (SWIFT), ~15% via digital platforms, ~10% via traditional MTOs. This is unusual — most LMIC remittance corridors are MTO-dominated. India's high bank penetration (Jan Dhan accounts: 530M) explains this.
- **Mexico vs. Philippines per-capita remittances:** Mexico receives $68B for 130M people (~$523/capita); Philippines receives $40B for 115M people (~$348/capita). But remittances are 8.5% of Philippine GDP vs. 3.9% of Mexican GDP — the Philippines is more remittance-dependent despite lower per-capita inflows.
- **Cost corridor extremes:** Sending $200 from South Africa to Botswana costs ~20% in fees; sending $200 from Singapore to India costs ~2.7%. This 7.4x cost differential on similar-distance corridors reflects market competition, not geography.
- **Crypto remittance test case:** El Salvador's Bitcoin remittance experiment showed <2% of remittances used Bitcoin in 2024, despite government promotion. This suggests crypto remittances remain a niche use case, not a systematic undercount in official figures.

---

## Sources

1. [World Bank — Remittance flows to LMICs reach $685 billion in 2024](https://blogs.worldbank.org/en/peoplemove/in-2024--remittance-flows-to-low--and-middle-income-countries-ar)
2. [World Bank — Remittances Slowed in 2023, Expected to Grow in 2024 (June 2024 press release)](https://www.worldbank.org/en/news/press-release/2024/06/26/remittances-slowed-in-2023-expected-to-grow-faster-in-2024)
3. [World Bank Remittance Prices Worldwide](https://remittanceprices.worldbank.org/)
4. [World Bank Open Data — Personal remittances received](https://data.worldbank.org/indicator/BX.TRF.PWKR.CD.DT)
5. [Migration Data Portal — Remittances overview](https://www.migrationdataportal.org/themes/remittances-overview)
6. [Western Union Q4/FY2024 Results](https://www.businesswire.com/news/home/20250204893052/en/Western-Union-Reports-Fourth-Quarter-and-Full-Year-2024-Results)
7. [FXC Intelligence — Remittances and money transfers 2024 year in data](https://www.fxcintel.com/research/reports/ct-remittances-money-transfers-2024-year-in-data)
8. [Federal Reserve — Global Remittances Cycle (Feb 2025)](https://www.federalreserve.gov/econres/notes/feds-notes/global-remittances-cycle-20250227.html)
9. [GPFI — 2024 Update on Progress Towards G20 Remittance Target](https://www.gpfi.org/sites/default/files/NEW%202024%20Update%20to%20Leaders%20on%20Progress%20Towards%20the%20G20%20Remittance%20Target.pdf)
10. [William Blair — Money Remittances: 2024 report](https://www.williamblair.com/-/media/downloads/eqr/2025/williamblair-money-remittances.pdf)
11. [Precedence Research — Remittance Market Forecast to $1T by 2035](https://www.businessresearchinsights.com/market-reports/remittance-market-110452)
12. [Grand View Research — Digital Remittance Market to $60B by 2030](https://www.grandviewresearch.com/press-release/global-digital-remittance-market)

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

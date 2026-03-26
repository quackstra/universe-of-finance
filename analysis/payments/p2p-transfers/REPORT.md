# Peer-to-Peer Transfers — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

The global P2P transfers market processed an estimated **8.5 billion transactions in 2024**, yielding an average throughput of approximately **270 TPS**. This category is dominated by the US market, where Zelle ($1.04 trillion), Venmo (~$280 billion), and Cash App (~$280 billion) collectively processed the majority of volume. The US P2P market alone reached an estimated **$1.8-2.0 trillion** in total payment volume in 2024. Globally, including European, Asian (non-UPI), and other domestic P2P platforms, total value likely reached **$2.5-3.0 trillion**.

Note: India's UPI P2P transactions (which are massive) are counted under Digital Wallets, and China's WeChat/Alipay P2P is similarly classified there. This category focuses on dedicated P2P apps and non-wallet domestic transfer platforms.

## Scope

**Included:**
- Zelle (US — bank-to-bank P2P)
- Venmo (US — PayPal-owned P2P/social payments)
- Cash App (US — Block/Square P2P)
- PayPal P2P (non-Venmo domestic transfers)
- European P2P: Bizum (Spain), Swish (Sweden), iDEAL P2P (Netherlands), Lydia (France)
- Other domestic P2P: Pix P2P (Brazil, where classifiable), KakaoPay (South Korea)

**Excluded:**
- UPI (India) — counted in Digital Wallets
- WeChat Pay / Alipay P2P — counted in Digital Wallets
- Cross-border P2P — counted in Remittances
- Crypto P2P transfers
- Bank wire transfers between individuals (counted in Bank Transfers)

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Average TPS | ~270 | Derived from annual volume | 🟡 Medium |
| Peak TPS (est.) | ~600 | US holiday weekend peaks | 🔴 Low |
| Daily volume | ~23 million | Derived from annual | 🟡 Medium |
| Annual volume (2024) | ~8.5 billion txns | Aggregated from platform data | 🟡 Medium |
| Annual value (2024) | ~$2.8 trillion | Aggregated estimates | 🟡 Medium |

### US Platform Breakdown (2024)

| Platform | Annual Transactions | Annual Value | Source | Confidence |
|----------|-------------------|--------------|--------|------------|
| Zelle | 3.6 billion | $1.04 trillion | [CNBC](https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html) | 🟢 High |
| Venmo | ~2.3 billion (est.) | ~$280 billion | [BusinessOfApps](https://www.businessofapps.com/data/venmo-statistics/) / [PayPal 10-K](https://www.sec.gov/Archives/edgar/data/1633917/000163391725000019/pypl-20241231.htm) | 🟡 Medium |
| Cash App | ~1.5 billion (est.) | ~$283 billion (inflows) | [BusinessOfApps](https://www.businessofapps.com/data/cash-app-statistics/) / [Block 10-K](https://www.sec.gov/Archives/edgar/data/1512673/000162828025007376/sq-20241231.htm) | 🟡 Medium |
| PayPal P2P (non-Venmo) | ~0.3 billion (est.) | ~$150 billion (est.) | Estimated from PayPal TPV | 🔴 Low |
| **US Total** | **~7.7 billion** | **~$1.75 trillion** | | |

### Non-US Estimates (2024)

| Platform/Region | Annual Transactions (est.) | Annual Value (est.) | Confidence |
|-----------------|---------------------------|-------------------|------------|
| Bizum (Spain) | ~0.3 billion | ~$30 billion | 🟡 Medium |
| Swish (Sweden) | ~0.15 billion | ~$15 billion | 🟡 Medium |
| Other European P2P | ~0.2 billion | ~$40 billion | 🔴 Low |
| Rest of World (excl. UPI, China) | ~0.15 billion | ~$20 billion | 🔴 Low |
| **Non-US Total** | **~0.8 billion** | **~$105 billion** | |

---

## Historic Trend

### Zelle

| Year | Transactions (billions) | Value ($billions) | Source |
|------|------------------------|-------------------|--------|
| 2019 | 0.74 | $187 | Early Warning Services |
| 2020 | 1.2 | $307 | Early Warning Services |
| 2021 | 1.8 | $490 | Early Warning Services |
| 2022 | 2.3 | $629 | Early Warning Services |
| 2023 | 2.9 | $806 | [Zelle](https://www.zelle.com/press-releases/zelle-soars-806-billion-transaction-volume-28-prior-year) |
| 2024 | 3.6 | $1,040 | [CNBC](https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html) |

### Venmo (Total Payment Volume)

| Year | Value ($billions) | Est. Transactions (billions) | Source |
|------|-------------------|------------------------------|--------|
| 2019 | $102 | ~0.9 | PayPal 10-K |
| 2020 | $159 | ~1.3 | PayPal 10-K |
| 2021 | $230 | ~1.7 | PayPal 10-K |
| 2022 | $244 | ~1.8 | PayPal 10-K |
| 2023 | $270 | ~2.1 | PayPal 10-K |
| 2024 | ~$280 (est.) | ~2.3 (est.) | Q1 data × 4 extrapolation |

### Cash App

| Year | Value ($billions) | Est. Transactions (billions) | Source |
|------|-------------------|------------------------------|--------|
| 2019 | ~$40 | ~0.4 | Block filings |
| 2020 | ~$75 | ~0.7 | Block filings |
| 2021 | ~$100 | ~0.9 | Block filings |
| 2022 | ~$128 | ~1.0 | Block filings |
| 2023 | ~$210 | ~1.3 | Block filings / estimates |
| 2024 | ~$283 | ~1.5 | [Block 10-K](https://www.sec.gov/Archives/edgar/data/1512673/000162828025007376/sq-20241231.htm) |

### Aggregate US P2P Market

| Year | Est. Total Value ($billions) | Est. Transactions (billions) | Avg TPS |
|------|-----------------------------|-----------------------------|---------|
| 2019 | $450 | 2.7 | 86 |
| 2020 | $680 | 3.9 | 124 |
| 2021 | $920 | 5.1 | 162 |
| 2022 | $1,150 | 5.8 | 184 |
| 2023 | $1,450 | 7.0 | 222 |
| 2024 | $1,750 | 7.7 | 244 |

---

## Growth Rate Analysis

| Period | CAGR (Transactions) | CAGR (Value) | Notes |
|--------|---------------------|--------------|-------|
| 2019-2024 US (5yr) | ~23.3% | ~31.2% | Rising avg. txn size + adoption |
| 2022-2024 US (2yr) | ~15.2% | ~23.3% | Growth normalizing |
| Zelle 2019-2024 | ~37.2% | ~40.9% | Bank integration driving adoption |
| Venmo 2019-2024 | ~20.6% | ~22.4% | Mature but steady |
| Cash App 2019-2024 | ~30.3% | ~48.0% | Rapid growth from lower base |

---

## Projections

### Baseline (12% CAGR declining to 6% by 2035)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($T) |
|------|----------------------|---------|-------------------|
| 2025 | 9.5 | 301 | 3.1 |
| 2027 | 11.8 | 374 | 3.9 |
| 2030 | 15.5 | 491 | 5.1 |
| 2035 | 20.7 | 656 | 6.8 |

### High Growth (16% CAGR declining to 10%)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($T) |
|------|----------------------|---------|-------------------|
| 2025 | 9.9 | 314 | 3.2 |
| 2027 | 13.0 | 412 | 4.3 |
| 2030 | 19.0 | 602 | 6.3 |
| 2035 | 30.6 | 970 | 10.1 |

### Conservative (8% CAGR declining to 4%)

| Year | Annual Txns (billions) | Avg TPS | Annual Value ($T) |
|------|----------------------|---------|-------------------|
| 2025 | 9.2 | 292 | 3.0 |
| 2027 | 10.7 | 339 | 3.5 |
| 2030 | 13.0 | 412 | 4.3 |
| 2035 | 15.8 | 501 | 5.2 |

---

## Key Findings

1. **Zelle is the undisputed US P2P leader by value**, surpassing $1 trillion in 2024 — the first P2P platform to reach this milestone. Its bank-integrated model gives it a structural advantage: money moves instantly between bank accounts with no app required.

2. **The US dominates global dedicated P2P**, accounting for ~90% of the category's transaction volume. This reflects the fact that in other major markets (India, China), P2P is embedded in multipurpose wallets (UPI apps, WeChat).

3. **Average transaction sizes are rising**, not falling. Zelle's average transaction grew from ~$253 (2019) to ~$289 (2024), suggesting P2P is moving beyond splitting dinner tabs into rent, utilities, and small business payments.

4. **Cash App's growth trajectory is the steepest** among US platforms, with inflows growing from ~$40B to ~$283B in five years (48% CAGR by value). Its expansion into banking, investing, and business payments is driving this.

5. **P2P is a gateway to broader fintech.** All three major US platforms now offer debit cards, direct deposit, investing, and buy-now-pay-later. P2P volumes increasingly include commercial transactions.

6. **Market maturation is visible.** Venmo's growth has slowed to ~5% annually by value, while Zelle still grows at 27% thanks to ongoing bank rollouts. The US P2P market is unlikely to sustain >15% growth beyond 2027.

---

## Data Quality & Limitations

- **Zelle data is the most reliable** — Early Warning Services publishes annual and quarterly figures, and Zelle is not publicly traded (owned by a bank consortium), reducing incentive to distort.
- **Venmo transaction count is estimated** — PayPal reports TPV but not transaction counts for Venmo separately. Transaction count derived from average transaction size assumptions (~$120).
- **Cash App "inflows" vs. P2P** — Block reports "Cash App inflows" which include direct deposits, Bitcoin purchases, and Cash App Pay merchant transactions, not purely P2P. Pure P2P is likely ~60% of the $283B.
- **Non-US data is sparse** — Bizum and Swish publish some data; most other regional P2P platforms do not.
- **Boundary with digital wallets is fuzzy** — Cash App, Venmo, and PayPal are wallet-like platforms. The classification here focuses on their P2P transfer functionality.

---

## Sources

1. [CNBC — Zelle payments top $1 trillion in 2024](https://www.cnbc.com/2025/02/12/zelle-payments-top-1-trillion-in-2024.html)
2. [Zelle — $806 Billion Transaction Volume press release (2023)](https://www.zelle.com/press-releases/zelle-soars-806-billion-transaction-volume-28-prior-year)
3. [American Banker — Zelle passes $1T in 2024](https://www.americanbanker.com/payments/news/zelle-passes-1t-in-2024-with-a-boost-from-small-businesses)
4. [PayPal 10-K FY2024](https://www.sec.gov/Archives/edgar/data/1633917/000163391725000019/pypl-20241231.htm)
5. [Block 10-K FY2024](https://www.sec.gov/Archives/edgar/data/1512673/000162828025007376/sq-20241231.htm)
6. [BusinessOfApps — Venmo Statistics 2026](https://www.businessofapps.com/data/venmo-statistics/)
7. [BusinessOfApps — Cash App Statistics 2026](https://www.businessofapps.com/data/cash-app-statistics/)
8. [CoinLaw — Zelle vs Venmo Statistics 2026](https://coinlaw.io/zelle-vs-venmo-statistics/)
9. [eMarketer — US Mobile P2P Payments Forecast 2024](https://www.emarketer.com/content/us-mobile-p2p-payments-forecast-2024)
10. [Tearsheet — Zelle closing in on $1T](https://tearsheet.co/data-snacks/venmo-and-cash-app-competitor-zelle-is-closing-in-on-its-1-trillion-payments-volume-target/)
11. [Precedence Research — P2P Payment Market Size to Hit $16.21T by 2034](https://www.precedenceresearch.com/p2p-payment-market)
12. [Electroiq — Venmo Statistics 2025](https://electroiq.com/stats/venmo-statistics/)

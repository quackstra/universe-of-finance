# Universe of Finance — Research Index

> Complete index of all 29 category analyses with current TPS estimates.

## The Big Number

**De-Duplicated Global Financial TPS: ~73,750**

*Range: 67,000–83,000 TPS. Programmatic validation via `tools/big_number.py`.*
*Coordinated global peak: ~147,000–246,000 TPS ([Peak TPS Analysis](PEAK_TPS.md)).*
*Run 6: Full 29-category reconciliation with 5 new payment categories and revised estimates.*

## Completed Analyses

### Payments (11 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence | Overlap |
|---|----------|---------|----------|-------------|--------------|------------|---------|
| 1 | [Consumer Cards](payments/consumer-cards/REPORT.md) | 24,501 | 61,250 | 772.7B | $51.9T | 🟢 91 | Primary rail |
| 2 | [Digital Wallets](payments/digital-wallets/REPORT.md) | 19,660 | 45,000 | 620B | $15.6T | 🟡 67 | ~10% card overlap |
| 3 | [Bank Transfers](payments/bank-transfers/REPORT.md) | 15,338 | 27,500 | 484B | — | 🟢 78 | Primary rail |
| 4 | [Bill Payments](payments/bill-payments/REPORT.md) | ~3,012 | — | ~95B | — | 🟡 48 | 90% overlap |
| 5 | [E-Commerce](payments/ecommerce/REPORT.md) | ~1,800 | — | ~57.5B | $6.3T | 🟡 67 | 95% overlap |
| 6 | [ATM Withdrawals](payments/atm-withdrawals/REPORT.md) | ~1,557 | — | ~49.1B | $7.7T | 🟡 52 | **Zero** overlap |
| 7 | [Payroll](payments/payroll/REPORT.md) | ~1,305 | — | ~41.2B | — | 🔴 35 | 90% overlap |
| 8 | [BNPL](payments/bnpl/REPORT.md) | ~634 | — | ~20B events | $450B GMV | 🟡 58 | 100% infra, 3.6× multiplier |
| 9 | [Insurance Premiums](payments/insurance-premiums/REPORT.md) | ~444 | — | ~14B | $7.2T | 🟡 52 | 90% overlap |
| 10 | [P2P Transfers](payments/p2p-transfers/REPORT.md) | 270 | 600 | 8.5B | $2.8T | 🟡 69 | Partial overlap |
| 11 | [Remittances](payments/remittances/REPORT.md) | 57 | 100 | 1.8B | $905B | 🟡 58 | Partial overlap |

### Traditional Finance (6 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence | Notes |
|---|----------|---------|----------|-------------|--------------|------------|-------|
| 12 | [Exchange-Traded Derivatives](traditional-finance/etd/REPORT.md) | ~9,500 | ~57,000 | 205.3B | — | 🟢 88 | India NSE = ~50% |
| 13 | [Equity Markets](traditional-finance/equity-markets/REPORT.md) | ~3,500 | ~80,000 | 61.5B | $106.5T | 🟢 86 | India 28% by count |
| 14 | [Commodities](traditional-finance/commodities/REPORT.md) | ~330 | — | ~10.4B | — | 🟢 74 | Exchange-traded only |
| 15 | [Foreign Exchange](traditional-finance/forex/REPORT.md) | ~127 | — | ~4B | $2,500T+ | 🟡 58 | Incl. 8M retail/day |
| 16 | [Fixed Income](traditional-finance/fixed-income/REPORT.md) | ~10.5 | — | ~332M | $145T outstanding | 🟡 60 | Incl. 219M repo |
| 17 | [OTC Derivatives](traditional-finance/otc-derivatives/REPORT.md) | ~0.17 | — | ~5.3M | $665T notional | 🟡 68 | Excl. FX derivatives |

### Digital Assets (4 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence | Notes |
|---|----------|---------|----------|-------------|--------------|------------|-------|
| 18 | [Centralised Exchanges](digital-assets/cex/REPORT.md) | ~3,210 | ~15,000 | ~101B | $77.3T | 🟡 56 | 20.6% wash adjusted |
| 19 | [L1 & L2 Blockchain](digital-assets/blockchain-l1-l2/REPORT.md) | ~415 | ~2,500 | ~13.1B | — | 🟢 76 | Solana vote-filtered |
| 20 | [Stablecoins](digital-assets/stablecoins/REPORT.md) | ~520 | ~2,000 | — | $5.7T adj. | 🟢 75 | Subset of L1/L2 |
| 21 | [DeFi](digital-assets/defi/REPORT.md) | *(subset)* | — | — | $4.16T | 🟡 62 | Subset of L1/L2 |

### Banking & Interbank (2 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 22 | [Interbank RTGS](banking/interbank-rtgs/REPORT.md) | ~50.1 | ~130 | ~1,581M | $5,614T | 🟢 82 |
| 23 | [Securities Settlement](banking/securities-settlement/REPORT.md) | ~41-48 | — | ~1.3-1.5B | $3.7 quadrillion | 🟢 74 |

### Gaming (2 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence | Overlap |
|---|----------|---------|----------|-------------|--------------|------------|---------|
| 24 | [In-Game Microtx](gaming/gaming-microtx/REPORT.md) | ~389 | ~778 | ~12.3B | $114B | 🔴 44 | 82% card/wallet overlap |
| 25 | [Game Sales](gaming/gaming-sales/REPORT.md) | ~92 | ~275 | ~2.9B | $60.2B | 🟡 56 | 84% card/wallet overlap |

### Government (1 category)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 26 | [Tax & Government](government/government-payments/REPORT.md) | ~1,002 | ~10,000 | ~31.6B | $25-30T | 🟡 50 |

### Emerging (3 categories)

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 27 | [IoT & M2M](emerging/iot-m2m/REPORT.md) | ~1,538 | ~2,500 | ~48.5B | — | 🟡 67 |
| 28 | [Tokenised RWA](emerging/rwa-tokenisation/REPORT.md) | ~2.4 | ~15 | ~75M | $24B TVL | 🟡 56 |
| 29 | [AI Agent Transactions](emerging/ai-agents/REPORT.md) | ~0.66 | ~8.5 | — | $600M | 🔴 34 |

## Double-Counting & Overlap Rules

These categories overlap — the [Overlap Matrix](OVERLAP_MATRIX.md) details de-duplication:

| Overlap | Rule | Impact |
|---------|------|--------|
| Digital Wallets ↔ Cards | ~10% of wallet txns ride card rails (Apple/Google Pay) | -62B |
| E-Commerce ↔ Cards/Transfers | Commerce layer, 95% paid via cards/transfers | -54.6B |
| DeFi ↔ L1/L2 | Subset — do not add | 0 |
| Stablecoins ↔ L1/L2 | Subset — do not add | 0 |
| Gaming ↔ Cards/Wallets | 82% on card/wallet rails | -12.4B |
| Bill Payments ↔ Direct Debit/Cards | 90% via existing payment rails | -85.5B |
| Insurance ↔ Cards/Transfers | 90% via existing payment rails | -12.6B |
| Payroll ↔ Bank Transfers | 90% is ACH/BACS/SEPA batch | -37.1B |
| BNPL ↔ Cards/Transfers | 100% infrastructure overlap, but genuine 3.6× multiplier | Complex |
| ATM ↔ Nothing | **Zero overlap** — cash-out, not a payment | 0 |
| Securities Settlement ↔ Trading | Settlement is downstream of trading | Separate per taxonomy |

## Cross-Cutting Analyses

- **[Overlap Matrix](OVERLAP_MATRIX.md)** — Full de-duplication methodology
- **[Confidence Scorecard](CONFIDENCE_SCORECARD.md)** — 0-100 scores for all 29 categories
- **[Time-Series 2015-2025](timeseries/TIMESERIES.md)** — A decade of TPS data
- **[Growth Analysis](timeseries/growth-analysis.md)** — Structural trends and regime changes
- **[Peak TPS](PEAK_TPS.md)** — Calendar co-occurrence and maximum global load
- **[Scenario Analysis](SCENARIOS.md)** — Recession, pandemic, crypto winter stress tests
- **[Data Freshness](DATA_FRESHNESS.md)** — Source staleness tracker
- **[Payments Overlap](payments/OVERLAP_ANALYSIS.md)** — Payments sector deep dive

---

*Last updated: 2026-03-28 (Run 6). 29 categories, 6 runs completed.*

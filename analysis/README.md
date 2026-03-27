# Universe of Finance — Research Index

> Auto-generated index of all completed transaction volume analyses.

## The Big Number

**De-Duplicated Global Financial TPS: ~70,200** (payment infrastructure) / **~71,200** (all economic events)

*Run 3 reconciliation with Solana vote filtering, government bottom-up model, and expanded RTGS coverage.*
*Programmatic validation (`tools/big_number.py`): ~70,741 TPS. Range: 64,000 – 80,000 TPS.*

## Completed Analyses

### Payments

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 1 | [Consumer Cards](payments/consumer-cards/REPORT.md) | 24,501 | 61,250 | 772.7B | $51.9T | 🟢 High |
| 2 | [Digital Wallets](payments/digital-wallets/REPORT.md) | 19,660 | 45,000 | 620B | $15.6T | 🟡 Medium |
| 3 | [Bank Transfers](payments/bank-transfers/REPORT.md) | 15,338 | 27,500 | 484B | — | 🟡 Medium |
| 4 | [E-Commerce](payments/ecommerce/REPORT.md) | ~1,800 | — | ~57.5B | $6.3T | 🟡 Medium |
| 5 | [P2P Transfers](payments/p2p-transfers/REPORT.md) | 270 | 600 | 8.5B | $2.8T | 🟡 Medium |
| 6 | [Remittances](payments/remittances/REPORT.md) | 57 | 100 | 1.8B | $905B | 🟡 Medium |

### Traditional Finance

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 7 | [Exchange-Traded Derivatives](traditional-finance/etd/REPORT.md) | ~9,500 | ~57,000 | 205.3B | — | 🟡 Medium |
| 8 | [Equity Markets](traditional-finance/equity-markets/REPORT.md) | ~3,500 | ~80,000 | 61.5B | $106.5T | 🟡 Medium |
| 9 | [Commodities](traditional-finance/commodities/REPORT.md) | ~330 | — | ~10.4B | — | 🟡 Medium |
| 10 | [Foreign Exchange](traditional-finance/forex/REPORT.md) | ~35 | — | ~750M | $2,500T+ | 🔴 Low |
| 11 | [Fixed Income](traditional-finance/fixed-income/REPORT.md) | ~7 (cash) / ~35 (w/ repo) | — | ~220M (cash) | $145T outstanding | 🔴 Low |
| 12 | [OTC Derivatives](traditional-finance/otc-derivatives/REPORT.md) | ~0.6 | — | ~15M | $665T notional | 🔴 Low |

### Digital Assets

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 13 | [Centralised Exchanges](digital-assets/cex/REPORT.md) | ~4,000 | ~15,000 | — | $77.3T | 🔴 Low |
| 14 | [L1 & L2 Blockchain](digital-assets/blockchain-l1-l2/REPORT.md) | ~415 | ~2,500 | ~13.1B | — | 🟡 Medium |
| 15 | [Stablecoins](digital-assets/stablecoins/REPORT.md) | ~520 | ~2,000 | — | $27.6T raw / $5.7T adj. | 🟡 Medium |
| 16 | [DeFi](digital-assets/defi/REPORT.md) | *(subset of L1/L2)* | — | — | $4.16T | 🟢 High (volume) |

### Banking & Interbank

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 17 | [Securities Settlement](banking/securities-settlement/REPORT.md) | ~41-48 | — | ~1.3-1.5B | $3.7 quadrillion | 🟡 Medium |
| 18 | [Interbank RTGS](banking/interbank-rtgs/REPORT.md) | ~50.1 | ~130 | ~1,581M | $5,614T | 🟡 Medium |

### Gaming

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 19 | [In-Game Microtransactions](gaming/gaming-microtx/REPORT.md) | ~389 | ~778 | ~12.3B | $114B | 🔴 Low |
| 20 | [Game Sales & Subscriptions](gaming/gaming-sales/REPORT.md) | ~92 | ~275 | ~2.9B | $60.2B | 🔴 Low |

### Government

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 21 | [Tax & Government Payments](government/government-payments/REPORT.md) | ~1,002 | ~10,000 | ~31.6B | $25-30T | 🟡 Medium |

### Emerging

| # | Category | Avg TPS | Peak TPS | Annual Txns | Annual Value | Confidence |
|---|----------|---------|----------|-------------|--------------|------------|
| 22 | [IoT & M2M Payments](emerging/iot-m2m/REPORT.md) | ~634 | ~2,500 | ~20B | — | 🔴 Low |
| 23 | [Tokenised RWA](emerging/rwa-tokenisation/REPORT.md) | ~2.4 | ~15 | ~75M | $24B TVL | 🔴 Low |
| 24 | [AI Agent Transactions](emerging/ai-agents/REPORT.md) | ~0.66 | ~8.5 | — | $600M | 🔴 Low |

## Double-Counting Notes

These categories have known overlaps — do NOT simply sum all TPS values:

- **Digital Wallets ↔ Consumer Cards**: Many wallet transactions (Apple Pay, Google Pay) ride on card rails. Significant overlap.
- **DeFi ↔ L1/L2 Blockchain**: DeFi is a *subset* of on-chain transactions. Do not add separately.
- **Stablecoins ↔ L1/L2 Blockchain**: Stablecoin transfers are a *subset* of on-chain transactions. Do not add separately.
- **E-Commerce ↔ Consumer Cards / Bank Transfers**: E-commerce is paid via cards or bank transfers. Overlap with payment categories.
- **Gaming ↔ Consumer Cards**: Most gaming purchases are made via card/wallet. ~2% of global card volume.
- **Securities Settlement ↔ Equity/Bond/Derivative Markets**: Settlement is downstream of trading. Different category per taxonomy rules but same economic event.

## TPS Leaders (Non-Overlapping)

The top 5 categories by transaction count, accounting for overlaps:

1. **Consumer Cards** — 24,501 TPS (772.7B/year)
2. **Digital Wallets** — 19,660 TPS (620B/year) *partial overlap with cards*
3. **Bank Transfers** — 15,338 TPS (484B/year)
4. **Exchange-Traded Derivatives** — 9,500 TPS (205.3B/year)
5. **Centralised Crypto Exchanges** — 4,000 TPS (est.)

---

*Last updated: 2026-03-27 (Run 3 reconciliation). Run `./run.sh scout` to see the full research backlog.*

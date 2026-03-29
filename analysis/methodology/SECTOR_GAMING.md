---
title: "Sector: Gaming"
parent: Methodology
grand_parent: Explore
nav_order: 6
---

# Sector Methodology: Gaming & Virtual Economies

> How we measure gaming transaction activity — 2 categories, ~481 TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

The Gaming sector measures **commerce events** within the digital gaming economy — in-game microtransactions (skins, items, virtual currency, loot boxes) and game purchases (digital sales, subscriptions, esports betting). At ~481 TPS, Gaming accounts for **0.7% of global financial TPS**.

Critically, Gaming is a **commerce layer**, not a payment layer. An estimated 65-80% of gaming purchases are paid via card networks, digital wallets, or bank transfers that are already counted in the Payments sector. Gaming counts the **economic event** (player buys a skin), not the payment flow (Visa processes the charge). For payment infrastructure TPS, Gaming is excluded; for economic transaction TPS, Gaming adds ~481 TPS.

---

## 2. Sector-Specific Measurement Challenges

**Revenue-to-transaction conversion.** Game publishers report revenue, not transaction counts. The core challenge is converting revenue → transaction count using average transaction size, which varies wildly: mobile microtransactions average $2-5, PC game purchases average $30-40, console game purchases average $50-60.

**Platform opacity.** App Store and Google Play do not publish transaction counts. Steam publishes some data (Steam Replay). Console platforms (PlayStation Store, Xbox Store, Nintendo eShop) disclose revenue but not transaction frequency.

**Free-to-play dominance.** 95%+ of mobile game revenue comes from <5% of players ("whales"). This extreme distribution means average transaction size is misleading — the median player transacts zero times, while whales may transact hundreds of times per year.

**In-game virtual currency.** Many games use intermediate virtual currencies (V-Bucks, Robux, Gold). The real-money purchase of virtual currency is one transaction, but the subsequent in-game spending of that currency generates many virtual transactions that are not real financial events. We count only the **real-money transaction**, not virtual currency spending.

**Regional variation.** China's gaming market (37% of global mobile gaming revenue) has distinct monetization patterns. Gacha/loot box mechanics dominate in Asia; battle pass/cosmetic models dominate in the West. Average transaction sizes differ by 2-3x.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume (B) | Confidence | Notes |
|---|----------|---------|-------------------|------------|-------|
| 1 | In-Game Microtransactions | 389 | 12.28 | 44 (Medium) | Revenue / avg txn size derivation |
| 2 | Digital Game Sales & Subscriptions | 92 | 2.89 | 56 (Medium) | Platform reports + estimates |

**Sector total: ~481 TPS**

---

## 4. Cross-Category Overlap Rules

### Intra-Sector Overlap

Microtransactions and Game Sales are **distinct transaction types** with no overlap:
- Microtransactions = in-game purchases within a game already owned/installed
- Game Sales = purchasing or subscribing to a game itself

No de-duplication needed within the sector.

### Cross-Sector Overlap (with Payments)

```
┌─────────────────────────────────────────────────────────┐
│  GAMING SECTOR (commerce layer)                          │
│                                                          │
│  ┌──────────────────┐  ┌──────────────────┐             │
│  │ Microtransactions │  │   Game Sales     │             │
│  │ 389 TPS          │  │   92 TPS         │             │
│  │                   │  │                  │             │
│  │ Paid via:         │  │ Paid via:        │             │
│  │ • Cards: 40%      │  │ • Cards: 45%     │             │
│  │ • Wallets: 25%    │  │ • Wallets: 25%   │             │
│  │ • Platform: 20%   │  │ • Platform: 20%  │             │
│  │ • Direct debit:10%│  │ • Direct: 10%    │             │
│  │ • Crypto/other:5% │  │                  │             │
│  └────────┬─────────┘  └────────┬─────────┘             │
│           │                      │                       │
│           └──────────┬───────────┘                       │
│                      ▼                                   │
├─────────────────────────────────────────────────────────┤
│  PAYMENTS SECTOR (payment rail)                          │
│                                                          │
│  ~65-75% of gaming TPS is already counted in             │
│  Consumer Cards, Digital Wallets, or Bank Transfers.     │
│                                                          │
│  Incremental gaming TPS (not on tracked rails):          │
│  ~120-170 TPS (platform balance, crypto, gift cards)     │
└─────────────────────────────────────────────────────────┘
```

**Decision:** Gaming is excluded from the payment infrastructure TPS total (~70,200) but included in the economic transaction TPS total (~71,200). This avoids double-counting while still capturing the economic activity.

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Newzoo Annual       ████████░░ ████████░ ████████░░  ████░░░░░░
Sensor Tower        ██████░░░░ █████████ ███████░░░  ██████░░░░
Steam Replay/DB     ███░░░░░░░ █████████ █████████░  ████████░░
SuperData (Nielsen) ████████░░ ███████░░ ████████░░  █████░░░░░
App Annie/data.ai   ██████░░░░ █████████ ███████░░░  ██████░░░░
Publisher 10-Ks     ████░░░░░░ █████████ █████████░  ███████░░░
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Revenue anchors):** Newzoo (global market size), Sensor Tower (mobile), publisher filings (EA, Activision, Tencent, NetEase)
**Tier 2 (Transaction proxies):** Steam database (PC), SuperData/Nielsen (cross-platform)
**Tier 3 (Conversion factors):** Academic studies on average transaction size, App Annie/data.ai (download and spend data)

---

## 6. Sector Triangulation Approach

### Gaming Sector Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [Revenue / AOV]       [Player Base ×      [Platform     │
│  Total revenue ÷       Conversion Rate ×   reported      │
│  avg order value       Avg Purchases/yr]   metrics]      │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ ~14B     │         │ ~16B     │        │ ~13B     │  │
│  │ annual   │         │ annual   │        │ annual   │  │
│  │ txns     │         │ txns     │        │ txns     │  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ Method B overcounts   │                    │
│              │ (assumes all payers   │                    │
│              │ are active; actual    │                    │
│              │ conversion is ~3-5%). │                    │
│              │ Method C undercounts  │                    │
│              │ (misses non-reported  │                    │
│              │ platforms). Method A  │                    │
│              │ is most reliable.     │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ ~15.2B annual txns    │                    │
│              │ ~481 TPS              │                    │
│              │ Range: 350-650 TPS    │                    │
│              │ Confidence: 50/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

**Method A (Revenue / AOV):** Global gaming revenue ($187B in 2024) → mobile microtransaction revenue ($92B) / avg transaction ($7.50) = ~12.3B + digital sales revenue ($95B) / avg purchase ($33) = ~2.9B. Total: ~15.2B.

**Method B (Player Base):** 3.4B gamers × 5% paying conversion × 89 purchases/yr (for payers) = ~15.1B. High uncertainty on conversion rate and purchase frequency.

**Method C (Platform Metrics):** Sum of Steam (~2B), App Store (~4B), Google Play (~5B), console stores (~2B) = ~13B. Undercounts indie platforms and direct-to-publisher.

---

## 7. Definition Standards

In Gaming, a **transaction** is a **real-money purchase event** — the moment a player spends actual currency (not virtual currency) on a game, in-game item, or subscription.

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| In-Game Microtransactions | Completed real-money purchase of virtual goods/currency | Virtual currency spending (post-purchase), free rewards, gifted items |
| Digital Game Sales | Completed game purchase or subscription renewal | Free game downloads, demo installations, wishlisting |

**Key distinction from Payments:** Gaming counts the **commerce event** (what was bought), not the payment method (how it was paid). The payment is counted in the Payments sector.

---

## 8. Known Gaps & Future Work

- **Average transaction size precision.** The AOV assumption ($7.50 for microtransactions, $33 for game sales) is the single highest-leverage variable. A ±20% change in AOV produces ±20% change in transaction count. Primary research (surveys, platform partnerships) would reduce this uncertainty.
- **China/Asia-Pacific microtransaction data.** Tencent and NetEase dominate Asian gaming but disclose revenue, not transaction counts. Chinese gacha/loot box mechanics produce different transaction patterns than Western cosmetic/battle pass models.
- **Esports betting.** Currently included in Game Sales but may warrant its own subcategory as the market grows. Transaction patterns differ significantly from game purchases.
- **Web3 gaming.** Blockchain-based game transactions (NFT purchases, token earning) blur the line between Gaming and Digital Assets sectors. Currently counted in Digital Assets (on-chain) rather than Gaming.
- **Virtual economy internal transactions.** The total volume of in-game virtual currency transactions is estimated at 10-50x the real-money transaction volume. These are economically meaningful but are not financial transactions under UoF definition.

---

*Gaming is a low-confidence sector due to the fundamental revenue-to-transaction conversion challenge. The methodology will improve as platforms begin publishing transaction count data alongside revenue.*

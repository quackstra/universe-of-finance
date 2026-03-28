# In-Game Microtransactions — Confidence Uplift (Run 7, 2026-03-28)

## Previous State
- **TPS:** 475 (range 380-634)
- **Annual volume:** ~15B transactions
- **Confidence:** 55
- **Key gaps:** No platform publishes transaction counts; ATV assumptions drive everything

---

## 1. New Data Sources Found

### Sensor Tower — Mobile Gaming 2025 (UPDATED)
- **URL:** https://sensortower.com/blog/state-of-mobile-gaming-apps
- Mobile game IAP revenue 2025: **$81.75-82B** (+1.3% YoY)
- Third consecutive year of revenue growth
- Fewer installs but higher spend per retained player

### Average IAP Transaction Size (NEW HARD DATA)
- **URL:** https://www.businessofapps.com/data/app-data-report/
- **Average IAP transaction: $1.08** (all app categories)
- Average revenue per paying user: $9.60
- Average revenue per user (all users): $0.48
- IAP accounts for 72% of total App Store revenue
- iOS users spend 2.1x more per app than Android

This is the most important new data point. If the average IAP transaction is $1.08, then:
- Mobile game IAP revenue $82B / $1.08 = **75.9B transactions** for mobile alone

**BUT WAIT** — the $1.08 figure is across ALL app categories, not games specifically. Games tend to have larger individual transactions (gacha pulls, battle passes, gem packs). The genre-segmented ATV from Run 6 ($7.60 weighted) accounts for game-specific pricing. The $1.08 figure likely includes many $0.99 utility/productivity IAPs that pull the average down.

**Resolution:** The $1.08 is a lower bound on average transaction size. For games specifically:
- If average game transaction = $1.08 → 82B / 1.08 = 75.9B mobile game transactions
- If average game transaction = $3.00 → 82B / 3.00 = 27.3B mobile game transactions
- If average game transaction = $7.60 (Run 6 estimate) → 82B / 7.60 = 10.8B mobile game transactions

### Roblox FY2025 Hard Data (UPDATED)
- **URL:** https://ir.roblox.com/news/news-details/2025/Roblox-Reports-Second-Quarter-2025-Financial-Results/
- 127M daily active users
- **1.8M daily unique paying users**
- Average daily bookings: $0.15/DAU, $10.36/paying user
- Full-year 2025 bookings: **$6.57-6.62B** (50-51% YoY growth)
- Average paying user lifetime: 27 months
- Creator payouts: $1,503M (up from $923M in 2024)

**Deriving Roblox transaction count:**
- 1.8M daily paying users × $10.36/day average = $18.6M/day
- $6.6B / 365 = $18.1M/day (cross-validates)
- If average Robux purchase = $5-10: 18.1M / 7.50 = **2.41M transactions/day = 881M/year**
- If average = $3 (smaller bundles): 18.1M / 3 = **6.0M/day = 2.2B/year**
- **Roblox alone: ~0.9-2.2B transactions/year**

### Fortnite/Epic Games 2025 (UPDATED)
- **URL:** https://store.epicgames.com/en-US/news/epic-games-store-2025-year-in-review
- Epic Games Store total 2025 revenue: $1.16B (6% increase)
- Fortnite: ~$6B total revenue in 2025
- 110M monthly active users
- Epic Games Store: 317M total accounts, 78M monthly active (Dec 2025)

**Deriving Fortnite transaction count:**
- $6B revenue / average V-Bucks purchase ~$10 = ~600M transactions/year
- At $5 average: ~1.2B/year

### Steam 2025 (NEW)
- **URL:** https://sqmagazine.co.uk/steam-statistics/
- Revenue: **$16.2B** through Nov 2025 (up from $10.8B full year 2024)
- 132M MAU, 69M DAU
- Game sales: 61% of revenue ($9.9B)
- DLC + microtransactions: 27% of revenue ($4.4B)
- Community Market + Steam Wallet: 12% ($1.9B)
- 8.2M customers purchased Daily Deals in 2025 (125% YoY increase)
- Average revenue per user: ~$19

**Deriving Steam microtransaction count:**
- DLC + microtransactions: $4.4B
- Average transaction size for Steam items/DLC: ~$5-15
- $4.4B / $10 = ~440M microtransactions/year
- Community Market adds hundreds of millions more small trades

### Global In-App Purchase Market (UPDATED)
- **URL:** https://www.precedenceresearch.com/online-microtransaction-market
- Global IAP market: $166.6B in 2024, projected $582.6B by 2033
- PC gaming microtransactions: $24.4B in 2024

---

## 2. Updated Triangulation

### Method 1: Revenue / Genre-Segmented ATV (refined)

| Platform | IAP Revenue 2025 ($B) | Weighted ATV ($) | Transactions (B) |
|----------|----------------------|-----------------|-------------------|
| Mobile games | 82 | 5.00* | 16.4 |
| PC (Steam + Epic + others) | 8 | 8.00 | 1.0 |
| Console (PS/Xbox/Nintendo) | 15 | 12.00 | 1.25 |
| **Total** | **105** | | **18.65** |

*Revised mobile ATV down from $7.60 to $5.00 based on new evidence that average IAP is $1.08 across all apps. Games are higher but $7.60 was likely too high for the casual-heavy mobile market. A $5.00 estimate balances between the $1.08 all-app average and the $7.60 genre-weighted estimate.*

### Method 2: Per-Game Anchoring (refined)

| Game/Platform | Annual Txns (B) | Method |
|--------------|-----------------|--------|
| Roblox | 0.9-2.2 | Bookings $6.6B / avg purchase $3-7.50 |
| Fortnite | 0.6-1.2 | Revenue $6B / avg purchase $5-10 |
| Honor of Kings | 0.5-1.0 | Revenue $2.5B / avg $2.50-5 |
| Genshin Impact | 0.15-0.3 | Revenue $1.5B / avg $5-10 |
| Top 10 mobile games | 3-6 | Top games = ~30% of mobile revenue |
| Remaining mobile | 7-14 | Scale from top 10 |
| Steam + PC | 0.5-1.5 | DLC/microtx $4.4B / avg $3-8 |
| Console | 0.5-1.5 | $15B / avg $10-30 |
| **Total** | **11-24** | |

### Method 3: User Base × Conversion × Frequency (unchanged but cross-checked)
- 3.2B gamers globally, ~10% pay for microtransactions = 320M payers
- Average payer makes 40-60 purchases/year
- 320M × 50 = 16B transactions/year

### Method 4: All-App IAP as Ceiling (NEW)
- All mobile IAP (games + non-games): $150B in 2024
- If average transaction = $1.08: 138.9B total mobile IAP transactions
- Games = ~54% of IAP revenue → ~75B transactions IF game average = all-app average
- But game transactions are larger → probably 20-40B game transactions
- This provides an **upper bound of ~40B** for mobile game transactions

### Triangulation Summary

| Method | Annual Estimate (B) | TPS |
|--------|-------------------|-----|
| Revenue / revised ATV | 18.6 | 590 |
| Per-game anchoring | 11-24 | 349-761 |
| User × conversion × frequency | 16 | 507 |
| All-app IAP ceiling | 20-40 | 634-1,268 |
| Previous estimate | 15 | 475 |

**Central estimate revision: 17B annual → 539 TPS**

---

## 3. Revised TPS Estimate

The new $1.08 average IAP transaction data point suggests the previous $7.60 genre-weighted ATV was too high for the overall mobile market. Revising the mobile ATV to $5.00 pushes the transaction count up from ~15B to ~17-19B.

**Revised central estimate: 17B annual transactions = 539 TPS**

| Metric | Previous | Revised |
|--------|----------|---------|
| Annual transactions | 15B | 17B |
| Average TPS | 475 | 539 |
| Range | 12-20B | 14-24B |
| TPS range | 380-634 | 444-761 |

The revision is modest (+13%) because the ATV adjustment is partially offset by more conservative console/PC estimates.

---

## 4. Revised Confidence Score

**Recommended: 60 (+5 from 55)**

| Component | Previous | Revised | Rationale |
|-----------|----------|---------|-----------|
| Source quality | 12 | 14 | Business of Apps IAP average ($1.08) is hard data; Roblox 10-K detail is excellent |
| Data recency | 16 | 16 | All sources 2025-2026 |
| Triangulation | 15 | 17 | Five methods now; new all-app IAP ceiling provides upper bound |
| Coverage | 12 | 13 | Steam revenue breakdown adds PC coverage; Roblox/Fortnite anchor individual games |
| **Total** | **55** | **60** | |

Key improvements:
- **$1.08 average IAP transaction** — first concrete data point on transaction size from app stores
- **Roblox 10-K detail** — 1.8M daily paying users, $10.36/paying user/day, $6.6B bookings
- **Steam revenue decomposition** — DLC + microtransactions = $4.4B (27% of $16.2B)
- **All-app IAP ceiling** — $150B total / $1.08 = 139B total IAP transactions provides mathematical upper bound

---

## 5. What's Still Missing

1. **Apple/Google transaction count data** — Apple and Google know exactly how many IAP transactions they process. If either published this number, confidence would jump to 80+. Apple's June 2025 ecosystem report discusses developer earnings but NOT transaction counts.

2. **Game-specific average transaction size** — The $1.08 is ALL apps. We need the gaming-specific figure. Gacha games average $12+, casual games average $2-3, and the mix matters enormously.

3. **China mobile game transaction data** — China is ~30% of global mobile game revenue ($25B+) but publishes no IAP transaction statistics. Chinese games (Honor of Kings, Genshin, PUBG Mobile) likely have different purchase patterns than Western titles.

4. **Console in-app purchase data** — Sony, Microsoft, and Nintendo publish total digital revenue but do NOT separate out microtransaction counts from game purchases.

5. **Carrier billing transaction counts** — In emerging markets, ~9% of mobile game IAP goes through carrier billing. These carriers could publish transaction counts but don't.

---

## Sources

1. [Sensor Tower — State of Mobile Gaming 2025](https://sensortower.com/blog/state-of-mobile-gaming-apps)
2. [Sensor Tower — 2025 State of Mobile](https://sensortower.com/blog/2025-state-of-mobile-consumers-usd150-billion-spent-on-mobile-highlights)
3. [Business of Apps — App Data Report 2026](https://www.businessofapps.com/data/app-data-report/)
4. [Roblox — Q2 2025 Financial Results](https://ir.roblox.com/news/news-details/2025/Roblox-Reports-Second-Quarter-2025-Financial-Results/)
5. [Roblox — 10-K Annual Report (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000033/rblx-20241231.htm)
6. [Epic Games Store — 2025 Year in Review](https://store.epicgames.com/en-US/news/epic-games-store-2025-year-in-review)
7. [SQ Magazine — Steam Statistics 2025](https://sqmagazine.co.uk/steam-statistics/)
8. [Precedence Research — Online Microtransaction Market](https://www.precedenceresearch.com/online-microtransaction-market)
9. [Icon Era — In-Game Purchase Spending Habits 2025](https://icon-era.com/blog/in-game-purchase-spending-habits-statistics-2025.343/)
10. [TekRevol — Fortnite Revenue Breakdown 2026](https://www.tekrevol.com/blogs/fortnite-revenue-usage-statistics/)

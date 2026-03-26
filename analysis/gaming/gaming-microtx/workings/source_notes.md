# In-Game Microtransactions — Source Notes

## Primary Sources

### 1. Sensor Tower — State of Mobile Gaming 2025
- URL: https://sensortower.com/blog/state-of-mobile-gaming-2025
- Data: Mobile gaming IAP revenue = $81B in 2024 (+4% YoY)
- Also: 3.5 trillion hours spent on mobile games (+8% YoY); sessions up 12%
- Quality: HIGH — Sensor Tower tracks App Store and Google Play directly
- Limitation: Does not cover third-party Android stores (China)

### 2. Sensor Tower — 2025 State of Mobile
- URL: https://sensortower.com/blog/2025-state-of-mobile-consumers-usd150-billion-spent-on-mobile-highlights
- Data: Total mobile app consumer spend = $150B in 2024; games = $81B
- Quality: HIGH

### 3. Newzoo — Global Games Market Report 2024
- URL: https://best-of-gaming.be/wp-content/uploads/2024/09/2024_Newzoo_Global_Games_Market_Report.pdf
- Data: Global gaming = $182.7B in 2024; Mobile $100.3B, Console $43.5B, PC $39B
- Quality: HIGH — industry standard report
- Note: Newzoo's mobile figure ($100.3B) includes advertising revenue; Sensor Tower's $81B is IAP-only

### 4. Precedence Research — Online Microtransaction Market
- URL: https://www.precedenceresearch.com/online-microtransaction-market
- Data: Market size $57.89B in 2024; CAGR 7.11% through 2034
- Quality: MEDIUM — narrower definition than our scope
- Uses more conservative boundaries (excludes some IAP categories)

### 5. Research and Markets — Online Microtransaction Market Size
- URL: https://www.researchandmarkets.com/report/online-microtransaction
- Data: $77.8B in 2024, growing to $86.51B in 2025 (CAGR 11.2%)
- Quality: MEDIUM — broader than Precedence but still narrower than our total

### 6. Game Developer — Average IAP Transaction Value
- URL: https://www.gamedeveloper.com/business/report-average-in-game-mobile-transaction-worth-14
- Data: Average mobile IAP = $14; 71% of transactions under $10; $9.99 most popular price point
- Quality: MEDIUM — older study but widely cited; cross-referenced with app store data
- Key insight: 30%+ of revenue from purchases >$50 (whale effect)

### 7. Icon Era — In-Game Purchase Spending Habits Statistics 2025
- URL: https://icon-era.com/blog/in-game-purchase-spending-habits-statistics-2025.343/
- Data: Average gamer spends $147/year on IAP (up from $132 in 2023)
- Quality: MEDIUM — aggregation of multiple sources

### 8. Newzoo / TweakTown — Games Industry 2024 Results
- URL: https://www.tweaktown.com/news/102255/games-industry-made-184-3-billion-in-2024-consoles-segment-was-84-digital/index.html
- Data: Console segment 84% digital; total industry $184.3B (alternate estimate)
- Quality: HIGH

### 9. Business of Apps — Genshin Impact Statistics
- URL: https://www.businessofapps.com/data/genshin-impact-statistics/
- Data: Genshin Impact revenue $710M in 2024 (down from $1.3B in 2023)
- Quality: HIGH — cross-referenced with Sensor Tower data

### 10. PocketGamer — Mobile App Downloads 2024
- URL: https://www.pocketgamer.biz/mobile-app-downloads-hit-136-billion-in-2024-as-revenue-surges-to-150bn/
- Data: 49.6B mobile game downloads in 2024 (-6% YoY)
- Quality: HIGH — Sensor Tower sourced

## Data Quality Assessment

| Metric | Confidence | Rationale |
|--------|-----------|-----------|
| Mobile IAP revenue | 🟢 High | Sensor Tower tracks stores directly |
| PC/Console IAP revenue | 🟡 Medium | Estimated from total platform revenue minus full game sales |
| Average transaction value | 🔴 Low | Few platforms disclose; varies enormously by genre/game |
| Transaction count | 🔴 Low | Derived figure (revenue / ATV); ATV uncertainty propagates |
| Historical trend | 🟡 Medium | Revenue trend is solid; transaction count trend is estimated |
| Growth projections | 🟡 Medium | Multiple industry sources agree on direction, differ on magnitude |

## Key Methodological Concerns

1. **ATV is the critical unknown.** A $5 average vs $15 average creates a 3x difference in
   transaction count. No platform publishes aggregate transaction counts.

2. **Mobile vs PC/Console ATV gap.** Mobile has many more small transactions ($0.99-$4.99)
   while PC/console skews toward $10-25 bundles. Using a single blended ATV would be misleading.

3. **China data opacity.** Chinese mobile gaming (largest single market) uses third-party
   Android stores not fully captured by Sensor Tower. Revenue figures may undercount by 10-20%.

4. **Free-to-play boundary.** Only 3-5% of F2P players make any purchase. The transaction
   count reflects paying users only, not the broader player base.

5. **Revenue recognition timing.** Virtual currency purchases create a transaction at purchase
   time, but the currency may be spent over weeks/months. We count the initial purchase as
   the transaction (matching the payment system perspective).

# In-Game Microtransactions — Assumptions

## A1. Scope Definition

"In-game microtransactions" includes:
- In-app purchases (IAP) in mobile games (skins, gacha, virtual currency, battle passes)
- In-game purchases in PC games (cosmetics, DLC microtransactions, loot boxes)
- In-game purchases in console free-to-play and live-service games
- Virtual currency top-ups (V-Bucks, Genesis Crystals, Robux, etc.)

Excluded:
- Full game purchases (covered in gaming-sales)
- Subscription fees (covered in gaming-sales)
- In-game advertising revenue (not a user transaction)
- Physical merchandise

## A2. Revenue-to-Transaction Conversion

The core challenge: platforms report REVENUE, not TRANSACTION COUNTS.

We use: `Transaction Count = Revenue / Average Transaction Value (ATV)`

### Mobile IAP ATV
- Game Developer (2023 report): average mobile IAP transaction = **$14**
- However, 71% of individual transactions are under $10
- Median transaction is closer to **$5-7** based on price point distribution
- We use **$8.50** as a weighted average that accounts for the heavy tail of whale spending
  but reflects that most individual transactions are small purchases ($0.99-$9.99)

### PC/Console IAP ATV
- PC/console microtransactions tend to be larger (battle passes $10-15, skin bundles $10-25)
- Average estimated at **$12.00** based on typical Fortnite/Valorant/CoD price points
- V-Bucks/currency packs cluster around $10-20

## A3. Platform Revenue Split

Based on Newzoo 2024 and Sensor Tower data:
- Mobile IAP revenue: **$81B** (Sensor Tower 2024)
- PC IAP revenue: **~$18B** estimated (PC gaming = $39B total; ~46% from IAP/microtransactions)
- Console IAP revenue: **~$15B** estimated (Console = $43.5B total; ~35% from IAP/F2P)
- **Total microtransaction revenue: ~$114B** (2024)

Note: The $57.9B-$77.8B "online microtransaction market" figures from Precedence Research
and Research & Markets use narrower definitions (often excluding battle passes, subscription
micro-content, and some mobile IAP categories). We use the broader Sensor Tower + platform
data which aligns with Newzoo's overall market sizing.

## A4. Revenue vs. Gross Bookings

Platform stores take 15-30% commission (Apple/Google 15-30%, Steam 20-30%, console 30%).
Revenue figures from Sensor Tower and Newzoo represent consumer spending (gross bookings),
not net developer revenue. This is the correct basis for counting transactions since each
consumer payment = one transaction regardless of platform cut.

## A5. Double-Counting Flag

Nearly all microtransactions are paid via credit/debit card, PayPal, or digital wallet
(which itself charges a card). These transactions are ALSO counted in:
- Consumer Card Payments (consumer-cards category)
- E-commerce Payments (ecommerce category)
- Digital Wallet volumes

This is noted but not adjusted for — each Universe of Finance category measures its own
domain's transaction volume. The cross-category overlap is documented for the aggregation
layer.

## A6. Growth Rate Assumptions

### Historical
- 2019-2020: +30% (COVID lockdown gaming boom)
- 2020-2021: -5% (post-COVID normalization in mobile)
- 2021-2022: -3% (continued mobile correction, inflation impact)
- 2022-2023: +5% (stabilization and recovery)
- 2023-2024: +7% (mobile rebound per Sensor Tower)

### Projections
- Baseline CAGR 2024-2035: 6% (maturing mobile, growth in emerging markets)
- High: 9% (AI-driven personalization, new platforms like VR/AR)
- Conservative: 3% (regulation, player fatigue, economic headwinds)

## A7. Seasonal Patterns

Gaming microtransactions peak during:
- Holiday season (Nov-Dec): ~1.5x average
- Summer (Jun-Aug): ~1.2x average
- New game/season launches: spike events

Peak TPS estimated at 2.0x average TPS to account for holiday + event stacking.

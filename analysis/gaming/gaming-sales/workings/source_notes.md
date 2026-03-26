# Digital Game Sales & Subscriptions — Source Notes

## Primary Sources

### 1. Newzoo — Global Games Market Report 2024
- URL: https://best-of-gaming.be/wp-content/uploads/2024/09/2024_Newzoo_Global_Games_Market_Report.pdf
- Data: Global gaming = $182.7B; Mobile $100.3B, Console $43.5B, PC $39B
- Digital = $175.8B (96.4%); Physical = $8.5B (3.6%)
- Quality: HIGH — industry standard report

### 2. TweakTown — Games Industry 2024 Results
- URL: https://www.tweaktown.com/news/102255/games-industry-made-184-3-billion-in-2024-consoles-segment-was-84-digital/index.html
- Data: Console segment 84% digital in 2024; total $184.3B (alternate estimate)
- Quality: HIGH — sourced from Newzoo

### 3. Icon Era — Steam Game Statistics
- URL: https://icon-era.com/statistics/steam-game-statistics/
- Data: Steam $10.8B revenue in 2024 (+24%); ~381M indie unit sales
- Also: 18,691 new games released; Winter Sale $950M; Summer Sale $876M
- Quality: MEDIUM — unit sales are indie-only; total units not disclosed

### 4. Epic Games Store — 2024 Year in Review
- URL: https://store.epicgames.com/en-US/news/epic-games-store-2024-year-in-review
- Data: $1.09B total revenue (+15%); 295M customers; 595M free games claimed
- Quality: HIGH — first-party data
- Note: 3rd-party sales declining despite overall revenue growth (Fortnite-driven)

### 5. SQ Magazine — Xbox Game Pass Stats
- URL: https://sqmagazine.co.uk/xbox-game-pass-subscriber/
- Data: Game Pass exceeded 35M subscribers
- Quality: MEDIUM — Microsoft rarely confirms exact figures

### 6. TweakTown — Xbox Game Pass 35 Million
- URL: https://www.tweaktown.com/news/105672/xbox-game-pass-broke-35-million-subscribers-at-some-point/index.html
- Data: Game Pass peaked above 35M at some point; Microsoft confirmed 34M in Feb 2024
- Quality: MEDIUM

### 7. Statista / Industry Reports — PS Plus Subscribers
- Multiple sources confirm PS Plus at ~51.2M subscribers
- 70% on base tier (Essential), 30% on Extra/Premium
- Quality: HIGH — Sony reports in quarterly earnings

### 8. Icon Era — Digital Sales Ratio 2024
- URL: https://icon-era.com/threads/digital-sales-ratio-2024-edition.14538/
- Data: Xbox Series 91% digital (US); PS5 78% digital; Switch 53% digital
- Quality: MEDIUM — US-centric data; global ratios may differ

### 9. thinglabs — Global Physical Game Revenue 2024
- URL: https://thinglabs.io/global-physical-game-revenue-in-2024-drops-nearly-10-to-just-8-5-billion
- Data: Physical game revenue fell ~10% to $8.5B in 2024
- Quality: MEDIUM

### 10. Udonis — Gaming Industry Report 2026
- URL: https://www.blog.udonis.co/mobile-marketing/mobile-games/gaming-industry
- Data: Historical gaming market sizes 2019-2024; growth rates
- Quality: MEDIUM — aggregation of Newzoo and other sources

## Data Quality Assessment

| Metric | Confidence | Rationale |
|--------|-----------|-----------|
| Total gaming market revenue | 🟢 High | Newzoo is industry standard |
| Digital vs physical split | 🟢 High | Multiple sources agree on 84-96% digital |
| Steam revenue | 🟡 Medium | Valve is private; figures from SteamSpy/estimates |
| Console game unit sales | 🟡 Medium | Sony/Nintendo report units; Xbox does not |
| Subscription counts | 🟡 Medium | Platforms report periodically; not always current |
| Average selling price | 🔴 Low | Varies enormously; no aggregate data published |
| Transaction count | 🔴 Low | Derived figure; ASP uncertainty propagates |
| Monthly vs annual sub split | 🔴 Low | No platform publishes this breakdown |

## Key Methodological Concerns

1. **Digital game revenue includes DLC.** Platform stores (Steam, PSN, Xbox Store) report
   total digital revenue which bundles base games, DLC, and sometimes IAP. We attempt to
   separate IAP (counted in gaming-microtx) but the boundary is fuzzy for DLC-sized content.

2. **Subscription cannibalization.** Game Pass and PS Plus Extra give access to games without
   individual purchases. As subscriptions grow, individual game purchase transactions may
   decline even as total gaming transactions increase (due to subscription renewals).

3. **Free game claims are not transactions.** Epic's 595M free game claims and PS Plus
   monthly games are not counted as transactions since no payment occurs.

4. **Bundled subscriptions.** Game Pass Ultimate includes Xbox Live Gold, EA Play, and cloud
   gaming. We count Ultimate as one subscription, but it represents multiple service bundles.

5. **Regional pricing.** Game prices vary significantly by region (US AAA = $70, Brazil = ~$35
   equivalent, India = ~$20 equivalent). Our ASP estimates are global averages weighted by
   regional revenue share.

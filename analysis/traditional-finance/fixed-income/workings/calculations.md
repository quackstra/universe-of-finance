# Fixed Income — TPS Calculations

## Cash Bond Trade Count

### US Market (TRACE data)

FINRA TRACE reported ~52 million bond transactions in 2024:
- Investment-grade corporate: ~19M trades
- High-yield corporate: ~8M trades (est.)
- Agency/securitized: ~25M trades (est.)

52M trades / 252 trading days = **~206,000 trades/day** (US TRACE-reported)

US Treasury trades (non-TRACE):
- Treasury ADV of $1,055B at average ticket of ~$10-15M = ~70,000-105,000 trades/day
- Central estimate: **~85,000 Treasury trades/day**

Total US: ~206K + ~85K = **~291,000 trades/day**

### Global Extrapolation

US share of global bond trading: ~40-45% (SIFMA estimates US = 40% of global bond market)
- Global fixed income market outstanding: $145T (2024)
- US fixed income outstanding: ~$58T (~40%)
- US share of trading activity likely higher (~45%) due to deeper electronic markets

Global cash bond trades: 291K / 0.45 = **~647K trades/day**
Rounded: **~600,000 trades/day**

## Repo Trade Count (Estimated)

### European Repo
- ICMA Survey: EUR 5T/day combined EU + UK repo turnover
- Average repo ticket size (European): EUR 50-100M
- At EUR 75M average: 5T / 75M = ~67,000 repo trades/day (European)

### US Repo
- Federal Reserve data: ~$4T/day in repo transactions
- US repo is more automated with smaller average tickets (~$25-50M)
- At $37.5M average: $4T / $37.5M = ~107,000 trades/day
- Triparty repo adds ~50,000-100,000 daily transactions
- Total US repo: ~180,000 trades/day

### Rest of World
- Japan, China, other markets: est. ~100,000 trades/day

### Total Global Repo
67K + 180K + 100K = **~350,000 repo trades/day** (institutional/inter-dealer)

However, many repo transactions are overnight auto-roll, with automated systems executing millions of small repo legs:
- Automated overnight repo: est. ~2M additional transactions/day
- Total including automated: **~2.5M repo transactions/day**

## Total Fixed Income

| Component | Daily Trades (est.) |
|-----------|-------------------|
| Cash bonds (global) | 600,000 |
| Repo (institutional) | 350,000 |
| Repo (automated/overnight) | 2,150,000 |
| **Total** | **~3,100,000** |

## TPS Calculation

### Cash Bonds Only
Trading hours: ~8-10h/day (bonds trade primarily in home market hours)
Effective hours: ~9h weighted average

Over trading hours: 600,000 / (9 x 3600) = **~18.5 TPS**
Over 24h (conservative): 600,000 / 86,400 = **~6.9 TPS**

### Including Repo
Over 24h: 3,100,000 / 86,400 = **~35.9 TPS**

## Peak TPS

Peak activity: Treasury auction days, roll dates, month-end
Peak concentration: ~3x average during peak hours
Peak TPS (incl. repo): ~100 TPS

## Annual Totals

Cash bonds: 600,000 x 252 = **~151 million trades/year**
Incl. repo: 3,100,000 x 252 = **~781 million trades/year**

## Annual Value

US Treasuries: $1,055B/day x 252 = ~$266T/year
US Corporate: $57.9B/day x 252 = ~$14.6T/year
Tradeweb total (multi-asset): $2.35T/day ADV

## Confidence Assessment

- US TRACE trade count: 🟢 High — regulatory reporting
- US Treasury ADV (value): 🟢 High — SIFMA/FINRA
- Global trade count: 🔴 Low — extrapolated from US data
- Repo trade count: 🔴 Low — no centralized reporting

# Commodities — TPS Calculations

## Total Exchange-Traded Commodity Volume (2024)

### Bottom-Up from Exchange Data

| Exchange | Commodity Contracts (est.) | Notes |
|----------|---------------------------|-------|
| ICE | 1.2B | Official: record 1.2B commodity contracts |
| CME (energy + metals + agriculture) | ~3.5B | Est. from 26.5M total ADV x 252 days = 6.7B total CME; commodity ~52% of CME volume |
| LME | 179M | Official: 179M lots |
| Shanghai Futures Exchange | ~1.0B | FIA estimate |
| Dalian Commodity Exchange | ~800M | FIA estimate |
| Zhengzhou Commodity Exchange | ~500M | FIA estimate |
| MCX (India) | ~200M | FIA estimate |
| Other exchanges | ~300M | TOCOM, Bursa Malaysia, etc. |

**Bottom-up total: ~7.7B**

BUT: there is significant overlap in reporting:
- CME and ICE report total exchange volume including cross-listed products
- Some Chinese exchange volume is day-trading (open + close same day counted twice)

### Top-Down from FIA

FIA 2024 total ETD: 205.34B contracts
WFE commodity share: ~3% (from subcategory breakdown)
3% x 205.34B = **~6.16B contracts**

FIA commodity subcategory (from WFE data):
- Commodity ETD: ~3% share, growth -4.1% YoY (WFE figures)
- But this seems too low vs. exchange-level data showing growth

### Reconciliation

The discrepancy is because:
1. WFE figures use a narrower member universe than FIA
2. Chinese exchanges may report differently
3. "Commodity" classification varies (some energy derivatives classified elsewhere)

**Central estimate: ~6.5B contracts** (between top-down 6.2B and bottom-up 7.7B after deducting overlaps)

## TPS Calculation

Commodity markets trade in regional time zones:
- US (CME/NYMEX/COMEX): ~23h electronic + pit
- Europe (ICE/LME): ~15h
- Asia (Shanghai/Dalian/Zhengzhou): ~8h
- Weighted effective hours: ~21.6h (same methodology as ETD category)

TPS = 6,500,000,000 / (252 x 21.6 x 3600) = 6,500,000,000 / 19,595,520 = **~332 per second**

Wait — recalculating:
- 6.5B annual / 252 days = 25.8M contracts/day
- 25.8M / (21.6 x 3600) = 25,800,000 / 77,760 = **~332 TPS**

Hmm, but the ETD category reports ~9,500 TPS for 205B contracts. Let me cross-check:
- 205B / (252 x 21.6h x 3600) = 205,000,000,000 / 19,595,520 = ~10,462 TPS

So commodity at 3% share: 10,462 x 0.03 = ~314 TPS. But earlier we reported ~1,200 in the report.

**Correction**: I was using an inconsistent methodology. Let me align with the ETD capsule approach.

If using calendar time (365 days x 24h) like some categories:
- 6.5B / (365 x 86,400) = 6,500,000,000 / 31,536,000 = **~206 TPS**

If using trading days and effective hours (aligned with ETD capsule):
- 6.5B / (252 x 21.6h x 3600) = **~332 TPS**

**Using the ETD capsule methodology (252 trading days, 21.6h effective): ~332 TPS**

I need to revise the report figure from ~1,200 to ~330. The error was in the initial estimate.

CORRECTION APPLIED: Average TPS = **~330** (not ~1,200 as initially estimated)

## Peak TPS Estimate

Peak concentration: ~5x average (commodity markets spike during OPEC announcements, USDA reports, LME warehouse data releases)
Peak TPS: 330 x 5 = **~1,650 TPS**

## Physical OTC Commodity Trades

Physical commodity trading (actual delivery contracts):
- Major trading houses (Vitol, Trafigura, Glencore, etc.): ~5,000-10,000 trades/day each
- Hundreds of smaller traders: ~50,000 trades/day
- Total physical OTC: ~200,000 trades/day = ~50M/year
- TPS contribution: ~2-3 TPS (negligible)

## Annual Value

Commodity ETD notional is hard to estimate (contracts vary enormously):
- Crude oil futures (WTI): ~$70K/contract → 655M contracts x $70K = ~$46T
- Gold futures: ~$200K/contract
- Carbon futures: ~$80/contract
- Total commodity ETD notional: estimated **$150-200T/year** (rough)

## Confidence Assessment

- Exchange-level data (ICE, CME, LME): 🟢 High
- Global aggregate: 🟡 Medium — requires combining multiple exchanges
- Physical OTC: 🔴 Low — no centralized reporting
- TPS: 🟡 Medium — derived from reasonable exchange data

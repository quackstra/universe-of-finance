# Forex — TPS Calculations

## Daily Turnover (Value)

BIS Triennial Survey data:
- April 2022: $7.5T/day (net-net basis)
- April 2025: $9.6T/day (net-net basis)

Interpolated 2024 estimate: $7.5T + (2/3) x ($9.6T - $7.5T) = **~$8.9T/day**
Conservative interpolation used: **~$8.5T/day** (growth may not be linear; 2024 was before 2025 survey spike)

## Estimating Transaction Count

### Approach 1: CLS Settlement Data

CLS Group settles ~500,000 FX trades per day with ~$7T daily settlement value (2024 ADV).

CLS coverage:
- By VALUE: CLS settles ~55-60% of global FX by value
- By COUNT: CLS covers primarily large institutional/interbank trades. Retail and smaller trades are not settled through CLS.
- Estimated CLS coverage by count: ~15-20%

If CLS = 500K trades/day at 17.5% market coverage:
**Total daily trades = 500,000 / 0.175 = ~2.86 million**

### Approach 2: Average Ticket Size

FX market segments:
- Interbank/dealer (45% of value): Average ticket ~$10-20M → ~215K-430K trades/day (from ~$4.3T value)
- Institutional (buy-side, 35% of value): Average ticket ~$2-5M → ~680K-1.7M trades/day (from ~$3.4T value)
- Retail (3-5% of value): Average ticket ~$10K-50K → ~6.5M-32.5M trades/day (from ~$325B value)

Retail FX is problematic: individual retail "trades" on platforms like IG, Plus500, etc. may number in the tens of millions per day, but many are CFDs rather than actual FX spot trades, and most are internally netted by brokers.

Excluding retail CFDs, estimated range: **~2-4 million trades/day**

### Central Estimate

Convergence of both approaches: **~3 million trades/day**

## TPS Calculation

FX market operates ~23.5 hours/day (Sunday 5 PM ET to Friday 5 PM ET, with a ~30 min gap).
Effective trading hours with meaningful volume: ~20 hours/day

Conservative (24h): 3,000,000 / 86,400 = **34.7 TPS**
Effective hours (20h): 3,000,000 / 72,000 = **41.7 TPS**
Rounded central estimate: **~35 TPS**

## Peak TPS Estimate

Peak activity is typically during the London/New York overlap (1-4 PM GMT).
Peak concentration factor: ~4x average (based on hourly volume distributions from CLS data).
Peak TPS estimate: 35 x 4 = **~140 TPS**

## Annual Volume

Annual trading days: ~252
Annual trade count: 3,000,000 x 252 = **~756 million trades**
Rounded: **~750 million trades/year**

Annual value: $8.5T x 252 = **~$2,142 trillion**

## Confidence Assessment

- Daily turnover (value): 🟢 High — BIS triennial survey is authoritative
- Transaction count: 🔴 Low — No official source reports global FX trade counts
- TPS: 🔴 Low — Derived from estimated counts

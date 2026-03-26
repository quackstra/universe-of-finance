# Equity Markets — Assumptions Register

## Core Definitions

| Assumption | Value | Rationale |
|-----------|-------|-----------|
| Definition of "transaction" | One executed trade (matched buy + sell) | Per Universe of Finance methodology |
| Trading days per year | 252 | US market convention; varies by market (245-253) |
| Effective global trading hours/day | 16-22 hours | Overlapping sessions across time zones |
| Primary session hours | 6.5 hours (per market) | Standard for most major exchanges |

## Data Interpretation Assumptions

### WFE "Number of Trades" Metric
- **Assumption**: WFE "number of trades" counts each executed fill as one trade
- **Impact**: If WFE counts order submissions differently, this would change estimates
- **Confidence**: 🟢 High — WFE methodology is well-documented

### World Bank "Stocks Traded, Total Value"
- **Assumption**: World Bank data captures the same scope as WFE electronic order book (EOB)
- **Reality**: World Bank data tends to be narrower (excludes some OTC, negotiated trades)
- **Impact**: Our value estimates may undercount by 15-30%
- **Confidence**: 🟢 High — World Bank sources from WFE/S&P

### Off-Exchange / Dark Pool Inclusion
- **Assumption**: WFE data includes TRF-reported trades in the US
- **Assumption**: Dark pool volume in Europe (~10-15% of equity volume) is partially captured
- **Impact**: If off-exchange is excluded, actual global trades could be 20-30% higher
- **Confidence**: 🟡 Medium — Coverage varies by exchange reporting

## Estimation Assumptions

### Average Trade Size
- **Assumption**: Global blended average trade size ~$1,730 in 2024
- **Derivation**: $106.5T value / 61.5B estimated trades
- **US average**: ~$10,000-15,000 (institutional-heavy)
- **India/China average**: ~$1,000-3,000 (retail-heavy, smaller lots)
- **Trend**: Declining due to fractional shares, retail participation, HFT fragmentation
- **Confidence**: 🟡 Medium

### APAC Share of Global Trade Count
- **Assumption**: APAC represents ~65% of global equity trades by count in 2024
- **Rationale**: India (#3 globally by trade count, +74% YoY), China (SSE + SZSE), Japan, Korea
- **Confidence**: 🟡 Medium — based on WFE regional data + individual exchange reports

### Peak TPS Calculation
- **Assumption**: Peak day sees ~3x average daily volume
- **Assumption**: 20% of peak-day volume concentrates in first 30 minutes of the busiest market
- **Confidence**: 🔴 Low — highly dependent on specific event and market

## Projection Assumptions

### Baseline Scenario (6.0% trade CAGR, 5.0% value CAGR)
- Moderate continued growth in emerging market participation
- Fractional shares become standard globally
- No major regulatory disruption to HFT
- GDP growth ~3% globally, equity returns ~5-7% nominal
- Gradual shift from developed to emerging market share

### High-Growth Scenario (9.0% trade CAGR, 7.5% value CAGR)
- India equity market participation explodes (demat accounts growing 30%+ annually)
- Fractional share trading becomes global standard
- Tokenized equities on blockchain reduce friction
- Emerging market exchanges modernize (Africa, SE Asia)
- Retail participation rises to 40-50% globally (currently 20-35% in developed markets)
- 24/7 trading gains traction in major markets
- Goldman Sachs: EM equity market cap share rises from 27% to 35% by 2030

### Conservative Scenario (3.0% trade CAGR, 3.0% value CAGR)
- SEC/EU HFT regulation reduces algorithmic trade volume
- Payment for order flow (PFOF) ban in EU reduces retail activity
- Tick size reforms (SEC Rule 612 amendments) reduce order fragmentation
- Market consolidation reduces number of venues
- Compliance costs ($1.5B+/year for HFT firms) drive exits
- Geopolitical fragmentation reduces cross-border trading
- Higher interest rates suppress equity valuations

## Known Data Gaps

| Gap | Impact | Mitigation |
|-----|--------|------------|
| No WFE granular annual trade count for 2024 | Must estimate from monthly + growth rates | Triangulated from 3 methods |
| Individual exchange trade counts (not value) scarce | Exchange breakdown is estimated | Used WFE growth rates applied to prior-year baselines |
| Pre-2019 trade count data unavailable | Historical timeseries estimated from value data | Used declining average trade size assumption |
| Dark pool trade counts globally | Off-exchange may be undercounted | Flagged as potential 20-30% undercount |
| Shenzhen/Shanghai individual trade counts | Not published in English sources | Estimated from WFE APAC totals and growth rates |

# OTC Derivatives — Key Assumptions

## Transaction Definition
- One OTC derivative trade = one bilateral contract execution between counterparties
- Includes: IRS, OIS, CDS (index + single-name), equity swaps, commodity swaps, swaptions, exotic options
- FX derivatives: presented for reference but primary count attributed to FX category
- Amendments, novations, and trade lifecycle events are NOT counted as new transactions
- Portfolio compression reducing gross positions does NOT generate new transaction counts

## Scope
- **In scope**: All OTC (bilateral) derivative contracts globally
- **Out of scope**: Exchange-traded derivatives (ETD category), FX spot (FX category), bond trading (fixed income category)
- **Overlap with FX category**: FX forwards, swaps, options appear in both. For aggregation, exclude from here.
- **Overlap with Commodities category**: OTC commodity swaps counted here; physical OTC commodity trades counted in Commodities.

## Value Data
- BIS semiannual statistics: Reports from 65 major dealers in 12 jurisdictions
- BIS triennial survey: Most comprehensive turnover data (every 3 years, in April)
- ISDA SwapsInfo: Weekly/quarterly trade counts from DTCC SDR data (US, EU, UK)
- Notional outstanding =/= market value (gross market value is ~3-4% of notional)

## Trade Count Estimation
- ISDA SwapsInfo is the best available source for IRD and CDS trade counts
- Coverage: US (CFTC reporting), EU (EMIR), UK (FCA) — the three largest OTC derivatives markets
- Rest-of-world extrapolation: Japan ~8%, Asia-Pacific ~8%, other ~4% of global IRD
- Equity and commodity OTC derivatives: no reliable trade count source; estimated from notional and avg trade size

## Market Hours
- OTC derivatives trade during business hours in each jurisdiction
- Global effective hours: ~10-12h/day (overlap between London, New York, Tokyo)
- 252 trading days/year
- TPS reported on 24h basis for consistency with other categories

## Double-Counting Notes
- FX derivatives overlap with FX category — excluded from aggregation total
- OTC commodity swaps overlap with Commodities category — commodity physical trades counted there, swaps here
- Central clearing: a trade counted once at execution, even if subsequently cleared through a CCP
- Trade compression: reduces notional but does not generate new trade counts
- Novation to CCP: counted as one original trade (not original + CCP novation)

## Projection Assumptions
- Baseline (5%): Modest growth from clearing mandates and hedging demand
- High growth (8%): Electronic OTC trading via SEFs, EM market development
- Conservative (2%): Migration to ETD alternatives, compression reduces counts
- Notional growth assumed to outpace trade count growth (larger average trade sizes)

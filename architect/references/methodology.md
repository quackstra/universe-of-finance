# Research Methodology Patterns

> Reusable patterns for measuring financial transaction volumes.

## Pattern 1: Direct Measurement

**When to use**: Data source provides exact transaction counts.

**Examples**: Blockchain explorers, exchange APIs, central bank RTGS statistics.

**Approach**:
1. Identify the authoritative data endpoint
2. Collect raw transaction counts for the measurement period
3. Convert to TPS: `tps = total_transactions / seconds_in_period`
4. For peak TPS, identify the highest single-day or single-hour period

**Confidence**: 🟢 High

## Pattern 2: Reported Aggregate

**When to use**: Organisations report aggregate figures in annual/quarterly reports.

**Examples**: Visa transaction volumes, SWIFT message counts, WFE exchange statistics.

**Approach**:
1. Identify the reporting entity and publication schedule
2. Extract the specific metric (distinguish "transactions" from "messages",
   "trades" from "orders", "volume" from "value")
3. Build timeseries from multiple report periods
4. Convert to TPS using the reporting period length
5. For peak TPS, use daily figures if available; otherwise estimate from
   annual with peak-to-average ratio

**Confidence**: 🟢 High (for reported figures), 🟡 Medium (for peak estimates)

## Pattern 3: Survey-Based Estimate

**When to use**: No direct measurement exists; data comes from surveys or samples.

**Examples**: BIS triennial FX survey, OTC derivatives estimates.

**Approach**:
1. Identify the survey methodology and sample
2. Note the survey date and extrapolation method
3. Use reported figures as point estimates
4. Apply confidence interval based on survey methodology
5. For inter-survey years, interpolate or use growth rate assumptions

**Confidence**: 🟡 Medium

## Pattern 4: Derived Estimate

**When to use**: No direct count available; must be calculated from related data.

**Examples**: Gaming microtransactions (derived from revenue and average price),
IoT payments (derived from device counts and usage patterns).

**Approach**:
1. Identify the derivation formula: `transactions = revenue / avg_transaction_value`
   or `transactions = users × avg_transactions_per_user × active_rate`
2. Source each input variable independently
3. Calculate the estimate
4. Provide a range (low/mid/high) based on input variable uncertainty
5. Cross-validate against any available partial data

**Confidence**: 🔴 Low to 🟡 Medium (depending on input quality)

## Pattern 5: Bottom-Up Aggregation

**When to use**: Category is composed of multiple sub-segments with independent data.

**Examples**: "All consumer payments" = cards + digital wallets + bank transfers + cash.

**Approach**:
1. Enumerate all sub-segments
2. Research each sub-segment independently
3. Sum the sub-segment figures
4. Apply double-counting correction if segments overlap
5. Cross-validate against any top-down aggregate

**Confidence**: Inherits from weakest sub-segment

## Projection Patterns

### CAGR Extrapolation
- **Best for**: Mature, stable-growth categories
- **Method**: Calculate 5-year CAGR from historic data, project forward
- **Risk**: Assumes past growth continues; fails at inflection points

### S-Curve Model
- **Best for**: Emerging categories with adoption dynamics
- **Method**: Fit logistic curve to adoption data; requires estimated ceiling
- **Risk**: Ceiling estimate is subjective; timing of inflection uncertain

### Driver-Based Model
- **Best for**: Categories with identifiable structural drivers
- **Method**: Model = f(population, smartphone penetration, GDP growth, ...)
- **Risk**: Driver relationships may not be stable

### Scenario Matrix
- **Best for**: Categories with high uncertainty
- **Method**: Define 2-3 key uncertainties, create scenarios for each combination
- **Risk**: Combinatorial explosion; keep to 3 scenarios max

## Anti-Patterns to Avoid

1. **False precision**: Reporting "4,237,891 TPS" when the real answer is
   "roughly 4 million". Always match precision to confidence.

2. **Apples to oranges**: Comparing Visa's "transaction volume" (authorization
   count) with SWIFT's "message count" (may include non-payment messages).
   Define terms precisely for each source.

3. **Survivorship bias**: Only measuring the big players and extrapolating.
   Long-tail small platforms may be significant in aggregate.

4. **Conflating value and volume**: $7.5 trillion/day in FX sounds massive,
   but the transaction COUNT may be modest. Always separate volume from value.

5. **Ignoring seasonality**: Holiday shopping, month-end settlements, tax
   deadlines all create seasonal peaks. Annual averages smooth these out.

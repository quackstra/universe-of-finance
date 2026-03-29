# MEST Time-Series Analysis

> Is the global economy getting more or less MEST-intensive over time?
> What forces are compressing or expanding the average MEST multiplier?

---

## The Central Question

The MEST Number (~545,000/s in 2025) is a function of two variables:

```
    MEST/s  =  Transaction Volume (TPS)  x  Average MEST Multiplier

    If TPS grows 8% per year but the multiplier drops 2% per year,
    MEST growth is only 6% per year.

    If both TPS and the multiplier grow, MEST growth compounds.
```

This analysis examines whether the average MEST multiplier (currently
~7.4x) is rising or falling, and what that means for the trajectory of
the MEST Number.

---

## Forces Reducing the MEST Multiplier

### 1. Real-Time Settlement Adoption

**Mechanism:** Real-time payment systems (UPI, Pix, FedNow, Faster
Payments) collapse the clearing and settlement phases into a near-atomic
operation. While our validation shows they do not eliminate MESTs (the
same bilateral state changes still occur), they reduce *some* overhead:

- Batch clearing MESTs (ACH operator sorting, batching) are eliminated
  when payments settle individually in real-time
- Reconciliation MESTs are reduced (fewer end-of-day batch reconciliation
  events between banks)
- Float management MESTs disappear (no need to track pending settlements)

**Scale of adoption:**
- UPI: launched 2016, now 21B+ transactions/month (2025)
- Pix: launched 2020, 64B transactions in 2024 (+53% YoY)
- FedNow: launched 2023, ~1.5% of US payment volume (growing)
- Global real-time payments: expected to reach 575B transactions by 2028
  (17% CAGR)

**MEST impact:** Real-time systems reduce the bank transfer multiplier
from ~5.5x (pure batch) to ~5x (blended) — a modest reduction. The
savings come from eliminating batch-specific overhead, not from reducing
the core bilateral state changes.

**Estimated MEST multiplier reduction: -0.1 to -0.3 per category affected**

### 2. Crypto/DeFi Intermediary Elimination

**Mechanism:** Blockchain-native transactions eliminate clearing houses,
CSDs, custodians, and correspondent banks. A DeFi swap is 2-3 MESTs vs.
10x for an equivalent equity trade through traditional infrastructure.

**Scale:**
- L1/L2 blockchain: ~415 TPS (tiny vs. traditional finance)
- DeFi TVL: ~$100B (small vs. $500T+ traditional)
- CEX: ~3,210 TPS with 4x multiplier (vs. 10x for equities)

**But this is substitution, not compression.** Crypto doesn't reduce the
MEST multiplier of traditional finance — it creates a parallel system
with inherently lower multipliers. The *weighted average* drops because
a growing share of transactions occur on low-MEST rails.

**Estimated impact on global average multiplier: -0.05 to -0.1**
(negligible in 2025 due to small share of global volume)

### 3. T+2 -> T+1 -> T+0 Settlement Compression

**Mechanism:** Shorter settlement cycles reduce counterparty risk and
margin requirements but, critically, do not eliminate processing steps.
Our validation confirmed that T+1 (implemented May 2024) compressed
the *timeline* without removing any MESTs.

**Timeline:**
- Pre-2017: T+3 was standard in most markets
- 2017: US moved to T+2
- 2023: India introduced T+1, optional T+0
- 2024: US, Canada, Mexico moved to T+1
- 2027: EU, UK, Switzerland plan T+1
- Future: T+0 under SEC evaluation

**MEST impact:** T+1 reduced the NSCC clearing fund by 23% (~$2.38B
freed) but the number of processing steps is unchanged. T+0 *could*
eliminate some clearing MESTs by making trade execution and settlement
atomic, but this is not yet implemented at scale.

**Estimated MEST multiplier reduction: 0 (current), -0.5 to -1.0 for
trading categories if/when T+0 is adopted**

### 4. Open Banking / PSD2

**Mechanism:** Open banking enables direct account-to-account payments
via APIs, bypassing card networks and their associated 7-MEST cascade.
A PSD2-initiated payment goes: Payer -> PISP -> Payer's Bank -> Payee's
Bank -> Payee, with ~3-4 MESTs instead of 7x through the card network.

**Scale:**
- EU open banking users projected at 132M+ in 2024
- PSD2 Payment Initiation Services (PIS) growing but still small share
  of total payments
- Card networks remain dominant for consumer payments

**MEST impact:** Each payment diverted from cards (7x) to open banking
(3-4x) saves 3-4 MESTs. But adoption is still early stage.

**Estimated MEST multiplier reduction: -0.05 to -0.1 on the global
weighted average** (growing as adoption increases)

---

## Forces Increasing the MEST Multiplier

### 1. Regulatory Reporting Expansion

**Mechanism:** Post-2008 regulation has dramatically expanded the number
of reports per trade. Each regulatory report where a counterparty and
regulator both have material interest in accuracy is a MEST.

**Key regulatory expansions (2015-2025):**

| Regulation | Year | Impact on MESTs |
|-----------|------|-----------------|
| EMIR (EU derivatives reporting) | 2014+ | +1-2 MESTs per OTC derivatives trade |
| MiFID II/MiFIR (trade/transaction reporting) | 2018 | +1 MEST per securities trade (transaction report to NCA) |
| Dodd-Frank (US derivatives clearing mandate) | 2013+ | +1-2 MESTs per swap (clearing + trade repository) |
| SFTR (securities financing reporting) | 2020 | +1 MEST per repo/securities lending trade |
| EMIR Refit (expanded fields, digital tokens) | 2024 | +0.5 MESTs per trade (more granular reporting) |
| MiFIR 3 (expanded scope, new identifiers) | 2025+ | +0.5 MESTs per trade (Chain IDs, aggregated order IDs) |

**Cumulative effect:** A securities trade in 2015 required ~1 regulatory
report MEST. In 2025, the same trade may require 2-3 regulatory report
MESTs (transaction report, trade report, position report, each to a
different regulator or repository).

**Estimated MEST multiplier increase: +0.5 to +1.0 for trading categories,
+0.2 for payments** (CTR/SAR thresholds unchanged but monitoring
increased)

### 2. AML/KYC Compliance Layers

**Mechanism:** Enhanced due diligence, transaction monitoring, and
sanctions screening add verification MESTs. When a bank screens a
transaction against sanctions lists and the result is shared with a
compliance authority or recorded in a bilateral system, that is a MEST.

**Growth indicators:**
- Global AML market: growing from $4.1B (2025) to $9.4B (2030), 17.8% CAGR
- RegTech market: projected to exceed $22B by mid-2025, 23.5% CAGR
- Compliance cost: exceeds $45B/year in Asia-Pacific alone
- Transaction monitoring automation: 70%+ of KYC to be automated by 2025

**MEST impact:** Most screening is internal (not bilateral, so not a
MEST). But suspicious activity reports (SARs), currency transaction
reports (CTRs), and cross-border reporting create bilateral MESTs between
FI and regulator. The threshold for reporting hasn't changed, but the
*volume* of flagged transactions has increased due to better detection.

**Estimated MEST multiplier increase: +0.1 to +0.2 across payments
categories**

### 3. BNPL Transaction Multiplication

**Mechanism:** A single purchase generates 3-4 installment payments, each
with its own payment cascade. BNPL literally multiplies the number of
underlying transactions.

**Growth indicators:**
- BNPL GMV: $109B in 2024, projected $597B by 2026
- Typical structure: 4 installments per purchase
- Average BNPL loan: $135 over 6 weeks
- 63% of BNPL users had multiple outstanding loans simultaneously (2022)

**MEST calculation:** One BNPL purchase = 1 merchant payment (paid upfront
by BNPL provider, ~5 MESTs) + 3-4 installment collections from consumer
(each ~3-4 MESTs on underlying rail) + credit decision MEST + final
reconciliation MEST.

Total: ~18-22 MESTs per purchase, vs. ~7 for a single card purchase.
The 6x multiplier we assigned captures this at the BNPL-transaction level,
but the broader impact is that each BNPL adoption *replaces* a 7x card
transaction with a 6x BNPL transaction that generates 3-4 *additional*
card/bank transactions underneath.

**Estimated MEST multiplier increase: +0.05 to +0.1 on global weighted
average** (BNPL is still <5% of e-commerce)

### 4. Embedded Finance / Platform Layers

**Mechanism:** When financial services are embedded in non-financial
platforms, additional intermediary layers are created. A payment through
an embedded finance platform flows: Consumer -> Platform -> Enabler ->
Bank -> Network -> Issuer -> ..., adding 1-2 MESTs per additional layer.

**Growth:**
- Embedded finance market: $148B (2025), projected $1.7T by 2034 (31.5% CAGR)
- Structure: platforms, enablers, and license holders each add a layer
- BaaS (Banking-as-a-Service) creates additional bilateral relationships

**Estimated MEST multiplier increase: +0.1 to +0.3 for affected
categories** (primarily consumer payments)

### 5. Sanctions / Geopolitical Fragmentation

**Mechanism:** As the global financial system fragments (Russia/SWIFT
disconnection, China CIPS growth, digital currency experiments), some
transactions require *additional* compliance MESTs for cross-system
interoperability and sanctions checking.

**Estimated MEST multiplier increase: +0.05 to +0.1 for cross-border
categories**

---

## The MEST Multiplier: 2015 vs. 2025

### Category-by-Category Estimate

| Category | Est. 2015 Mult | Est. 2025 Mult | Change | Primary Driver |
|----------|---------------|---------------|--------|----------------|
| Consumer Cards | 7x | 7x | 0 | Stable: four-party model unchanged |
| Digital Wallets | 4x | 5x | +1x | Wallet ecosystems added platform fee + statement MESTs |
| Bank Transfers | 5x | 5x | 0 | Stable: ACH/SWIFT unchanged; RT adoption neutral |
| ETD | 9x | 10x | +1x | EMIR/Dodd-Frank added regulatory report MESTs |
| Equity Markets | 9x | 10x | +1x | MiFID II added transaction reporting MEST; T+1 did not reduce steps |
| Forex | 7x | 8x | +1x | EMIR reporting + CLS expansion |
| Fixed Income | 7x | 8x | +1x | SFTR + MiFID II reporting |
| OTC Derivatives | 10x | 12x | +2x | EMIR + Dodd-Frank clearing mandates + trade repository reporting |
| CEX (Crypto) | 3x | 4x | +1x | Regulatory reporting emerging (MiCA, etc.) |
| L1/L2 Blockchain | 2x | 2x | 0 | On-chain unchanged |

### Aggregate MEST Multiplier Trend

```
    Global Weighted Average MEST Multiplier
    ════════════════════════════════════════

    2015:  ~6.5x
    │
    │  Regulatory reporting expansion pushes trading categories up
    │  Digital wallet maturation adds layers
    │  BNPL creates transaction multiplication
    │  Embedded finance adds intermediary layers
    │
    │  Partially offset by:
    │  Real-time payment adoption (modest reduction)
    │  Crypto substitution (tiny volume effect)
    │  Open banking (early stage)
    │
    2025:  ~7.4x
    │
    │  MEST multiplier increased ~14% over the decade
    │
    │  This means MEST growth has been FASTER than TPS growth:
    │  - TPS grew ~8% CAGR (driven by digital wallets, UPI, Pix)
    │  - MEST multiplier grew ~1.3% CAGR (driven by regulation + layers)
    │  - Total MEST/s grew ~9.4% CAGR
    │
    ▼
    2030:  ~7.8x (projected)
           Forces increasing multiplier (regulation, embedded finance)
           are stronger than forces decreasing it (RT payments, crypto)
           in the near term.
```

### The MEST Number Over Time

| Year | Est. Global TPS | Est. Avg Mult | Est. MEST/s | Annual MESTs |
|------|----------------|--------------|-------------|-------------|
| 2015 | ~35,000 | ~6.5x | ~228,000 | ~7.2T |
| 2018 | ~45,000 | ~6.8x | ~306,000 | ~9.7T |
| 2020 | ~50,000 | ~7.0x | ~350,000 | ~11.0T |
| 2022 | ~60,000 | ~7.2x | ~432,000 | ~13.6T |
| 2025 | ~73,750 | ~7.4x | ~545,000 | ~17.2T |
| 2028 (proj) | ~95,000 | ~7.6x | ~722,000 | ~22.8T |
| 2030 (proj) | ~110,000 | ~7.8x | ~858,000 | ~27.1T |

---

## Scenario Analysis: MEST Multiplier in 2030

### Scenario 1: Regulation Dominates (Multiplier: ~8.2x)

- EMIR Refit, MiFIR 3, and equivalents in Asia add 1+ regulatory MEST per
  trade globally
- Embedded finance reaches $500B+, adding intermediary layers everywhere
- BNPL grows to 15% of e-commerce, multiplying transactions
- Real-time payments grow but don't eliminate MESTs
- T+0 remains experimental

**Result:** ~8.2x multiplier, ~902,000 MEST/s, ~28.4T annual

### Scenario 2: Equilibrium (Multiplier: ~7.8x)

- Regulatory expansion slows as frameworks mature
- Real-time payments reach 30% of bank transfers
- Open banking displaces some card transactions
- T+1 becomes global standard
- Crypto remains <5% of global volume

**Result:** ~7.8x multiplier, ~858,000 MEST/s, ~27.1T annual

### Scenario 3: Compression Accelerates (Multiplier: ~7.0x)

- T+0 implemented in major markets (US, EU, India)
- Open banking captures 20% of consumer payment share from cards
- DeFi/stablecoin adoption grows 10x from current levels
- Regulatory deduplication reduces redundant reports
- Embedded finance consolidation reduces layers

**Result:** ~7.0x multiplier, ~770,000 MEST/s, ~24.3T annual

---

## Key Insights

### 1. The MEST Multiplier Is Rising, Not Falling

Despite the narrative that technology simplifies finance, the average MEST
multiplier has *increased* from ~6.5x (2015) to ~7.4x (2025). The primary
driver is regulation: post-2008 reforms added reporting requirements that
create new bilateral state changes for every trade.

### 2. Real-Time Payments Are a Speed Improvement, Not a MEST Reduction

Our validation confirmed that UPI, Pix, and FedNow process the same
number of bilateral state changes as batch systems. They reduce settlement
*risk* (by compressing the time window) and eliminate *batch overhead*
(sorting, batching) but do not reduce the core bilateral state changes.
Real-time is a UX and risk improvement, not an infrastructure burden
improvement.

### 3. Crypto Is the Only True MEST Compressor — But Its Volume Is Tiny

Blockchain-native transactions have 60-80% fewer MESTs than traditional
equivalents. But at <5% of global transaction volume, the effect on the
weighted average is negligible. Even 10x growth in crypto volume would
only reduce the global MEST multiplier by ~0.1-0.2.

### 4. The Biggest MEST Threat Is T+0 Settlement

Atomic settlement (T+0) is the only force that could fundamentally
compress trading-category multipliers by eliminating the clearing and
settlement cascade. If T+0 becomes standard for equities and ETD, their
multipliers could drop from 10x to 5-6x — a significant reduction
affecting ~25% of total MESTs. But T+0 remains experimental (only India
offers optional T+0 as of 2025).

### 5. The MEST Number Will Cross 1 Million/s by ~2032

Under all three scenarios, the MEST Number grows because TPS growth
(~8% CAGR) dominates any multiplier compression. Even in the most
aggressive compression scenario, MEST/s reaches ~770,000 by 2030.
Crossing 1 million MEST/s is likely by the early 2030s.

---

## Implications for Infrastructure

### What a Rising MEST Multiplier Means

1. **Settlement infrastructure must grow faster than transaction volume.**
   If TPS grows 8%/year but MESTs grow 9.4%/year, clearing houses, CSDs,
   and settlement systems need to scale ahead of the TPS curve.

2. **Regulatory technology is the fastest-growing MEST category.** The
   MESTs driven by regulatory reporting (trade reports, transaction
   reports, position reports, SARs) are growing faster than transaction
   MESTs. This creates a market for RegTech infrastructure that processes
   regulatory MESTs at scale.

3. **The blockchain thesis gets stronger over time.** If the traditional
   MEST multiplier keeps rising (due to regulation and intermediary
   layers) while blockchain MESTs stay at 2-3x, the *efficiency gap*
   widens. This strengthens the long-term case for on-chain settlement
   of traditional assets (RWA tokenization, T+0 via blockchain).

4. **MEST-per-dollar is declining.** While the MEST multiplier per
   *transaction* is rising, the average transaction value is falling
   (due to micropayments, microtransactions, digital wallets). The MEST
   burden per dollar of economic value transferred is roughly flat.

---

```
    MEST Multiplier Trajectory
    ══════════════════════════

    Multiplier
         │
      8.5┤                                          ╱ Scenario 1 (8.2x)
         │                                       ╱
      8.0┤                                    ╱     ╱ Scenario 2 (7.8x)
         │                                 ╱     ╱
      7.5┤                        ───●  ╱     ╱     ╱ Scenario 3 (7.0x)
         │                      ╱      ╱     ╱
      7.0┤                   ●╱     ╱     ╱
         │                ╱      ╱
      6.5┤  ●──────────●      ╱
         │            ╱
      6.0┤         ╱
         │
         └──┬──────┬──────┬──────┬──────┬──────┬──
          2015   2018   2020   2022   2025   2030

    The multiplier has been rising ~1.3% CAGR since 2015.
    Regulatory expansion is the dominant upward force.
    Real-time payments and crypto are modest downward forces.
```

---

*This time-series analysis was produced as part of Universe of Finance
Run 8. Estimates are based on regulatory timeline analysis, real-time
payment adoption data, settlement cycle changes, and MEST validation
findings. March 2026.*

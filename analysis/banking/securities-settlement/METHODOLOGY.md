# Securities Settlement -- Measurement Methodology

## Transaction Definition

One securities settlement transaction = **one delivery-versus-payment (DVP)
or free-of-payment (FOP) instruction that results in a change of ownership
of securities at a Central Securities Depository (CSD) or International CSD**.

Counted at: **netted settlement instruction** (post-CCP netting, post-matching).
Excluded: trade execution (covered in equity-markets/ETD capsules), cash
settlement leg (covered in interbank-rtgs), failed instructions that were
resubmitted (counted once at final settlement), custody/safekeeping events.

---

## Triangulation Approach

### Method A: CSD Annual Reports (Bottom-Up)

Sum reported settlement volumes from the three pillars:
- DTCC (DTC + NSCC + FICC + ATP): ~500M+ estimated
- Euroclear group: 331M confirmed
- Clearstream (ICSD + CSD): ~200M estimated
- T2S overlap adjustment: -50M (Euroclear/Clearstream settle via T2S)

Total: **~1.0-1.1B** (Western CSDs only)

### Method B: Trade-to-Settlement Ratio

Global exchange-traded volumes (~10B+ trades) x observed netting ratio
(5:1 to 10:1) = **1.0-2.0B** settlement instructions.

### Method C: DTCC Value Reverse-Engineering

DTCC processed $3.7 quadrillion in 2024. At average settlement value
per instruction of ~$2.5-5.0M, this implies **740M-1.5B** DTCC
instructions alone.

```
+---------------------------------------------------+
|              RAW ESTIMATES                          |
|                                                     |
|  Method A           Method B           Method C     |
|  [CSD Reports]      [Trade Ratio]      [Value/Avg]  |
|  +------------+     +------------+     +----------+ |
|  | 1.0-1.1B   |     | 1.0-2.0B   |     | 0.74-    | |
|  | (Western)  |     | (global)   |     | 1.5B     | |
|  +-----+------+     +-----+------+     +----+-----+ |
|        |                  |                  |       |
|        +------------------+------------------+       |
|                           v                          |
|              +------------------------+              |
|              |    RECONCILIATION      |              |
|              | Method A misses Asian  |              |
|              | CSDs (China CSDC,      |              |
|              | India NSDL/CDSL, Japan |              |
|              | JASDEC). Adding est.   |              |
|              | 300-500M Asian settl.  |              |
|              | aligns Methods A+B.    |              |
|              +----------+-------------+              |
|                         v                            |
|              +------------------------+              |
|              |   FINAL ESTIMATE       |              |
|              |   1.3-1.5B +/- 200M    |              |
|              |   ~44 TPS (calendar)   |              |
|              |   Confidence: 74/100   |              |
|              +------------------------+              |
+---------------------------------------------------+
```

---

## Reconciliation

The three methods converge at 1.0-1.5B. The spread is driven by:

1. **Asian CSD gap**: China CSDC, India NSDL/CDSL, Japan JASDEC, Korea
   KSD are not included in Method A but contribute significantly to
   Method B's trade-derived estimate
2. **DTCC transaction count opacity**: DTCC publishes value ($3.7Q)
   prominently but does not provide a single headline transaction count
   across all subsidiaries -- the biggest data limitation
3. **Netting ratio uncertainty**: The 5:1 to 10:1 trade-to-settlement
   ratio varies by asset class (equities ~8:1, fixed income ~3:1)

---

## Key Methodological Challenges

### Netting Ratios: 1 Trade =/= 1 Settlement

The relationship between trades executed and settlement instructions is
complex and non-linear:

```
TRADE EXECUTION LAYER          CLEARING LAYER          SETTLEMENT LAYER
+------------------+       +------------------+     +------------------+
| 10B+ global      |       | CCP novation:    |     | 1.3-1.5B net     |
| trades executed  | ----> | 1 trade becomes  | --> | settlement       |
| on exchanges     |       | 2 cleared legs   |     | instructions     |
|                  |       | (buy-CCP +       |     | at CSDs          |
|                  |       |  CCP-sell)        |     |                  |
|                  |       |                  |     |                  |
|                  |       | Multilateral     |     | Netting ratio:   |
|                  |       | netting: NSCC    |     | 5:1 to 10:1      |
|                  |       | nets ~98% of     |     | (varies by       |
|                  |       | equity value     |     | asset class)     |
+------------------+       +------------------+     +------------------+
```

Key netting ratios:
- **NSCC (US equities)**: Nets ~98% of trade value; ~8:1 trade-to-settlement
- **FICC (US Treasuries)**: ~3:1 to 5:1 (less nettable due to maturity dates)
- **Euroclear**: Reports "netted transactions" (331M) -- already post-netting

### Settlement Instruction Multiplier

One trade can generate multiple settlement instructions:
- DvP instruction (securities leg)
- Cash instruction (payment leg, counted in RTGS)
- Partial deliveries (if securities are sourced from multiple accounts)
- Fails and resubmissions (~2-3% fail rate for US equities)
- Corporate action adjustments

### T+1 Impact (May 2024)

The US move to T+1 settlement compressed the window from 2 business
days to 1 without changing annual transaction counts. Impact:
- **Peak processing intensity increased** (same volume in half the time)
- **Fail rates initially spiked** then normalised
- **FX settlement pressure increased** (less time for cross-border funding)
- NSCC's 545M single-day peak (April 2025) demonstrates capacity headroom

### Euroclear/Clearstream/T2S Overlap

Euro-denominated securities settled via Euroclear or Clearstream may also
transit T2S (the Eurosystem platform). Double-counting risk exists if we
sum all three. We use **Euroclear's netted figure** as the primary count
and treat T2S as infrastructure-level data, not an additive source.

---

## Overlap Analysis

Securities settlement sits between trading and cash settlement:

```
TRADING LAYER                 THIS CAPSULE              CASH LAYER
+------------------+      +-------------------+     +------------------+
| Equity Markets   |      | Securities        |     | Interbank RTGS   |
| ~10B+ trades     | ---> | Settlement        | --> | Cash leg of DVP  |
|                  |      | 1.3-1.5B instrns  |     | settled via      |
| ETD Markets      |      |                   |     | Fedwire/T2/etc.  |
| (futures/options)|      | Counted: the      |     |                  |
|                  |      | securities        |     | Overlap: VALUE   |
+------------------+      | delivery leg      |     | overlaps (same   |
                          +-------------------+     | economic event,  |
                                                    | different leg)   |
                                                    +------------------+

Overlap: INTENTIONAL
A $1M equity settlement is counted as:
  - 1 securities delivery (THIS capsule)
  - 1 cash payment (interbank-rtgs capsule)
These are different dimensions of the same DVP event.
Transaction COUNT overlap is minimal; VALUE overlap is ~100%.
```

---

## Coverage Assessment

```
Category: Securities Settlement (1.3-1.5B annual transactions)

Region            Volume    Share   Data Quality
----------------- -------- ------- ----------------
US (DTCC)         ########   36%   High value data; count estimated
EU (Euroclear)    ######     24%   331M confirmed (press release)
EU (Clearstream)  ####       14%   Annualised from 5-month YTD
EU (T2S)          ###        12%   ECB growth rates, not abs. count
Asia-Pacific      ???         14%   NOT INCLUDED in estimate
                                   (China CSDC, India NSDL/CDSL,
                                    Japan JASDEC -- est. 300-500M)
```

**Coverage gap**: Asian CSDs represent an estimated 300-500M additional
settlement transactions not included in the 1.3-1.5B estimate. If
included, global total could reach 1.8-2.0B.

---

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ---------  --------  ----------  -----------
DTCC Annual Rpt     ████████░  █████████ ██████████  █████░░░░░
Euroclear Results   █████████  █████████ ██████████  ████████░░
Clearstream Stats   ██████░░░  ████████░ █████████░  ██████░░░░
ECB T2S Reports     ██████░░░  ████████░ ██████████  █████░░░░░
BIS CPMI-IOSCO      ████████░  █████░░░░ ██████████  ██████░░░░
                    ---------  --------  ----------  -----------
Composite Score:    74/100     84/100    95/100      60/100
```

**Overall confidence: 74/100** -- Strong authority (CSDs are regulated
infrastructure) but granularity is weak. DTCC's value-centric reporting
and the Asian CSD gap are the two biggest limitations.

---

## Revision History

| Date       | Change                                          | Impact           |
|------------|------------------------------------------------|------------------|
| 2026-03-26 | Initial estimate: 1.3-1.5B, ~44 TPS            | Baseline         |
| 2026-03-26 | Note: Asian CSDs could add 300-500M             | Open question    |

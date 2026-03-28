# Fixed Income / Bond Markets — Measurement Methodology

## Transaction Definition

- **What counts**: One bond trade (purchase or sale) between counterparties, OR one repo transaction (repurchase agreement opening or closing leg)
- **Counting point**: Trade execution (reported to TRACE/MSRB in US; platform confirmation in Europe). Repo counted at the transaction instruction level (each settlement instruction = 1 transaction, per FICC GSD convention)
- **Why this point**: US has mandatory trade reporting (TRACE, MSRB); execution is the only consistently observed event across geographies
- **Key ambiguities**:
  - **Repo inclusion**: The single most consequential definitional decision. Repo adds ~868K trades/day (vs ~448K for cash bonds), nearly tripling the total. We include repo as a segment within fixed income but report both with-repo and without-repo figures
  - **Repo counting convention**: FICC GSD counts settlement instructions, not economic trades. A repo with 10 collateral substitutions generates 10+ FICC transactions from one economic agreement. FICC peak of 1.206M transactions likely includes both repo AND cash Treasury clearing
  - **Overnight vs. term repo**: Overnight repo that rolls daily generates a new transaction each day (same economic position, 252 annual transactions). Similar to FX swap roll inflation
  - **Triparty repo**: One triparty repo may involve hundreds of underlying securities but is booked as one transaction at the triparty agent level
  - **TRACE scope**: Covers corporate, agency, and securitized bonds. Does NOT cover Treasuries or munis (separate systems). TRACE captures 99% of US corporate bond trading

## Triangulation Approach

### Method A: US Bottom-Up (Anchored by TRACE + MSRB)

- **Source**: FINRA TRACE 52M/year (corporate/agency/securitized) + MSRB 14.5M/year (municipal) + Treasury estimate 12.6M/year ($1,055B ADV / ~$21M avg trade)
- **Value**: 79.1M US cash bond trades/year
- **Strengths**: TRACE and MSRB are regulatory mandates with near-complete coverage. MSRB is direct count data. High confidence for US
- **Weaknesses**: Treasury trade count is derived (no consolidated tape for Treasury trade counts). TRACE counts both sides of dealer-to-dealer trades

### Method B: Global Extrapolation

- **Source**: US = ~70% of global cash bond trade count (based on electronic trading adoption and market structure analysis). US 79.1M / 0.70 = 113M global
- **Value**: ~112.9M (with Europe 13.8M, APAC/EM 20M estimated separately)
- **Strengths**: Uses the best-measured market (US) as anchor
- **Weaknesses**: The 70% US share assumption is critical. Europe is less electronified (more voice), which means lower trade counts relative to value. APAC is poorly measured

### Method C: Repo from FICC GSD + LCH RepoClear

- **Source**: FICC GSD peak 1.206M transactions/day (Apr 9, 2025); normal ~600-750K/day, repo portion ~400-500K/day. LCH RepoClear 14.6M trade sides/year (~29K unique trades/day). China exchange repo ~160K trades/day
- **Value**: ~868K repo trades/day globally (~219M/year)
- **Strengths**: FICC peak is a hard data point from DTCC. LCH provides European anchor. China exchange repo adds a previously unknown component
- **Weaknesses**: FICC transaction definition is unclear (settlement instructions vs. economic trades). Bilateral repo is unmeasured. Confidence interval remains wide (113M-378M annually)

```
┌──────────────────────────────────────────────────────────┐
│                  FIXED INCOME COUNT MODEL                  │
│                                                            │
│  US TRACE+MSRB     Global Cash       Repo (FICC/LCH)     │
│  [regulatory data]  [extrapolated]    [hard + estimated]   │
│  ┌──────────┐      ┌──────────┐     ┌──────────┐         │
│  │ 79.1M/yr │      │112.9M/yr │     │ 219M/yr  │         │
│  │ US cash  │      │ global   │     │ global   │         │
│  │ bonds    │      │ cash     │     │ repo     │         │
│  └────┬─────┘      └────┬─────┘     └────┬─────┘         │
│       │                 │                │                │
│       └────────┬────────┘                │                │
│                ▼                         │                │
│       ┌────────────────┐                │                │
│       │ CASH BONDS     │                │                │
│       │ 112.9M/year    │                │                │
│       │ ~3.6 TPS       │                │                │
│       └────────┬───────┘                │                │
│                │                         │                │
│                └─────────┬───────────────┘                │
│                          ▼                                │
│                 ┌──────────────────┐                      │
│                 │ TOTAL FIXED INC  │                      │
│                 │ 331.6M/year      │                      │
│                 │ ~10.5 TPS        │                      │
│                 │ Range: 201-518M  │                      │
│                 │ Confidence: 68   │                      │
│                 └──────────────────┘                      │
└──────────────────────────────────────────────────────────┘
```

## Reconciliation

Cash bond counts are anchored by TRACE (52M) and MSRB (14.5M) — high-confidence regulatory data. The Treasury component (12.6M) is derived and less certain. Global extrapolation assumes US = 70% of count, which is validated by the US having TRACE (no equivalent globally), the deepest corporate bond market, and the highest electronic trading adoption.

Repo counts are anchored by FICC GSD peak data and LCH RepoClear annual data. The key insight from the Run 5 deep dive: previous estimates assumed $75-150M average repo trade size, but FICC data implies ~$9-12M per transaction (because FICC counts settlement instructions, not economic trades). This 8-10x increase in implied trade count per dollar is the most material revision in the fixed income methodology.

## Key Adjustments

### The Repo Inclusion Decision

```
Fixed Income: With vs Without Repo
═════════════════════════════════════════════════════

Cash bonds only:    ████████               112.9M/year  (~3.6 TPS)
                    │
+ US repo:          ██████████████████     238.9M/year
  (FICC ~500K/day)  │
+ Europe repo:      ███████████████████    264.1M/year
  (LCH + Eurex)     │
+ China repo:       ████████████████████   314.5M/year
  (exchange: 160K/d)│
+ Japan + UK + RoW: █████████████████████  331.6M/year  (~10.5 TPS)

Range (low-high):   ████████░░░░░░░░░░░░░  201-518M/year
```

We include repo because:
1. Repo is a fixed income transaction (collateralised by bonds)
2. Repo daily value ($20T+) dwarfs cash bond trading
3. FICC GSD provides hard transaction count data
4. Excluding repo would understate fixed income activity by ~2x

### FICC Transaction Definition Uncertainty

The FICC GSD peak of 1.206M transactions (Apr 9, 2025) is our strongest anchor but has definitional ambiguity:

| Interpretation | Implied repo trades/day | Impact |
|---------------|------------------------|--------|
| Includes cash Treasury + repo; each settlement instruction | ~400-500K repo (our central) | Central estimate |
| Repo only; each economic trade | ~1.0M repo | Would double our repo count |
| All FICC products; heavily inflated by novation/substitution | ~200-300K "real" repo | Would halve our estimate |

This single definitional question is the largest source of uncertainty in the fixed income methodology. A DTCC investor relations inquiry could resolve it.

## Overlap Analysis

```
Fixed Income Overlap Waterfall
═══════════════════════════════════════════════════

Total FI trades (incl repo)  ██████████████████████  331.6M/year
                             │
(-) FX-related repo          ██████████████████████  331.6M/year
    (collateralised by FX,   │  Counted HERE, not
    but counted as FI)       │  in FX category
                             │
(-) Treasury ETD overlap     ██████████████████████  331.6M/year
    (futures on bonds)       │  Treasury FUTURES are
                             │  in ETD category, not
                             │  here. Cash bonds only.
                             ▼
                             ════════════════════════
De-duplicated FI             ██████████████████████  331.6M/year
                             (no reduction — boundary
                              is clean: cash+repo only)
```

- **No overlap with ETD**: Bond futures/options are in the ETD category. This category covers cash bonds and repo only
- **No overlap with OTC Derivatives**: Interest rate swaps are OTC derivatives, not fixed income. This category is cash instruments only
- **Marginal overlap with FX**: Some repo may be collateralised by non-domestic bonds involving FX legs, but this is counted as fixed income per convention

## Coverage Assessment

```
Segment             Coverage   Source            Notes
─────────────────── ────────── ──────────────── ──────────────────
US corporate (TRACE) █████████ FINRA mandatory   99% US coverage
US munis (MSRB)      █████████ MSRB mandatory    14.5M direct count
US Treasury          ██████░░░ Derived from ADV  No trade count tape
US repo (FICC)       ███████░░ DTCC FICC GSD     Peak data + estimates
European bonds       ████░░░░░ Tradeweb ADV      No count equivalent
European repo        ████░░░░░ LCH + ICMA        Outstanding, not count
China repo           ████░░░░░ PBOC + SSE/SZSE   Limited granularity
APAC/EM bonds        ██░░░░░░░ Estimated          No TRACE equivalent
─────────────────── ────────── ──────────────── ──────────────────
Overall: ~55% directly observed (US dominance)
         ~45% estimated (non-US markets)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
FINRA TRACE         ████░░░░░  █████████ ██████████  ██████████
MSRB (munis)        ███░░░░░░  █████████ ██████████  ██████████
SIFMA Statistics    ████████░  █████████ █████████░  ██████░░░░
DTCC FICC GSD       ██░░░░░░░  █████████ █████████░  ████████░░
LCH RepoClear       ██░░░░░░░  ████████░ █████████░  ██████░░░░
Tradeweb ADV        ██░░░░░░░  █████████ ████████░░  ██████░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    58/100     90/100    92/100      72/100
```

- **Score**: 68/100
- **Key drivers of uncertainty**:
  - FICC GSD transaction definition is the single biggest unknown — does 1.206M include both cash Treasury and repo? Both opening and closing legs?
  - Non-US bond trade counts are estimated, not observed. No TRACE equivalent exists outside the US
  - Bilateral repo is unmeasured globally
  - China exchange repo could have dramatically higher or lower per-trade sizes than assumed
  - US Treasury trade count is derived ($1,055B ADV / ~$21M avg trade) — no consolidated trade count tape
- **High-confidence elements**: TRACE (52M), MSRB (14.5M), US Treasury ADV ($1,055B), market outstanding ($145T)

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-26 | Initial report | Run 2: Fixed income category created |
| 2026-03-27 | Count triangulation | Run 4: Bottom-up segmented model |
| 2026-03-28 | Repo deep dive | Run 5: FICC GSD + LCH anchors; repo revised from ~84M to ~219M/year |
| 2026-03-28 | Methodology doc created | Run 6: Formal methodology documentation |

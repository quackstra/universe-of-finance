# Methodology Visual Template

> Standard visual formats for all category and sector methodology documentation.
> Every methodology section MUST include at least one triangulation diagram.

## 1. Triangulation Funnel

Use for showing how multiple independent estimates converge on a final number.

```
┌─────────────────────────────────────────────────┐
│              RAW ESTIMATES                        │
│                                                   │
│  Method A          Method B          Method C     │
│  [Source: X]       [Source: Y]       [Source: Z]  │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐ │
│  │ 850B     │     │ 720B     │     │ 790B     │ │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘ │
│       │                │                │        │
│       └────────────────┼────────────────┘        │
│                        ▼                          │
│              ┌──────────────────┐                 │
│              │  RECONCILIATION  │                 │
│              │  Method A over-  │                 │
│              │  counts X by 15% │                 │
│              │  Method B misses │                 │
│              │  region Y        │                 │
│              └────────┬─────────┘                 │
│                       ▼                           │
│              ┌──────────────────┐                 │
│              │ FINAL ESTIMATE   │                 │
│              │ 773B ± 50B       │                 │
│              │ Confidence: 🟢 91│                 │
│              └──────────────────┘                 │
└─────────────────────────────────────────────────┘
```

## 2. Overlap Waterfall

Use for showing how gross TPS becomes de-duplicated TPS.

```
Gross TPS          ████████████████████████████  86,900
                   │
(-) DeFi/Stable    ████████████████████████████  86,900  (subsets, not added)
    subset         │
(-) E-commerce     ███████████████████████████   85,100  -1,800 (95% overlap)
    overlap        │
(-) Gaming         ██████████████████████████    84,720  -380 (82% overlap)
    overlap        │
(-) Wallet/Card    █████████████████████████     82,750  -1,970 (10% overlap)
    overlap        │
(-) Bill/Payroll/  ████████████████████████      70,741  -12,009
    Insurance      │
    overlap         ▼
                   ════════════════════════════
De-duplicated      ████████████████████         ~70,741 TPS
```

## 3. Source Confidence Matrix

Use for showing data quality across sources for a category.

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Nilson Report       ████████░  ████████  █████████░  ███████░░░
Visa 10-K           ████░░░░░  █████████ █████████░  ██████████
BIS Red Book        ██████░░░  █████░░░░ ██████████  ██████░░░░
McKinsey GPR        ████████░  ██████░░░ ████████░░  ████░░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    78/100     82/100    91/100      68/100
```

## 4. Category Stack Diagram

Use for showing how commerce layers sit on payment rails.

```
┌─────────────────────────────────────────────────┐
│ COMMERCE LAYERS (what people buy)                │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │E-Commerce│ │  Gaming  │ │Insurance │ ...      │
│ │  57.5B   │ │  15.2B   │ │   14B    │         │
│ │ 95% ↓    │ │ 82% ↓    │ │ 90% ↓    │         │
│ └──────────┘ └──────────┘ └──────────┘         │
├─────────────────────────────────────────────────┤
│ CREDIT LAYERS (how purchases are financed)       │
│ ┌──────────┐                                     │
│ │   BNPL   │ 3.6× multiplier                    │
│ │  5.5B → 20B installment events                │
│ └──────────┘                                     │
├─────────────────────────────────────────────────┤
│ PAYMENT RAILS (how money moves)                  │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │  Cards   │ │  Bank    │ │ Wallets  │ ...      │
│ │  772.7B  │ │ Transfers│ │  620B    │         │
│ │          │ │  484B    │ │          │         │
│ └──────────┘ └──────────┘ └──────────┘         │
├─────────────────────────────────────────────────┤
│ SETTLEMENT INFRASTRUCTURE (how it clears)        │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │   RTGS   │ │   CCP    │ │   CSD    │         │
│ │  1,581M  │ │  netting │ │  1.3-1.5B│         │
│ └──────────┘ └──────────┘ └──────────┘         │
└─────────────────────────────────────────────────┘
```

## 5. Regional Heatmap (text-based)

```
Category: Consumer Cards (772.7B annual transactions)

Region          Volume    Share   Growth
─────────────── ──────── ─────── ───────
🇨🇳 China       ████████ 32%     +8%
🇺🇸 USA         ██████░░ 24%     +5%
🇪🇺 Europe      ████░░░░ 16%     +6%
🇮🇳 India       ███░░░░░ 12%     +22%  ← fastest
🇧🇷 LatAm       ██░░░░░░ 8%      +11%
🌍 Rest         ██░░░░░░ 8%      +7%
```

## 6. Methodology Decision Tree

Use for explaining how a category's TPS was derived.

```
START: "How many [X] transactions happen annually?"
  │
  ├─ Is there a primary regulator/authority that publishes counts?
  │   ├─ YES → Use as anchor (e.g., Nilson Report for cards)
  │   │         └─ Cross-validate with operator filings
  │   └─ NO → Go to proxy estimation
  │
  ├─ Proxy Estimation
  │   ├─ Is total VALUE known?
  │   │   ├─ YES → Value ÷ avg transaction size = count
  │   │   │         └─ Sensitivity: avg txn size ±20% → count ±20%
  │   │   └─ NO → Go to bottom-up
  │   │
  │   └─ Bottom-Up
  │       ├─ Sum known operators (>50% coverage?)
  │       │   ├─ YES → Extrapolate remainder by market share
  │       │   └─ NO → Use population/GDP scaling from reference country
  │       │
  │       └─ Validate against top-down GDP ratio or per-capita benchmarks
  │
  └─ RECONCILE all methods
      ├─ Methods agree within 20%? → Confidence: HIGH
      ├─ Methods agree within 50%? → Confidence: MEDIUM
      └─ Methods disagree >50%?    → Confidence: LOW, investigate why
```

## Rules

1. Every METHODOLOGY.md MUST include at least one triangulation funnel
2. Categories with overlap MUST include an overlap waterfall or stack diagram
3. Categories with regional data MUST include a regional heatmap
4. The methodology decision tree should appear in sector-level docs
5. All diagrams use ASCII art (renders in any markdown viewer, no images needed)
6. Numbers in diagrams must match the latest data.json values

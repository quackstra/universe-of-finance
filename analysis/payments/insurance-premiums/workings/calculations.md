# Insurance Premium Payments — Calculations & Derivations

> All math shown step-by-step. Every input is tagged with source and confidence.

---

## 1. Global Insurance Premium Value (2024)

**Primary Source:** Swiss Re sigma No. 3/2025
- Global gross written premiums = **~$7.2 trillion** in 2024
- Life insurance: ~$3.0T (42%)
- Non-life insurance: ~$4.2T (58%)
- Growth: +5.9% over 2023 ($6.8T)

**Cross-check:** IAIS Global Insurance Market Report 2024 cites ~$7.0T for 2023, implying ~$7.4T for 2024 at trend growth. Within 3% of Swiss Re figure.

**Working figure:** $7.2 trillion 🟢 High

---

## 2. Bottom-Up Transaction Count Model

### Step 1: Estimate global policies in force by segment

| Segment | Policies (B) | Source / Reasoning | Confidence |
|---------|-------------|-------------------|------------|
| Auto/Motor | 1.5B | ~1.4B registered vehicles globally (OICA); ~75% insured + fleet policies | 🟡 |
| Health (private) | 2.5B | ~600M in US + 200M EU private + 500M India + 1.2B China/ROW; counted as covered lives | 🔴 |
| Property/Home | 0.5B | ~500M homeowner/renter insurance policies; low penetration in emerging markets | 🔴 |
| Life | 2.0B | Swiss Re estimates ~2B individual life policies in force globally | 🟡 |
| Commercial | 0.2B | Estimated from Lloyd's market size + commercial lines data | 🔴 |
| **Total** | **6.7B** | | |

### Step 2: Apply payment frequency

```
Auto:       1.5B × [0.70 × 12 months + 0.30 × 1 annual] = 1.5B × 8.7 = 13.05B
             → Adjust for lapsed/cancelled mid-year (-33%): ~4.4B ✓
             Reasoning: not all 1.5B policies are active all year; effective
             payment events = policies × avg months active × payment share

Health:     2.5B covered lives → est. 1.5B unique payment relationships
             (family plans, employer-intermediated)
             1.5B × [0.60 × 12 + 0.40 × 4 copays/year] = 1.5B × (7.2 + 1.6) = 13.2B
             → Adjust for public-system-no-premium (-75%): ~3.3B ≈ 3.5B ✓

Property:   0.5B × [0.20 × 12 + 0.30 × 4 + 0.50 × 1] = 0.5B × 4.1 = 2.05B
             → Adjust for escrow bundling (-40%): ~1.2B ✓

Life:       2.0B × [0.50 × 12 + 0.20 × 4 + 0.30 × 1] = 2.0B × 7.1 = 14.2B
             → Adjust for group/employer-paid (-55%): ~6.4B
             → Further adjust for lapsed (-50%): ~3.2B ✓

Commercial: 0.2B × [0.20 × 12 + 0.40 × 4 + 0.40 × 1] = 0.2B × 4.4 = 0.88B ≈ 0.8B ✓
```

### Step 3: Sum and adjust

```
Raw sum:    4.4 + 3.5 + 1.2 + 3.2 + 0.8 = 13.1B

Add:        Payment failures & retries (+5%):     +0.65B
            Mid-term adjustments/endorsements (+2%): +0.26B

Total:      ~14.0B transactions (central estimate)
Range:      12-16B (reflecting uncertainty in policy counts and frequency assumptions)
```

**Result: ~14 billion annual transactions** 🟡 Medium

---

## 3. Average TPS Calculation (2024)

```
Seconds in a year = 365 × 86,400 = 31,536,000

Average TPS = 14 × 10⁹ / 31,536,000
            = 14,000,000,000 / 31,536,000
            = 443.8 TPS
```

**Result: ~444 TPS average** 🔴 Low

---

## 4. Peak TPS Estimation

Insurance premiums have a distinctive temporal pattern:
- Monthly premiums cluster on the 1st and 15th of each month (auto-debit dates)
- Annual premiums cluster in January and renewal anniversary months
- Estimated peak/average ratio: 1.5-1.8x

```
Peak TPS (est.) = 444 × 1.6 = ~710 TPS
Range: 600-800 TPS
```

**Result: ~700 TPS peak** 🔴 Low

---

## 5. Average Transaction Value

```
Avg transaction value = $7.2T / 14B = $514

Cross-check by segment:
- Auto: $4.4B txns × ~$150/month = ~$660B → $150 avg ✓
- Health: $3.5B txns × ~$250/month = ~$875B → $250 avg ✓
- Property: $1.2B txns × ~$500/payment = ~$600B → $500 avg ✓
- Life: $3.2B txns × ~$200/month = ~$640B → $200 avg ✓
- Commercial: $0.8B txns × ~$10,000/payment = ~$8T → problematic

Note: Commercial segment average is skewed by very large commercial policies.
The $514 global average is pulled up by commercial lines.

Excluding commercial: ($7.2T - ~$3T commercial) / (14B - 0.8B) = $4.2T / 13.2B = $318 avg
```

---

## 6. Projection Models

### Baseline

```
Assumptions:
- Premium growth: 5% (2025-2026), 4.5% (2027-2028), 4% (2029-2035)
- Txn count growth = premium growth + 1% (monthly billing shift)
- Effective CAGR: ~5% (2025-2030), ~4.5% (2030-2035)

Year    Txns (B)    TPS
2025    14.7        466
2026    15.4        488
2027    16.2        514
2028    16.9        536
2029    17.8        564
2030    18.6        590
2035    23.8        755    [5yr CAGR from 2030: 5%]
```

### High Growth

```
Assumptions:
- Emerging market insurance penetration doubles
- Microinsurance adds 2B+ policies
- Embedded insurance creates new flows
- CAGR: 8% (2025-2030), 7% (2030-2035)

Year    Txns (B)    TPS
2026    16.4        520
2028    19.3        612
2030    22.8        723
2035    33.0        1046
```

### Conservative

```
Assumptions:
- Developed market saturation
- Climate repricing reduces policy counts
- CAGR: 3% (2025-2030), 2.5% (2030-2035)

Year    Txns (B)    TPS
2026    14.7        466
2028    15.6        495
2030    16.5        523
2035    19.3        612
```

---

## 7. Overlap Calculation

```
Payment channel distribution:
- Direct debit:     45% × 14B = 6.3B → counted in Bank Transfers
- Card payment:     25% × 14B = 3.5B → counted in Consumer Cards
- Bank transfer:    15% × 14B = 2.1B → counted in Bank Transfers
- Cash/check:       10% × 14B = 1.4B → NOT counted elsewhere
- Digital wallet:    5% × 14B = 0.7B → counted in Digital Wallets

Overlap total: 6.3 + 3.5 + 2.1 + 0.7 = 12.6B (90%)
Incremental:   1.4B (10%) → 44 TPS
```

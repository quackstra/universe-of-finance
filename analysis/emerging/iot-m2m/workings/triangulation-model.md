# IoT/M2M Payment Triangulation Model

> Created: 2026-03-27
> Purpose: Bottom-up segment-by-segment triangulation to improve confidence on the ~20B annual transaction estimate (~634 TPS).

## Methodology

The existing REPORT.md estimated 15-25B annual IoT/M2M transactions based on broad industry reports and top-down market sizing. This triangulation builds the estimate bottom-up from six segments, using hard data points where available and clearly-flagged extrapolations where not. Each segment is modelled independently, then overlap is deducted.

**Approach per segment:**
1. Identify installed base or user count (hard data preferred)
2. Estimate transaction frequency per unit (from operator disclosures or proxy data)
3. Cross-check against market value data where available
4. Assign per-segment confidence

---

## Data Sources

| # | Source | Type | Segment |
|---|--------|------|---------|
| 1 | NPCI FASTag Statistics (npci.org.in) | Primary/regulatory | Toll — India |
| 2 | China Ministry of Transport — ETC adoption reports | Government | Toll — China |
| 3 | E-ZPass IAG Statistics (e-zpassiag.com) | Industry body | Toll — US |
| 4 | Transport for London — contactless/Oyster journey data | Operator | Transit — UK |
| 5 | JR East — Suica daily transaction reports | Operator | Transit — Japan |
| 6 | Octopus Card Wikipedia / annual reports | Operator/secondary | Transit — HK |
| 7 | IEA Global EV Outlook 2025 | International org | EV charging |
| 8 | Cantaloupe 2025 Micropayment Trends Report | Industry | Vending |
| 9 | NAMA Census data | Industry body | Vending |
| 10 | IEA Smart Meter deployment data | International org | Smart meters |
| 11 | Astute Analytica / GlobeNewsWire smart meter market report | Industry report | Smart meters |
| 12 | SNS Insider / GM Insights — In-Vehicle Payment Services | Industry report | Connected vehicles |
| 13 | Grand View Research — Wearable Payments Devices Market | Industry report | Wearables |
| 14 | Juniper Research — IoT Payments | Industry report | Cross-segment |
| 15 | PTOLEMUS — Electronic Tolling Europe Study 2023 | Industry report | Toll — Europe |

---

## Model

### 1. Toll Collection & Transit Card Taps

This is the most data-rich segment. We split into electronic toll collection (ETC) and transit smart card taps.

#### 1a. Electronic Toll Collection

| Region | Installed Base / Users | Avg Trips/Year | Annual Txns | Confidence | Source |
|--------|----------------------|----------------|-------------|------------|--------|
| **China** | 300M+ ETC users; >90% expressway coverage | ~40-50 trips/user/year | **12-15B** | Medium | Ministry of Transport reports; market research |
| **India (FASTag)** | ~80M FASTags issued | ~48 trips/year (3.8B txns in FY2023-24) | **4.0-4.5B** | High | NPCI FASTag Statistics: 3.8B in FY23-24, growing ~11% YoY; Dec 2024 = 382M monthly |
| **United States (E-ZPass + SunPass etc.)** | 59M+ E-ZPass devices; plus SunPass, FasTrak, TxTag | ~60-80 trips/device/year | **3.5-5B** | Medium | E-ZPass IAG statistics; IBTTA data |
| **Europe (EETS + national)** | 100M+ vehicles using ETC; 70%+ electronic penetration | ~30-40 trips/year | **3-4B** | Medium | PTOLEMUS; >27 countries integrated |
| **Rest of World** (Brazil, Japan, Australia, Middle East) | ~50M ETC users combined | ~30-40 trips/year | **1.5-2B** | Low | Various national reports |
| **SUBTOTAL** | | | **24-30.5B** | | |

**Midpoint: ~27B toll transactions/year**

This is significantly higher than the original 8-12B estimate in REPORT.md. The original estimate underweighted China (which dominates global ETC volume) and missed India's FASTag system entirely. India alone contributes ~4B+ annual transactions with hard NPCI data.

#### 1b. Transit Smart Card Taps

| System | Cards/Users | Daily Taps | Annual Taps | Confidence | Source |
|--------|------------|------------|-------------|------------|--------|
| **Japan IC cards** (Suica, Pasmo, ICOCA, etc.) | 112M+ Suica alone; ~200M total IC cards | ~20-25M transit + ~3.4M retail/day | **~8-10B** | Medium | JR East: 6.6M daily Suica txns (2018); 300M/month Tokyo metro (2024); retail usage growing |
| **London (Oyster + contactless)** | ~10M active | ~6-8M taps/day | **~2.2-2.9B** | Medium | TfL: ~1.6B contactless + ~0.5-0.6B Oyster journeys in 2024 |
| **Hong Kong (Octopus)** | 33M+ cards; 99% penetration | ~15M taps/day (transit + retail) | **~5.5B** | Medium | Octopus annual reports |
| **China transit cards** (various city systems) | 500M+ users across 40+ cities | ~30-50M taps/day | **~11-18B** | Low | Various city transit authority reports |
| **Other global transit** (Seoul T-money, Singapore EZ-Link, Navigo Paris, etc.) | ~100M users combined | ~15-20M taps/day | **~5.5-7.3B** | Low | Various |
| **SUBTOTAL** | | | **32-44B** | | |

**Midpoint: ~38B transit taps/year**

**CRITICAL OVERLAP NOTE:** Transit card taps are a grey area. Many (especially contactless bank card taps on TfL) are processed as regular card transactions and already counted in consumer-cards. We classify them here because the payment is triggered by a machine (gate/reader) in a semi-autonomous way, but we must deduct overlap later.

#### Combined Toll + Transit: ~65B gross, but transit overlaps heavily with consumer cards.

**For IoT/M2M scope (autonomous device-initiated):**
- Toll collection is clearly M2M (transponder auto-debits): **~27B**
- Transit taps are borderline — the tap is human-initiated but machine-processed. We include only the pure smart-card (non-bank-card) portion: roughly 60% of transit taps = **~23B**
- **Toll + Transit net for M2M: ~50B** (but this broadens the original scope)

**Conservative (matching original REPORT.md scope, toll-only):** **~27B**

### 2. EV Charging Payments

| Data Point | Value | Source |
|-----------|-------|--------|
| Global public charging points (end 2024) | >5 million | IEA Global EV Outlook 2025 |
| Annual additions (2024) | +1.3 million (30% YoY growth) | IEA |
| Average sessions per charger per day | ~2-4 (varies: DC fast = 6-10, AC slow = 1-2) | Industry estimates, ChargePoint disclosures |
| Global EV fleet (end 2024) | ~45M light-duty EVs | IEA |
| Public charging share of total charging | ~20-25% | IEA |

**Bottom-up calculation:**
- 5M public chargers x avg 2.5 sessions/day x 365 = **4.6B sessions/year** (gross)
- Cross-check: 45M EVs x 20% public charging x ~100 public sessions/year = **900M sessions** — this seems low
- Reconciliation: Many chargers in China have lower utilisation; the per-charger estimate likely overstates. Realistic range: **1.5-3B sessions/year**
- Home charging that auto-bills (smart EVSE with automatic utility billing): ~35M home chargers x 250 sessions/year = **8.75B** — but most are just electricity consumption, not separate payment transactions. Only ~10% trigger a distinct payment event = **~0.9B**

**EV Charging total: ~2.5-4B transactions/year**
**Midpoint: ~3B**
Confidence: Medium (IEA charger data is solid; session frequency is estimated)

### 3. Smart Meter Billing Events

| Data Point | Value | Source |
|-----------|-------|--------|
| Global smart meters installed | ~1.8B (end 2025) | Astute Analytica / IEA |
| Billing frequency (current dominant model) | Monthly | Industry standard |
| Meters that trigger automated payment | ~40% (rest are prepaid or manual bill pay) | Estimated |

**Bottom-up calculation:**
- 1.8B meters x 40% auto-pay x 12 months = **8.6B billing events/year**
- Daily/hourly billing (emerging): <1% of meters today = **~65M additional**
- UK example: 33M smart meters x 12 = 396M billing events (matches scale)

**Smart Meter Billing total: ~8-9B transactions/year**
**Midpoint: ~8.5B**
Confidence: Low-Medium (meter count is solid; auto-pay percentage is estimated)

### 4. Vending & Unattended Retail

| Data Point | Value | Source |
|-----------|-------|--------|
| Global vending machines | ~25.4M (2025) | Market reports |
| Cashless-enabled machines | ~58% = ~14.7M | Cantaloupe 2025 report |
| Annual cashless transactions globally | ~8.2B reported | Cantaloupe / industry data |
| Avg cashless txns per enabled machine per day | ~1.5-2 | Derived: 8.2B / 14.7M / 365 |

**Bottom-up calculation:**
- 8.2B annual cashless vending transactions is a direct industry figure
- Cross-check: 14.7M machines x 1.5 txns/day x 365 = 8.0B — consistent
- Additional unattended retail (parking meters, car washes, laundromats, EV chargers already counted separately): ~2-3B

**Vending & Unattended Retail total: ~8-11B transactions/year**
**Midpoint: ~9.5B** (vending only ~8.2B; adding other unattended retail ~1.3B)
Confidence: Medium (Cantaloupe/NAMA data is fairly authoritative for vending; other unattended retail is estimated)

### 5. Connected Vehicle Payments (non-toll, non-charging)

| Data Point | Value | Source |
|-----------|-------|--------|
| Connected cars with payment features | ~225M (15% of 1.5B registered vehicles) | McKinsey; SNS Insider |
| In-vehicle payment market (2025) | $5.4-5.8B | SNS Insider; Future Market Insights |
| Parking + fuel = 47.6% of in-vehicle payments | ~$2.6B | SNS Insider |
| Average transaction value (parking/fuel) | ~$10-15 | Estimated |

**Bottom-up calculation:**
- 225M connected vehicles x ~5% actually use in-vehicle payment features = ~11M active users
- Active users x ~50 autonomous payments/year (auto-parking, auto-fuel, insurance telematics) = **~550M**
- Cross-check from market value: $5.4B / $12 avg = ~450M transactions — broadly consistent

**Connected Vehicle Payments total: ~0.4-0.6B transactions/year**
**Midpoint: ~0.5B**
Confidence: Low (very early market; adoption rates are estimated)

### 6. Wearable Payments

| Data Point | Value | Source |
|-----------|-------|--------|
| Wearable payment devices market (2024) | $58B | Grand View Research |
| Active smartwatches with NFC | ~300M globally | Estimated from shipment data |
| Wearable payment penetration | ~15-20% of smartwatch owners use it regularly | Industry surveys |

**Bottom-up calculation:**
- 300M NFC-enabled wearables x 18% active x ~80 payment txns/year = **~4.3B**
- But these are almost entirely tap-to-pay at POS terminals — human-initiated, not M2M
- True M2M wearable payments (auto-transit, auto-gym-entry, etc.): <5% = **~0.2B**

**Wearable Payments (M2M portion): ~0.1-0.3B transactions/year**
**Midpoint: ~0.2B**
Confidence: Low (most wearable payments overlap entirely with consumer cards; M2M portion is a guess)

### 7. Industrial IoT Payments

No hard data exists for this segment. All estimates are derived from market value.

| Data Point | Value | Source |
|-----------|-------|--------|
| Industrial IoT payment market | ~$27B (from original REPORT.md) | Research Nester |
| Average B2B IoT payment value | ~$500-5,000 | Estimated |

**Top-down from market value:**
- $27B / $2,000 avg = **~13.5M transactions**
- These are high-value, low-frequency (automated procurement, supply chain settlements)

**Industrial IoT total: ~0.01-0.05B transactions/year**
**Midpoint: ~0.02B**
Confidence: Very Low (no direct data; pure estimation)

---

## Results

### Per-Segment Summary

| Segment | Annual Txns (B) | TPS | Confidence | Change from REPORT.md |
|---------|----------------|-----|------------|----------------------|
| Electronic toll collection | **27.0** | 856 | Medium | Was 8-12B; +15B from China/India recount |
| Transit smart card taps (M2M portion) | **23.0** | 729 | Low | New segment (was not separated) |
| EV charging | **3.0** | 95 | Medium | Was 0.5-1B; +2B from 5M charger recount |
| Smart meter billing | **8.5** | 269 | Low-Medium | Was 2-4B; +4.5B from 1.8B meter base |
| Vending & unattended retail | **9.5** | 301 | Medium | Was 3-5B; +4.5B from Cantaloupe data |
| Connected vehicle payments | **0.5** | 16 | Low | Was 0.5-1B; refined to low end |
| Wearable payments (M2M) | **0.2** | 6 | Low | New segment |
| Industrial IoT | **0.02** | 0.6 | Very Low | Was 1-2B; revised sharply down |
| **GROSS TOTAL** | **71.7** | **2,274** | | |

### Overlap Deductions

| Overlap | Deduction | Rationale |
|---------|-----------|-----------|
| Transit taps already in consumer-cards | -23.0B | Transit taps via bank contactless cards (TfL ~60% contactless bank cards). Already counted above as M2M portion only — but the entire transit category is borderline M2M. If we exclude transit entirely: deduct 23B. |
| Wearable payments in consumer-cards | -0.2B | Nearly all wearable payments route through card networks |
| EV charging via card rails | -0B | Already a distinct payment event even if settled on card rails |
| Smart meter via bank transfer rails | -0B | Distinct billing event even if settled via direct debit |

### Three Scoping Models

**Narrow scope (device-autonomous only, no human tap):**
Toll + EV charging + Smart meter + Industrial IoT + Connected vehicle = **39.0B** (~1,237 TPS)

**Medium scope (includes vending/unattended where human presence triggers machine payment):**
Narrow + Vending/unattended = **48.5B** (~1,538 TPS)

**Broad scope (includes transit smart card taps):**
Medium + Transit card taps (M2M portion) = **71.5B** (~2,267 TPS)

### Recommended Estimate (Medium Scope)

**~48.5B transactions/year (~1,538 TPS)**

This is the most defensible scope: it includes payments that are device-initiated or device-mediated (toll transponders, EV chargers, smart meters, vending machines, connected vehicles) but excludes transit taps which are fundamentally human-initiated. This represents a significant upward revision from the original 20B midpoint.

### Updated data.json values

- **avg_tps**: 1,538 (medium scope midpoint)
- **annual_volume**: 48,500,000,000
- **confidence**: low → **low-medium** (triangulated from multiple segments but still relies on estimates for several)
- **Range**: 35-65B (narrow to broad scope)

---

## Overlap Analysis

### What overlaps with other Universe of Finance categories

| This Segment | Overlaps With | Direction | Magnitude |
|-------------|--------------|-----------|-----------|
| Transit smart card taps | Consumer Cards | Transit taps via contactless bank cards are already counted in consumer-cards. ~40% of London transit, ~30% of Tokyo transit uses bank cards. | ~10-15B of the 38B transit taps |
| Wearable payments | Consumer Cards | Nearly 100% of wearable NFC payments are card-rail transactions | ~4.3B (but only ~0.2B was M2M) |
| EV charging | Consumer Cards, Digital Wallets | ~70% of EV charging payments are settled via card or wallet | Settlement overlap, not transaction count overlap |
| Smart meter billing | Bank Transfers | ~80% of smart meter auto-payments are direct debit (bank transfer) | Settlement overlap, not count overlap |
| Toll collection | Bank Transfers, Consumer Cards | ~60% settled via linked bank account, ~30% via linked card | Settlement overlap |
| Vending | Consumer Cards, Digital Wallets | ~77% of cashless vending is card/mobile pay | Settlement overlap |

**Key distinction:** Most IoT/M2M transactions settle on existing payment rails (cards, bank transfers) but represent distinct transaction *events* that would not otherwise exist. A toll transponder beep is a transaction event even though the money moves via a linked Visa card. We count the event, not the settlement.

### Overlap with digital-wallets
Some transit and vending payments go through Apple Pay / Google Pay — these are counted in both IoT/M2M (as the event) and digital-wallets (as the settlement method). Estimated overlap: ~3-5B transactions.

---

## Open Questions

1. **China toll collection volume is the biggest uncertainty.** We estimated 12-15B from 300M users x 40-50 trips/year, but actual utilisation rates could be 20 trips/year (suburban users) or 100+ trips/year (freight trucks). Authoritative data from China's Ministry of Transport would narrow this by 5-10B.

2. **Transit smart card scope decision matters enormously.** Including or excluding transit taps swings the total by 23B (50% of medium-scope estimate). The project should make a clear scoping call.

3. **Smart meter billing frequency is changing.** If utilities move from monthly to daily or hourly billing (as UK smart meter infrastructure supports), the 8.5B could become 100B+ within a decade. This is the micropayment revolution referenced in REPORT.md.

4. **India FASTag is the best-documented M2M system.** NPCI publishes monthly transaction counts. This should be used as the primary calibration point for the model.

5. **The original REPORT.md estimate of 1-2B for Industrial IoT was too high.** B2B automated procurement is high-value, low-frequency. The actual transaction count is likely <50M/year.

6. **Vending machine data from Cantaloupe (8.2B annual cashless transactions) is a game-changer.** This single data point more than doubles the original 3-5B vending estimate and is from the industry's own reporting.

7. **How should we handle transit card retail purchases?** Suica and Octopus are widely used for convenience store purchases (3.4M/day for Suica alone). These are human-initiated retail transactions that happen to use a transit-origin payment method. Currently excluded from our M2M scope.

# IoT & Machine-to-Machine Payments — Transaction Volume Analysis

> Part of the [Universe of Finance](../../../README.md) project.

## Executive Summary

Machine-to-machine (M2M) and IoT payments — where devices autonomously initiate and settle financial transactions without human intervention — are an emerging category with a **deceptively large current footprint and an enormous projected future.** Today, identifiable M2M payment transactions (toll collection, EV charging, vending machines, smart meters) generate an estimated **~15-25 billion transactions per year** (~475-790 TPS), though most are processed through existing card/bank payment rails and are therefore difficult to separate from conventional payment statistics. The autonomous IoT payments market was valued at **~$77 billion in 2025** and is projected to grow at 30-45% CAGR. With **21.1 billion connected IoT devices** in 2025 (growing to ~39 billion by 2030), the potential for device-initiated payments to become a dominant transaction category by the mid-2030s is substantial.

## Scope

This analysis covers payment transactions initiated autonomously by machines or IoT devices:

1. **Electronic toll collection** — RFID/transponder-based highway tolls (E-ZPass, Via Verde, etc.)
2. **EV charging payments** — automated billing at charging stations
3. **Vending & unattended retail** — smart vending machines, micro-markets, parking meters
4. **Smart meter billing** — utility payments triggered by smart meters (electricity, gas, water)
5. **Connected vehicle payments** — fuel, parking, insurance-by-mile, in-vehicle commerce
6. **Industrial IoT payments** — supply chain, logistics, automated procurement

Excluded: Payments merely *processed by* IoT devices but initiated by humans (e.g., tap-to-pay at a store); AI agent transactions (covered separately); crypto-native M2M payments (covered in AI agents).

---

## Current State

### Transaction Volume

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Avg TPS | ~475-790 | Derived from 15-25B annual txns | :red_circle: Low |
| Peak TPS (est.) | ~2,000-3,000 | Rush hour tolling, peak utility billing | :red_circle: Low |
| Daily volume | ~41-68 million | Derived from annual estimates | :red_circle: Low |
| Annual volume (est.) | ~15-25 billion | Aggregated from subcategories ([calculations](workings/calculations.md#1-annual-transaction-estimate)) | :red_circle: Low |
| Market value (2025) | ~$77 billion | [Research Nester](https://www.researchnester.com/reports/autonomous-iot-payments-market/6532) | :yellow_circle: Medium |
| Connected IoT devices | 21.1 billion | [IoT Analytics](https://iot-analytics.com/number-connected-iot-devices/) | :green_circle: High |

### Subcategory Breakdown

| Subcategory | Est. Annual Txns (B) | Market Value ($B) | Notes | Confidence |
|-------------|---------------------|-------------------|-------|------------|
| Electronic toll collection | ~8-12 | ~10.5 | 600M+ ETC users globally; 1.2M equipped lanes | :yellow_circle: Medium |
| Vending & unattended retail | ~3-5 | ~15 | ~15M machines globally; shifting to cashless | :red_circle: Low |
| Smart meter billing | ~2-4 | ~8 | ~1.3B smart meters installed; billing is monthly/quarterly | :red_circle: Low |
| EV charging payments | ~0.5-1 | ~5 | Growing rapidly with EV adoption; ~3M public chargers globally | :red_circle: Low |
| Connected vehicle payments | ~0.5-1 | ~12 | Fuel, parking, tolls via in-car systems | :red_circle: Low |
| Industrial IoT payments | ~1-2 | ~27 | Supply chain, logistics, automated procurement | :red_circle: Low |

### Regional Breakdown

| Region | Share | Notes |
|--------|-------|-------|
| Asia-Pacific | ~40% | China leads in ETC (300M+ users), smart meters, EV charging |
| Europe | ~25% | Cross-border tolling (27+ countries); strong EV charging growth |
| North America | ~25% | E-ZPass network; connected vehicle payments |
| Rest of World | ~10% | Growing toll infrastructure in Middle East, Latin America |

---

## Historic Trend

### IoT Connected Devices (All Types)

| Year | Connected Devices (B) | YoY Growth | Source | Confidence |
|------|----------------------|-----------|--------|------------|
| 2018 | 7.0 | — | IoT Analytics | :green_circle: High |
| 2019 | 8.3 | +19% | IoT Analytics | :green_circle: High |
| 2020 | 9.7 | +17% | IoT Analytics | :green_circle: High |
| 2021 | 11.3 | +16% | IoT Analytics | :green_circle: High |
| 2022 | 13.1 | +16% | IoT Analytics | :green_circle: High |
| 2023 | 16.6 | +27% | IoT Analytics | :green_circle: High |
| 2024 | 18.5 | +12% | IoT Analytics | :green_circle: High |
| 2025 | 21.1 | +14% | IoT Analytics | :green_circle: High |

### IoT Payments Market Evolution

| Year | Market Size ($B, est.) | Notes | Confidence |
|------|----------------------|-------|------------|
| 2020 | ~15 | Early stage; toll + vending dominant | :red_circle: Low |
| 2022 | ~30 | Post-COVID acceleration; contactless adoption | :red_circle: Low |
| 2024 | ~54 | [GM Insights](https://www.gminsights.com/industry-analysis/autonomous-iot-payments-market) | :yellow_circle: Medium |
| 2025 | ~77 | [Research Nester](https://www.researchnester.com/reports/autonomous-iot-payments-market/6532) | :yellow_circle: Medium |

**Key observations:**
- IoT device growth has been steady at ~15% CAGR, providing the infrastructure base for M2M payments
- Most current M2M payments ride on existing payment rails (card networks, bank transfers) and are invisible in payment statistics
- The shift from "device processes a human-initiated payment" to "device autonomously pays" is gradual and hard to measure precisely
- EV charging is the fastest-growing subcategory, tracking electric vehicle adoption (40%+ CAGR)

---

## Growth Rate Analysis

| Period | CAGR | Metric | Context |
|--------|------|--------|---------|
| 2020-2025 | ~38% | Market value | Rapid growth from low base |
| 2023-2030 | ~8% | IoT device count | [GSMA](https://www.gsmaintelligence.com/research/iot-market-forecast-to-2030-connections-by-region-and-vertical) |
| 2025-2030 | ~30-45% | Autonomous IoT payments market | Multiple market research projections |
| 2024-2030 | ~46% | IoT monetisation market | [GM Insights](https://www.gminsights.com/industry-analysis/internet-of-things-iot-monetization-market) |

The disconnect between device growth (~8% CAGR) and payment market growth (~30-45% CAGR) reflects increasing monetisation per device — more devices are being equipped with payment capability, and each payment-enabled device generates more transactions over time.

---

## Projections

> **Note:** This category is uniquely difficult to project because the boundary between "IoT payment" and "regular payment processed by an IoT device" is blurry and shifting. Projections focus on genuinely autonomous, device-initiated payments.

### Baseline (Steady IoT Monetisation)

**Assumptions:**
1. IoT devices reach ~39B by 2030; 5-10% are payment-enabled
2. Average payment-enabled device generates 50-100 transactions/year
3. EV charging grows 35% CAGR; toll collection grows 8%; vending grows 5%
4. No fundamental protocol change — M2M payments continue on existing rails

| Year | Projected TPS | Annual Volume (B) | Payment-Enabled Devices (B) |
|------|---------------|-------------------|-----------------------------|
| 2026 | 950 | 30 | 2.5 |
| 2028 | 1,500 | 47 | 3.5 |
| 2030 | 2,500 | 79 | 5.0 |
| 2035 | 8,000 | 252 | 10.0 |

### High Growth (Autonomous Vehicle + Smart City Boom)

**Assumptions:**
1. Autonomous vehicles begin commercial deployment at scale by 2030, each generating 500+ M2M payments/year
2. Smart city infrastructure (parking, energy, waste) all become payment-enabled
3. Micropayment protocols (streaming payments for utilities, pay-per-use everything) emerge
4. IoT devices reach 50B by 2030; 15-20% payment-enabled

| Year | Projected TPS | Annual Volume (B) | Payment-Enabled Devices (B) |
|------|---------------|-------------------|-----------------------------|
| 2026 | 1,200 | 38 | 3.0 |
| 2028 | 3,000 | 95 | 5.0 |
| 2030 | 10,000 | 315 | 10.0 |
| 2035 | 50,000 | 1,577 | 25.0 |

### Conservative (Slow Monetisation)

**Assumptions:**
1. Payment enablement stays below 5% of IoT devices
2. Most M2M payments remain toll collection and vending — mature, slow-growth categories
3. EV charging grows but doesn't transform payment patterns
4. No micropayment revolution — batch billing persists

| Year | Projected TPS | Annual Volume (B) | Payment-Enabled Devices (B) |
|------|---------------|-------------------|-----------------------------|
| 2026 | 700 | 22 | 2.0 |
| 2028 | 900 | 28 | 2.5 |
| 2030 | 1,200 | 38 | 3.0 |
| 2035 | 2,500 | 79 | 5.0 |

*Full projection tables: [workings/calculations.md](workings/calculations.md#4-projection-models)*

**2035 Range:** M2M payment volumes could range from **~2,500 TPS (conservative) to ~50,000 TPS (high growth)** by 2035. The high-growth scenario would make IoT payments rival consumer card payments in transaction count, driven by the shift to pay-per-use models and autonomous vehicle deployment.

---

## Key Findings

1. **IoT payments are already large but invisible.** An estimated 15-25B annual transactions already occur as M2M payments, but they flow through existing card/bank rails and are counted as regular payments. The category's true size is hidden in other statistics.

2. **Toll collection is the mature anchor.** With 600M+ ETC users and 8-12B transactions/year, electronic tolling is the most established M2M payment category. It demonstrates the pattern: start as a convenience feature, become the default, then enable new business models (congestion pricing, usage-based road tax).

3. **EV charging is the growth catalyst.** EV charging payments are growing 35%+ annually and represent the most visible new M2M payment category. By 2030, with 50M+ EVs on the road, charging alone could generate 2-5B transactions/year.

4. **The micropayment revolution is the wild card.** If IoT devices shift from batch billing (monthly utility bills) to streaming micropayments (pay-per-kWh, pay-per-minute parking), transaction counts could increase 100x without changing total value. This is the key assumption separating conservative from high-growth scenarios.

5. **21 billion devices, but only ~10% pay for anything.** The vast majority of IoT devices (sensors, monitors, cameras) generate data but not payments. The key metric is not total IoT devices but payment-enabled devices, which is growing faster than the overall IoT base.

6. **Autonomous vehicles are the 2030s catalyst.** A single autonomous vehicle could generate 500+ M2M payments per year (tolls, charging, parking, insurance, maintenance). A fleet of 10M autonomous vehicles would add 5B+ transactions annually.

---

## Data Quality & Limitations

- **Separation problem:** The biggest challenge is separating M2M payments from human-initiated payments processed by IoT devices. A contactless tap at a parking meter is M2M; a tap at a coffee shop is not. The boundary is subjective.
- **Market size figures vary wildly.** Different research firms define "IoT payments" differently, producing estimates ranging from $2.5B (micro-payments only) to $430B+ (all IoT-adjacent payment value). We use the $77B figure from Research Nester as a mid-range for autonomous IoT payments specifically.
- **Transaction count data is :red_circle: Low confidence throughout.** No organisation tracks "M2M payment transactions" as a distinct category.
- **Regional data is sparse** outside of toll collection (where China and Europe publish reasonably good data).
- **Projection models for this category are more speculative than most** because the growth depends on technology adoption curves (autonomous vehicles, smart meters, micropayment protocols) that are inherently uncertain.

---

## Open Questions & Triangulation Opportunities

### What We Can't Directly Observe
- **Most IoT payments are invisible** — bundled into utility bills, toll invoices, fleet management fees, or subscription charges. The payment is device-initiated but appears in payment system data as a regular card/bank transaction.
- **Payment-enabled device percentage**: We estimate 5-10% of 21.1B IoT devices are payment-enabled, but no authoritative source tracks this. The true figure could be 3% or 15%.
- **Micropayment vs batch billing split**: A smart meter can generate a monthly bill (1 transaction) or a per-kWh streaming payment (thousands of transactions). The current split is unknown and the trend direction is the key variable for projections.
- **Industrial IoT payment volume**: B2B automated procurement and supply chain payments are the most opaque subcategory. Transaction counts and values are not reported by any public source.

### Triangulation Strategies
| Gap | Approach | Proxy Data Available | Expected Precision |
|-----|----------|---------------------|-------------------|
| Toll collection volume | China: 300M+ ETC users x avg 40 trips/year = 12B tolling events. Europe: Viapass, ASFINAG publish transaction counts. US: E-ZPass handles ~12B transactions/year across 19 states. | National toll authority annual reports; IBTTA (International Bridge, Tunnel and Turnpike Association) data | :green_circle: |
| EV charging sessions | Global public chargers (~3M in 2024). At avg 2-3 sessions/day per charger = 2.2-3.3B sessions/year. Cross-check with IEA Global EV Data Explorer. | IEA Global EV Outlook; BloombergNEF EV charging data; ChargePoint/EVgo quarterly earnings (sessions disclosed) | :yellow_circle: |
| Smart meter billing frequency | 1.3B smart meters installed globally (IEA). If 90% bill monthly = 14B billing events. If 10% shift to daily/hourly = add 45B+ events. | IEA smart meter deployment data; utility company annual reports on billing frequency | :yellow_circle: |
| Vending machine transactions | ~15M vending machines globally. At 50-100 cashless transactions/day per machine with 40% cashless adoption = 110-220B transactions/year? No — only ~30% of machines are payment-enabled. Revised: ~5M machines x 30 cashless txns/day = 55B/year? This seems too high. Cross-check with industry reports. | NAMA (National Automatic Merchandising Association) data; Japan Vending Machine Association (Japan has 4M+ machines) | :red_circle: |
| Connected vehicle payments | 1.5B registered vehicles globally; ~15% have connected payment features (2024). At 10-20 autonomous payments/year (fuel, tolls, parking) = 2.3-4.5B transactions. | McKinsey Connected Car report; OEM connected services subscriber counts (GM OnStar, BMW ConnectedDrive) | :yellow_circle: |

### Key Modeling Questions
- **The micropayment revolution is the single biggest uncertainty.** If utilities, tolling, and parking shift from batch billing to per-use micropayments, IoT transaction counts could increase 100x without changing total payment value. What are the incentives for this shift, and which jurisdictions/sectors will adopt first?
- How many EV charging transactions will there be by 2030? This depends on: EV fleet size (projected 150-230M by 2030), public vs home charging split (currently ~20% public), and sessions per public charger per day. At 200M EVs x 20% public x 100 sessions/year = 4B transactions — but this could be 2B or 10B.
- What is the autonomous vehicle M2M payment multiplier? A single autonomous taxi could generate 50+ M2M payments per day (per-ride insurance, per-kWh charging, per-minute parking, toll per segment, maintenance alerts). At scale, 10M autonomous vehicles could add 180B+ transactions/year.
- Will IoT payments remain on card/bank rails or migrate to crypto micropayment channels? If IOTA, Lightning Network, or similar protocols capture IoT micropayments, these transactions would shift from the card/bank ecosystem to a new rail entirely.

### Reference Comparisons
- **E-ZPass as mature M2M benchmark**: The US E-ZPass network processes ~12B toll transactions/year across 19 states and 40+ agencies. This is the best-documented M2M payment system and can serve as a calibration point for other regions.
- **ChargePoint quarterly disclosures**: ChargePoint (the largest US EV charging network) reports quarterly charging sessions and revenue. In Q3 2024, ChargePoint reported ~70M charging sessions. Annualised across all networks globally, this suggests 500M-1B EV charging transactions in 2024 — consistent with our 0.5-1B estimate.
- **Smart meter deployment curve as payment predictor**: IEA reports 1.3B smart meters installed globally, growing ~10% annually. Not all smart meters trigger autonomous payments today (most just enable automated meter reading), but the installed base provides the infrastructure for future payment automation. The conversion from "smart metering" to "smart billing/payment" is the key adoption metric to watch.

---

## Sources

1. [IoT Analytics — Number of Connected IoT Devices Growing 14% to 21.1 Billion](https://iot-analytics.com/number-connected-iot-devices/)
2. [Ericsson — IoT Connections Forecast (Mobility Report)](https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/iot-connections-outlook)
3. [GSMA Intelligence — IoT Market Forecast to 2030](https://www.gsmaintelligence.com/research/iot-market-forecast-to-2030-connections-by-region-and-vertical)
4. [Research Nester — Autonomous IoT Payments Market Size & Share 2037](https://www.researchnester.com/reports/autonomous-iot-payments-market/6532)
5. [GM Insights — Autonomous IoT Payments Market Size 2024-2032](https://www.gminsights.com/industry-analysis/autonomous-iot-payments-market)
6. [GM Insights — IoT Monetization Market Size 2025-2034](https://www.gminsights.com/industry-analysis/internet-of-things-iot-monetization-market)
7. [Introspective Market Research — IoT Payments Market to Reach $14,886B by 2030](https://introspectivemarketresearch.com/press-release/iot-payments-market/)
8. [RealTime Data Stats — IoT-Based Micro-Payments Market 2030](https://realtimedatastats.com/research-report/iot-based-micro-payments-market)
9. [Mastercard — How IoT Will Shape the Future of Payments (2021)](https://www.mastercard.com/news/media/wddjfrhn/how-iot-will-shape-the-future-of-payments.pdf)
10. [GlobeNewsWire — Electronic Toll Collection Market to $20.56B by 2033](https://www.globenewswire.com/news-release/2024/03/22/2850890/0/en/Global-Electronic-Toll-Collection-Market-Size-To-Worth-USD-20-56-Billion-By-2033-CAGR-Of-7-71.html)
11. [Transforma Insights — IoT Forecast Highlights](https://transformainsights.com/research/forecast/highlights)

# IoT & Machine-to-Machine Payments — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. M2M Payment Definition
**Assumption:** An M2M payment is one where the device autonomously initiates the payment without direct human action at the point of transaction.
**Reasoning:** This excludes tap-to-pay at a store (human-initiated via IoT device) but includes toll transponders (device-triggered as vehicle passes), EV chargers with auto-billing, and smart meter-triggered utility payments.
**Risk:** The boundary is subjective. A parking meter payment could be human-initiated (tapping a card) or M2M (licence plate recognition + auto-billing). We include both in our estimates because the infrastructure is IoT-based.

### A2. Existing Rail Invisibility
**Assumption:** Most M2M payments today are processed through existing card networks or bank transfer systems and are not separately identifiable in payment statistics.
**Reasoning:** A toll payment via E-ZPass ultimately settles as a card charge or ACH debit. From the payment network's perspective, it's just another transaction.
**Risk:** This means our estimates may double-count with other Universe of Finance categories (consumer cards, bank transfers). The intent is to measure IoT-initiated transactions regardless of settlement rail.

---

## Transaction Count Assumptions

### A3. Toll Collection User Count
**Assumption:** 600M+ global ETC users, with China accounting for ~300M.
**Reasoning:** GlobeNewsWire (2024) reports 600M+ ETC users. China's Ministry of Transport reports wide ETC adoption following the 2019 mandate for highway toll collection.
**Risk:** "User" counts may include inactive registrations. Actual regular users may be 60-70% of registered count.

### A4. EV Charging Transaction Frequency
**Assumption:** ~3M public chargers globally, averaging 2.5 paid sessions per day.
**Reasoning:** IEA Global EV Outlook provides charger counts. Utilisation varies enormously — high-traffic urban chargers may handle 10+ sessions/day; rural chargers may see 1-2.
**Risk:** Public charger count is growing 30%+ annually, so any point-in-time figure is quickly outdated. Utilisation rates are poorly reported.

### A5. Vending Machine Classification
**Assumption:** 3-5B annual vending/unattended retail transactions qualify as M2M.
**Reasoning:** While vending purchases are human-initiated, the payment processing is automated and IoT-enabled (connected machines, cashless readers). We include cashless vending as M2M because the infrastructure is identical.
**Risk:** Purists would exclude vending since a human chooses to buy. We include it because the payment infrastructure is IoT-native.

### A6. Smart Meter Payment Trigger Rate
**Assumption:** Only ~30% of smart meter readings trigger an autonomous payment transaction.
**Reasoning:** Most smart meters report data that feeds into a monthly bill, which the customer then pays manually. Only pre-pay meters and some smart billing systems trigger automatic payments.
**Risk:** As smart meter billing evolves toward pay-as-you-go (especially in developing nations and for EV charging), this percentage will increase.

---

## Projection Assumptions

### A7. IoT Device Growth
**Assumption:** IoT connected devices grow from 21.1B (2025) to ~39B (2030) to ~60B (2035).
**Reasoning:** IoT Analytics reports 21.1B for 2025. GSMA projects 38.7B by 2030. We extrapolate to ~60B by 2035 assuming continued but decelerating growth.
**Risk:** Low — device count projections are well-established and come from multiple independent sources (IoT Analytics, Ericsson, GSMA, Transforma Insights).

### A8. Payment-Enabled Percentage
**Assumption:** Currently ~10% of IoT devices are payment-enabled; this grows to 13% (baseline) or 20% (high growth) by 2030.
**Reasoning:** Most IoT devices are sensors, monitors, and trackers that generate data but not payments. Payment-enabled devices include tolling equipment, EV chargers, connected vehicles, smart meters, and vending machines.
**Risk:** This is the most uncertain assumption. If new categories emerge (e.g., home appliances auto-ordering supplies, wearables auto-paying), the percentage could be much higher.

### A9. Autonomous Vehicle Impact
**Assumption (High Growth):** 10M autonomous vehicles by 2030, 100M by 2035, each generating 500 M2M payments/year.
**Reasoning:** An AV needs to pay for charging, tolls, parking, insurance (per-mile), data services, maintenance, and mapping updates. 500 transactions/year is conservative if these become streaming micropayments.
**Risk:** Autonomous vehicle deployment timelines are highly uncertain. Full autonomy (Level 4/5) may be delayed beyond 2030 in most markets.

### A10. Micropayment Revolution
**Assumption (High Growth):** Streaming payments for utilities, data, and services multiply transaction frequency 5-10x.
**Reasoning:** Instead of monthly electricity bills, smart meters could trigger payments per kWh. Instead of parking fees, payment could stream per minute. This is technically feasible today but not widely deployed.
**Risk:** Micropayment protocols face transaction cost barriers on traditional rails. Crypto/blockchain micropayment channels could enable this, but adoption is uncertain.

---

## Market Value Assumptions

### A11. Market Size Definition
**Assumption:** The $77B figure (Research Nester) refers to the autonomous IoT payments market value (revenue of the payments infrastructure/services), not the total transaction value flowing through M2M systems.
**Reasoning:** Total transaction value is much higher (~$300-500B/year) but the market research figure captures the revenue of the ecosystem enabling those payments.
**Risk:** Different reports use different definitions, making cross-source comparison difficult.

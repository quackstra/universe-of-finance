# Assumptions — Bank Transfers (ACH/RTGS)

## Scope Definition

1. **"Bank Transfers"** includes: ACH/batch credit transfers, real-time payments (UPI, PIX, FedNow, Faster Payments, SEPA Instant), RTGS/wire transfers (Fedwire, TARGET2/T2, CHAPS, BOJ-NET), and cross-border wires (SWIFT gpi, CIPS).
2. **Excludes**: Card payments (Visa, Mastercard), digital wallets (Apple Pay, Google Pay) unless they ride on bank transfer rails (e.g., UPI via Google Pay counts as UPI), cheques, cash, cryptocurrency.
3. **Real-time payments are classified as bank transfers** because they are account-to-account movements through banking infrastructure, even though they differ from traditional batch ACH.

## Data Year

4. Primary data year is **2024** for current state. Where 2024 data is unavailable, 2023 data is used with explicit notation.
5. Historical timeseries covers **2015-2024** where possible. For systems launched after 2015 (UPI: 2016, PIX: 2020, FedNow: 2023), timeseries starts at launch.

## Geographic Scope

6. **Global aggregate** is constructed bottom-up from major systems:
   - **US**: ACH (Nacha) + Fedwire + FedNow
   - **Europe**: SEPA Credit Transfers + TARGET2/T2 + UK (Faster Payments, BACS, CHAPS)
   - **India**: UPI
   - **Brazil**: PIX
   - **China**: Domestic CNAPS (estimated) + CIPS cross-border
   - **Rest of World**: Estimated from ACI Worldwide global totals minus known systems

## Estimation Methodology

7. **TPS calculation**: Annual volume / (365.25 days * 86,400 seconds). This gives average TPS over a full calendar year including nights/weekends when volume is lower.
8. **Peak TPS estimate**: Based on peak day volumes where available (e.g., PIX 252.1M on Dec 20, 2024), divided by 86,400 seconds. Where peak day isn't known, we estimate 2.5x average daily volume based on observed ratios.
9. **Business-day adjusted TPS**: Where relevant (RTGS systems operating ~250 days), we calculate operational TPS separately.

## Currency Conversion

10. All values converted to **USD** using approximate 2024 average exchange rates:
    - EUR/USD = 1.08
    - GBP/USD = 1.27
    - INR/USD = 0.012 (83.3 INR per USD)
    - BRL/USD = 0.20 (5.0 BRL per USD)
    - RMB/USD = 0.139 (7.2 RMB per USD)
    - JPY/USD = 0.0066 (151 JPY per USD)

## Data Reconciliation

11. **Nacha vs. FedACH**: Nacha reports total ACH Network (33.6B), which includes both FedACH and EPN (The Clearing House). FedACH alone was 20.1B in 2024. We use Nacha's full network figure for US ACH.
12. **Nacha "off-network"**: Total ACH including off-network was 40.2B in 2024. We use the 33.6B on-network figure for consistency.
13. **PIX variance**: Sources report 57B-69B for 2024 PIX volume. We use 63B as a reasonable midpoint with medium confidence.
14. **UPI figures**: NPCI reports 131.1B for calendar year 2024 (not fiscal year). Some sources report ~172B which likely includes Jan-Mar 2025 or counts sub-transactions. We use 131.1B as the conservative calendar-year figure.
15. **China domestic payments**: CNAPS domestic volume is not publicly reported in English. We estimate China's domestic electronic credit transfers at ~80B based on BIS CPMI proportional data and China's share of global non-cash payments. This is a RED confidence estimate.

## Growth Projections

16. **Baseline projection (2026-2035)**: Applies observed 5-year CAGRs to each subcategory, with gradual deceleration (CAGR reduces by 0.5 percentage points per year after 2028).
17. **High-growth scenario**: Assumes real-time payments maintain 25%+ CAGR through 2030 driven by UPI global expansion, PIX continued growth, FedNow/SEPA Instant mandates, and new RTP launches in Africa/SE Asia.
18. **Conservative scenario**: Assumes regulatory friction, interoperability challenges, and slower-than-expected adoption in mature markets. Real-time growth decelerates to 10% CAGR by 2028.

## Double-Counting Prevention

19. **SWIFT messages are NOT added to other system volumes** — SWIFT is a messaging network, not a settlement system. A Fedwire or TARGET2 payment may also generate a SWIFT message. We track SWIFT separately for cross-border context but do not add it to global totals.
20. **FedNow is tracked separately from ACH** — they are distinct rails despite both being US domestic transfer systems.
21. **SEPA Instant is a subset of SEPA Credit Transfers** — we break it out but don't double-count.

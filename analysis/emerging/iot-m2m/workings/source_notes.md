# IoT & Machine-to-Machine Payments — Source Notes

> Extended notes on each source consulted during research. Accessed 2026-03-26.

---

## Primary Sources

### 1. IoT Analytics — Number of Connected IoT Devices
- **URL:** https://iot-analytics.com/number-connected-iot-devices/
- **Key data:** 18.5B connected IoT devices in 2024 (+12% YoY); 21.1B projected for 2025 (+14%); forecasting continued double-digit growth
- **Reliability:** :green_circle: High — IoT Analytics is the leading independent tracker of IoT device statistics
- **Notes:** Counts all IoT connections (consumer, enterprise, industrial). Does not distinguish payment-enabled devices. Updated regularly with actual vs projected figures.

### 2. Ericsson — IoT Connections Forecast (Mobility Report)
- **URL:** https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/iot-connections-outlook
- **Key data:** Cellular IoT connections: 4.5B (2025), approaching 8B by 2030
- **Reliability:** :green_circle: High — Ericsson is a primary infrastructure provider
- **Notes:** Focuses specifically on cellular IoT connections, which are a subset of all IoT. Cellular-connected devices are more likely to be payment-enabled than non-cellular (WiFi/BLE) devices.

### 3. GSMA Intelligence — IoT Market Forecast to 2030
- **URL:** https://www.gsmaintelligence.com/research/iot-market-forecast-to-2030-connections-by-region-and-vertical
- **Key data:** 38.7B IoT connections by 2030 (8% CAGR 2023-2030); IoT revenues doubling from $1T (2024) to $2T (2030)
- **Reliability:** :green_circle: High — GSMA represents the global mobile operator industry
- **Notes:** The $1T-$2T revenue figure includes all IoT monetisation, not just payments.

### 4. Research Nester — Autonomous IoT Payments Market
- **URL:** https://www.researchnester.com/reports/autonomous-iot-payments-market/6532
- **Key data:** Market valued at $77.3B (2025); projected to reach $3,775B by 2037
- **Reliability:** :yellow_circle: Medium — market research firm; methodology not fully transparent
- **Notes:** The $3,775B (2037) projection implies ~35% CAGR, which is aggressive but within the range of other estimates. Definition of "autonomous IoT payments" aligns with our scope.

### 5. GM Insights — Autonomous IoT Payments Market 2024-2032
- **URL:** https://www.gminsights.com/industry-analysis/autonomous-iot-payments-market
- **Key data:** Market at $54.3B (2024), growing to significant scale by 2032
- **Reliability:** :yellow_circle: Medium
- **Notes:** Slightly lower 2024 figure than Research Nester's 2025 figure, which is consistent if ~40% YoY growth is assumed.

### 6. GM Insights — IoT Monetization Market 2025-2034
- **URL:** https://www.gminsights.com/industry-analysis/internet-of-things-iot-monetization-market
- **Key data:** IoT monetisation market at $1.01T (2024), 46.4% CAGR to 2034
- **Reliability:** :yellow_circle: Medium
- **Notes:** This is the broadest definition — includes data monetisation, platform fees, and payments. Too broad for our scope but useful for context.

### 7. GlobeNewsWire — Electronic Toll Collection Market
- **URL:** https://www.globenewswire.com/news-release/2024/03/22/2850890/0/en/Global-Electronic-Toll-Collection-Market-Size-To-Worth-USD-20-56-Billion-By-2033-CAGR-Of-7-71.html
- **Key data:** ETC market at $10.5B (2023), projected to $20.56B by 2033 (7.71% CAGR); 600M+ ETC users worldwide; 1.2M+ equipped toll lanes
- **Reliability:** :yellow_circle: Medium
- **Notes:** Useful for the most mature M2M payment subcategory. Toll collection is growing modestly as new toll roads are built, but it's a mature market.

### 8. Mastercard — How IoT Will Shape the Future of Payments (2021)
- **URL:** https://www.mastercard.com/news/media/wddjfrhn/how-iot-will-shape-the-future-of-payments.pdf
- **Key data:** Mastercard's vision for IoT payments; identifies connected cars, wearables, and home devices as payment vectors
- **Reliability:** :yellow_circle: Medium — thought leadership rather than data source
- **Notes:** Dated (2021) but provides useful framework for categorising M2M payment types.

---

## Data Gaps

1. **M2M transaction counts** — no organisation tracks payments specifically initiated by machines vs humans
2. **EV charging transaction volumes** — global aggregate data is sparse; most data is per-operator or per-country
3. **Smart meter payment trigger rates** — what percentage of meter reads actually trigger autonomous payments vs feed into manual billing
4. **Connected vehicle payment data** — OEMs do not publish transaction data from in-vehicle payment systems
5. **Regional breakdowns** of M2M payment volume are almost entirely estimated

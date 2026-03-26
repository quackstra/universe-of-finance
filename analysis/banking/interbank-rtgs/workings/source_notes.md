# Interbank RTGS — Source Notes

## Primary Sources

### Fedwire Funds Service
- **URL**: https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html
- **Publisher**: Federal Reserve Bank Services
- **Data quality**: Excellent. Monthly, quarterly, and annual statistics published with transaction counts and values. Updated regularly.
- **Key 2024 data**: Daily avg 836,322 transactions, daily avg value ~$4.51T, avg transfer value ~$5.4M
- **Historical data**: Available back to 1987
- **Confidence**: 🟢 High

### ECB T2 (ex-TARGET2)
- **URL**: https://www.ecb.europa.eu/paym/target/t2/facts/html/index.en.html
- **Publisher**: European Central Bank
- **Data quality**: Excellent. Annual reports and fact sheets published. The TARGET Services Annual Report 2024 was published July 2025.
- **Key 2024 data**: ~108M transactions (record high), daily avg ~400,000 transactions, daily avg value ~€2.2T
- **Note**: T2 replaced TARGET2 in March 2023. Some discontinuity in time series.
- **Confidence**: 🟢 High

### CHAPS / Bank of England
- **URL**: https://www.bankofengland.co.uk/payment-and-settlement/payment-and-settlement-statistics
- **Publisher**: Bank of England / Pay.UK
- **Data quality**: Excellent. Annual report with detailed breakdowns by payment type, value bands, and peak days.
- **Key 2024 data**: 52.7M payments, £87.5T total value, daily avg ~208,000 payments, avg payment value £1.7M
- **Peak day**: 2 April 2024 — 344,099 payments (all-time record)
- **Confidence**: 🟢 High

### BOJ-NET
- **URL**: https://www.boj.or.jp/en/statistics/set/kess/index.htm
- **Publisher**: Bank of Japan
- **Data quality**: Good, but English-language access is limited. Monthly PDFs published.
- **Key data**: Daily avg ~19,000 payments, daily avg value ~¥73T (from most recent available report)
- **Limitation**: Could not confirm exact 2024 annual total from English sources
- **Confidence**: 🟡 Medium

### CLS Group
- **URL**: https://www.cls-group.com/about/annual-report-2024/annual-report-2024/
- **Publisher**: CLS Group Holdings AG
- **Data quality**: Good for value data, limited for transaction counts.
- **Key 2024 data**: Daily avg settled value >$7T, record $19.1T (20 June 2024), record funding efficiency $72B for $19.1T day
- **Transaction count**: Not regularly published. Record day 3.2M trades (July 2022). Annual count estimated.
- **Confidence**: 🟡 Medium (value data high; transaction count low)

## Secondary Sources

### BIS CPMI Statistics
- **URL**: https://www.bis.org/statistics/dataportal/payment_stats.htm
- **Publisher**: Bank for International Settlements
- **Data quality**: Comprehensive cross-country data but typically 1-2 years behind
- **Use**: Cross-validation of national statistics, historical trends
- **Confidence**: 🟢 High (for years covered)

### Federal Reserve Annual Report
- **URL**: https://www.federalreserve.gov/paymentsystems/fedfunds_ann.htm
- **Data quality**: Confirms FRB Services figures; useful for YoY comparison narratives
- **Key 2023 note**: "number of Fedwire funds transfers originated by depository institutions decreased 1.4 percent, to approximately 193 million"

### Pay.UK Annual Statistics 2024
- **URL**: https://www.wearepay.uk/wp-content/uploads/2025/03/Annual-Statistics-2024-v1.2.pdf
- **Publisher**: Pay.UK (UK payments infrastructure operator)
- **Use**: Complements Bank of England data with broader UK payment system context

## Data Gaps

1. **China HVPS/CIPS**: China's high-value payment system processes significant volumes but detailed English-language statistics are limited. CIPS (cross-border) reported 8.2M transactions in 2024, but domestic HVPS data is harder to access.

2. **India RTGS**: RBI publishes RTGS statistics but they were not included in this capsule's scope. India's RTGS processes ~1M transactions/day (~$500B daily value).

3. **Switzerland SIC**: Swiss Interbank Clearing system is significant for its size relative to GDP but small in absolute transaction terms.

4. **CLS transaction counts**: The biggest data gap. CLS publishes comprehensive value statistics but transaction count data requires estimation.

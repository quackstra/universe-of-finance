# Interbank RTGS — Assumptions

## Scope Assumptions

1. **CLS inclusion**: CLS is included as an RTGS-adjacent system because it performs final settlement of FX obligations via payment-versus-payment, using RTGS systems as the funding mechanism. This is a judgment call — CLS could also be classified under "FX Markets" if that category existed in the taxonomy.

2. **Excluding smaller RTGS systems**: We focus on the five largest systems (Fedwire, T2, CHAPS, BOJ-NET, CLS). Other national RTGS systems (CIPS in China, RBI in India, SIC in Switzerland, etc.) are excluded from the detailed breakdown but partially captured in the aggregate estimate. This means the 423M total is an undercount of global RTGS activity.

3. **Excluding Fedwire Securities**: Fedwire operates two services — Funds (payments) and Securities (government bond settlement). Only Funds is counted here; Securities settlement is covered in the securities-settlement capsule.

## Data Assumptions

4. **Fedwire 2024 volume**: Calculated as daily average of 836,322 × 251 business days = ~209.9M. The exact annual figure may differ slightly due to rounding; FRB Services publishes the precise number.

5. **T2 2024 volume**: ECB described 2024 traffic as "nearly 108 million transactions" — we use 108M as a round figure.

6. **BOJ-NET volume**: The ~19,000 daily average and ~¥73 trillion daily value are from the most recent English-language BOJ publication available. Japanese-language sources may have more current data.

7. **CLS transaction count**: This is the least certain figure. CLS publishes value data readily but transaction counts are infrequent. Our estimate of ~250M annual trades is derived from the ratio of the 3.2M record-day trades to the $19.1T record-day value, applied to the $7T average daily value. This methodology assumes a linear relationship between value and trade count, which may not hold.

## FX Rate Assumptions

8. **EUR/USD = 1.09**: Approximate 2024 average (actual range: 1.06-1.12)
9. **GBP/USD = 1.27**: Approximate 2024 average (actual range: 1.23-1.34)
10. **USD/JPY = 149.5** (JPY/USD = 0.00669): Approximate 2024 average (actual range: 140-162)

## Projection Assumptions

11. **3% baseline volume CAGR**: Based on observed 5-year CAGRs of 3.2% (Fedwire), 4.2% (T2), 3.9% (CHAPS). The composite is slightly below the weighted average because we expect growth to moderate as central banks improve netting efficiency.

12. **5% baseline value CAGR**: Value grows faster than volume because average transaction sizes increase with inflation and financial market growth.

13. **24/7 RTGS impact not modeled in baseline**: The Bank of England has signaled interest in extended RTGS hours, but this is not yet operational. If adopted, it could increase daily transaction counts by 10-20% by spreading settlement across more hours.

## Double-Counting Notes

14. **CLS vs RTGS overlap**: CLS settles through national RTGS systems. A CLS-settled FX trade generates funding payments in Fedwire, T2, BOJ-NET, etc. The report headline value of ~$2,150T EXCLUDES CLS to avoid this overlap. When CLS is included, the gross value is ~$3,700T but this overstates unique economic activity.

15. **RTGS as final settlement layer**: Many upstream systems (ACH, card networks, CCPs) generate net settlement obligations that are ultimately discharged through RTGS. The RTGS transaction count captures only the final settlement, not the upstream transactions. This is by design per the taxonomy's approach.

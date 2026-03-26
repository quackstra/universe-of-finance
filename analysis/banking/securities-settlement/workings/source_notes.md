# Securities Settlement — Source Notes

## Primary Sources

### DTCC Annual Report 2024
- **URL**: https://www.dtcc.com/annuals/2024/files/DTCC-Annual-Report-2024-Print.pdf
- **Publisher**: Depository Trust & Clearing Corporation
- **Data quality**: Good for value data and revenue; limited on transaction count granularity
- **Key 2024 data**: Revenue $2.49B (+11% YoY), $3.7 quadrillion in securities transactions processed, custody/asset servicing for $99T in securities issues
- **Limitation**: Does not provide a single headline annual transaction count across DTC+NSCC+FICC
- **Confidence**: 🟢 High (value), 🟡 Medium (transaction counts)

### DTCC CFO Letter (2024 Annual Report)
- **URL**: https://www.dtcc.com/annuals/2024/letters/cfo/
- **Key data**: Revenue breakdown, NSCC daily avg value $2.219T
- **Confidence**: 🟢 High

### DTCC Record Volumes Press Release (April 2025)
- **URL**: https://www.dtcc.com/news/2025/april/23/dtcc-processes-record-volumes-across-services-amid-market-volatility
- **Key data**: NSCC peak 545M transactions (7 April 2025), NSCC peak value $5.55T (9 April 2025), previous NSCC peak 409M (27 January 2021 meme stock event)
- **Note**: April 2025 data, not 2024, but demonstrates capacity
- **Confidence**: 🟢 High

### Euroclear 2024 Results Press Release
- **URL**: https://www.euroclear.com/newsandinsights/en/press/2025/mr-05-euroclear-delivers-strong-results-in-2024.html
- **Publisher**: Euroclear
- **Data quality**: Excellent. Clear headline metrics.
- **Key 2024 data**: 331M netted transactions, €1,162T settled value, >€40T assets under custody (record high)
- **Q1-Q3 detail**: 243M transactions, €850T (up 5% YoY)
- **Confidence**: 🟢 High

### Clearstream Monthly Figures
- **URL**: https://www.clearstream.com/clearstream-en/newsroom/240613-3997020
- **Publisher**: Clearstream (Deutsche Boerse Group)
- **Data quality**: Monthly figures published; need aggregation for annual totals
- **Key data (YTD May 2024)**: ICSD 8.0M txns, CSD 71.7M txns, IFS 18.4M txns
- **Limitation**: Only 5 months of data available from this source
- **Confidence**: 🟡 Medium

### Clearstream Settlement Efficiency 2024
- **URL**: https://www.clearstream.com/clearstream-en/newsroom/250131-4258778
- **Key data**: Settlement instructions volume increased 25% in 2024; failed instructions declined 14%
- **Confidence**: 🟢 High (for efficiency metrics)

### ECB TARGET Services Annual Report 2024
- **URL**: https://www.ecb.europa.eu/press/targetservar/html/ecb.targetservar2024.en.html
- **Publisher**: European Central Bank
- **Key data**: T2S volumes peaked in 2024, up 14% from previous year. First full year on consolidated T2-T2S platform.
- **Limitation**: T2S-specific transaction count not prominently reported
- **Confidence**: 🟡 Medium

## Secondary Sources

### DTCC on Wikipedia
- **URL**: https://en.wikipedia.org/wiki/Depository_Trust_%26_Clearing_Corporation
- **Use**: Historical value figures, subsidiary descriptions
- **Key data**: DTC handles ~1.3M daily delivery transactions, settled through ~70 NSS transfers/day
- **Confidence**: 🟡 Medium (secondary source, but well-cited)

### DTCC $3.7 Quadrillion Reports
- **URLs**:
  - https://finance.yahoo.com/news/dtcc-handles-3-7-quadrillion-162255289.html
  - https://dailycryptobriefs.com/news/dtcc-tokenizes-us-treasuries-canton-network/
- **Context**: Multiple outlets reported $3.7Q in 2025 articles about DTCC's Canton Network tokenization initiative
- **Confidence**: 🟡 Medium (journalistic sources citing DTCC)

### SIFMA T+1 After Action Report
- **URL**: https://www.sifma.org/resources/guides-playbooks/t1-after-action-report
- **Publisher**: SIFMA (Securities Industry and Financial Markets Association)
- **Use**: Context on T+1 transition impact (28 May 2024)
- **Confidence**: 🟢 High

### Euroclear S&P Rating Report
- **URL**: https://www.euroclear.com/content/dam/euroclear/investor-relations/debtinvestors/Standard%20and%20Poor's%20Ratings%20Report%20-%20Euroclear%20Bank%20-%2013%20December%202024.PDF
- **Use**: Additional financial and operational data
- **Confidence**: 🟢 High

## Data Gaps

1. **DTCC transaction count**: The single biggest gap. We need a unified annual count across DTC, NSCC, and FICC. The CPMI-IOSCO quarterly quantitative disclosures may contain this but are dense technical documents.

2. **Clearstream full-year 2024**: Only had YTD through May 2024 from publicly accessible sources. The full annual report may have been published but was not found in search results.

3. **T2S absolute transaction count**: ECB reports growth rates and peaks but the absolute annual transaction count for T2S specifically is not easily extractable from the TARGET Services reporting.

4. **Asian settlement infrastructure**: JASDEC (Japan), CCDC/SHCH (China), CCIL (India) are significant but not covered in detail. This creates a downward bias in the global total.

5. **Repo and securities lending**: These generate significant settlement volumes (estimated 5-10% of total) but are not broken out separately in most reporting.

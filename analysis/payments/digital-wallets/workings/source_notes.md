# Digital Wallets & Mobile Payments — Source Notes

## Source Quality Assessment

### Tier 1: Official/Regulatory (High Confidence)
- **NPCI** — India's payment system operator, publishes monthly UPI statistics. Data is authoritative and granular. Used for all UPI figures.
- **Safaricom Annual Report** — Publicly listed company (NSE), audited financials. M-Pesa transaction volumes are in the audited notes. FY2024 report used.
- **PBOC** — People's Bank of China publishes aggregate mobile payment statistics. Accessed via Statista secondary reporting.

### Tier 2: Industry Reports (Medium Confidence)
- **Worldpay Global Payments Report 2024** — Annual industry benchmark covering 40+ markets. Digital wallet share of spend figures are widely cited. Value figures are reliable; transaction count estimates less so.
- **BusinessOfApps** — Aggregator of public company data and analyst estimates. Used for WeChat Pay and Google Pay figures. Cross-referenced against multiple sources.
- **Electroiq** — Statistical aggregation site. Used for Alipay and Apple Pay figures. Quality varies; cross-referenced where possible.

### Tier 3: Analyst Estimates (Low Confidence)
- **Apple Pay transaction count** — Apple does not publish this. The 20B figure for 2023 comes from analyst estimates (Electroiq, Chargeflow) with ~20% uncertainty. Apple confirms "billions" of transactions but won't specify.
- **Google Pay 66B figure** — Cited by BusinessOfApps but mostly India/UPI. Not independently verifiable outside of Google's occasional press releases.
- **WeChat Pay "1 billion daily" claim** — Widely cited but sourced from Tencent investor presentations where definition of "transaction" may include non-payment interactions.

## Data Gaps

1. **No unified global database** for digital wallet transactions exists. Every figure is an aggregation.
2. **Samsung Pay** does not publish transaction volumes at all.
3. **PayPal mobile wallet** vs. PayPal web — PayPal reports $1.68T total TPV but doesn't break out mobile wallet specifically.
4. **Regional wallets** (GCash, GoPay, MoMo, etc.) — Limited public data; estimates based on national payment system reports where available.
5. **Transaction count vs. value disconnect** — Some sources report value only, requiring average transaction size assumptions to derive counts.

## Key URLs Accessed

| Source | URL | Date Accessed | Notes |
|--------|-----|---------------|-------|
| NPCI UPI Stats | https://www.npci.org.in/product/upi/product-statistics | 2026-03-26 | Monthly data downloadable |
| PIB Press Release | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2200569 | 2026-03-26 | IMF recognition of UPI |
| Worldpay GPR | https://worldpay.globalpaymentsreport.com/ | 2026-03-26 | Registration required for full report |
| Safaricom AR 2024 | https://www.safaricom.co.ke/annualreport_2024/ | 2026-03-26 | PDF download |
| Business Standard (UPI Dec) | https://www.business-standard.com/finance/news/upi-transactions-surge-to-record-16-73-bn-in-dec-value-at-rs-23-25-trn-125010100457_1.html | 2026-03-26 | Dec 2024 monthly peak |

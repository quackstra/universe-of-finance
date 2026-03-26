# Digital Wallets & Mobile Payments — Assumptions

## Key Assumptions

### 1. Double-Counting Treatment
- Apple Pay and Google Pay in Western markets are treated as **overlay** on card rails
- Only ~25% of Apple Pay's 20B transactions are counted as "native" digital wallet (in-app purchases, P2P)
- Google Pay's 66B transactions are predominantly UPI in India — excluded from separate count to avoid double-counting with UPI
- This is a conservative approach; some reports count all wallet-initiated transactions regardless of underlying rail

### 2. China Aggregate vs. Platform Split
- PBOC's aggregate 280B mobile payment figure is used as the authoritative China number
- Alipay and WeChat Pay splits are estimated from market share data (~55% WeChat, ~40% Alipay, ~5% others by volume)
- The "1 billion daily transactions" claim for WeChat Pay likely includes mini-program interactions, not just payments

### 3. "Others" Category
- Includes: Samsung Pay, PayPal mobile, GCash (Philippines), GoPay (Indonesia), MoMo (Vietnam), PIX mobile (Brazil), Paytm Payments Bank (non-UPI), regional wallets
- Estimated at 133B for 2024 — this is the least confident number in the aggregate
- PIX in Brazil processed ~42B transactions in 2024, but PIX is classified under Bank Transfers in this taxonomy

### 4. Value Figures
- UPI value converted at ₹85 = $1 (2024 average)
- China value converted at ¥7.1 = $1 (2024 average)
- M-Pesa value uses Safaricom's own USD conversion (~KSh 130 = $1)

### 5. M-Pesa Scope
- Includes all M-Pesa markets (Kenya, Tanzania, DRC, Mozambique, Ethiopia, etc.)
- Kenya accounts for ~60% of total M-Pesa volume

### 6. Projection Assumptions
- **Baseline**: Digital wallet adoption continues in emerging markets at current pace; developed markets see single-digit growth
- **High growth**: India's UPI model is replicated across SE Asia and Africa via interoperability agreements (already in progress with Singapore, UAE)
- **Conservative**: Regulatory intervention (e.g., China's Ant Group restructuring), data privacy laws limiting wallet functionality

### 7. Peak TPS
- Peak TPS of ~45,000 is a rough concurrent-system estimate, not a single-platform peak
- Alibaba has reported 544,000 TPS on Singles' Day — but this is a seconds-long burst, not sustained
- UPI's peak sustained TPS (December 2024): ~6,250

### 8. Year Alignment
- UPI data uses calendar year 2024 (Jan-Dec), not Indian fiscal year (Apr-Mar)
- Safaricom/M-Pesa uses FY ending March 2024
- China data uses calendar year 2024
- Minor misalignment accepted for comparability

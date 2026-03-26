# Fixed Income — Key Assumptions

## Transaction Definition
- One bond trade = one execution between two counterparties (buy/sell)
- Includes: government bonds, corporate bonds, municipal bonds, agency/MBS, securitized products
- Repo: one repo transaction = one agreement (not split into opening + closing legs)
- Excludes: primary market issuance (new bond sales), bond ETF trades (covered in equity/ETF category)
- Excludes: interest rate swaps (covered in OTC derivatives category)

## Scope
- **In scope**: Secondary market cash bond trading + repo
- **Out of scope**: Bond futures (ETD category), interest rate swaps (OTC derivatives), bond ETFs (equity markets)

## Value Data
- SIFMA ADV data is well-reported for US market
- Tradeweb provides electronic platform ADV
- Global outstanding from SIX Group / SIFMA: $145T (2024)

## Trade Count Estimation
- TRACE is the only reliable source of bond trade counts (US corporate/agency only)
- US Treasuries trade count estimated from ADV / average ticket size
- Global extrapolation assumes US = 45% of global bond trading activity
- Repo trade counts are poorly reported; estimated from value / average ticket size

## Market Hours
- Cash bonds: primarily domestic market hours (~8-10h/day)
- Repo: largely overnight and domestic hours
- 252 trading days/year

## Repo Treatment
- Repo is included in this category per taxonomy
- Repo inflates both value turnover and transaction counts significantly
- Automated overnight repo (auto-roll) generates high transaction counts but is economically a single rolling position
- We present both "cash bonds only" and "including repo" TPS figures

## Double-Counting Notes
- Bond futures are in ETD category
- Interest rate swaps are in OTC derivatives
- Bond ETF trades are in equity markets
- A bond trade generates one clearing instruction and one settlement — counted once per taxonomy rules

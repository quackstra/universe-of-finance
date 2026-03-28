# Digital Wallets & Mobile Payments — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed payment initiated through a digital wallet or mobile payment application** where the wallet is the consumer-facing payment interface. Specifically:

- **Counting point:** Completed payment — the transaction successfully debits the wallet balance, linked bank account, or linked card and credits the merchant/recipient
- **Unit:** One payment event at a merchant or to a recipient. A single tap/scan/in-app payment = one transaction
- **Inclusions:** UPI payments (India), Alipay/WeChat Pay QR payments (China), Apple Pay NFC tap payments, Google Pay payments, M-Pesa mobile money transfers, Samsung Pay, other regional wallets
- **Exclusions:** Card-not-present e-commerce (separate capsule), P2P transfers via Venmo/Zelle/Cash App (separate capsule), cryptocurrency wallet transactions, bank transfer app payments (separate capsule)

## Triangulation Approach

### Method A: Bottom-Up Platform Aggregation (Primary)

- **Source:** NPCI (UPI 172B), Statista/PBOC (China mobile 280B), Safaricom AR (M-Pesa 30B), Electroiq (Apple Pay ~20B), industry estimates (others ~133B)
- **Value:** ~620 billion transactions
- **Strengths:** UPI data is published monthly by NPCI with high granularity; M-Pesa is disclosed in Safaricom annual report; Apple Pay has third-party estimates
- **Weaknesses:** China mobile payment data (280B) is aggregated — Alipay and WeChat Pay do not publish individual transaction counts; "others" bucket (~133B) is residual estimation; Google Pay's 66B overlaps heavily with UPI

### Method B: Worldpay Global Payments Report (Value-Based Cross-Check)

- **Source:** Worldpay Global Payments Report 2024
- **Value:** $15.6 trillion in digital wallet transaction value globally
- **Derived count:** $15.6T / ~$25 implied average transaction value = ~624B transactions
- **Strengths:** Independent industry report covering all major markets; annual methodology
- **Weaknesses:** Value-to-count conversion requires assumed AOV; AOV varies enormously (UPI avg ~$17, Apple Pay avg ~$50, Alipay avg ~$70)

### Method C: PBOC + NPCI + Regional Central Bank Sum

- **Source:** PBOC payment statistics (China), NPCI (India), Bank of Ghana, Central Bank of Kenya, ECB contactless stats
- **Value:** ~590-640B range depending on "other wallets" estimate
- **Strengths:** Central bank data is authoritative within jurisdiction; covers the two largest markets (China + India = ~73% of global wallet volume)
- **Weaknesses:** PBOC aggregates all "mobile payments" including some bank app transfers; many countries lack separate wallet statistics

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [Platform Sum]       [Worldpay GPR]      [Central Banks]│
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 620B         │    │ ~624B        │    │ 590-640B   │ │
│  │ (5 platform  │    │ (value/AOV   │    │ (PBOC+NPCI │ │
│  │  groups)     │    │  derived)    │    │  +others)  │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ A vs B: <1% gap        │                │
│                │ (within AOV assumption │                │
│                │  error)               │                │
│                │ C range brackets A/B  │                │
│                │ Central tendency: 620B│                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   620B transactions    │                │
│                │   19,660 TPS           │                │
│                │   Confidence: 67/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**Bottom-up platform aggregation (Method A) anchors the final estimate** because:
1. UPI (172B, 28% of total) is directly observed from NPCI monthly statistics — the highest-quality input
2. M-Pesa (30B, 5%) is from audited Safaricom annual report
3. China total (280B, 45%) uses PBOC/Statista aggregation — lower quality but the best available

The Worldpay GPR value-derived count (Method B, ~624B) validates the aggregate within 1%. Central bank data (Method C) brackets the estimate at 590-640B.

**Key reconciliation issue:** Google Pay's reported 66B transactions are mostly UPI-based in India and are already counted in the UPI 172B figure. The 620B aggregate carefully avoids this double-count by using China total (not Alipay + WeChat separately) and attributing Google Pay India volume to UPI.

## Overlap Analysis

```
Digital Wallets: 620B total
                │
(-) Card-rail   │
    overlay     ████████████████████████████████████  620B
    (~40B)      │ Apple Pay/Google Pay/Samsung Pay
                │ NFC payments that ride on Visa/MC
                │ rails — ALSO counted in Consumer
                │ Cards. Deducted HERE, kept in Cards.
                │
(-) UPI overlap │ UPI 172B is ALSO counted in
    with Bank   │ Bank Transfers (RTP segment).
    Transfers   │ Deducted HERE, kept in Bank Transfers.
                │
                ▼
De-duplicated   ████████████████████  ~408B
                Digital Wallets subtracts card-rail
                overlay (~40B) and UPI (~172B) to
                avoid double-counting with base layers.
                Incremental wallet volume: ~408B
```

**Digital Wallets is an overlay category.** It sits above the card and bank transfer base layers. To avoid double-counting:
- ~40B Apple Pay/Google Pay/Samsung Pay NFC transactions are kept in Consumer Cards (base layer)
- ~172B UPI transactions are kept in Bank Transfers (base layer)
- Digital Wallets contributes ~408B incremental transactions (primarily China mobile payments + M-Pesa + non-card wallet payments)

## Coverage Assessment

- **Directly observed:** UPI (~28%) from NPCI monthly data; M-Pesa (~5%) from Safaricom AR — total ~33% directly observed
- **Semi-observed:** China mobile payments (~45%) from PBOC aggregate statistics — transaction-level breakdown between Alipay/WeChat not disclosed
- **Estimated:** Apple Pay (~3%), other wallets (~19%) — derived from industry estimates and value/AOV ratios

```
Region          Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
China           ████████ 45.2%   Medium (PBOC aggregate only)
India (UPI)     ██████░░ 27.7%   High (NPCI monthly data)
Africa (M-Pesa) ██░░░░░░  4.8%   High (Safaricom AR)
SE Asia         ██░░░░░░  5.0%   Low (fragmented markets)
North America   █░░░░░░░  4.0%   Medium (Apple Pay estimates)
Europe          █░░░░░░░  3.5%   Medium (ECB contactless)
Rest of World   ██░░░░░░  9.8%   Low (residual estimate)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
NPCI (UPI)          ████░░░░░  █████████ ██████████  ██████████
PBOC/Statista       ████████░  ████████░ ███████░░░  ████░░░░░░
Safaricom (M-Pesa)  ██░░░░░░░  █████████ █████████░  ████████░░
Worldpay GPR        █████████  █████████ ████████░░  █████░░░░░
Electroiq/BizApps   █████████  ████████░ █████░░░░░  ████░░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    72/100     85/100    70/100      55/100
```

- **Final confidence score:** 67/100
- **Key uncertainty drivers:**
  - China mobile payment breakdown (45% of total, corporate-confidential)
  - Apple Pay/Google Pay transaction counts (estimates vary 2x between sources)
  - "Other wallets" residual bucket (~133B, 21% of total, weakly sourced)
  - Overlap deduplication with UPI/card rails requires careful boundary management

## Revision History

- **Run 1 (2026-03-26):** Initial estimate — 620B from platform aggregation, Worldpay cross-check
- **Run 2 (2026-03-26):** Added platform breakdown, overlap analysis with card rails and bank transfers
- **Run 6 (2026-03-28):** Methodology documentation formalized

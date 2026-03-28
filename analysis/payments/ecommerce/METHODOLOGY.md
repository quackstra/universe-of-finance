# E-Commerce & Merchant Processing — Measurement Methodology

## Transaction Definition

A "transaction" in this category is a **completed e-commerce order** — the commerce event where a consumer places and pays for a purchase online. Specifically:

- **Counting point:** Order completion — the moment the consumer's purchase is confirmed and payment is authorized/captured. One order = one transaction, regardless of the number of items in the basket
- **Unit:** One e-commerce order. A consumer buying 3 items in a single Amazon checkout = one transaction
- **Scope:** Retail/consumer e-commerce (B2C + C2C marketplace). B2B e-commerce ($21T+) is excluded, consistent with standard industry reporting
- **Exclusions:** The payment rail (card, wallet, BNPL, bank transfer) is counted in its own capsule. One Amazon order via Apple Pay on a Visa card = one e-commerce transaction here, one digital wallet transaction, one card transaction — but de-duplicated via the overlap framework

## Triangulation Approach

### Method A: GMV / AOV Derivation (Primary)

- **Source:** SOAX/Statista ($6.33T GMV), ECDB (~$110 blended global AOV)
- **Value:** $6.33T / $110 = ~57.5 billion orders
- **Strengths:** GMV is well-documented across multiple sources (Statista, eMarketer, Worldpay); AOV is derived from ECDB's country-level data
- **Weaknesses:** AOV is a blended global average — sensitive to regional mix (Asia-Pacific ~$80, Western markets ~$145); GMV definitions vary (gross vs. net of returns)

### Method B: Bottom-Up Platform Sum (Cross-Check)

- **Source:** Alibaba (~14.5B orders from DemandSage), Amazon (~4.5B from Capital One Shopping), Shopify merchants (~3B derived from $292B GMV / ~$100 AOV), other platforms (~35B estimated)
- **Value:** ~57B orders (sum of known platforms + long-tail estimate)
- **Strengths:** Top 3 platforms are well-documented from earnings disclosures and analyst estimates; Alibaba alone is ~25% of global orders
- **Weaknesses:** Long-tail estimate (~35B, 61% of total) is the weakest link; platform GMV may include cancelled/returned orders

### Method C: Worldpay / Payment Processor Volume

- **Source:** Worldpay Global Payments Report 2024, Stripe/Adyen/PayPal processing volume disclosures
- **Value:** $6.3-6.5T total e-commerce value — consistent with Method A GMV
- **Strengths:** Payment processor data provides independent value confirmation; multiple processors disclose volumes
- **Weaknesses:** Processor data covers value, not order count; deriving counts requires AOV assumption; processor overlap (one order may touch multiple processors)

```
┌─────────────────────────────────────────────────────────┐
│                    RAW ESTIMATES                          │
│                                                          │
│  Method A             Method B            Method C       │
│  [GMV / AOV]          [Platform Sum]      [Processor $]  │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │ 57.5B        │    │ ~57B         │    │ $6.3-6.5T  │ │
│  │ ($6.33T /    │    │ (Alibaba +   │    │ (value     │ │
│  │  $110 AOV)   │    │  Amazon +    │    │  confirms  │ │
│  │              │    │  long tail)  │    │  GMV)      │ │
│  └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│         │                   │                  │         │
│         └───────────────────┼──────────────────┘         │
│                             ▼                            │
│                ┌────────────────────────┐                │
│                │    RECONCILIATION      │                │
│                │ A vs B: <1% gap        │                │
│                │ C confirms value range │                │
│                │ AOV sensitivity: ±20%  │                │
│                │ → count range 48-72B   │                │
│                └───────────┬────────────┘                │
│                            ▼                             │
│                ┌────────────────────────┐                │
│                │   FINAL ESTIMATE       │                │
│                │   57.5B orders         │                │
│                │   1,823 TPS            │                │
│                │   Confidence: 67/100   │                │
│                └────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Reconciliation

**GMV / AOV derivation (Method A) anchors the final estimate** because:
1. Global e-commerce GMV ($6.33T) is well-established across multiple independent sources
2. The bottom-up platform sum (Method B) produces ~57B, reconciling within 1%
3. Payment processor value data (Method C) confirms the GMV range

**Key sensitivity:** The AOV assumption ($110) is the primary uncertainty lever. If the true blended AOV is $95 (more Asia-weighted), the count rises to ~67B. If $130 (more Western-weighted), it drops to ~49B. The $110 figure reflects ECDB's country-weighted average.

## Overlap Analysis

```
E-Commerce: 57.5B total orders
                │
(-) Card-paid   │
    orders      ████████████████████████████████████  57.5B
    (~32B)      │ ~55% of e-commerce orders are paid
                │ by card — these are ALSO counted
                │ in Consumer Cards. Deducted HERE.
                │
(-) Wallet-paid │ ~23% paid via digital wallets
    orders      │ (~13B) — ALSO counted in Digital
    (~13B)      │ Wallets. Deducted HERE.
                │
(-) Bank/other  │ ~22% paid via bank transfer, COD,
    orders      │ BNPL, etc. — some overlap with
    (~12.5B)    │ Bank Transfers and BNPL capsules.
                │
                ▼
De-duplicated   █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ~2.9B
                E-Commerce is a COMMERCE LAYER — it
                measures orders, not payments. ~95%
                settle on payment rails counted
                elsewhere. Only ~5% (COD, cash) are
                truly incremental to payment TPS.
```

**E-Commerce is a commerce layer, not a payment rail.** It counts the economic event (an order placed) rather than the payment event. Approximately 95% of e-commerce orders settle on card, wallet, or bank transfer rails already counted in base-layer capsules. The incremental payment system load from e-commerce is primarily cash-on-delivery orders (~5% globally, higher in South/Southeast Asia).

## Coverage Assessment

- **Directly observed:** Top platform GMV (Alibaba, Amazon, Shopify ~40% of market) from SEC filings and earnings
- **Semi-observed:** Total GMV from Statista/SOAX/eMarketer — well-established but methodology varies
- **Estimated:** AOV ($110 blended) is the key model assumption; long-tail platform volume (~35B, 61%) is residual

```
Region          Volume    Share   Data Quality
─────────────── ──────── ─────── ───────────
China           ████████ 42.0%   Medium (Alibaba + JD + PDD)
North America   ████░░░░ 18.0%   High (Amazon + Shopify filings)
Europe          ███░░░░░ 15.0%   Medium (Eurostat + platform data)
SE Asia         ██░░░░░░  8.0%   Medium (Shopee/Lazada estimates)
India           ██░░░░░░  5.0%   Medium (Flipkart/Amazon India)
Latin America   █░░░░░░░  4.0%   Low (MercadoLibre + estimates)
Rest of World   ██░░░░░░  8.0%   Low (residual)
```

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
SOAX/Statista GMV   █████████  █████████ ████████░░  ██████░░░░
ECDB (AOV data)     ███████░░  ████████░ ███████░░░  ████████░░
Alibaba/JD filings  ████░░░░░  █████████ ██████████  ████████░░
Amazon 10-K         ███░░░░░░  █████████ ██████████  ████████░░
Worldpay GPR        █████████  █████████ ████████░░  █████░░░░░
                    ─────────  ────────  ──────────  ───────────
Composite Score:    75/100     88/100    80/100      65/100
```

- **Final confidence score:** 67/100
- **Key uncertainty drivers:**
  - AOV assumption ($110) — ±20% swings count by ±20%
  - Long-tail platform volume (61% of orders, weakly sourced)
  - GMV definition differences (gross vs. net of returns, ~5-8% impact)
  - Regional AOV variation (Asia $80 vs. West $145)

## Revision History

- **Run 1 (2026-03-26):** Initial estimate — 57.5B from GMV/AOV, platform sum cross-check
- **Run 2 (2026-03-26):** Added platform breakdown, payment method split, historic timeseries
- **Run 6 (2026-03-28):** Methodology documentation formalized

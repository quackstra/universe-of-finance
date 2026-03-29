---
title: "Sector: Payments"
parent: Methodology
grand_parent: Explore
nav_order: 2
---

# Sector Methodology: Payments

> How we measure the world's payment transactions — 11 categories, ~53,200 de-duplicated TPS.
> **Last Updated**: 2026-03-28 (Run 6)

---

## 1. Sector Overview

The Payments sector measures all electronic fund transfers between parties — card swipes, bank transfers, wallet taps, peer-to-peer sends, remittances, and the commerce/credit layers that ride on them. At ~53,200 de-duplicated TPS, Payments accounts for **75% of all global financial TPS**. It is both the largest sector and the most overlap-prone, because every commerce event (e-commerce, gaming, government, insurance) ultimately settles through a payment rail.

---

## 2. Sector-Specific Measurement Challenges

**Massive overlap between categories.** A consumer buying shoes on Amazon via Apple Pay funded by a Visa card appears in E-Commerce, Digital Wallets, and Consumer Cards simultaneously. Naive summation overcounts by ~14%.

**UPI's dual identity.** India's UPI (172B transactions) is simultaneously a bank transfer system (A2A real-time payments) and a mobile wallet system (accessed via PhonePe, Google Pay, Paytm). It is the single largest overlap in the entire taxonomy.

**China opacity.** Alipay and WeChat Pay process an estimated 280B annual transactions, but detailed breakdowns are corporate-confidential. We rely on PBOC aggregate reports and Statista estimates.

**Commerce vs. payment layers.** E-Commerce (57.5B), BNPL (5.5B purchases), Insurance (14B), Payroll (41.2B), and Bill Payments (95B) are real economic events, but 60-95% of their payment flows are already counted in Cards, Bank Transfers, or Wallets. They are commerce/credit layers, not incremental payment rails.

**Cash blindspot.** An estimated 18-20% of global consumer spending is cash. ATM withdrawals (49.1B) are the closest proxy for cash transaction volume, but cash-to-cash transfers are invisible.

---

## 3. Categories in This Sector

| # | Category | Avg TPS | Annual Volume (B) | Confidence | Overlap Status |
|---|----------|---------|-------------------|------------|----------------|
| 1 | Consumer Card Payments | 24,501 | 772.7 | 91 (High) | Base layer |
| 2 | Digital Wallets & Mobile Payments | 19,660 | 620 | 67 (Medium-High) | -172B UPI, -40B card-rail |
| 3 | Bank Transfers (ACH/RTP/Wire) | 15,338 | 484 | 78 (Medium-High) | Base layer (includes UPI) |
| 4 | Bill Payments | 3,012 | 95 | Medium | ~90% on bank/card rails |
| 5 | E-Commerce & Merchant Processing | 1,823 | 57.5 | 67 (Medium-High) | ~95% overlay on rails |
| 6 | ATM Withdrawals | 1,557 | 49.1 | Medium | Gateway to cash economy |
| 7 | Payroll Payments | 1,305 | 41.2 | Low | ~95% via ACH/bank rails |
| 8 | Insurance Premium Payments | 444 | 14 | Low | ~90% on bank/card rails |
| 9 | Peer-to-Peer Transfers | 270 | 8.5 | 69 (Medium-High) | Minor wallet overlap |
| 10 | Buy Now Pay Later (BNPL) | 175 (purchase) / 634 (installment) | 5.5 (purchase) / 20 (installment) | Medium | Credit layer on rails |
| 11 | Remittances | 57 | 1.8 | 58 (Medium) | Minor bank/P2P overlap |

**Raw sector sum: ~68,167 TPS** | **De-duplicated: ~53,200 TPS** (22% overcount in raw)

---

## 4. Cross-Category Overlap Rules

### Overlap Waterfall

```
Gross Payment TPS      ████████████████████████████████  ~68,167
                       │
(-) UPI double-count   ████████████████████████████      ~62,714  -5,453
    (172B in Wallets   │                                 (UPI counted in Bank Transfers;
    AND Bank Xfers)    │                                  subtract from Wallets)
                       │
(-) Card-rail wallets  ███████████████████████████       ~61,446  -1,268
    (Apple/Google/     │                                 (40B on Visa/MC rails)
    Samsung Pay)       │
                       │
(-) E-Commerce on      ██████████████████████████        ~59,716  -1,730
    existing rails     │                                 (95% of 57.5B already counted)
                       │
(-) Bill payments on   █████████████████████████         ~57,005  -2,711
    bank/card rails    │                                 (90% of 95B already counted)
                       │
(-) Payroll on ACH     ████████████████████████          ~55,765  -1,240
                       │                                 (95% of 41.2B already counted)
(-) Insurance on       ███████████████████████           ~55,365  -400
    bank/card rails    │                                 (90% of 14B already counted)
(-) BNPL on card/      ██████████████████████            ~55,190  -175
    bank rails         │                                 (purchases ride on existing rails)
(-) P2P/Remittance     ██████████████████████            ~55,165  -25
    minor overlaps     │
                        ▼
                       ═══════════════════════════
De-duplicated          ████████████████████               ~53,200 TPS
```

### Base Layer Rule

**Cards** (772.7B) and **Bank Transfers** (484B) are the two base payment layers. They represent the actual infrastructure that moves money. All other payment categories are measured for overlap against these two layers, plus the incremental portion of Wallets (408B after deducting UPI and card-rail wallets).

---

## 5. Primary Data Sources

### Source Confidence Matrix

```
                    Coverage   Recency   Authority   Granularity
                    ─────────  ────────  ──────────  ───────────
Nilson Report       █████████░ █████████ █████████░  ████████░░
Visa/MC 10-K        ████░░░░░  █████████ █████████░  ██████████
BIS CPMI Red Book   ██████░░░  █████░░░░ ██████████  ██████░░░░
NPCI (UPI data)     ████░░░░░  █████████ █████████░  █████████░
PBOC Reports        ████░░░░░  ████████░ █████████░  ████░░░░░░
ACI Worldwide       ████████░  ████████░ ███████░░░  ████░░░░░░
Worldpay GPR        ████████░  █████████ ███████░░░  ██████░░░░
Nacha (US ACH)      ███░░░░░░  █████████ █████████░  ██████████
GSMA (Mobile $)     ██████░░░  ████████░ ████████░░  █████░░░░░
BCB (PIX data)      ███░░░░░░  █████████ █████████░  █████████░
                    ─────────  ────────  ──────────  ───────────
```

**Tier 1 (Primary anchors):** Nilson Report (cards), BIS CPMI (bank transfers), NPCI (UPI), Visa/Mastercard filings
**Tier 2 (Cross-validation):** ACI Worldwide (real-time payments), PBOC (China), Worldpay GPR (e-commerce payment mix)
**Tier 3 (Gap-filling):** GSMA (mobile money), Statista, industry estimates

---

## 6. Sector Triangulation Approach

### Payments Sector Triangulation Funnel

```
┌─────────────────────────────────────────────────────────┐
│              RAW ESTIMATES                                │
│                                                          │
│  Method A              Method B            Method C      │
│  [Top-Down]            [Bottom-Up]         [Rail-Based]  │
│  GDP × payment         Sum of operator     Card networks │
│  intensity ratio       disclosures         + RTP systems │
│  ┌──────────┐         ┌──────────┐        ┌──────────┐  │
│  │ 1,750B   │         │ 1,620B   │        │ 1,690B   │  │
│  │ annual   │         │ annual   │        │ annual   │  │
│  └────┬─────┘         └────┬─────┘        └────┬─────┘  │
│       │                    │                    │        │
│       └────────────────────┼────────────────────┘        │
│                            ▼                              │
│              ┌───────────────────────┐                    │
│              │    RECONCILIATION     │                    │
│              │ Top-down overcounts   │                    │
│              │ by ~5% (includes      │                    │
│              │ some cash-funded).    │                    │
│              │ Bottom-up misses long │                    │
│              │ tail (~50B in small   │                    │
│              │ market wallets).      │                    │
│              │ Rail-based best fit.  │                    │
│              └──────────┬────────────┘                    │
│                         ▼                                 │
│              ┌───────────────────────┐                    │
│              │   FINAL ESTIMATE      │                    │
│              │ 1,679B unique txns    │                    │
│              │ ~53,200 TPS           │                    │
│              │ Range: 48,000-58,000  │                    │
│              │ Confidence: 78/100    │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

**Method A (Top-Down):** Global consumer spending (~$65T) x electronic payment penetration (~82%) x avg transaction frequency per dollar yields ~1,750B electronic payment events. Overstates because it includes some cash-intermediated flows.

**Method B (Bottom-Up):** Sum of Visa (233B) + Mastercard (166B) + UnionPay (158B) + other cards (216B) + UPI (172B) + China mobile (280B) + mobile money (108B) + ACH/batch (106B) + P2P (8.5B) + other = ~1,620B. Understates because it misses small-market operators.

**Method C (Rail-Based):** Card networks (773B) + bank transfers (484B) + incremental wallets (408B) + other = ~1,690B. Our preferred method because it counts at the infrastructure level.

---

## 7. Definition Standards

In the Payments sector, a **transaction** is a completed payment instruction — the point at which money is irrevocably committed to move from payer to payee.

| Category | Counting Point | What Is Excluded |
|----------|---------------|------------------|
| Consumer Cards | Clearing instruction (post-auth, pre-settle) | Declined auths, reversals, chargebacks |
| Bank Transfers | Initiated payment instruction (ACH item, RTP message) | Rejected items, returned payments |
| Digital Wallets | Completed wallet transaction | Failed attempts, cancelled orders |
| E-Commerce | Completed checkout event | Cart abandonments, cancelled orders |
| P2P Transfers | Completed transfer | Cancelled sends |
| Remittances | Completed cross-border transfer | Cancelled/returned remittances |
| ATM Withdrawals | Completed cash dispensing event | Balance inquiries, declined withdrawals |
| Bill Payments | Completed payment event | Scheduled but not executed payments |
| Payroll | Individual salary/wage deposit | Batch file submissions (1 file may contain 10,000 deposits) |
| Insurance | Premium payment event | Policy quotes, renewal notices |
| BNPL | Purchase-level: 1 checkout = 1 txn; Installment-level: each payment = 1 txn | Declined applications |

---

## 8. Known Gaps & Future Work

- **China mobile payment detail.** Alipay/WeChat Pay 280B estimate is based on PBOC aggregate data. Direct operator disclosures would improve confidence by 10+ points.
- **Cash economy measurement.** ATM withdrawals (49.1B) capture cash entry points but not subsequent cash-to-cash transactions. Diary studies and econometric cash-use models could provide bounds.
- **Bill payment de-duplication.** The 95B bill payment figure is new (Run 4) and its overlap with bank transfers needs more granular analysis by payment method.
- **Payroll and insurance overlap.** Both are heavily rail-dependent categories added in Run 4. The 95% and 90% overlap estimates are conservative and could be refined with payment method surveys.
- **Real-time payment explosion.** RTP volume grew 42% YoY (ACI Worldwide). Current 378B estimate may already be stale. Quarterly updates would improve recency.
- **On-us transaction gap.** Payments within a single bank (payer and payee at the same institution) may not appear in interbank statistics. The Fed estimates 10-15% of US non-cash payments are on-us. Global extrapolation is needed.

---

*Payments sector methodology evolves as new categories are added and overlap analysis is refined. The de-duplication framework is the most critical component — without it, the sector total would overstate by 22%.*

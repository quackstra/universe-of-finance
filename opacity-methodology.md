---
title: "Opacity Index — Methodology"
layout: default
nav_order: 50
permalink: /opacity-methodology/
---

# Opacity Index — Methodology (v1.0)

> CC BY 4.0 · last updated 2026-07-20

## What it measures

The Opacity Index scores each system **0–100 on how measurable it is** — higher = darker.

It is **not** the [confidence score](analysis/CONFIDENCE_SCORECARD.md). Confidence = how sure
the Universe of Finance is of *its own estimate*. Opacity = how measurable the system is *at
all*. They correlate but diverge: a system can be **low-confidence yet low-opacity** (new but
fully on-chain) or **high-confidence yet high-opacity** (we are sure it is unmeasurable).

**Headline:** ~60% of categorised transaction throughput flows through systems scoring
**60+** on opacity — reported self-servingly, on a lag, or not at all.

## The rubric

Each system scores on four dimensions that sum to 100:

| Dimension | Points | 0 points | Max points |
|-----------|--------|----------|------------|
| **Latency** | 0–30 | real-time (<1 min) | never published |
| **Granularity** | 0–25 | per-transaction | no figures at any granularity |
| **Verifiability** | 0–25 | independently auditable public ledger | unverifiable self-report or third-party estimate |
| **Coverage** | 0–20 | full system measured | shadow/proxy estimate only |

### Sanity anchors

The rubric is calibrated so that:

- Public blockchains ≈ **0-5**
- Pix / UPI ≈ **20-35**
- Card networks ≈ **55-70**
- China WMPs ≈ **90+**
- Hawala / cash ≈ **95+**

If the rubric stops reproducing these anchors, we revise **the rubric** — not the anchors'
evidence.

## Category scores

Every score below is the sum of its four dimensions — fully auditable.

| System | Opacity | Lat /30 | Gran /25 | Ver /25 | Cov /20 | Justification | Source |
|---|---|---|---|---|---|---|---|
| IoT & M2M | **78** | 24 | 20 | 18 | 16 | Machine-to-machine payments are barely instrumented; count is a forward estimate. | Industry projection |
| Insurance Premiums | **76** | 22 | 20 | 18 | 16 | Claim/premium counts are modeled from frequency; NAIC compilation is paywalled. | Population x frequency model; NAIC (paywalled) |
| Microtransactions | **74** | 22 | 18 | 18 | 16 | In-game economies are closed; counts inferred from publisher revenue. | Publisher revenue estimates |
| Remittances | **70** | 18 | 16 | 18 | 18 | World Bank publishes annually and formal-only; informal/hawala flows (~60% uplift) are unmeasured. | World Bank; informal estimated |
| Digital Wallets | **68** | 22 | 18 | 16 | 12 | Fragmented private operators; China's PBOC reports only aggregates, Alipay/WeChat internals closed. | PBOC, operator disclosures |
| Payroll | **68** | 22 | 18 | 14 | 14 | Batch ACH/BACS payroll is buried inside bank-transfer aggregates; no dedicated public count. | Labor + payroll-provider estimates |
| OTC Derivatives | **68** | 18 | 18 | 16 | 16 | BIS reports notional semiannually; trade counts are inferred, bilateral deals are dark. | BIS OTC statistics (semiannual) |
| BNPL | **66** | 20 | 16 | 16 | 14 | Private providers disclose GMV, not installment-event counts; multiplier is modeled. | Provider earnings, modeled installments |
| Game Sales | **66** | 20 | 16 | 16 | 14 | Storefront transaction counts inferred from revenue; platforms don't publish counts. | Market-research revenue estimates |
| Bill Payments | **64** | 20 | 18 | 14 | 12 | Biller aggregators report sparsely; no consolidated public count. | Estimate from biller/aggregator data |
| P2P Transfers | **64** | 18 | 16 | 16 | 14 | App operators (Venmo, Zelle, Cash App) disclose selectively; no consolidated feed. | Operator disclosures |
| Fixed Income | **62** | 16 | 16 | 14 | 16 | Largely OTC; TRACE covers US corporates only, repo counts are estimated. | TRACE (partial); repo estimated |
| Consumer Cards | **60** | 20 | 18 | 14 | 8 | Volumes surface only in quarterly network earnings as aggregates; no public per-transaction data. | Nilson Report / Visa & Mastercard 10-Q filings |
| E-Commerce | **60** | 18 | 16 | 14 | 12 | Derived from retail sales aggregates; transaction counts modeled, not observed. | eMarketer, retail sales estimates |
| AI Agents | **60** | 10 | 14 | 16 | 20 | Nascent; some on-chain agent activity is visible, most is unmeasured. | On-chain sample + projection |
| Forex | **58** | 14 | 16 | 14 | 14 | The BIS Triennial Survey is authoritative but published every three years — structural latency. | BIS Triennial Survey |
| ATM Withdrawals | **56** | 18 | 16 | 12 | 10 | ATM network stats are annual/aggregate; cash-out is the last mile of measurability. | RBR/central-bank ATM statistics |
| Government Payments | **56** | 18 | 16 | 10 | 12 | Published in budget documents annually; auditable but coarse and lagged. | Treasury / budget disclosures |
| Bank Transfers | **54** | 18 | 16 | 12 | 8 | Central banks publish aggregate ACH/RTGS volumes but on a lag and without per-payment detail. | Central-bank payment statistics |
| CEX (Crypto) | **50** | 6 | 12 | 20 | 12 | Real-time but self-reported and wash-trade inflated; off-exchange internals unverifiable. | Exchange APIs, wash-trade adjusted (CCData) |
| Commodities | **48** | 12 | 12 | 10 | 14 | Exchange-traded volume is measured; physical OTC settlement is largely dark. | Exchange volumes; OTC estimated |
| Securities Settlement | **46** | 14 | 12 | 10 | 10 | CSD/ICSD annual reports give instruction counts; coarse and periodic. | DTCC, Euroclear, Clearstream reports |
| Interbank RTGS | **40** | 14 | 12 | 8 | 6 | Central banks publish system volumes; auditable but lagged and aggregate. | Central-bank RTGS statistics |
| RWA Tokenisation | **38** | 6 | 8 | 10 | 14 | On-chain and measurable, but small, early, and concentrated in a few issuers. | On-chain (rwa.xyz) |
| ETD (Derivatives) | **27** | 8 | 8 | 6 | 5 | Exchanges publish daily contract volumes; auditable and near-complete. | FIA, exchange daily statistics |
| Equity Markets | **24** | 6 | 6 | 6 | 6 | Consolidated tape is near real-time and auditable; only dark-pool share is opaque. | WFE, exchange tape |
| Stablecoins | **14** | 2 | 2 | 4 | 6 | On-chain transfers are per-tx and auditable; only issuer reserves add opacity. | On-chain (Etherscan, etc.) |
| L1/L2 Blockchain | **8** | 1 | 1 | 2 | 4 | The measurability anchor: every transaction is public, timestamped, and independently verifiable. | On-chain explorers / RPC |

## Country spotlight scores

| System | Opacity | Lat /30 | Gran /25 | Ver /25 | Cov /20 | Justification | Source |
|---|---|---|---|---|---|---|---|
| China | **88** | 24 | 22 | 22 | 20 | The largest blind spot in global finance: WMPs, shadow banking, and wallet internals surface only as PBOC aggregates, if at all. The ±6,000 TPS band exceeds whole sectors. | PBOC aggregates; shadow banking estimated |
| United Kingdom | **46** | 12 | 12 | 12 | 10 | Faster Payments and card rails are published, but London's dominant FX/OTC franchise is bilateral and opaque. | Pay.UK, BIS FX (London share) |
| Japan | **44** | 14 | 12 | 8 | 10 | JPX and bank rails are well-measured, but a large residual cash economy and fragmented QR wallets add coverage gaps. | BOJ, JPX, wallet operators |
| European Union | **38** | 12 | 10 | 8 | 8 | ECB publishes comprehensive payment statistics and MiCA adds crypto reporting; measurable but lagged and aggregate. | ECB payment statistics, MiCA disclosures |
| India | **30** | 8 | 8 | 8 | 6 | UPI publishes exact monthly counts with a ~10-day lag; among the most measurable large economies. Residual cash/informal keeps it above the blockchain floor. | NPCI UPI statistics |
| Brazil | **24** | 6 | 6 | 6 | 6 | Pix is published by the central bank with an open data programme; one of the most measurable payment systems on Earth. | Banco Central do Brasil Pix statistics |

## Challenge a score

Every score is **arguable from this rubric and its cited source**. To contest one, open a PR
editing `data/opacity.json` with **public, citable evidence** and a one-line justification.
Scores move on evidence, not opinion.

## Changelog

- **v1.0** (2026-07-20) — initial index: 28 categories + 6 country spotlights scored.

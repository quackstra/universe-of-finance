---
title: "AI Agent Transactions — Methodology"
parent: Emerging
grand_parent: Explore
nav_order: 103
---

# AI Agent Transactions -- Measurement Methodology

## Transaction Definition

One AI agent transaction = **one financial payment autonomously initiated,
negotiated, or settled by an AI agent without human-in-the-loop approval
for that specific payment event**.

Counted at: **settlement** (the payment is executed, not just requested).
Included: x402 protocol payments (API monetisation), AP2 protocol
payments, agent-to-agent commerce settlements, enterprise agent autonomous
procurement payments, autonomous DeFi agent trades/swaps.
Excluded: human-directed AI assistant purchases ("Siri, buy me a coffee"),
algorithmic/HFT trading (covered in traditional finance), IoT payments
(separate capsule), AI model training costs (not a payment transaction).

---

## Honest Assessment: This Is Mostly Speculative

**This is the most speculative category in the Universe of Finance.**

The entire category is less than 2 years old. The only protocol with
published transaction data (x402) has experienced a 92% decline from its
December 2025 peak. Industry projections span a 500x range (200 to
100,000 TPS by 2035). We present this analysis as scenario exploration,
not forecasting.

```
+-------------------------------------------------------------------+
|                  DATA AVAILABILITY SPECTRUM                        |
|                                                                     |
|  MEASURED                                        SPECULATIVE       |
|  <-----|---------|---------|---------|---------|--->               |
|        |         |         |         |         |                   |
|  x402 txn    x402 peak   Enterprise  Gartner   Agent-to-agent    |
|  count       daily vol   AI agent    $15T B2B  autonomous         |
|  (100M+      (731K)      deployment  prediction commerce          |
|  cumulative)              (80% F500)            (unmeasured)       |
|  [OBSERVED]  [OBSERVED]  [SURVEYED]  [PREDICTED][CONCEPTUAL]      |
|                                                                     |
|  Confidence decreases --->                                         |
+-------------------------------------------------------------------+
```

What we actually know:
- x402 has processed 100M+ cumulative transactions (on-chain, verifiable)
- x402 peaked at ~731K daily transactions (December 2025)
- x402 currently processes ~57K daily transactions (March 2026, -92%)
- x402 annual payment volume reached ~$600M in 2025
- 80% of Fortune 500 deploy multi-step AI agents (Gartner survey)
- Enterprise AI agent market valued at ~$7.8B (MarketsAndMarkets)

What we do not know:
- Whether x402 volume will recover, plateau, or continue declining
- How many enterprise AI agent actions involve actual payments
- Whether agent-to-agent commerce exists in meaningful volume
- Whether Gartner's $15T B2B prediction is within an order of magnitude

---

## Triangulation Approach

### Method A: x402 On-Chain Data (Observable)

x402 settles on Base (Coinbase L2). All transactions are queryable:
- Cumulative: 100M+ transactions
- Peak daily: ~731K (Dec 2025)
- Current daily: ~57K (Mar 2026)
- Annual run rate at current level: ~21M/year
- Annual run rate at peak: ~267M/year

### Method B: Enterprise Deployment Extrapolation

40% of enterprise apps will feature AI agents by 2026 (Gartner).
~500K enterprise apps globally x 40% = 200K AI-agent-enabled apps.
If 10% of agent actions involve payments: 200K x 1,000 payments/year
= 200M agent payment transactions.

### Method C: AI API Call Volume as Ceiling

Major AI providers (Anthropic, OpenAI, Google) process ~100B+ API
calls/year (estimated from revenue proxies). If 0.1-1% involve a
payment: **100M-1B** agent payment transactions.

```
+---------------------------------------------------+
|              RAW ESTIMATES                          |
|                                                     |
|  Method A            Method B          Method C     |
|  [x402 On-Chain]     [Enterprise]      [API Ceiling]|
|  +-------------+     +-----------+     +---------+  |
|  | 21-267M     |     | ~200M     |     | 100M-1B |  |
|  | (current to |     | (if 10%   |     | (if 0.1-|  |
|  |  peak rate) |     |  of agent |     |  1% of  |  |
|  |             |     |  actions  |     |  API     |  |
|  |             |     |  pay)     |     |  calls   |  |
|  +------+------+     +-----+-----+     +----+----+  |
|         |                  |                |        |
|         +------------------+----------------+        |
|                            v                         |
|              +------------------------+              |
|              |    RECONCILIATION      |              |
|              | All methods produce    |              |
|              | 100M-1B range for      |              |
|              | near-term (2026-2027). |              |
|              | But the 92% x402      |              |
|              | decline suggests the   |              |
|              | lower end is more      |              |
|              | realistic TODAY.       |              |
|              +----------+-------------+              |
|                         v                            |
|              +------------------------+              |
|              |   CURRENT STATE        |              |
|              |   ~21M/year (current)  |              |
|              |   ~0.66 TPS            |              |
|              |   Confidence: 34/100   |              |
|              +------------------------+              |
+---------------------------------------------------+
```

---

## Key Methodological Challenges

### Near-Zero Actual Data

Unlike every other category in the Universe of Finance, AI agent
transactions have essentially no historical baseline:

| Category          | Years of Data | Baseline Confidence |
|-------------------|--------------|---------------------|
| Consumer Cards    | 50+          | Very High           |
| Bank Transfers    | 30+          | High                |
| Gaming            | 15+          | Medium (derived)    |
| IoT/M2M           | 10+          | Medium              |
| RWA Tokenisation  | 5            | Low-Medium          |
| **AI Agents**     | **<2**       | **Very Low**        |

### The Hype Cycle Problem

x402's trajectory perfectly illustrates the Gartner Hype Cycle:

```
Volume  |         * Peak (731K/day, Dec 2025)
(daily) |        / \
        |       /   \
        |      /     \
        |     /       \    Where does it stabilise?
        |    /         \        ?
        |   /           \      / \
        |  /             \    /   ?
        | /               \  /
        |/                 \/  <- Trough (57K/day, Mar 2026)
        +-----|------|------|------|----->
              H1    H2     H1     H2
             2025  2025   2026   2026

The sustainable baseline is UNKNOWN.
Could stabilise at 50K, 200K, or 500K daily.
```

### Protocol Fragmentation Risk

The market may fragment across incompatible standards:
- **x402** (Coinbase): USDC on Base, HTTP-native
- **AP2** (Google): Multiple rails, enterprise-focused
- **Traditional** (Visa/MC): Agent commerce APIs on existing rails
- **Custom enterprise**: SAP, Oracle, Salesforce agent payment integrations

If standards fragment, no single protocol's data represents the market.

### Observable vs Predicted Split

```
AI Agent Transaction Estimates
+-------------------------------------------+
|                                           |
|  OBSERVED (verifiable today)              |
|  +-------------------------------------+ |
|  | x402: 100M+ cumulative              | |
|  | x402: ~57K daily (Mar 2026)         | |
|  | x402: $600M annual volume (2025)    | |
|  +-------------------------------------+ |
|                                           |
|  SURVEYED (reported, not verified)        |
|  +-------------------------------------+ |
|  | 80% Fortune 500 deploy AI agents    | |
|  | Enterprise AI agent market: $7.8B   | |
|  +-------------------------------------+ |
|                                           |
|  PREDICTED (analyst projections)          |
|  +-------------------------------------+ |
|  | Gartner: $15T B2B by 2028           | |
|  | Gartner: 20% programmable money 2030| |
|  | MarketsAndMarkets: $52.6B by 2030   | |
|  +-------------------------------------+ |
|                                           |
|  SPECULATIVE (no evidence base)           |
|  +-------------------------------------+ |
|  | Agent-to-agent autonomous commerce  | |
|  | Universal micropayment protocol     | |
|  | 100,000 TPS by 2035 (high scenario) | |
|  +-------------------------------------+ |
|                                           |
+-------------------------------------------+
```

---

## Overlap Analysis

```
AI agent payments are a FULL SUBSET of blockchain L1/L2 transactions
(for x402/AP2) or traditional payment rails (for enterprise agents):

+-------------------------------------------+
|  Total Payment Ecosystem                  |
|                                           |
|  +-- Blockchain L1/L2 ----------------+ |
|  |                                     | |
|  |  +-- x402 (Base/USDC) ----------+  | |
|  |  | AI agent crypto payments     |  | |
|  |  | (~21M/year current)          |  | |
|  |  +------------------------------+  | |
|  |                                     | |
|  +-------------------------------------+ |
|                                           |
|  +-- Traditional Rails ---------------+ |
|  |                                     | |
|  |  +-- Enterprise agent payments --+  | |
|  |  | AI agents using invoicing,    |  | |
|  |  | ACH, purchase orders          |  | |
|  |  | (volume UNKNOWN)              |  | |
|  |  +------------------------------+  | |
|  |                                     | |
|  +-------------------------------------+ |
+-------------------------------------------+

x402 payments: 100% subset of blockchain-l1-l2
Enterprise agent payments: subset of B2B bank transfers
```

---

## Coverage Assessment

```
Category: AI Agent Transactions (~21M annual at current run rate)

Protocol/Channel  Volume    Share   Data Quality
----------------- -------- ------- ----------------
x402 (Coinbase)   ########   ~90%  On-chain (excellent)
AP2 (Google)      #           ~2%  Not published
Enterprise custom ##          ~5%  Opaque
DeFi agents       #           ~3%  On-chain but not tagged
```

**Coverage**: x402 dominates observable data (~90% of known agent
payment volume). This means our estimate is essentially "x402 + a
small adjustment" rather than a true market-wide measurement.

---

## Confidence Assessment

```
                    Coverage   Recency   Authority   Granularity
                    ---------  --------  ----------  -----------
x402 On-Chain       ██████████ █████████ ██████████  ██████████
Gartner Surveys     ████████░  █████████ ████████░░  ██░░░░░░░░
MarketsAndMarkets   ██████░░░  █████████ ██████░░░░  ██░░░░░░░░
Enterprise Reports  ████░░░░░  ████████░ ██████░░░░  ██░░░░░░░░
AP2 / Google        ██░░░░░░░  ████████░ █████████░  █░░░░░░░░░
                    ---------  --------  ----------  -----------
Composite Score:    34/100     88/100    62/100      38/100
```

**Overall confidence: 34/100** -- The lowest in the Universe of Finance.
x402 on-chain data is excellent for what it covers, but it covers one
protocol in a pre-market category. The 500x spread between conservative
and high-growth TPS projections (200 to 100,000 by 2035) reflects
genuine fundamental uncertainty about whether AI agent commerce becomes
a dominant paradigm or remains niche. Any analysis of this space will
be outdated within months.

---

## Revision History

| Date       | Change                                          | Impact           |
|------------|------------------------------------------------|------------------|
| 2026-03-26 | Initial estimate: ~0.66 TPS (current), 34/100  | Baseline         |
| 2026-03-26 | Peak reference: ~8.5 TPS (Dec 2025)            | Historical peak  |

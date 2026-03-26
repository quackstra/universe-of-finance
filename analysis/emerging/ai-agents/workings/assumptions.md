# AI Agent Transactions — Assumptions

> Every assumption documented with reasoning. Referenced from calculations and projections.

---

## Data Collection Assumptions

### A1. x402 as Primary Data Source
**Assumption:** The x402 protocol's published transaction statistics represent the majority (~60-80%) of all publicly visible AI agent payment transactions.
**Reasoning:** x402 is the first and most adopted agent payment protocol, with published metrics (100M+ cumulative txns, $600M annual volume). Google's AP2 does not publish comparable metrics yet.
**Risk:** Significant AI agent payment activity may occur through custom enterprise solutions, traditional payment APIs, and private channels not captured by x402 metrics.

### A2. "AI Agent Transaction" Definition
**Assumption:** An AI agent transaction is one where an autonomous AI system (not a human) makes the payment decision and initiates the payment.
**Reasoning:** This distinguishes from: (a) human-initiated payments processed by AI (e.g., voice assistant shopping), (b) algorithmic/HFT trading (rules-based, not AI-autonomous), (c) traditional automated payments (cron jobs, scheduled transfers).
**Risk:** The boundary is fuzzy and becoming fuzzier. As AI agents become embedded in more systems, the distinction between "AI-initiated" and "automated" payments may become meaningless.

### A3. Market Data Vintage
**Assumption:** Transaction volume data is current as of March 2026. Market size projections use 2025 base figures.
**Reasoning:** This is the most rapidly changing category; any data older than 6 months is potentially outdated.
**Risk:** The 92% decline in x402 daily volume (Dec 2025 to Mar 2026) means our snapshot captures a post-hype period. Volumes could recover, stabilise, or decline further.

---

## Market Assumptions

### A4. Enterprise AI Agent Market Size
**Assumption:** The AI agent market is $7.8B (2025) growing to $52.6B (2030) at 46.3% CAGR.
**Reasoning:** MarketsAndMarkets projection, corroborated by Gartner's prediction that 40% of enterprise apps will feature AI agents by 2026 (up from 5% in 2025).
**Risk:** Market size figures from research firms in nascent categories routinely miss by 2-3x in either direction. The 46.3% CAGR may be aggressive or conservative.

### A5. Gartner $15T B2B Prediction
**Assumption:** Gartner's prediction that AI agents will "command" $15T in B2B purchases by 2028 refers to AI-influenced or AI-recommended purchases, not necessarily AI-initiated payment transactions.
**Reasoning:** "Command" likely means AI agents are involved in the purchasing decision (recommendation, negotiation, vendor selection) rather than literally initiating $15T in autonomous payments.
**Risk:** If taken literally, $15T in agent-initiated payments by 2028 would be revolutionary. We use 5-10% of this figure as the agent-initiated portion in projections.

### A6. Gartner 20% Programmable Money
**Assumption:** Gartner's prediction that 20% of monetary transactions will be programmable by 2030 is an aspiration that partially materialises (1-5% realistic).
**Reasoning:** "Programmable money" is broader than AI agent transactions — it includes smart contracts, conditional payments, and automated settlement. Even 1% would be transformative.
**Risk:** This prediction may refer to programmable capability rather than actual usage. Many transactions could be *capable* of programmability without actually using it.

---

## Projection Assumptions

### A7. Baseline Growth Trajectory
**Assumption:** AI agent payment transactions grow at ~80-100% CAGR from 2026-2030, then 50-60% CAGR from 2030-2035.
**Reasoning:** Aligned with the enterprise AI agent market CAGR (46.3%) plus additional growth from x402/AP2 protocol adoption. Payment growth should exceed market size growth because more agents and more transactions per agent.
**Risk:** The 92% daily volume decline in early 2026 could indicate that sustainable growth will be much slower. Alternatively, it could be a temporary correction.

### A8. Average Transaction Value Evolution
**Assumption:** Average AI agent transaction value grows from ~$6 (2025, API calls) to ~$20 (2030, mix of API calls and procurement) to ~$20 (2035, scale effect keeps average moderate despite larger individual transactions).
**Reasoning:** Early transactions are micro-payments for API access ($0.01-$10). As agents move to procurement and B2B commerce, individual transaction values increase. But the volume of micro-payments grows faster, keeping the average moderate.
**Risk:** If agent commerce is dominated by B2B procurement (high value, low count), the profile looks very different from API monetisation (low value, high count).

### A9. High Growth Scenario
**Assumption:** 100M+ autonomous AI agents operate globally by 2030, each averaging 1,577 payment transactions per year.
**Reasoning:** Gartner predicts 40% of enterprise apps have AI agents by 2026. If there are 500M enterprise software instances and 40% have agents by 2028, that's 200M agents. Not all make payments, but the high-growth scenario assumes aggressive adoption.
**Risk:** Extremely speculative. Autonomous spending authority for AI agents requires trust, governance frameworks, and liability resolution that may take a decade to develop.

### A10. Conservative Scenario
**Assumption:** AI agent payments remain primarily crypto-native, limited to API monetisation and DeFi bot transactions.
**Reasoning:** Enterprise caution about granting autonomous spending authority to AI agents. Regulatory frameworks for AI liability develop slowly. Traditional B2B payment flows (invoicing, POs) persist.
**Risk:** May be too pessimistic if enterprise adoption of x402/AP2 accelerates faster than expected.

---

## Risk Factors

### R1. Regulatory Risk
AI agents making autonomous financial decisions raises unresolved legal questions: who is liable for a bad purchase? Can an AI agent enter a binding contract? Are agent wallets subject to KYC/AML? These questions are being actively debated but not resolved.

### R2. Security Risk
Autonomous AI agents with payment authority are a novel attack surface. Prompt injection, adversarial manipulation, and agent compromise could lead to financial losses. The "two-stage commit" pattern (draft → preview → confirm) is a mitigation but adds friction.

### R3. Protocol Fragmentation
x402, AP2, and potential future protocols could fragment the market. If agents need different protocols for different services, adoption friction increases.

### R4. Hype Cycle Risk
The 92% decline in x402 daily volume is a warning signal. Crypto-adjacent technologies frequently experience hype cycles where initial excitement vastly outpaces sustained utility. AI agent payments may follow the same pattern.

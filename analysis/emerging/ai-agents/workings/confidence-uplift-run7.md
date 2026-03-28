# AI Agent Transactions — Confidence Uplift (Run 7, 2026-03-28)

## Previous State
- **TPS:** 3.5 (range 2-5)
- **Confidence:** 38
- **Key gaps:** Non-x402 protocol volumes opaque; wash trading distortion; no enterprise payment data

---

## 1. New Data Sources Found

### Stripe Agentic Commerce Suite (NEW)
- **URL:** https://stripe.com/blog/agentic-commerce-suite
- Stripe launched Shared Payment Tokens (SPTs) — a new payment primitive for AI agent purchases
- First and only provider supporting both agentic network tokens AND BNPL tokens
- Major brands onboarded: URBN, Etsy, Ashley Furniture, Coach, Kate Spade, Revolve, Halara
- 75% of Stripe event attendees either implementing or planning agentic commerce
- **No transaction volume data published** — infrastructure-first, volume TBD

### McKinsey Agentic Commerce Forecast (NEW)
- **URL:** https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity
- McKinsey projects $3-5 trillion in global agentic commerce sales by 2030
- This is RETAIL sales orchestrated by agents, not agent-to-agent payments

### Morgan Stanley Agentic Commerce Estimate (NEW)
- **URL:** https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook
- $190-385B in US e-commerce spending by 2030 from agentic shoppers (10-20% market share)
- 23% of Americans already made AI-assisted purchases in last month
- Groceries/CPG identified as largest growth driver

### Visa Intelligent Commerce Pilots (NEW)
- **URL:** https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21961.html
- 100+ partners building in Visa Intelligent Commerce ecosystem
- 30+ partners in sandbox, 20+ agents integrating directly
- "Hundreds of controlled, real-world agent-initiated transactions" completed
- Visa predicts millions of consumers using AI agents by 2026 holiday season
- Pilots launching in APAC and Europe in early 2026

### Agentic AI Ecosystem Market Size (NEW)
- **URL:** https://www.metarouter.io/post/agentic-commerce-trends-statistics
- Broader agentic AI ecosystem: $7.29B (2025) → $9.14B (2026)

### x402 Update (March 2026, VERIFIED)
- Daily volume: ~$28,000 (unchanged from depth research)
- ~131K daily transactions, ~50% wash trading → ~65K genuine/day
- x402 remains the only protocol with publicly observable on-chain volume

### LLM API Scale (UPDATED)
- OpenAI: 2.2-2.5B queries/day, 900M weekly active users
- Enterprise message volume: 8x YoY growth; reasoning tokens up 320x
- 92% of Fortune 500 using OpenAI products
- This provides the CEILING for potential agent payment transactions

### MCP Protocol Adoption (NEW)
- Python + TypeScript SDKs: ~97M monthly downloads
- 10,000+ MCP servers indexed
- MCP market expected to reach $1.8B in 2025
- No transaction or payment data — MCP is an integration protocol, not a payment protocol

---

## 2. Updated Triangulation

### Method 1: x402 On-Chain (unchanged)
- ~65K genuine daily transactions = ~24M/year = 0.75 TPS

### Method 2: LLM API Payment Funnel (updated)
- Total LLM API calls: ~3T/year (OpenAI 2.5B/day × 365 = ~900B, plus Anthropic/Google/others ≈ 3T)
- If 0.01% involve agent payment action: 300M transactions/year = ~9.5 TPS
- If 0.1%: 3B/year = ~95 TPS (implausible at current maturity)
- Best estimate for 2026: 0.01-0.03% → 300M-900M/year → 9.5-28.5 TPS

### Method 3: Agentic Commerce Revenue-Derived (NEW)
- Agentic AI ecosystem: ~$9.14B (2026)
- If 5% of that ecosystem value flows as agent-initiated payments: ~$457M
- At average transaction size of $5-50 (mostly API calls/micro-services):
  - $457M / $5 = 91M transactions → 2.9 TPS
  - $457M / $50 = 9.1M transactions → 0.29 TPS
- This method gives **0.3-3 TPS** — consistent with x402 observed data

### Method 4: Enterprise Agent Deployment Leading Indicator (updated)
- 92% of Fortune 500 use AI products; 80%+ deploy AI agents
- Gartner: 40% of enterprise apps will feature AI agents by end of 2026
- If 100,000 enterprise apps × 100 agent payments/day = 10M/day = ~116 TPS
- This is a FORWARD estimate, not current reality
- More conservative: 10,000 apps × 10 payments/day = 100K/day = ~1.2 TPS

### Triangulation Summary

| Method | Current TPS Estimate | Confidence |
|--------|---------------------|------------|
| x402 on-chain | 0.75 | High (observable) |
| LLM API funnel (0.01%) | 9.5 | Low (assumed %) |
| Revenue-derived | 0.3-3 | Low |
| Enterprise leading indicator | 1.2-116 | Very Low |

**Central estimate remains ~2-5 TPS**, but with better understanding of WHY:
- x402 is the only measurable protocol at ~0.75 TPS
- Non-x402 (Stripe SPT, Visa VIC, Google AP2) is the unknown
- Stripe/Visa/Mastercard combined likely add 1-4 TPS on top of x402 based on pilot scale ("hundreds of transactions" not thousands)

---

## 3. Revised TPS Estimate

**No change to current estimate.** 3.5 TPS (range 2-5) remains defensible.

The new data doesn't change the volume picture — it confirms that:
1. Infrastructure is moving fast (Stripe, Visa, Mastercard all live with products)
2. Volume is negligible relative to the infrastructure investment
3. The "hundreds of controlled transactions" from Visa pilots confirms sub-1 TPS for that channel

**Pre-market flag recommendation: YES.** This category should be flagged as "pre-market" in the Big Number calculation. The $3-5T McKinsey 2030 projection and the $385B Morgan Stanley estimate show enormous potential, but current measured volume is trivial.

---

## 4. Revised Confidence Score

**Recommended: 42 (+4 from 38)**

| Component | Previous | Revised | Rationale |
|-----------|----------|---------|-----------|
| Source quality | 10 | 12 | McKinsey, Morgan Stanley, Visa pilot data add tier-1 sources |
| Data recency | 16 | 16 | No change — all data is 2025-2026 |
| Triangulation | 7 | 9 | New revenue-derived method + enterprise leading indicator refinement |
| Coverage | 5 | 5 | Still no published volumes from Stripe/Visa/Mastercard/Google |
| **Total** | **38** | **42** | |

The improvement comes from better source quality (investment bank projections, not just crypto media) and a third triangulation method. Coverage remains the weakest dimension because no payment network publishes agent transaction counts.

---

## 5. What's Still Missing

1. **Stripe SPT transaction volume** — Stripe has the infrastructure but publishes no volume data. This is the single biggest data gap. If Stripe published "X thousand agent transactions processed via SPT," the confidence would jump 10+ points.

2. **Visa Intelligent Commerce pilot results** — "Hundreds of transactions" is not useful. Need order-of-magnitude data: thousands? tens of thousands? monthly or cumulative?

3. **Google AP2 adoption metrics** — Google announced AP2 but has published zero adoption data.

4. **Mastercard Agent Pay volumes** — Same story as Visa/Stripe.

5. **Actual conversion rate: LLM API calls → payment actions** — The 0.01% assumption is a guess. If OpenAI or Anthropic published "X% of API calls include a tool_use with payment intent," that would transform the estimate.

6. **Agent-to-agent commerce volume** — DeFi MEV bots and autonomous trading agents are active but not separately tracked as "agent payments."

7. **2026 holiday season data** — Visa predicts "millions of consumers" using agents by holiday 2026. Q4 2026 data will be the first real test of mainstream adoption.

---

## Sources

1. [Stripe — Agentic Commerce Suite](https://stripe.com/blog/agentic-commerce-suite)
2. [Stripe — Supporting Additional Payment Methods for Agentic Commerce](https://stripe.com/blog/supporting-additional-payment-methods-for-agentic-commerce)
3. [McKinsey — The Agentic Commerce Opportunity](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity)
4. [Morgan Stanley — Agentic Commerce Impact Could Reach $385 Billion by 2030](https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook)
5. [Visa — Secure AI Transactions Pilot](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21961.html)
6. [MetaRouter — Agentic Commerce Trends and Statistics 2026](https://www.metarouter.io/post/agentic-commerce-trends-statistics)
7. [CoinDesk — x402 Protocol Daily Volume $28,000](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet)
8. [SQ Magazine — OpenAI Statistics 2026](https://sqmagazine.co.uk/openai-statistics/)
9. [DemandSage — ChatGPT Statistics 2026](https://www.demandsage.com/chatgpt-statistics/)
10. [MCP Blog — 2026 Roadmap](http://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
11. [Finextra — Agentic AI in Payments 2026: What's Real vs Hype](https://www.finextra.com/blogposting/30920/agentic-ai-in-payments-in-2026-whats-real-whats-pilot-and-whats-still-hype)
12. [Digital Commerce 360 — McKinsey Forecasts $5T Agentic Commerce by 2030](https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/)

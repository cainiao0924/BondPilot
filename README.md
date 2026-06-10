# BondPilot

BondPilot is an AI + Web3 agent prototype for interest-rate market review and controlled on-chain execution.

It uses real treasury futures, intraday bars, funding sentiment and institution behavior data to generate daily market reviews. YieldAgent then converts the review into auditable strategy suggestions, wallet-policy constraints and mock on-chain execution tasks.

## Problem

Interest-rate trading requires fast interpretation of futures prices, funding conditions, institution behavior and technical signals. Traditional reports are not directly actionable, and AI agents need explicit risk controls before they can interact with wallets or execution systems.

## Solution

BondPilot builds a structured pipeline:

1. Collect treasury futures data, intraday bars, funding sentiment and institution behavior.
2. Generate a daily bond futures review.
3. Use YieldAgent to convert the review into a structured decision.
4. Attach wallet policy, budget limits and human approval requirements.
5. Prepare a mock Cobo Agentic Wallet action for audit and demonstration.

## Demo Flow

```text
DM Data
→ OSS
→ Market Context
→ Report Generator
→ YieldAgent
→ Wallet Policy
→ Cobo Action Mock
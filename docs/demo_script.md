# Demo Script

## Step 1: Show Automated Market Review

BondPilot first collects treasury futures data, intraday bars, funding sentiment and institution behavior. It generates a daily market review and Feishu image report.

## Step 2: Show Market Context

The market context JSON contains funding sentiment, money market rates and institution behavior by banks, securities firms, insurers and funds.

## Step 3: Run YieldAgent

YieldAgent reads the market context and daily review, then produces a structured decision JSON.

## Step 4: Show Wallet Policy

The decision JSON includes a demo-only wallet policy:

- max budget: 100 USDC
- human approval required
- no real trade execution
- no private key access

## Step 5: Show Cobo Action Mock

YieldAgent prepares a mock Cobo Agentic Wallet action. The action is pending human approval and cannot execute real trades.
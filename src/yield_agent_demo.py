# -*- coding: utf-8 -*-
"""
YieldAgent v0.1 for BondPilot

This demo reads market context and a daily bond futures review,
then produces an auditable strategy suggestion and a mock wallet policy action.

It is demo-only and does not execute real trades.
"""

import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLES_DIR = PROJECT_ROOT / "samples"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def extract_market_view(market_context: dict, report_text: str) -> str:
    funding = market_context.get("funding", {})
    institution = market_context.get("institution_behavior", {})

    funding_comment = funding.get("comment", "")
    insti_comment = institution.get("comment", "")

    parts = []

    if funding_comment:
        parts.append(funding_comment)

    if insti_comment:
        parts.append(insti_comment)

    if not parts and report_text:
        first_lines = [x.strip() for x in report_text.splitlines() if x.strip()]
        parts.append(" ".join(first_lines[:5]))

    if not parts:
        return "Market context is unavailable. YieldAgent keeps observe-only mode."

    return " ".join(parts)


def decide_signal(market_context: dict, report_text: str):
    """
    Very simple rule engine for hackathon MVP.
    Later this can be replaced by an LLM or a more formal strategy engine.
    """
    text = (json.dumps(market_context, ensure_ascii=False) + "\n" + report_text).lower()

    action_plan = [
        "Do not execute any real trade in demo mode.",
        "Use TL and T as the main observation targets.",
        "Check whether intraday strength is confirmed by funding and institution behavior."
    ]

    caution_terms = ["追多性价比下降", "偏紧", "震荡", "等待确认", "回落", "压制"]
    positive_terms = ["偏买", "转松", "站上", "偏强", "买方"]

    caution_score = sum(1 for term in caution_terms if term in text)
    positive_score = sum(1 for term in positive_terms if term in text)

    if caution_score >= positive_score:
        signal = "observe"
        risk_level = "medium"
        action_plan.extend([
            "Keep observe-only stance before confirmation.",
            "Do not chase TL at high level.",
            "Watch whether T and TL can hold key moving-average support."
        ])
    else:
        signal = "watch_for_long_duration"
        risk_level = "medium-high"
        action_plan.extend([
            "Watch for possible duration extension signal.",
            "Require human approval before any wallet-budget action.",
            "Confirm with funding, institution behavior and technical levels."
        ])

    return signal, risk_level, action_plan


def build_wallet_policy(signal: str, risk_level: str) -> dict:
    return {
        "mode": "demo_only",
        "max_budget": "100 USDC",
        "requires_human_approval": True,
        "no_real_trade": True,
        "allowed_actions": [
            "create_demo_budget",
            "create_audit_log",
            "prepare_policy_guarded_task"
        ],
        "blocked_actions": [
            "real_trade",
            "unapproved_transfer",
            "private_key_access"
        ],
        "risk_level": risk_level,
        "policy_note": "YieldAgent can only create a mock wallet action. Real execution requires explicit human approval."
    }


def build_cobo_action_mock(signal: str) -> dict:
    return {
        "platform": "Cobo Agentic Wallet",
        "action": "create_policy_guarded_task",
        "asset": "USDC",
        "amount": "100",
        "purpose": "demo strategy budget for YieldAgent",
        "status": "pending_human_approval",
        "execution": "mock_only",
        "reason": f"YieldAgent signal is {signal}."
    }


def generate_decision(date: str) -> dict:
    market_context_path = SAMPLES_DIR / f"market_context_{date}.json"
    report_path = SAMPLES_DIR / f"bond_futures_formal_review_{date}.md"

    market_context = load_json(market_context_path)
    report_text = load_text(report_path)

    market_view = extract_market_view(market_context, report_text)
    signal, risk_level, action_plan = decide_signal(market_context, report_text)

    decision = {
        "project": "BondPilot",
        "agent": "YieldAgent",
        "version": "v0.2",
        "date": date,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "market_view": market_view,
                "decision_basis": [
            "Funding sentiment and money market rates are used to judge liquidity pressure.",
            "Institution behavior is used to identify main buyers and sellers in 30Y and 10Y bonds.",
            "Daily futures review and intraday bars are used to judge TL/T market structure.",
            "The agent stays in observe mode when signals are mixed or when chasing risk is high."
        ],
        "risk_controls": [
            "Demo only.",
            "No real trade execution.",
            "Human approval required before wallet action.",
            "Max demo budget is limited to 100 USDC.",
            "Private keys are never exposed to the agent."
        ],
        "why_cobo_wallet": "Cobo Agentic Wallet is used as the controlled execution layer. YieldAgent can only prepare a policy-guarded mock task with budget limits and human approval, instead of directly moving assets.",
        "signal": signal,
        "risk_level": risk_level,
        "action_plan": action_plan,
        "wallet_policy": build_wallet_policy(signal, risk_level),
        "cobo_action_mock": build_cobo_action_mock(signal),
        "audit_note": "Decision generated from treasury futures review, DM intraday data, funding sentiment and institution behavior. Demo only; not investment advice."
    }

    return decision


def main():
    date = "20260605"
    decision = generate_decision(date)

    output_path = SAMPLES_DIR / f"yield_agent_decision_{date}.json"
    output_path.write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(decision, ensure_ascii=False, indent=2))
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
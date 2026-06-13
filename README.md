# BondPilot

BondPilot

面向利率市场复盘与受策略约束钱包动作提案的 AI + Web3 Agent 原型

BondPilot 是一个面向利率市场的 AI + Web3 Agent 原型，用于自动完成国债期货市场复盘，并生成受策略约束的钱包动作提案。

系统使用真实的国债期货行情、日内 K 线、资金情绪、货币市场利率和机构行为数据，自动生成每日市场复盘。随后，YieldAgent 将复盘结果转化为结构化、可审计的市场判断、风险控制规则、钱包策略约束，以及模拟的 Cobo Agentic Wallet 动作提案。

当前 MVP 不执行真实链上交易，不访问私钥，也未直接接入 Cobo SDK。项目重点展示 AI Agent 如何在预算限制、人工审批、权限控制和审计要求下，安全地生成钱包动作提案。

## Problem

BondPilot 构建了一套结构化的利率市场 Agent 工作流：

自动获取国债期货行情、日内 K 线、资金情绪、货币市场利率和机构行为数据。
自动生成每日国债期货复盘。
由 YieldAgent 将复盘内容转化为结构化决策。
为决策附加预算限制、人工审批、允许动作和禁止动作等钱包策略。
生成模拟的 Cobo Agentic Wallet 动作提案，用于展示和审计。

完整流程如下：

DM 真实市场数据
→ 阿里云函数与 OSS
→ 每日国债期货复盘
→ YieldAgent 决策
→ Wallet Policy 钱包策略
→ Cobo Action Mock 动作提案
→ 审计记录v

## Solution

BondPilot 构建了一套结构化的工作流程：

自动获取国债期货行情、日内 K 线、资金情绪和机构行为数据。
自动生成每日国债期货复盘。
使用 YieldAgent 将复盘内容转化为结构化决策。
为决策附加钱包策略、预算限制和人工审批要求。
生成模拟的 Cobo Agentic Wallet 动作提案，用于审计和演示。

## Demo Flow
DM 数据 → OSS 存储 → 市场环境数据 → 报告生成器 → YieldAgent 决策 → 钱包策略 → Cobo 动作模拟提案

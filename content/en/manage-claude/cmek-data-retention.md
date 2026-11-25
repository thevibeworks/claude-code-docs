---
title: CMEK, data retention, and ZDR
url: https://platform.claude.com/docs/en/manage-claude/cmek-data-retention
description: Why a workspace with a key retains data, what that means for ZDR, and what Anthropic can preserve outside your key.
---

On Claude Platform, customer-managed encryption keys (CMEK) and [legacy zero data retention (Legacy ZDR)](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) can’t share a workspace. On Claude Enterprise, an organization can use CMEK and Claude Code ZDR together, but it then [can’t turn on Claude Docs or Claude Sheets](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).

However, on Claude Platform you can attach a key to a workspace that uses [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS). EFS is ZDR, and the workspace’s Sealed Safety Data is written to storage that you own. EFS is in beta. For the steps, see [Attach a customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key) in the EFS guide.

## A key needs a workspace that retains data

CMEK encrypts stored data, and under Legacy ZDR on Claude Platform, Anthropic doesn’t store your prompts or responses. With [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS), Anthropic encrypts your Sealed Safety Data under your key before writing it to your bucket. So you can attach a key only to a workspace with **Standard data retention** (30 days) or one that uses EFS.

After you attach a key, you can’t turn off data retention for that workspace. To go back to a workspace that doesn’t retain data, create a new one and move your traffic to it.

## In a Legacy ZDR organization

A Legacy ZDR organization on Claude Platform can use CMEK. You switch one workspace to **Standard data retention**, accept the data retention terms, and attach your key to it. The workspace you switch can’t be the default workspace, whose retention follows the organization’s. Your other workspaces keep Legacy ZDR.

[Choose your setup page](https://platform.claude.com/docs/en/manage-claude/cmek#set-it-up) and follow its attach step.

## Limited preservation outside your key

In three narrow cases, Anthropic may preserve specific records under Anthropic-managed encryption:

* Where Anthropic is required by law to retain records (for example, material reported to NCMEC under 18 U.S.C. § 2258A)
* Exigent risk of serious harm (for example, CBRNE weapons development, offensive cyberattacks, or imminent threats of violence)
* Violations of Section D.4 of Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) or equivalent terms in a customer’s other applicable agreement with Anthropic

Outside of [CSAM screening](https://support.claude.com/en/articles/9020328-csam-detection-and-reporting), preservation requires a human reviewer’s explicit decision and follows Anthropic’s [retention policy for commercial data](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data). For every instance of preservation, a corresponding [Compliance API Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) event is generated with a reason code conveying the purpose of the preservation. See [CMEK content preservation](https://platform.claude.com/docs/en/manage-claude/access-transparency#cmek-content-preservation) for details. Safety screening metadata is retained under Anthropic-managed encryption and remains readable after key revocation. These are records derived from Anthropic’s automated safety scans, such as pattern identifiers and match indicators, not conversation content.

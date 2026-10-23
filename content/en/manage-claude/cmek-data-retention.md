---
title: CMEK, data retention, and ZDR
url: https://platform.claude.com/docs/en/manage-claude/cmek-data-retention
description: Why a workspace with a key retains data, what that means for ZDR, and what Anthropic can preserve outside your key.
---

On Claude Platform, customer-managed encryption keys (CMEK) and [zero data retention (ZDR)](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) can't share a workspace. On Claude Enterprise, an organization can use CMEK and ZDR together, but it then [can't turn on artifacts](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).

## A key needs a workspace that retains data

CMEK encrypts stored data, and under ZDR on Claude Platform, Anthropic doesn't store your prompts or responses. So you can attach a key only to a workspace with **Standard data retention** (30 days).

After you attach a key, you can't turn off data retention for that workspace. To return to ZDR, create a new workspace and move your traffic to it.

## In a ZDR organization

A ZDR organization on Claude Platform can use CMEK. You switch one workspace to **Standard data retention**, accept the data retention terms, and attach your key to it. The workspace you switch can't be the default workspace, whose retention follows the organization's. Your other workspaces keep ZDR.

[Choose your setup page](https://platform.claude.com/docs/en/manage-claude/cmek#set-it-up) and follow its attach step.

## Limited preservation outside your key

In three narrow cases, Anthropic may preserve specific records under Anthropic-managed encryption:

* Where Anthropic is required by law to retain records (for example, material reported to NCMEC under 18 U.S.C. § 2258A)
* Exigent risk of serious harm (for example, CBRNE weapons development, offensive cyberattacks, or imminent threats of violence)
* Violations of Section D.4 of Anthropic's [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) or equivalent terms in a customer's other applicable agreement with Anthropic

Outside of [CSAM screening](https://support.claude.com/en/articles/9020328-csam-detection-and-reporting), preservation requires a human reviewer's explicit decision and follows Anthropic's [retention policy for commercial data](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data). For every instance of preservation, a corresponding [Compliance API Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) event is generated with a reason code conveying the purpose of the preservation. See [CMEK content preservation](https://platform.claude.com/docs/en/manage-claude/access-transparency#cmek-content-preservation) for details. Safety screening metadata is retained under Anthropic-managed encryption and remains readable after key revocation. These are records derived from Anthropic's automated safety scans, such as pattern identifiers and match indicators, not conversation content.

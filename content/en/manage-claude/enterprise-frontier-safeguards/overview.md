---
title: Enterprise Frontier Safeguards
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview
description: Zero Data Retention (ZDR) for eligible organizations that use Claude's most capable models, with Sealed Safety Data in your own cloud account.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

Enterprise Frontier Safeguards (EFS) is [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) for eligible organizations that use [Claude’s most capable models](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements), such as Claude Fable 5.1. Anthropic doesn’t retain your prompts and responses. Sealed Safety Data is written to storage that you own. EFS requires your own bucket. A workspace on [Anthropic-managed storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) isn’t on EFS, because Anthropic stores encrypted copies of that workspace’s prompts and responses.

Use EFS when you want Claude’s most capable models but need to keep your Sealed Safety Data in your own cloud account. With EFS, people at your organization, not reviewers at Anthropic, review [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). EFS includes both:

* [Customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage): A bucket that receives your Sealed Safety Data (prompts, responses, and model reasoning, encrypted in Anthropic’s format). Your team can’t read Sealed Safety Data, even in your own bucket.
* [Your team reviews Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases): Anthropic Human Review is always off, so your own team reviews flagged cases that automated safety monitoring finds.

<Frame>
  ![EFS, Anthropic managed, and Legacy ZDR compared. Enterprise Data Controls covers review and the key on Anthropic managed.](https://platform.claude.com/docs/images/efs-how-it-works-enterprise-data-controls.svg)
</Frame>

Anthropic doesn’t charge for EFS, and EFS doesn’t change model behavior, API pricing, or rate limits. Your cloud provider bills you for that storage as usual, including reads, writes, and data egress.

EFS covers requests to the Messages API in a workspace configured for EFS regardless of model. It does not cover data that is stored by Claude Platform features for their own use, even within a Messages API request, such as code execution containers, Files API uploads, Batch API results, and Claude Managed Agents sessions. See [Data and retention](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#data-and-retention) in the FAQ.

## Get access

To get EFS, follow these steps:

1. If the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console already shows **Enterprise Frontier Safeguards**, skip to step 2. Otherwise, contact your Anthropic account team to request access. If you don’t have an account team, complete the [Enterprise Frontier Safeguards request form](https://claude.com/form/enterprise-frontier-safeguards).
2. Once Anthropic confirms that your organization is eligible, an Organization Admin accepts the terms from the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console.
3. To set up EFS, follow the [EFS setup guide for your platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console).

On Amazon Bedrock, you get access through AWS. See [Enterprise Frontier Safeguards on Amazon Bedrock](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-amazon-bedrock).

## On Claude Platform, EFS applies to a whole workspace

Once EFS takes effect for a workspace, it applies to every request to every model in that workspace, including models that don’t require data retention.

To use EFS for only some traffic, use separate workspaces. The [API key](https://platform.claude.com/docs/en/manage-claude/workspaces#api-keys-and-resource-scoping) or workspace ID that you send determines which card a request uses. A new workspace leaves your existing workspaces and their API keys as they are.

## Enterprise Data Controls

On Claude Platform, accepting the [EFS and Enterprise Data Controls terms](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access) gives you both. With Enterprise Data Controls, you can [use a customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys) or [turn off Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) on Anthropic-managed storage. With either one, [Access Transparency](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency) is on for your organization.

## See also

<CardGroup cols={2}>
  <Card title="Set up customer-owned storage" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage">
    Keep your Sealed Safety Data in storage in your own cloud account.
  </Card>

  <Card title="Review Safety Cases" icon="file" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases">
    Receive, investigate, and respond to the Safety Cases that Anthropic sends.
  </Card>

  <Card title="Use a customer-managed key" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys">
    Encrypt your data using a key you hold in your own key management service, with EFS or with Anthropic-managed storage.
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Setup guide" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console">
    Get access and set up EFS on the platform you use.
  </Card>

  <Card title="Enterprise Frontier Safeguards FAQ" icon="book" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq">
    Answers to common questions about EFS.
  </Card>
</CardGroup>

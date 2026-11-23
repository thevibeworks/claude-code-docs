---
title: Human Review and Access Transparency
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency
description: Turn off Anthropic Human Review and check your record of Anthropic's access to your data.
---

<Warning>
  Enterprise Data Controls is in beta on Claude Platform. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

Anthropic’s automated safety monitoring checks your prompts and responses, and a small, specialized team at Anthropic can review what it finds. This is called Anthropic Human Review, and it’s on by default for new workspaces that use Anthropic-managed storage.

On Claude Platform, Enterprise Data Controls allows you to [turn off Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) on Anthropic-managed storage. [Enterprise Frontier Safeguards (EFS)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) allows you to [bring your own storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage) and [do your own review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). Eligible enterprise organizations on Claude Platform can get both by accepting the terms from the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console. Before you accept, read [What getting access changes](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access).

[Access Transparency](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency) gives you a record each time someone at Anthropic views your data. Access Transparency does not cover every piece of data in your organization. See [what Access Transparency doesn’t cover](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-does-not-cover).

## When does automated safety monitoring access your data?

The following table shows how and when automated safety monitoring and Anthropic Human Review can access your data:

| Who | When | What record you get |
| ----- | ----- | ----- |
| Automated safety monitoring systems | Every workspace with Anthropic-managed storage or Enterprise Frontier Safeguards. Not on workspaces on **Legacy ZDR**. These systems check your prompts and responses for misuse. This check is fully automated, so no person sees your content at this step. | No [`anthropic_access` event](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency). |
| A small, specialized team of approved reviewers at Anthropic | Only while Anthropic Human Review is on. Only this team reviews what automated safety monitoring finds. See [reason codes](https://platform.claude.com/docs/en/manage-claude/access-transparency#reason-codes) for the types of reasons Anthropic would access content. | An `anthropic_access` event each time someone views your data, where [Access Transparency covers](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-covers) the access. |

With [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage), Anthropic’s systems write your Sealed Safety Data to your bucket and read it back to run automated safety monitoring. For an Amazon S3 bucket, see [Anthropic’s calls in AWS CloudTrail](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#cloudtrail).

## Turn off Anthropic Human Review

If you have configured Enterprise Frontier Safeguards for a workspace, your own team gets a [Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) to review instead of Anthropic’s team. Ensure you have read [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#where-cases-arrive) before turning off Anthropic Human Review.

Anthropic’s Claude Managed Agents service doesn’t run sessions or [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) in a workspace with Anthropic Human Review off. That workspace’s existing sessions stop accepting new messages. The [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) refuses new batches in that workspace too. To run sessions, dreams, or batches, create them in a workspace that has Anthropic Human Review on.

To configure Anthropic Human Review for a workspace, go to the [Data retention](https://platform.claude.com/settings/privacy) page as an Organization Admin. A change can take up to 2 hours to apply. Workspaces that use Enterprise Frontier Safeguards always have Anthropic Human Review off. On Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS, using Enterprise Frontier Safeguards is the only way to turn it off.

You can enforce Anthropic Human Review settings across your new workspaces by [setting a workspace policy](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#set-organization-defaults) on your organization’s [Data retention](https://platform.claude.com/settings/privacy) page.

For more, see [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console), [Turn on EFS on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#turn-on-efs-for-a-workspace), or [Turn on EFS on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#turn-on-efs-for-a-workspace).

## Check Access Transparency

Access Transparency gives you a record whenever someone at Anthropic views your data. These records come through as `anthropic_access` events in your Compliance API Activity Feed. For the boundaries of what’s recorded, see [what Access Transparency covers](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-covers).

For Claude Platform customers using Enterprise Frontier Safeguards or Enterprise Data Controls, Access Transparency turns on for your entire organization the first time you start connecting a bucket, attach a customer-managed key, or turn off Anthropic Human Review. Once it turns on, it starts recording within 2 hours.

The Compliance API must be on for you to read these events.

If you turn the Compliance API off, Anthropic keeps recording Access Transparency events, and you can read them once you turn it back on. Your organization’s other activity isn’t recorded while it’s off and can’t be recovered later.

To read your Access Transparency events, you need a key that can read the Activity Feed. If you use Claude Platform on AWS, skip to [On Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency-on-aws).

<Steps>
  <Step title="Create a key">
    [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access) and create a Compliance Access Key or an Admin API key that can read the Activity Feed.
  </Step>

  <Step title="Read anthropic_access events">
    Read `anthropic_access` events from your [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed).
  </Step>
</Steps>

On Claude Platform, an empty result says nothing about data in customer-owned storage, because there’s currently no Access Transparency record for that data. For what AWS CloudTrail in your AWS account records about your bucket, see [Anthropic’s calls in AWS CloudTrail](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#cloudtrail).

Here’s how to read the result:

* **No `anthropic_access` events:** Your Activity Feed shows no access to your data by Anthropic personnel, for everything [Access Transparency covers](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-covers). An event can arrive up to 2 business days after the access it records.
* **An `anthropic_access` event:** Someone at Anthropic viewed your data. Look up its reason in the [reason codes](https://platform.claude.com/docs/en/manage-claude/access-transparency#reason-codes).

To verify the events themselves, see [Verify Access Transparency events with the transparency log](https://platform.claude.com/docs/en/manage-claude/access-transparency-log).

### On Claude Platform on AWS

On Claude Platform on AWS, you [sign each request with your AWS credentials](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#sig-v4-authentication) instead of using a Compliance API key. To read your Activity Feed, send a `GET` request over HTTPS with these parts:

* **Host:** `aws-external-anthropic.{region}.api.aws`, where `{region}` is the region of one of your workspaces.
* **Path:** `/v1/compliance/activities`.
* **Header:** `anthropic-version: 2023-06-01`.
* **Filter (optional):** `activity_types%5B%5D=anthropic_access` in the query string, to get only Access Transparency events. Keep the brackets encoded, or the signature won’t match.

Your IAM principal needs the `aws-external-anthropic:ListComplianceActivities` action.

Here’s how to read the response:

* **A list, even an empty one:** The Compliance API is on. An event can take up to 2 business days to appear.
* **An `anthropic_access` event:** Someone at Anthropic viewed your data. The [reason codes](https://platform.claude.com/docs/en/manage-claude/access-transparency#reason-codes) explain why.
* **A 400 error, `Compliance API is not enabled for this organization`:** The Compliance API is off. Turn it on with the **Compliance API** toggle, wait about 1 minute, then send the Activity Feed request again.

To turn on the Compliance API, use the **Compliance API** toggle on the [Compliance](https://platform.claude.com/settings/security) page in the Claude Console. Your IAM principal needs the `aws-external-anthropic:UpdateComplianceSettings` action on `Resource: "*"`. The `AnthropicFullAccess` policy includes this action.

## Next steps

<CardGroup cols={2}>
  <Card title="Review Safety Cases" icon="file" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases">
    Review what automated safety monitoring finds, with your own team.
  </Card>

  <Card title="Check your setup" icon="check" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#check-your-setup">
    On Claude Platform, check that Sealed Safety Data reaches your bucket before you start production use.
  </Card>
</CardGroup>

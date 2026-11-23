---
title: Set up Enterprise Frontier Safeguards on Claude Platform
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console
description: Turn on Enterprise Frontier Safeguards for a Claude Platform workspace and choose its storage and key.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

You set up [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS) in the Claude Console. EFS applies to every request to every model in a [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) where you turn it on. To decide which workspaces should use it, see [Plan your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#plan-your-setup).

Setup has five parts:

1. Get access.
2. Add cloud resources: your storage buckets and encryption keys.
3. Turn on EFS for a workspace.
4. Optionally, set a policy for new workspaces.
5. Check your setup.

## Plan your setup

Plan your setup first, because you can’t undo some of the choices.

First, decide which [workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces) use Enterprise Frontier Safeguards. On Claude Platform, EFS covers [every request to every model in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview#workspace-scope). To use EFS for only some traffic, use separate workspaces. The Default Workspace can’t use EFS.

If your organization has a Legacy Zero Data Retention (ZDR) arrangement, use a new workspace for EFS, and select the **Enterprise Frontier Safeguards** card as you create it. In the Claude Console, you can’t select that card for an existing workspace on **Legacy ZDR**.

Then, check which steps you can undo and what else each step changes. Only a [customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys) is optional.

| Step | Can you undo it? | What else it changes |
| ----- | ----- | ----- |
| Get access for an organization | Not by yourself. You can’t turn off [Access Transparency](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency) once it’s on. To remove your organization’s access, contact your Anthropic account team. | Turns on the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) for your organization (see [Accept the terms](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access)). On Claude Platform, [Access Transparency](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency) also turns on once you configure your workspace. Getting access doesn’t turn EFS on for any workspace. |
| [Attach a customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key) | No. It’s permanent. | Turns off some features. See [what changes with a key](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed). |
| Use [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage) | Partly. You can [change or stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket), but stopping takes the workspace off EFS. | Needs Anthropic [Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off, so people at your organization must review [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#where-cases-arrive). Plan to use the bucket with [one Anthropic organization only](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#before-you-begin). |

Finally, answer these questions:

<AccordionGroup>
  <Accordion title="Where should my bucket be, and what does it cost?">
    Choose the cloud account and region for your bucket before you start:

    * **Amazon S3:** See [Create and connect your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles) and the [supported AWS regions](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket). Anthropic recommends `us-east-2`.
    * **Google Cloud Storage:** See [what the bucket and its project need](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-before-you-begin) and the [supported regions](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#supported-regions).

    If your AWS organization blocks outside accounts with resource control policies (RCPs), ask early for [an exception for Anthropic’s AWS account](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic).

    Anthropic doesn’t charge for EFS, but your cloud provider bills you for storage, reads, writes, and key operations, plus any applicable network transfer. Anthropic reads and writes your bucket from its own regions, which can affect your network transfer costs.
  </Accordion>

  <Accordion title="Who on my team needs to be involved?">
    To set up EFS and review Safety Cases afterward, you need these people:

    | Who | What they do |
    | ----- | ----- |
    | A cloud admin | Runs a setup file from the Claude Console that creates the bucket and a key and gives Anthropic access, for [Amazon S3](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles) or [Google Cloud Storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket). |
    | An Organization Admin | In the Claude Console, connects the bucket, turns on EFS for each workspace, and attaches any key. |
    | Your reviewers | [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). |
  </Accordion>
</AccordionGroup>

## Before you begin

To set up Enterprise Frontier Safeguards, you need the following:

* The Organization Admin role in the Claude Console.

## 1. Get access

To get access on Claude Platform, an Organization Admin accepts the terms for your organization. Accepting the terms also enables an Organization Admin to turn off Anthropic Human Review. If your Anthropic account team has already given your organization access, skip this section.

<Warning>
  Accepting the terms turns on the Compliance API for your organization, and for any other eligible organization linked to your [Verification Portal](https://portal.anthropic.com) profile.
</Warning>

### What getting access changes

Only eligible organizations can get Enterprise Frontier Safeguards. To request access, contact your Anthropic account team. If you don’t have an account team, complete the [Enterprise Frontier Safeguards request form](https://claude.com/form/enterprise-frontier-safeguards). EFS is currently available for your organization’s internal use only. If your organization has [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness) turned on, it can’t get EFS. You can’t combine EFS with some Anthropic access programs, so tell your Anthropic account team which programs your organizations use.

Accepting the terms changes more than the workspaces you plan to use. Read these main changes before you accept:

<AccordionGroup>
  <Accordion title="You can’t turn off Access Transparency once it’s on">
    [Access Transparency](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#check-access-transparency) records Anthropic personnel access to [the data that it covers](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-covers). When it turns on depends on where you use Claude:

    * On Claude Platform, it turns on the first time you start connecting a bucket, attach a customer-managed key, or turn off Anthropic Human Review. If a workspace already has a key, a bucket, or Anthropic Human Review off, Access Transparency turns on when you get access.
    * On Claude Models on Google Cloud (Anthropic managed) or Claude Platform on AWS, it turns on when you get access.

    Once it’s on, it’s on for every workspace in the organization. If another Claude Console organization under the same [parent organization](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need) has Access Transparency, now or later, you can’t turn it off in that organization either. An organization linked to your Verification Portal profile, now or later, can also get Access Transparency. To find out which of your organizations have Access Transparency, ask your Anthropic account team.
  </Accordion>

  <Accordion title="The Compliance API turns on and starts recording activity">
    If any of those organizations has a [parent organization](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need), this happens in every organization under that parent, even if someone had turned the Compliance API off. Where people sign in to apps such as Claude Code and Cowork with a Claude subscription plan, the Compliance API also stores session transcripts.
  </Accordion>

  <Accordion title="Anthropic can copy data to your storage">
    Getting access also means that workspaces that are configured to retain data, either in Anthropic-managed storage or in your own bucket, may keep copies of your API requests and responses. Your team can read a copy only if you connect **Safety Case and Transcript storage** or if Anthropic [flags it for your review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). Reconfiguring workspace or organization settings later doesn’t remove copies already kept.
  </Accordion>
</AccordionGroup>

### Accept the terms

To accept the terms, go to the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console and click **Accept terms** on the **Enterprise Frontier Safeguards** card. If you don’t see **Accept terms** there, sign in to the [Verification Portal](https://portal.anthropic.com), select your organization, and click **Accept terms**.

Ask your Anthropic account team for access if you can’t sign in to the Verification Portal or don’t see **Accept terms** there either. If you don’t have an account team, complete the [Enterprise Frontier Safeguards request form](https://claude.com/form/enterprise-frontier-safeguards).

If your organization has access, the [Programs](https://platform.claude.com/settings/programs) page shows **Enterprise Frontier Safeguards** with a **Configure** button.

## 2. Add cloud resources

To use Enterprise Frontier Safeguards, you need your own bucket. Your own encryption key is optional. Without one, a workspace uses an Anthropic-managed key. To add your bucket and key, go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and select **Organization** at the top of the page.

To use your own key, create a [customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys) in your own key management service, then register it with Anthropic under **Encryption keys**.

To set up your bucket for [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage), follow the steps for your cloud provider:

* **Amazon S3:** Follow [Set up customer-owned storage on Amazon S3](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#amazon-s3) to the end of [Create and connect your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles).
* **Google Cloud Storage:** Follow [Set up customer-owned storage on Google Cloud Storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#google-cloud-storage) to the end of [Create and test the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket).

Workspaces can use your bucket once **Test setup** passes.

## 3. Turn on EFS for a workspace

To turn on Enterprise Frontier Safeguards for a workspace, go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console. Select **Enterprise Frontier Safeguards** for the workspace first, then your storage, then your own key if you want one, and save.

With EFS, Anthropic Human Review is always off, so your organization is responsible for reviewing any [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) that Anthropic sends you. When you save, the Claude Console turns [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off for the workspace.

Decide who on your team reviews Safety Cases. To learn how Safety Cases reach your team, see [Get Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#prepare).

<Steps>
  <Step title="Select Enterprise Frontier Safeguards">
    If your organization has a Legacy Zero Data Retention (ZDR) arrangement, you will need to create a new workspace to use EFS. The Claude Console marks the **Enterprise Frontier Safeguards** card **Ineligible** for an existing workspace on **Legacy ZDR**. To use EFS, select the card as you create a new workspace. Keep your traffic on the old workspace until you finish [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#check-your-setup).

    To select the card as you create a workspace, first read the rest of this part. Then, create the workspace on the [Workspaces](https://platform.claude.com/settings/workspaces) page and select **Enterprise Frontier Safeguards**, your storage, and your key if you use one. Then, go to [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#check-your-setup).

    If you can’t select your bucket as you create the workspace, check that it passed **Test setup**. If that doesn’t help, or the Claude Console doesn’t finish creating the workspace, contact your Anthropic account team.

    To select the card for a workspace that you already have, switch from **Organization** to the workspace at the top of the [Data retention](https://platform.claude.com/settings/privacy) page. You can’t select **Enterprise Frontier Safeguards** for the Default Workspace, which always follows your organization’s data retention setting.

    Then, select the **Enterprise Frontier Safeguards** card.
  </Step>

  <Step title="Select your storage">
    <Warning>
      Until [your bucket selection takes effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take), Sealed Safety Data might go to Anthropic-managed storage, even from a new workspace, and even if your organization has a Legacy ZDR arrangement. Send only test requests with no sensitive data to this workspace until 10 minutes after the first new object arrives under `slab/` or `safeguards-data/slab/` in your bucket.
    </Warning>

    Select your bucket under **Sealed Safety Data storage**. The Claude Console can’t create a workspace with **Enterprise Frontier Safeguards** without one. Optionally, select it under **Safety Case and Transcript storage** too, now or later. A workspace has two storage settings:

    * **Sealed Safety Data storage:** Sets where Anthropic sends [Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored): prompts, responses, and model reasoning, encrypted in Anthropic’s format. Your team can’t read Sealed Safety Data, even in your own bucket.
    * **Safety Case and Transcript storage:** Sets where Anthropic sends Transcripts and Safety Cases for your team to read. To receive them in your bucket, see [Transcripts and Safety Cases in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket).

    If you leave **Safety Case and Transcript storage** at **Not copied to your storage**, your team gets Safety Cases only if your organization has [access to the Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#get-access).

    Once a workspace uses your bucket, the bucket is tied to this organization. Treat the tie as permanent. For a Google Cloud Storage bucket, also read [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace) before you save.

    <Warning>
      Check that the Compliance API is on before you send requests, and keep it on. Requests that you send while it’s off have no Transcript, so your team can’t review them later. To find the setting, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api).
    </Warning>
  </Step>

  <Step title="Attach a customer-managed key">
    To encrypt your data with your own key, select the key under **Encryption key**. You can select a key once you’ve [created and registered it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key). Attaching a key is permanent, so read the [limitations of customer-managed keys](https://platform.claude.com/docs/en/manage-claude/cmek#what-you-commit-to) before you save.

    On a workspace that already serves traffic, the key can take up to a day to take effect after you save.

    A key also turns off some features. See [what changes with a key](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed).
  </Step>
</Steps>

## 4. Set a policy for new workspaces

Optionally, you can set an organization-wide policy so that new workspaces use EFS controls. With a policy, you select the settings for new workspaces. You can require that [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) is on or off (under **Who reviews flagged cases?**), require customer-owned storage or a customer-managed key, or name a specific bucket or key.

[Register a key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#add-cloud-resources) or [add a bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage) before you require them, or no one can create a workspace that keeps Sealed Safety Data.

To set or change the policy, select **Organization** at the top of the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and find **Policy for new workspaces**.

The policy applies to new workspaces and doesn’t change workspaces that already exist. To change an existing workspace, see [Turn on EFS for a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#turn-on-efs-for-a-workspace). If a request to create or change a workspace breaks the policy, Anthropic refuses it.

## 5. Check your setup

Send test requests with no sensitive data to the workspace. New objects appear under `slab/` or `safeguards-data/slab/` in the bucket that you selected under **Sealed Safety Data storage**, once [your bucket selection takes effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take). Wait 10 minutes after the first new object before you send real traffic. If another workspace already sends data to this bucket, new objects don’t show that this change took effect, so ask your Anthropic account team before you send real traffic.

## Check who reaches your bucket and key

To see who reaches your Amazon S3 bucket and your customer-managed key, check your own logs. If you find another caller, contact your Anthropic account team.

* **Amazon S3 bucket:** Open **Event history** in AWS CloudTrail in `us-east-2`, even if your bucket is in another region. Every `AssumeRole` call into the IAM roles that your setup created should come from the Anthropic AWS account that your setup file named. The Claude Console’s setup files name account `804820989669`. To log reads, writes, and deletes of objects too, see [Anthropic’s calls in AWS CloudTrail](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#cloudtrail).
* **Customer-managed key:** Once [your key takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), your key’s audit log shows calls from Anthropic, but not one for each request. Every call outside your team should come from the identity that [the setup page for your key’s service](https://platform.claude.com/docs/en/manage-claude/cmek#set-it-up) names. In AWS CloudTrail, that identity shows `userIdentity.accountId` `915198916910` and a `userIdentity.principalId` that ends in `:anthropic-cmek`.

## Next steps

<CardGroup cols={2}>
  <Card title="Review Safety Cases" icon="file" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases">
    Receive, investigate, and respond to the Safety Cases that Anthropic sends.
  </Card>

  <Card title="If your key stops working" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#if-your-key-stops-working">
    What happens to requests, and what to do.
  </Card>

  <Card title="If your bucket stops working" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working">
    What happens to your data, and how to recover.
  </Card>

  <Card title="Change or stop using your bucket" icon="sliders" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket">
    Move to a new bucket or take a workspace off EFS.
  </Card>
</CardGroup>

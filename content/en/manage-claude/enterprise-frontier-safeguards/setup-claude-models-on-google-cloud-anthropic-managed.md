---
title: Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed
description: Turn on Enterprise Frontier Safeguards for a workspace on Claude Models on Google Cloud (Anthropic managed), and choose its storage and key.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

To set up [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS), open the Claude Console from the Google Cloud console. EFS applies to every request to every model in a workspace where you turn it on. To decide which workspaces should use it, see [Plan your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#plan-your-setup).

Setup has three parts:

1. Add cloud resources: your storage bucket and encryption key.
2. Turn on EFS for a workspace.
3. Check your setup.

## Plan your setup

Plan your setup first, because you can’t undo some of the choices.

First, decide which [workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces) use Enterprise Frontier Safeguards. To use EFS for only some traffic, use separate workspaces. The Default Workspace can’t use EFS.

If your organization has a Legacy Zero Data Retention (ZDR) arrangement, use a new workspace for EFS, and select the **Enterprise Frontier Safeguards** card as you create it. In the Claude Console, you can’t select that card for an existing workspace on **Legacy ZDR**.

Finally, answer these questions:

<AccordionGroup>
  <Accordion title="Where should my bucket be, and what does it cost?">
    Choose the cloud account and region for your bucket before you start:

    * **Google Cloud Storage:** See [what the bucket and its project need](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-before-you-begin) and the [supported regions](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#supported-regions).

    Anthropic doesn’t charge for EFS, but your cloud provider bills you for storage, reads, writes, and key operations, plus any applicable network transfer. Anthropic reads and writes your bucket from its own regions, which can affect your network transfer costs.
  </Accordion>

  <Accordion title="Who on my team needs to be involved?">
    To set up EFS and review Safety Cases afterward, you need these people:

    | Who | What they do |
    | ----- | ----- |
    | A cloud admin | Runs a setup file from the Claude Console that creates the bucket and a key and gives Anthropic access, for [Google Cloud Storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket). |
    | An Organization Admin | In the Claude Console, connects the bucket, turns on EFS for each workspace, and attaches any key. |
    | Your reviewers | [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). |
  </Accordion>
</AccordionGroup>

## Before you begin

To set up Enterprise Frontier Safeguards, you need the following:

* [`roles/claude.admin`](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#using-the-claude-console) on the Google Cloud project whose organization will use EFS.
* [Access to EFS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#what-getting-access-changes) for your organization, from your Anthropic account team. Getting access can change settings that you can’t change back.
* To use your own key: [customer-managed keys turned on](https://platform.claude.com/docs/en/manage-claude/cmek#availability) for your organization.

## What getting access changes

<Warning>
  Accepting the terms turns on the Compliance API for your organization, and for any other eligible organization linked to your [Verification Portal](https://portal.anthropic.com) profile.
</Warning>

Accepting the terms also enables an Organization Admin to turn off Anthropic Human Review. If your Anthropic account team has already given your organization access, skip this section.

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

## 1. Add cloud resources

To open the Claude Console, go to [Claude Platform](https://console.cloud.google.com/agent-platform/claude-platform) in the Google Cloud console and select your project. Then, select **Anthropic managed** and click **Open Claude Console**. Do this before you follow links on this page to the Claude Console. Each link opens in the Anthropic organization that your browser is signed in to. To check which organization you’re in, go to **Settings** > **Organization**. **Google Cloud project number** must show your project’s number, not its ID. If the page has no such row, you’re probably in another organization.

To use EFS, you need your own bucket. Your own encryption key is optional. Without one, a workspace uses an Anthropic-managed key. To add your bucket and key, go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and select **Organization** at the top of the page.

To use your own key, create a [customer-managed key](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms) in Google Cloud KMS, then register it with Anthropic under **Encryption keys**. Follow the **Claude Platform** tab and stop before **Attach the key to a workspace**. Use a different key from your bucket’s own key, which you create with the bucket.

To set up your bucket for customer-owned storage, use a new bucket for this organization alone. If this organization already has a bucket, you can use that one. Follow [Set up customer-owned storage on Google Cloud Storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#google-cloud-storage) to the end of [Create and test the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#gcs-create-the-bucket).

Cloud Audit Logs doesn’t record some changes that you make on the Data retention page. These are changes to storage destinations, the policy for new workspaces, and a workspace’s storage, key, or Anthropic Human Review.

## 2. Turn on EFS for a workspace

To turn on Enterprise Frontier Safeguards, create a workspace. Then, select the **Enterprise Frontier Safeguards** card and your storage, add your own key if you use one, and save once.

<Steps>
  <Step title="Create a workspace">
    Create a new workspace for EFS on the [Workspaces](https://platform.claude.com/settings/workspaces) page, even if you already have workspaces. The Default Workspace can’t use EFS.

    * **If you can select an Enterprise Frontier Safeguards card:** You can turn on EFS as you create the workspace. First, read the rest of this part. Then, select the card, your bucket under both storage settings, and your key if you use one. Create the workspace and go to [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#check-your-setup).
    * **Otherwise, if your organization has a Legacy Zero Data Retention (ZDR) arrangement:** Don’t create the workspace. Check that your bucket passed **Test setup**. If it did, contact your Anthropic account team.
    * **Otherwise:** Create the workspace and continue with the next step.

    Don’t send requests to the workspace until you reach [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#check-your-setup).
  </Step>

  <Step title="Select Enterprise Frontier Safeguards">
    Go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console. At the top of the page, switch from **Organization** to the workspace that you created for EFS. Then, select the **Enterprise Frontier Safeguards** card. Stay on this page for the remaining steps, and don’t save until the last one.

    If you can’t select the card, check that your bucket passed **Test setup**. If it did, contact your Anthropic account team.
  </Step>

  <Step title="Select your storage">
    Select your bucket under **Sealed Safety Data storage**. Then, select the same bucket under **Safety Case and Transcript storage**. If you don’t select a bucket under **Safety Case and Transcript storage**, your save fails.

    <Warning>
      Once a workspace uses your bucket, the bucket is tied to this organization, and you can’t delete its storage destination. Treat the tie as permanent.
    </Warning>

    Before you save, read [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#gcs-use-your-bucket-in-a-workspace).

    To move to another bucket, ask your Anthropic account team first.

    If the Claude Console doesn’t show **Safety Case and Transcript storage**, contact your Anthropic account team before you save. If it refuses your bucket, contact them before you connect another bucket. After you save a bucket under **Safety Case and Transcript storage**, you can’t clear that setting while the workspace is on EFS.

    <Warning>
      Check that the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) is on before you send requests, and keep it on. Requests that you send while it’s off might not have a Transcript, even after you turn it on. In another tab, find the **Compliance API** toggle on the [Compliance](https://platform.claude.com/settings/security) page.
    </Warning>
  </Step>

  <Step title="Attach a customer-managed key">
    To encrypt your data with your own key, select the key under **Encryption key**. Attaching a key is permanent, so read the [limitations of customer-managed keys](https://platform.claude.com/docs/en/manage-claude/cmek#what-you-commit-to) before you save or create the workspace.
  </Step>

  <Step title="Save">
    When you save or create the workspace with your bucket, the Claude Console turns [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off for the workspace. With EFS, Anthropic Human Review is always off. Once the change takes effect, [a small, specialized team at Anthropic](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#who-at-anthropic-can-access-your-data) no longer reviews the workspace’s new prompts and responses. From then on, reviewing [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) is your team’s job. [Monitor your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#set-up-alerts), because the 7 days to respond start when Anthropic sends a Safety Case.
  </Step>
</Steps>

## 3. Check your setup

<Warning>
  Until [your bucket selection takes effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#confirm-that-objects-arrive), Sealed Safety Data might go to Anthropic-managed storage, even if your organization has a Legacy Zero Data Retention (ZDR) arrangement. Until then, send only test requests with no sensitive data to this workspace.
</Warning>

Send test requests to the workspace. Use the [new workspace’s ID](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#find-your-workspace-id) in these requests, and in every later request that EFS should cover. Then, [confirm that objects arrive](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#confirm-that-objects-arrive) in your bucket. These objects are Sealed Safety Data and don’t show that Transcripts or Safety Cases arrive.

Send nothing but test requests until 10 minutes after the first new object arrives under `safeguards-data/slab/` in your organization’s folder of the bucket. Keep your traffic on your existing workspaces until then. If another workspace already sends data to this bucket, new objects don’t show that this change took effect. In that case, ask your Anthropic account team before you send real traffic.

On the [Workspaces](https://platform.claude.com/settings/workspaces) page, select the workspace and check that **Cases, transcripts** under **Data retention** shows your bucket. If it’s missing or shows anything else, contact your Anthropic account team before you send real traffic.

## Next steps

<CardGroup cols={2}>
  <Card title="If your key stops working" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#if-your-key-stops-working">
    What happens to requests, and what to do.
  </Card>

  <Card title="If your bucket stops working" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#gcs-if-your-bucket-stops-working">
    What happens to your data, and how to restore your bucket.
  </Card>

  <Card title="Stop using your bucket" icon="sliders" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=gcp#gcs-stop-using-your-bucket">
    Keep your data when you stop using your bucket.
  </Card>
</CardGroup>

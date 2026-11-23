---
title: Set up Enterprise Frontier Safeguards on Claude Platform on AWS
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws
description: Turn on Enterprise Frontier Safeguards for a Claude Platform on AWS workspace and choose its storage and key.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

You set up [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS) in the Claude Console, which you open from the AWS Console. EFS applies to every request to every model in a workspace where you turn it on. To decide which workspaces should use it, see [Plan your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#plan-your-setup).

Setup has three parts:

1. Add cloud resources: your storage buckets and encryption keys.
2. Turn on EFS for a workspace.
3. Check your setup.

## Plan your setup

Plan your setup first, because you can’t undo some of the choices.

First, decide which [workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces) use Enterprise Frontier Safeguards. To use EFS for only some traffic, use separate workspaces. The Default Workspace can’t use EFS.

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

    If your AWS organization blocks outside accounts with resource control policies (RCPs), ask early for [an exception for Anthropic’s AWS account](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic).

    Anthropic doesn’t charge for EFS, but your cloud provider bills you for storage, reads, writes, and key operations, plus any applicable network transfer. Anthropic reads and writes your bucket from its own regions, which can affect your network transfer costs.
  </Accordion>

  <Accordion title="Who on my team needs to be involved?">
    To set up EFS and review Safety Cases afterward, you need these people:

    | Who | What they do |
    | ----- | ----- |
    | A cloud admin | Runs a setup file from the Claude Console that creates the bucket and a key and gives Anthropic access, for [Amazon S3](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles). |
    | An Organization Admin | In the Claude Console, connects the bucket, turns on EFS for each workspace, and attaches any key. |
    | Your reviewers | [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases). |
  </Accordion>
</AccordionGroup>

## Before you begin

To set up Enterprise Frontier Safeguards, you need the following:

* The Admin role in the Claude Console. To get the role, go to the **Claude Platform on AWS** service page in the AWS Console, select **Admin**, and click **Sign in**. Sign in this way before you follow links on this page to the Claude Console. Each link opens in the Anthropic organization that your browser is signed in to.
* [Access to EFS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#what-getting-access-changes) for your organization, from your Anthropic account team.
* [IAM permissions](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#iam-permissions) for your IAM principal.

Use a new workspace for EFS, even if you already have workspaces. Anthropic recommends that you set its **AWS region** to `us-east-2` to avoid network transfer costs, but it isn’t required. You can’t change the region later.

If your organization has a Legacy Zero Data Retention (ZDR) arrangement, follow these steps:

1. [Add your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#add-cloud-resources), check that it passes **Test setup**, and then come back to this list.
2. Read [Turn on EFS for a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#turn-on-efs-for-a-workspace).
3. Create the workspace on the [Workspaces](https://platform.claude.com/settings/workspaces) page. As you create it, select the **Enterprise Frontier Safeguards** card and your bucket under both storage settings. If you can’t select the card or your bucket, or the Claude Console doesn’t finish creating the workspace, contact your Anthropic account team.
4. To use your own key, [create and register it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#add-cloud-resources), and attach it on the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page.
5. Go to [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#check-your-setup).

Otherwise, before you start, create the workspace on the [Workspaces](https://platform.claude.com/settings/workspaces) page, and don’t select the **Enterprise Frontier Safeguards** card. That card needs your bucket, which you add after you create the workspace. Don’t send requests to the workspace until you [turn on EFS for it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#turn-on-efs-for-a-workspace).

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

### Accept the terms

To accept the terms, go to the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console and click **Accept terms** on the **Enterprise Frontier Safeguards** card. If you don’t see **Accept terms** there, sign in to the [Verification Portal](https://portal.anthropic.com), select your organization, and click **Accept terms**.

Ask your Anthropic account team for access if you can’t sign in to the Verification Portal or don’t see **Accept terms** there either. If you don’t have an account team, complete the [Enterprise Frontier Safeguards request form](https://claude.com/form/enterprise-frontier-safeguards).

## 1. Add cloud resources

To use Enterprise Frontier Safeguards, you need your own bucket. Your own encryption key is optional. Without one, a workspace uses an Anthropic-managed key. To add your bucket and key, go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and select **Organization** at the top of the page.

To use your own key, create a [customer-managed key](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws) in AWS KMS, in the workspace’s region, then register it with Anthropic under **Encryption keys**. The linked guide’s sample key policy needs the workspace’s compartment ID, so create the workspace first.

To set up your bucket for [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=aws), read [what the bucket and its AWS account need](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=aws#before-you-begin), then [create and connect your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=aws#create-the-bucket-and-roles). In the Claude Console, the **Connect storage** dialog fills in **AWS account ID** with the ID of the AWS account where you signed up. To create your bucket in a different AWS account, change the ID. Workspaces can use your bucket once **Test setup** passes.

## 2. Turn on EFS for a workspace

To turn on Enterprise Frontier Safeguards for a workspace, go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console. For the workspace, select **Enterprise Frontier Safeguards** and your storage, add your own key if you want one, and save once.

<Steps>
  <Step title="Select Enterprise Frontier Safeguards">
    If your organization has a Legacy Zero Data Retention (ZDR) arrangement, you will need to create a new workspace to use EFS. The Claude Console marks the **Enterprise Frontier Safeguards** card **Ineligible** for an existing workspace on **Legacy ZDR**. To use EFS, select the card as you create the workspace, as [Before you begin](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#before-you-begin) describes. Keep your traffic on your existing workspaces until you finish [Check your setup](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#check-your-setup).

    Otherwise, at the top of the page, switch from **Organization** to the workspace that you created for EFS. Then, select the **Enterprise Frontier Safeguards** card.

    If the Claude Console marks the card **Ineligible**, the badge’s tooltip says why and what to do. If the Claude Console hides the card, contact your Anthropic account team.

    Stay on this page for the remaining steps, and don’t save until the last one.
  </Step>

  <Step title="Select your storage">
    <Warning>
      Until [your bucket selection takes effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=aws#how-long-changes-take), Sealed Safety Data might go to Anthropic-managed storage, even from a new workspace, and even if your organization has a Legacy ZDR arrangement. Send only test requests with no sensitive data to this workspace until 10 minutes after the first new object arrives under `slab/` or `safeguards-data/slab/` in your bucket.
    </Warning>

    Select your bucket under both of the workspace’s storage settings:

    * **Sealed Safety Data storage:** Sets where Anthropic sends [Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage?cloud=aws#what-is-stored): prompts, responses, and model reasoning, encrypted in Anthropic’s format. Your team can’t read Sealed Safety Data, even in your own bucket.
    * **Safety Case and Transcript storage:** Sets where Anthropic sends Transcripts and [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) for your team to read.

    Select your bucket under **Safety Case and Transcript storage** even if the Claude Console marks that setting as optional. EFS requires a bucket there. If you leave that setting empty, your save might fail or leave Anthropic Human Review on.

    Keep these points in mind when you select your bucket:

    * If the Claude Console doesn’t show **Safety Case and Transcript storage**, contact your Anthropic account team before you save. If the Claude Console refuses your bucket, contact your Anthropic account team before you connect another bucket.
    * After you save a bucket under **Safety Case and Transcript storage**, you can’t clear that setting while the workspace is on EFS. To [move to another bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-your-bucket), ask your Anthropic account team first.
    * If your bucket stops working, tell your Anthropic account team as soon as you notice. Anthropic can’t write data to your bucket during the failure. About 1 day after that data was sent, Anthropic deletes whatever it hasn’t recovered. See [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).

    Once a workspace uses your bucket, the bucket is tied to this organization, and you can’t delete its storage destination. Treat the tie as permanent.

    <Warning>
      Check that the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) is on before you send requests, and keep it on. Requests that you send while it’s off might not have a Transcript, even after you turn it on. In another tab, find the **Compliance API** toggle on the [Compliance](https://platform.claude.com/settings/security) page.
    </Warning>
  </Step>

  <Step title="Attach a customer-managed key">
    To encrypt your data with your own key, select the key under **Encryption key**. You can select a key once you’ve [created and registered it](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws). Attaching a key is permanent, so read the [limitations of customer-managed keys](https://platform.claude.com/docs/en/manage-claude/cmek#what-you-commit-to) before you save.

    A key also turns off some features. See [what changes with a key](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed).
  </Step>

  <Step title="Save">
    When you save, the Claude Console turns [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off for the workspace. With EFS, Anthropic Human Review is always off. Once the change takes effect, [a small, specialized team at Anthropic](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#who-at-anthropic-can-access-your-data) no longer reviews the workspace’s new prompts and responses. From then on, reviewing [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) is your team’s job.
  </Step>
</Steps>

## 3. Check your setup

Send test requests with no sensitive data to the workspace. New objects appear under `slab/` or `safeguards-data/slab/` in the bucket that you selected under **Sealed Safety Data storage**, once [your bucket selection takes effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?cloud=aws#how-long-changes-take). Wait 10 minutes after the first new object before you send real traffic. If another workspace already sends data to this bucket, new objects don’t show that this change took effect, so ask your Anthropic account team before you send real traffic.

On the [Workspaces](https://platform.claude.com/settings/workspaces) page, select the workspace and check that **Cases, transcripts** under **Data retention** shows the bucket that you selected under **Safety Case and Transcript storage**. If it’s missing or shows another bucket, contact your Anthropic account team before you send real traffic. If it reads **Not copied to your storage**, select your bucket under **Safety Case and Transcript storage** on the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page, and click **Save**.

## Check who reaches your bucket and key

To see who reaches your Amazon S3 bucket and your customer-managed key, check your own logs. If you find another caller, contact your Anthropic account team.

* **Amazon S3 bucket:** Open **Event history** in AWS CloudTrail in `us-east-2`, even if your bucket is in another region. Every `AssumeRole` call into the IAM roles that your setup created should come from the Anthropic AWS account that your setup file named. The Claude Console’s setup files name account `804820989669`. To log reads, writes, and deletes of objects too, see [Anthropic’s calls in AWS CloudTrail](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage?cloud=aws#cloudtrail).
* **Customer-managed key:** Once [your key takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), CloudTrail shows `Encrypt` or `Decrypt` calls on your key, but not one for each request. Every call outside your team should show `userIdentity.invokedBy` `aws-external-anthropic.amazonaws.com`, the AWS service principal that your key policy allows.

## IAM permissions

The IAM principal that you sign in with needs permission to set up storage. The `AnthropicFullAccess` policy includes it. In a policy of your own, allow these `aws-external-anthropic` actions on `Resource: "*"`:

* `RegisterAccountExternalStorage`: Connect a storage destination.
* `ActivateAccountExternalStorage`: Run **Test setup**.
* `GetAccountExternalStorage`: View a storage destination.
* `ListAccountExternalStorages`: List your storage destinations.
* `UpdateAccountExternalStorage`: Change a storage destination’s display name.
* `DeregisterAccountExternalStorage`: Delete a storage destination. This doesn’t delete your S3 bucket.
* `GetAccountPrograms`: See what Anthropic has approved for your organization.
* `GetAccountWorkspacePolicy`: See your organization’s policy for new workspaces.
* `UpdateAccountWorkspacePolicy`: Change your organization’s policy for new workspaces.
* `UpdateComplianceSettings`: Change the Compliance API setting.

Allow these actions even if [IAM actions for Claude Platform on AWS](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions) doesn’t list them. That page lists the other actions that you need in parts 1 and 2:

* `AssumeConsole`
* `CreateWorkspace`
* `ListWorkspaces`
* `GetWorkspace`
* `UpdateWorkspace`
* `RegisterKey`
* `ListKeys`
* `GetKey`

Your IAM principal also needs two AWS STS actions: `sts:GetWebIdentityToken` and `sts:TagGetWebIdentityToken`. The `AnthropicFullAccess` policy includes both. If you use a policy of your own, grant both actions as shown in [IAM policies](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#iam-policies).

To attach a key, you also need the [KMS permissions for that key](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws#prerequisites).

## Next steps

<CardGroup cols={2}>
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

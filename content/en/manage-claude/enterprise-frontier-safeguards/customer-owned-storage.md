---
title: Customer-owned storage
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage
description: Keep data in a bucket in your own cloud account.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

<Where cloud="aws" label="Claude Platform on AWS">

With Enterprise Frontier Safeguards (EFS), you bring your own storage and store your own data, under your own access policies and audit logging. Anthropic deletes prompts and responses promptly after the relevant response has been generated and they are written to your bucket. You provide storage for:

</Where>

<Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">

Customer-owned storage keeps a workspace’s data in a bucket in your own cloud account, not in Anthropic-managed storage. Enterprise Frontier Safeguards (EFS) requires it for Sealed Safety Data. For Transcripts and Safety Cases, it’s required on [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed). Three categories of data can go into your bucket:

</Where>

<Where cloud="claude" label="Claude Platform">

Customer-owned storage keeps a workspace’s Sealed Safety Data and Transcripts in a bucket in your own cloud account, not in Anthropic-managed storage. Enterprise Frontier Safeguards (EFS) requires it for Sealed Safety Data. For Transcripts and Safety Cases, it’s optional on Claude Platform. Three categories of data can go into your bucket:

</Where>

* **[Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored):** Prompts, responses, and model reasoning, encrypted in Anthropic’s format.
* **Transcript:** A readable copy of a prompt and response, for your team to read.
* **Safety Correspondence:** Safety Cases, Safety Notices, and your Safety Case Responses. Never prompts and responses. Your team reviews Safety Cases as [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) describes.

<Where bucket="s3" label="Amazon S3">You create the Amazon S3 bucket, an encryption key, and roles in your own cloud account. The key encrypts the bucket, and the roles give Anthropic access to it.</Where> <Where bucket="gcs" label="Google Cloud Storage">You create the Google Cloud Storage bucket, an encryption key, custom roles, and grants to Anthropic’s accounts in your own cloud account. The key encrypts the bucket, and the grants give Anthropic access to it.</Where> <Where bucket="s3" label="Amazon S3">Your account’s logs record each time Anthropic assumes one of your roles (see [Anthropic’s calls in AWS CloudTrail](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#cloudtrail)).</Where> You can remove Anthropic’s access. For Sealed Safety Data, requests in the affected workspace may then be refused until access is restored. <Where bucket="s3" label="Amazon S3">To remove it, follow the steps in [Stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#stop-using-your-bucket) in order.</Where> <Where bucket="gcs" label="Google Cloud Storage">To remove it, follow the steps in [Stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-stop-using-your-bucket) in order.</Where>

Anthropic doesn’t charge for customer-owned storage, but your cloud provider bills you for storage, reads, writes, and key operations, plus any applicable network transfer.

<CardGroup cols={3}>
  <Where cloud="aws" label="Claude Platform on AWS">

  <Card title="Set up Enterprise Frontier Safeguards on Claude Platform on AWS" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws">
    Turn on Enterprise Frontier Safeguards for a workspace and choose its storage and key.
  </Card>

  </Where>

  <Where cloud="claude" label="Claude Platform">

  <Where bucket="s3" label="Amazon S3">

  <Card title="Set up customer-owned storage" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage">
    Create your bucket, its key, and its roles, then connect them in the Claude Console.
  </Card>

  </Where>

  <Where bucket="gcs" label="Google Cloud Storage">

  <Card title="Set up customer-owned storage on Google Cloud Storage" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#google-cloud-storage">
    Create your bucket, its key, and its roles, then connect them in the Claude Console.
  </Card>

  </Where>

  </Where>

  <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">

  <Card title="Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed">
    Turn on Enterprise Frontier Safeguards for a workspace and choose its storage and key.
  </Card>

  </Where>

  <Where bucket="s3" label="Amazon S3">

  <Card title="Manage customer-owned storage" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage">
    Check your bucket’s status, fix a bucket that stops working, and change or stop using it.
  </Card>

  </Where>

  <Where bucket="gcs" label="Google Cloud Storage">

  <Card title="If your bucket stops working" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-if-your-bucket-stops-working">
    Fix a bucket that stops working, or stop using it.
  </Card>

  </Where>

  <Where bucket="s3" label="Amazon S3">

  <Where cloud="claude" label="Claude Platform">

  <Card title="Set up customer-owned storage with the Admin API" icon="code" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api">
    Script the Claude Console’s part with the Admin API, where an External Storage is Anthropic’s record of your bucket.
  </Card>

  </Where>

  </Where>
</CardGroup>

## What’s stored, and where

The three data categories differ in who can read them and in what happens if Anthropic can’t write to your bucket. <Where cloud="claude" label="Claude Platform"><Where bucket="s3" label="Amazon S3">[Transcripts and Safety Cases in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket) says which buckets can receive Transcripts and Safety Cases.</Where> <Where bucket="gcs" label="Google Cloud Storage">[Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace) says how to select your bucket for Transcripts and Safety Cases.</Where></Where> <Where cloud="aws" label="Claude Platform on AWS">EFS requires your bucket for Transcripts and Safety Cases too.</Where> <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">EFS requires your bucket for Transcripts and Safety Cases too.</Where>

| Data category | Who can read it | If Anthropic can’t write to your bucket |
| ----- | ----- | ----- |
| Sealed Safety Data: prompts, responses, and model reasoning, encrypted in Anthropic’s format. | Your team can’t read it, even in storage you own. It’s for automated safety monitoring. For the detail, see [When does automated safety monitoring access your data?](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#who-at-anthropic-can-access-your-data) | <Where bucket="s3" label="Amazon S3">Requests to the workspace keep working during a [grace period of up to 24 hours](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working). After that, Anthropic might refuse them. Anthropic retries writes for a limited time and doesn’t send that data to Anthropic-managed storage instead. Tell your Anthropic account team as soon as you notice a failure, because Anthropic deletes data that hasn’t reached your bucket. On Claude Platform, it deletes that data about 72 hours after the request. On any other platform, it can do so as early as about a day after the request.</Where> <Where bucket="gcs" label="Google Cloud Storage">Requests to the workspace keep working during a grace period of up to 24 hours. After that, Anthropic might refuse them. Anthropic retries a failed write, then deletes the data about a day after the request. Nobody can recover that data, and it doesn’t go to Anthropic-managed storage. Tell your Anthropic account team as soon as you notice a failure. See [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-if-your-bucket-stops-working).</Where> |
| Transcripts of your prompts and responses. The Transcripts might include requests that never lead to a Safety Case, so plan who can read your bucket. | Your team. Anthropic writes them in a form your team can read. | <Where cloud="claude aws" label="Claude Platform or Claude Platform on AWS">A failure of this storage alone doesn’t block requests.</Where> You don’t receive Transcripts or Safety Cases there while Anthropic can’t write to it. |
| Safety Correspondence: Safety Cases, Safety Notices, and your Safety Case Responses. | Your team, and Anthropic (see the paragraph after this table). | The same as for Transcripts. |

Safety Cases, Safety Notices, and your Safety Case Responses (together, Safety Correspondence) never contain your prompts or responses. A Safety Case contains identifiers and details, such as status, timestamps, policy categories, any enforcement action taken, and references to the related Transcripts. <Where bucket="s3" label="Amazon S3">Anthropic can read Safety Cases and your Safety Case Responses in your bucket through [the review role](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-roles), but its identities can’t read your Transcripts or write or change your Safety Case Responses.</Where> <Where bucket="gcs" label="Google Cloud Storage">Anthropic can read Safety Cases and your Safety Case Responses in your bucket, but its identities can’t read your Transcripts or write or change your Safety Case Responses.</Where> Wherever your Safety Cases are delivered, Anthropic also keeps a record of Safety Correspondence, which authorized Anthropic personnel can read. That record doesn’t contain prompts or responses.

### The two storage settings

A workspace on the **Enterprise Frontier Safeguards** card has two storage settings:

* **Sealed Safety Data storage** sets where Anthropic sends Sealed Safety Data. It’s required, and it offers only your own storage.
* **Safety Case and Transcript storage** sets where Anthropic sends Transcripts and Safety Cases. <Where cloud="claude" label="Claude Platform">It’s optional. Without a bucket under it, your team gets Safety Cases only if your organization has [access to the Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#get-access). **Not copied to your storage** means that Anthropic doesn’t copy them to your storage. <Where bucket="s3" label="Amazon S3">If the bucket under **Sealed Safety Data storage** [can receive them](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket), you can select it too, when you first save or later.</Where> <Where bucket="gcs" label="Google Cloud Storage">If the Data retention page shows that setting, you can select the same bucket when you first save or later. See [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace).</Where></Where> <Where cloud="aws" label="Claude Platform on AWS">EFS requires it. See [Set up Enterprise Frontier Safeguards on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws). **Not copied to your storage** means that Anthropic doesn’t copy them to your storage.</Where> <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">EFS requires it. See [Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed). **Not copied to your storage** means that Anthropic doesn’t copy them to your storage.</Where>

Transcripts and Safety Cases go to the same bucket, and you can’t choose one without the other.

### How long Sealed Safety Data stays

<Where cloud="claude" label="Claude Platform">

Sealed Safety Data stays in your bucket for a limited number of days after you send the request. That time is the retention period, and it’s up to 28 days.

</Where>

<Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">

Sealed Safety Data stays in your bucket for a limited number of days after you send the request. That time is the retention period, and it’s up to 28 days.

</Where>

<Where cloud="aws" label="Claude Platform on AWS">

The retention period for Sealed Safety Data is up to 28 days after you send the request.

</Where>

<Where bucket="gcs" label="Google Cloud Storage">

Your bucket’s own lifecycle rules delete each object of Sealed Safety Data after it’s 28 days old and permanently remove it at least a day later.

</Where>

<Where bucket="s3" label="Amazon S3">

<Where cloud="claude" label="Claude Platform">

Anthropic deletes an object from your bucket once everything in it is past the retention period. You don’t set up any cleanup. [Old versions and some objects stay longer](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-removes-data).

</Where>

</Where>

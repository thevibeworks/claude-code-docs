---
title: Use a customer-managed key
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys
description: Encrypt your data using a key you hold in your own key management service.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

With a customer-managed key (CMEK), Anthropic encrypts your data using a key that you hold in your own key management service: AWS KMS, Google Cloud KMS, or Azure Key Vault. Within about an hour of [disabling your key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#revoke-your-key), Anthropic can no longer decrypt data your key protects.

In the Claude Console, you attach your key to each [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) that uses it, and get access through [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS) or [Enterprise Data Controls](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview#enterprise-data-controls).

## Before you attach a key

You need to be an Organization Admin to attach keys.

Your organization also needs access to customer-managed keys. To get access with EFS, follow the “Get access” section of [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access). To get access without EFS, contact your Anthropic account team, as [Who can use CMEK](https://platform.claude.com/docs/en/manage-claude/cmek#availability) describes.

Attaching your first key turns on [Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency#access-transparency-with-customer-managed-keys) for your whole organization, unless it’s already on. You can’t turn it off. With Access Transparency on, your organization can’t [call the Claude API directly from a browser](https://platform.claude.com/docs/en/manage-claude/authentication#browser-based-applications).

A key turns off some features, and [attaching a key is permanent](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key), so Anthropic recommends reading these parts of the customer-managed encryption keys guide first:

* [What changes with a key](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed): the features a key turns off.
* [What a key covers](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#encrypted-with-your-key): what your key encrypts.
* [What revoking a key means](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does): what revoking or disabling your key does. You can’t undo deleting your key.

### If you use customer-owned storage

A workspace that uses both customer-owned storage and a customer-managed key has two separate keys:

| Key | Where it’s created | What it does |
| ----- | ----- | ----- |
| Your bucket’s key | With your bucket, when you [create the bucket and roles](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles) | Encrypts your bucket. |
| Your customer-managed key | In your key management service, following the guides later on this page | Encrypts your data. It’s the key you attach to a workspace. |

Don’t use the same key for both. Which keys encrypt what’s in your bucket depends on the type of data:

* **Sealed Safety Data:** Anthropic encrypts the content under your customer-managed key before writing it to your bucket, and your storage service encrypts the stored object again under your bucket’s key. Once your customer-managed key stops working, Anthropic can’t decrypt that stored content, whatever happens to your bucket’s key.
* **Transcripts and Safety Cases:** Only your bucket’s key encrypts them.

## Attach a customer-managed key

<Warning>
  Attaching a key is permanent. You can’t detach the key or swap it for a different one. Rotating the key material within the same key is supported. On Claude Platform, the workspace can’t switch to **Legacy ZDR**, and you create a new workspace to use a different key.
</Warning>

<Steps>
  <Step title="Create and register your key">
    Follow the guide for your key management service to create your key and register it with Anthropic, then come back here to attach it.

    * [AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms)
    * [Google Cloud KMS](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms)
    * [Azure Key Vault](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault)
  </Step>

  <Step title="Attach your key">
    Attach your key before the workspace serves traffic, because the key can take up to a day to take effect on a workspace that already does.

    If the workspace will use customer-owned storage, first [connect a storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage) to your organization under **Storage destinations**. If it uses EFS, follow the steps in [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console).

    To attach your key, follow these steps for each workspace that will use it:

    1. Go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and select the workspace at the top.
    2. Select your key under **Encryption key** and save.

    If the workspace uses Anthropic-managed storage, there’s nothing more to do.

    To set up a key on Claude Platform on AWS, follow the steps in [Set up CMEK on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws).

    To set up a key on Claude Models on Google Cloud (Anthropic managed), follow the steps for your own key in [Add cloud resources](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#add-cloud-resources). You need `roles/claude.admin` instead of Organization Admin. You don’t need a bucket to use a key.
  </Step>
</Steps>

## Revoke your key

On Claude Platform, once your key has [taken effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), requests to the workspace start failing up to an hour after you revoke or disable it. Within about an hour of disabling your key, Anthropic can no longer decrypt data your key protects. A small set of records [stays outside your key](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#limited-preservation-outside-your-key). Revoking or disabling your key doesn’t delete data or undo reads that have already happened.

Before you revoke your key, read [what revoking means and what can’t be undone](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does). For what happens to your requests and who’s told, see [If your key stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#if-your-key-stops-working).

## If your key stops working

The following table shows what happens on Claude Platform when a workspace can’t use your key, and what to do about it.

| Event | Requests | Your data | Who’s told | What to do |
| ----- | ----- | ----- | ----- | ----- |
| Your key is revoked or disabled | If your key has taken effect, requests can keep succeeding for up to an hour. After that, requests to the workspace fail. | Once your key stops working, Anthropic can’t decrypt what your key protects until you re-enable your key or restore Anthropic’s access to the key. You can’t undo deleting your key. | Anthropic usually emails the members of your organization who can manage encryption keys. On Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS, Anthropic instead usually emails the person who completed your organization’s setup. | Re-enable your key, or restore Anthropic’s access to it. Requests that failed in the meantime aren’t retried, and retention periods keep running. See [what comes back when you re-enable a key](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#restore-access). |
| Your key management service can’t be reached | Can keep succeeding for up to an hour. After that, requests to the workspace fail. On the Messages API, they return a [503 error with the code `cmek_key_unreachable`](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#unreachable-key), and you can retry them. The Message Batches API retries them for you until your key is available or the batch expires. | What’s already stored is unchanged. Once your key stops working, Anthropic can’t decrypt what your key protects until your key management service can be reached again. Records Anthropic can’t encrypt during the outage aren’t kept. | No one. | Restore access to your key management service. |

If the workspace also uses customer-owned storage, see [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).

## Rotate or replace your key

You can rotate the key material within the same key without changing anything in the Claude Console.

On Claude Platform, to use a different key, create a new workspace with the new key and move your traffic to it, because [attaching a key is permanent](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key).

## Next steps

<CardGroup cols={2}>
  <Card title="Set up Enterprise Frontier Safeguards on Claude Platform" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console">
    For a workspace on EFS, attach your key, then check your setup.
  </Card>

  <Card title="Set up customer-owned storage" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage">
    Keep your Sealed Safety Data in storage in your own cloud account.
  </Card>

  <Card title="Customer-managed encryption keys" icon="book" href="https://platform.claude.com/docs/en/manage-claude/cmek">
    What a key covers, what it turns off, and what revoking it means.
  </Card>
</CardGroup>

---
title: Customer-managed encryption keys
url: https://platform.claude.com/docs/en/manage-claude/cmek
description: Use a key you hold in your own cloud to encrypt data that Claude stores.
---

Ask Claude Code about this feature

```text
/claude-api tell me about customer-managed encryption keys
```

With customer-managed encryption keys (CMEK), you create a key in your own AWS KMS, Google Cloud KMS, or Azure Key Vault. Anthropic uses it to encrypt certain data at rest. The key stays under your control, so you can rotate it, audit its use, and remove Anthropic’s access.

## Choose your setup page

Choose the service that holds your key. Claude Platform on AWS, which also uses AWS KMS, has its own page.

<CardGroup cols={2}>
  <Card title="AWS KMS" href="https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms">
    For Claude Platform and Claude Enterprise.
  </Card>

  <Card title="Google Cloud KMS" href="https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms">
    For Claude Platform and Claude Enterprise.
  </Card>

  <Card title="Azure Key Vault" href="https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault">
    For Claude Platform and Claude Enterprise.
  </Card>

  <Card title="Claude Platform on AWS" href="https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws">
    For organizations whose Claude Console sidebar shows **Account managed by AWS**.
  </Card>
</CardGroup>

On Claude Platform, you can also add and attach your key [with the Admin API](https://platform.claude.com/docs/en/manage-claude/cmek-admin-api).

## Understand CMEK before you set it up

Which product you use decides what your key encrypts, what stays under Anthropic’s key, and which features turn off or change.

<CardGroup cols={2}>
  <Card title="How CMEK works" href="https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works">
    How your key protects data, when it takes effect, and what you can see.
  </Card>

  <Card title="CMEK, data retention, and ZDR" href="https://platform.claude.com/docs/en/manage-claude/cmek-data-retention">
    Using a key with zero data retention (ZDR), and what Anthropic can preserve outside your key.
  </Card>

  <Card title="What CMEK covers on Claude Platform" href="https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform">
    Look up a feature or a kind of data.
  </Card>

  <Card title="What CMEK covers on Claude Enterprise" href="https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise">
    Look up a feature, and see what your users will notice.
  </Card>
</CardGroup>

## What you commit to

* Once you attach a key, you [can’t remove or replace it](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does).
* Your key protects only data written [after it takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect).
* If your key is deleted, Anthropic can’t recover the data it protects. [While the key is disabled](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#restore-access), Claude can’t read that data.
* On Claude Platform, a workspace with a key [must retain data](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention).

## Who can use CMEK

CMEK is optional. To turn it on for an eligible organization, contact your Anthropic account team. You need one of these roles to set it up:

* Claude Platform: Organization Admin
* Claude Platform on AWS: Admin
* Claude Enterprise: Owner or Primary Owner

## After setup

* [What happens when you rotate, disable, or delete your encryption key](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle)
* [Troubleshoot CMEK](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting)

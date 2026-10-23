---
title: Troubleshoot CMEK
url: https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting
description: Find the cause and fix for a CMEK error message, a failed verification, or an unexpected log entry.
---

**Verify** in the Claude Console, **Add** on claude.ai, and the Admin API's validate call all run the same check. When it fails (**Connection failed** in the Claude Console), see the causes for [AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#aws-kms), [Google Cloud KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#google-cloud-kms), or [Azure Key Vault](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#azure-key-vault).

If a feature stopped working, it might be one that customer-managed encryption keys (CMEK) turn off. Check the [Claude Platform list](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#turned-off-or-changed) or [Claude Enterprise list](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).

If nothing here fits, contact your Anthropic account team.

## Requests fail after setup

### `cmek_key_disabled`

```text wrap
Customer-managed encryption key is disabled or revoked. Re-enable the key to restore access.
```

This 400 error means your key management service refused Anthropic's call. Check these causes in order:

1. The key is disabled.
2. Anthropic's access to the key was removed. [Your setup page](https://platform.claude.com/docs/en/manage-claude/cmek#set-it-up) shows the access Anthropic needs.
3. On AWS KMS, the key policy [lists workspaces](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces) but not this one.
4. On AWS KMS, an IP condition blocks [Anthropic's outbound IP addresses](https://platform.claude.com/docs/en/api/ip-addresses#outbound-ip-addresses).

Fix the cause. [Two limits apply](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#restore-access) when access returns.

### `cmek_key_network_blocked`

```text wrap
The request to your key management service was blocked by its network access controls (for example, a KMS firewall or IP allowlist). Verify that your KMS network rules allow requests from Anthropic's published IP addresses, or contact Anthropic support if your configuration looks correct.
```

This is a 400 error. The key itself might be healthy. Allow [Anthropic's published IP addresses](https://platform.claude.com/docs/en/api/ip-addresses) in your key management service's network rules.

### `cmek_key_unreachable`

```text wrap
The workspace's customer-managed encryption key could not be reached. Try again shortly. If this continues, check that the key is available in your key management service, or contact Anthropic support.
```

This 503 error means [Anthropic couldn't reach your key](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#unreachable-key). Retry the request.

## Verification fails: AWS KMS

| Cause                                                | Fix                                                                                                                                                                                    |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong organization ID                                | The `org_uuid` condition must list [your Anthropic organization ID](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#prerequisites), the UUID without the `org_` prefix. |
| A workspace is missing from the policy               | A `compartment_uuid` condition must [list the compartment ID](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces) of each workspace the key is attached to.     |
| Access granted through IAM instead of the key policy | Anthropic's role needs access in [the key policy itself](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy).                                                   |

To print the key policy, run:

```bash
aws kms get-key-policy \
  --region <REGION> \
  --key-id <KEY_ARN> \
  --policy-name default
```

### A key that already protects data

If you're [replacing the policy on a key](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces#replace-the-key-policy) that already protects data, add this statement so Anthropic can still decrypt that data. In its condition, list the compartment ID of every workspace the key is or was attached to.

```json
{
  "Sid": "AllowAnthropicCMEKDecryptExistingData",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
    }
  }
}
```

## Verification fails: Google Cloud KMS

| Cause                             | Fix                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong organization label          | The key needs the [organization label](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#organization-label), with your Anthropic organization ID in lowercase. |
| Domain restricted sharing         | This organization policy blocks the grant to Anthropic's service account. [Add an exception](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#prerequisites).  |
| Disabled or destroyed key version | The key's primary version must be enabled.                                                                                                                                            |

To check the grant, run:

```bash
gcloud kms keys get-iam-policy <your-key-name> \
  --project=<your-project-id> \
  --location=<region> \
  --keyring=<your-keyring-name>
```

## Verification fails: Azure Key Vault

| Cause                                     | Fix                                                                                                                                                                  |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong organization tag                    | The key's current version needs the [organization tag](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault#organization-tag).                     |
| Role assignment not yet in effect         | A new role assignment can take a few minutes. Wait, then try again.                                                                                                  |
| The vault's network rules block Anthropic | Check the rules against the [vault settings Anthropic needs](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault#check-your-vault-configuration). |

## Attaching fails on Claude Platform on AWS

Claude Platform on AWS has no **Verify** step, so a problem with the key shows when you attach it.

| Cause                 | Fix                                                                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key policy mismatch   | Print the key policy with the [`get-key-policy` command](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#aws-kms) and compare it with the [policy on the setup page](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws#prepare-the-key-policy). |
| Condition mismatch    | Any `EncryptionContext` or `aws:SourceArn` condition must include this workspace.                                                                                                                                                                                                                  |
| Key state or location | The key must be enabled, single-Region, and in the same AWS account and region as the workspace.                                                                                                                                                                                                   |
| Missing permissions   | The principal you're signed in as needs `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key.                                                                                                                                                                                            |

If attaching still fails, find the denied `kms:` event in CloudTrail in the key's account. It shows the calling principal and, for cryptographic calls, the encryption context. Fix the cause, then click **Save** again.

## Attaching or adding a key is refused

### The workspace doesn't retain data

```text wrap
CMEK keys can only be attached to workspaces in this organization that have inference data retention enabled.
```

[Your organization uses zero data retention (ZDR)](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#zdr-organizations), and a key needs a workspace that retains data. Switch the workspace to **Standard data retention** first.

### The workspace has no Encryption key setting

Only [a workspace that retains data](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention) has this setting, so select **Standard data retention** for the workspace first. A ZDR organization's default workspace can't be switched, so use another.

### There is no Encryption keys section

In the Claude Console, select **Organization** from the dropdown menu at the top of the Data retention page. If the section is still missing, your role doesn't include it or CMEK isn't turned on for your organization. Your Anthropic account team turns CMEK on.

### The workspace already has a key

```text wrap
This workspace already has a different external key attached.
```

A workspace's key can't be replaced, so [create a new workspace](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#change-keys) for a different key.

### Adding a key on claude.ai fails

```text wrap
The encryption key couldn’t be added.
```

The check on your key failed. Find the cause for [AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#aws-kms), [Google Cloud KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#google-cloud-kms), or [Azure Key Vault](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#azure-key-vault). To retry, click **Add key** again. The dialog box opens with your earlier details. Select the checkbox, click **Continue**, then click **Add**.

## Expected errors in CloudTrail

On Claude Platform and Claude Enterprise, Anthropic checks the key whenever you verify it, attach it to a workspace, or view it on claude.ai. Each check adds four expected access-denied errors to CloudTrail.

To filter them out, match all three values:

* `requestParameters.encryptionContext.associatedData`: `Y21lay12YWxpZGF0aW9u`
* `userIdentity.accountId`: `915198916910`
* `resources.ARN`: `arn:aws:kms:<REGION>:<AWS_ACCOUNT_ID>:key/<KEY_ID>`

The first value alone isn't enough, because any caller can set it.

---
title: Limit an AWS KMS key to specific workspaces
url: https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces
description: Add a key policy condition that names the workspaces allowed to use your AWS KMS key.
---

The [key policy from setup](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy) lets every workspace in your organization use the key. With this optional condition, a workspace that isn’t listed can’t use it.

Add a workspace’s [compartment ID](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#what-one-key-protects) to the policy before you [attach the key](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#register-the-key-with-anthropic) to that workspace. For a new workspace, that means creating it without the key.

## Copy the workspace’s compartment ID

In the Claude Console, open the [Data retention](https://platform.claude.com/settings/privacy) page and select the workspace from the dropdown menu at the top. Copy the **Compartment ID** under **Encryption key**. The [Get Workspace](https://platform.claude.com/docs/en/api/organization/workspaces/retrieve) endpoint returns it as `compartment_id`.

A Claude Enterprise organization has one compartment ID. Copy it from your key under **Encryption keys** in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls).

## Add the condition to the key policy

Replace the `AllowAnthropicCMEKCrypto` statement with this one. Fill in your Anthropic organization ID and the compartment ID of every workspace that uses the key. A key that already protects data [needs one more statement](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#existing-data).

```json
{
  "Sid": "AllowAnthropicCMEKCrypto",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
  },
  "Action": ["kms:Encrypt", "kms:Decrypt"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:anthropic:org_uuid": ["<ORGANIZATION_UUID>"]
    },
    "StringEqualsIfExists": {
      "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
    }
  }
}
```

## Replace the key policy on an existing key

1. In the [AWS KMS console](https://console.aws.amazon.com/kms), open the key and click the **Key policy** tab.
2. If you see **Switch to policy view**, click it.
3. Click **Edit**.
4. Replace the JSON with your key policy.
5. Click **Save changes**.

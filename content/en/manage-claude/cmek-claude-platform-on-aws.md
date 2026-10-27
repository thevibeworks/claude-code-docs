---
title: Set up CMEK on Claude Platform on AWS
url: https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws
description: Create an AWS KMS key in your AWS account and attach it to a workspace on Claude Platform on AWS.
---

If your Claude Console sidebar doesn’t show **Account managed by AWS**, follow [Set up CMEK with AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms) instead.

## Before you start

* Customer-managed encryption keys (CMEK) are [turned on for your organization](https://platform.claude.com/docs/en/manage-claude/cmek#availability).

* In the AWS account that hosts your organization, you can create AWS KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).

* You have the **Admin** role in the [Claude Console](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#using-the-claude-console).

* The IAM principal you sign in with has these permissions:

  * Sign in: `aws-external-anthropic:AssumeConsole`
  * Add a key: `aws-external-anthropic:RegisterKey`
  * View keys: `aws-external-anthropic:ListKeys` and `aws-external-anthropic:GetKey`
  * Attach a key: `aws-external-anthropic:UpdateWorkspace` or `aws-external-anthropic:CreateWorkspace`, plus `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key
  * Pick the key from a list (optional): `kms:ListKeys` and `kms:DescribeKey`

  To scope them, see [IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys).

* You have a workspace with no key attached, ideally a new one, because [existing data stays under Anthropic’s key](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect). The key policy lists its compartment ID.

In the Claude Console, open the [Data retention](https://platform.claude.com/settings/privacy) page and select the workspace from the dropdown menu at the top. Copy the **Compartment ID** under **Encryption key**. The [Get Workspace](https://platform.claude.com/docs/en/api/organization/workspaces/retrieve) endpoint returns it as `compartment_id`.

## In AWS: create the key

### Write the key policy

This policy gives the AWS service principal `aws-external-anthropic.amazonaws.com` access to your key. Use only the name published on this page, never one sent by email or chat. Copy the policy into a text editor:

```json key-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccountRootAdmin",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<AWS_ACCOUNT_ID>:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowClaudePlatformOnAWSCrypto",
      "Effect": "Allow",
      "Principal": {
        "Service": "aws-external-anthropic.amazonaws.com"
      },
      "Action": ["kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
        }
      }
    },
    {
      "Sid": "AllowClaudePlatformOnAWSDescribe",
      "Effect": "Allow",
      "Principal": {
        "Service": "aws-external-anthropic.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    }
  ]
}
```

Replace `<AWS_ACCOUNT_ID>` with your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html) and `<COMPARTMENT_UUID>` with the [compartment ID](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws#prerequisites).

The optional `EncryptionContext` condition limits the key to the workspaces you list. Before you attach the key to another workspace, add that workspace’s compartment ID and [replace the policy on the key](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces#replace-the-key-policy). To do without the condition, delete the `Condition` block from the `AllowClaudePlatformOnAWSCrypto` statement. If you add the condition later, list every workspace the key is already attached to.

To narrow access further, use the key policy, not IP-based restrictions. Add an `aws:SourceArn` condition to both service principal statements. This one allows every workspace in your AWS account:

```text wrap
"ArnLike": {"aws:SourceArn": "arn:aws:aws-external-anthropic:*:<AWS_ACCOUNT_ID>:workspace/*"}
```

For specific workspaces, list their full [workspace ARNs](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#service-details) instead, in this form:

```text wrap
arn:aws:aws-external-anthropic:<REGION>:<AWS_ACCOUNT_ID>:workspace/<WORKSPACE_ID>
```

### Create the key

Create the key in the AWS account that hosts your organization, in the same region as the workspace.

<Tabs>
  <Tab title="AWS Console">
    <Steps>
      <Step title="Open the Create key wizard">
        Open the [AWS KMS console](https://console.aws.amazon.com/kms) and switch to the region for the key. Go to **Customer managed keys** and click **Create key**.
      </Step>

      <Step title="Configure key">
        Make sure that these options are selected:

        * **Key type:** Symmetric
        * **Key usage:** Encrypt and decrypt
        * **Advanced options > Key material origin:** KMS
        * **Advanced options > Regionality:** Single-Region key

        Click **Next**.

        <Frame caption="Symmetric, encrypt and decrypt, single-Region key.">
          ![AWS KMS Configure key step with Symmetric key type, Encrypt and decrypt key usage, and Single-Region key selected.](https://platform.claude.com/docs/images/cmek/aws-configure-key.png)
        </Frame>
      </Step>

      <Step title="Add labels">
        Enter an **Alias** for the key, such as `anthropic-cmek`. Click **Next**.

        <Frame caption="An alias for the key.">
          ![AWS KMS Add labels step with an alias of anthropic-cmek and a description of Anthropic CMEK.](https://platform.claude.com/docs/images/cmek/aws-add-labels.png)
        </Frame>
      </Step>

      <Step title="Define key administrative permissions">
        Don’t select any key administrators. Your key policy already gives your AWS account full admin control. Click **Next**.

        <Frame caption="Leave key administrators empty.">
          ![AWS KMS Define key administrative permissions step listing IAM roles that can administer the key.](https://platform.claude.com/docs/images/cmek/aws-admin-permissions.png)
        </Frame>
      </Step>

      <Step title="Define key usage permissions">
        Don’t select any key users, and don’t add anything under **Other AWS accounts**. Your key policy already grants the access that’s needed. Click **Next**.
      </Step>

      <Step title="Edit key policy">
        Click **Edit**. Replace the whole policy with your key policy, then click **Next**.
      </Step>

      <Step title="Review">
        Click **Finish**.
      </Step>

      <Step title="Copy the key ARN">
        In **Customer managed keys**, open the new key and copy its ARN. Whoever adds the key in Claude needs it.
      </Step>
    </Steps>
  </Tab>

  <Tab title="AWS CLI">
    Save your key policy as `key-policy.json`, then create the key. Replace `<REGION>` with the key’s region.

    ```bash
    aws kms create-key \
      --region <REGION> \
      --description "Anthropic CMEK" \
      --key-usage ENCRYPT_DECRYPT \
      --policy file://key-policy.json
    ```

    Copy `KeyMetadata.Arn` from the output. Whoever adds the key in Claude needs the ARN.
  </Tab>
</Tabs>

## In Claude: add and attach the key

Sign in to the Claude Console through AWS. To script this part instead, use the endpoints listed in [IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys).

<Steps>
  <Step title="Open the encryption key settings">
    In the Claude Console, open [Encryption keys](https://platform.claude.com/settings/privacy#encryption-keys) on the Data retention page. If the section isn’t there, select **Organization** from the dropdown menu at the top.
  </Step>

  <Step title="Add the key">
    Under **Encryption keys**, click **Add key** and enter a **Display name**.
  </Step>

  <Step title="Enter the key ARN">
    In **KMS key ARN**, select your key. If it isn’t listed, click **Enter ARN manually** and paste the ARN. Anthropic rejects alias ARNs and multi-Region keys. Click **Add**.
  </Step>

  <Step title="Attach the key to a workspace">
    <Warning>
      Attaching a key [can’t be undone](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does). You can’t remove it from the workspace or replace it. If the key is deleted, Anthropic can’t recover the data it protects.
    </Warning>

    1. At the top of the Data retention page, select the workspace from the dropdown menu.
    2. Under **Encryption key**, select the key and click **Save**.
    3. Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

    You see **Workspace settings updated.** Once the key [takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), CloudTrail records the calls to your key.

    Attaching checks the key with one encrypt call and one decrypt call, so a key policy problem shows up here. If you get a KMS access error, see the [causes and fixes](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#claude-platform-on-aws).
  </Step>
</Steps>

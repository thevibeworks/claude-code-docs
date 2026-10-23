---
title: Set up CMEK with AWS KMS
url: https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms
description: Create an AWS KMS key, give Anthropic access to it, and put it to use in Claude Platform or Claude Enterprise.
---

Let Claude Code set up this feature for you

```text
/claude-api help me configure a customer-managed encryption key with AWS KMS
```

If your Claude Console sidebar shows **Account managed by AWS**, follow [Set up CMEK on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws) instead.

## Before you start

In Claude:

* Customer-managed encryption keys (CMEK) are [turned on for your organization](https://platform.claude.com/docs/en/manage-claude/cmek#availability).
* You have your Anthropic organization ID, the UUID without the `org_` prefix. Copy it from [Organization](https://platform.claude.com/settings/organization) in the Claude Console, or from **Organization settings > Organization and access** on claude.ai. Whoever creates the key needs it.
* You're an Organization Admin on Claude Platform, or an Owner or Primary Owner on Claude Enterprise.
* On Claude Platform, you have a workspace that [retains data](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention), ideally a new one, because [existing data stays under Anthropic's key](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect).
* On Claude Enterprise, you know [which features turn off or change](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).

In AWS:

* You can create AWS KMS keys and set their key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
* Any IP restriction on AWS KMS access allows [Anthropic's outbound IP addresses](https://platform.claude.com/docs/en/api/ip-addresses#outbound-ip-addresses).

## In AWS: create the key

After a failed **Verify** or **Add**, see the [fixes for AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#aws-kms).

### Write the key policy

This policy gives Anthropic's IAM role access to your key. Use only the role ARN published on this page, never one sent by email or chat. Copy the policy into a text editor:

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
        }
      }
    },
    {
      "Sid": "AllowAnthropicCMEKDescribe",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    }
  ]
}
```

Replace `<AWS_ACCOUNT_ID>` with your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html) and `<ORGANIZATION_UUID>` with your [Anthropic organization ID](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#prerequisites). Keep the `kms:EncryptionContext:anthropic:org_uuid` condition, or verification fails.

You can also [limit the key to specific workspaces](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces) by listing their compartment IDs. If you're replacing the policy on a key that already protects Claude data, [add one more statement](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#existing-data).

### Create the key

Create the key in a US region. For the lowest latency, use `us-east-2`.

To use a key you already have in AWS KMS, [replace its key policy](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces#replace-the-key-policy).

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
        Don't select any key administrators. Your key policy already gives your AWS account full admin control. Click **Next**.

        <Frame caption="Leave key administrators empty.">
          ![AWS KMS Define key administrative permissions step listing IAM roles that can administer the key.](https://platform.claude.com/docs/images/cmek/aws-admin-permissions.png)
        </Frame>
      </Step>

      <Step title="Define key usage permissions">
        Don't select any key users, and don't add anything under **Other AWS accounts**. Your key policy already grants the access that's needed. Click **Next**.
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
    Save your key policy as `key-policy.json`, then create the key. Replace `<REGION>` with the key's region.

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

Each check of the key in Claude adds four expected access-denied errors to CloudTrail. You can [filter them out](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#cloudtrail).

## In Claude: add and attach the key

To script this part on Claude Platform, [use the Admin API](https://platform.claude.com/docs/en/manage-claude/cmek-admin-api) instead.

<Tabs>
  <Tab title="Claude Platform">
    <Steps>
      <Step title="Open the encryption key settings">
        In the Claude Console, open [Encryption keys](https://platform.claude.com/settings/privacy#encryption-keys) on the Data retention page. If the section isn't there, select **Organization** from the dropdown menu at the top.
      </Step>

      <Step title="Add the key">
        Under **Encryption keys**, click **Add key**. Enter a **Display name**, select **AWS KMS**, and click **Continue**.
      </Step>

      <Step title="Enter the key ARN">
        Check that your [key policy](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy) contains the **Organization ID for the key policy** shown in the dialog box. Paste the key ARN into **KMS key ARN** and click **Add**.
      </Step>

      <Step title="Verify the key">
        In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If **Connection failed** appears instead, see [Troubleshoot CMEK](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting).
      </Step>

      <Step title="Attach the key to a workspace">
        <Warning>
          Attaching a key [can't be undone](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does). You can't remove it from the workspace or replace it. If the key is deleted, Anthropic can't recover the data it protects.
        </Warning>

        1. At the top of the Data retention page, select the workspace from the dropdown menu.
        2. Under **Encryption key**, select the key and click **Save**.
        3. Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

        You see **Workspace settings updated.** Once the key [takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), your cloud provider's audit log shows Anthropic's calls to the key.

        In a [ZDR organization](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#zdr-organizations), after you select the workspace, select **Standard data retention** so that **Encryption key** appears. After you click **Save**, click **Accept** on the data retention terms.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Claude Enterprise">
    On Claude Enterprise, CMEK applies to the whole organization, and you can add only one key.

    <Warning>
      Adding a key [can't be undone](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does). You can't remove it from the organization or replace it. If the key is deleted, Anthropic can't recover the data it protects.
    </Warning>

    Adding the key [turns off or changes some features](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed) for every user. To try CMEK first, use a separate organization.

    <Steps>
      <Step title="Open the encryption key settings">
        Go to [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find **Encryption keys**.
      </Step>

      <Step title="Add the key">
        Click **Add key**. Enter a **Display name** and select **AWS KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.
      </Step>

      <Step title="Enter the key ARN">
        Check that your [key policy](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy) contains the **Organization ID for the key policy** shown in the dialog box. Paste the key ARN into **KMS key ARN** and click **Add**.
      </Step>

      <Step title="Confirm that the key was added">
        The check can take up to 30 seconds. When **Encryption key configured.** appears, click **Done**. If **The encryption key couldn’t be added.** appears instead, [find the cause and retry](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#claude-ai-add-fails).

        Your key protects data written from then on. Tell your users [which features changed](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).
      </Step>
    </Steps>
  </Tab>
</Tabs>

---
title: Set up CMEK with Google Cloud KMS
url: https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms
description: Create a Google Cloud KMS key, give Anthropic access to it, and put it to use in Claude Platform or Claude Enterprise.
---

Let Claude Code set up this feature for you

```text
/claude-api help me configure a customer-managed encryption key with Google Cloud KMS
```

## Before you start

In Claude:

* Customer-managed encryption keys (CMEK) are [turned on for your organization](https://platform.claude.com/docs/en/manage-claude/cmek#availability).
* You have your Anthropic organization ID, the UUID without the `org_` prefix. Copy it from [Organization](https://platform.claude.com/settings/organization) in the Claude Console, or from **Organization settings > Organization and access** on claude.ai. Whoever creates the key needs it.
* You're an Organization Admin on Claude Platform, or an Owner or Primary Owner on Claude Enterprise.
* On Claude Platform, you have a workspace that [retains data](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention), ideally a new one, because [existing data stays under Anthropic's key](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect).
* On Claude Enterprise, you know [which features turn off or change](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).

In Google Cloud:

* The Cloud KMS API is turned on.
* You can create key rings and keys, and set IAM policy on them (`roles/cloudkms.admin` or equivalent).
* Cloud KMS [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) (Data Read and Data Write) are on, so Cloud Logging records Anthropic's use of your key. They're off by default.
* If your Google Cloud organization enforces domain restricted sharing (`constraints/iam.allowedPolicyMemberDomains`), it blocks the grant to Anthropic's service account. Add a project-level exception, or allow Anthropic's Cloud Identity customer ID. Contact Anthropic for the ID.

## In Google Cloud: create the key

After a failed **Verify** or **Add**, see the [fixes for Google Cloud KMS](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#google-cloud-kms).

These steps label the key with your Anthropic organization ID in lowercase (`<ORGANIZATION_UUID>`) and grant access to Anthropic's service account:

```text wrap
anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com
```

Use only this address, never one sent by email or chat.

For the lowest latency, use `us-east5` or `us-central1`. Anthropic strongly recommends HSM protection.

To use a key you already have, [add the organization label](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#organization-label) first.

<Tabs>
  <Tab title="Google Cloud Console">
    <Steps>
      <Step title="Create or choose a key ring">
        In the Google Cloud console, go to the [Key management](https://console.cloud.google.com/security/kms) page. Open a key ring in a single-region US location, such as `us-east5`, or create one.
      </Step>

      <Step title="Configure the key">
        Click **Create key** and enter a name. Select these options:

        * **Protection level:** HSM
        * **Key material:** Generated key
        * **Purpose:** Symmetric encrypt/decrypt
        * **Algorithm:** Google symmetric key
      </Step>

      <Step title="Add the organization label">
        Click **Additional settings**, then **Add label**. Enter the organization label:

        * **Key 1:** `anthropic-org-<ORGANIZATION_UUID>`
        * **Value 1:** `true`

        Click **Create**.

        <Frame caption="An HSM-protected symmetric encrypt/decrypt key with the organization label.">
          ![Google Cloud KMS Create key page with HSM protection, symmetric encrypt/decrypt, and the anthropic-org label set to true.](https://platform.claude.com/docs/images/cmek/gcp-create-key-label.png)
        </Frame>
      </Step>

      <Step title="Open the key's permissions">
        On the key ring details page, select the checkbox next to the key. Open the **Permissions** panel and click **Grant access**.
      </Step>

      <Step title="Grant Anthropic's service account access to the key">
        Check that **Resource** shows the key, not the key ring or project. Enter these values:

        * **New principals:** `anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com`
        * **Role:** Cloud KMS CryptoKey Encrypter/Decrypter

        Click **Add another role** and select **Cloud KMS Viewer**. Click **Save**.

        <Frame caption="Grant the Anthropic service account both roles, scoped to the key.">
          ![Grant access dialog with the Anthropic service account assigned Cloud KMS CryptoKey Encrypter/Decrypter and Viewer roles.](https://platform.claude.com/docs/images/cmek/gcp-grant-access.png)
        </Frame>
      </Step>

      <Step title="Copy the full key resource name">
        On the key ring details page, open the key's **Actions** menu and click **Copy resource name**.

        <Frame caption="Copy the key's full resource name from the actions menu.">
          ![Google Cloud key ring details with the Copy resource name action highlighted in the key's actions menu.](https://platform.claude.com/docs/images/cmek/gcp-copy-resource-name.png)
        </Frame>
      </Step>
    </Steps>
  </Tab>

  <Tab title="gcloud CLI">
    In each command, replace these placeholders:

    * **`<your-project-id>`:** your Google Cloud project ID
    * **`<region>`:** the key's location, such as `us-east5`
    * **`<your-keyring-name>`:** the key ring's name
    * **`<your-key-name>`:** the key's name
    * **`<ORGANIZATION_UUID>`:** your Anthropic organization ID in lowercase

    <Steps>
      <Step title="Create or choose a key ring">
        Skip this step if you already have a key ring to reuse.

        ```bash
        gcloud kms keyrings create <your-keyring-name> \
          --project=<your-project-id> \
          --location=<region>
        ```
      </Step>

      <Step title="Create the key">
        ```bash
        gcloud kms keys create <your-key-name> \
          --project=<your-project-id> \
          --location=<region> \
          --keyring=<your-keyring-name> \
          --purpose=encryption \
          --protection-level=hsm \
          --labels=anthropic-org-<ORGANIZATION_UUID>=true
        ```

        For software protection, omit `--protection-level=hsm`.
      </Step>

      <Step title="Grant Anthropic's service account access to the key">
        Run both commands:

        ```bash
        gcloud kms keys add-iam-policy-binding <your-key-name> \
          --project=<your-project-id> \
          --location=<region> \
          --keyring=<your-keyring-name> \
          --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
          --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
        ```

        ```bash
        gcloud kms keys add-iam-policy-binding <your-key-name> \
          --project=<your-project-id> \
          --location=<region> \
          --keyring=<your-keyring-name> \
          --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
          --role=roles/cloudkms.viewer
        ```
      </Step>

      <Step title="Get the full key resource name">
        ```bash
        gcloud kms keys describe <your-key-name> \
          --project=<your-project-id> \
          --location=<region> \
          --keyring=<your-keyring-name> \
          --format="value(name)"
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

Whoever adds the key in Claude needs its full resource name, in this format:

```text wrap
projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>
```

### Add the organization label to a key you already have

Verification fails unless the key has the label `anthropic-org-<ORGANIZATION_UUID>` set to `true`, with your Anthropic organization ID in lowercase. To add the label, run:

```bash
gcloud kms keys update <your-key-name> \
  --project=<your-project-id> \
  --location=<region> \
  --keyring=<your-keyring-name> \
  --update-labels=anthropic-org-<ORGANIZATION_UUID>=true
```

The other values are in the key's full resource name, and the command keeps existing labels. Then skip to [the steps that grant access](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#encryption-key-setup).

## In Claude: add and attach the key

To script this part on Claude Platform, [use the Admin API](https://platform.claude.com/docs/en/manage-claude/cmek-admin-api) instead.

<Tabs>
  <Tab title="Claude Platform">
    <Steps>
      <Step title="Open the encryption key settings">
        In the Claude Console, open [Encryption keys](https://platform.claude.com/settings/privacy#encryption-keys) on the Data retention page. If the section isn't there, select **Organization** from the dropdown menu at the top.
      </Step>

      <Step title="Add the key">
        Under **Encryption keys**, click **Add key**. Enter a **Display name**, select **Google Cloud KMS**, and click **Continue**.
      </Step>

      <Step title="Enter the key resource name">
        Check that your key has the **Organization label** shown in the dialog box. Paste the key's full resource name into **Key resource name** and click **Add**.
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
        Click **Add key**. Enter a **Display name** and select **Google Cloud KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.
      </Step>

      <Step title="Enter the key resource name">
        Check that your key has the **Organization label** shown in the dialog box. Paste the key's full resource name into **Key resource name** and click **Add**.
      </Step>

      <Step title="Confirm that the key was added">
        The check can take up to 30 seconds. When **Encryption key configured.** appears, click **Done**. If **The encryption key couldn’t be added.** appears instead, [find the cause and retry](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#claude-ai-add-fails).

        Your key protects data written from then on. Tell your users [which features changed](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed).
      </Step>
    </Steps>
  </Tab>
</Tabs>

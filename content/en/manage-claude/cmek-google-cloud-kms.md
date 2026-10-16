---
title: Configure Google Cloud KMS for CMEK
url: https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms
description: Use Google Cloud KMS to provide an encryption key for your organization.
---

Let Claude Code set up this feature for you

```text
/claude-api help me configure a customer-managed encryption key with Google Cloud KMS
```

This guide shows how to use a Google Cloud KMS key as a [customer-managed encryption key (CMEK)](https://platform.claude.com/docs/en/manage-claude/cmek) for your Anthropic organization.

<Warning>
  Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](https://platform.claude.com/docs/en/manage-claude/cmek) before you begin.
</Warning>

## Prerequisites

* A Google Cloud project with billing enabled.
* The Cloud KMS API enabled (`cloudkms.googleapis.com`).
* Permissions to create KMS key rings and keys, and to set IAM policy on them (`roles/cloudkms.admin` or equivalent).
* Cloud KMS Data Access audit logs (Data Read and Data Write) turned on for the project, so that Cloud Logging records Anthropic's use of your key. They're off by default. To turn them on, see Google's [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).
* To create the key from the command line, the [`gcloud` CLI](https://cloud.google.com/cli) installed and authenticated.
* To register the key through the API, an Anthropic Admin API key for your organization.

## Anthropic service account email

In this guide, you give the following Anthropic service account access to your key:

```text wrap
anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com
```

<Warning>
  Use only this published service account email. Never trust an identifier provided over email, chat, or any onboarding channel.
</Warning>

<Note>
  **Domain restricted sharing:** If your Google Cloud organization enforces `constraints/iam.allowedPolicyMemberDomains`, it rejects the IAM bindings for this service account. Add a project-level exception to that constraint, or add Anthropic's Cloud Identity customer ID (format `C0xxxxxxxx`) to the allowed list. Contact Anthropic for the customer ID.
</Note>

## Encryption key setup

The key must meet these requirements:

* **Location:** Use a single-region US location, such as `us-east5`. Multi-region locations such as `us` and `global` aren't supported. See [Availability and regions](https://platform.claude.com/docs/en/manage-claude/cmek#availability-and-regions).
* **Type:** Use a symmetric key with the `ENCRYPT_DECRYPT` purpose. Anthropic strongly recommends HSM protection.
* **Organization label:** Add the label `anthropic-org-<ORGANIZATION_UUID>` with the value `true`. Replace `<ORGANIZATION_UUID>` with your Anthropic organization ID in lowercase. Validation fails without this label. To label an existing key, see [Keys you already have](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#existing-key-label).
* **Access:** Give Anthropic's service account the `roles/cloudkms.cryptoKeyEncrypterDecrypter` and `roles/cloudkms.viewer` roles on the key itself.

<Note>
  **Finding your organization ID:** Use the bare UUID, not the `org_`-prefixed ID. Copy it from one of these places:

  * **Claude Console:** the **Organization ID** field on the [Organization](https://platform.claude.com/settings/organization) page (`platform.claude.com/settings/organization`)
  * **claude.ai:** the **Organization ID** field under **Organization settings > Organization**
  * **Admin API:** the `id` field from the [Organization Info](https://platform.claude.com/docs/en/api/organization/retrieve) endpoint
</Note>

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

You register the key with its full resource name, in this format:

```text wrap
projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>
```

<Note>
  **Keys you already have:** Add the organization label with this command, in Cloud Shell or with the gcloud CLI:

  ```bash
  gcloud kms keys update <your-key-name> \
    --project=<your-project-id> \
    --location=<region> \
    --keyring=<your-keyring-name> \
    --update-labels=anthropic-org-<ORGANIZATION_UUID>=true
  ```

  The placeholders match the parts of the key's full resource name. The command merges the label with any labels the key already has. Then grant access and copy the resource name as the preceding steps describe.

  To share one key among several Anthropic organizations, add one organization label for each.
</Note>

## Register the key with Anthropic

<Tabs>
  <Tab title="Claude Platform">
    <Tabs>
      <Tab title="Claude Console">
        <Steps>
          <Step title="Open the encryption key settings">
            In the Claude Console, go to the [Data retention](https://platform.claude.com/settings/privacy#encryption-keys) page (`platform.claude.com/settings/privacy`). If you don't see **Encryption keys**, select **Organization** from the dropdown menu at the top of the page.
          </Step>

          <Step title="Add the key">
            Under **Encryption keys**, click **Add key**. Enter a **Display name** and select **Google Cloud KMS**. Click **Continue**.
          </Step>

          <Step title="Enter the key resource name">
            The dialog box shows an **Organization label**. Check that your key has this label. Paste the full key resource name into **Key resource name** and click **Add**.
          </Step>

          <Step title="Validate the key">
            In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#troubleshoot-validation) for common causes.
          </Step>

          <Step title="Attach the key to a workspace">
            Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](https://platform.claude.com/docs/en/manage-claude/cmek#how-it-works).

            On the Data retention page, select the workspace from the dropdown menu at the top of the page. Under **Encryption key**, select the key and click **Save**.
          </Step>

          <Step title="Confirm the change">
            Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.
          </Step>
        </Steps>
      </Tab>

      <Tab title="API">
        <Steps>
          <Step title="Create the external key">
            Replace `<friendly-name>` with a display name. Replace the value that starts with `projects/` with the full key resource name.

            <CodeGroup>
              ```bash cURL
              curl -sS "https://api.anthropic.com/v1/organizations/external_keys" \
                -H "x-api-key: $ANTHROPIC_API_KEY" \
                -H "anthropic-version: 2023-06-01" \
                -H "content-type: application/json" \
                -d '{
                  "display_name": "<friendly-name>",
                  "geo": "us",
                  "provider_config": {
                    "type": "gcp",
                    "key_name": "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>"
                  }
                }'
              ```

              ```bash CLI
              ant organization:external-keys create <<'YAML'
              display_name: "<friendly-name>"
              geo: us
              provider_config:
                type: gcp
                key_name: "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>"
              YAML
              ```

              ```python Python
              client = anthropic.Anthropic()

              external_key = client.organization.external_keys.create(
                  display_name="<friendly-name>",
                  geo="us",
                  provider_config={
                      "type": "gcp",
                      "key_name": "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>",
                  },
              )

              print(f"id: {external_key.id}")
              print(f"display_name: {external_key.display_name}")
              ```

              ```typescript TypeScript
              const client = new Anthropic();

              const externalKey = await client.organization.externalKeys.create({
                display_name: "<friendly-name>",
                geo: "us",
                provider_config: {
                  type: "gcp",
                  key_name:
                    "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>"
                }
              });

              console.log(`id: ${externalKey.id}`);
              console.log(`display_name: ${externalKey.display_name}`);
              ```

              ```csharp C#
              using Anthropic.Models.Organization.ExternalKeys;

              AnthropicClient client = new();

              var externalKey = await client.Organization.ExternalKeys.Create(new()
              {
                  DisplayName = "<friendly-name>",
                  Geo = Geo.Us,
                  ProviderConfig = new GcpExternalKeyConfig
                  {
                      KeyName = "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>"
                  }
              });

              Console.WriteLine($"id: {externalKey.ID}");
              Console.WriteLine($"display_name: {externalKey.DisplayName}");
              ```

              ```go Go
              client := anthropic.NewClient()

              externalKey, err := client.Organization.ExternalKeys.New(context.Background(), anthropic.OrganizationExternalKeyNewParams{
              	DisplayName: anthropic.String("<friendly-name>"),
              	Geo:         anthropic.OrganizationExternalKeyNewParamsGeoUs,
              	ProviderConfig: anthropic.OrganizationExternalKeyNewParamsProviderConfigUnion{
              		OfGCP: &anthropic.GCPExternalKeyConfigParam{
              			KeyName: "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>",
              		},
              	},
              })
              if err != nil {
              	log.Fatal(err)
              }

              fmt.Printf("id: %s\n", externalKey.ID)
              fmt.Printf("display_name: %s\n", externalKey.DisplayName)
              ```

              ```java Java
              import com.anthropic.models.organization.externalkeys.ExternalKeyCreateParams;

              void main() {
                  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

                  var params = ExternalKeyCreateParams.builder()
                      .displayName("<friendly-name>")
                      .geo(ExternalKeyCreateParams.Geo.US)
                      .gcpProviderConfig("projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>")
                      .build();
                  var externalKey = client.organization().externalKeys().create(params);

                  IO.println("id: " + externalKey.id());
                  IO.println("display_name: " + externalKey.displayName().orElseThrow());
              }
              ```

              ```php PHP
              use Anthropic\Organization\ExternalKeys\ExternalKeyCreateParams\Geo;
              // ...

              $client = new Client();

              $externalKey = $client->organization->externalKeys->create(
                  displayName: '<friendly-name>',
                  geo: Geo::US,
                  providerConfig: [
                      'type' => 'gcp',
                      'keyName' => 'projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>',
                  ],
              );

              echo "id: {$externalKey->id}\n";
              echo "display_name: {$externalKey->displayName}\n";
              ```

              ```ruby Ruby
              client = Anthropic::Client.new

              external_key = client.organization.external_keys.create(
                display_name: "<friendly-name>",
                geo: :us,
                provider_config: {
                  type: :gcp,
                  key_name: "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>"
                }
              )

              puts "id: #{external_key.id}"
              puts "display_name: #{external_key.display_name}"
              ```
            </CodeGroup>

            The `id` field of the response contains the external key ID. Copy it for the next two steps:

            ```json
            {
              "type": "external_key",
              "id": "ekey_<id>",
              "display_name": "<friendly-name>"
            }
            ```
          </Step>

          <Step title="Validate the key">
            Replace `ekey_<id>` with the external key ID.

            <CodeGroup>
              ```bash cURL
              curl -sS -X POST "https://api.anthropic.com/v1/organizations/external_keys/ekey_<id>/validate" \
                -H "x-api-key: $ANTHROPIC_API_KEY" \
                -H "anthropic-version: 2023-06-01"
              ```

              ```bash CLI
              ant organization:external-keys validate --external-key-id "ekey_<id>"
              ```

              ```python Python
              client = anthropic.Anthropic()

              validation = client.organization.external_keys.validate("ekey_<id>")

              print(f"status: {validation.status}")
              print(f"error: {validation.error}")
              ```

              ```typescript TypeScript
              const client = new Anthropic();

              const validation = await client.organization.externalKeys.validate("ekey_<id>");

              console.log(`status: ${validation.status}`);
              console.log(`error: ${validation.error}`);
              ```

              ```csharp C#
              AnthropicClient client = new();

              var validation = await client.Organization.ExternalKeys.Validate("ekey_<id>");

              Console.WriteLine($"status: {validation.Status.Raw()}");
              Console.WriteLine($"error: {validation.Error}");
              ```

              ```go Go
              client := anthropic.NewClient()

              validation, err := client.Organization.ExternalKeys.Validate(context.Background(), "ekey_<id>")
              if err != nil {
              	log.Fatal(err)
              }

              fmt.Printf("status: %s\n", validation.Status)
              fmt.Printf("error: %s\n", validation.Error)
              ```

              ```java Java
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              var validation = client.organization().externalKeys().validate("ekey_<id>");

              IO.println("status: " + validation.status().asString());
              IO.println("error: " + validation.error().orElse(""));
              ```

              ```php PHP
              $client = new Client();

              $validation = $client->organization->externalKeys->validate(
                  externalKeyID: 'ekey_<id>',
              );

              echo "status: {$validation->status}\n";
              echo "error: {$validation->error}\n";
              ```

              ```ruby Ruby
              client = Anthropic::Client.new

              external_key_id = "ekey_<id>"
              validation = client.organization.external_keys.validate(external_key_id)

              puts "status: #{validation.status}"
              puts "error: #{validation.error}"
              ```
            </CodeGroup>

            A successful response looks like this:

            ```json
            { "type": "external_key_validation", "status": "success", "error": null }
            ```

            If validation fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#troubleshoot-validation).
          </Step>

          <Step title="Attach the key to a workspace">
            Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](https://platform.claude.com/docs/en/manage-claude/cmek#how-it-works).

            Replace `<workspace-id>` with the workspace ID and `ekey_<id>` with the external key ID.

            <CodeGroup>
              ```bash cURL
              curl -sS -X POST "https://api.anthropic.com/v1/organizations/workspaces/<workspace-id>" \
                -H "x-api-key: $ANTHROPIC_API_KEY" \
                -H "anthropic-version: 2023-06-01" \
                -H "content-type: application/json" \
                -d '{
                  "external_key_id": "ekey_<id>"
                }'
              ```

              ```bash CLI
              ant organization:workspaces update \
                --workspace-id "<workspace-id>" \
                --external-key-id "ekey_<id>"
              ```

              ```python Python
              client = anthropic.Anthropic()

              workspace = client.organization.workspaces.update(
                  "<workspace-id>", external_key_id="ekey_<id>"
              )

              print(f"id: {workspace.id}")
              print(f"external_key_id: {workspace.external_key_id}")
              ```

              ```typescript TypeScript
              const client = new Anthropic();

              const workspace = await client.organization.workspaces.update("<workspace-id>", {
                external_key_id: "ekey_<id>"
              });

              console.log(`id: ${workspace.id}`);
              console.log(`external_key_id: ${workspace.external_key_id}`);
              ```

              ```csharp C#
              AnthropicClient client = new();

              var workspace = await client.Organization.Workspaces.Update("<workspace-id>", new()
              {
                  ExternalKeyID = "ekey_<id>"
              });

              Console.WriteLine($"id: {workspace.ID}");
              Console.WriteLine($"external_key_id: {workspace.ExternalKeyID}");
              ```

              ```go Go
              client := anthropic.NewClient()

              workspace, err := client.Organization.Workspaces.Update(
              	context.Background(),
              	"<workspace-id>",
              	anthropic.OrganizationWorkspaceUpdateParams{
              		ExternalKeyID: anthropic.String("ekey_<id>"),
              	},
              )
              if err != nil {
              	log.Fatal(err)
              }

              fmt.Printf("id: %s\n", workspace.ID)
              fmt.Printf("external_key_id: %s\n", workspace.ExternalKeyID)
              ```

              ```java Java
              import com.anthropic.models.organization.workspaces.WorkspaceUpdateParams;

              void main() {
                  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

                  var params = WorkspaceUpdateParams.builder()
                      .externalKeyId("ekey_<id>")
                      .build();
                  var workspace = client.organization().workspaces().update("<workspace-id>", params);

                  IO.println("id: " + workspace.id());
                  IO.println("external_key_id: " + workspace.externalKeyId().orElseThrow());
              }
              ```

              ```php PHP
              $client = new Client();

              $workspace = $client->organization->workspaces->update(
                  workspaceID: '<workspace-id>',
                  externalKeyID: 'ekey_<id>',
              );

              echo "id: {$workspace->id}\n";
              echo "external_key_id: {$workspace->externalKeyID}\n";
              ```

              ```ruby Ruby
              client = Anthropic::Client.new

              workspace_id = "<workspace-id>"
              workspace = client.organization.workspaces.update(
                workspace_id,
                external_key_id: "ekey_<id>"
              )

              puts "id: #{workspace.id}"
              puts "external_key_id: #{workspace.external_key_id}"
              ```
            </CodeGroup>
          </Step>
        </Steps>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Claude Enterprise">
    On Claude Enterprise, CMEK applies to the whole organization, and an organization can have only one key.

    <Steps>
      <Step title="Open the encryption key settings">
        Go to [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find **Encryption keys**.
      </Step>

      <Step title="Add the key">
        Click **Add key**. Enter a **Display name** and select **Google Cloud KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.
      </Step>

      <Step title="Enter the key resource name">
        The dialog box shows an **Organization label**. Check that your key has this label. Paste the full key resource name into **Key resource name** and click **Add**.
      </Step>

      <Step title="Confirm that validation passed">
        When the check passes, **Encryption key configured** appears, and your organization is CMEK-protected from then on. If the check fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#troubleshoot-validation).
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Troubleshoot validation

If validation fails, common causes are:

* **Wrong organization label:** Make sure the key has the [organization label](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#organization-label), with your bare organization ID in lowercase.
* **VPC Service Controls:** A service perimeter that protects Cloud KMS in your project can block Anthropic. Add Anthropic to an access level on the perimeter, or exclude the key's project from it.
* **Domain restricted sharing:** The `constraints/iam.allowedPolicyMemberDomains` org policy blocks the binding for Anthropic's service account. To check that the binding is there, run `gcloud kms keys get-iam-policy <your-key-name> --project=<your-project-id> --location=<region> --keyring=<your-keyring-name>`. To allow it, see [Anthropic service account email](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#anthropic-service-account-email).
* **Disabled or destroyed key version:** Confirm that the key's primary version is enabled.

## Terraform

To create the key with Terraform, use the `google_kms_key_ring`, `google_kms_crypto_key`, and `google_kms_crypto_key_iam_member` resources from the `google` provider.

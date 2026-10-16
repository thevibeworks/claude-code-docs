---
title: Configure AWS KMS for CMEK
url: https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms
description: Use AWS KMS to provide an encryption key for your organization.
---

Let Claude Code set up this feature for you

```text
/claude-api help me configure a customer-managed encryption key with AWS KMS
```

This guide shows how to use an [AWS KMS](https://aws.amazon.com/kms/) key as a [customer-managed encryption key (CMEK)](https://platform.claude.com/docs/en/manage-claude/cmek) for your Anthropic organization.

<Warning>
  Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](https://platform.claude.com/docs/en/manage-claude/cmek) before you begin.
</Warning>

<Note>
  **Claude Platform on AWS:** If your Claude Console sidebar shows **Account managed by AWS**, your organization is on Claude Platform on AWS. Follow [Set up CMEK on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws) instead.
</Note>

## Prerequisites

* An AWS account with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
* To create the key from the command line, the [AWS CLI](https://aws.amazon.com/cli/) installed and authenticated.
* To register the key through the API, an Anthropic Admin API key for your organization.

## Amazon Resource Name (ARN) for Anthropic

The key policy in this guide gives the following Anthropic IAM role access to your key:

```text wrap
arn:aws:iam::915198916910:role/anthropic-cmek-client-us
```

<Warning>
  Use only this published ARN. Never trust an identifier provided over email, chat, or any onboarding channel.
</Warning>

## Encryption key setup

### Prepare the key policy

Copy this policy into a text editor:

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

Replace the two placeholders:

* **`<AWS_ACCOUNT_ID>`:** your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html). To print it with the AWS CLI, run `aws sts get-caller-identity --query Account --output text`.
* **`<ORGANIZATION_UUID>`:** your Anthropic organization ID

<Note>
  **Finding your organization ID:** Use the bare UUID, not the `org_`-prefixed ID. Copy it from one of these places:

  * **Claude Console:** the **Organization ID** field on the [Organization](https://platform.claude.com/settings/organization) page (`platform.claude.com/settings/organization`)
  * **claude.ai:** the **Organization ID** field under **Organization settings > Organization**
  * **Admin API:** the `id` field from the [Organization Info](https://platform.claude.com/docs/en/api/organization/retrieve) endpoint
</Note>

Don't remove the `kms:EncryptionContext:anthropic:org_uuid` condition, or validation fails. To share one key among several Anthropic organizations, list each organization ID in it. To limit the key to specific workspaces, see the [optional workspace condition](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#workspace-condition).

<Warning>
  **Keys that already protect data:** If the key is already configured for CMEK, add this fourth statement so that Anthropic can still decrypt the existing data. In its condition, list the [compartment ID](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#compartment-id) of every workspace the key is or was attached to.

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
</Warning>

### Create the key

Create the key in a [US region](https://platform.claude.com/docs/en/manage-claude/cmek#availability-and-regions). For the lowest latency, use `us-east-2`.

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
          ![AWS KMS Create key wizard on the Configure key step, with Symmetric key type, Encrypt and decrypt key usage, and Single-Region key selected.](https://platform.claude.com/docs/images/cmek/aws-configure-key.png)
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
        In **Customer managed keys**, open the new key and copy its ARN. You need the ARN to register the key.
      </Step>
    </Steps>

    To replace the key policy on a key that already exists:

    1. Open the key and click the **Key policy** tab.
    2. If you see **Switch to policy view**, click it.
    3. Click **Edit**.
    4. Replace the JSON with your key policy.
    5. Click **Save changes**.
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

    Copy `KeyMetadata.Arn` from the output. You need it to register the key.
  </Tab>
</Tabs>

<Note>
  **Optional:** To limit the key to specific workspaces, replace the `AllowAnthropicCMEKCrypto` statement in the key policy with this one. List one compartment ID for each workspace.

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

  Add each workspace's compartment ID before you attach the key to it. For a new workspace:

  1. Create the workspace without the key.
  2. Add its compartment ID to the policy.
  3. Attach the key.

  **Finding your compartment ID:** In the Claude Console, go to the [Data retention](https://platform.claude.com/settings/privacy) page (`platform.claude.com/settings/privacy`). Select the workspace from the dropdown menu at the top of the page. The ID is under **Encryption key**, in the **Compartment ID** field. You can also read the `compartment_id` field returned by the [Get Workspace](https://platform.claude.com/docs/en/api/organization/workspaces/retrieve) endpoint.
</Note>

## Register the key with Anthropic

Validating the key adds expected access-denied errors to CloudTrail. If you alert on these errors, see [Expected errors in CloudTrail](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#expected-errors-in-cloud-trail) first.

<Tabs>
  <Tab title="Claude Platform">
    <Tabs>
      <Tab title="Claude Console">
        <Steps>
          <Step title="Open the encryption key settings">
            In the Claude Console, go to the [Data retention](https://platform.claude.com/settings/privacy#encryption-keys) page (`platform.claude.com/settings/privacy`). If you don't see **Encryption keys**, select **Organization** from the dropdown menu at the top of the page.
          </Step>

          <Step title="Add the key">
            Under **Encryption keys**, click **Add key**. Enter a **Display name** and select **AWS KMS**. Click **Continue**.
          </Step>

          <Step title="Enter the key ARN">
            The dialog box shows the **Organization ID for the key policy**. Check that your [key policy](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy) contains this ID. Paste the key ARN into **KMS key ARN** and click **Add**.
          </Step>

          <Step title="Validate the key">
            In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#troubleshoot-validation) for common causes.
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
            Replace `<friendly-name>` with a display name and `<key-arn-from-create-key-step>` with the key ARN.

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
                    "type": "aws",
                    "kms_arn": "<key-arn-from-create-key-step>"
                  }
                }'
              ```

              ```bash CLI
              ant organization:external-keys create <<'YAML'
              display_name: "<friendly-name>"
              geo: us
              provider_config:
                type: aws
                kms_arn: "<key-arn-from-create-key-step>"
              YAML
              ```

              ```python Python
              client = anthropic.Anthropic()

              external_key = client.organization.external_keys.create(
                  display_name="<friendly-name>",
                  geo="us",
                  provider_config={"type": "aws", "kms_arn": "<key-arn-from-create-key-step>"},
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
                  type: "aws",
                  kms_arn: "<key-arn-from-create-key-step>"
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
                  ProviderConfig = new AwsExternalKeyConfig
                  {
                      KmsArn = "<key-arn-from-create-key-step>"
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
              		OfAWS: &anthropic.AWSExternalKeyConfigParam{
              			KMSARN: "<key-arn-from-create-key-step>",
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
              import com.anthropic.models.organization.externalkeys.AwsExternalKeyConfig;
              import com.anthropic.models.organization.externalkeys.ExternalKeyCreateParams;

              void main() {
                  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

                  var params = ExternalKeyCreateParams.builder()
                      .displayName("<friendly-name>")
                      .geo(ExternalKeyCreateParams.Geo.US)
                      .providerConfig(AwsExternalKeyConfig.builder()
                          .kmsArn("<key-arn-from-create-key-step>")
                          .build())
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
                      'type' => 'aws',
                      'kmsARN' => '<key-arn-from-create-key-step>',
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
                  type: :aws,
                  kms_arn: "<key-arn-from-create-key-step>"
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

            If validation fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#troubleshoot-validation).
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
        Click **Add key**. Enter a **Display name** and select **AWS KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.
      </Step>

      <Step title="Enter the key ARN">
        The dialog box shows the **Organization ID for the key policy**. Check that your [key policy](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#key-policy) contains this ID. Paste the key ARN into **KMS key ARN** and click **Add**.
      </Step>

      <Step title="Confirm that validation passed">
        When the check passes, **Encryption key configured** appears, and your organization is CMEK-protected from then on. If the check fails, see [Troubleshoot validation](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#troubleshoot-validation).
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Troubleshoot validation

If validation fails, common causes are:

* **Wrong organization ID:** Make sure the `org_uuid` condition lists your bare organization ID, not the `org_`-prefixed ID.
* **Encryption context mismatch:** If the policy has a `kms:EncryptionContext:anthropic:compartment_uuid` condition, make sure it lists the [compartment ID](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#compartment-id) of each workspace the key is attached to. On an older key, the compartment statement might still allow `kms:Encrypt`. In that case, keep the all-zeros value (`00000000-0000-0000-0000-000000000000`) in the list too.
* **Resource control policies (RCPs):** Some RCPs deny KMS operations when `aws:PrincipalOrgID` does not match your AWS organization. An RCP like this blocks Anthropic's role. Add an exception to it for this key or for Anthropic's role ARN. Service control policies do not apply here.
* **Access granted through IAM instead of the key policy:** Grant Anthropic's role access in the key policy itself, not through an IAM policy in your account. To check the key policy, run `aws kms get-key-policy --region <REGION> --key-id <KEY_ARN> --policy-name default`.
* **Region mismatch:** Confirm that the key is in a US region.

### Expected errors in CloudTrail

Anthropic validates the key whenever you verify it, attach it to a workspace, or view it in the Claude Enterprise settings. Each validation adds four access-denied errors to CloudTrail. These errors are expected.

To filter them out, match all three of these values:

* `requestParameters.encryptionContext.associatedData`: `Y21lay12YWxpZGF0aW9u`
* `userIdentity.accountId`: `915198916910`
* `resources.ARN`: `arn:aws:kms:<REGION>:<AWS_ACCOUNT_ID>:key/<KEY_ID>`

The first value alone isn't enough, because any caller can set it.

## Terraform

To create the key with Terraform, use the `aws_kms_key` and `aws_kms_alias` resources from the `aws` provider.

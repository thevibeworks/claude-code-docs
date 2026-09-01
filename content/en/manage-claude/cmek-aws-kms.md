---
title: Configure AWS KMS for CMEK
url: https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms
description: Use AWS KMS to provide an encryption key for your organization.
---

```bash Configure with the /claude-api skill in Claude Code
claude "/claude-api help me configure a customer-managed encryption key with AWS KMS"
```

This guide walks through configuring an [AWS KMS](https://aws.amazon.com/kms/) key as a [customer-managed encryption key (CMEK)](https://platform.claude.com/docs/en/manage-claude/cmek) for your Anthropic organization.

<Warning>
  Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](https://platform.claude.com/docs/en/manage-claude/cmek) before you begin.
</Warning>

<Note>
  **Claude Platform on AWS:** On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), your key policy grants access to an AWS service principal instead of Anthropic's IAM role, there is no separate validation step, and you register and attach the key in the Claude Console. Follow [Set up CMEK on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#claude-platform-on-aws) on this page instead of the steps in the next sections.
</Note>

## Prerequisites

* An AWS account with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
* An Anthropic Admin API key for your organization.
* The [AWS CLI](https://aws.amazon.com/cli/) installed and authenticated.

## Amazon Resource Name (ARN) for Anthropic

To have Anthropic use your encryption key, you must give Anthropic's IAM role a KMS key it can use for encrypting data. The ARN for Anthropic CMEK is:

```text wrap
arn:aws:iam::915198916910:role/anthropic-cmek-client-us
```

<Warning>
  Use only this published ARN. Never trust an identifier provided over email, chat, or any onboarding channel.
</Warning>

## Encryption key setup

<Steps>
  <Step title="Create the KMS key with a cross-account key policy">
    The key policy grants Anthropic's IAM role cross-account access. Three statements are required:

    1. **Account root admin:** the standard KMS pattern. Your account retains full admin control.
    2. **Anthropic encrypt and decrypt:** the `kms:Encrypt` and `kms:Decrypt` actions, which Anthropic uses to encrypt and decrypt the data keys that protect your workspace data (envelope encryption).
    3. **Anthropic describe:** the metadata read Anthropic performs at startup. It is granted separately because `DescribeKey` has no `EncryptionContext` parameter, so an `EncryptionContext` condition on this action would always deny.

    ```bash
    export YOUR_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

    aws kms create-key \
      --region <region> \
      --description "Anthropic CMEK" \
      --key-usage ENCRYPT_DECRYPT \
      --policy "{
        \"Version\": \"2012-10-17\",
        \"Statement\": [
          {
            \"Sid\": \"AccountRootAdmin\",
            \"Effect\": \"Allow\",
            \"Principal\": {\"AWS\": \"arn:aws:iam::${YOUR_ACCOUNT}:root\"},
            \"Action\": \"kms:*\",
            \"Resource\": \"*\"
          },
          {
            \"Sid\": \"AllowAnthropicCMEKCrypto\",
            \"Effect\": \"Allow\",
            \"Principal\": {\"AWS\": \"arn:aws:iam::915198916910:role/anthropic-cmek-client-us\"},
            \"Action\": [\"kms:Encrypt\", \"kms:Decrypt\"],
            \"Resource\": \"*\",
            \"Condition\": {
              \"StringEquals\": {
                \"kms:EncryptionContext:anthropic:compartment_uuid\": [
                  \"00000000-0000-0000-0000-000000000000\",
                  \"<compartment-uuid>\"
                ]
              }
            }
          },
          {
            \"Sid\": \"AllowAnthropicCMEKDescribe\",
            \"Effect\": \"Allow\",
            \"Principal\": {\"AWS\": \"arn:aws:iam::915198916910:role/anthropic-cmek-client-us\"},
            \"Action\": \"kms:DescribeKey\",
            \"Resource\": \"*\"
          }
        ]
      }"
    ```

    Capture `KeyMetadata.Arn` from the output. You need it when you register the key in the next step.

    The `EncryptionContext` condition is recommended but optional. Anthropic always includes your workspace's compartment ID in the encryption context, so ciphertext is cryptographically bound to that compartment regardless. Adding the condition provides defense-in-depth at the IAM layer. To start without it, omit the `Condition` block from the `AllowAnthropicCMEKCrypto` statement and add it later with `kms:PutKeyPolicy`.

    <Note>
      **Finding your compartment ID:** Where to find your compartment ID differs between Claude Platform and Claude Enterprise. See the **Claude Platform** and **Claude Enterprise** tabs under **Register the key with Anthropic**.
    </Note>

    You can also create the key from the AWS Console. Choose a symmetric key with the encrypt and decrypt key usage, a single-region key, and KMS key material origin. The Create-key wizard commits a key policy at its **Review** step: If you add Anthropic's account ID `915198916910` under key usage permissions there, the generated policy grants the whole Anthropic account broader actions (such as `kms:ReEncrypt*` and `kms:GenerateDataKey*`) with no `EncryptionContext` condition, and validation would still succeed against it. To avoid leaving an over-permissive key, finish the wizard with administrative permissions only, then open the key's **Key policy** tab and replace the JSON with the role-scoped policy shown earlier (the three statements scoped to the `anthropic-cmek-client-us` role, with the `EncryptionContext` condition).

    <Frame caption="Configure key: symmetric, encrypt and decrypt, single-region key.">
      ![AWS KMS Create key wizard on the Configure key step, with Symmetric key type, Encrypt and decrypt key usage, and Single-Region key selected.](https://platform.claude.com/docs/images/cmek/aws-configure-key.png)
    </Frame>

    <Frame caption="Add an alias and description for the key.">
      ![AWS KMS Add labels step with an alias of anthropic-cmek and a description of Anthropic CMEK.](https://platform.claude.com/docs/images/cmek/aws-add-labels.png)
    </Frame>

    <Frame caption="Define key administrative permissions (optional). Your account retains full admin control.">
      ![AWS KMS Define key administrative permissions step listing IAM roles that can administer the key.](https://platform.claude.com/docs/images/cmek/aws-admin-permissions.png)
    </Frame>

    <Frame caption="Do not add Anthropic's account ID here. This wizard step produces an over-permissive policy. Leave usage permissions empty and edit the Key policy JSON after creation (see the preceding key policy).">
      ![AWS KMS Define key usage permissions step with Anthropic's account ID entered under Other AWS accounts.](https://platform.claude.com/docs/images/cmek/aws-usage-permissions.png)
    </Frame>
  </Step>
</Steps>

## Register the key with Anthropic

How you register the key depends on which product you use.

<Tabs>
  <Tab title="Claude Platform">
    <Note>
      **Claude Platform on AWS:** The principal, key policy, and registration flow differ, and there is no separate validation step. Follow [Set up CMEK on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#claude-platform-on-aws) instead of this tab.
    </Note>

    <Note>
      **Finding your compartment ID:** Each workspace has a compartment ID that scopes its CMEK data. Find it in the Claude Console under **Workspace > Security**, under **Encryption key** (the **Compartment ID** field), or read the `compartment_id` field returned by the [Get Workspace](https://platform.claude.com/docs/en/api/admin-api/workspaces/get-workspace) endpoint. Substitute that value for `<compartment-uuid>` in the preceding key policy.

      Key validation always sends the all-zeros compartment UUID (`00000000-0000-0000-0000-000000000000`) as the encryption context, because validation runs before the key is attached to any workspace. Live traffic sends the compartment ID of each attached workspace.

      Any `EncryptionContext` condition must allow the all-zeros value plus the compartment ID of every workspace the key is attached to. Validation also runs again whenever key setup is re-run, so keep the all-zeros entry in place permanently.

      To attach the key to an additional workspace, add that workspace's compartment ID to the condition with `kms:PutKeyPolicy` before attaching.
    </Note>

    <Steps>
      <Step title="Register the key with Anthropic">
        Create an external key configuration through the Admin API.

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
          ant beta:organization:external-keys create <<'YAML'
          display_name: "<friendly-name>"
          geo: us
          provider_config:
            type: aws
            kms_arn: "<key-arn-from-create-key-step>"
          YAML
          ```

          ```python Python
          client = anthropic.Anthropic()

          external_key = client.beta.organization.external_keys.create(
              display_name="<friendly-name>",
              geo="us",
              provider_config={"type": "aws", "kms_arn": "<key-arn-from-create-key-step>"},
          )

          print(f"id: {external_key.id}")
          print(f"display_name: {external_key.display_name}")
          ```

          ```typescript TypeScript
          const client = new Anthropic();

          const externalKey = await client.beta.organization.externalKeys.create({
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
          using Anthropic.Models.Beta.Organization.ExternalKeys;

          AnthropicClient client = new();

          var externalKey = await client.Beta.Organization.ExternalKeys.Create(new()
          {
              DisplayName = "<friendly-name>",
              Geo = Geo.Us,
              ProviderConfig = new BetaAwsExternalKeyConfig
              {
                  KmsArn = "<key-arn-from-create-key-step>"
              }
          });

          Console.WriteLine($"id: {externalKey.ID}");
          Console.WriteLine($"display_name: {externalKey.DisplayName}");
          ```

          ```go Go
          client := anthropic.NewClient()

          externalKey, err := client.Beta.Organization.ExternalKeys.New(context.Background(), anthropic.BetaOrganizationExternalKeyNewParams{
          	DisplayName: anthropic.String("<friendly-name>"),
          	Geo:         anthropic.BetaOrganizationExternalKeyNewParamsGeoUs,
          	ProviderConfig: anthropic.BetaOrganizationExternalKeyNewParamsProviderConfigUnion{
          		OfAWS: &anthropic.BetaAWSExternalKeyConfigParam{
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
          import com.anthropic.models.beta.organization.externalkeys.BetaAwsExternalKeyConfig;
          import com.anthropic.models.beta.organization.externalkeys.ExternalKeyCreateParams;

          void main() {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              var params = ExternalKeyCreateParams.builder()
                  .displayName("<friendly-name>")
                  .geo(ExternalKeyCreateParams.Geo.US)
                  .providerConfig(BetaAwsExternalKeyConfig.builder()
                      .kmsArn("<key-arn-from-create-key-step>")
                      .build())
                  .build();
              var externalKey = client.beta().organization().externalKeys().create(params);

              IO.println("id: " + externalKey.id());
              IO.println("display_name: " + externalKey.displayName().orElseThrow());
          }
          ```

          ```php PHP
          use Anthropic\Beta\Organization\ExternalKeys\ExternalKeyCreateParams\Geo;
          // ...

          $client = new Client();

          $externalKey = $client->beta->organization->externalKeys->create(
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

          external_key = client.beta.organization.external_keys.create(
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

        The response contains the external key ID:

        ```json
        {
          "type": "external_key",
          "id": "ekey_<id>",
          "display_name": "<friendly-name>"
        }
        ```
      </Step>

      <Step title="Validate the key">
        Trigger an encrypt and decrypt round-trip against your key.

        <CodeGroup>
          ```bash cURL
          curl -sS -X POST "https://api.anthropic.com/v1/organizations/external_keys/ekey_<id>/validate" \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "anthropic-version: 2023-06-01"
          ```

          ```bash CLI
          ant beta:organization:external-keys validate --external-key-id "ekey_<id>"
          ```

          ```python Python
          client = anthropic.Anthropic()

          validation = client.beta.organization.external_keys.validate("ekey_<id>")

          print(f"status: {validation.status}")
          print(f"error: {validation.error}")
          ```

          ```typescript TypeScript
          const client = new Anthropic();

          const validation = await client.beta.organization.externalKeys.validate("ekey_<id>");

          console.log(`status: ${validation.status}`);
          console.log(`error: ${validation.error}`);
          ```

          ```csharp C#
          AnthropicClient client = new();

          var validation = await client.Beta.Organization.ExternalKeys.Validate("ekey_<id>");

          Console.WriteLine($"status: {validation.Status.Raw()}");
          Console.WriteLine($"error: {validation.Error}");
          ```

          ```go Go
          client := anthropic.NewClient()

          validation, err := client.Beta.Organization.ExternalKeys.Validate(context.Background(), "ekey_<id>")
          if err != nil {
          	log.Fatal(err)
          }

          fmt.Printf("status: %s\n", validation.Status)
          fmt.Printf("error: %s\n", validation.Error)
          ```

          ```java Java
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          var validation = client.beta().organization().externalKeys().validate("ekey_<id>");

          IO.println("status: " + validation.status().asString());
          IO.println("error: " + validation.error().orElse(""));
          ```

          ```php PHP
          $client = new Client();

          $validation = $client->beta->organization->externalKeys->validate(
              externalKeyID: 'ekey_<id>',
          );

          echo "status: {$validation->status}\n";
          echo "error: {$validation->error}\n";
          ```

          ```ruby Ruby
          client = Anthropic::Client.new

          external_key_id = "ekey_<id>"
          validation = client.beta.organization.external_keys.validate(external_key_id)

          puts "status: #{validation.status}"
          puts "error: #{validation.error}"
          ```
        </CodeGroup>

        A successful response looks like this:

        ```json
        { "type": "external_key_validation", "status": "success", "error": null }
        ```

        If validation fails, common causes are:

        * **Encryption context mismatch:** Validation fails while data traffic works (or the reverse) with an opaque `AccessDeniedException` when a `kms:EncryptionContext:anthropic:compartment_uuid` condition allows only one of the two values Anthropic sends. Validation sends the all-zeros UUID (`00000000-0000-0000-0000-000000000000`); live traffic sends the attached workspace's compartment ID. Confirm the condition lists both. To rule the condition out entirely, temporarily remove the `Condition` block from the `AllowAnthropicCMEKCrypto` statement and re-validate.
        * **Resource control policies (RCPs):** If your AWS organization has an RCP that denies KMS operations when `aws:PrincipalOrgID` does not match your org, it blocks Anthropic's cross-account role. The RCP needs a carve-out for this key or for Anthropic's role ARN. Service control policies do not apply here, because they do not evaluate for external principals calling through resource-based policies.
        * **Access granted through IAM instead of the key policy:** Cross-account KMS access must be granted in the key policy itself, not through an IAM policy in your account. Check with `aws kms get-key-policy --key-id <id> --policy-name default`.
        * **Region mismatch:** Confirm the key's region is one Anthropic operates in for the geo tier you configured.
      </Step>

      <Step title="Attach the key to a workspace">
        Once the key is validated, attach it to a new workspace before you send any requests to that workspace. For a workspace that already receives requests, the key can take [up to a day to take effect](https://platform.claude.com/docs/en/manage-claude/cmek#how-it-works).

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
          ant beta:organization:workspaces update \
            --workspace-id "<workspace-id>" \
            --external-key-id "ekey_<id>"
          ```

          ```python Python
          client = anthropic.Anthropic()

          workspace = client.beta.organization.workspaces.update(
              "<workspace-id>", external_key_id="ekey_<id>"
          )

          print(f"id: {workspace.id}")
          print(f"external_key_id: {workspace.external_key_id}")
          ```

          ```typescript TypeScript
          const client = new Anthropic();

          const workspace = await client.beta.organization.workspaces.update("<workspace-id>", {
            external_key_id: "ekey_<id>"
          });

          console.log(`id: ${workspace.id}`);
          console.log(`external_key_id: ${workspace.external_key_id}`);
          ```

          ```csharp C#
          AnthropicClient client = new();

          var workspace = await client.Beta.Organization.Workspaces.Update("<workspace-id>", new()
          {
              ExternalKeyID = "ekey_<id>"
          });

          Console.WriteLine($"id: {workspace.ID}");
          Console.WriteLine($"external_key_id: {workspace.ExternalKeyID}");
          ```

          ```go Go
          client := anthropic.NewClient()

          workspace, err := client.Beta.Organization.Workspaces.Update(
          	context.Background(),
          	"<workspace-id>",
          	anthropic.BetaOrganizationWorkspaceUpdateParams{
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
          import com.anthropic.models.beta.organization.workspaces.WorkspaceUpdateParams;

          void main() {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              var params = WorkspaceUpdateParams.builder()
                  .externalKeyId("ekey_<id>")
                  .build();
              var workspace = client.beta().organization().workspaces().update("<workspace-id>", params);

              IO.println("id: " + workspace.id());
              IO.println("external_key_id: " + workspace.externalKeyId().orElseThrow());
          }
          ```

          ```php PHP
          $client = new Client();

          $workspace = $client->beta->organization->workspaces->update(
              workspaceID: '<workspace-id>',
              externalKeyID: 'ekey_<id>',
          );

          echo "id: {$workspace->id}\n";
          echo "external_key_id: {$workspace->externalKeyID}\n";
          ```

          ```ruby Ruby
          client = Anthropic::Client.new

          workspace_id = "<workspace-id>"
          workspace = client.beta.organization.workspaces.update(
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

  <Tab title="Claude Enterprise">
    In [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), open **Encryption keys**, then click **Add key**. Choose **AWS** and click **Continue**, then paste the Key ARN from the previous step and click **Add**. Anthropic validates the key with an encrypt and decrypt round-trip. Once it shows as verified, your organization is CMEK-protected from that point forward.

    The key details step of this flow displays your organization's **Compartment ID** with a copy button. Substitute that value for `<compartment-uuid>` in the key policy (see the Create the KMS key step under Encryption key setup); you can open the flow to copy the ID before you create the key. After setup, the ID remains visible on the key under **Encryption keys**.

    On Claude Enterprise, CMEK applies to the whole organization, so there is no separate workspace attach step, and an organization can have only one key.
  </Tab>
</Tabs>

## Set up CMEK on Claude Platform on AWS

On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), CMEK uses AWS KMS keys only, and setup differs from the preceding sections in these ways:

* **Principal:** Your key policy grants access to the AWS service principal `aws-external-anthropic.amazonaws.com`. Anthropic's IAM role and account ID are not used, so the [ARN for Anthropic](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#amazon-resource-name-arn-for-anthropic) does not apply.
* **Key requirements:** The key must be a symmetric KMS key with encrypt and decrypt usage, single-region, and in the same AWS account and region as the workspace you attach it to. Cross-account keys are not supported: the key must be in the AWS account that hosts your organization. Multi-region keys (key IDs that begin with `mrk-`) and alias ARNs are rejected when you register the key; use the key ARN.
* **No separate validation step:** Apart from those checks on the key ARN at registration, the key is validated when you attach it to a workspace. The attach call performs an encrypt/decrypt round against the key with that workspace's compartment ID as the encryption context, so a key policy problem surfaces at attach time rather than at registration. Unlike the Claude Platform policy earlier on this page, an `EncryptionContext` condition therefore needs no all-zeros entry.
* **Where you manage keys:** Register and attach keys in the Claude Console, signed in through AWS with the Admin role. The external key endpoints are also available on Claude Platform on AWS, authorized through [IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys); there, a key is identified by its KMS key ARN rather than an `ekey_` ID.

<Warning>
  Use only this published service principal name. Never trust an identifier provided over email, chat, or any onboarding channel.
</Warning>

### Prerequisites

* The AWS account that hosts your Claude Platform on AWS organization, with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
* The **Admin** role in the Claude Console for Claude Platform on AWS. See [Using the Claude Console](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#using-the-claude-console).
* For the IAM principal you sign in to the Claude Console with: besides `aws-external-anthropic:AssumeConsole`, the [IAM actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys) for the operations you perform there, because the Encryption keys page and key attachment go through the AWS gateway. Registering a key is `RegisterKey` (with `ListKeys` and `GetKey` to view registrations), and attaching one is `UpdateWorkspace` or `CreateWorkspace`. The external key actions (and `CreateWorkspace`) are account-scoped, so grant them on `Resource: "*"`; a policy limited to workspace ARNs does not include them.
* For the IAM principal that attaches the key to a workspace (the identity you signed in to the Claude Console with): `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key. Your principal's access to the key is checked when you attach it, in addition to the service principal's.
* Optional, for the key picker in the Claude Console: `kms:ListKeys` and `kms:DescribeKey` for the principal you sign in with. Without them, paste the key ARN instead.

### Create the KMS key

The key policy has three statements: your account's root admin statement; a statement that lets the Claude Platform on AWS service principal encrypt, decrypt, and generate data keys; and a separate statement for `kms:DescribeKey`. Both service-principal statements carry a recommended `aws:SourceArn` condition: the service calls your key on behalf of a specific workspace and passes that [workspace's ARN](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#service-details) as the source ARN, so the pattern shown limits the grant to workspaces in your own AWS account. `DescribeKey` is granted separately because it has no `EncryptionContext` parameter, so an `EncryptionContext` condition on that action would always deny.

If you plan to use the optional `EncryptionContext` condition shown here, create the workspace first (without a key) and copy its compartment ID from the Claude Console under **Workspace > Security**, under **Encryption key** (the **Compartment ID** field), or from the `compartment_id` field returned by the [Get Workspace](https://platform.claude.com/docs/en/api/admin-api/workspaces/get-workspace) endpoint. Substitute it for `<compartment-uuid>`. Otherwise, delete the `StringEquals` entry from that statement's `Condition` block and keep the `ArnLike` entry.

```bash
export YOUR_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

aws kms create-key \
  --region <workspace-region> \
  --description "Anthropic CMEK (Claude Platform on AWS)" \
  --key-usage ENCRYPT_DECRYPT \
  --policy "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [
      {
        \"Sid\": \"AccountRootAdmin\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"AWS\": \"arn:aws:iam::${YOUR_ACCOUNT}:root\"},
        \"Action\": \"kms:*\",
        \"Resource\": \"*\"
      },
      {
        \"Sid\": \"AllowClaudePlatformOnAWSCrypto\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"aws-external-anthropic.amazonaws.com\"},
        \"Action\": [\"kms:Encrypt\", \"kms:Decrypt\", \"kms:GenerateDataKey\"],
        \"Resource\": \"*\",
        \"Condition\": {
          \"ArnLike\": {
            \"aws:SourceArn\": \"arn:aws:aws-external-anthropic:*:${YOUR_ACCOUNT}:workspace/*\"
          },
          \"StringEquals\": {
            \"kms:EncryptionContext:anthropic:compartment_uuid\": [
              \"<compartment-uuid>\"
            ]
          }
        }
      },
      {
        \"Sid\": \"AllowClaudePlatformOnAWSDescribe\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"aws-external-anthropic.amazonaws.com\"},
        \"Action\": \"kms:DescribeKey\",
        \"Resource\": \"*\",
        \"Condition\": {
          \"ArnLike\": {
            \"aws:SourceArn\": \"arn:aws:aws-external-anthropic:*:${YOUR_ACCOUNT}:workspace/*\"
          }
        }
      }
    ]
  }"
```

Capture `KeyMetadata.Arn` from the output. You need it when you register the key.

Both conditions are optional hardening, and they compose. The `aws:SourceArn` condition can be written before any workspace exists; to pin the key to particular workspaces instead of your whole account, list their full workspace ARNs in place of the wildcard pattern, and to start without it, delete the `ArnLike` entry from both service-principal statements (removing a `Condition` block that this leaves empty). The `EncryptionContext` condition is also optional. Every encrypt, decrypt, and data-key call made for a workspace, including the attach-time check, carries that workspace's compartment ID as `anthropic:compartment_uuid`, so the condition lists the compartment ID of each workspace you attach the key to and needs no all-zeros entry. Adding it binds the key to the workspaces you list at the IAM layer as well. Because a compartment ID exists only once its workspace exists, the order is: create the workspace, put its compartment ID in the condition (at key creation, or later with `kms:PutKeyPolicy`), then attach the key. Before attaching the key to each additional workspace, add that workspace's compartment ID the same way. To start without it, delete the `StringEquals` entry from the `AllowClaudePlatformOnAWSCrypto` statement's `Condition` block; if you add it later, include the compartment ID of every workspace the key is already attached to.

You can also create the key from the AWS Console: choose a symmetric key with the encrypt and decrypt key usage, a single-region key, and KMS key material origin, in the workspace's region. Leave key usage permissions empty in the Create-key wizard, then open the key's **Key policy** tab and replace the JSON with the policy shown here.

### Register and attach the key

<Steps>
  <Step title="Register the key">
    In the Claude Console, open **Settings > Encryption keys** and click **Add key**. Enter a display name, then choose the key from the key picker or choose **Enter ARN manually** and paste the key ARN, and click **Add**. The key must be in the AWS account that hosts your organization; cross-account keys are not supported. The picker lists the enabled, customer-managed, symmetric, single-region keys in your account in one of your organization's regions; for a key the picker doesn't list, enter the ARN. It lists keys only if the principal you signed in with can call `kms:ListKeys` and `kms:DescribeKey`.
  </Step>

  <Step title="Attach the key to a workspace">
    Attach the key to a new workspace before you send any requests to that workspace. For a workspace that already receives requests, the key can take [up to a day to take effect](https://platform.claude.com/docs/en/manage-claude/cmek#how-it-works). In the Claude Console, open the workspace and, under **Security**, select the key in **Encryption key**, save, and confirm. You can also select a key when you create a workspace in the Claude Console, but only if your key policy does not yet name specific workspaces (no `EncryptionContext` condition, and the account-wide `aws:SourceArn` pattern rather than individual workspace ARNs), because the workspace's ID and compartment ID are assigned at creation. Once attached, a workspace's key can't be changed.

    This is when the key is validated: the attach call checks your principal's access to the key and performs an encrypt/decrypt round against it with the workspace's compartment ID as the encryption context, so a problem with either the key policy or your principal's permissions surfaces as an error on that call. If the attach fails with a KMS access error, check the following:

    * The key policy names the `aws-external-anthropic.amazonaws.com` service principal and grants `kms:Encrypt`, `kms:Decrypt`, and `kms:GenerateDataKey`, plus `kms:DescribeKey` in a separate statement that has no `EncryptionContext` condition.
    * The `aws:SourceArn` condition matches this workspace's ARN (your account ID, and the workspace if you listed specific ARNs), and any `EncryptionContext` condition includes this workspace's compartment ID.
    * The key is enabled, single-region, and in the same AWS account and region as the workspace.
    * The principal you are signed in as has `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key.
    * No service control policy or resource control policy in your AWS organization prevents the service principal or your principal from using the key.
    * If the policy looks right and the attach still fails, find the denied `kms:` event in CloudTrail in the key's account (it shows the calling principal and, for cryptographic calls, the encryption context), then retry with the `aws:SourceArn` condition temporarily removed to tell a source-ARN mismatch apart from an encryption-context mismatch.
  </Step>
</Steps>

## Terraform

For infrastructure-as-code deployments, the same steps map to the `aws` provider with the `aws_kms_key` and `aws_kms_alias` resources.

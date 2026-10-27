---
title: Add and attach an encryption key with the Admin API
url: https://platform.claude.com/docs/en/manage-claude/cmek-admin-api
description: Create, validate, and attach a customer-managed encryption key with three Admin API calls.
---

These calls work on Claude Platform. On Claude Enterprise or Claude Platform on AWS, follow [your setup page](https://platform.claude.com/docs/en/manage-claude/cmek#set-it-up).

Creating an external key is what **Add key** does in the Claude Console, and validating it is what **Verify** does.

## Before you start

* Customer-managed encryption keys (CMEK) are [turned on for your organization](https://platform.claude.com/docs/en/manage-claude/cmek#availability).
* You have an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys). The samples read it from `ANTHROPIC_API_KEY`.
* You’ve created your key in [AWS KMS](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms#encryption-key-setup), [Google Cloud KMS](https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms#encryption-key-setup), or [Azure Key Vault](https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault#encryption-key-setup), and kept the values the setup steps tell you to copy.
* You have a workspace that [retains data](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention), ideally a new one, because [existing data stays under Anthropic’s key](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect).

## Create, validate, and attach the key

<Steps>
  <Step title="Create the external key">
    <Tabs>
      <Tab title="AWS">
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
      </Tab>

      <Tab title="Google Cloud">
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
      </Tab>

      <Tab title="Azure">
        Replace the placeholders:

        * `<friendly-name>`: a display name
        * `https://<your-vault-name>.vault.azure.net/`: the vault URI
        * `<your-key-name>`: the key name
        * `<your-tenant-id>`: the vault’s tenant ID

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
                "type": "azure",
                "vault_uri": "https://<your-vault-name>.vault.azure.net/",
                "key_name": "<your-key-name>",
                "tenant_id": "<your-tenant-id>"
              }
            }'
          ```

          ```bash CLI
          ant organization:external-keys create <<'YAML'
          display_name: "<friendly-name>"
          geo: us
          provider_config:
            type: azure
            vault_uri: "https://<your-vault-name>.vault.azure.net/"
            key_name: "<your-key-name>"
            tenant_id: "<your-tenant-id>"
          YAML
          ```

          ```python Python
          client = anthropic.Anthropic()

          external_key = client.organization.external_keys.create(
              display_name="<friendly-name>",
              geo="us",
              provider_config={
                  "type": "azure",
                  "vault_uri": "https://<your-vault-name>.vault.azure.net/",
                  "key_name": "<your-key-name>",
                  "tenant_id": "<your-tenant-id>",
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
              type: "azure",
              vault_uri: "https://<your-vault-name>.vault.azure.net/",
              key_name: "<your-key-name>",
              tenant_id: "<your-tenant-id>"
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
              ProviderConfig = new AzureExternalKeyConfigParam
              {
                  VaultUri = "https://<your-vault-name>.vault.azure.net/",
                  KeyName = "<your-key-name>",
                  TenantID = "<your-tenant-id>"
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
          		OfAzure: &anthropic.AzureExternalKeyConfigParam{
          			VaultURI: "https://<your-vault-name>.vault.azure.net/",
          			KeyName:  "<your-key-name>",
          			TenantID: "<your-tenant-id>",
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
          import com.anthropic.models.organization.externalkeys.AzureExternalKeyConfigParam;
          import com.anthropic.models.organization.externalkeys.ExternalKeyCreateParams;

          void main() {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              var params = ExternalKeyCreateParams.builder()
                  .displayName("<friendly-name>")
                  .geo(ExternalKeyCreateParams.Geo.US)
                  .providerConfig(AzureExternalKeyConfigParam.builder()
                      .vaultUri("https://<your-vault-name>.vault.azure.net/")
                      .keyName("<your-key-name>")
                      .tenantId("<your-tenant-id>")
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
                  'type' => 'azure',
                  'vaultURI' => 'https://<your-vault-name>.vault.azure.net/',
                  'keyName' => '<your-key-name>',
                  'tenantID' => '<your-tenant-id>',
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
              type: :azure,
              vault_uri: "https://<your-vault-name>.vault.azure.net/",
              key_name: "<your-key-name>",
              tenant_id: "<your-tenant-id>"
            }
          )

          puts "id: #{external_key.id}"
          puts "display_name: #{external_key.display_name}"
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    The `id` in the response is the external key ID. Copy it for the next two steps.

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

    If `status` is `failure`, the `error` field says why. See [Troubleshoot CMEK](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting).
  </Step>

  <Step title="Attach the key to a workspace">
    <Warning>
      Attaching a key [can’t be undone](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does). If the key is deleted, Anthropic can’t recover the data it protects.
    </Warning>

    Replace `<workspace-id>` with the workspace ID, which starts with `wrkspc_`, and `ekey_<id>` with the external key ID.

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

    The response shows the attached key’s ID in `external_key_id`. If the request is refused, [look up the error](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#refused).
  </Step>
</Steps>

---
title: Set up customer-owned storage
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage
description: Create a bucket in your own cloud account, connect it in the Claude Console, and confirm that your Sealed Safety Data arrives in it.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

With Enterprise Frontier Safeguards (EFS), [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage) keeps a workspace’s Sealed Safety Data in a bucket in your own cloud account.

<Where cloud="aws" label="Claude Platform on AWS">

Start with [Set up Enterprise Frontier Safeguards on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws), and use this page for the bucket itself.

</Where>

<Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">

Start with [Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed).

</Where>

<Where bucket="s3" label="Amazon S3">

## Set up customer-owned storage on Amazon S3

<Where method="console" label="Claude Console">

To set up your storage in Amazon S3, create the resources in your own cloud account, then connect them in the Claude Console:

1. [Update your cloud organization’s policies](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic) to allow access from select external accounts.
2. [Create your bucket and its encryption key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket).
3. [Create the roles](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-roles) that give Anthropic access to your bucket.
4. [Connect your bucket in the Claude Console](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#connect-the-bucket), and test the setup.

Once the test passes, you can [use your bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#use-your-bucket-in-a-workspace).

The **Connect storage** dialog gives you the setup file and tests your setup.

</Where>

<Where method="api" label="Admin API">

You can use the Admin API to register, check, and attach your Amazon S3 bucket for [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage). The Admin API is useful if you want to script your setup or manage many workspaces. Although you can handle most steps through the API, you still need to get a setup file from the Claude Console, as [Get your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#get-the-setup-file) describes.

In the API, an External Storage is Anthropic’s record of your bucket, not your bucket itself.

</Where>

## Before you begin

Make sure that you have the following:

* **An Organization Admin** in the Claude Console, who gets the setup file and connects your bucket.
* **[Access to Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console).** If your organization has it, the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console shows it with a **Configure** button.
* **A cloud account for your bucket.** Anthropic recommends a dedicated account that holds only this bucket and that no other Anthropic organization has used for customer-owned storage. You can also [use an account that holds other buckets](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles).
* **No automation that deletes your bucket, its key, or the roles.** Check with the team that manages the cloud account, because some test accounts have a cleanup job. If something deletes one of them, [your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).

<Warning title="Using a bucket ties it to one Anthropic organization">
  The first time you use a bucket, you tie the bucket, its name, its key, and its roles to this organization. That first use is when you select the bucket for a workspace and save, or create a workspace with it (in the API, the first attach request that succeeds). Treat the tie as permanent. Don’t plan on another Anthropic organization using the bucket, its name, its key, or its roles for customer-owned storage.
</Warning>

<Where method="api" label="Admin API">

### Authenticate your requests

<Tabs>
  <Tab title="cURL">
    Every request on this page sends `anthropic-version: 2026-10-21` and `anthropic-beta: efs-2026-10-01`. Send one of these credentials with each request:

    * **An OAuth bearer token with the `org:admin` scope:** Every request on this page takes one in the `authorization: Bearer` header. To get one, see [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token). The examples read it from `$ANTHROPIC_AUTH_TOKEN`. The token is short-lived: if a request returns a 401 error, get a new one.
    * **A personal key or service account key:** Every request on this page takes one in `x-api-key`. Use a key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). The Admin API refuses a key that’s scoped to a workspace, even for requests on that workspace.
    * **An Admin API key:** It can’t attach or detach storage: those requests return a permission error. The External Storage requests take one in `x-api-key`. To get one, see [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys).

    For a token or a personal or service account key, the account must have the admin role. To use a key, replace the `authorization` header in each example with `x-api-key: $ANTHROPIC_API_KEY`.
  </Tab>

  <Tab title="CLI">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the `ant` CLI sends the key. The token is short-lived: if a request returns a 401 error, get a new one. Leave `ANTHROPIC_WORKSPACE_ID` unset: with it set, a key gets a 400 error on these requests.

    The CLI sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` with `--beta` yourself, as the attach and detach examples show.

    When the API refuses a request, the CLI prints the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="Python">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="TypeScript">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="C#">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="Go">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="Java">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="PHP">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>

  <Tab title="Ruby">
    Use one credential for every request on this page. Use an [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope. Or use a personal key or service account key that isn’t scoped to a workspace (see [Key types](https://platform.claude.com/docs/en/manage-claude/authentication#key-types)). Either way, the account must have the admin role. Don’t use an Admin API key: it can’t attach or detach storage.

    Set `ANTHROPIC_AUTH_TOKEN` to the token or `ANTHROPIC_API_KEY` to the key. Set only one: with both set, the SDK sends the key. The token is short-lived: if a request returns a 401 error, get a new one.

    The SDK sends your credential and the `anthropic-version` header for you. On the External Storage requests, it also sends `anthropic-beta: efs-2026-10-01`. On workspace requests that set `inference_data_privacy`, it doesn’t, so pass `efs-2026-10-01` to the SDK yourself, as the attach and detach examples show.

    When the API refuses a request, the SDK call fails with an error whose text holds the whole response body. Look there for `error.details.error_code`.
  </Tab>
</Tabs>

## Register your bucket

You can register your bucket before you create it. The Claude Console uses the details that you register to fill in [your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#get-the-setup-file).

Tell Anthropic which bucket you plan to use:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/organizations/external_storage \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: efs-2026-10-01" \
    -H "content-type: application/json" \
    -d '{
      "display_name": "Claude retention",
      "provider_config": {
        "type": "aws",
        "account_id": "111122223333",
        "bucket_name": "acme-claude-retention",
        "region": "us-east-2"
      }
    }'
  ```

  ```bash CLI
  ant beta:organization:external-storage create \
    --display-name "Claude retention" \
    --provider-config '{type: aws, account_id: "111122223333", bucket_name: acme-claude-retention, region: us-east-2}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  storage = client.beta.organization.external_storage.create(
      display_name="Claude retention",
      provider_config={
          "type": "aws",
          "account_id": "111122223333",
          "bucket_name": "acme-claude-retention",
          "region": "us-east-2",
      },
  )

  print(f"id: {storage.id}")
  print(f"status: {storage.status.type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const storage = await client.beta.organization.externalStorage.create({
    display_name: "Claude retention",
    provider_config: {
      type: "aws",
      account_id: "111122223333",
      bucket_name: "acme-claude-retention",
      region: "us-east-2"
    }
  });

  console.log(`id: ${storage.id}`);
  console.log(`status: ${storage.status.type}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ExternalStorage;

  AnthropicClient client = new();

  var storage = await client.Beta.Organization.ExternalStorage.Create(new()
  {
      DisplayName = "Claude retention",
      ProviderConfig = new BetaAwsExternalStorageConfigParam
      {
          AccountID = "111122223333",
          BucketName = "acme-claude-retention",
          Region = "us-east-2",
      },
  });

  Console.WriteLine($"id: {storage.ID}");
  Console.WriteLine($"status: {storage.Status.Type.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  storage, err := client.Beta.Organization.ExternalStorage.New(
  	context.Background(),
  	anthropic.BetaOrganizationExternalStorageNewParams{
  		DisplayName: anthropic.String("Claude retention"),
  		ProviderConfig: anthropic.BetaOrganizationExternalStorageNewParamsProviderConfigUnion{
  			OfAWS: &anthropic.BetaAWSExternalStorageConfigParam{
  				AccountID:  "111122223333",
  				BucketName: "acme-claude-retention",
  				Region:     "us-east-2",
  			},
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", storage.ID)
  fmt.Printf("status: %s\n", storage.Status.Type)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.externalstorage.BetaAwsExternalStorageConfigParam;
  import com.anthropic.models.beta.organization.externalstorage.ExternalStorageCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = ExternalStorageCreateParams.builder()
          .displayName("Claude retention")
          .providerConfig(BetaAwsExternalStorageConfigParam.builder()
              .accountId("111122223333")
              .bucketName("acme-claude-retention")
              .region("us-east-2")
              .build())
          .build();
      var storage = client.beta().organization().externalStorage().create(params);

      IO.println("id: " + storage.id());
      IO.println("status: " + storage.status().type());
  }
  ```

  ```php PHP
  $client = new Client();

  $storage = $client->beta->organization->externalStorage->create(
      displayName: 'Claude retention',
      providerConfig: [
          'type' => 'aws',
          'accountID' => '111122223333',
          'bucketName' => 'acme-claude-retention',
          'region' => 'us-east-2',
      ],
  );

  echo "id: {$storage->id}\n";
  echo "status: {$storage->status->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  storage = client.beta.organization.external_storage.create(
    display_name: "Claude retention",
    provider_config: {
      type: :aws,
      account_id: "111122223333",
      bucket_name: "acme-claude-retention",
      region: "us-east-2"
    }
  )

  puts "id: #{storage.id}"
  puts "status: #{storage.status.type}"
  ```
</CodeGroup>

`provider_config` identifies your bucket. Before you send the request, check each field against its constraint:

* `type`: `aws`.
* `account_id`: the 12-digit ID of the AWS account that owns your bucket. [Create and connect your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles) outlines when an account can hold more than one bucket.
* `bucket_name`: globally unique, 3 to 63 lowercase letters, digits, and hyphens, starting and ending with a letter or digit, with no dots. If the setup file creates your bucket, don’t reuse the name of a bucket that you already own.
* `region`: the AWS region your bucket is in, one of the [regions that Anthropic supports](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket). If your bucket isn’t in the region you give, [activating your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-activate) fails.

The response looks like this:

```json
{
  "type": "external_storage",
  "id": "estrg_01SDCCSbTxrXDpWc1phhtcfK",
  "display_name": "Claude retention",
  "provider_config": {
    "type": "aws",
    "account_id": "111122223333",
    "bucket_name": "acme-claude-retention",
    "region": "us-east-2"
  },
  "status": {
    "type": "pending_configuration"
  },
  "setup_template_version": null,
  "created_at": "2026-10-08T17:00:00Z",
  "updated_at": "2026-10-08T17:00:00Z"
}
```

Keep your bucket’s `id`, which starts with `estrg_`, for use in later steps.

The request can fail for reasons such as these:

* **Your organization isn’t approved:** If your organization can make these requests but Anthropic hasn’t approved it to use customer-owned storage, the response tells you to contact your Anthropic account team.
* **Your organization isn’t eligible:** If `error.details.error_code` is `organization_not_eligible`, customer-owned storage isn’t available to your organization.
* **The bucket is already registered:** Anthropic refuses a second registration of the same bucket. To find the existing one, list your External Storage with `GET /v1/organizations/external_storage`.

</Where>

## Create and connect your bucket

To set up customer-owned storage, you need to create three things in your AWS account: your bucket, a KMS key, and IAM roles. With CloudFormation or Terraform, one file creates all of them. With your own tooling, you create each one yourself.

You can put more than one bucket in the same AWS account, even if the buckets belong to different Anthropic organizations. If you do, or if other teams work in the account, keep the following in mind:

* **Separate resources:** Each organization needs a bucket and a KMS key of its own, and each bucket needs a stack of its own or, with Terraform, a folder of its own.
* **Who else works in the account:** Anyone in the AWS account who can create IAM roles, or who has wide Amazon S3 and AWS KMS permissions, can read your Transcripts and Safety Case files, delete files, and cut off Anthropic’s access.

### 1. Update your AWS organization’s policies

In this step, you add an exception for Anthropic’s AWS account to your AWS organization’s policies, so that Anthropic can reach your bucket. You need this step only if your AWS organization has a resource control policy (RCP) that denies AWS STS actions to principals outside the organization. If you skip the change under a policy like that, **Test setup** fails at the IAM roles. Another team often makes the change, so it makes sense to ask for it early.

Anthropic reaches your bucket through IAM roles that you create in a later step. It assumes those roles from its AWS account, `804820989669`, and works in Amazon S3 and AWS KMS as those roles. Under an RCP of that kind, AWS refuses Anthropic’s requests to assume the roles, whatever the roles’ trust policies say.

#### Find out whether the step applies

If you created your AWS account with **Sign up for AWS (new)**, the step applies. That account belongs to an AWS organization whose policies AWS manages, and those policies include an RCP of this kind. The policy is `ManagedAccountResourceControlPolicy`, and the statement is `DenyAnyoneOutsideMyOrgAndAWS`. Before you try to change the policy, read [Managed policies for your organization](https://docs.aws.amazon.com/accounts/latest/reference/scps-and-rcps-for-projects.html) in AWS’s documentation.

For any other account, ask the team that manages your AWS organization’s policies whether an RCP denies AWS STS actions to principals outside the organization. If none does, skip this change and go to [step 2](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket).

#### Add Anthropic’s AWS account to the policy

Ask the team that manages your AWS organization’s policies to add Anthropic’s AWS account to the statement that denies outside principals. In this example, the added line is `aws:PrincipalAccount`, beside the organization ID:

```json
{
  "Sid": "EnforceOrgIdentities",
  "Effect": "Deny",
  "Principal": "*",
  "Action": ["sts:*", "s3:*", "kms:*"],
  "Resource": "*",
  "Condition": {
    "StringNotEqualsIfExists": {
      "aws:PrincipalOrgID": "o-exampleorgid",
      "aws:PrincipalAccount": "804820989669"
    },
    "BoolIfExists": { "aws:PrincipalIsAWSService": "false" }
  }
}
```

If your own statement already lists accounts under `aws:PrincipalAccount`, add `804820989669` to that list instead of adding a second line.

If a workspace on Claude Platform also uses a [customer-managed encryption key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys) in AWS KMS, Anthropic calls that key from account `915198916910`. If your statement denies AWS KMS actions, add that account too.

The added line in the example exempts every principal in Anthropic’s AWS account, for every action and every resource that the statement covers. A narrower exception should be enough, but Anthropic has seen **Test setup** pass only with the account-wide exception. For what a narrower exception has to allow, see [Template reference](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#template-reference).

<Where method="console" label="Claude Console">

#### Check that it worked

To check the change, run **Test setup** in step 4. If a policy blocks Anthropic, the test shows [several failed checks](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).

</Where>

### 2. Create your bucket and its KMS key

In this step, you create the bucket that holds your data, along with its KMS key. The KMS key is the bucket’s default encryption key, so it encrypts what Anthropic writes there. This key is separate from the [customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key) you attach to a workspace.

Create your bucket and its KMS key in one of these AWS regions: `us-east-2`, `us-east-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `ap-northeast-1`, or `ap-southeast-2`. You can’t change a bucket’s region later. Your bucket’s region determines where your cloud provider stores the bucket’s objects. It doesn’t change [where model inference runs](https://platform.claude.com/docs/en/manage-claude/data-residency#inference-geo) or where Anthropic processes your data. Anthropic recommends `us-east-2` because Anthropic reads and writes your bucket from `us-east-2`.

The setup file creates the key and the bucket with these settings:

| Resource | Settings |
| ----- | ----- |
| KMS key | A single-region key in the same AWS account and region as the bucket, with rotation on. Your account administers it. Its policy names neither Anthropic nor the roles. |
| Bucket | Versioning on. Default encryption with the KMS key, named by its key ARN, with S3 Bucket Key on. Public access blocked. ACLs off (`BucketOwnerEnforced`). S3 Object Lock off. |
| Lifecycle rules | The next table lists what they do. |
| S3 Inventory | Daily reports for `slab/` and `media/`. Amazon S3 delivers them under `inventory/` in the same bucket. Two more reports cover the same prefixes under `safeguards-data/` and go under `safeguards-data/inventory/`. |
| Bucket policy | It denies permanent deletes of object versions under `slab/`, refuses requests without TLS, and lets Amazon S3 deliver the inventory reports. It also refuses every IAM role whose name starts with `anthropic-efs-`, except this setup’s. |

Keep `anthropic-efs-` out of your own roles’ names and paths, including the role that deploys the file, because the bucket policy refuses those roles.

The lifecycle rules do the following:

| What the lifecycle rules act on | What they do |
| ----- | ----- |
| Old versions under `slab/` and `media/` | Delete them after 3 days |
| Incomplete multipart uploads | Stop them after 7 days |
| Inventory reports | Expire them after 14 days |
| Leftover delete markers | Remove them |
| Transcripts and Safety Case summaries | Expire them after 28 days, and delete their earlier versions 3 days later |
| Other Safety Case files, your team’s responses included | Expire them after 2,555 days (about 7 years), and keep each earlier version for the same number of days after it stops being current |

#### Get your setup file

<Where method="console" label="Claude Console">

Get the setup file and its commands from the **Create in AWS** step of the **Connect storage** dialog. If the dialog isn’t open, open it as [step 4](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#connect-the-bucket) describes, enter your bucket’s details, and stop at **Create in AWS**. Save the file and commands, because the Claude Console doesn’t show them after the test passes. If someone else runs the file in AWS, send them the file and commands, and click **Test setup** when they’ve finished.

</Where>

<Where method="api" label="Admin API">

Get the setup file and its commands from the Claude Console, which fills in your values. As an Organization Admin, open the [Data retention](https://platform.claude.com/settings/privacy) page and select **Organization** at the top. Click **Finish setup** beside the bucket you registered, and stop at **Create in AWS**. Run the file as [Create your bucket and its KMS key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket) describes. You can also create the same resources another way, as long as they match the file.

</Where>

Create everything in the region that you entered in the dialog, even if the file’s header names `us-east-2`. For a new bucket, run only the file that the dialog gives you, which creates seven roles. If you already ran an earlier file that creates roles with fixed names, see “Test setup says that Anthropic could not assume the verify role” in [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).

<Warning title="Don’t run a seven-role file over a setup with fixed role names">
  If you have a setup that passed **Test setup** and its roles have fixed names, such as `anthropic-efs-ingest`, leave that setup and its storage destination as they are. In that setup’s Terraform folder, don’t apply a file that creates seven roles, because the apply deletes the fixed-name roles and cuts off Anthropic’s access.
</Warning>

<Tabs>
  <Tab title="CloudFormation">
    #### Deploy the CloudFormation stack

    1. **Check the AWS account.** Save the file in an empty folder. From that folder, run `aws sts get-caller-identity` and check that it shows the AWS account for your bucket.
    2. **Deploy the stack.** In the same terminal, run the dialog’s deploy command as shown, which has your values filled in. Don’t change the stack’s name, `anthropic-storage-<RoleDigest>`, because the template refuses any other. `RoleDigest` is a 20-character value that’s already in the command.

    **Check that it worked.** The command prints `Successfully created/updated stack` and your stack’s name. If the deploy fails, see [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).
  </Tab>

  <Tab title="Terraform">
    #### Apply the Terraform file

    The Terraform file needs Terraform 1.5 or later and version 5 or 6 of the AWS provider.

    1. **Check the AWS account.** Save the file in an empty folder, because Terraform loads every `.tf` file in the folder. Run `aws sts get-caller-identity` and check that it shows the AWS account for your bucket.
    2. **Apply the file.** From that folder, run the dialog’s commands, which have your values filled in. Don’t edit the file. Read the plan before you type `yes`, on this apply and every later one, and stop if the first plan shows anything to destroy.

    **Check that it worked.** The apply ends with `Apply complete!` and lists its outputs, including the bucket’s name, its region, and the key’s ARN. If the apply fails, see [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).

    Keep the whole folder, including `terraform.tfstate`, `.terraform/`, and `.terraform.lock.hcl`. The file has no backend block, so Terraform keeps its state there. If you lose that state, the next apply fails at the bucket until you restore the state or run `terraform import` for the resources.
  </Tab>

  <Tab title="Your own tooling">
    #### Create the key and the bucket yourself

    With your own tooling, you build from the CloudFormation template. [Open the **Create in AWS** step](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#get-the-setup-file) of the **Connect storage** dialog, select **CloudFormation** to download the template, then select **Your own tooling** and note the external ID and the role ARNs. Copy every setting from that template, because **Test setup** checks parts of your setup against it. Replace the template’s `${…}` placeholders with your own values. For the partition, use `aws`.

    **Create the key:**

    * Create a single-region KMS key in your bucket’s AWS account, in the region where you create the bucket. Match the template’s key, which is symmetric and has rotation on.
    * Copy the template’s key policy, which lets your account administer the key. It also lets Amazon S3 call `kms:GenerateDataKey` for this account and this bucket, so that S3 Inventory can deliver its daily reports.

    **Create the bucket** with the settings in this step’s table. Copy the template’s lifecycle rules, S3 Inventory configurations, and bucket policy, and add no other lifecycle rule.

    In the bucket’s default encryption, name the key by its key ARN. **Test setup** fails if you name the key by an alias name, an alias ARN, or a bare key ID. It also fails if your bucket lacks one of the template’s required lifecycle rules, or has another rule that expires objects.

    **Test setup** doesn’t check the following parts of your setup, so compare them with the template yourself:

    * The rest of the bucket policy. **Test setup** checks only the two statements that refuse other setups’ roles.
    * The S3 Inventory configurations.
    * The KMS key’s policy and its settings, such as rotation. **Test setup** only confirms that Anthropic can use the key through Amazon S3.
  </Tab>
</Tabs>

### 3. Create the IAM roles

This step covers the seven IAM roles that give Anthropic access to your bucket. Each role allows one kind of work. Each role’s name is `anthropic-efs-<RoleDigest>-<ending>`, where `RoleDigest` is a 20-character value that’s specific to this setup.

| Role name ends in | What Anthropic does through it | What it can do with your bucket’s KMS key |
| ----- | ----- | ----- |
| `ingest` | Writes your Sealed Safety Data under `slab/` and `media/`. | `kms:GenerateDataKey` and `kms:Decrypt` |
| `read` | Reads under `slab/`, `media/`, and `slab-manifest/`, and lists those three prefixes. | `kms:Decrypt` |
| `maintenance` | Reads and writes objects under `slab/`, `media/`, and `slab-manifest/`, and adds delete markers to them. Reads the inventory reports under `inventory/` and the bucket’s configuration. Lists `slab/`, `media/`, `slab-manifest/`, and `inventory/`. Can list unfinished multipart uploads anywhere in the bucket. It never removes an object version. | `kms:GenerateDataKey` and `kms:Decrypt` |
| `media-erasure` | Lists `media/` and permanently deletes object versions under it, and nothing else. | Nothing |
| `verify` | Writes, reads, and deletes test objects and their versions under `verify/`, and lists object versions there. Reads the bucket’s configuration. Can read the inventory report manifests under `inventory/`, and list `inventory/`. | `kms:GenerateDataKey`, `kms:Decrypt`, and `kms:DescribeKey` |
| `transcripts` | Writes Transcripts under `transcripts/`. Lists and permanently deletes their versions. It can’t read a Transcript. | `kms:GenerateDataKey` and `kms:Decrypt` |
| `review` | Writes, reads, and lists Safety Cases under `review-cases/`. Writes summaries and Safety Notices under `review-summaries/` and `review-notices/`. Reads and lists your team’s responses under `review-responses/`. Can permanently delete cases, summaries, and Safety Notices. It can’t read a Transcript, or write, change, or delete a response. | `kms:GenerateDataKey` and `kms:Decrypt` |

Each role trusts only roles in Anthropic’s AWS account, `804820989669`, whose names start with `anthropic-storage-broker-` (for the review role, `anthropic-review-broker-`). The caller must be in Anthropic’s AWS organization. Each role also requires your external ID and a source identity from that role’s permitted set. Your setup file has each role’s full policy.

For each of the first five roles in the table, the permissions also apply to the same prefixes under `safeguards-data/`, such as `safeguards-data/slab/`. The lifecycle rules and the bucket policy cover those prefixes too. [What protects object versions in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-protects-object-versions) says what Anthropic’s roles can’t delete.

<Tabs>
  <Tab title="CloudFormation">
    #### Use the roles from the CloudFormation stack

    The stack you deployed in [step 2](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket) created all the roles, so there’s nothing to run here.
  </Tab>

  <Tab title="Terraform">
    #### Use the roles from the Terraform apply

    The apply in [step 2](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket) created all the roles, so there’s nothing to run here.
  </Tab>

  <Tab title="Your own tooling">
    #### Create the roles yourself

    The **Your own tooling** option in the **Create in AWS** step lists role ARNs. Create one role for each ARN, with the exact name that the ARN contains.

    Copy each role’s whole trust policy and its permissions from your CloudFormation template. The `transcripts` and `review` roles’ permissions are in `TranscriptsRolePolicy` and `ReviewRolePolicy`. Then, adjust each copy:

    * **Trust policy:** Set the external ID to the value that **Your own tooling** shows, and change nothing else.
    * **Permissions:** Replace the template’s references with your own values, including your region and your KMS key’s ARN.

    For every role, compare the permissions and the trust policy with the template yourself. **Test setup** doesn’t read any role’s permissions or trust policy.
  </Tab>
</Tabs>

<Warning title="Leave the bucket and the roles as they are">
  After you create your bucket and the roles, don’t change the bucket, its bucket policy, its KMS key’s policy, or the roles. The one change that you can make is to set [`ReviewExpiryDays`](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#template-reference). If Anthropic’s checks find any other change, they fail.
</Warning>

<Where method="console" label="Claude Console">

### 4. Connect your bucket in the Claude Console

Sign in to the Claude Console in the Anthropic organization whose workspaces will use your bucket, because the roles accept only that organization’s ID.

On the [Data retention](https://platform.claude.com/settings/privacy) page, select **Organization** at the top. Under **Storage destinations**, click **Connect storage**, or click **Finish setup** if you already started the dialog. A storage destination is the Claude Console’s record of your bucket.

#### Select your provider

Select **Amazon S3**, then click **Continue**.

#### Enter your bucket details

Enter the AWS account ID and AWS region where you’ll create your bucket. Under **New bucket name**, enter the name you’ll give your new bucket. Don’t reuse the name of a bucket that you already own.

#### Create in AWS

If you’ve already run this step’s file, go to **Test setup**. If you haven’t, select **CloudFormation**, **Terraform**, or **Your own tooling**, then follow [steps 1 to 3](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic).

#### Test the setup

Click **Test setup**. Anthropic checks your bucket, its key, and the roles for Sealed Safety Data, and lists anything to fix. If the test fails, see [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).

</Where>

<Where method="api" label="Admin API">

### 4. Activate your bucket

Ask Anthropic to check your setup. The request has no body:

<CodeGroup>
  ```bash cURL
  curl -X POST https://api.anthropic.com/v1/organizations/external_storage/estrg_01SDCCSbTxrXDpWc1phhtcfK/activate \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: efs-2026-10-01"
  ```

  ```bash CLI
  ant beta:organization:external-storage activate \
    --external-storage-id estrg_01SDCCSbTxrXDpWc1phhtcfK
  ```

  ```python Python
  client = anthropic.Anthropic()

  storage = client.beta.organization.external_storage.activate(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  )

  print(f"status: {storage.status.type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const storage = await client.beta.organization.externalStorage.activate(
    "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  console.log(`status: ${storage.status.type}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var storage = await client.Beta.Organization.ExternalStorage.Activate(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  Console.WriteLine($"status: {storage.Status.Type.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  storage, err := client.Beta.Organization.ExternalStorage.Activate(
  	context.Background(),
  	"estrg_01SDCCSbTxrXDpWc1phhtcfK",
  	anthropic.BetaOrganizationExternalStorageActivateParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("status: %s\n", storage.Status.Type)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var storage = client.beta().organization().externalStorage()
      .activate("estrg_01SDCCSbTxrXDpWc1phhtcfK");

  IO.println("status: " + storage.status().type());
  ```

  ```php PHP
  $client = new Client();

  $storage = $client->beta->organization->externalStorage->activate(
      externalStorageID: 'estrg_01SDCCSbTxrXDpWc1phhtcfK',
  );

  echo "status: {$storage->status->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  storage = client.beta.organization.external_storage.activate("estrg_01SDCCSbTxrXDpWc1phhtcfK")

  puts "status: #{storage.status.type}"
  ```
</CodeGroup>

Anthropic checks your bucket, its KMS key, and the roles for Sealed Safety Data while the request runs. If everything passes, the status becomes `available` and your bucket is ready to attach. If a check fails, see [Troubleshooting on Manage customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-troubleshooting).

</Where>

## Use your storage destination in a workspace

<Where method="console" label="Claude Console">

Once your bucket passes its test, select it for each workspace that should use it. Do this before the workspace carries traffic that you need stored in your bucket, because [the change doesn’t take effect right away](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take). If your organization has a Legacy Zero Data Retention (ZDR) arrangement, select the **Enterprise Frontier Safeguards** card and your bucket as you create the workspace. <Where cloud="aws" label="Claude Platform on AWS">Follow the Legacy ZDR steps in [Set up Enterprise Frontier Safeguards on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws).</Where>

</Where>

Anthropic strongly recommends a customer-managed key for a workspace that uses customer-owned storage, but doesn’t require one. Before you decide, read [what a customer-managed key adds](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#if-you-use-your-own-bucket) beyond your bucket’s own KMS key.

<Where method="console" label="Claude Console">

<Warning>
  Selecting a bucket for a workspace [ties the bucket to this organization](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#before-you-begin). Treat the tie as permanent. Before you select a bucket, check that you’re in the Anthropic organization whose workspaces will use this bucket.
</Warning>

On the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page, select the **Enterprise Frontier Safeguards** card, then select your bucket under **Sealed Safety Data storage**. <Where cloud="aws" label="Claude Platform on AWS">Also select your bucket under **Safety Case and Transcript storage**.</Where> <Where cloud="claude" label="Claude Platform">**Safety Case and Transcript storage** is optional. Without a bucket under it, your team gets Safety Cases only if your organization has [access to the Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#get-access). You can select your bucket under it if your bucket [can receive Transcripts and Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket).</Where>

Then, save the workspace. If Anthropic refuses your bucket when you save, see [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting).

Saving turns Anthropic Human Review off, which [can take up to 2 hours](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take). To check that your save worked, make sure that **Case review by** reads **My organization** in the workspace’s side panel on the [Workspaces](https://platform.claude.com/settings/workspaces) page. If **Case review by** doesn’t read **My organization**, open the workspace on the [Data retention](https://platform.claude.com/settings/privacy) page and click **Save** again, even if you’ve changed nothing. If you can’t, or **Case review by** still doesn’t read **My organization**, contact your Anthropic account team before you send real traffic.

</Where>

<Where method="api" label="Admin API">

### Attach your bucket to a workspace

Attach your bucket to each workspace that should use it. Attaching tells Anthropic to store that workspace’s Sealed Safety Data in your bucket.

In an organization with a Legacy Zero Data Retention (ZDR) arrangement, don’t attach your bucket to a workspace that has data retention off. [Create a workspace with your bucket already attached](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-create-workspace-attached) instead.

<Warning>
  Before you send this request, check that your key or token belongs to the organization whose workspaces will use this bucket. The first attach request that succeeds [ties your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#before-you-begin), its name, its KMS key, and its IAM roles to that organization. Treat this as permanent.
</Warning>

To attach your bucket, update the workspace with `POST /v1/organizations/workspaces/{workspace_id}` and set `inference_data_privacy.safeguards_storage` to type `external` with your bucket’s ID. This field is the Claude Console’s **Sealed Safety Data storage**.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: efs-2026-10-01" \
    -H "content-type: application/json" \
    -d '{
      "inference_data_privacy": {
        "safeguards_storage": {
          "type": "external",
          "external_storage_id": "estrg_01SDCCSbTxrXDpWc1phhtcfK"
        },
        "human_review": {
          "type": "disabled"
        }
      }
    }'
  ```

  ```bash CLI
  ant beta:organization:workspaces update \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --beta efs-2026-10-01 <<YAML
  inference_data_privacy:
    safeguards_storage:
      type: external
      external_storage_id: estrg_01SDCCSbTxrXDpWc1phhtcfK
    human_review:
      type: disabled
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.workspaces.update(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      inference_data_privacy={
          "safeguards_storage": {
              "type": "external",
              "external_storage_id": "estrg_01SDCCSbTxrXDpWc1phhtcfK",
          },
          "human_review": {"type": "disabled"},
      },
      betas=["efs-2026-10-01"],
  )

  privacy = workspace.inference_data_privacy
  if privacy and privacy.safeguards_storage:
      print(f"safeguards_storage: {privacy.safeguards_storage.type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspace = await client.beta.organization.workspaces.update(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    {
      inference_data_privacy: {
        safeguards_storage: {
          type: "external",
          external_storage_id: "estrg_01SDCCSbTxrXDpWc1phhtcfK"
        },
        human_review: { type: "disabled" }
      },
      betas: ["efs-2026-10-01"]
    }
  );

  const type = workspace.inference_data_privacy?.safeguards_storage?.type;
  console.log(`safeguards_storage: ${type}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Workspaces;

  AnthropicClient client = new();

  var workspace = await client.Beta.Organization.Workspaces.Update(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      new()
      {
          InferenceDataPrivacy = new()
          {
              SafeguardsStorage = new BetaExternalStorageMemberParam
              {
                  ExternalStorageID = "estrg_01SDCCSbTxrXDpWc1phhtcfK",
              },
              HumanReview = new() { Type = BetaAnthropicHumanReviewParamType.Disabled },
          },
          Betas = ["efs-2026-10-01"],
      }
  );

  var type = workspace.InferenceDataPrivacy?.SafeguardsStorage?.Type.Raw();
  Console.WriteLine($"safeguards_storage: {type}");
  ```

  ```go Go
  client := anthropic.NewClient()

  workspace, err := client.Beta.Organization.Workspaces.Update(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.BetaOrganizationWorkspaceUpdateParams{
  		InferenceDataPrivacy: anthropic.BetaInferenceDataPrivacyUpdateParam{
  			SafeguardsStorage: anthropic.BetaStorageMemberParamOfExternal("estrg_01SDCCSbTxrXDpWc1phhtcfK"),
  			HumanReview: anthropic.BetaAnthropicHumanReviewParam{
  				Type: anthropic.BetaAnthropicHumanReviewParamTypeDisabled,
  			},
  		},
  		Betas: []anthropic.AnthropicBeta{"efs-2026-10-01"},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("safeguards_storage: %s\n", workspace.InferenceDataPrivacy.SafeguardsStorage.Type)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.BetaAnthropicHumanReviewParam;
  import com.anthropic.models.beta.organization.workspaces.BetaInferenceDataPrivacyUpdateParam;
  import com.anthropic.models.beta.organization.workspaces.WorkspaceUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = WorkspaceUpdateParams.builder()
          .inferenceDataPrivacy(BetaInferenceDataPrivacyUpdateParam.builder()
              .externalSafeguardsStorage("estrg_01SDCCSbTxrXDpWc1phhtcfK")
              .humanReview(BetaAnthropicHumanReviewParam.builder()
                  .type(BetaAnthropicHumanReviewParam.Type.DISABLED)
                  .build())
              .build())
          .addBeta("efs-2026-10-01")
          .build();
      var workspace = client.beta().organization().workspaces()
          .update("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", params);

      IO.println("safeguards_storage: " + workspace.inferenceDataPrivacy()
          .flatMap(privacy -> privacy.safeguardsStorage())
          .map(storage -> storage.type().asString())
          .orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $workspace = $client->beta->organization->workspaces->update(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      inferenceDataPrivacy: [
          'safeguardsStorage' => [
              'type' => 'external',
              'externalStorageID' => 'estrg_01SDCCSbTxrXDpWc1phhtcfK',
          ],
          'humanReview' => ['type' => 'disabled'],
      ],
      betas: ['efs-2026-10-01'],
  );

  echo "safeguards_storage: {$workspace->inferenceDataPrivacy?->safeguardsStorage?->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace = client.beta.organization.workspaces.update(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    inference_data_privacy: {
      safeguards_storage: {
        type: :external,
        external_storage_id: "estrg_01SDCCSbTxrXDpWc1phhtcfK"
      },
      human_review: {
        type: :disabled
      }
    },
    betas: ["efs-2026-10-01"]
  )

  puts "safeguards_storage: #{workspace.inference_data_privacy&.safeguards_storage&.type}"
  ```
</CodeGroup>

When the request succeeds, your bucket’s status becomes `active`. The example request also sets `inference_data_privacy.human_review` to type `disabled`, because in the Admin API an attach alone doesn’t turn [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off. With Enterprise Frontier Safeguards (EFS), Anthropic Human Review is always off and your own team reviews the workspace’s [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases).

An attach [doesn’t take effect right away](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take). Until it does, Sealed Safety Data from a workspace that had no [safety data bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) might go to Anthropic-managed storage. Until 10 minutes after the first new object arrives, send only test requests with no sensitive data, because Anthropic’s servers don’t all pick up the change at once. To confirm that the attach has taken effect, watch for new objects arriving under `slab/` or `safeguards-data/slab/` in your bucket. Neither the `active` status nor reading the workspace back shows that the attach has taken effect. If another workspace already sends data to this bucket, new objects don’t show it either, so ask your Anthropic account team before you send real traffic.

To move a workspace to another bucket, follow [Change your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-your-bucket). At step 1, [register](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-register) and [activate](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-activate) your new bucket. At step 2, send the attach request with the new bucket’s ID instead. If `transcripts_storage` names your old bucket, set it to the new bucket’s ID in the same request. Don’t [detach](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-stop) first, or new Sealed Safety Data can go to Anthropic-managed storage.

The attach request can return errors such as these:

* `human_review_on_with_external_storage`: Anthropic can return this if you leave `human_review` out while Anthropic Human Review is on.
* `approval_required`: Your organization doesn’t have Anthropic’s approval to turn off Anthropic Human Review. The request changes nothing.
* `workspace_policy_violation`: Your organization’s policy refuses the request, for example because it requires Anthropic Human Review.
* `transcripts_storage_required`: Nothing changes. [Set `transcripts_storage` too](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-attach-transcripts) in the same request.

For more on attach errors, see [Troubleshooting on Manage customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-troubleshooting).

#### Send Transcripts and Safety Cases to a bucket

To send Transcripts and Safety Cases to your bucket, set `inference_data_privacy.transcripts_storage` to type `external` with the same ID as `safeguards_storage`. This field is the Claude Console’s **Safety Case and Transcript storage**. You can set both storage fields in the same request. If a check fails on either field, Anthropic stops the whole request. [Transcripts and Safety Cases in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket) says which buckets can receive them.

#### Create a workspace with your bucket already attached

To create a workspace with your bucket already attached, send the same `inference_data_privacy` settings to `POST /v1/organizations/workspaces`. The attach still [doesn’t take effect right away](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take). In an organization with a Legacy ZDR arrangement, data retention can be off for the new workspace. If it’s off, nothing goes to your bucket until you turn it on. To turn it on, open the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console, click **Finish switching**, and then click **Accept**. The workspace starts to keep Sealed Safety Data at **Accept**, so allow time for the attach to take effect first. Send only test requests until 10 minutes after the first new object arrives.

If the create request returns `approval_required`, `grant_required`, `authorization_check_unavailable`, `human_review_on_with_external_storage`, or `transcripts_storage_required`, the workspace isn’t created.

Approval for chosen workspaces can’t cover a workspace that doesn’t exist yet. If the create request returns `grant_required` in an organization with a Legacy ZDR arrangement, don’t create the workspace without your bucket. Contact your Anthropic account team. In any other organization, create the workspace without `inference_data_privacy`, ask your Anthropic account team to have the workspace approved, and then attach your bucket as [Attach your bucket to a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-attach) describes.

</Where>

<Where cloud="claude" label="Claude Platform">

For the full steps, including the workspace’s other settings, see [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#turn-on-efs-for-a-workspace).

</Where>

<Where cloud="aws" label="Claude Platform on AWS">

For the full steps, including the workspace’s other settings, see [Set up Enterprise Frontier Safeguards on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws#turn-on-efs-for-a-workspace).

</Where>

You can use [a policy for new workspaces](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#set-organization-defaults) to require customer-owned storage for every new workspace that keeps Sealed Safety Data.

### Confirm that the change took effect

Before the workspace carries traffic that you need stored in your bucket, send test requests with no sensitive data until new objects arrive under `slab/` or `safeguards-data/slab/`. Then, wait 10 more minutes, because Anthropic’s servers don’t all pick up the change at once. Until that wait ends, send only test requests, because your Sealed Safety Data might go to Anthropic-managed storage. If another workspace already sends data to this bucket, new objects don’t show that this change took effect, so ask your Anthropic account team before you send real traffic. If no new objects have appeared under `slab/` or `safeguards-data/slab/` 4 hours after you make the change, contact your Anthropic account team.

The change doesn’t take effect right away. While you wait, the following are expected, even when setup succeeded:

* **The wait.** When a new workspace, or one on Anthropic-managed storage, starts to use your bucket, the change usually takes effect within 10 minutes, but it can take longer.
* **No new objects.** Until the change takes effect, your Sealed Safety Data from that workspace’s requests might go to Anthropic-managed storage, and new objects might not appear under `slab/` or `safeguards-data/slab/`.
* **An Active status with no objects.** Your bucket can show as **Active** in **Storage destinations** before the change takes effect, so **Active** doesn’t mean that objects are arriving.
* **Anthropic Human Review.** If the change also turns off Anthropic Human Review, that can take up to 2 hours. Until then, Anthropic’s review team might still review the workspace’s data.

If you later move a workspace to a different bucket or off EFS, that move doesn’t take effect right away either. After a move between two Amazon S3 buckets in one save or request, new Sealed Safety Data can still go to your old bucket for a while. That move doesn’t by itself send new data to Anthropic-managed storage. Keep your old bucket, and Anthropic’s access to it, as [Change or stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket) describes.

## Transcripts and Safety Cases in your bucket

To receive a workspace’s Transcripts and Safety Cases in your bucket, check that the bucket can receive them, then select it for the workspace. Transcripts and Safety Cases go to the same bucket, and you can’t choose one without the other.

<Where cloud="aws" label="Claude Platform on AWS">

[Set up Enterprise Frontier Safeguards on Claude Platform on AWS](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws) has the steps for **Safety Case and Transcript storage**.

</Where>

<Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">

[Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#turn-on-efs-for-a-workspace) has the steps for **Safety Case and Transcript storage**.

</Where>

<Where cloud="claude" label="Claude Platform">

To find out whether a bucket can receive Transcripts and Safety Cases, look at the names of its roles:

* **Names that start with `anthropic-efs-<RoleDigest>-`:** The bucket can receive Transcripts and Safety Cases.
* **Fixed names, such as `anthropic-efs-ingest`:** The bucket can’t receive them. To receive them, [change to a new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-your-bucket) and select it under both storage settings.

If the bucket can receive them, open the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page. If it shows **Safety Case and Transcript storage**, select the same bucket under that setting and under **Sealed Safety Data storage**. If you select a different bucket, it might not receive Transcripts and Safety Cases, even if the save succeeds. When you save, Anthropic checks that the bucket is set up for Transcripts and Safety Cases. If Anthropic refuses the bucket, the whole save stops. To fix it, see [Troubleshooting](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting). If the page doesn’t show **Safety Case and Transcript storage** with the **Enterprise Frontier Safeguards** card selected, contact your Anthropic account team.

Each kind of file has its own prefix:

| Prefix | What’s there | Who writes it |
| ----- | ----- | ----- |
| `transcripts/` | Transcripts | Anthropic |
| `review-cases/`, `review-summaries/`, and `review-notices/` | Safety Case files | Anthropic |
| `review-responses/` | Your team’s responses | Your team. No Anthropic role can write, change, or delete them. |

The setup file’s lifecycle rules expire all of these files after [the number of days set for each](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket).

</Where>

### Give your team access to the bucket

To give your team access, add the following permissions to your own users’ IAM policies. Nothing that the setup file creates needs to change.

* **To read Transcripts and Safety Cases:** allow `s3:GetObject` under `transcripts/` and the review prefixes (`review-cases/`, `review-responses/`, `review-summaries/`, and `review-notices/`), `s3:ListBucket` on the bucket with an `s3:prefix` condition that limits it to those prefixes, and `kms:Decrypt` on the key. Don’t grant S3 access to any other prefix.
* **To read a file’s earlier versions:** also allow `s3:GetObjectVersion` and `s3:ListBucketVersions`, with the same limits.
* **To write responses under `review-responses/`:** also allow `s3:PutObject` on `review-responses/*` and `kms:GenerateDataKey` on the key. Write responses with the bucket’s default encryption, because Anthropic can’t read a response under another KMS key.

For the review process, see [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases).

## Troubleshooting

<AccordionGroup>
  <Accordion title="The CloudFormation deploy fails">
    If the deploy stops at once with an error about `Fn::Select`, the stack’s name and `RoleDigest` don’t match. Nothing changed, so run the dialog’s command exactly as shown. If you were updating a stack with another name, keep it as it is and contact your Anthropic account team.

    To find the reason for any other failure, either run the two read-only commands that the **Create in AWS** step shows below the deploy command, or open the stack’s **Events** tab in the AWS CloudFormation console.

    If the bucket name is taken, delete the failed stack and the storage destination, then connect a new storage destination with another bucket name. If the reason still isn’t clear, send all of the output to your Anthropic account team. Don’t add `--debug` to any command, because debug output can include your AWS session token.
  </Accordion>

  <Accordion title="The Terraform apply fails">
    If the first apply fails partway, run the same apply again to create what’s missing. If the apply fails because another AWS account already has a bucket with the name you entered, Terraform creates nothing, and running the apply again doesn’t help. Instead, delete the storage destination, connect a new storage destination with another bucket name, and apply with the commands that the dialog gives you for the new storage destination. If your own AWS account has the bucket from an earlier apply, keep the name, and either restore the folder’s state or run `terraform import`.
  </Accordion>

  <Accordion title="Test setup says that Anthropic couldn’t run the test">
    Run the test again in a few minutes. If the test keeps showing this message, tell your Anthropic account team.
  </Accordion>

  <Accordion title="Test setup says that Anthropic could not assume the verify role">
    With this problem, **Test setup** can show several failed checks. The first failed check’s message begins “Anthropic could not assume the verify role”, and the other messages say that a role “must have the setup template’s trust policy”. This can happen even when you created your bucket and the roles exactly as described.

    First, look at the names of your IAM roles. If this bucket has never passed **Test setup** and its roles have fixed names, such as `anthropic-efs-ingest`, your setup comes from an earlier setup file. Anthropic doesn’t accept a new bucket whose roles have fixed names, and changing the roles doesn’t make the test pass. Instead, do the following:

    1. Delete the storage destination.
    2. [Start again with **Connect storage**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles), with a new bucket name, and use the file or the values that the dialog gives you. With Terraform, use a new folder, and don’t apply in the earlier one.
    3. Afterward, if no other bucket uses the earlier roles, you can remove them, as the step **Remove Anthropic’s access** in [Stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#stop-using-your-bucket) describes. Then, you can delete the unused bucket.

    If your roles don’t have fixed names, or this bucket has passed **Test setup** before, work through these checks:

    1. Check that your setup in AWS completed with the file or the values from the dialog. Check that the AWS account ID and the region you entered are the ones you deployed in. To change either, delete the storage destination and connect a new one. A copy of the file from anywhere else can create roles with other names, which the test can’t find. If you used one, delete the storage destination, connect a new one with a new bucket name, and use the file that the dialog gives you.

    2. Check that you ran the dialog’s command exactly as shown, so that the external ID and the role names are right. What to do depends on what you changed:

       * **The organization ID:** Run the dialog’s command again. If Terraform then stops because the organization ID changed, its message says what to add to the command. With CloudFormation, if your stack’s name differs from the one in the dialog’s command, follow the next item instead.

       * **`RoleDigest`, with CloudFormation:** Open the stack whose deploy succeeded in the AWS CloudFormation console. Check **Created time** on its **Stack info** tab and `BucketName` on its **Outputs** tab. What to do depends on what they show:

         * **Created time is when you first deployed for this bucket:** Delete the stack, which leaves its bucket and KMS key behind. Delete that unused bucket, and any failed stack that has the name in the dialog’s command. Then, run the dialog’s command with the dialog’s file.
         * **The stack is older than that, and shows another bucket:** Leave it alone, and run the dialog’s command for this bucket.
         * **The stack is older than that, and shows this bucket:** Your deploy changed another bucket’s stack. Run nothing more, and contact your Anthropic account team at once.

       * **The bucket name:** Tell your Anthropic account team.

    3. If the first two checks find nothing wrong, check whether [an AWS organization policy blocks Anthropic](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic). A single policy that refuses Anthropic can cause every failed check. If a policy is the cause, the setup files need no change.

    After a fix, click **Test again**. If you closed the dialog, click **Finish setup** in **Storage destinations**, then click **Test setup**. If the test still fails, tell your Anthropic account team.
  </Accordion>

  <Accordion title="Test setup mentions another organization’s External Storage">
    This section applies when **Test setup** fails with one check whose message begins “Another organization’s External Storage”. The check fails when another Anthropic organization has used part of this setup, or when the bucket name is in use in a different AWS account. The check can also count storage destinations of a deleted organization.

    If another organization has used this AWS account, you can keep the account. First, check that you deployed the file that the dialog gives you for this bucket, then test again.

    If the test still fails, or no other organization has used this AWS account, use a new bucket name, with a key and roles of its own. Start again with **Connect storage**, because **Finish setup** keeps the AWS account and bucket name you entered. If the new bucket fails in the same way, tell your Anthropic account team.
  </Accordion>

  <Accordion title="Anthropic refuses your bucket when you save a workspace">
    The first time you select your bucket for a workspace and save, Anthropic repeats the checks from **Test setup**. If Anthropic refuses your bucket, one of those checks might have failed, for one of two reasons:

    * Something has changed since the test passed: a bucket setting, the bucket’s KMS key, an IAM role, or an AWS organization policy.
    * Another Anthropic organization has used part of this setup or, if your roles have fixed names, this AWS account.

    The Claude Console lists the failed checks in a dialog. If you selected a bucket under **Safety Case and Transcript storage**, no checks are listed, and the error doesn’t mention Human Review, go to the next problem, “Anthropic refuses your bucket under Safety Case and Transcript storage”.

    If the only failed check starts with “Another organization’s External Storage”, what to do depends on which setting the error is under:

    * **Safety Case and Transcript storage:** Contact your Anthropic account team.
    * **Sealed Safety Data storage:** Use a new bucket name, with a key and roles of its own. Then, [start again with **Connect storage**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles).

    For any other failed check, fix the cause, then save the workspace again. If you can’t tell the cause, contact your Anthropic account team. If the error is under **Safety Case and Transcript storage**, follow the next problem, “Anthropic refuses your bucket under Safety Case and Transcript storage”.

    If the error says that Enterprise Frontier Safeguards needs Anthropic Human Review off, the save changed nothing. The same is true if the error says that Anthropic doesn’t offer Human Review of data in your own storage. Your organization needs Anthropic’s approval to turn off Anthropic Human Review, and your organization’s policy must not require Anthropic Human Review. If your organization lacks the approval, have an Organization Admin [accept the terms](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access). If the terms aren’t offered, ask your Anthropic account team. If the policy requires Anthropic Human Review, ask an admin to change the policy. Under that policy, the **Enterprise Frontier Safeguards** card might show **Ineligible**. If neither applies, reload the page and save again. If the error comes back, contact your Anthropic account team.
  </Accordion>

  <Accordion title="Anthropic refuses your bucket under Safety Case and Transcript storage">
    If your bucket’s roles have fixed names, such as `anthropic-efs-ingest`, the bucket can’t receive Transcripts and Safety Cases, and trying again doesn’t help. <Where cloud="aws" label="Claude Platform on AWS">Ask your Anthropic account team before you do anything else.</Where> Don’t use [the setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#get-the-setup-file) to update that bucket’s setup. To receive Transcripts and Safety Cases, [change to a new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-your-bucket) and select it under both **Sealed Safety Data storage** and **Safety Case and Transcript storage** before you save. If the dialog gives you a file with fixed role names, don’t run it, and contact your Anthropic account team.

    If your bucket’s roles don’t have fixed names, fix what the failed checks list, then save the workspace again. If the only failed check starts with “Another organization’s External Storage”, contact your Anthropic account team. Also contact your Anthropic account team if the message says that the bucket can’t store Cases and transcripts, or that storage can’t be attached for transcripts yet.

    If the error says that Anthropic can’t check the bucket’s setup, or only that workspace settings failed to update, check that your bucket is still selected under both storage settings and save again. If the error comes back, contact your Anthropic account team.

    <Where cloud="claude" label="Claude Platform">

    To save only **Sealed Safety Data storage**, select **Not copied to your storage** under **Safety Case and Transcript storage** if the page offers that choice. If it doesn’t, contact your Anthropic account team.

    </Where>
  </Accordion>
</AccordionGroup>

## Template reference

Review the CloudFormation template or Terraform file that the **Create in AWS** step gives you before you run it. The file has each role’s full policy, with every action and condition.

To change when Safety Case files and your team’s responses expire, set `ReviewExpiryDays` (in Terraform, `review_expiry_days`), the one value that you can set yourself. It’s the number of days after which those files expire, up to 9,999. The default is 2,555, about 7 years. These rules apply, so read them before you change it:

* A summary expires after 28 days if that’s sooner.
* A file expires even if its review isn’t complete, so ask your Anthropic account team before you set a low number.
* A new number also applies to the files already in your bucket, so a lower number can expire older files and remove earlier versions.
* An expired, replaced, or deleted file stays as an earlier version for the same number of days again, or at most 3 days for a summary. To remove a file at once, delete all its versions.
* With Terraform, pass `review_expiry_days` on every apply. An apply without it goes back to the default.

<AccordionGroup>
  <Accordion title="What the roles can do with your bucket’s KMS key">
    Each KMS permission in [the table of roles](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-roles) applies only to the KMS key that the setup file creates for your bucket. `kms:GenerateDataKey` and `kms:Decrypt` also carry the `kms:ViaService` condition for Amazon S3 in your bucket’s region, so a role can encrypt and decrypt with the key only through Amazon S3, not by calling AWS KMS itself.
  </Accordion>

  <Accordion title="What a narrower AWS organization policy exception has to allow">
    A narrower exception has to allow two calls, `sts:AssumeRole` and `sts:SetSourceIdentity`. The calls come from IAM roles in Anthropic’s AWS account whose names start with `anthropic-storage-broker-` or `anthropic-review-broker-`. The calls go only to this setup’s roles, in the AWS account that holds your bucket, and the setup files allow Anthropic’s callers nothing else. Anthropic’s work in Amazon S3 and AWS KMS then runs as this setup’s roles, which are principals in your own AWS account. An exception that allows those two calls should be enough, but Anthropic has seen **Test setup** pass only with the account-wide exception. **Test setup** never tries the `review` role, so a passing test doesn’t show that your exception covers `anthropic-review-broker-`.
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Manage customer-owned storage" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage">
    Check your bucket’s status, fix a bucket that stops working, and change or stop using it.
  </Card>

  <Where cloud="claude" label="Claude Platform">

  <Card title="Set up Enterprise Frontier Safeguards on Claude Platform" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console">
    Select your storage destination for a workspace, then check your setup.
  </Card>

  </Where>

  <Where cloud="aws" label="Claude Platform on AWS">

  <Card title="Set up Enterprise Frontier Safeguards on Claude Platform on AWS" icon="settings" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-platform-on-aws">
    Select your storage destination for a workspace, then check your setup.
  </Card>

  </Where>

  <Card title="Use a customer-managed key" icon="lock" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys">
    Encrypt your data using a key you hold in your own key management service.
  </Card>
</CardGroup>

</Where>

<Where bucket="gcs" label="Google Cloud Storage">

## Set up customer-owned storage on Google Cloud Storage

A Google Cloud Storage bucket in your own cloud account keeps a workspace’s [Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored). To set up the bucket, create it with Terraform and connect it in the Claude Console. Your team can’t read Sealed Safety Data. Before you start, read [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace).

Setup has three parts:

1. [Check your Google Cloud organization policies](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#check-your-policies).
2. [Create and test the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket).
3. [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace).

## Before you begin

Make sure that you have the following:

* **[Access to Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console).**

  <Where cloud="claude" label="Claude Platform">If your organization has it, the [Programs](https://platform.claude.com/settings/programs) page in the Claude Console shows it with a **Configure** button.</Where>
* **A way to connect your bucket.** On Claude Platform, check that you can select **Google Cloud Storage** under **Connect storage**. **Connect storage** is on the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console, with **Organization** selected at the top. If you can’t select **Google Cloud Storage**, contact your Anthropic account team before you start part 1.
* **An Organization Admin** in the Claude Console, who gets the setup file and connects your bucket. <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">On Claude Models on Google Cloud (Anthropic managed), that’s someone with [`roles/claude.admin`](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#using-the-claude-console) on the Google Cloud project whose organization will use this bucket.</Where>
* **A Google Cloud project** where no automation removes custom roles, grants, or buckets.
* **Tools:** [Terraform 1.9 or later](https://developer.hashicorp.com/terraform/install) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
* **Roles on the project:** Project Owner or all of `roles/storage.admin`, `roles/cloudkms.admin`, `roles/iam.roleAdmin`, and `roles/serviceusage.serviceUsageAdmin`.
* **A role for policy changes:** `roles/orgpolicy.policyAdmin` on the Google Cloud organization. Project Owner doesn’t include it.

## 1. Check your Google Cloud organization policies

In this step, you make sure that your Google Cloud organization’s policies let the setup file create its resources and give Anthropic access to your bucket.

### Allow the accounts

To let the setup file grant access to Anthropic, allow the following accounts if domain-restricted sharing is on. It’s the default in Google Cloud organizations created on or after May 3, 2024, and it allows IAM grants only to your organization’s members. If you don’t allow the accounts, the apply stops with an error such as “One or more users named in the policy do not belong to a permitted customer.”

The last account is your project’s own Cloud Storage service agent, which uses the bucket’s key:

* `anthropic-efs-ingest@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-read@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-maintenance@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-media-erasure@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-verify@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-transcripts@anthropic-storage-us.iam.gserviceaccount.com`
* `anthropic-efs-review@anthropic-storage-us.iam.gserviceaccount.com`
* `service-123456789012@gs-project-accounts.iam.gserviceaccount.com`, with your project’s number

In a policy, write `serviceAccount:` before each address. Change each constraint that applies to this project:

* **`constraints/iam.managed.allowedPolicyMembers`** lists single accounts. Add them all.

* **`constraints/iam.allowedPolicyMemberDomains`** lists whole organizations only. Choose one of these options:

  * On this project, enforce `constraints/iam.managed.allowedPolicyMembers` with your own organization and these accounts, then override `constraints/iam.allowedPolicyMemberDomains`.
  * Take the constraint off this project, apply, and put it back ([forcing account access](https://docs.cloud.google.com/organization-policy/restrict-domains#forcing_access)). Repeat at any later apply that adds or replaces a grant.

Allow up to 15 minutes for a policy change to take effect.

### Check your other policies

Check that your organization’s other policies give the setup what it needs:

| Policy | What the setup needs |
| ----- | ----- |
| `constraints/cloudkms.allowedProtectionLevels` | Allows `HSM` |
| `constraints/gcp.resourceLocations` | Allows your bucket’s [region](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#supported-regions) |
| `constraints/storage.softDeletePolicySeconds` | Allows 0 |
| `constraints/gcp.restrictCmekCryptoKeyProjects` | Allows this project |
| `constraints/storage.retentionPolicySeconds` | Doesn’t apply to this project |
| VPC Service Controls perimeter | An ingress rule admits Anthropic’s accounts, from any source, to `storage.googleapis.com` |
| IP filtering or an IAM deny policy | Doesn’t reach Anthropic’s accounts |

## 2. Create and test the bucket

In this step, you download a Terraform file from the Claude Console, apply it, and test the result. The file creates the bucket, an `HSM` Cloud KMS key that encrypts it, custom roles, and grants to Anthropic’s accounts. It also prepares the bucket to hold Transcripts and Safety Cases.

The bucket’s own lifecycle rules delete each object of Sealed Safety Data after it’s 28 days old and permanently remove it at least a day later.

<Warning>
  Anyone with the Viewer role on the project can download the objects in all its buckets, including any Transcripts and Safety Case files. Those files aren’t sealed, so anyone who downloads them can read them. Anyone with the Editor or Owner role can also change or delete the objects. Use one project for more than one Anthropic organization only if you accept that access.
</Warning>

1. On the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console, select **Organization** at the top and click **Connect storage**. Make sure that you’re in the Anthropic organization whose workspaces will use this bucket.

   * **On Claude Models on Google Cloud (Anthropic managed):** The dialog doesn’t ask for a provider, and it fills in the number of the project whose organization will use this bucket. If it does otherwise, you’re in the wrong organization. Open the Claude Console from that project.
   * **On Claude Platform:** Select **Google Cloud Storage**.
   * If **Connect storage** is missing or unavailable, or **Google Cloud Storage** shows **Not available yet**, contact your Anthropic account team.

2. Enter your project’s number, or check it if the dialog has filled it in. Then, enter a new bucket name that’s unlikely to be in use. Under **Google Cloud region**, keep `us-east5` or select [another region](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#supported-regions). After you click **Continue**, you can change these three values only by [deleting the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#delete-a-storage-destination) and connecting it again.

3. Select **Terraform**, enter your project’s ID, and download `customer-bucket-setup-gcs.tf` to an empty folder.

4. In that folder, run the following commands. The dialog shows the two `terraform` commands with your own values.

```bash
gcloud auth login
gcloud auth application-default login
gcloud services enable storage.googleapis.com --project acme-claude-storage
gcloud services enable cloudkms.googleapis.com --project acme-claude-storage
gcloud services enable iam.googleapis.com --project acme-claude-storage

terraform init
terraform apply \
  -var "project_id=acme-claude-storage" \
  -var "project_number=123456789012" \
  -var "organization_id=8a3f2c1e-5b7d-4e9a-a1c6-2f4e8d0b7c35" \
  -var "bucket_name=acme-claude-retention" \
  -var "region=us-east5"
```

On your first apply, at `Enter a value:`, answer `yes` only if the plan shows `Plan: 42 to add, 0 to change, 0 to destroy.` If it doesn’t, answer `no`, download the file again over the old one, and run both `terraform` commands again. If the plan still differs, contact your Anthropic account team.

Keep the whole folder and the apply command. The Claude Console doesn’t show the command again once the test passes.

After the apply, wait 10 minutes for the grants to take effect, then click **Test setup** and wait for **Ready**.

<Warning title="Leave what the file created as it is">
  If you change what the file created, you can lose data or end Anthropic’s access to your bucket.
</Warning>

In particular, don’t:

* Add a lifecycle rule that deletes objects.
* Turn off versioning.
* Change or remove the file’s rules, roles, grants, or labels.
* Turn on soft delete, a retention policy, object retention, a default hold, or Requester Pays.
* Change the bucket’s default key.
* Disable or destroy the key or its versions, or remove its grant to Cloud Storage. Objects would become unreadable.
* Change, move, delete, or add objects in the folder named after your Anthropic organization ID. The exception is your team’s [response files](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file), which go under `review-responses/` in that folder.
* Remove `prevent_destroy` from the file.
* Run `terraform taint` or `terraform apply -replace=...` on a grant.

### Supported regions

You can use any region in the dialog’s **Google Cloud region** list. Anthropic recommends `us-east5` because Anthropic reads and writes your bucket from `us-east5`. A bucket in another region can affect your network transfer costs. Your bucket’s region determines where your cloud provider stores the bucket’s objects. It doesn’t change [where model inference runs](https://platform.claude.com/docs/en/manage-claude/data-residency#inference-geo) or where Anthropic processes your data.

### If an apply or Test setup fails

To fix a failure, find it in this table and do what it says. For any other failure, apply again from the same folder with the same values.

| What you see | What to do |
| ----- | ----- |
| In a new project, Google Cloud refuses a grant or the bucket. | Wait 10 minutes, then apply again. |
| Google Cloud refuses a grant to an Anthropic account or to Cloud Storage. | [Allow the accounts](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#allow-the-accounts), then apply again. |
| An organization policy refuses the key or the bucket. | [Check your other policies](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#check-your-other-policies), then apply again. |
| “Instance cannot be destroyed.” or “organization\_id differs from the value that Terraform’s state keeps” | Pass the first apply’s values. If its `organization_id` was wrong, change nothing and contact your Anthropic account team. |
| A grant “is tainted, so must be replaced.” | Don’t apply the plan. If the grant is in Google Cloud, run `terraform untaint` with its address. If not, run `terraform state rm` with its address and apply again. |
| The bucket’s name is already taken. | [Delete the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#delete-a-storage-destination), then start again from [Create and test the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket) with a new name and a new empty folder. The first apply’s key and roles stay in your project. |
| **Test setup** says that another organization has used this bucket. | [Delete the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#delete-a-storage-destination), then start again from [Create and test the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket) with a new bucket name and a new empty folder. The first apply’s bucket, key, and roles stay where they are. |

### Update a bucket from an earlier setup file

If **Test setup** says that the bucket comes from an earlier setup template, update the bucket with the current file:

1. Wherever you listed Anthropic’s accounts, add any that are new in [Allow the accounts](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#allow-the-accounts).
2. Click **Finish setup**, enter your project’s ID, and download the file over the old one in your folder.
3. Run `terraform init`, then your apply command with the same values. If the plan fails or would destroy or replace anything, answer `no` and contact your Anthropic account team.
4. Wait 10 minutes, then click **Test setup**.

### Delete a storage destination

To delete a storage destination that shows **Needs setup** or **Ready**, select **Delete** in its row menu under **Storage destinations**. The bucket and Anthropic’s grants stay in your project.

## 3. Use your Cloud Storage bucket in a workspace

Once your bucket passes its test, select it for each workspace that should use it. If your organization has a Legacy Zero Data Retention (ZDR) arrangement, select the **Enterprise Frontier Safeguards** card and your bucket as you create the workspace.

With EFS, Anthropic Human Review is always off, so reviewing [Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases) is your own team’s job.

Before you select the bucket, check that you’re in the Anthropic organization whose workspaces will use it. Once you save or create a workspace with the bucket selected, you can’t delete the storage destination. After that, no other Anthropic organization can use the bucket for customer-owned storage.

<Warning>
  Talk to your Anthropic account team before you select the bucket if:

  * **Your organization uses Legacy Zero Data Retention.** Sealed Safety Data [might go to Anthropic-managed storage at first](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#confirm-that-objects-arrive).
  * **You want more than one bucket or many workspaces.** Anthropic limits the number of each. If you go over a limit, data doesn’t arrive in your bucket, and the Claude Console shows no error.
</Warning>

Attaching a [customer-managed key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#attach-a-customer-managed-key) to the workspace is permanent. Use a different key from the bucket’s own key.

On the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page, select the **Enterprise Frontier Safeguards** card, then select your bucket under **Sealed Safety Data storage**. Under **Safety Case and Transcript storage**, you select the bucket for Transcripts and Safety Cases in a form that your team can read. If the page shows that setting, you can select the same bucket. <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">Your save fails if you don’t select a bucket under that setting. If the page doesn’t show the setting, contact your Anthropic account team before you save.</Where> Then, save the workspace. If Anthropic refuses your bucket when you save, contact your Anthropic account team before you connect another bucket. <Where cloud="claude" label="Claude Platform">For the full steps, see [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#turn-on-efs-for-a-workspace).</Where> <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">For the full steps, see [Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-claude-models-on-google-cloud-anthropic-managed#turn-on-efs-for-a-workspace).</Where>

Saving turns Anthropic Human Review off, which can take up to 2 hours. To check that your save worked, make sure that **Case review by** reads **My organization** in the workspace’s side panel on the [Workspaces](https://platform.claude.com/settings/workspaces) page. If it doesn’t read **My organization**, open the workspace on the [Data retention](https://platform.claude.com/settings/privacy) page and click **Save** again, even if you’ve changed nothing. If you can’t, or **Case review by** still doesn’t read **My organization**, contact your Anthropic account team before you send real traffic.

In your bucket, the files that [Safety Case files](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files) describes go in the folder named after your Anthropic organization ID, such as `<organization ID>/review-cases/<id>.json` and `<organization ID>/review-responses/<case_id>.json`.

To review Safety Cases in your bucket, your team needs to list and read the files under `transcripts/`, `review-cases/`, `review-summaries/`, `review-notices/`, and `review-responses/` in your organization’s folder. To respond, your team also needs to create files under `review-responses/`. The setup file doesn’t give your team this access, so grant it yourself in Google Cloud IAM. Limit read access to these folders, and limit create access to `review-responses/`.

### Confirm that objects arrive

Before the workspace carries traffic that you need stored in your bucket, confirm that new objects arrive. Then, wait 10 more minutes, because Anthropic’s servers don’t all pick up the change at once. Until then, send only test requests, because the workspace’s Sealed Safety Data might go to Anthropic-managed storage. If another workspace already sends data to this bucket, new objects don’t show that this change took effect, so ask your Anthropic account team before you send real traffic.

Send test requests with no sensitive data to that workspace. <Where cloud="claude" label="Claude Platform">Use a credential for that workspace.</Where> Then, list `slab/` with your apply command’s `bucket_name` and `organization_id`:

```bash
gcloud storage ls gs://acme-claude-retention/8a3f2c1e-5b7d-4e9a-a1c6-2f4e8d0b7c35/safeguards-data/slab/
```

The **Active** status can show before objects arrive, so don’t rely on it. If the command still stops with “One or more URLs matched no objects.”, contact your Anthropic account team. Objects under `slab/` show that Sealed Safety Data arrives. They don’t show that Transcripts or Safety Cases arrive.

### If your bucket stops working

To avoid losing data, restore a bucket that stops working as soon as you can. If a write to your bucket fails, Anthropic retries it, then deletes the data about a day after the request. Nobody can recover that data, and it doesn’t go to Anthropic-managed storage.

To notice a failure, watch for new objects under `slab/`. Don’t rely on an email or on the bucket’s status to warn you. If you notice a failure, tell your Anthropic account team as soon as you can.

To restore your bucket, do what fits the change:

* **Grants or settings:** Apply again with the same values. The plan should destroy nothing.
* **A deleted custom role:** Run `gcloud iam roles undelete` within 7 days. An apply doesn’t restore it.
* **A disabled key version:** Run `gcloud kms keys versions enable`, after `restore` if it’s scheduled for destruction.
* **Anything else:** Contact your Anthropic account team.

## Stop using your bucket

To stop using your bucket, follow these steps in order, or you can lose data. <Where cloud="gcp" label="Claude Models on Google Cloud (Anthropic managed)">Follow them before you cancel your subscription or delete your project. Neither action takes a workspace off the bucket.</Where>

Before you change or remove a workspace’s bucket, [respond to its open Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#respond-to-a-case) and [wait until they close](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#after-you-respond). If you change or remove the bucket first, Anthropic might not read your response file.

<Warning title="Keep the setup file with its state">
  Without the file, Terraform plans to destroy everything still in the state, and `prevent_destroy` no longer stops it.
</Warning>

1. Take every workspace off the bucket. On each workspace’s [Data retention](https://platform.claude.com/settings/privacy) page, select another bucket under **Sealed Safety Data storage**. Or, select the **Anthropic managed** card or, if listed, the **Legacy ZDR** card. Talk to your Anthropic account team before you select another bucket. If **Safety Case and Transcript storage** still shows this bucket, change that setting too. Then, save.

   * **If you can’t select the Anthropic managed card,** first change your organization’s [policy for new workspaces](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#set-organization-defaults).
   * Either card takes the workspace off EFS, and the **Anthropic managed** card can [turn Anthropic Human Review back on](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review). To use EFS again after **Legacy ZDR**, create a new workspace on the **Enterprise Frontier Safeguards** card.

2. Send test requests with no sensitive data from each workspace and run the [list command](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#confirm-that-objects-arrive) with `--recursive --long` until no new objects arrive. The **Draining** status can show early and has no end date, so don’t rely on it.

3. Stop any pipeline from applying the file, because a `terraform apply` creates Anthropic’s grants again. Then, talk to your Anthropic account team and wait for their answer. Anthropic still needs its access after it stops writing, to read what’s stored and to delete what has expired. Once the team confirms that Anthropic has stopped using the bucket, remove only Anthropic’s grants with your last apply’s values:

```bash
terraform destroy \
  -target=google_storage_bucket_iam_member.object \
  -target=google_storage_bucket_iam_member.list \
  -target=google_storage_bucket_iam_member.bucket \
  -target=google_storage_bucket_iam_member.review_object \
  -target=google_storage_bucket_iam_member.review_bucket \
  -var "project_id=acme-claude-storage" \
  -var "project_number=123456789012" \
  -var "organization_id=8a3f2c1e-5b7d-4e9a-a1c6-2f4e8d0b7c35" \
  -var "bucket_name=acme-claude-retention" \
  -var "region=us-east5"
```

The plan must add and change nothing, and destroy only `google_storage_bucket_iam_member` resources. Disabling the key doesn’t end Anthropic’s access, because the accounts can still list and delete.

</Where>

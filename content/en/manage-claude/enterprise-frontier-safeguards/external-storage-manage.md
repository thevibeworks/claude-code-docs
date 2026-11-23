---
title: Manage customer-owned storage
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage
description: Check your bucket's status, fix the bucket if it stops working, and change or stop using it.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

Use this page after a workspace uses [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage) with [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS). It covers how to check your bucket’s status, fix the bucket if it stops working, and change or stop using it.

## Bucket statuses

Find each bucket’s status under **Storage destinations** on the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console, with **Organization** selected at the top:

| Status | Meaning |
| ----- | ----- |
| **Needs setup** | <Where bucket="s3" label="Amazon S3">[**Test setup**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#test-the-setup)</Where> <Where bucket="gcs" label="Google Cloud Storage">[**Test setup**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-create-the-bucket)</Where> hasn’t passed. |
| **Ready** | Your bucket passed **Test setup**, and no workspace uses it. |
| **Active** | A workspace is set to use it. |
| **Failed last check** | The most recent check didn’t pass. See [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working). |
| **Draining** | No workspace uses it now, but one did. <Where bucket="s3" label="Amazon S3">[Keep your bucket, and Anthropic’s access to it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket).</Where> <Where bucket="gcs" label="Google Cloud Storage">[Keep your bucket, and Anthropic’s access to it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-stop-using-your-bucket).</Where> |
| **Deleting** | <Where bucket="s3" label="Amazon S3">Anthropic is [finishing a delete](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#delete-a-storage-destination) of this storage destination.</Where> <Where bucket="gcs" label="Google Cloud Storage">Anthropic is finishing a delete of this storage destination.</Where> You can’t use it. |

Anthropic checks a bucket before a workspace first uses it. Once a day, Anthropic also checks each bucket that a workspace uses or that shows as **Draining**. The daily check can pass while your bucket’s IAM roles for [Transcripts and Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage) fail.

If the daily check is inconclusive, the status and the last-checked time don’t change, even if your bucket has stopped working. A **Draining** bucket stays **Draining** even if it fails the check.

If a check fails, even for a **Draining** bucket, Anthropic usually emails the members of your organization who can manage encryption keys. On [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#set-up-your-account) and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#set-up-your-account), Anthropic instead usually emails the person who completed your organization’s setup.

<Where method="api" label="Admin API">

<Where bucket="s3" label="Amazon S3">

## Check your bucket

These Admin API requests use the credentials in [Authenticate your requests](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-authenticate) on Set up customer-owned storage.

Get one bucket to see its status:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/organizations/external_storage/estrg_01SDCCSbTxrXDpWc1phhtcfK \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: efs-2026-10-01"
  ```

  ```bash CLI
  ant beta:organization:external-storage retrieve \
    --external-storage-id estrg_01SDCCSbTxrXDpWc1phhtcfK
  ```

  ```python Python
  client = anthropic.Anthropic()

  storage = client.beta.organization.external_storage.retrieve(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  )

  print(f"status: {storage.status.type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const storage = await client.beta.organization.externalStorage.retrieve(
    "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  console.log(`status: ${storage.status.type}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var storage = await client.Beta.Organization.ExternalStorage.Retrieve(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  Console.WriteLine($"status: {storage.Status.Type.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  storage, err := client.Beta.Organization.ExternalStorage.Get(
  	context.Background(),
  	"estrg_01SDCCSbTxrXDpWc1phhtcfK",
  	anthropic.BetaOrganizationExternalStorageGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("status: %s\n", storage.Status.Type)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var storage = client.beta().organization().externalStorage()
      .retrieve("estrg_01SDCCSbTxrXDpWc1phhtcfK");

  IO.println("status: " + storage.status().type());
  ```

  ```php PHP
  $client = new Client();

  $storage = $client->beta->organization->externalStorage->retrieve(
      externalStorageID: 'estrg_01SDCCSbTxrXDpWc1phhtcfK',
  );

  echo "status: {$storage->status->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  storage = client.beta.organization.external_storage.retrieve("estrg_01SDCCSbTxrXDpWc1phhtcfK")

  puts "status: #{storage.status.type}"
  ```
</CodeGroup>

To list all your buckets, call `GET /v1/organizations/external_storage`. Results come newest first, 20 per page, or up to 1,000 per page if you pass `?limit=`. To get the next page, pass the response’s `next_page` as `?page=`.

`status.type` tells you where your bucket is in its lifecycle. Each value matches a status the Claude Console shows under [Bucket statuses](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health):

| API status | Console status | Meaning |
| ----- | ----- | ----- |
| `pending_configuration` | Needs setup | Registered, not yet activated. |
| `available` | Ready | Activated, and no workspace uses it. |
| `active` | Active | At least one workspace is set to use it. |
| `draining` | Draining | No workspace uses it now, but at least one did before. Keep your bucket, and Anthropic’s access to it, as [Change or stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket) describes. |

For `available`, `active`, and `draining`, `status` also has two fields. `healthy` says whether your bucket passed its latest check, and `last_checked_at` says when that check ran. For `draining`, it also has `removal_started`, which is `true` once a delete has begun. The Claude Console then shows **Deleting**. For `available` and `active`, a `healthy` value of `false` shows as **Failed last check** in the Claude Console. See [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).

`healthy` and `last_checked_at` are set when your bucket is activated, and when it passes Anthropic’s check before it’s attached as `safeguards_storage`. On Claude Platform, the daily check also sets them when it reaches a result (see [Bucket statuses](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health)). If a day’s check reaches no result, they stay as they were, so `healthy` can stay `true` even if your bucket stops working. Don’t rely on these fields alone. To notice a failure, watch for new objects under `slab/` or `safeguards-data/slab/` while you send requests.

</Where>

</Where>

## If your bucket stops working

<Where bucket="s3" label="Amazon S3">

To fix a bucket that stops working, check [your bucket’s status](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health), then restore your bucket or its IAM roles as this section describes.

If you selected your storage destination for a workspace in the last few hours and nothing has arrived under `slab/` or `safeguards-data/slab/`, [the change might not have taken effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take).

While Anthropic can’t write to a bucket that holds [Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored), the following happens:

* **Requests:** Requests keep working during a grace period of up to 24 hours. After that, Anthropic might refuse requests to the workspace.
* **Your Sealed Safety Data:** Anthropic retries writes for a limited time. It doesn’t send the data to Anthropic-managed storage instead.

To avoid losing data, keep the following in mind:

* To notice a failure, watch for new objects under `slab/` or `safeguards-data/slab/` while you send requests. Don’t wait for an email about a failure, and don’t rely on [your bucket’s status](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health) alone.
* Restore your bucket as soon as you can. If Anthropic can’t write to your bucket for more than about an hour, tell your Anthropic account team at once, and again when your bucket works. After you restore your bucket, Anthropic has to run a recovery, which isn’t guaranteed to succeed.
* On Claude Platform, about 72 hours after Sealed Safety Data was sent, Anthropic deletes whatever it hasn’t recovered. On Claude Platform on AWS, the time can be shorter, so tell your Anthropic account team as soon as you notice a failure.

How you restore your bucket depends on what changed:

* **The IAM roles:** If something removed Anthropic’s access to your bucket, restore the roles exactly as they were.

  * **CloudFormation:** Don’t delete or update your stack, and don’t create a second stack for this bucket. Instead, contact your Anthropic account team at once.
  * **Terraform:** Run the apply command from the header of your bucket’s Terraform file again, in the same folder as before, with the same region and values. If you don’t have the folder, contact your Anthropic account team at once.
  * **Your own tooling:** Create the roles again with the same names, and with the trust policies and permissions in the file from the **Connect storage** dialog. If you didn’t keep that file, contact your Anthropic account team.

* **Your bucket’s KMS key, if someone disabled it:** Enable it again.

* **Your bucket’s KMS key, if someone scheduled its deletion:** Cancel the deletion before the chosen waiting period of 7 to 30 days ends. Then, enable the key, because AWS leaves it disabled. After the waiting period, AWS KMS deletes the key, and nobody can read what it encrypted.

* **An AWS organization policy:** If a policy now keeps Anthropic out, [add Anthropic’s AWS account to it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#add-anthropic-to-the-rcp).

* **Your customer-managed key, if the workspace has one:** Follow [If your key stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys#if-your-key-stops-working).

If your roles have fixed names, such as `anthropic-efs-ingest`, restore that same setup, as this list describes. Don’t move it to a different setup file. For reference, use the file you deployed.

</Where>

<Where bucket="gcs" label="Google Cloud Storage">

See [If your Cloud Storage bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-if-your-bucket-stops-working).

</Where>

## Change or stop using your bucket

<Where bucket="s3" label="Amazon S3">

To move to a new bucket or to stop using your bucket, follow the steps in this section. Either way, keep your old bucket, and Anthropic’s access to it, until everything in your bucket is past [the retention period](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#retention-period) and your bucket is no longer listed under [**Storage destinations**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health). [Some objects stay in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-removes-data) after that.

Before you change or remove a workspace’s bucket, [respond to its open Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#respond-to-a-case) and [wait until they close](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#after-you-respond). If you change or remove the bucket first, Anthropic might not read your [response file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file).

While your bucket shows as **Draining**, keep the bucket, its versioning, its lifecycle rules, its KMS key, and its IAM roles in place. **Draining** doesn’t end by itself. It ends when you [delete the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#delete-a-storage-destination) or select the bucket for a workspace again. If you can’t delete it, talk to your Anthropic account team before you remove Anthropic’s access. On Claude Platform on AWS, you can’t delete a storage destination once a workspace has used it, so it keeps showing as **Draining**. Plan to keep your bucket and Anthropic’s access to it.

For as long as you keep your bucket, don’t disable its KMS key or schedule the key’s deletion. If you do, writes to your bucket and reads from it start to fail, so [restore the key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).

If you delete a bucket that a workspace has used, don’t create it again under the same name while its storage destination is listed. [Set up a new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-your-bucket) with a new name instead.

### Change your bucket

To move your workspaces to a new bucket, follow these steps. To move to a Google Cloud Storage bucket instead, talk to your Anthropic account team, because [Anthropic limits the number of buckets](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace). On Claude Platform on AWS, ask your Anthropic account team before you change your bucket.

<Warning>
  The move doesn’t take effect right away, as [Confirm that the change took effect](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take) describes. New Sealed Safety Data can still go to your old bucket for a while, even after objects arrive in your new one. Keep your old bucket, and Anthropic’s access to it, as [Change or stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#change-or-stop-using-your-bucket) describes. If you remove either early, you can lose new data.
</Warning>

1. [Create and connect your new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket-and-roles). Create it with a stack of its own or, with Terraform, in a folder of its own. Don’t update your existing stack to point at a new bucket, or Anthropic loses access to your old bucket while it still holds your data.
2. In each workspace that uses your old bucket, [select your new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#turn-on-efs-for-a-workspace) under **Sealed Safety Data storage** in the Claude Console. Don’t take your old bucket off the workspace first, or new Sealed Safety Data can go to Anthropic-managed storage. If the workspace also uses your old bucket under **Safety Case and Transcript storage**, select your new bucket under that setting too. Then, save.

<Where method="api" label="Admin API">

At step 1, [register](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-register) and [activate](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-activate) your new bucket. At step 2, [send the attach request](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-attach) with your new bucket’s ID instead. If `transcripts_storage` names your old bucket, set it to the new bucket’s ID in the same request.

</Where>

<Where method="console" label="Claude Console">

### Stop using your bucket

To stop using your bucket, take it off each workspace first, and remove Anthropic’s access to your bucket last. A workspace that stops sending Sealed Safety Data to your bucket leaves EFS.

<Steps>
  <Step title="Take your bucket off each workspace">
    On the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page, select a card other than **Enterprise Frontier Safeguards**, and save. By default, the **Anthropic managed** card turns [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) back on. The [Glossary](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) describes each card.

    To stop only Transcripts and Safety Cases, select **Not copied to your storage** under **Safety Case and Transcript storage** instead. If the bucket still receives Sealed Safety Data, don’t follow the rest of these steps.
  </Step>

  <Step title="Keep your bucket while it drains">
    Once you’ve taken it off every workspace, your bucket shows as **Draining** in **Storage destinations**. Keep your bucket, and Anthropic’s access to it, while the status is **Draining**. To end **Draining**, [delete the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#delete-a-storage-destination). On Claude Platform on AWS, your bucket stays **Draining**, so plan to keep it and Anthropic’s access to it. Don’t do the next step until the delete finishes or your Anthropic account team tells you to. Transcripts and Safety Cases already in your bucket stay there until your bucket’s lifecycle rules expire them. See [What’s in the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#whats-in-the-bucket).
  </Step>

  <Step title="Remove Anthropic’s access">
    To remove Anthropic’s access, remove your bucket’s IAM roles with the tool you used to create them. After you remove Anthropic’s access, Sealed Safety Data stays in your bucket until you delete it.

    <Tabs>
      <Tab title="CloudFormation">
        Delete your bucket’s stack. The stack’s name is in your deploy command: `anthropic-storage-<RoleDigest>`, or `anthropic-storage-<organization ID>` for a setup with fixed role names. Deleting the stack keeps your bucket and its key.
      </Tab>

      <Tab title="Terraform">
        Remove only your bucket’s roles and their policies, so that you keep your data. In the folder that holds your bucket’s Terraform file, run the removal command from the Terraform file’s header with the region and the values you used at setup.

        Expect warnings about `-target`. Check that every resource that the plan lists is an `aws_iam_role` or an `aws_iam_role_policy`, then type `yes`. A later apply creates the roles again.
      </Tab>

      <Tab title="Your own tooling">
        Delete that bucket’s IAM roles.
      </Tab>
    </Tabs>

    <Warning>
      Once the roles are gone, don’t select your bucket for a workspace again until they’re back. On Claude Platform on AWS, or if your roles have fixed names, Anthropic doesn’t check a **Draining** bucket before the save, so the save can succeed even though Anthropic can’t write to your bucket. If you used CloudFormation, deploying the template again doesn’t restore Anthropic’s access, so contact your Anthropic account team before you select your bucket.
    </Warning>
  </Step>
</Steps>

</Where>

<Where method="api" label="Admin API">

### Stop using your bucket

These Admin API requests use the credentials in [Authenticate your requests](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-authenticate) on Set up customer-owned storage.

To stop using your bucket, follow these steps in order:

1. Detach your bucket from each workspace.
2. Keep your bucket while it drains.
3. Delete its External Storage.
4. [Remove Anthropic’s access](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-remove-access).

To detach your bucket from a workspace, set each storage field that names your bucket to type `internal`. The fields are `inference_data_privacy.safeguards_storage` and `inference_data_privacy.transcripts_storage`, and you can set both in the same request. If you set `safeguards_storage` to type `internal`, the workspace switches to Anthropic-managed storage and comes off EFS. Anthropic might refuse a detach that leaves [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) off, so the following request also sets `inference_data_privacy.human_review` to type `enabled`, which turns Anthropic Human Review back on:

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
          "type": "internal"
        },
        "human_review": {
          "type": "enabled"
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
      type: internal
    human_review:
      type: enabled
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.workspaces.update(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      inference_data_privacy={
          "safeguards_storage": {"type": "internal"},
          "human_review": {"type": "enabled"},
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
        safeguards_storage: { type: "internal" },
        human_review: { type: "enabled" }
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
              SafeguardsStorage = new BetaInternalStorageParam(),
              HumanReview = new() { Type = BetaAnthropicHumanReviewParamType.Enabled },
          },
          Betas = ["efs-2026-10-01"],
      }
  );

  var type = workspace.InferenceDataPrivacy?.SafeguardsStorage?.Type.Raw();
  Console.WriteLine($"safeguards_storage: {type}");
  ```

  ```go Go
  client := anthropic.NewClient()

  internal := anthropic.NewBetaInternalStorageParam()
  workspace, err := client.Beta.Organization.Workspaces.Update(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.BetaOrganizationWorkspaceUpdateParams{
  		InferenceDataPrivacy: anthropic.BetaInferenceDataPrivacyUpdateParam{
  			SafeguardsStorage: anthropic.BetaStorageMemberParamUnion{OfInternal: &internal},
  			HumanReview: anthropic.BetaAnthropicHumanReviewParam{
  				Type: anthropic.BetaAnthropicHumanReviewParamTypeEnabled,
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
  import com.anthropic.models.beta.organization.workspaces.BetaInternalStorageParam;
  import com.anthropic.models.beta.organization.workspaces.WorkspaceUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = WorkspaceUpdateParams.builder()
          .inferenceDataPrivacy(BetaInferenceDataPrivacyUpdateParam.builder()
              .safeguardsStorage(BetaInternalStorageParam.builder().build())
              .humanReview(BetaAnthropicHumanReviewParam.builder()
                  .type(BetaAnthropicHumanReviewParam.Type.ENABLED)
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
          'safeguardsStorage' => ['type' => 'internal'],
          'humanReview' => ['type' => 'enabled'],
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
        type: :internal
      },
      human_review: {
        type: :enabled
      }
    },
    betas: ["efs-2026-10-01"]
  )

  puts "safeguards_storage: #{workspace.inference_data_privacy&.safeguards_storage&.type}"
  ```
</CodeGroup>

If [your organization’s policy](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#set-organization-defaults) requires customer-owned storage or requires Anthropic Human Review to be off, Anthropic refuses this request with `workspace_policy_violation` for a workspace that keeps Sealed Safety Data. Change the policy first, then send the request.

Like an attach, a detach [doesn’t take effect right away](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#how-long-changes-take).

After the last detach, your bucket’s status becomes `draining`. The status doesn’t leave `draining` by itself. It leaves when you attach the bucket again or delete its External Storage. Keep your bucket and Anthropic’s access to it until the delete finishes. If you can’t delete the External Storage, talk to your Anthropic account team before you remove Anthropic’s access. [Delete a storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#delete-a-storage-destination) says who can delete it and what to do first.

Then, delete your bucket’s External Storage. The External Storage is Anthropic’s record of your bucket, not your bucket itself. What happens depends on your bucket’s status:

* `pending_configuration` or `available`: Anthropic deletes the External Storage at once.
* `active`: Anthropic refuses the delete.
* `draining`: The first call returns a 400 error with `external_storage_in_use`. [Get the External Storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-check). If `status.removal_started` is `false`, the error’s message says what to do. If it’s `true`, you can’t undo the removal. Send the delete again every few minutes until it succeeds, which can take about 30 minutes. If it’s still refused after an hour, contact your Anthropic account team. A 503 error means that nothing changed, so try again later.

If [your organization’s policy](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#set-organization-defaults) lists this bucket, Anthropic refuses the delete until you remove the bucket from the policy. Once a workspace has used your bucket, treat your bucket name, KMS key, and IAM roles as [tied to your organization](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#before-you-begin).

<CodeGroup>
  ```bash cURL
  curl -X DELETE https://api.anthropic.com/v1/organizations/external_storage/estrg_01SDCCSbTxrXDpWc1phhtcfK \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: efs-2026-10-01"
  ```

  ```bash CLI
  ant beta:organization:external-storage delete \
    --external-storage-id estrg_01SDCCSbTxrXDpWc1phhtcfK
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted = client.beta.organization.external_storage.delete(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  )

  print(f"id: {deleted.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deleted = await client.beta.organization.externalStorage.delete(
    "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  console.log(`id: ${deleted.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deleted = await client.Beta.Organization.ExternalStorage.Delete(
      "estrg_01SDCCSbTxrXDpWc1phhtcfK"
  );

  Console.WriteLine($"id: {deleted.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deleted, err := client.Beta.Organization.ExternalStorage.Delete(
  	context.Background(),
  	"estrg_01SDCCSbTxrXDpWc1phhtcfK",
  	anthropic.BetaOrganizationExternalStorageDeleteParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deleted.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deleted = client.beta().organization().externalStorage()
      .delete("estrg_01SDCCSbTxrXDpWc1phhtcfK");

  IO.println("id: " + deleted.id());
  ```

  ```php PHP
  $client = new Client();

  $deleted = $client->beta->organization->externalStorage->delete(
      externalStorageID: 'estrg_01SDCCSbTxrXDpWc1phhtcfK',
  );

  echo "id: {$deleted->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  deleted = client.beta.organization.external_storage.delete("estrg_01SDCCSbTxrXDpWc1phhtcfK")

  puts "id: #{deleted.id}"
  ```
</CodeGroup>

#### Remove Anthropic’s access

To remove Anthropic’s access, remove your bucket’s IAM roles with the tool you used to create them. After you remove Anthropic’s access, Sealed Safety Data stays in your bucket until you delete it. In a bucket that holds Transcripts and Safety Cases, the lifecycle rules keep expiring those files until you change the rules.

<Tabs>
  <Tab title="CloudFormation">
    Delete your bucket’s stack. The stack’s name is in your deploy command: `anthropic-storage-<RoleDigest>`, or `anthropic-storage-<organization ID>` for a setup with fixed role names. Deleting the stack keeps your bucket and its key.
  </Tab>

  <Tab title="Terraform">
    Remove only your bucket’s roles and their policies, so that you keep your data. In the folder that holds your bucket’s Terraform file, run the removal command from the Terraform file’s header with the region and the values you used at setup.

    Expect warnings about `-target`. Check that every resource that the plan lists is an `aws_iam_role` or an `aws_iam_role_policy`, then type `yes`. A later apply creates the roles again.

    `terraform destroy` without `-target` fails and destroys nothing, because the key, the bucket, its settings, and its bucket policy carry `prevent_destroy`.
  </Tab>

  <Tab title="Your own tooling">
    Delete that bucket’s IAM roles.
  </Tab>
</Tabs>

<Warning>
  Once the roles are gone, don’t select your bucket for a workspace again until they’re back. On Claude Platform on AWS, or if your roles have fixed names, Anthropic doesn’t check a **Draining** bucket before the save, so the save can succeed even though Anthropic can’t write to your bucket. If you used CloudFormation, deploying the template again doesn’t restore Anthropic’s access, so contact your Anthropic account team before you select your bucket.
</Warning>

</Where>

</Where>

<Where bucket="gcs" label="Google Cloud Storage">

Talk to your Anthropic account team before you move to a new bucket, because [Anthropic limits the number of buckets](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace).

See [how to stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-stop-using-your-bucket).

</Where>

<Where bucket="s3" label="Amazon S3">

## Delete a storage destination

To end Anthropic’s use of a bucket that shows as **Draining**, delete its storage destination. On Claude Platform on AWS, you can’t delete a storage destination once a workspace has used it. On Claude Platform, you can delete one for an Amazon S3 bucket only if Anthropic’s records show that your organization uses Claude for internal tools alone. If you can’t delete it, talk to your Anthropic account team before you remove Anthropic’s access. You can’t undo a delete.

<Where cloud="claude" label="Claude Platform">

Before you delete it, do the following:

* **Wait until `slab/` and `media/` are empty,** at the top of the bucket and under `safeguards-data/`. Most of what’s there leaves by itself a few days after [the retention period](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#retention-period) ends for the last data sent there. Don’t delete anything before then. You’d lose data, and Anthropic doesn’t warn you. If [objects stay](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-removes-data) after that, delete them without a version ID. Old versions and delete markers count too, so wait for the lifecycle rules to clear them, at least 3 days after each delete.
* **Keep Anthropic’s access** until the delete finishes, because Anthropic looks in the bucket first.

<Warning>
  Deleting a storage destination removes nothing from your bucket. Transcripts, Safety Cases, and your team’s responses can still be there, and anyone with access to the bucket and its key can read them. Empty the bucket, including earlier file versions, before anyone uses it for customer-owned storage again.
</Warning>

<Where method="console" label="Claude Console">

Under **Storage destinations** on the [Data retention](https://platform.claude.com/settings/privacy) page, select **Delete** in the row’s menu. If the Claude Console refuses the delete, its message says why. If the row is still listed after a few minutes, select **Finish deleting** in its menu. If it’s still listed after an hour, contact your Anthropic account team. Once the row has gone, follow the last step of [Stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#stop-using-your-bucket) to remove Anthropic’s access. You can then delete your bucket.

</Where>

<Where method="api" label="Admin API">

Send the delete request, as [Stop using your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-stop) describes. It takes more than one call. Once it succeeds, [remove Anthropic’s access](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#api-remove-access). You can then delete your bucket.

</Where>

</Where>

</Where>

## What removes data from your bucket

<Where bucket="s3" label="Amazon S3">

<Where cloud="claude" label="Claude Platform">

Anthropic deletes objects under `slab/` and `media/` through the [maintenance role](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-roles). Anthropic deletes an object under `slab/` only after everything in that object is past its retention period.

</Where>

If your bucket uses `safeguards-data/`, this section and [What protects object versions in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-protects-object-versions) apply to the same prefixes under `safeguards-data/`.

Because your bucket keeps versions, a delete by the maintenance role only adds a delete marker, and the old version stays. The lifecycle rules permanently delete each old version at least 3 days later, and then remove the delete marker.

Some objects stay in your bucket, because no lifecycle rule in the setup files deletes them:

* **Under `slab/`:** Anthropic looks through each day’s objects for ones to delete, but only for a limited number of days. An object that it hasn’t deleted by then stays in your bucket.
* **Under `slab-manifest/`:** Anthropic’s software never deletes objects under this prefix, so they build up.
* **Under `media/`:** An interrupted or repeated write can leave objects that Anthropic no longer tracks. They stay encrypted. A monthly cleanup looks for them, but it can leave them in place.

Leave the objects Anthropic writes as they are, including these leftover objects while a workspace uses your bucket. If you can’t keep them, contact your Anthropic account team, unless you’re [deleting the storage destination](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#delete-a-storage-destination).

Change your bucket’s lifecycle rules only by setting [`ReviewExpiryDays`](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#template-reference). Don’t turn on S3 Object Lock or add a lifecycle rule that expires or archives objects. If you do, your bucket fails [**Test setup**](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#test-the-setup) and [Anthropic’s daily check](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health).

### What protects object versions in your bucket

Only the lifecycle rules can permanently delete an object version under `slab/`. This holds as long as versioning is on and the bucket policy keeps its `NobodyHardDeletesSlabVersions` statement. The statement denies `s3:DeleteObjectVersion` under `slab/` to every person and role, Anthropic’s included.

Anthropic’s roles can’t change the bucket policy, versioning, or the lifecycle rules.

The bucket policy has no statement like `NobodyHardDeletesSlabVersions` for other prefixes. The media-erasure role can permanently delete object versions under `media/`. The transcripts and review roles can permanently delete Transcripts, Safety Cases, summaries, and Safety Notices, but not your team’s responses.

</Where>

<Where bucket="gcs" label="Google Cloud Storage">

Your bucket’s own lifecycle rules delete each object of Sealed Safety Data after it’s 28 days old. Don’t change them.

</Where>

<Where bucket="s3" label="Amazon S3">

## Anthropic’s calls in AWS CloudTrail

Each time Anthropic assumes one of your roles, AWS CloudTrail records the call in your account. You can find those records in CloudTrail **Event history**:

* **Where to look:** Look in `us-east-2`. **Event history** shows one AWS region at a time and keeps those records for 90 days with no setup.
* **What a record shows:** Each record carries a source identity that names the kind of work, and every later call in that session carries it too.
* **What Event history leaves out:** **Event history** doesn’t show reads, writes, and deletes of objects, which are Amazon S3 data events. To have CloudTrail record them, turn on data event logging for your bucket. AWS charges for that logging.

### Calls from Test setup and the daily check

**Test setup** and the [daily check](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health) send requests with the external ID or the source identity missing or wrong. Your roles must refuse them, so those refusals are expected. If a role refuses a request that has your external ID and a source identity that the role accepts, that refusal isn’t expected. It might mean that [an AWS organization policy blocks Anthropic](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic).

</Where>

<Where method="api" label="Admin API">

## Troubleshooting

<AccordionGroup>
  <Accordion title="Every setup request returns an error or says that inference_data_privacy isn’t a valid field">
    The requests that set up External Storage return an error until your organization has [access to Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access). They also return one when they don’t send the beta header. With an OAuth bearer token, they also return one when the token lacks the `org:admin` scope. Without the header, the attach and detach requests return a different error, saying that `inference_data_privacy` isn’t a valid field. If that happens with access and the header in place, contact your Anthropic account team.
  </Accordion>

  <Accordion title="The activate request returns failed checks">
    If a check fails, the request returns a 400 error with `error.details.error_code` set to `storage_verification_failed`. `error.details.failed_checks` lists each problem as an object with `check`, `role`, and `message`. Fix each problem that `failed_checks` lists and call activate again. The `already_registered` check has its own fix, later in this item.

    If the first `message` starts with “Anthropic could not assume the verify role”, check the following in order:

    1. Look at the names of your IAM roles. A new bucket whose roles have fixed names, such as `anthropic-efs-ingest`, fails this check. For such a bucket, delete this External Storage, [register a new bucket name](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-register), and use the file from [Get your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api#get-the-setup-file).
    2. Otherwise, check that you created your setup from the file in [Get your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api#get-the-setup-file).
    3. Check whether [an AWS organization policy is blocking Anthropic](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#if-an-aws-organization-policy-blocks-anthropic).

    If `failed_checks` holds one object with `check` set to `already_registered`, another Anthropic organization has used part of this setup, or the bucket name is in use in a different AWS account. External Storage of a deleted organization can still count as one of these uses.

    If another organization has used this AWS account, you can keep the account. First, check that you deployed the file from [Get your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api#get-the-setup-file) for this bucket, then call activate again.

    If the check still fails, or no other organization has used this AWS account, use a new bucket name, with a key and roles of its own, and [register the new bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-register). If the new bucket fails in the same way, tell your Anthropic account team.

    [The attach request](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-attach) can fail with the `already_registered` check too. If the check fails for `safeguards_storage`, the fix is the same. If the check fails for `transcripts_storage`, contact your Anthropic account team. If your roles have fixed names, an `already_registered` failure at attach can also mean that another organization has used this AWS account.

    If the activate request or [the attach request](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#api-attach) returns a 503 error with no `error.details.error_code`, Anthropic couldn’t run its check, so try again in a few minutes. If it keeps happening, tell your Anthropic account team.
  </Accordion>

  <Accordion title="The attach request returns an error about Anthropic’s approval">
    Anthropic can approve customer-owned storage for your whole organization or for chosen workspaces. This request can return two errors about that approval, and in both cases nothing changes. Registering your bucket and activating it can return the same two codes. No workspace is involved at those steps, so the message is about your organization’s approval, not a workspace’s.

    | What you get | What it means | What to do |
    | ----- | ----- | ----- |
    | A 400 error with `error.details.error_code` set to `grant_required` | Anthropic’s approval doesn’t cover this workspace. The message says the workspace isn’t approved to use External Storage and to contact your Anthropic account team. | Ask your Anthropic account team to have the workspace approved, then send the request again. |
    | A 503 error with `error.details.error_code` set to `authorization_check_unavailable`, and a `Retry-After` header | Anthropic’s approval couldn’t be checked at that moment. | Wait the number of seconds in the `Retry-After` header, then send the same request again. |

    Before you contact your Anthropic account team, check that an Organization Admin has [accepted the EFS and Enterprise Data Controls terms](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access). A new approval can take a short while to reach the API, so a request sent right after you get it can still return `grant_required`. Send it again, and contact your Anthropic account team if it keeps happening.

    The attach request can also return `approval_required`. To get Anthropic’s approval to turn off Anthropic Human Review, see [Set up Enterprise Frontier Safeguards on Claude Platform](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#get-access).
  </Accordion>

  <Accordion title="The attach request refuses your bucket in transcripts_storage">
    The request returns a 400 error. A failed check changes nothing, so a `safeguards_storage` in the same request isn’t attached either. What to do depends on the error:

    * If `error.details.error_code` is `storage_verification_failed` and `error.details.failed_checks` holds one object whose `check` is `transcripts_support`, sending the request again doesn’t help. The object’s `message` says why. [Troubleshooting for customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#troubleshooting) says what to do.
    * If `check` is `already_registered`, or the error says that storage can’t be attached for transcripts yet, contact your Anthropic account team.
    * For any other check, fix what its `message` says and send the request again.

    In each case, you can send the same request without `transcripts_storage`. If Anthropic accepts that request, only `safeguards_storage` is attached. If the request without `transcripts_storage` returns `transcripts_storage_required`, use a bucket that can receive Transcripts and Safety Cases, or contact your Anthropic account team.
  </Accordion>

  <Accordion title="Your bucket’s default encryption key changed">
    If your bucket’s default encryption key changed after you activated the bucket and no workspace uses the bucket yet, Anthropic refuses the attach, because it checks the bucket again at that point. To use another key with IAM roles you created with your own tooling, follow these steps:

    1. Delete this External Storage.
    2. Let every role except `media-erasure` use the new key, including where the `transcripts` and `review` roles’ write conditions name the key.
    3. In the new key’s policy, let Amazon S3 call `kms:GenerateDataKey`, as the key policy in your setup file does, so that S3 Inventory can deliver its daily reports.
    4. Set your bucket’s default encryption to the new key, named by its key ARN. The key must meet the requirements for the bucket’s key in the **Your own tooling** tab of [Create your bucket and its KMS key](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#create-the-bucket).
    5. Register your bucket again and activate it.

    Anthropic’s CloudFormation template and Terraform file set the roles up for one key and have no supported way to use another. For a setup with fixed role names, such as `anthropic-efs-ingest`, don’t register the same bucket again. Create a new bucket with the file from [Get your setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api#get-the-setup-file).
  </Accordion>

  <Accordion title="Only some of a workspace request’s changes were saved">
    If the response says some of the request’s changes might have been saved and others not, send the same request again. Changes already saved aren’t repeated.

    Don’t resend a create request that returns `workspace_created_incomplete`, because the workspace already exists and a second create makes a second workspace. Instead, follow the response’s message, which usually says to update the workspace that `error.details.workspace_id` names. In an organization with a Legacy Zero Data Retention (ZDR) arrangement, if the message says to update `inference_data_privacy`, archive the workspace and create it again.
  </Accordion>
</AccordionGroup>

</Where>

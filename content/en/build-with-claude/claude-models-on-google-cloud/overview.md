---
title: Claude Models on Google Cloud
url: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview
description: Compare Claude Models on Google Cloud (Anthropic managed) and Claude Models on Google Cloud (Google managed), and find out which one you use.
---

You can use Claude through your Google Cloud project in two ways:

* **[Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed):** Anthropic operates the [Claude API](https://platform.claude.com/docs/en/api/overview).
* **[Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed):** Google operates Claude models as part of Google Cloud's Agent Platform.

## How the two Google Cloud offerings differ

The following table compares Claude Models on Google Cloud (Anthropic managed) with Claude Models on Google Cloud (Google managed).

| Aspect                                           | [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)                                                        | [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)                                                                                                 |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API surface**                                  | Claude API endpoints<br />`/v1/{endpoint}`                                                                                                                                                                        | Agent Platform prediction endpoints                                                                                                                                                                                                                  |
| **Request format**                               | Same as the Claude API<br />`model` in the request body<br />`anthropic-version` header                                                                                                                           | `model` in the URL<br />`anthropic_version` in the request body                                                                                                                                                                                      |
| **Streaming**                                    | `"stream": true` in the request body                                                                                                                                                                              | A separate `:streamRawPredict` endpoint                                                                                                                                                                                                              |
| **Location**                                     | `global`<br />See [Project, location, and workspace resolution](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#project-location-and-workspace-resolution). | A global, multi-region, or regional endpoint<br />See [Global, multi-region, and regional endpoints](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed#global-multi-region-and-regional-endpoints). |
| **Model IDs for models earlier than Claude 4.6** | The Claude API ID<br />Example: `claude-haiku-4-5-20251001`                                                                                                                                                       | The Claude API ID, with `@` in place of the hyphen before the snapshot date<br />Example: `claude-haiku-4-5@20251001`<br />See [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).           |
| **Services to enable on your project**           | See [Set up your account](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#set-up-your-account).                                                             | The Agent Platform API<br />`aiplatform.googleapis.com`                                                                                                                                                                                              |
| **Anthropic organization**                       | A new Anthropic organization for your project                                                                                                                                                                     | None                                                                                                                                                                                                                                                 |
| **Billing**                                      | Google Cloud Marketplace                                                                                                                                                                                          | Google Cloud, as Agent Platform usage                                                                                                                                                                                                                |
| **Rate limits**                                  | Managed by Anthropic                                                                                                                                                                                              | Managed by Google Cloud                                                                                                                                                                                                                              |

## What both offerings share

* **Credentials:** Both offerings use Google Cloud credentials, including Application Default Credentials. You grant access to each offering separately, through its own IAM roles.

  * [Credentials for Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#authentication)
  * [Credentials for Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed#before-making-api-calls)

* **Billing:** Charges for both offerings appear on your Google Cloud bill.

  * [Billing for Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#billing)
  * [Billing for Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed#billing)

* **Model IDs:** Claude 4.6 and later models use their Claude API IDs on both offerings. See [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

* **SDKs:** Anthropic's [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) support both offerings.

## Moving between the two offerings

Follow the steps for whichever offering you're moving to:

* [Steps for moving to Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#migrating-from-google-managed)
* [Steps for moving to Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed#migrating-from-anthropic-managed)

## Which offering are you using?

The following table lists values that identify Claude Models on Google Cloud (Anthropic managed) and Claude Models on Google Cloud (Google managed). Find a value you already have. For example, look for the host in your request URLs or the SDK client in your code. The heading of that value's column is your offering.

| What to check                                               | [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)                                                                                                                           | [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)                                                                                                                                                                      |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Where your requests go**                                  | `claude.googleapis.com`<br />The URL includes your workspace ID.<br />It ends in a Claude API path, such as `.../invoke/v1/messages`.                                                                                                                                                | One of these Agent Platform hosts:<br />`aiplatform.googleapis.com`<br />`aiplatform.us.rep.googleapis.com`<br />`aiplatform.eu.rep.googleapis.com`<br />`{region}-aiplatform.googleapis.com`<br />The URL path contains `.../publishers/anthropic/models/{model}`.<br />It ends in `:rawPredict` or `:streamRawPredict`. |
| **SDK client in your code**                                 | `AnthropicGoogleCloud` (csharp: `AnthropicGoogleCloudClient`; go: `googlecloud.NewClient()`; java: `GoogleCloudBackend`; php: `Anthropic\GoogleCloud\Client`; ruby: `Anthropic::GoogleCloudClient`)<br />In every SDK, the client name contains `GoogleCloud` (all lowercase in Go). | `AnthropicVertex` (csharp: `AnthropicVertexClient`; go: `vertex.WithGoogleAuth()`; java: `VertexBackend`; php: `Anthropic\Vertex\Client`; ruby: `Anthropic::VertexClient`)<br />In every SDK, the client name contains `Vertex` (all lowercase in Go).                                                                    |
| **IAM roles that grant access**                             | `roles/claude.admin`<br />`roles/claude.user`<br />`roles/claude.viewer`                                                                                                                                                                                                             | Agent Platform IAM roles                                                                                                                                                                                                                                                                                                  |
| **Management console**                                      | The Claude Console, at `platform.claude.com`<br />You open it from the Google Cloud console.                                                                                                                                                                                         | The Google Cloud console                                                                                                                                                                                                                                                                                                  |
| **Where each offering appears in the Google Cloud console** | The option labeled **Anthropic managed**<br />See [Set up your account](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#set-up-your-account).                                                                                  | Claude models in [Model Garden](https://cloud.google.com/model-garden)                                                                                                                                                                                                                                                    |

If you call `api.anthropic.com` with an API key, you use neither offering. To move those calls to Claude Models on Google Cloud (Anthropic managed), see [Moving from an existing Anthropic organization](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#moving-from-an-existing-anthropic-organization).

## Next steps

<CardGroup cols={2}>
  <Card title="Claude Models on Google Cloud (Anthropic managed)" icon="cloud" href="https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed">
    Set up your account and make your first request.
  </Card>

  <Card title="Claude Models on Google Cloud (Google managed)" icon="cloud" href="https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed">
    Install an SDK and make your first request.
  </Card>

  <Card title="IAM permissions for Claude Models on Google Cloud (Anthropic managed)" icon="lock" href="https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions">
    Look up permissions, roles, and audit log types.
  </Card>
</CardGroup>

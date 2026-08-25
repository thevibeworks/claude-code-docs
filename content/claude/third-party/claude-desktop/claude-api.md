> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with the Claude API

> Configure Claude Desktop on 3P to send inference directly to Anthropic's Claude API instead of a cloud-provider-hosted Claude deployment

To use Anthropic's Claude API directly as the inference provider, set [`inferenceProvider`](/docs/third-party/claude-desktop/configuration#inferenceprovider) to `anthropic` and supply an API key as described below. This is the first-party path: inference goes straight to Anthropic rather than to a Claude deployment hosted in your Amazon, Google, or Microsoft tenancy.

<Note>
  When `inferenceProvider` is `anthropic`, inference traffic goes to Anthropic's API endpoints rather than staying within your cloud provider. The data-residency and compliance statements on these pages do not apply to this option.
</Note>

## Choose an authentication approach

There are three options. With neither a static key nor a credential helper configured, each user sees **Sign in with Claude Console** on first launch: the app opens the browser, the user signs in and selects a Claude Console (API) organization, and the app creates a personal API key for them and stores it encrypted on the device until it is revoked in Console; usage is billed to that Console organization. Alternatively, place a static API key in the managed configuration as `inferenceAnthropicApiKey`, or, where static keys aren't permitted, set [`inferenceCredentialHelper`](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that fetches a short-lived credential at runtime; see [Write a credential helper](/docs/third-party/claude-desktop/credential-helper). Browser sign-in reaches `platform.claude.com` in addition to `api.anthropic.com`.

## Configure the app

### Configuration keys

| Setting                                                                              | Type     | Availability    | Default | Description                                                                                   |
| ------------------------------------------------------------------------------------ | -------- | --------------- | ------- | --------------------------------------------------------------------------------------------- |
| <span id="inferenceanthropicapikey" />Claude API key<br />`inferenceAnthropicApiKey` | `string` | MDM + Bootstrap | —       | Leave blank to fetch a key via browser sign-in, or to supply the key via a credential helper. |

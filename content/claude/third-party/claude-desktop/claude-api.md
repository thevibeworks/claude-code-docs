> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with the Claude API

> Configure Claude Desktop on 3P to send inference directly to Anthropic's Claude API instead of a cloud-provider-hosted Claude deployment

To use Anthropic's Claude API directly as the inference provider, set [`inferenceProvider`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceprovider) to `anthropic` and choose how users authenticate, as described in [Choose an authentication approach](#choose-an-authentication-approach). This is the first-party path: inference goes straight to Anthropic rather than to a Claude deployment on Google Cloud's Agent Platform, Amazon Bedrock, or Microsoft Foundry.

> [!NOTE]
>
> When `inferenceProvider` is `anthropic`, inference traffic goes to Anthropic's API endpoints rather than staying within your cloud provider. The data-residency and compliance statements on these pages do not apply to this option.

## Choose an authentication approach

There are three options. With neither a static key nor a credential helper configured, each user sees **Sign in with Claude Console** on first launch: the app opens the browser, the user signs in and selects a Claude Console (API) organization, and the app keeps that sign-in encrypted on the device and renews it as needed, without creating an API key. Usage is billed to that Console organization, and about a month after a user signs in, the app asks them to sign in again. Alternatively, place a static API key in the managed configuration as `inferenceAnthropicApiKey`, or, where static keys aren't permitted, set [`inferenceCredentialHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that fetches a short-lived credential at runtime; see [Write a credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper.md). Browser sign-in reaches `platform.claude.com`, `hcaptcha.com`, and `*.hcaptcha.com` in addition to `api.anthropic.com`.

Claude Desktop versions before 3.1623.0 created a personal API key in the Console organization when a user signed in with Claude Console, and the app doesn't delete those keys. A device that signed in that way and then updates to 3.1623.0 or later keeps using its key until you revoke the key in Claude Console or the user signs out. The device's next sign-in creates no key.

[Code](https://claude.com/docs/third-party/claude-desktop/code.md) sessions also ask Anthropic for the Claude Code [server-managed settings](https://code.claude.com/docs/en/server-managed-settings) of the organization that owns the credential. See [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) for how they combine with your Claude Desktop configuration.

## Which devices offer the Claude API account sign-in

On a device with no Claude Desktop configuration, the standard sign-in screen in Claude Desktop 3.1623.1 or later also links to a screen titled **Use your Claude API account**. There a user can click **Sign in with Claude Console** or enter an API key, with no setup from you.

Claude Desktop doesn't offer or accept that sign-in on a device where an [MDM profile or registry policy](https://claude.com/docs/third-party/claude-desktop/mdm.md#4-deploy-the-configuration), or the [root-owned configuration file on Linux](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file), manages the configuration. To confirm that a profile manages a device's configuration, check that the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer > Configure Third-Party Inference…**) opens read-only on that device. If the window is still editable, the profile doesn't manage the configuration, for example because it sets only [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence). A profile takes effect at the app's next launch, and until then a running app can still offer and accept the sign-in.

Under a profile that manages the configuration, the app ignores any configuration that an earlier Claude API account sign-in saved. A profile can itself select the Claude API with no static key or credential helper. Users then sign in with **Sign in with Claude Console**, and each selects the Console organization that their usage is billed to, as described under [Choose an authentication approach](#choose-an-authentication-approach). A user who already signed in with Claude Console keeps that sign-in, and the Console organization they chose, until the app next asks them to sign in.

## Configure the app

### Configuration keys

[Entry labels](https://claude.com/docs/third-party/claude-desktop/configuration.md#entry-labels) says what each label means.

#### `inferenceAnthropicApiKey`

stringSince 1.8089.0

**Claude API key.** Leave blank to sign in with your browser, or to supply the key via a credential helper.

***

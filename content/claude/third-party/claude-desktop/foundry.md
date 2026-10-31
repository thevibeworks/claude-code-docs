> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with Microsoft Foundry

> Set up Microsoft Foundry, choose an authentication path for your organization, and configure Claude Desktop on 3P to use Claude models on Microsoft Foundry

This page walks an IT administrator through a Microsoft Foundry deployment: creating the Microsoft Foundry resource, choosing the authentication path that fits your organization, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

> [!NOTE]
>
> Microsoft Foundry offers Claude models in two hosting options, Hosted on Azure and Hosted on Anthropic, and you choose one when you configure the model deployment in Microsoft Foundry. Under both options, Anthropic operates the Claude models and handles conversation data as an independent processor for Microsoft. Your use of Claude through Microsoft Foundry is subject to Anthropic's data use terms.
>
> Deployments hosted on Azure run inference in an Anthropic-operated service on Azure infrastructure, not in your Azure tenant, and prompts and completions remain within Azure. The only data the service sends out of Azure to Anthropic is usage metadata and any content that Anthropic's safety systems flag. Deployments hosted on Anthropic send prompts and completions to Anthropic's own infrastructure for inference. See [hosting options for Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options) for details.

## Choose an authentication approach

| Scenario | Use | Per-user identity | Notes |
| - | - | - | - |
| Proof of concept, single team | [API key](#api-key) (`inferenceFoundryApiKey`) | No (shared key) | A long-lived secret distributed in the managed profile. Simplest to start. |
| Broad rollout with per-user identity | [In-app Entra ID sign-in](#in-app-entra-id-sign-in) (`inferenceFoundryTenantId`, `inferenceFoundryClientId`, `inferenceFoundryAuthFlow`) | Yes | Users sign in with their Entra ID account inside the app, through a device code, the system browser, or the OS identity broker. The device-code flow requires app version 1.9255.0 or later; the browser flow requires app version 1.19367.0 or later. |
| Your organization already has tooling that obtains a Microsoft Foundry credential | [Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper) (`inferenceCredentialHelper`) | Depends on what the helper obtains | An executable that prints the credential to stdout at runtime. |

## Set up Azure

These steps are performed once per Azure subscription. You need permission to create resources and, for in-app sign-in, to register an application in Microsoft Entra ID.

**1. Create a Microsoft Foundry resource**

In the Azure portal, create a Microsoft Foundry resource in your subscription. Record the **resource name**; the app constructs the endpoint as `<resource-name>.services.ai.azure.com`. If the app should reach Microsoft Foundry through a gateway or proxy you operate instead, see [Route requests through a gateway](#route-requests-through-a-gateway). The resource name is still required in that case.

**2. Deploy the Claude models**

In the Microsoft Foundry portal for your resource, deploy the Claude models you intend to serve. Record each **deployment name**; you will list these in `inferenceModels`.

**3. Obtain an API key (API-key approach only)**

If you chose the API-key approach, copy one of the resource's keys from the Azure portal. You will place it in the managed configuration in [Configure the app](#configure-the-app).

**4. Register an Entra ID application (in-app sign-in only)**

If you chose in-app Entra ID sign-in, register an application in the [Microsoft Entra admin center](https://entra.microsoft.com) under **Identity → Applications → App registrations → New registration**. On the registration:

* Under **API permissions**, select **Add a permission**, find **Azure Cognitive Services** in the API picker, and add the **Delegated** permission **user\_impersonation** so the issued token is accepted by your Microsoft Foundry resource. (The app requests this permission as the scope `https://cognitiveservices.azure.com/.default`.) All three sign-in flows need it. After adding the permission, select **Grant admin consent**; in tenants that disable user consent, sign-in fails with error code `AADSTS65001` until consent is granted.
* Under **Authentication**, complete the setup for the sign-in flow you plan to use (see [In-app Entra ID sign-in](#in-app-entra-id-sign-in) for how the flows differ):
  * For the device-code flow (the default), enable **Allow public client flows**. Entra ID rejects device-code sign-in without it.
  * For the browser flow (`inferenceFoundryAuthFlow` set to `browser`), select **Add a platform → Mobile and desktop applications** and add the redirect URI `http://127.0.0.1/callback`. Use the literal address `127.0.0.1`, not `localhost`: Entra ID matches the scheme, host, and path exactly and ignores only the port. The browser flow completes sign-in without **Allow public client flows**. Conditional Access policies that block the device-code authentication flow do not apply to the browser flow.
  * For the broker flow (`inferenceFoundryAuthFlow` set to `broker`), enable **Allow public client flows** and add the platform's broker redirect URI under **Mobile and desktop applications**. See [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application) on the OS identity broker page for the redirect URI values and why the public-client setting is required.

Record the **Directory (tenant) ID** and **Application (client) ID**.

Grant the users or groups who will sign in a role on the Microsoft Foundry resource that permits inference (for example, **Cognitive Services User**).

## Prepare devices

What each end-user device needs depends on the authentication approach you chose.

### API key

No per-device preparation is required. Place the resource's API key in the managed configuration as `inferenceFoundryApiKey`.

### In-app Entra ID sign-in

Distribute `inferenceFoundryTenantId` and `inferenceFoundryClientId` in the managed configuration. To use the browser or broker flow instead of the default device-code flow, also set `inferenceFoundryAuthFlow` to `browser` or `broker`.

The device-code and browser flows need no per-device preparation. The broker flow signs in through the operating system's native Microsoft identity broker, so each device must meet the platform requirements on the [OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#prepare-devices) page.

When the tenant and client IDs are set and `inferenceCredentialKind` is `interactive`, the app shows a **Sign in with Microsoft** page at first launch. Clicking the button starts a sign-in against `login.microsoftonline.com`; what the user sees depends on `inferenceFoundryAuthFlow`:

* **Device code** (the key is unset or `device-code`): the app displays a short verification code and opens the Microsoft sign-in page in the default browser, where the user enters the code and approves access.
* **Browser** (the key is `browser`): the app opens the Microsoft sign-in page in the default browser, where the user signs in and approves access. The browser shows a confirmation page and the user switches back to the app; there is no code to enter.
* **Broker** (the key is `broker`): the app opens the operating system's native Microsoft account picker, where the user selects or signs in to a work account. The dialog closes and the app returns to Cowork; nothing opens in the browser. Because the broker issues the token, sign-in satisfies Conditional Access policies that require a compliant or managed device or token protection, which the other two flows cannot satisfy on their own. See [Sign in through the OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md) for what the broker is and when to choose it.

On success, the app returns to Cowork. For the device-code and browser flows the app stores the refresh token encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows), and both flows store the same token against the same app registration, so switching between them later does not itself prompt users to sign in again. For the broker flow the operating system's broker holds the credential, and the app stores only a reference to the signed-in account.

If the app can no longer renew the credential silently, it shows a **Sign in again** prompt; clicking it reopens the configured sign-in flow. For the device-code and browser flows this happens when the stored refresh token expires or is revoked. For the broker flow it happens when the broker can no longer renew the token silently.

`inferenceFoundryTenantId`, `inferenceFoundryClientId`, and `inferenceFoundryAuthFlow` can be set through the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#choose-how-users-authenticate-to-your-provider), an MDM profile, or a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md). When a bootstrap server delivers `inferenceFoundryResource`, `inferenceFoundryTenantId`, or `inferenceFoundryClientId`, the values are among the [keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent), so users may see a one-time approval dialog depending on how `bootstrapUrl` reached the device.

> [!NOTE]
>
> A [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) supplies per-user configuration values when the app starts. In-app sign-in supplies each user's inference credential, the Entra ID token that authorizes model calls. A deployment with a bootstrap server still needs each user to sign in, and signing in doesn't deliver configuration.

#### Allow network egress

The sign-in flow reaches `login.microsoftonline.com` in addition to your Microsoft Foundry endpoint. Both hosts are included automatically in the **Egress** section of the in-app configuration window when these keys are set. When you [route requests through a gateway](#route-requests-through-a-gateway), the gateway's host replaces the resource host there.

### Route requests through a gateway

To send Microsoft Foundry traffic through a gateway or proxy you operate, such as Azure API Management in front of the resource, set `inferenceFoundryBaseUrl` (**Azure AI Foundry base URL**) to the gateway's base URL including any path, for example `https://llm-gateway.example.com/foundry`. It replaces the default `https://<resource-name>.services.ai.azure.com/anthropic` endpoint in Chat, Cowork, and Code, and it takes the same value as Claude Code's `ANTHROPIC_FOUNDRY_BASE_URL`, so one value serves both. `inferenceFoundryResource` is still required. The value must use `https`; from an MDM profile or the local configuration file it may instead be `http` for a proxy listening on the device's own loopback address (a bootstrap server response cannot deliver a loopback value).

The app sends the gateway the same credential it would send Microsoft Foundry: the API key, the credential helper's output, or with in-app sign-in each user's Entra ID token issued for the Azure Cognitive Services audience. A gateway that validates tokens must therefore accept that audience. If you want users to sign in against your own API's app registration instead, for example to map app roles to gateway policy, use the [gateway provider](https://claude.com/docs/third-party/claude-desktop/gateway.md) with its Entra ID sign-in rather than the Microsoft Foundry provider.

This key works from an MDM profile, the local configuration file, and a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md), where it is one of the [keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent). The Claude add-in for Microsoft 365 does not apply it yet and keeps calling the resource endpoint directly; if the add-in must also go through your gateway, configure the add-in's own gateway mode.

## Configure the app

Open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Foundry**, then fill in the **Foundry credentials** card with the values for whichever authentication approach you chose:

| Field | API key | In-app Entra ID sign-in |
| - | - | - |
| Azure AI Foundry resource name | `your-foundry-resource` | `your-foundry-resource` |
| Azure AI Foundry API key | your resource key | *leave empty* |
| Entra ID tenant ID | *leave empty* | `00000000-0000-0000-0000-000000000000` |
| Entra ID client ID | *leave empty* | `11111111-1111-1111-1111-111111111111` |
| Entra ID sign-in flow | *leave empty* | `browser` or `broker`, or leave empty for the default device-code flow |
| Azure AI Foundry base URL | *optional*, see [Route requests through a gateway](#route-requests-through-a-gateway) | *optional* |

Under **Models**, add at least one **Model list** entry using the Microsoft Foundry deployment name.

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) for the export and deployment workflow.

### Configuration keys

The full set of `inferenceFoundry*` keys is below. Set `inferenceProvider` to `foundry`, supply the resource name, and provide exactly one credential source.

[Entry labels](https://claude.com/docs/third-party/claude-desktop/configuration.md#entry-labels) says what each label means.

#### `inferenceFoundryResource`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Azure AI Foundry resource name.** Azure AI Foundry resource name used to construct the endpoint URL.

***

#### `inferenceFoundryBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 2.110.0

**Azure AI Foundry base URL.** Full base URL for a gateway or proxy in front of Foundry, path included (replaces [https://RESOURCE.services.ai.azure.com/anthropic](https://RESOURCE.services.ai.azure.com/anthropic)).

> [accordion] More detail
>
> Point it only at a gateway or proxy that you run. Requests carry the credential that the app would send to Foundry: the user's Entra ID token, the API key or the helper script's output.
>
> Use the value that you would give Claude Code as `ANTHROPIC_FOUNDRY_BASE_URL`. `inferenceFoundryResource` is still required and should name the resource behind the gateway.

***

#### `inferenceFoundryApiKey`

stringSince 1.2581.0

**Azure AI Foundry API key.** API key for Azure AI Foundry inference.

***

#### `inferenceFoundryTenantId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID tenant ID.** Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope.

***

#### `inferenceFoundryClientId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.9255.0

**Entra ID client ID.** Application (client) ID of the Entra ID app registration. Device-code sign-in requires the app to allow public client flows.

***

#### `inferenceFoundryAuthFlow`

enumSince 1.19367.0

**Entra ID sign-in flow.** How Entra sign-in runs: device code (default), system browser, or the OS identity broker.

One of: `device-code`, `browser`, `broker`

> [accordion] More detail
>
> * **`device-code`:** shows a code to enter at microsoft.com/devicelogin. The app registration must have **Allow public client flows** enabled.
> * **`browser`:** register `http://127.0.0.1/callback` under **Mobile and desktop applications**. It works with **Allow public client flows** disabled. Conditional Access policies that block device-code sign-in do not affect it.
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access policies that require a compliant or managed device, or token protection. Add the redirect URIs listed under [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

You must also set `inferenceModels` to a list of Microsoft Foundry deployment names. See the [Configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencemodels).

## What users experience

| Approach | First launch | Re-authentication |
| - | - | - |
| API key | The app opens directly; no user action. | Never, until you rotate the key in the managed profile. |
| In-app Entra ID sign-in, device-code flow | The app shows a **Sign in with Microsoft** page; the user approves a device code in the browser, and the app returns to Cowork. | When the stored refresh token expires or is revoked under your tenant's policy. The app prompts in-app. |
| In-app Entra ID sign-in, browser flow | The app shows a **Sign in with Microsoft** page; the user signs in through the system browser, with no code to enter, and the app returns to Cowork. | When the app can no longer renew the stored token. The app prompts in-app. |
| In-app Entra ID sign-in, broker flow | The app shows a **Sign in with Microsoft** page; the user picks or signs in to a work account in the operating system's native account picker, and the app returns to Cowork. | When the broker can no longer renew the token silently. The app prompts in-app. |

## Troubleshoot

To check each key's value and whether the provider settings are valid, or to find out why the app doesn't enter 3P mode, see [Verifying the deployment](https://claude.com/docs/third-party/claude-desktop/installation.md#verifying-the-deployment). Application log locations are listed in [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives).

If sign-in fails at the token step, confirm the **Azure Cognitive Services** permission is granted and consented on the app registration. For the device-code flow, also confirm **Allow public client flows** is enabled; Entra ID rejects device-code sign-in without it.

If sign-in fails with error code `AADSTS650057`, the **user\_impersonation** permission is missing from the app registration. Add it under **API permissions**.

If sign-in fails with error code `AADSTS65001`, the permission has not been consented. Select **Grant admin consent** on the **API permissions** page, or have the user accept the consent prompt if your tenant allows user consent.

If browser-flow sign-in fails in the browser with error code `AADSTS50011`, the redirect URI is missing from the app registration or does not match. Add `http://127.0.0.1/callback` under **Authentication → Mobile and desktop applications**, using the literal address `127.0.0.1`, not `localhost`.

If the browser shows the confirmation page but in-app sign-in still fails, with error code `AADSTS7000218` in the application logs, the redirect URI is registered under the **Web** platform. Move it under **Mobile and desktop applications**.

For broker-flow sign-in failures (error codes `AADSTS50011`, `AADSTS900971`, `AADSTS7000218`, or a message that the OS identity broker is unavailable), see [Troubleshoot](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#troubleshoot) on the OS identity broker page. To unblock a device that cannot meet the broker requirements, set `inferenceFoundryAuthFlow` to `browser` for that device instead.

Each sign-in attempt has a time limit: five minutes for the device-code and broker flows and ten minutes for the browser flow. If the user does not finish within the limit, the attempt fails and the user can click **Sign in with Microsoft** to start again.

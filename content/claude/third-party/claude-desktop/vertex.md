> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with Google Cloud's Agent Platform

> Set up Google Cloud, choose an authentication path for your organization, and configure Claude Desktop on 3P to use Claude models on Google Cloud's Agent Platform

This page walks an IT administrator through a complete deployment on Google Cloud's Agent Platform (formerly Vertex AI): enabling Claude in your Google Cloud project, choosing the authentication path that fits your organization, preparing devices, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

## Choose an authentication approach

Claude Desktop authenticates to Google Cloud's Agent Platform with Google Cloud Application Default Credentials, which you can supply in several ways. The right way depends on whether your users have Google identities and whether you need per-user attribution in Cloud Audit Logs.

| Scenario | Use | Per-device prerequisite | Per-user Cloud Audit Logs identity | Notes |
| - | - | - | - | - |
| Proof of concept, single team | [Service-account key](#credentials-file) (`inferenceVertexCredentialsFile`) | The key file on each device | No (shared service account) | A long-lived secret distributed to every device. Simplest to start; not recommended for broad rollout. |
| Users have Google Workspace or Cloud Identity accounts | [In-app Google sign-in](#in-app-google-sign-in) (`inferenceVertexOAuth*`) | None | Yes | Users sign in with their Google account inside the app. |
| Users authenticate with a third-party IdP (Entra ID, Okta, Ping, …) and you don't want to provision Google identities | [In-app Workforce Identity sign-in](#in-app-workforce-identity-sign-in) (`inferenceVertexWorkforce*`) | None | Yes (workforce-pool principal) | Users sign in with their corporate identity inside the app. The app runs PKCE against your IdP and exchanges the ID token at Google STS. |
| Your organization already has tooling that obtains a bearer token accepted by Google Cloud's Agent Platform | [Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper) (`inferenceCredentialHelper`) | The helper executable on each device | Depends on what the helper obtains | The helper prints a token, and the app sends that token as the bearer token on each inference request. |
| You already operate an LLM proxy | [Gateway provider](https://claude.com/docs/third-party/claude-desktop/gateway.md) instead of Google Cloud's Agent Platform | None | At your gateway | The proxy holds the Google Cloud credentials; the app authenticates only to the proxy. |

> [!WARNING]
>
> If your Google Workspace or Cloud Identity organization enforces a **Google Cloud session length** of a few hours or less (Admin console → Security → Google Cloud session control), the in-app Google sign-in stores a refresh token that is subject to that policy, and users will be prompted to sign in again each time the refresh token expires. For short session policies, either mark your OAuth client as a [trusted app exempt from reauthentication](https://support.google.com/a/answer/9368756), or use a service-account key, Workforce Identity sign-in, or the gateway provider instead.

## Set up Google Cloud

Complete these steps once per Google Cloud project, regardless of which authentication approach you chose. You need a project with Owner or Editor access.

**1. Enable the Vertex AI API**

In the [Google Cloud console](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com), enable the **Vertex AI API** for your project.

**2. Enable Claude models in Model Garden**

In the [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden), locate the Claude models you intend to deploy and click **Enable** on each. Model availability varies by region; enable them in the region you will set as `inferenceVertexRegion`.

**3. Grant users access to Google Cloud's Agent Platform**

Each authenticated principal needs permission to call the model. On the project's **IAM** page, grant the **Vertex AI User** role (`roles/aiplatform.user`) to:

* the service account, if using a service-account key file
* the Google group containing your users, if using in-app Google sign-in

If your organization uses a narrower custom role, it must include at minimum `aiplatform.endpoints.predict`.

**4. Create an OAuth client (in-app Google sign-in only)**

If you chose in-app Google sign-in, create a Desktop-app OAuth client in your project. See [In-app Google sign-in](#in-app-google-sign-in) below for the full procedure, including consent-screen setup.

**5. Federate to your IdP (optional)**

If your users authenticate with Microsoft Entra ID, Okta, or another identity provider and do not already have Google accounts, you have two options:

* **Workforce Identity Federation** (recommended). Create a workforce pool with an OIDC provider, and use the [in-app Workforce Identity sign-in](#in-app-workforce-identity-sign-in) approach. Users sign in directly with their corporate identity; no Google identity is provisioned.
* **Cloud Identity with SAML SSO.** Provision a free Cloud Identity tenant and configure SAML single sign-on to your IdP. Users then sign in through the in-app Google sign-in approach with a Google identity that is backed by your IdP. See [Set up SSO with a third-party IdP](https://support.google.com/cloudidentity/answer/12032922) in the Cloud Identity documentation.

## Prepare devices

### Credentials file

Create a service account in your project, grant it the **Vertex AI User** role, and download its JSON key. Distribute the key file to a fixed path on each device through your device-management tooling and set `inferenceVertexCredentialsFile` to that path.

`inferenceVertexCredentialsFile` accepts any Application Default Credentials JSON format, so if your environment already produces an `authorized_user` file (from `gcloud auth application-default login`) or an `external_account` Workforce Identity Federation configuration, you can set the key to that file's path instead. For `external_account` files, the `credential_source` must be of type `file` or `url` (`executable` sources are not supported), and separate tooling on the device must obtain the IdP token and write it to the configured location; Claude Desktop does not perform that step.

### In-app Google sign-in

No per-device preparation is required. The sign-in experience uses a Google OAuth client that **you create in your own Google Cloud project**; Anthropic does not provide or operate an OAuth client for this flow. Distribute the OAuth client ID and secret in the managed configuration (see [Configure the app](#configure-the-app)).

#### How it works

When `inferenceVertexOAuthClientId` and `inferenceVertexOAuthClientSecret` are both set, the app shows a **Sign in with Google Cloud** page at first launch. Clicking the button opens the system browser for a standard Google consent flow, and the app listens on a loopback address for the redirect. By default, the app requests the `openid`, `email`, `profile`, and `https://www.googleapis.com/auth/cloud-platform` scopes. On success, the app stores the user's Google refresh token encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows) and returns to Cowork.

The refresh token stays in the app. For each session, the app exchanges it at Google for a short-lived access token, gives the session that token, and renews it in the background. The app writes no credentials file and doesn't set `GOOGLE_APPLICATION_CREDENTIALS`. Hooks and MCP servers that run on the device, and commands in Code sessions, use the user's own `gcloud` credentials, if there are any, and not this sign-in. Before Claude Desktop 5.1231.0, the app wrote the refresh token to a `.gcp-credentials.json` file in each session's folder, and from that version on it deletes those files at launch.

If the stored refresh token is revoked or expires, the app shows a **Sign in again** prompt; clicking it reopens the Google consent flow in the browser. If you deploy a new OAuth client ID, the app clears the stored token and shows the sign-in page on next launch.

#### Create the OAuth client

**1. Configure the OAuth consent screen**

In the Google Cloud Console, in the project where you enabled Claude models, open **APIs & Services → OAuth consent screen**.

If your project belongs to a Google Workspace organization, select the **Internal** user type. Internal apps are limited to users in your Workspace and do not require Google verification, regardless of which scopes they request.

If the project is not in a Workspace organization, you must use the **External** user type. Because this flow requests the `https://www.googleapis.com/auth/cloud-platform` scope, Google classifies the app as using a sensitive scope, and publishing it beyond test users requires Google's OAuth verification process. For that reason, Internal is strongly recommended for enterprise deployments.

**2. Create a Desktop OAuth client**

In **APIs & Services → Credentials**, choose **Create credentials → OAuth client ID**, and select **Desktop app** as the application type.

Record the generated **Client ID** (ending in `.apps.googleusercontent.com`) and **Client secret**. For installed applications, Google does not treat the client secret as confidential; the flow is protected by PKCE and by the loopback redirect, so it is safe to distribute the secret in a managed configuration profile.

You do not need to add redirect URIs. Desktop-app clients permit loopback (`http://127.0.0.1:<port>`) redirects automatically.

**3. Allow network egress**

The sign-in flow and subsequent token refreshes reach `accounts.google.com` and `oauth2.googleapis.com` from the user's device. These hosts are already included in the standard egress requirements for Google Cloud's Agent Platform, so if you allowed egress based on the **Egress** section of the configuration window, no additional firewall changes are needed.

#### Federate to a third-party identity provider

The in-app sign-in always opens Google's authorization endpoint, because Google Cloud's Agent Platform only accepts Google-issued access tokens. To have users authenticate with your organization's own identity provider (Microsoft Entra ID, Okta, Ping, or an in-house SAML IdP) instead of a Google password, configure Cloud Identity as a broker:

1. In the Google Admin console, set up [SSO with a third-party IdP](https://support.google.com/cloudidentity/answer/12032922) and assign the SSO profile to your Claude Desktop users' organizational unit.
2. Provision those users into Cloud Identity (via SCIM from your IdP, or Google Cloud Directory Sync) so IAM grants resolve.
3. Optionally set `inferenceVertexOAuthLoginHint` so Google skips its own account chooser and routes straight to your IdP with the user's identity pre-filled.

With this in place, clicking **Sign in with Google Cloud** opens the browser, Google immediately redirects to your IdP, the user authenticates there (including smart-card or PIV authentication if your IdP supports it), and Google issues the tokens on return. Claude Desktop is unchanged; the federation is configured entirely in Google Admin and your IdP.

#### Notes and limitations

* **Precedence.** When both `inferenceVertexOAuthClientId` and `inferenceVertexCredentialsFile` are set and `inferenceCredentialKind` is not, Google sign-in takes precedence and the credentials file is ignored (the app logs a multi-credential warning). To force the credentials file, set `inferenceCredentialKind` to `vendor-profile` or remove the OAuth client keys.
* **Both keys required.** Set `inferenceVertexOAuthClientId` and `inferenceVertexOAuthClientSecret` together. With only one of them set, the app shows no **Sign in with Google Cloud** page.

### In-app Workforce Identity sign-in

No per-device preparation is required. In Google Cloud, create a [workforce pool](https://cloud.google.com/iam/docs/workforce-identity-federation) with an OIDC provider pointing at your organization's IdP, and grant the pool's principals the **Vertex AI User** role on the project.

In your IdP, register a native OAuth client for the app. The app does not send a client secret in this flow, so the client must be public (no client authentication) with PKCE required. The sign-in redirect lands on `http://127.0.0.1:<port>/callback`, where the operating system chooses `<port>` on each sign-in:

* If your IdP permits loopback redirect URIs on any port (the [RFC 8252](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3) native-app pattern, supported by Microsoft Entra ID under the **Mobile and desktop applications** platform), register `http://127.0.0.1/callback` and leave `redirectPort` unset.
* If your IdP requires an exact registered redirect URI (such as Okta or PingFederate), set the `redirectPort` field of `inferenceVertexWorkforceOidc` to a fixed port and register the resulting URI exactly, for example `http://127.0.0.1:53180/callback`.

Register the redirect URI with `127.0.0.1` rather than `localhost`, because the app uses `127.0.0.1` by default and most IdPs do not treat the two as interchangeable. If your IdP accepts only `localhost` in a registered redirect URI, set the `redirectHost` field of [`inferenceVertexWorkforceOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencevertexworkforceoidc) to `localhost` and register `http://localhost/callback` instead, or `http://localhost:<port>/callback` when you set `redirectPort`.

Distribute the workforce-pool provider audience (`inferenceVertexWorkforceAudience`, in the form `//iam.googleapis.com/locations/global/workforcePools/POOL/providers/PROVIDER`) and the IdP OIDC client (`inferenceVertexWorkforceOidc`) in the managed configuration. The app then shows a **Sign in with Google Cloud** page on first launch. For the sign-in, the app runs an authorization-code-with-PKCE flow against your IdP in the system browser, exchanges the returned ID token for a Google Cloud access token at `sts.googleapis.com`, and stores the IdP refresh token encrypted with the operating system's secure storage. No `gcloud` CLI, helper script, or Google identity is required.

The app always requests the `offline_access` scope so that the IdP returns a refresh token for silent renewal. If your IdP rejects `offline_access` on this client (for example, a PingFederate public client without the Refresh Token grant type enabled), set the `omitOfflineAccess` field of `inferenceVertexWorkforceOidc` to `true`. Without a refresh token the app cannot refresh silently, so users will be prompted to sign in again each time the IdP's ID token expires, typically about once an hour.

When your IdP is Microsoft Entra ID, you can run this sign-in through the [OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md) on Windows and macOS instead of the system browser by setting `inferenceVertexWorkforceAuthFlow` to `broker`. The `issuer` in `inferenceVertexWorkforceOidc` must then be `https://login.microsoftonline.com/TENANT_ID/v2.0`, and no loopback redirect URI is needed. The token exchange at `sts.googleapis.com` is unchanged.

## Configure the app

With Google Cloud set up and devices prepared, open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**) on an evaluation device. In the **Connection** section, set **Inference provider** to **Vertex AI** and fill in the **Vertex AI credentials** card with the values for whichever authentication approach you chose:

| Field | Service-account key | In-app Google sign-in |
| - | - | - |
| Credential kind | **Cloud vendor profile** | **Interactive sign-in** |
| GCP project ID | `your-gcp-project` | `your-gcp-project` |
| GCP region | for example, `us-east5` | for example, `us-east5` |
| GCP credentials file path | `/path/to/sa-key.json` | *field hidden* |
| Vertex OAuth client ID | *field hidden* | `1234567890-abc123.apps.googleusercontent.com` |
| Vertex OAuth client secret | *field hidden* | `GOCSPX-xxxxxxxxxxxxxxxxxxxx` |
| Vertex OAuth scopes | *field hidden* | *leave empty for the default* |
| Vertex AI base URL | *optional* | *optional* |

For the other authentication approaches, select a different **Credential kind**:

* **[In-app Workforce Identity sign-in](#in-app-workforce-identity-sign-in)**: select **Workforce Identity**
* **[Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper)**: select **Helper script**

Under **Models**, add at least one **Model list** entry using the publisher model ID, for example `claude-sonnet-5`.

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) for the export and deployment workflow.

### Check the connection to Google Cloud

With the **Vertex AI** provider selected in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window), the **Test connection** button doesn't send a test request to Google Cloud. If your credential helper fails, the result names the error. Otherwise, the result reads `Vertex auth cannot be probed from the main process.`

To check the connection, send a message through it:

1. In the in-app configuration window, click **Apply Changes**.
2. Click **Save & Restart**. If your changes are already saved, click **Relaunch now** instead.
3. If **Credential kind** is **Interactive sign-in** or **Workforce Identity**, click **Sign in with Google Cloud** after the app relaunches, and complete the sign-in.
4. Send a message. A reply from Claude confirms the connection.

### Configuration keys

Set `inferenceProvider` to `vertex`, supply a project and region, and provide exactly one credential source.

The region can be a single region such as `us-east5`, the `eu` or `us` multi-region, or `global`. The app routes inference to a different endpoint host for multi-regions and `global`; if you allowlist egress by hostname, see the [inference provider egress hosts](https://claude.com/docs/third-party/claude-desktop/telemetry.md#inference-provider).

[Entry labels](https://claude.com/docs/third-party/claude-desktop/configuration.md#entry-labels) says what each label means.

#### `inferenceVertexProjectId`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP project ID.** Google Cloud project ID for Vertex AI inference.

***

#### `inferenceVertexRegion`

stringSince 1.2581.0

**GCP region.** GCP region where your Vertex AI Claude models are deployed.

***

#### `inferenceVertexBaseUrl`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Vertex AI base URL.** Private Service Connect endpoint, if you use one.

***

#### `inferenceVertexOAuthClientId`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**Vertex OAuth client ID.** Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file.

***

#### `inferenceVertexOAuthClientSecret`

stringSince 1.2581.0

**Vertex OAuth client secret.** Secret for the Desktop-app OAuth client above. Google does not treat such secrets as confidential, so the Admin Console can set it.

***

#### `inferenceVertexOAuthScopes`

stringSince 1.2581.0

**Vertex OAuth scopes.** Override the Google OAuth scopes (space-separated). Leave blank for the default.

***

#### `inferenceVertexOAuthLoginHint`

stringSince 1.12603.0

**Vertex OAuth login hint.** Pre-fill Google's account chooser and forward to your federated IdP. \{username} expands to the OS login name.

***

#### `inferenceVertexWorkforceAudience`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity audience.** Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity.

***

#### `inferenceVertexWorkforceUserProject`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity billing project.** GCP project for STS billing and quota. Defaults to the Vertex project ID above.

***

#### `inferenceVertexWorkforceAuthFlow`

enumSince 1.25927.0

**Workforce Identity sign-in flow.** How the IdP sign-in runs: system browser (default) or the OS Microsoft Entra broker.

One of: `browser`, `broker`

> [accordion] More detail
>
> * **`browser`:** register the redirect URI `http://127.0.0.1:<port>/callback` with your identity provider (for Entra, `http://127.0.0.1/callback`).
> * **`broker`:** uses Web Account Manager on Windows or Company Portal on macOS, and does not work on Linux. It can satisfy Conditional Access device and token-protection policies.
>
> `broker` needs Microsoft Entra ID, with the `issuer` in `inferenceVertexWorkforceOidc` set to `https://login.microsoftonline.com/{tenant-id}/v2.0`. Add the redirect URIs from [Register the Entra ID application](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#register-the-entra-id-application).

***

#### `inferenceVertexWorkforceOidc`

object

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.10628.0

**Workforce Identity IdP (OIDC).** Your organization’s OpenID Connect identity provider. Users sign in there, and the app exchanges their ID token at GCP STS.

> [accordion] Child attributes (9)
>
> **clientId** `string` *required*
>
> OAuth client ID of the desktop app registration at your identity provider (public client, PKCE).
>
> **issuer** `string`
>
> HTTPS issuer with OIDC discovery. Set this, or set the authorization and token URLs instead.
>
> **authorizationUrl** `string`
>
> HTTPS authorization endpoint. Used with the token URL when no issuer is set.
>
> **tokenUrl** `string`
>
> HTTPS token endpoint. Used with the authorization URL when no issuer is set.
>
> **scopes** `string`
>
> Space-separated scopes. Defaults to openid profile email offline\_access.
>
> **redirectPort** `integer`
>
> Fixed loopback port for the sign-in redirect. Leave unset to use a free port each time.
>
> **redirectHost** `enum`
>
> Use localhost only if your IdP’s registered redirect URI specifies it.
>
> One of: `127.0.0.1`, `localhost`
>
> **omitOfflineAccess** `boolean`
>
> Turn on only if your identity provider rejects offline\_access on this client. Users then sign in again each time the token expires.
>
> **additionalRedirectReferrerHosts** `string`
>
> Space-separated hostnames also accepted as the referrer of the sign-in callback, besides the authorization URL’s host.
>
> > [accordion] More detail
> >
> > If the app rejects the sign-in callback because of its referrer, the app log names the rejected host. Add that hostname here.

***

#### `inferenceVertexCredentialsFile`

string

Consent required (A value that a bootstrap server delivers applies only after the user approves it, unless machine-scoped device management set that server's address. The trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**GCP credentials file path.** Full path to a service-account JSON file. Unset: Application Default Credentials.

***

If none of `inferenceVertexCredentialsFile`, the OAuth client keys, the Workforce Identity keys, or `inferenceCredentialHelper` is set, the Google client library falls back to the standard Application Default Credentials search path on the device (`~/.config/gcloud/application_default_credentials.json`, then the environment's metadata server).

You must also set `inferenceModels` to a list of publisher model IDs, for example `claude-sonnet-5`. See the [Configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md#inferencemodels).

## What users experience

For in-app Google sign-in, the browser flow runs on the host (outside the Cowork sandbox), so it can use the user's existing Google session and any security keys or passkeys configured on the device. Users can sign out by revoking the app from their Google Account's [third-party connections page](https://myaccount.google.com/connections); the app detects the revoked token and shows a **Sign in again** prompt.

## Troubleshoot

To check each key's value and whether the provider settings are valid, or to find out why the app doesn't enter 3P mode, see [Verifying the deployment](https://claude.com/docs/third-party/claude-desktop/installation.md#verifying-the-deployment). Application log locations are listed in [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives).

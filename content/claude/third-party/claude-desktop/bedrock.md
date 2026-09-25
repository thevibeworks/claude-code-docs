> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with Amazon Bedrock

> Set up AWS, choose an authentication path for your organization, and configure Claude Desktop on 3P to use Claude models on Amazon Bedrock

This page walks an IT administrator through a complete Amazon Bedrock deployment: enabling Claude in your AWS account, choosing the authentication path that fits your organization, preparing devices, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

## Choose an authentication approach

Amazon Bedrock supports several ways to authenticate, and the right one depends on whether your end users already work with AWS and whether you need per-user identity in CloudTrail. Use the table below to pick a path before doing any AWS or device setup.

| Scenario                                                    | Use                                                                                    | Per-device prerequisite                 | Per-user CloudTrail identity | Notes                                                                                                                                           |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Proof of concept, single team                               | [Bearer token](#bearer-token) (`inferenceBedrockBearerToken`)                          | None                                    | No (shared key)              | A long-lived secret distributed in the managed profile. Simplest to start; not recommended for broad rollout.                                   |
| Broad rollout to users without AWS tooling                  | [In-app AWS sign-in](#in-app-aws-sign-in) (`inferenceBedrockSso*`)                     | None                                    | Yes                          | Users sign in through IAM Identity Center inside the app. No AWS CLI required. Requires app version 1.6259.0 or later.                          |
| Developers who already use the AWS CLI                      | [Named profile](#named-profile) (`inferenceBedrockProfile`)                            | AWS CLI v2 and a pushed `~/.aws/config` | Yes                          | IT can distribute the AWS config file directly; the app runs `aws sso login` for the user when the session expires.                             |
| You run an authenticating proxy in front of Amazon Bedrock  | [Identity provider sign-in](#sign-in-with-your-identity-provider) (`inferenceIdpOidc`) | None                                    | At your proxy                | Users sign in with your identity provider; the proxy calls Amazon Bedrock with its own AWS credentials. Requires app version 2.7032.0 or later. |
| You already operate an LLM gateway (Anthropic Messages API) | [Gateway provider](/docs/third-party/claude-desktop/gateway) instead of Amazon Bedrock      | None                                    | At your gateway              | The gateway holds the AWS credentials; the app authenticates only to the gateway.                                                               |

If a static credential in the managed profile is acceptable but an Amazon Bedrock API key is not, you can also set [`inferenceCredentialHelper`](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that prints an Amazon Bedrock bearer token to stdout at runtime.

When more than one credential is configured, the app uses the first one present in this order: identity provider sign-in, in-app AWS sign-in, named profile, credential helper, bearer token. To remove ambiguity, set `inferenceCredentialKind` explicitly (see the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencecredentialkind)).

## Set up AWS

These steps are performed once per AWS organization, regardless of which authentication approach you chose. You need an AWS account with permission to manage Amazon Bedrock model access and IAM Identity Center.

<Steps>
  <Step title="Enable Claude models in Amazon Bedrock">
    In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/), open **Model access** and request access to the Claude models you intend to deploy. Access is granted per region, so enable the models in the same region you will set as `inferenceBedrockRegion`.
  </Step>

  <Step title="Create an IAM Identity Center permission set">
    Skip this step if you chose the bearer-token or identity provider sign-in approach. The named-profile and in-app AWS sign-in approaches both use IAM Identity Center to issue per-user AWS credentials.

    In the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/), create a permission set with an inline policy that allows Amazon Bedrock inference. The minimal policy is:

    ```json theme={null}
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": [
          "bedrock:InvokeModel",
          "bedrock:InvokeModelWithResponseStream"
        ],
        "Resource": "*"
      }]
    }
    ```

    Set the permission set's **Session duration** to between 8 and 12 hours. This value sets how long each set of temporary AWS credentials lasts before the app requests a new set from IAM Identity Center. It does not control how often users sign in. Sign-in frequency follows the access portal session duration, described under [What users experience](#what-users-experience).
  </Step>

  <Step title="Federate Identity Center to your IdP (optional)">
    If your organization uses Microsoft Entra ID, Okta, or another SAML identity provider, you can configure it as the identity source for IAM Identity Center so users sign in with their existing corporate credentials. The per-device steps on this page are unchanged. See [Connect to an external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html) in the AWS documentation.
  </Step>

  <Step title="Assign users to the permission set">
    In IAM Identity Center, assign the permission set to the AWS account that hosts Amazon Bedrock, and add the users or groups who should have access.
  </Step>

  <Step title="Record the values you need for device configuration">
    From the IAM Identity Center **Settings** page, note:

    * **AWS access portal URL**: of the form `https://d-xxxxxxxxxx.awsapps.com/start` (or your custom subdomain)
    * **Identity Center region**: the region where Identity Center is enabled, which may differ from your Amazon Bedrock region
    * **AWS account ID**: the 12-digit ID of the account where you enabled Amazon Bedrock
    * **Permission set name**: the name you gave the permission set above
  </Step>
</Steps>

## Prepare devices

What each end-user device needs depends on the authentication approach you chose.

### Bearer token

No per-device preparation is required. In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys), generate an API key. The key's underlying IAM principal must be allowed the `bedrock:CallWithBearerToken` action; without it, requests return an authorization error even though the key was created. You will place the key in the managed configuration; see [Configure the app](#configure-the-app).

### In-app AWS sign-in

No per-device preparation is required. The sign-in experience uses **your organization's AWS IAM Identity Center instance**; the app registers an OIDC client dynamically with your Identity Center at runtime, so you do not create or distribute a client ID. Distribute the four `inferenceBedrockSso*` keys in the managed configuration (see [Configure the app](#configure-the-app)).

#### How it works

When all four `inferenceBedrockSso*` keys are set, the app shows a **Sign in with AWS** page at first launch. Clicking the button starts an OAuth device-authorization flow with your IAM Identity Center's OIDC endpoint and opens the AWS access portal in the system browser. The app displays a short verification code so the user can confirm that the browser prompt matches the app that requested it. Identity Center redirects the user to whichever identity provider you have configured (Entra ID, Okta, Google Workspace, or the Identity Center built-in directory).

On success, the app stores the IAM Identity Center access token and refresh token encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows), dismisses the sign-in page, and shows Cowork.

At the start of each Cowork or Code session, the app exchanges the stored token with IAM Identity Center for short-lived AWS credentials scoped to the configured account and permission set, and writes them to the session's AWS credentials files, described under [Transient credential files](/docs/third-party/claude-desktop/data-storage#transient-credential-files). The session reads them through `AWS_SHARED_CREDENTIALS_FILE` and `AWS_PROFILE`, so the secret values are never passed as environment variables. This is the same credential shape that `aws sso login` produces, obtained without the AWS CLI.

If the stored token expires or is revoked, the app shows a **Sign in again** prompt; clicking it reopens the AWS access portal in the browser. If you deploy a different `inferenceBedrockSsoStartUrl`, the app finds no stored token for the new URL and shows the sign-in page on next launch.

#### Allow network egress

The sign-in flow and token refresh reach the IAM Identity Center endpoints for the region you set as `inferenceBedrockSsoRegion`:

* `oidc.<sso-region>.amazonaws.com`
* `portal.sso.<sso-region>.amazonaws.com`

These hosts are included automatically in the **Egress** section of the in-app configuration window when the SSO keys are set, so if you built your firewall allowlist from that output, no additional changes are needed. The browser step also reaches your AWS access portal (`*.awsapps.com`) and, if federated, your external identity provider.

#### Notes and limitations

* **All four keys required.** A partial set does not enable in-app sign-in. If `inferenceCredentialKind` is set to `interactive`, the app treats the configuration as invalid, logs an error that names the missing keys, and does not connect until they are supplied. If `inferenceCredentialKind` is not set, the app uses whichever other credential the configuration provides, or reports that no credential is configured.
* **One account and role per deployment.** Every user in a given managed configuration signs in to the same AWS account and assumes the same permission set. To give different groups different Amazon Bedrock permissions, deploy distinct configuration profiles with different `inferenceBedrockSsoRoleName` values.
* **Mid-session credential refresh.** The app checks the AWS credentials' expiry before each turn and silently mints new ones from the stored IAM Identity Center token when they are close to expiring. If the Identity Center token itself has expired or been revoked, the app shows a **Sign in again** prompt; click it to re-authenticate with AWS in your browser. The access portal session duration in IAM Identity Center sets how long the Identity Center sign-in itself lasts, as described under [What users experience](#what-users-experience).
* **Connection probe.** The in-app **Test connection** button completes the AWS sign-in if needed, then sends a short test request to a model from your **Models** list through the app's Claude Code runtime. Add at least one model first, because this credential type cannot discover models automatically. If the app has not yet finished downloading its Claude Code runtime, the test reports that it cannot run; wait a moment and try again. Named-profile mode behaves the same way.
* **Configuration rotation.** If you change `inferenceBedrockSsoStartUrl` in the managed profile, existing users are automatically signed out and prompted to sign in again on next launch.

### Named profile

Each device needs AWS CLI v2 installed and an AWS config file that defines the named profile.

You do not need users to run `aws configure sso` interactively. That command is a wizard that writes a profile stanza to `~/.aws/config` (macOS) or `%USERPROFILE%\.aws\config` (Windows), and you can distribute that file directly through your device-management tooling instead. A profile that uses IAM Identity Center looks like:

```ini theme={null}
[profile claude-cowork]
sso_session = corp
sso_account_id = 123456789012
sso_role_name = ClaudeCoworkAccess
region = us-west-2

[sso-session corp]
sso_start_url = https://d-xxxxxxxxxx.awsapps.com/start
sso_region = us-east-1
sso_registration_scopes = sso:account:access
```

When the cached IAM Identity Center token is missing or expired, the app prompts the user to sign in and runs `aws sso login --profile claude-cowork` itself, which opens the browser for IAM Identity Center sign-in and caches a token under `~/.aws/sso/cache/`. Users can also run the command in a terminal; the app and the CLI share the same token cache. When the token can be refreshed silently, the app does so without prompting.

To run the login command, the app locates the AWS CLI by searching the launch environment's `PATH`, the user's login-shell `PATH`, and standard install locations such as `/usr/local/bin` and `/opt/homebrew/bin` on macOS. If your fleet installs the AWS CLI somewhere else, or you want every device to use one specific binary, set `inferenceBedrockAwsCliPath` to the absolute path of the executable.

If your AWS configuration files are not at the default location, set `inferenceBedrockAwsDir` to the directory that contains them.

### Sign in with your identity provider

Use this approach when a proxy in front of Amazon Bedrock validates tokens from your OpenID Connect identity provider, such as Microsoft Entra ID or Okta. Each user signs in with the identity provider, and Claude Desktop sends the user's token as `Authorization: Bearer` on every inference request to the proxy at `inferenceBedrockBaseUrl`. The proxy calls Amazon Bedrock with its own AWS credentials. Claude Code sessions started from the app use the same token (`AWS_BEARER_TOKEN_BEDROCK`) and proxy URL. Requires Claude Desktop 2.7032.0 or later.

Set `inferenceCredentialKind` to `external-idp` (in the in-app configuration window, set **Credential kind** to **Identity provider sign-in (OIDC)**). Example `.mobileconfig` payload (Okta):

```xml theme={null}
<key>inferenceProvider</key>
<string>bedrock</string>
<key>inferenceBedrockRegion</key>
<string>us-west-2</string>
<key>inferenceBedrockBaseUrl</key>
<string>https://bedrock-proxy.example.corp</string>
<key>inferenceCredentialKind</key>
<string>external-idp</string>
<key>inferenceIdpOidc</key>
<string>{"issuer":"https://YOUR_ORG.okta.com","clientId":"YOUR_CLIENT_ID","redirectPort":53180}</string>
<key>inferenceModels</key>
<string>["us.anthropic.claude-sonnet-5"]</string>
```

[`inferenceIdpOidc`](/docs/third-party/claude-desktop/configuration#inferenceidpoidc) takes the same fields as the gateway provider's [`inferenceGatewayOidc`](/docs/third-party/claude-desktop/gateway#single-sign-on-configuration-keys), and you register the identity-provider application the same way; see [Set up single sign-on](/docs/third-party/claude-desktop/gateway#set-up-single-sign-on). To sign in through the [OS identity broker](/docs/third-party/claude-desktop/entra-broker) instead of the browser (Microsoft Entra ID only), set `inferenceIdpAuthFlow` to `broker`.

Notes:

* `inferenceBedrockBaseUrl` (your proxy) is required: Amazon Bedrock endpoints, including VPC endpoints, reject identity-provider tokens. Without a proxy, use [in-app AWS sign-in](#in-app-aws-sign-in).
* No model discovery: list the model IDs in `inferenceModels`.
* The proxy receives the OIDC ID token by default and must check that its `aud` is your `clientId`; for a proxy that validates OAuth access tokens, set `bearerTokenType` and `scopes` in [`inferenceIdpOidc`](/docs/third-party/claude-desktop/configuration#inferenceidpoidc).

## Configure the app

With AWS set up and devices prepared, open the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**) on an evaluation device. In the **Connection** section, set **Inference provider** to **Bedrock** and fill in the **Bedrock credentials** card with the values for whichever authentication approach you chose:

| Field                | Bearer token                | In-app AWS sign-in                       | Named profile          |
| -------------------- | --------------------------- | ---------------------------------------- | ---------------------- |
| AWS region           | e.g. `us-west-2`            | e.g. `us-west-2`                         | e.g. `us-west-2`       |
| AWS bearer token     | your Amazon Bedrock API key | *leave empty*                            | *leave empty*          |
| Bedrock base URL     | *optional*                  | *optional*                               | *optional*             |
| AWS profile name     | *leave empty*               | *leave empty*                            | `claude-cowork`        |
| AWS config directory | *leave empty*               | *leave empty*                            | *only if not `~/.aws`* |
| AWS CLI path         | *leave empty*               | *leave empty*                            | *optional*             |
| AWS SSO start URL    | *leave empty*               | `https://d-xxxxxxxxxx.awsapps.com/start` | *leave empty*          |
| AWS SSO region       | *leave empty*               | e.g. `us-east-1`                         | *leave empty*          |
| AWS SSO account ID   | *leave empty*               | `123456789012`                           | *leave empty*          |
| AWS SSO role name    | *leave empty*               | `BedrockInference`                       | *leave empty*          |
| Bedrock service tier | *optional*                  | *optional*                               | *optional*             |

Under **Models**, add a **Model list** entry using the Amazon Bedrock inference-profile ID (optional for bearer-token or credential-helper auth, which auto-discover models; required otherwise), for example `us.anthropic.claude-sonnet-5`.

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm) for the export and deployment workflow.

### Configuration keys

The full set of `inferenceBedrock*` keys is below. Set `inferenceProvider` to `bedrock`, supply a region, and provide exactly one credential source.

| Setting                                                                                          | Type     | Availability                            | Default | Description                                                                                                       |
| ------------------------------------------------------------------------------------------------ | -------- | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| <span id="inferencebedrockregion" />AWS region<br />`inferenceBedrockRegion`                     | `string` | MDM + Bootstrap<br />Added in 1.2581.0  | —       | AWS region for the Bedrock runtime endpoint.                                                                      |
| <span id="inferencebedrockbaseurl" />Bedrock base URL<br />`inferenceBedrockBaseUrl`             | `string` | MDM + Bootstrap<br />Added in 1.2581.0  | —       | For VPC endpoints or gateway proxies. Host origin only.                                                           |
| <span id="inferencebedrockservicetier" />Bedrock service tier<br />`inferenceBedrockServiceTier` | `enum`   | MDM + Bootstrap<br />Added in 1.5186.0  | —       | Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand. One of: `flex`, `priority`.            |
| <span id="inferencebedrockbearertoken" />AWS bearer token<br />`inferenceBedrockBearerToken`     | `string` | MDM + Bootstrap<br />Added in 1.2581.0  | —       | Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those. |
| <span id="inferencebedrockssostarturl" />AWS SSO start URL<br />`inferenceBedrockSsoStartUrl`    | `string` | MDM + Bootstrap<br />Added in 1.6259.0  | —       | Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.                              |
| <span id="inferencebedrockssoregion" />AWS SSO region<br />`inferenceBedrockSsoRegion`           | `string` | MDM + Bootstrap<br />Added in 1.6259.0  | —       | IAM Identity Center home region.                                                                                  |
| <span id="inferencebedrockssoaccountid" />AWS SSO account ID<br />`inferenceBedrockSsoAccountId` | `string` | MDM + Bootstrap<br />Added in 1.6259.0  | —       | 12-digit AWS account ID assigned to users in IAM Identity Center.                                                 |
| <span id="inferencebedrockssorolename" />AWS SSO role name<br />`inferenceBedrockSsoRoleName`    | `string` | MDM + Bootstrap<br />Added in 1.6259.0  | —       | IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.                      |
| <span id="inferencebedrockprofile" />AWS profile name<br />`inferenceBedrockProfile`             | `string` | MDM + Bootstrap<br />Added in 1.2581.0  | —       | AWS named profile to use for Bedrock inference credentials.                                                       |
| <span id="inferencebedrockawsdir" />AWS config directory<br />`inferenceBedrockAwsDir`           | `string` | MDM + Bootstrap<br />Added in 1.2581.0  | —       | Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.                              |
| <span id="inferencebedrockawsclipath" />AWS CLI path<br />`inferenceBedrockAwsCliPath`           | `string` | MDM + Bootstrap<br />Added in 1.13576.0 | —       | Absolute path to the aws executable. Leave unset to find it on PATH.                                              |

<AccordionGroup>
  <Accordion title="inferenceBedrockServiceTier details">
    Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.
  </Accordion>
</AccordionGroup>

Set `inferenceModels` to a list of Amazon Bedrock inference-profile IDs, for example `us.anthropic.claude-sonnet-5`. When using a bearer token or credential helper, Claude Desktop auto-discovers available Claude models from your account if this is unset; otherwise the list is required. Application-inference-profile ARNs and provisioned-throughput ARNs are also accepted; pair them with a [`labelOverride`](/docs/third-party/claude-desktop/configuration#inferencemodels) so the picker shows a readable name instead of the raw ARN. See the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencemodels).

## What users experience

The first-launch and re-authentication behavior depends on the authentication approach.

| Approach                  | First launch                                                                                                                                 | Re-authentication                                                                                                                                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bearer token              | The app opens directly; no user action.                                                                                                      | Never, until you rotate the key in the managed profile.                                                                                                                                                           |
| In-app AWS sign-in        | The app shows a **Sign in with AWS** page; the user approves in the browser, and the app returns to Cowork.                                  | When the IAM Identity Center access portal session expires (defaults to 8 hours; configurable up to 90 days). The app prompts in-app; no terminal needed.                                                         |
| Named profile             | The app opens directly if the AWS SSO cache is fresh; otherwise it prompts in-app and runs `aws sso login` for you, which opens the browser. | When the IAM Identity Center session expires, the app prompts in-app and re-runs `aws sso login`.                                                                                                                 |
| Identity provider sign-in | The app shows a sign-in page; the user signs in at your identity provider.                                                                   | When the token expires, the app renews it silently; it prompts again only if the renewal fails or [`inferenceSessionLifetimeSec`](/docs/third-party/claude-desktop/configuration#inferencesessionlifetimesec) elapses. |

For in-app AWS sign-in, the browser flow runs on the host (outside the Cowork sandbox), so it uses the user's existing identity-provider session and any security keys or passkeys configured on the device. The **AWS access portal session duration** setting (IAM Identity Center → **Settings** → **Authentication**) controls how long users stay signed in across app restarts. To force a user to sign in again sooner, delete their active session from the IAM Identity Center console.

If the app cannot locate the AWS CLI, it cannot drive the login itself; it instructs the user to install AWS CLI v2 and run `aws sso login --profile <name>` manually.

## Troubleshoot

To confirm which keys the app read and whether the provider settings validated, use **Help → Troubleshooting → Generate Diagnostic Report**, export the report, and check `managed-config.txt` and `provider-status.txt`; see [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [Data storage and residency](/docs/third-party/claude-desktop/data-storage).

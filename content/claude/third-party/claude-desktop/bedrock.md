> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with Amazon Bedrock

> Set up AWS, choose an authentication path for your organization, and configure Claude Desktop on 3P to use Claude models on Amazon Bedrock

This page walks an IT administrator through a complete Amazon Bedrock deployment: enabling Claude in your AWS account, choosing the authentication path that fits your organization, preparing devices, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

## Choose an authentication approach

Amazon Bedrock supports several ways to authenticate, and the right one depends on whether your end users already work with AWS and whether you need per-user identity in CloudTrail. Use the table below to pick a path before doing any AWS or device setup.

| Scenario                                   | Use                                                                               | Per-device prerequisite                 | Per-user CloudTrail identity | Notes                                                                                                                  |
| ------------------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Proof of concept, single team              | [Bearer token](#bearer-token) (`inferenceBedrockBearerToken`)                     | None                                    | No (shared key)              | A long-lived secret distributed in the managed profile. Simplest to start; not recommended for broad rollout.          |
| Broad rollout to users without AWS tooling | [In-app AWS sign-in](#in-app-aws-sign-in) (`inferenceBedrockSso*`)                | None                                    | Yes                          | Users sign in through IAM Identity Center inside the app. No AWS CLI required. Requires app version 1.6259.0 or later. |
| Developers who already use the AWS CLI     | [Named profile](#named-profile) (`inferenceBedrockProfile`)                       | AWS CLI v2 and a pushed `~/.aws/config` | Yes                          | IT can distribute the AWS config file directly; the app runs `aws sso login` for the user when the session expires.    |
| You already operate an LLM proxy           | [Gateway provider](/docs/third-party/claude-desktop/gateway) instead of Amazon Bedrock | None                                    | At your gateway              | The proxy holds the AWS credentials; the app authenticates only to the proxy.                                          |

If a static credential in the managed profile is acceptable but an Amazon Bedrock API key is not, you can also set [`inferenceCredentialHelper`](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that prints an Amazon Bedrock bearer token to stdout at runtime.

When more than one credential is configured, the app uses the first one present in this order: in-app AWS sign-in, named profile, credential helper, bearer token. To remove ambiguity, set `inferenceCredentialKind` explicitly (see the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencecredentialkind)).

## Set up AWS

These steps are performed once per AWS organization, regardless of which authentication approach you chose. You need an AWS account with permission to manage Amazon Bedrock model access and IAM Identity Center.

<Steps>
  <Step title="Enable Claude models in Amazon Bedrock">
    In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/), open **Model access** and request access to the Claude models you intend to deploy. Access is granted per region, so enable the models in the same region you will set as `inferenceBedrockRegion`.
  </Step>

  <Step title="Create an IAM Identity Center permission set">
    Skip this step if you chose the bearer-token approach. The named-profile and in-app AWS sign-in approaches both use IAM Identity Center to issue per-user AWS credentials.

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

    Set the permission set's **Session duration** to between 8 and 12 hours. This value controls how long a user can run Claude Desktop before needing to sign in to AWS again.
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

At the start of each Cowork session, the app exchanges the stored token with IAM Identity Center for short-lived AWS credentials scoped to the configured account and permission set, and passes them into the session sandbox as `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. This is the same credential shape that `aws sso login` produces, obtained without the AWS CLI.

If the stored token expires or is revoked, the app shows a **Sign in again** prompt; clicking it reopens the AWS access portal in the browser. If you deploy a different `inferenceBedrockSsoStartUrl`, the app finds no stored token for the new URL and shows the sign-in page on next launch.

#### Allow network egress

The sign-in flow and token refresh reach the IAM Identity Center endpoints for the region you set as `inferenceBedrockSsoRegion`:

* `oidc.<sso-region>.amazonaws.com`
* `portal.sso.<sso-region>.amazonaws.com`

These hosts are included automatically in the **Egress** section of the in-app configuration window when the SSO keys are set, so if you built your firewall allowlist from that output, no additional changes are needed. The browser step also reaches your AWS access portal (`*.awsapps.com`) and, if federated, your external identity provider.

#### Notes and limitations

* **All four keys required.** If only some of the `inferenceBedrockSso*` keys are set, the app logs a warning and ignores the partial configuration.
* **One account and role per deployment.** Every user in a given managed configuration signs in to the same AWS account and assumes the same permission set. To give different groups different Amazon Bedrock permissions, deploy distinct configuration profiles with different `inferenceBedrockSsoRoleName` values.
* **Mid-session credential refresh.** The app checks the AWS credentials' expiry before each turn and silently mints new ones from the stored IAM Identity Center token when they are close to expiring. If the Identity Center token itself has expired or been revoked, the app shows a **Sign in again** prompt; click it to re-authenticate with AWS in your browser. The permission set's session duration controls how long the Identity Center token remains valid, so set it long enough to cover a working day.
* **Connection probe.** The in-app **Test connection** button reports that the connection cannot be verified in this mode, because the app cannot sign Amazon Bedrock requests outside the sandbox. This matches the behavior of named-profile mode and does not indicate a problem.
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

Under **Models**, add a **Model list** entry using the Amazon Bedrock inference-profile ID (required for profile or SSO auth; optional for bearer-token or credential-helper auth, which auto-discover), for example `us.anthropic.claude-sonnet-5`.

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm) for the export and deployment workflow.

### Configuration keys

The full set of `inferenceBedrock*` keys is below. Set `inferenceProvider` to `bedrock`, supply a region, and provide exactly one credential source.

| Setting                                                                                          | Type     | Availability    | Default | Description                                                                                                       |
| ------------------------------------------------------------------------------------------------ | -------- | --------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| <span id="inferencebedrockregion" />AWS region<br />`inferenceBedrockRegion`                     | `string` | MDM + Bootstrap | —       | AWS region for the Bedrock runtime endpoint.                                                                      |
| <span id="inferencebedrockbaseurl" />Bedrock base URL<br />`inferenceBedrockBaseUrl`             | `string` | MDM + Bootstrap | —       | For VPC endpoints or gateway proxies. Host origin only.                                                           |
| <span id="inferencebedrockservicetier" />Bedrock service tier<br />`inferenceBedrockServiceTier` | `enum`   | MDM + Bootstrap | —       | Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand. One of: `flex`, `priority`.            |
| <span id="inferencebedrockbearertoken" />AWS bearer token<br />`inferenceBedrockBearerToken`     | `string` | MDM + Bootstrap | —       | Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those. |
| <span id="inferencebedrockssostarturl" />AWS SSO start URL<br />`inferenceBedrockSsoStartUrl`    | `string` | MDM + Bootstrap | —       | Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.                              |
| <span id="inferencebedrockssoregion" />AWS SSO region<br />`inferenceBedrockSsoRegion`           | `string` | MDM + Bootstrap | —       | IAM Identity Center home region.                                                                                  |
| <span id="inferencebedrockssoaccountid" />AWS SSO account ID<br />`inferenceBedrockSsoAccountId` | `string` | MDM + Bootstrap | —       | 12-digit AWS account ID assigned to users in IAM Identity Center.                                                 |
| <span id="inferencebedrockssorolename" />AWS SSO role name<br />`inferenceBedrockSsoRoleName`    | `string` | MDM + Bootstrap | —       | IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.                      |
| <span id="inferencebedrockprofile" />AWS profile name<br />`inferenceBedrockProfile`             | `string` | MDM + Bootstrap | —       | AWS named profile to use for Bedrock inference credentials.                                                       |
| <span id="inferencebedrockawsdir" />AWS config directory<br />`inferenceBedrockAwsDir`           | `string` | MDM + Bootstrap | —       | Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.                              |
| <span id="inferencebedrockawsclipath" />AWS CLI path<br />`inferenceBedrockAwsCliPath`           | `string` | MDM + Bootstrap | —       | Absolute path to the aws executable. Leave unset to find it on PATH.                                              |

<AccordionGroup>
  <Accordion title="inferenceBedrockServiceTier details">
    Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.
  </Accordion>
</AccordionGroup>

Set `inferenceModels` to a list of Amazon Bedrock inference-profile IDs, for example `us.anthropic.claude-sonnet-5`. When using a bearer token or credential helper, Claude Desktop auto-discovers available Claude models from your account if this is unset; for profile or SSO authentication, the list is required. Application-inference-profile ARNs and provisioned-throughput ARNs are also accepted; pair them with a [`labelOverride`](/docs/third-party/claude-desktop/configuration#inferencemodels) so the picker shows a readable name instead of the raw ARN. See the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencemodels).

## What users experience

The first-launch and re-authentication behavior depends on the authentication approach.

| Approach           | First launch                                                                                                                                 | Re-authentication                                                                                                                                         |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bearer token       | The app opens directly; no user action.                                                                                                      | Never, until you rotate the key in the managed profile.                                                                                                   |
| In-app AWS sign-in | The app shows a **Sign in with AWS** page; the user approves in the browser, and the app returns to Cowork.                                  | When the IAM Identity Center access portal session expires (defaults to 8 hours; configurable up to 90 days). The app prompts in-app; no terminal needed. |
| Named profile      | The app opens directly if the AWS SSO cache is fresh; otherwise it prompts in-app and runs `aws sso login` for you, which opens the browser. | When the IAM Identity Center session expires, the app prompts in-app and re-runs `aws sso login`.                                                         |

For in-app AWS sign-in, the browser flow runs on the host (outside the Cowork sandbox), so it uses the user's existing identity-provider session and any security keys or passkeys configured on the device. The **AWS access portal session duration** setting (IAM Identity Center → **Settings** → **Authentication**) controls how long users stay signed in across app restarts. To force a user to sign in again sooner, delete their active session from the IAM Identity Center console.

If the app cannot locate the AWS CLI, it cannot drive the login itself; it instructs the user to install AWS CLI v2 and run `aws sso login --profile <name>` manually.

## Troubleshoot

To confirm which keys the app read and whether credentials validated, use **Help → Troubleshooting → Copy Managed Configuration Report**; see [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [Data storage and residency](/docs/third-party/claude-desktop/data-storage).

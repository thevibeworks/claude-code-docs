> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude Desktop on 3P with Amazon Bedrock Mantle

> Configure Claude Desktop on 3P to use Claude models through Amazon Bedrock Mantle's Anthropic-native API surface

Amazon Bedrock Mantle is Amazon Bedrock's Anthropic-native API surface. Unlike the standard [Amazon Bedrock provider](/docs/third-party/claude-desktop/bedrock.md), Mantle speaks the Anthropic Messages API directly and authenticates with a bearer token rather than the AWS SigV4 credential chain, so no AWS CLI, named profile, or IAM Identity Center setup is needed on the device. In practice, Mantle is the Amazon Bedrock provider with a different runtime endpoint and a single bearer-token credential path.

## Choose an authentication approach

Mantle supports a bearer token only. There is no in-app AWS sign-in or named-profile support for this provider; if you need per-user IAM Identity Center authentication, use the standard [Amazon Bedrock provider](/docs/third-party/claude-desktop/bedrock.md) instead.

| Scenario | Use | Notes |
| - | - | - |
| Any Mantle deployment | [Bearer token](#bearer-token) (`inferenceBedrockBearerToken`) | A long-lived token distributed in the managed profile. |
| Token must not be stored statically | [Credential helper](/docs/third-party/claude-desktop/configuration.md#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the bearer token to stdout at runtime. |

## Set up AWS

Enable Claude models in Amazon Bedrock for the region you will set as `inferenceBedrockRegion`, and obtain a Mantle bearer token for that account. See [Set up AWS](/docs/third-party/claude-desktop/bedrock.md#set-up-aws) on the Amazon Bedrock page for the model-access step; the IAM Identity Center steps there are not needed for Mantle.

## Prepare devices

### Bearer token

No per-device preparation is required. Place the Mantle bearer token in the managed configuration as `inferenceBedrockBearerToken`.

The app reaches `bedrock-mantle.<region>.api.aws` (or the host in `inferenceBedrockBaseUrl` if you set one). This host is included automatically in the **Egress** section of the in-app configuration window. The `.api.aws` zone has no FIPS endpoint variant.

## Configure the app

Open the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration.md#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Bedrock Mantle**, then fill in the credentials card:

| Field | Value |
| - | - |
| AWS region | e.g. `us-east-1` |
| AWS bearer token | your Mantle bearer token |
| Bedrock base URL | *optional* |

If you set **Bedrock base URL**, provide the full SDK base URL including the `/anthropic` path (for example `https://bedrock-mantle.us-east-1.api.aws/anthropic`); it replaces the default `bedrock-mantle.<region>.api.aws/anthropic` endpoint.

Under **Models**, add at least one **Model list** entry. Mantle has no model-list endpoint, so model discovery is not available and `inferenceModels` is required.

Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](/docs/third-party/claude-desktop/mdm.md) for the export and deployment workflow.

### Configuration keys

Mantle reuses the `inferenceBedrock*` key names. Only `inferenceBedrockRegion`, `inferenceBedrockBearerToken`, and `inferenceBedrockBaseUrl` apply; the other keys below (`inferenceBedrockProfile`, `inferenceBedrockSso*`, `inferenceBedrockAwsDir`, `inferenceBedrockAwsCliPath`, `inferenceBedrockServiceTier`) are ignored for this provider.

[Entry labels](/docs/third-party/claude-desktop/configuration.md#entry-labels) says what each label means.

#### `inferenceBedrockRegion`

stringSince 1.2581.0

**AWS region.** AWS region for the Bedrock runtime endpoint.

***

#### `inferenceBedrockBaseUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Origin-pinned (A URL that a bootstrap server delivers must share the origin of bootstrapUrl, or Claude Desktop drops it. The limit is lifted when bootstrapOidc is set, and it does not apply to a value set in an MDM profile, the local configuration file or the Enterprise Admin Console.)

Since 1.2581.0

**Bedrock base URL.** For VPC endpoints or gateway proxies. Host origin only.

***

#### `inferenceBedrockServiceTier`

enumSince 1.5186.0

**Bedrock service tier.** Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand.

One of: `flex`, `priority`

> **More detail**
>
> Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.

***

#### `inferenceBedrockBearerToken`

stringSince 1.2581.0

**AWS bearer token.** Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those.

***

#### `inferenceBedrockSsoStartUrl`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO start URL.** Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below.

***

#### `inferenceBedrockSsoRegion`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO region.** IAM Identity Center home region.

***

#### `inferenceBedrockSsoAccountId`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO account ID.** 12-digit AWS account ID assigned to users in IAM Identity Center.

***

#### `inferenceBedrockSsoRoleName`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.6259.0

**AWS SSO role name.** IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above.

***

#### `inferenceBedrockProfile`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS profile name.** AWS named profile to use for Bedrock inference credentials.

***

#### `inferenceBedrockAwsDir`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.2581.0

**AWS config directory.** Folder with AWS config/credentials. Defaults to \~/.aws when no bearer token is set.

***

#### `inferenceBedrockAwsCliPath`

string

Consent required (A value that a bootstrap server or a self-hosted session host delivers applies only after the user approves it, unless machine-scoped device management set that server's address. For a bootstrap server, the trustBootstrapDelivery key overrides that default. A value set in an MDM profile, the local configuration file or the Enterprise Admin Console needs no approval.)

Since 1.13576.0

**AWS CLI path.** Absolute path to the aws executable. Leave unset to find it on PATH.

***

You must also set `inferenceModels`. As with the standard Amazon Bedrock provider, server-side Web Search is not supported. See the [Configuration reference](/docs/third-party/claude-desktop/configuration.md#inferencemodels).

## What users experience

The app opens directly on first launch with no user action. Users are never prompted to sign in; re-authentication happens only when you rotate the bearer token in the managed profile.

## Troubleshoot

To confirm which keys the app read and whether the provider settings validated, use **Help → Troubleshooting → Generate Diagnostic Report**, export the report, and check `managed-config.txt` and `provider-status.txt`; see [Verifying the deployment](/docs/third-party/claude-desktop/installation.md#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [User identity and local data](/docs/third-party/claude-desktop/data-storage.md#where-data-lives).

> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect an AWS role

> Let Claude sign in to an IAM role in your AWS account with a short-lived identity token instead of stored access keys. Covers the identity provider and trust policy to create in AWS, how to connect the role in the console, and how to verify the connection in CloudTrail.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>AWS roles are connected at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation and use the **Cloud roles** section. Connecting a role needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

With an AWS role connection, Claude signs in to an IAM role in your AWS account with a short-lived identity token and calls AWS with the role's permissions. No access key is stored in Claude. The token names your organization and the [agent](/docs/claude-tag/concepts/agent-identity) making the request (Claude's identity in one Slack channel), and your role's trust policy decides which tokens to accept. If someone else manages your AWS account, give them the values from the console and the trust policy below; the console steps need a Claude Tag admin.

## Before you begin

* You're an organization Owner, or an admin with full Claude Tag management permission.
* You can create an IAM identity provider and an IAM role in an AWS account in the standard AWS partition. Roles in AWS GovCloud (US) and AWS China can't be connected.
* You know which AWS service hosts Claude will call, for example `s3.us-west-2.amazonaws.com` and `*.s3.us-west-2.amazonaws.com` for S3 in one region.

## Copy the values from the console

In **Cloud roles**, click **Connect an AWS role** and copy the **Issuer**, **Audience**, and **Subject prefix** rows from the **Set the role's trust policy to accept these values** card. Then click **Cancel**; you connect the role after creating it in AWS.

| Value          | What it is                                                                                                                                                                                          |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issuer         | `https://identity.anthropic.com/agents`. The URL of the identity provider you create in AWS, including the `/agents` path.                                                                          |
| Audience       | `sts.amazonaws.com`. The same for every organization, so it can't identify yours.                                                                                                                   |
| Subject prefix | `wimse://identity.anthropic.com/org/<your organization ID>/agent/`. Every token's subject starts with this prefix and ends with one agent's ID. The trust policy must require at least this prefix. |

## Create the identity provider and role in AWS

<Steps>
  <Step title="Create the IAM identity provider">
    In the AWS account that owns the role, create an IAM OpenID Connect (OIDC) identity provider with the provider URL `https://identity.anthropic.com/agents` and the audience `sts.amazonaws.com`. Include the `/agents` path. A provider created with the bare hostname, or with any other path, makes every sign-in fail later with an invalid-token or provider error from AWS. You don't need to supply a certificate thumbprint, because AWS verifies the provider's certificate itself.

    To confirm the provider, run `aws iam get-open-id-connect-provider --open-id-connect-provider-arn <provider ARN>` and check that `Url` is `identity.anthropic.com/agents` (AWS stores the URL without `https://`) and `ClientIDList` contains `sts.amazonaws.com`.
  </Step>

  <Step title="Create the role with this trust policy">
    Create an IAM role with the trust policy below. Replace the account ID with yours (the rest of the provider ARN is the same for every account), and replace the `sub` value with your **Subject prefix** followed by `*`.

    ```json theme={null}
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::123456789012:oidc-provider/identity.anthropic.com/agents"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "identity.anthropic.com/agents:aud": "sts.amazonaws.com"
            },
            "StringLike": {
              "identity.anthropic.com/agents:sub": "wimse://identity.anthropic.com/org/org_01Hx7rQkPzT9sN3mVbJw2eYd/agent/*"
            }
          }
        }
      ]
    }
    ```

    Keep both conditions. Because every organization's tokens come from the same issuer with the same audience, the `sub` condition is the only thing that limits the role to your organization; see [Authorize on the subject](/docs/claude-tag/admins/federated-access/token-reference#authorize-on-the-subject). The wildcard replaces only the agent ID at the end. Never put a wildcard before `/agent/`. `StringEquals` on the prefix never matches, so keep the prefix condition under `StringLike`. Both condition keys start with `identity.anthropic.com/agents:` (the issuer without `https://`).

    The prefix condition is the minimum, and it admits every agent in your organization. Where your use case allows, pin the role to specific agents instead, which is the strongest form: use `StringEquals` on `identity.anthropic.com/agents:sub` with one full subject, or a JSON array of full subjects. The console doesn't show agent IDs, so you learn a subject from CloudTrail after a first sign-in under the prefix condition. Agent IDs change when a Slack channel is deleted and recreated, so update the policy when that happens.
  </Step>

  <Step title="Attach permissions">
    Attach a least-privilege permissions policy to the role for the work Claude will do. The check under [Verify the connection](#verify-the-connection) needs no permissions. Each sign-in gives Claude temporary credentials that last 1 hour, the AWS default. Claude doesn't ask for a different length, and the role's maximum session duration setting doesn't change this. To cut off access before they expire, use the role's **Revoke active sessions** option in IAM or change its permissions.
  </Step>
</Steps>

## Connect the role in the console

<Steps>
  <Step title="Open the Connect an AWS role dialog">
    In **Cloud roles**, click **Connect an AWS role**.
  </Step>

  <Step title="Enter the role ARN">
    In the **Role ARN** field, enter the role's ARN, for example `arn:aws:iam::123456789012:role/ClaudeTag`. The role's name is used as the connection's name.
  </Step>

  <Step title="Narrow the allowed AWS hosts">
    The **Allowed AWS hosts** field starts with `*.amazonaws.com`, which lets Claude use the role with any AWS service. Keep that entry for the first verification, then narrow the list to the hosts Claude needs from the connection's [**Edit connection** dialog](/docs/claude-tag/admins/add-connections#set-allowed-websites) on the bundle's **Credentials** tab. A wildcard covers subdomains only: `*.s3.us-west-2.amazonaws.com` matches `example-reports.s3.us-west-2.amazonaws.com` but not `s3.us-west-2.amazonaws.com`. The AWS CLI and SDKs use both forms for S3, so list both the plain host and the wildcard for each region, and for `us-east-1` also `*.s3.amazonaws.com`, the older global S3 address some tools still use there. Every host must end in `.amazonaws.com`. The sign-in itself goes to the AWS Security Token Service (STS) from Anthropic's side and doesn't need an entry here.
  </Step>

  <Step title="Confirm the trust policy">
    Select the checkbox labeled **The role's trust policy requires the subject prefix shown above**. The **Connect role** button stays disabled until you do. Select it only if the trust policy pins `sub` to one or more full subjects under your **Subject prefix**, or to your prefix followed by `*` under `StringLike`, as described under [Create the identity provider and role in AWS](#create-the-identity-provider-and-role-in-aws).
  </Step>

  <Step title="Choose an Access bundle and connect">
    Choose a bundle from the **Access bundle** list, or click **New bundle**, enter a **Bundle name**, and click **Create bundle**. Then click **Connect role**. This creates a [connection](/docs/claude-tag/admins/add-connections) in that bundle, labeled **AWS role** on its **Credentials** tab, with the hosts you entered under **Allowed hosts**. A role can be connected in one bundle only; to use it in several scopes (workspaces or channels), attach that bundle to each.
  </Step>
</Steps>

The **Cloud roles** table has **Role**, **Access bundle**, **Allowed hosts**, **Added**, and **Actions** columns. Each connection's name appears under **Role** with the role's ARN and an **AWS role** chip beneath it, and **Remove** is under **Actions**.

## Let agents use the role

Claude uses the role in channels whose scope has the bundle attached. [Attach the bundle to a workspace or channel](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) if it isn't attached already.

Claude also needs to know what the role is for. Add a line like this to the scope's [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions):

```text wrap theme={null}
Use the AWS CLI to read the S3 bucket example-reports in us-west-2. AWS access is already set up.
```

Claude calls AWS with `curl`, an AWS SDK, or the AWS CLI, as with an [AWS SigV4 credential](/docs/claude-tag/admins/connections/custom#aws-sigv4). [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) signs each request at the network boundary with the role's temporary credentials, so the sandbox never holds them.

New threads pick up the connection on their own. In a thread already running, ask Claude to use AWS. If Claude still can't, send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) at the channel's top level (not inside a thread) to start a fresh session with your organization's current configuration.

## Verify the connection

In a channel whose workspace or channel has the bundle attached, start a new thread and ask Claude to run a connectivity check. The check is Claude's own request to `sts.amazonaws.com`, so keep `*.amazonaws.com` under the connection's **Allowed hosts** for this check, or add `sts.amazonaws.com` if you already narrowed the list. The sign-in itself needs no entry there. After the check passes, remove `sts.amazonaws.com` again if you added it, or narrow the wildcard. While it is listed, Claude can send any STS request signed with the role's credentials. If the role is allowed to assume another role, the credentials AWS returns are readable in Claude's sandbox. The call needs no permissions policy on the role. Send Claude this prompt:

```text wrap theme={null}
@Claude Connectivity check for this channel's AWS connection. Please run exactly:

curl -sS -o /tmp/resp.txt -w '%{http_code}' 'https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15'

and tell me the HTTP status code it prints and, only if it is not 200, the first 200 characters of /tmp/resp.txt.
```

A status of 200 means the sign-in worked. Then check CloudTrail in the AWS account for an `AssumeRoleWithWebIdentity` event on your role whose identity provider names `identity.anthropic.com/agents`. Claude signs in at the global STS endpoint, `sts.amazonaws.com`, so the event is recorded in the US East (N. Virginia) region; look there or in a multi-region trail, and allow a few minutes for it to appear. The role session name is an opaque ID for the Claude session that signed in. Claude may reuse one sign-in's credentials for most of the hour across threads in the same channel, so not every request produces a sign-in event. After AWS denies a request, Claude signs in again on the next one.

If Claude reports that the request was refused, CloudTrail usually shows why.

* No sign-in event at all means the request never reached AWS, most often because the host isn't in the connection's **Allowed AWS hosts**.
* An invalid-token or provider error on the sign-in usually means the identity provider's URL doesn't exactly match the issuer, `https://identity.anthropic.com/agents`.
* `AccessDenied` on the sign-in means the trust policy didn't accept the token. Check the `sub` condition and the condition-key prefix.
* A denied action after a successful sign-in means AWS denied the action. Check the role's permissions policy first, then any bucket policy, permissions boundary, or service control policy.

See [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting) for the errors Claude shows.

To disconnect a role, click **Remove** in the role's row of the **Cloud roles** table, then **Remove role** in the confirmation. Claude stops using the role within about a minute, in existing threads as well as new ones, and the connection is removed from its bundle. Credentials from an earlier sign-in stay valid in AWS until they expire, within 1 hour; they're held only by Agent Proxy, never by Claude's sandbox.

## Common errors

Two messages come up while connecting:

* **"This role is already connected in the bundle"**: the role already has its one connection. [Attach that bundle to the scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) instead.
* **"Enter a role ARN like `arn:aws:iam::123456789012:role/ClaudeTag`"**: the **Role ARN** field rejected the value, most often because the ARN is in the AWS GovCloud (US) or AWS China partition, which can't be connected.

For other dialog messages, see [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the Access bundle and connection model
* [Attach a bundle to a scope](/docs/claude-tag/admins/attach-to-scope): where a role connection applies
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim in the token, lifetimes, and key rotation
* [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting): console and runtime errors for every connection type
* [AWS SigV4 credential](/docs/claude-tag/admins/connections/custom#aws-sigv4): the stored-key alternative, and how Claude signs AWS requests

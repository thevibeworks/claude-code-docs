> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect a service that isn't in the list

> Connect a tool that has no built-in preset to Claude Tag. Covers credential types, what each form field means, and how to add a custom MCP server.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

For a service that doesn't have a preset Connect button, use **Custom tool** on the bundle's Credentials tab. This works for any service with an HTTP API. The [BigQuery](/docs/claude-tag/admins/connections/bigquery) guide is a worked example.

## Add a custom HTTP API

### What you need from the service

* A service-account credential (an API key, token, or OAuth client), not your personal login
* The API host (for example `api.example.com`)
* How the API authenticates (which header or flow it expects)

See [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service) for the service-account patterns.

### Fill out the Custom tool form

| Field                        | What to enter                                                                                                                                                                                                                                                                                                  |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                     | A label for this connection (for example "Internal billing API")                                                                                                                                                                                                                                               |
| **Credential type**          | Pick the type that matches how the API authenticates; see [Credential types](#credential-types)                                                                                                                                                                                                                |
| **Allowed websites**         | The API's host (for example `api.example.com`). A wildcard is allowed as the leftmost label. You can't enter `*` alone here; a credential is always limited to specific hosts (see [Allow all hosts](/docs/claude-tag/admins/add-connections#allow-all-hosts)). The credential is sent only to hosts you list here. |
| **Path prefixes** (optional) | Restrict the credential to specific URL paths under the host. Shown only for the MCP Connector type, and only when the provider you pick doesn't fix its own hosts and paths.                                                                                                                                  |
| **Custom headers**           | Any extra headers the API requires beyond the credential. Shown only for the Bearer credential type.                                                                                                                                                                                                           |

After saving, where the credential has an allow rule, you can narrow it by HTTP method and path from its **Edit connection** dialog; see [Restrict by path or method](/docs/claude-tag/admins/add-connections#restrict-by-path-or-method).

### Credential types

| Type                                            | Use for                                                                                                     |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Bearer**                                      | An API key or token sent as `Authorization: Bearer <token>`. Most SaaS REST APIs.                           |
| **Basic**                                       | HTTP Basic authentication (`Authorization: Basic <base64(user:password)>`)                                  |
| **Body parameter**                              | A token the API expects in the request body or query string instead of a header                             |
| **AWS SigV4**                                   | AWS services and APIs that require Signature Version 4 signing                                              |
| **GCP access token (with Service Account Key)** | Google Cloud APIs; the proxy exchanges the SA key for an access token                                       |
| **GCP IAP (with Service Account Key)**          | Google Cloud services behind Identity-Aware Proxy                                                           |
| **OAuth 2.0 JWT bearer**                        | APIs that accept a JWT signed with your private key in exchange for an access token (DocuSign, for example) |
| **OAuth 2.0 client credentials**                | Machine-to-machine OAuth with a client ID and secret                                                        |
| **MCP Connector**                               | OAuth sign-in. Sign in once as an admin; the agent acts as that account.                                    |

For GitHub repositories, use the GitHub connection at [Configure GitHub access](/docs/claude-tag/admins/configure-github) rather than a credential from this table.

If you're unsure which type, check the service's API authentication docs for which header or flow it expects.

### AWS SigV4

Use the **AWS SigV4** credential type for AWS service APIs (S3, Lambda, Amazon Bedrock, an API Gateway endpoint with IAM authorization). Agent Proxy reads the AWS service and signing region from the hostname and signs each outbound request with the credential at the boundary, so neither the model nor the sandbox holds the keys. The host must be an `amazonaws.com` endpoint; the proxy can't sign requests to an API Gateway custom domain or to a non-AWS API that uses Signature Version 4.

| Field             | Value                                                                                                                   |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------- |
| Access key ID     | The IAM user or role access key, for example `AKIAIOSFODNN7EXAMPLE`                                                     |
| Secret access key | The matching secret access key                                                                                          |
| Session token     | Optional. Only needed for temporary credentials from AWS STS.                                                           |
| Allowed websites  | The AWS service endpoint host, for example `s3.us-east-1.amazonaws.com` or `abc123.execute-api.us-east-1.amazonaws.com` |

Use long-lived credentials from a dedicated IAM user where you can. Temporary STS credentials work but expire on their own schedule, and the connection stops working when they do; you re-enter all three values to rotate.

Claude can call the endpoint with `curl`, an AWS SDK, or the AWS CLI. The sandbox holds no real AWS credentials, so a CLI or SDK signs the request with placeholder values; Agent Proxy strips that signature and re-signs with the stored credential before the request leaves for AWS. The one shape it can't re-sign is chunked payload signing. If Claude reports that chunked signing isn't supported through the proxy, have it set `payload_signing_enabled = false` in `~/.aws/config` and retry.

#### When AWS returns `SignatureDoesNotMatch`

A `SignatureDoesNotMatch` response from AWS means the request AWS received doesn't match the one Agent Proxy signed.

| Check                                                                   | What to do                                                                                                                                                                                    |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The access key ID and secret access key belong to the same IAM identity | Re-enter the access key ID, secret access key, and session token together. The form is write-only, so a partial update can leave them mismatched.                                             |
| No proxy or gateway of your own sits between Anthropic and AWS          | A second proxy that adds, strips, or reorders headers, or that re-signs the request, invalidates the signature Agent Proxy attached. Point **Allowed websites** at the AWS endpoint directly. |

A dropped or expired session token is a different failure: AWS rejects it with a token error such as `InvalidClientTokenId`, not `SignatureDoesNotMatch`. Rotate all three fields.

### OAuth 2.0 JWT bearer

Use the **OAuth 2.0 JWT bearer** credential type for APIs that exchange a JWT signed with your private key for an access token. The [Salesforce guide](/docs/claude-tag/admins/connections/salesforce) is a worked example.

The **Private key (PEM)** field takes a PEM-encoded RSA private key without a passphrase, the format that begins with `-----BEGIN PRIVATE KEY-----` or `-----BEGIN RSA PRIVATE KEY-----`. Identity providers such as Okta export the key as a JWK (a JSON object) by default; convert a JWK to PEM before pasting it. The form doesn't check the key's format, so a key in the wrong format fails only when you save.

#### When saving fails with "Failed to create egress credential"

Saving the form can return the error "Failed to create egress credential. Check your inputs and try again." The most likely cause is a private key that isn't PEM-encoded, for example a JWK pasted as-is into the **Private key (PEM)** field. Convert the key to PEM and save again.

Saving also fails when a PEM-encoded key isn't an RSA key or has a passphrase. Once the key is in the right format, re-check each field against the values from your service.

## Add a custom MCP server

The server must be a remote endpoint that Claude can reach at a URL over the internet. An MCP server that runs on a person's machine over stdio, including one packaged as a [desktop extension](/docs/connectors/custom/desktop-extensions), can't be connected, because [sessions](/docs/claude-tag/concepts/glossary#session) run in a cloud sandbox that Anthropic hosts, not on anyone's machine. Host the server as a remote endpoint first, then follow the steps below.

To give Claude an MCP server (one you run, or a vendor's hosted MCP endpoint), the pattern is a plugin plus a credential:

<Steps>
  <Step title="Add a plugin that declares the MCP server">
    In the bundle's **Plugins** tab (or via your [skills repository](/docs/claude-tag/admins/skills-repo)), add a plugin whose `.mcp.json` points at the server URL. The plugin tells Claude the server exists and how to call it.
  </Step>

  <Step title="Add a credential for the server's host">
    On the **Credentials** tab, click **Connect** next to **Custom tool** and add a credential for the MCP server's host (for example, a Bearer token with **Allowed websites** set to `your-mcp-host.example.com`). This lets the call leave the sandbox with auth attached.
  </Step>
</Steps>

The plugin's `.mcp.json` is loaded because it's part of an attached plugin; an `.mcp.json` checked into a repository Claude clones is not loaded.

## Verify the connection

In a channel under the bundle's scope, in a new thread, ask Claude to make a small read against the API:

```text wrap theme={null}
@Claude can you reach api.example.com? Try a GET on /health.
```

Check the service's own audit log to confirm the call landed under your service account. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

If Claude reports that it can't use the credential, check its status on the [Access bundles page](https://claude.ai/admin-settings/claude-tag/access-bundles). **Not active** means no allow rule uses the credential yet. **Approval needed** means another admin submitted it through a shared setup link; select **Review**, then **Approve**. See [Verify the connection saved](/docs/claude-tag/admins/add-connections#verify-the-connection-saved).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connection model
* [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential): for public APIs that need no auth
* [Allow all hosts](/docs/claude-tag/admins/add-connections#allow-all-hosts): the egress option that lets Claude reach any public host without a credential

> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect a service that isn't in the list

> Connect a tool that isn't in Claude Tag's connector list. Covers credential types, what each form field means, and how to add a custom MCP server.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

For a service that isn't in the **Add a connector** list, add a custom connector. This works for any service with an HTTP API. The [BigQuery](/docs/claude-tag/admins/connections/bigquery) guide is a worked example.

To open the form, go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Connectors** tab, click **Add**, and select **Custom connector** at the bottom of the list. A connector added there for a host that isn't on the **Connectors** tab yet is on in every workspace and channel once you save it. For a host already listed under **Custom hosts**, the new credential starts off everywhere until you choose where it applies. For narrower reach:

* **Some channels**: [restrict it on its page](/docs/claude-tag/admins/add-connections#restrict-a-connector-to-some-channels).
* **One workspace or channel**: on that place's page, click **Add** under **Claude's access**, select **Connector**, select **Custom connector** under **Connect new** on the **Connectors** tab, and click **Continue**. See [Connect a service for one workspace or channel](/docs/claude-tag/admins/add-connections#connect-a-service-for-one-workspace-or-channel).
* **The places a bundle applies**: add it to the [bundle](/docs/claude-tag/admins/add-connections#create-a-bundle). Open the bundle's page, and under **What's in it** click **Add**, choose **Connector**, and select **Custom connector**.

## Add a custom HTTP API

### What you need from the service

* A service-account credential (an API key, token, or OAuth client), not your personal login
* The API host (for example `api.example.com`)
* How the API authenticates (which header or flow it expects)

See [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service) for the service-account patterns.

<a id="fill-out-the-custom-tool-form" />

### Fill out the custom connector form

| Field | What to enter |
| :- | :- |
| **Name** | A label for this connector (for example "Internal billing API") |
| **Credential type** | Pick the type that matches how the API authenticates; see [Credential types](#credential-types) |
| **Allowed websites** | The API's host (for example `api.example.com`). A wildcard is allowed as the leftmost label. You can't enter `*` alone here; a credential is always limited to specific hosts (see [Allow all hosts](/docs/claude-tag/admins/add-connections#allow-all-hosts)). The credential is sent only to hosts you list here. |
| **Path prefixes** (optional) | Restrict the credential to specific URL paths under the host. For the MCP Connector type, shown only when the provider you pick doesn't fix its own hosts and paths. |
| **Custom headers** | Any extra headers the API requires beyond the credential. Shown only for the Bearer credential type. |

After saving, where the credential has an allow rule, you can narrow it by HTTP method and path from its **Edit connection** dialog, opened from **Edit** in the credential's row menu on the connector's page; see [Restrict by path or method](/docs/claude-tag/admins/add-connections#restrict-by-path-or-method). To narrow a credential before any channel can use it, add the connector to a new [bundle](/docs/claude-tag/admins/add-connections#create-a-bundle), select **Edit** from the menu on its row under **What's in it**, and add the bundle's places last.

### Credential types

| Type | Use for |
| :- | :- |
| **Bearer** | An API key or token sent as `Authorization: Bearer <token>`. Most SaaS REST APIs. |
| **Basic** | HTTP Basic authentication (`Authorization: Basic <base64(user:password)>`) |
| **Body parameter** | A token the API expects in the request body or query string instead of a header |
| **AWS SigV4** | AWS service APIs on `amazonaws.com` endpoints that require Signature Version 4 signing |
| **GCP access token (with Service Account Key)** | Google Cloud APIs; the proxy exchanges the SA key for an access token |
| **GCP IAP (with Service Account Key)** | Google Cloud services behind Identity-Aware Proxy |
| **OAuth 2.0 JWT bearer** | APIs that accept a JWT signed with your private key in exchange for an access token (DocuSign, for example) |
| **OAuth 2.0 client credentials** | Machine-to-machine OAuth with a client ID and secret |
| **MCP Connector** | OAuth sign-in to one of the providers in the picker or to a [remote MCP connector](/docs/connectors/custom/add-unlisted) your organization has added on claude.ai. Sign in once as an admin; the agent acts as that account. Other OAuth APIs can't be connected this way. |

<Note>The **MCP Connector** type signs in to a connector from your organization's connector library. If you register a new connector from this form with **Add custom connector…**, that connector is added to the library on the **Connectors** page at [`claude.ai/admin-settings/connectors`](https://claude.ai/admin-settings/connectors), not only to Claude Tag. Removing the Claude Tag connector later leaves the library entry in place.</Note>

For GitHub repositories, use the Claude GitHub App at [Configure GitHub access](/docs/claude-tag/admins/configure-github) rather than a credential from this table.

If you're unsure which type, check the service's API authentication docs for which header or flow it expects.

### AWS SigV4

Use the **AWS SigV4** credential type for AWS service APIs such as S3, Lambda, and DynamoDB. Agent Proxy reads the AWS service and signing region from the hostname and signs each outbound request with the credential at the boundary, so neither the model nor the sandbox holds the keys.

Agent Proxy signs requests to hostnames in these forms:

* `service.region.amazonaws.com`
* S3 virtual-hosted-style endpoints, for example `my-bucket.s3.us-east-1.amazonaws.com`
* Service hostnames with extra parts before the service name, as long as the region is the last part before `amazonaws.com`, for example the Amazon ECR API host `api.ecr.us-east-1.amazonaws.com` or the host of an API Gateway invoke URL, `abc123.execute-api.us-east-1.amazonaws.com`
* Hosts with no region for S3 and for a fixed set of services that includes IAM, STS, Route 53, CloudFront, and Organizations, for example `iam.amazonaws.com` or `sts.amazonaws.com`

Requests to other hostnames fail before reaching AWS. Agent Proxy can't sign a request to a hostname with no region for any other service, such as `ec2.amazonaws.com`, or to a hostname with the region before the service name, such as an OpenSearch domain endpoint (`my-domain.us-east-1.es.amazonaws.com`). It also can't sign requests to an API Gateway custom domain or to a non-AWS API that uses Signature Version 4.

| Field | Value |
| :- | :- |
| Access key ID | The IAM user or role access key, for example `AKIAIOSFODNN7EXAMPLE` |
| Secret access key | The matching secret access key |
| Session token | Optional. Only needed for temporary credentials from AWS STS. |
| Allowed websites | The AWS service endpoint host, for example `s3.us-east-1.amazonaws.com` or `lambda.us-east-1.amazonaws.com` |

Use long-lived credentials from a dedicated IAM user where you can. Temporary STS credentials work but expire on their own schedule, and the connector stops working when they do; you re-enter all three values to rotate.

Claude can call the endpoint with `curl`, an AWS SDK, or the AWS CLI. The sandbox holds no real AWS credentials, so a CLI or SDK signs the request with placeholder values; Agent Proxy strips that signature and re-signs with the stored credential before the request leaves for AWS. If a request comes back with HTTP 502 and a reason that begins `injection failed ("<connection name>")`, Agent Proxy couldn't sign it. The troubleshooting entry [An AWS request fails after a successful sign-in](/docs/claude-tag/admins/federated-access/troubleshooting#an-aws-request-fails-after-a-successful-sign-in) lists each cause the reason text names and its fix; the causes and fixes are the same for a connector that stores an access key.

#### When AWS returns `SignatureDoesNotMatch`

A `SignatureDoesNotMatch` response from AWS means the request AWS received doesn't match the one Agent Proxy signed.

| Check | What to do |
| :- | :- |
| The access key ID and secret access key belong to the same IAM identity | Re-enter the access key ID, secret access key, and session token together. The form is write-only, so a partial update can leave them mismatched. |
| No proxy or gateway of your own sits between Anthropic and AWS | A second proxy that adds, strips, or reorders headers, or that re-signs the request, invalidates the signature Agent Proxy attached. Point **Allowed websites** at the AWS endpoint directly. |

A dropped or expired session token is a different failure: AWS rejects it with a token error such as `InvalidClientTokenId`, not `SignatureDoesNotMatch`. Rotate all three fields.

### OAuth 2.0 JWT bearer

Use the **OAuth 2.0 JWT bearer** credential type for APIs that exchange a JWT signed with your private key for an access token. The [Salesforce guide](/docs/claude-tag/admins/connections/salesforce) is a worked example.

The **Private key (PEM)** field takes a PEM-encoded RSA private key without a passphrase, the format that begins with `-----BEGIN PRIVATE KEY-----` or `-----BEGIN RSA PRIVATE KEY-----`. Identity providers such as Okta export the key as a JWK (a JSON object) by default; convert a JWK to PEM before pasting it. The form doesn't check the key's format, so a key in the wrong format fails only when you save.

#### When saving fails with "Failed to create egress credential"

Saving the form can return the error "Failed to create egress credential. Check your inputs and try again." The most likely cause is a private key that isn't PEM-encoded, for example a JWK pasted as-is into the **Private key (PEM)** field. Convert the key to PEM and save again.

Saving also fails when a PEM-encoded key isn't an RSA key or has a passphrase. Once the key is in the right format, re-check each field against the values from your service.

## Add a custom MCP server

The server must be a remote endpoint that Claude can reach at a URL over the internet. An MCP server that runs on a person's machine over stdio, including one packaged as a [desktop extension](/docs/connectors/custom/add-unlisted#install-a-local-connector-in-the-desktop-app), can't be connected, because [sessions](/docs/claude-tag/concepts/glossary#session) run in a cloud sandbox that Anthropic hosts, not on anyone's machine. Host the server as a remote endpoint first, then follow the steps below.

To give Claude an MCP server (one you run, or a vendor's hosted MCP endpoint), the pattern is a plugin plus a credential:

<Steps>
  <Step title="Add a plugin that declares the MCP server">
    Add a plugin whose `.mcp.json` points at the server URL, from your organization's library or your [skills repository](/docs/claude-tag/admins/skills-repo), wherever the server should be available; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). The plugin tells Claude the server exists and how to call it.
  </Step>

  <Step title="Add a credential for the server's host">
    Add a custom connector for the MCP server's host (for example, a Bearer token with **Allowed websites** set to `your-mcp-host.example.com`), where the plugin applies. This lets the call leave the sandbox with auth attached.
  </Step>
</Steps>

The plugin's `.mcp.json` is loaded because it's part of an attached plugin; an `.mcp.json` checked into a repository Claude clones is not loaded.

## Verify the custom connector

In a channel where the connector applies, in a new thread, ask Claude to make a small read against the API:

```text wrap theme={null}
@Claude can you reach api.example.com? Try a GET on /health.
```

Check the service's own audit log to confirm the call landed under your service account. New threads pick up the connector on their own.

If Claude reports that it can't use the credential, open the connector from the **Connectors** tab, where custom connectors are listed under **Custom hosts**. In its **Access from** table, **Not enabled** means no allow rule sends the credential yet; click **Enable** and confirm. A credential a teammate submitted through a setup link waits on the **Requests** tab of [**Notifications**](https://claude.ai/admin-settings/notifications) as **Approval needed**; click **Review**, then **Approve**. See [Verify the connector saved](/docs/claude-tag/admins/add-connections#verify-the-connector-saved).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connector model
* [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential): for public APIs that need no auth
* [Allow all hosts](/docs/claude-tag/admins/add-connections#allow-all-hosts): the egress option that lets Claude reach any public host without a credential

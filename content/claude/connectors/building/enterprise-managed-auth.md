> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Managed Auth for connectors

> Support auto-connect in Claude by accepting identity assertions from a customer's identity provider or from Claude, so users skip the OAuth consent step.

> [!NOTE]
>
> Enterprise Managed Auth is available on Claude Team and Enterprise plans. After your authorization server supports it, email `mcp-review@anthropic.com` to have [your directory listing](https://claude.com/docs/connectors/building/managing-your-listing.md) marked as supporting Enterprise Managed Auth.

Enterprise Managed Auth (EMA) lets organizations connect their users to your MCP server without sending each user through an OAuth consent screen. Claude presents your authorization server with an identity assertion instead: a signed JSON Web Token (JWT) issued by [the customer's identity provider or by Claude](#who-issues-the-identity-assertion). Your authorization server validates the assertion and returns an access token.

Claude calls this feature auto-connect, for identity provider-issued and Claude-issued assertions alike. The connector directory labels listings marked as supporting it **Auto-connect**.

To support auto-connect, you [make your authorization server accept and validate the assertion](#authorization-server-requirements), [test your implementation](#test-your-implementation), and [give customer administrators the settings and documentation they need](#support-customer-administrators).

## Understand how Enterprise Managed Auth works

The diagram shows the exchange between Claude, your authorization server, and your MCP server. Your MCP server receives the same kind of bearer token it would after the interactive OAuth flow.

![Sequence diagram with three participants: Claude, your authorization server, and your MCP server. The user is already signed in to Claude. 1, Claude sends POST /token to your authorization server with the jwt-bearer grant and the signed JWT assertion. 2, your authorization server checks that iss is the issuer registered for the workspace, fetches that issuer's keys, and verifies the signature. 3, it validates typ, aud, client\_id, exp, and jti. 4, it returns an access\_token to Claude. 5, Claude sends the tool call to your MCP server with the Bearer access\_token. 6, your MCP server returns the tool result to Claude. Requests are solid arrows and responses are dashed arrows.](https://mintcdn.com/claude-ai/sb_HHLiaouvnOmRA/images/connectors/enterprise-managed-auth-exchange.svg?fit=max\&auto=format\&n=sb_HHLiaouvnOmRA\&q=85\&s=14077dd8e8d93a01f20bd21b1c031029)

The flow is defined by the [MCP enterprise managed authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization), and the identity assertion is based on the [Identity Assertion JWT Authorization Grant (ID-JAG)](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/).

### Who issues the identity assertion

Each customer workspace, meaning the customer's tenant in your product, trusts one issuer of identity assertions. The issuer for a customer is one of the following:

* **Identity provider-issued**: the customer's identity provider issues and signs the assertion under its own issuer URL, for a user who signed in to Claude through the organization's single sign-on (SSO).
* **Claude-issued**: Claude issues and signs the assertion under an issuer URL that belongs to the customer's Claude organization. The URL has the form `https://identity.anthropic.com/issuers/<issuer-id>`, where `<issuer-id>` differs for each Claude organization and isn't the organization's ID. Claude-issued assertions are in beta.

The token format and the exchange at your token endpoint are the same in both cases.

## Prerequisites

Before adding Enterprise Managed Auth, make sure the following are already in place:

* Your MCP server implements [MCP authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization), including Protected Resource Metadata (PRM) discovery. See the [authentication guide](https://claude.com/docs/connectors/building/authentication.md) for Claude-specific requirements
* Your authorization server registers Claude using either a client that Anthropic set up for your server's URL, as [Which credentials Claude uses when several are set](https://claude.com/docs/connectors/building/authentication.md#which-credentials-claude-uses-when-several-are-set) describes, or a [Client ID Metadata Document](https://claude.com/docs/connectors/building/authentication.md#dcr-and-cimd-details). Enterprise Managed Auth sign-ins don't use a client ID and secret that you entered in the developer portal. If that is how Claude is registered with you, email `mcp-review@anthropic.com` with your listing's name and its exact server URLs before you ask to have your listing marked as supporting Enterprise Managed Auth, and don't put the secret in the email

Enterprise Managed Auth works with [lazy authentication](https://claude.com/docs/connectors/building/lazy-authentication.md). When your MCP server answers a tool call with `401 Unauthorized` and the user's organization has Enterprise Managed Auth configured for your connector, Claude runs the exchange and retries the call instead of showing the **Connect** card.

Enterprise Managed Auth doesn't apply to authless servers. A fully authless server never returns `401`, so there is no point at which Claude can exchange an assertion.

> [!WARNING]
>
> Dynamic Client Registration (DCR) isn't supported with Enterprise Managed Auth. When the customer's identity provider issues the assertions, it stamps a fixed `client_id` into every one, so your authorization server must recognize that client before the first assertion arrives. The identifier of a client created through DCR never matches the `client_id` that the identity provider stamps.

## Authorization server requirements

If your MCP server relies on a hosted identity platform, confirm that the platform supports the JWT bearer authorization grant ([RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523)), runs every check in [Validate the identity assertion](#validate-the-identity-assertion), and can register an issuer URL that doesn't belong to the customer's identity provider as a trusted issuer.

**1. Ensure the JWT bearer grant is supported**

Your authorization server must accept `urn:ietf:params:oauth:grant-type:jwt-bearer` at its token endpoint and advertise it in the `grant_types_supported` array of its [authorization server metadata (RFC 8414)](https://datatracker.ietf.org/doc/html/rfc8414). In this example metadata, the grant type is highlighted:

```json {7} theme={null}
{
  "issuer": "https://auth.example.com",
  "token_endpoint": "https://auth.example.com/token",
  "grant_types_supported": [
    "authorization_code",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer"
  ]
}
```

List the grant type here even if your token endpoint already accepts it.

Claude sends assertions when your metadata also meets these conditions:

* The `issuer` matches the URL Claude fetched the metadata from, as [RFC 8414 section 3.3](https://datatracker.ietf.org/doc/html/rfc8414#section-3.3) requires
* The `token_endpoint` is on the same registrable domain as the `issuer`. Different hosts under that domain work, such as `https://api.example.com/token` for the issuer `https://www.example.com`

Keep the `issuer` value exactly as published, trailing slash included. A Claude-issued setup records the value, and a changed value stops sign-ins for that customer.

**2. Register the trusted issuer**

Bind each customer workspace to one trusted issuer rather than accepting any well-formed JWT, and allow that issuer to be a Claude issuer URL, not only a URL on an identity provider's domain. The binding happens in [your product's admin settings](#admin-settings-in-your-product), where a workspace's administrator enters the issuer URL and your authorization server stores it as that workspace's trusted issuer. Resolve each assertion to exactly one workspace, as [Validate the identity assertion](#validate-the-identity-assertion) describes.

> [!WARNING]
>
> Use the JWT validation built into your authorization server product, or its vendor's validation library, rather than writing your own signature verification.

**3. Understand the token request**

Claude sends a form-encoded `POST` to your authorization server's token endpoint. The highlighted parameters are the JWT bearer grant type, the signed assertion, and the `client_id` your server must already recognize:

```http {5-7} theme={null}
POST /token HTTP/1.1
Host: auth.example.com
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
&assertion=eyJhbGciOi...
&client_id=your-registered-client-id
&scope=read%20write
&resource=https://mcp.example.com
```

Client authentication is left out of this example. Answer at the `token_endpoint` URL itself, because Claude doesn't follow redirects on this request. The `client_id` is the value Claude is registered under at your authorization server, which for a Client ID Metadata Document is the document's URL. If that client has a secret or key, require it on this request:

* **Client secret**: Claude sends the secret in the request body, so accept `client_secret_post` for this client
* **Signed client assertion**: if Claude is registered with you through its Client ID Metadata Document and your authorization server metadata lists `private_key_jwt` in `token_endpoint_auth_methods_supported`, Claude can send this request as a second client, `https://claude.ai/oauth/mcp-oauth-client-metadata/confidential_client`, with a signed client assertion. Accept that `client_id` as well as the public document's URL, and verify the client assertion with the keys at the `jwks_uri` in the `confidential_client` document

The **Client** check in [Validate the identity assertion](#validate-the-identity-assertion) compares the assertion's `client_id` claim with this request's `client_id`:

* **Claude-issued**: the claim names the client that sends this request
* **Identity provider-issued**: the claim is the client ID that the customer's administrator registered for your connector in their identity provider. Claude's managed authorization setup gives the identity provider's setup the client ID that Claude presents on this request, so the two values should match when the administrator registers your connector through it. An administrator who registers your connector another way must enter the client ID that Claude presents on this request, so name it in your setup documentation

Adding or removing `private_key_jwt` in `token_endpoint_auth_methods_supported` changes which client Claude presents through its metadata document. After customers are set up, that change can make their identity provider-issued sign-ins fail the **Client** check until each administrator runs Claude's managed authorization setup again or enters the new client ID in their identity provider. Tell administrators before you make it.

A Claude-issued request always carries the `resource` parameter ([Resource Indicators, RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)), set to the `resource` in your Protected Resource Metadata when that is your MCP server's URL or a parent of it, and otherwise to your MCP server's URL. An identity provider-issued request carries it whenever the customer's identity provider supports forwarding it. Accept the request whether or not `resource` is present, and use it for audience binding when it is.

Your authorization server [validates the assertion](#validate-the-identity-assertion) and returns a standard OAuth token response with an access token. Include `expires_in` so Claude knows when to get a new token. Claude doesn't use a refresh token from this grant, so don't issue one for it. Keep issuing refresh tokens in the interactive OAuth flow, which relies on them.

### Identity assertion claims

This example shows the decoded payload of an identity assertion:

```json theme={null}
{
  "iss": "https://issuer.example.com",
  "sub": "abcdefghijklmnopqrstuvwxyz",
  "email": "alex@example.com",
  "aud": ["https://auth.example.com"],
  "client_id": "your-registered-client-id",
  "scope": "read write",
  "aud_tenant": "your-tenant-id",
  "iat": 1790000000,
  "nbf": 1789999985,
  "exp": 1790000045,
  "jti": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```

The `iss` claim is either the identity provider's issuer URL or a Claude issuer URL, whichever the workspace trusts. The ID-JAG format makes `email`, `scope`, and `aud_tenant` optional, so an identity provider can leave them out. A Claude-issued assertion always carries `email`, and can leave out `scope` and `aud_tenant`. The example's other values follow a Claude-issued assertion, and an identity provider can send `aud` as a string, leave out `nbf`, and set a different lifetime.

* **`sub` in identity provider-issued assertions**: `sub` is the identity provider's identifier for the user, and the ID-JAG format requires it to match the subject your product receives when that user signs in through SSO. Find the user by `iss` and `sub` together, among the members of the workspace the assertion resolved to.
* **`sub` and `email` in Claude-issued assertions**: `sub` is an opaque value that differs under each issuer and, unlike an identity provider's `sub`, doesn't match the subject your product receives through SSO, so [find the user by `email`](#claude-issued-assertions), not by `sub`. Storing that `sub` is optional.
* **`aud_tenant`**: your own identifier for a customer's workspace, for products where `iss` alone doesn't identify one workspace, such as when one customer has several workspaces that trust the same issuer. For identity provider-issued assertions, the customer's administrator can enter your tenant ID in their identity provider's settings for your product, if the identity provider has a field for it. For Claude-issued ones, they can enter it in Claude's managed authorization setup for your connector. Claude doesn't check the value, so use it only to choose the workspace, and still run the issuer check in [Validate the identity assertion](#validate-the-identity-assertion) against that workspace's registered issuer.

### Validate the identity assertion

Run these checks, in this order, on every token request. When a check fails, reject the request with `invalid_grant`, as the [JWT bearer token processing rules (RFC 7523 section 3)](https://datatracker.ietf.org/doc/html/rfc7523#section-3) require.

Before the first check, find the one workspace the assertion is for. If you identify workspaces by your own tenant ID and the assertion carries [`aud_tenant`](#identity-assertion-claims), take the workspace that `aud_tenant` names. Otherwise, take the workspace that registered `iss`, and reject the assertion if no workspace or more than one did.

1. **Issuer**: `iss` equals, as an exact string, the trusted issuer registered for that workspace. A prefix or host match admits other customers' users. Check this before you fetch any keys.
2. **Keys**: fetch `<iss>/.well-known/openid-configuration`, confirm that the document's `issuer` equals `iss`, and fetch the key set from the document's `jwks_uri`. Use only keys from that key set, and ignore any key or key URL carried in the assertion's header. Don't pin a single key. Cache keys for as long as the response headers allow, and fetch them again when an assertion names a `kid` you haven't seen.
3. **Signature**: the signature verifies against a key from that key set. Accept ES256 and RS256, and reject every other `alg`, including `none` and HMAC algorithms such as HS256. Claude-issued assertions use ES256.
4. **Type**: the `typ` header is `oauth-id-jag+jwt`. Check `typ` yourself if your JWT library doesn't check it.
5. **Audience**: `aud` is your authorization server's own `issuer` value, exactly as your metadata publishes it. The claim can arrive as a string or as a JSON array with one element, so use your library's audience option rather than comparing the raw claim text.
6. **Client**: the `client_id` claim equals the `client_id` of this request.
7. **Subject**: a `sub` claim is present. Whether you find the user by `sub` or by `email` [depends on the issuer](#identity-assertion-claims).
8. **Time**: `exp` hasn't passed, `iat` isn't in the future, and `nbf`, when present, has passed. Allow at most 60 seconds of clock skew.
9. **Replay**: a `jti` claim is present. Accept each `jti` from an issuer once, and remember it at least until the assertion's `exp` plus your clock-skew allowance. Treat `jti` as an opaque string. If you can't check whether a `jti` was already used, reject the request.

Issue the access token for that workspace only, even when the same user belongs to other workspaces in your product.

### Claude-issued assertions

These points apply to Claude-issued assertions:

* **What the assertion says**: the user is a current member of the customer's Claude organization, and `email` is the address of their Claude account, in lowercase. The assertion doesn't say that the user signed in through the customer's identity provider or used multi-factor authentication, and it carries no group claims.
* **Discovery document**: a Claude issuer's discovery document, at `<iss>/.well-known/openid-configuration`, holds `issuer` and `jwks_uri` and has no `authorization_endpoint` or `token_endpoint`. Read `issuer` and `jwks_uri` from it yourself rather than passing it to a validator that expects a full OpenID Connect provider configuration.
* **Lifetime**: each assertion expires within a minute, and each sign-in and each renewal gets a new assertion with a new `jti`.
* **User lookup**: find the user by `email` among the members of the workspace the assertion resolved to. Compare the whole address, ignore letter case, and keep dots and plus tags as they are. If no member of the workspace has the address, reject the request, or create the user only when the address is on an email domain the workspace has verified with your service.

> [!WARNING]
>
> Sign a user in by `email` only when your service has verified that user's email address, or when the address is on an email domain the workspace has verified. An issuer URL isn't a secret, and whoever runs an identity provider can put any address in `email`, so someone can register another customer's issuer URL, or an identity provider of their own, in a workspace they control.

### Access token lifetime

Issue access tokens with whatever lifetime your security policy calls for. A short lifetime, such as one hour, doesn't make users sign in again each time a token expires. Claude gets a new identity assertion without any user interaction and exchanges it at your token endpoint for a new access token.

When a user is removed from the customer's Claude organization, Claude stops signing Claude-issued assertions for them. Access tokens you already issued stay valid, so your access token lifetime bounds how long a removed user keeps access.

## Test your implementation

Test end to end from a Claude organization on a Team or Enterprise plan, signed in as an Owner or Primary Owner. You can use your company's own organization or [a Team organization that you create for testing](https://support.claude.com/en/articles/9267247-get-started-with-the-team-plan). While you develop, Okta's [Cross App Access sandbox](https://xaa.dev) exercises your authorization server and MCP server without a Claude organization. Point the sandbox at your authorization server to check that your server accepts an identity assertion over the JWT bearer grant, mints a scoped access token, and serves its metadata for discovery.

### Choose a test organization

Pick the organization by the kind of assertion you're testing:

* **Claude-issued**: test this first, because the organization needs no single sign-on (SSO), verified domain, or identity provider, so a Team organization that you create for testing qualifies as it is. Don't use an organization that signs in to Claude through Okta, because **Claude-issued** isn't available in one that does.
* **Identity provider-issued**: use an organization that signs in to Claude through Okta. If your company's organization does, test there. Otherwise, you need an Okta org, such as an integrator org from Okta's [Integrator Free Plan](https://developer.okta.com/signup/), and a Team organization that you create. Follow [Set up single sign-on](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso) to verify a domain for the Team organization and connect SSO, choosing Okta as the provider. In the Okta org, give yourself and each test user an address on that domain. Sign in to Claude through SSO before you run the connection test.

To test both kinds of assertion in one organization, test **Claude-issued** first, then connect Okta single sign-on and switch the connector to **IdP-managed**. A connector set up with **Claude-issued** keeps working after you connect Okta, but once you switch it, the setup doesn't offer **Claude-issued** again unless you remove single sign-on from the organization. To test in either order, use two organizations.

### Add your connector and run the connection test

**1. Add your MCP server as a custom connector**

Add your MCP server as a custom connector for the test organization, as [Add the connector for the organization](https://claude.com/docs/connectors/custom/add-unlisted.md#add-the-connector-for-the-organization) describes.

If your MCP server is already in the [Connectors Directory](https://claude.com/docs/connectors/directory.md), add the custom connector at a different URL from your listing's, such as a staging deployment of the same server. A connector at your listing's URL, whether you add it from the directory or by URL, shows **Managed authorization** once your listing is marked as supporting Enterprise Managed Auth. The **Authentication** section is on the connector's **Configuration** tab.

To test at your listing's production URL before your listing is marked, email `mcp-review@anthropic.com` and ask to have Enterprise Managed Auth enabled for your connector in your test organization. Include your listing's name and the **Organization ID**, which you copy from [**Organization settings > Organization and access**](https://claude.ai/admin-settings/organization).

**2. Open the managed authorization setup**

Open the connector you added. In its **Authentication** section, which is separate from the **Authentication** setting you chose while adding the connector, click **Set up** on the **Managed authorization** row. Under **Identity source**, choose **IdP-managed** for identity provider-issued assertions or **Claude-issued** for Claude-issued ones.

For **IdP-managed**, follow the first step under **Setup guide** to register Claude and your connector in your Okta org. For the steps in the Okta Admin Console, see Okta's [Cross App Access guide for AI agents](https://developer.okta.com/docs/guides/xaa-agent-to-app/main/).

**3. Register the issuer in your test workspace**

Register the issuer URL as the trusted issuer of a test workspace in your product. For **Claude-issued**, copy the **Issuer URL** that the setup shows into your test workspace, and if you identify workspaces by your own tenant ID, enter the test workspace's ID in **Tenant ID (optional)**.

**4. Run the connection test**

Click **Run test** under **Connection status**. The test shows which step failed, what Claude sent and what came back, and, for a Claude-issued assertion that was signed, its decoded claims.

### Cases to check before launch

Check each of these cases before you launch:

* An assertion from the workspace's registered issuer signs the right user in
* An assertion whose `iss` no workspace has registered is refused
* An assertion whose `aud_tenant` names a workspace that registered a different issuer is refused
* An assertion whose `iss` is registered for more than one workspace is refused, unless you identify workspaces by your own tenant ID and the assertion's `aud_tenant` names one of those workspaces
* The same assertion presented a second time is refused
* An assertion whose `aud` isn't your authorization server's issuer is refused
* For a Claude-issued assertion, the user is found by verified email within the workspace the assertion resolved to, not by `sub`
* A Claude-issued assertion for an address your service hasn't verified, on a domain the workspace hasn't verified, is refused

## Support customer administrators

A customer's administrator turns on Enterprise Managed Auth for their organization. For a connector added from the directory, an Owner or Primary Owner clicks **Set up auto-connect** on its row in [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors), which opens the managed authorization setup. Claude's guide for administrators is [Auto-connect your organization's apps to Claude](https://support.claude.com/en/articles/15537633-auto-connect-your-organization-s-apps-to-claude).

### Admin settings in your product

In your product's admin settings, give each customer's administrator a control that turns Enterprise Managed Auth on or off for their workspace and a field for the trusted issuer URL. Accept only an `https` URL in the field, and let only the workspace's administrators set it. The administrator copies the URL from their identity provider or, for Claude-issued assertions, from the **Issuer URL** box in Claude's managed authorization setup for your connector. When the administrator saves, register the URL as that workspace's trusted issuer.

If you identify workspaces by your own tenant ID, show that ID in the same settings. The administrator enters it in the **Tenant ID (optional)** field in Claude's managed authorization setup for your connector, and it then arrives in each Claude-issued assertion as [`aud_tenant`](#identity-assertion-claims).

### Provide setup documentation

Publish documentation that walks an enterprise administrator through enabling Enterprise Managed Auth for your product, including how to enter a Claude issuer URL as the trusted issuer, and add its URL to [your directory listing](https://claude.com/docs/connectors/building/managing-your-listing.md). Claude shows the link in the Claude admin console when an administrator sets up Enterprise Managed Auth for your connector.

### Okta Integration Network apps

If your product has an app in the Okta Integration Network, work with Okta to enable Cross App Access (XAA) for that app. Until that app supports Cross App Access, customers who use Okta need to create a custom app in Okta for your product before they can set up Enterprise Managed Auth.

## Launch checklist

Confirm each of the following before you ask Anthropic to mark your directory listing as supporting Enterprise Managed Auth:

* Sign-in works end to end for each kind of assertion your server accepts
* Every case in [Cases to check before launch](#cases-to-check-before-launch) passes, including the refused ones
* Your admin settings let a customer's administrator set the trusted issuer for their workspace
* Your setup documentation for administrators is published, and its URL is on [your directory listing](https://claude.com/docs/connectors/building/managing-your-listing.md)

Then email `mcp-review@anthropic.com` with your listing's name and the kinds of assertion your server accepts. If your connector isn't listed yet, [submit it](https://claude.com/docs/connectors/building/submission.md) before you email. Anthropic reviews the request and sets which kinds the listing is marked as supporting.

## Related resources

* [Authentication for connectors](https://claude.com/docs/connectors/building/authentication.md): baseline OAuth requirements your server must already meet
* [Lazy authentication](https://claude.com/docs/connectors/building/lazy-authentication.md): ask users to sign in only when Claude reaches a tool that needs their account
* [Test your connector](https://claude.com/docs/connectors/building/testing.md): verify your connector works end to end in Claude
* [Troubleshoot your connector](https://claude.com/docs/connectors/building/troubleshooting.md): diagnose common authentication and connection issues

> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Managed Auth for connectors

> Accept identity assertions from enterprise SSO so users connect to your MCP server without a separate OAuth consent step.

<Note>
  Enterprise Managed Auth is available on Claude Team and Enterprise plans. MCP server developers and identity provider vendors can [register interest](https://docs.google.com/forms/d/e/1FAIpQLSf1goHGNDVFK7rncYuh6wnRpWSy7eGOcgL1i8uw3oyKFO9UUA/viewform) in supporting this flow.
</Note>

Enterprise Managed Auth (EMA) lets a user connect to your MCP server silently, using the single sign-on session they already have with their organization. Instead of showing each user an OAuth consent screen, Claude presents your authorization server with an identity assertion: a signed JSON Web Token (JWT), issued by the customer's identity provider, that vouches for the user's identity.

Your authorization server validates the assertion and returns an access token in a single back-channel request. There is no browser redirect and no per-connector consent page. From the user's point of view, the connector is available as soon as their administrator enables it.

This page is for connector developers who need their authorization server to accept Enterprise Managed Auth. The customer's administrator handles identity provider setup and Claude admin console configuration, so those aren't covered here. The page walks through [how the exchange works](#understand-how-enterprise-managed-auth-works), the [prerequisites](#prerequisites), [what your authorization server must support](#authorization-server-requirements), [how to test](#test-your-implementation), and [what to give customer administrators](#support-customer-administrators).

## Understand how Enterprise Managed Auth works

When a user whose organization has Enterprise Managed Auth configured invokes your connector, Claude obtains a signed identity assertion for that user and exchanges it directly at your token endpoint for an access token. The user never sees a browser redirect or a consent screen, and your MCP server receives the same kind of bearer token it would after the interactive OAuth flow. The diagram shows the exchange between Claude, your authorization server, and your MCP server.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/-njlLvrWxFCRdJVz/images/connectors/enterprise-managed-auth-exchange.svg?fit=max&auto=format&n=-njlLvrWxFCRdJVz&q=85&s=2bdd0b680bda337b37632516b8dc5e84" alt="Sequence diagram with three participants: Claude, your authorization server, and your MCP server. The user is already signed in to Claude through their organization's single sign-on. 1, Claude sends POST /token to your authorization server with the jwt-bearer grant and the signed JWT assertion. 2, your authorization server fetches the issuer's JWKS and verifies the signature. 3, it validates iss, aud, exp, sub, and client_id. 4, it returns an access_token to Claude. 5, Claude sends the tool call to your MCP server with the Bearer access_token. 6, your MCP server returns the tool result to Claude. Requests are solid arrows and responses are dashed arrows." width="1000" height="560" data-path="images/connectors/enterprise-managed-auth-exchange.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/-njlLvrWxFCRdJVz/images/connectors/enterprise-managed-auth-exchange-dark.svg?fit=max&auto=format&n=-njlLvrWxFCRdJVz&q=85&s=5b8c6c81ef448cfb08deb05f0d02b712" alt="Sequence diagram with three participants: Claude, your authorization server, and your MCP server. The user is already signed in to Claude through their organization's single sign-on. 1, Claude sends POST /token to your authorization server with the jwt-bearer grant and the signed JWT assertion. 2, your authorization server fetches the issuer's JWKS and verifies the signature. 3, it validates iss, aud, exp, sub, and client_id. 4, it returns an access_token to Claude. 5, Claude sends the tool call to your MCP server with the Bearer access_token. 6, your MCP server returns the tool result to Claude. Requests are solid arrows and responses are dashed arrows." width="1000" height="560" data-path="images/connectors/enterprise-managed-auth-exchange-dark.svg" />

Two parties are involved in this exchange: the customer's identity provider signs the assertion, and your authorization server verifies it and issues the access token. Both roles are often served by commercial identity platforms, so the distinction here is about which tenant plays which role rather than about product type. The identity provider publishes its signing keys as a JSON Web Key Set, and your authorization server fetches that key set to verify each assertion.

The Enterprise Managed Auth flow is defined by the [MCP enterprise managed authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) and is built on the standard [JWT bearer authorization grant (RFC 7523)](https://datatracker.ietf.org/doc/html/rfc7523). The assertion profile follows the [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/).

### Enterprise Managed Auth with lazy authentication

Enterprise Managed Auth also works with [lazy authentication](/docs/connectors/building/lazy-authentication). When your server returns `401 Unauthorized` for a protected tool call, Claude normally shows the inline **Connect** card and runs the interactive OAuth flow. If the user's organization has Enterprise Managed Auth configured for your connector, Claude runs the silent JWT bearer exchange instead and retries the tool call without showing a prompt.

Your MCP server returns the same `401` with a `WWW-Authenticate` header as described in the [lazy authentication guide](/docs/connectors/building/lazy-authentication#answer-a-protected-call-with-401-before-the-mcp-sdk-runs). Your authorization server must still meet the [authorization server requirements](#authorization-server-requirements).

Enterprise Managed Auth doesn't apply to authless servers. A fully authless server never returns `401`, so there is no point at which Claude can exchange an assertion.

## Prerequisites

Before adding Enterprise Managed Auth, make sure the following are already in place:

* Your MCP server implements [MCP authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization), including Protected Resource Metadata (PRM) discovery, and follows the [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices). See the [authentication guide](/docs/connectors/building/authentication) for Claude-specific requirements
* Your authorization server registers Claude using either [Anthropic-held client credentials](/docs/connectors/building/authentication#anthropic-held-client-credentials) or a [Client ID Metadata Document](/docs/connectors/building/authentication#dcr-and-cimd-details)

<Warning>
  Dynamic Client Registration (DCR) isn't supported with Enterprise Managed Auth. The identity provider stamps a fixed `client_id` into every assertion it issues, so your authorization server must already recognize that client before the first assertion arrives. A client created on the fly through DCR can't satisfy this requirement because its identifier never matches the value in the assertion.
</Warning>

## Authorization server requirements

Your authorization server must support the JWT bearer authorization grant ([RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523)), which lets an authorization server exchange a signed JWT for an access token, and must trust each customer's identity provider as an issuer. This section is for the authorization server operator.

If your MCP server relies on a hosted identity platform, there is typically no code to write. Confirm that the platform supports the JWT bearer authorization grant and enable it for your tenant. Support varies by product, and some commercial authorization servers and identity platforms don't support it yet, so confirm that yours does and that the customer's identity provider can be registered as a trusted issuer. If you run your own authorization server, the steps in this section describe what it needs to support.

<Steps>
  <Step title="Ensure the JWT bearer grant is supported">
    Your authorization server must accept `urn:ietf:params:oauth:grant-type:jwt-bearer` at its token endpoint and advertise it in the `grant_types_supported` array of its [authorization server metadata (RFC 8414)](https://datatracker.ietf.org/doc/html/rfc8414). In this example metadata, the highlighted entry is the one Claude looks for:

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

    Claude reads this metadata to discover whether your server supports Enterprise Managed Auth. The grant type must be listed here for Claude to offer the feature to the customer, even if your token endpoint would already accept it silently.
  </Step>

  <Step title="Register the trusted issuer">
    For each customer, your authorization server needs to trust that customer's identity provider as a JWT issuer. Your authorization server fetches the identity provider's JSON Web Key Set and uses it to verify the signature on every incoming assertion.

    Your authorization server is responsible for maintaining an explicit allowlist of trusted issuer URLs per tenant rather than accepting any well-formed JWT. It must reject an assertion whose `iss` isn't on the tenant's allowlist with `invalid_grant`, even if the signature is valid.

    <Warning>
      Never accept an identity assertion without full validation. Your authorization server must verify the signature, issuer, audience, expiry, and subject on every request. Use the JWT validation built into your authorization server product. If you need to inspect assertions in your own code, use the validation library or token introspection endpoint provided by your authorization server vendor rather than writing custom verification logic.
    </Warning>
  </Step>

  <Step title="Understand the token request">
    Claude sends a form-encoded `POST` to your authorization server's token endpoint. The highlighted parameters are the JWT bearer grant type, the signed assertion, and the `client_id` your server must already recognize:

    ```http {5-7} theme={null}
    POST /token HTTP/1.1
    Host: auth.example.com
    Content-Type: application/x-www-form-urlencoded

    grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
    &assertion=eyJhbGciOi...
    &client_id=your-registered-client-id
    &scope=openid profile
    &resource=https://mcp.example.com
    ```

    The `assertion` parameter carries the signed JWT. The `client_id` is the value Claude is registered under at your authorization server. Claude also includes the `resource` parameter ([Resource Indicators, RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)) set to your MCP server URL whenever the customer's identity provider supports forwarding it. Some identity provider configurations cannot pass a resource indicator through, so your authorization server should accept the request whether or not `resource` is present and use it for audience binding when it is.

    Your authorization server validates the assertion according to the [JWT bearer token processing rules (RFC 7523 section 3)](https://datatracker.ietf.org/doc/html/rfc7523#section-3) and returns a standard OAuth token response. Claude then presents the returned access token as a `Bearer` credential on calls to your MCP server, exactly as it does after the interactive flow.

    <Note>
      Your authorization server sets the access token lifetime, and the customer's identity provider sets the assertion lifetime. Anthropic doesn't control either value.
    </Note>
  </Step>
</Steps>

### Access token lifetime

Issue access tokens with whatever lifetime your security policy calls for. A short lifetime, such as one hour, doesn't force users to repeat single sign-on each time a token expires.

When a user signs in to Claude through their organization's SSO, Claude obtains a long-lived refresh token from the identity provider. Claude uses that refresh token to request a fresh identity assertion from the identity provider whenever it needs one, without any user interaction. Claude then exchanges the new assertion at your token endpoint for a new access token. From the user's point of view, the connection stays active for as long as the identity provider's refresh token remains valid.

The customer's identity provider issues the refresh token. Treat it as long-lived.

## Test your implementation

End-to-end testing requires a Claude organization with Enterprise Managed Auth enabled and an identity provider tenant configured to issue assertions for your authorization server's audience.

If your identity provider is Okta, refer to Okta's [Cross App Access participation guide](https://support.okta.com/help/s/article/claude-enterprise-managed-auth-with-okta-cross-app-access-xaa-beta-participation-guide?language=en_US) and configure your organization so you can test your MCP server's Cross App Access (XAA) implementation.

### Test with the cross-app access playground

[Okta's cross-app access playground](https://xaa.dev) lets you exercise the flow without a Claude organization. The playground is useful while you develop, and when your organization's single sign-on isn't on a supported identity provider. On the playground you can do the following:

* Walk the full flow end to end against a sandbox IdP, with every token shown decoded
* Point it at your own MCP server or REST API to check resource metadata discovery, the `WWW-Authenticate` hint on `401` responses, and token validation
* Point it at your own authorization server to check that it accepts an identity assertion over the JWT bearer grant, mints a scoped access token, and serves its metadata for discovery
* Bring your own OIDC or SAML identity provider in place of the sandbox one
* Re-run a single failed step and inspect service configurations, discovery documents, and a live event log

## Support customer administrators

A customer's administrator turns on Enterprise Managed Auth for their organization, so your product needs an admin control for it, setup documentation they can follow, and, for Okta customers, an app that supports Cross App Access.

### Admin settings in your product

In your product's admin settings, give each customer's administrator a control that turns Enterprise Managed Auth on or off for their organization and a field for their identity provider's issuer URL. When the administrator saves, add that URL to the organization's allowlist of trusted issuers, as described in [Authorization server requirements](#authorization-server-requirements).

### Provide setup documentation

You can publish documentation that walks an enterprise administrator through enabling Enterprise Managed Auth for your product and add its URL to [your directory listing](/docs/connectors/building/managing-your-listing). Claude shows the link in the Claude admin console when an administrator sets up Enterprise Managed Auth for your connector.

### Okta Integration Network apps

If your product has an app in the Okta Integration Network, work with Okta to enable Cross App Access (XAA) for that app. Until that app supports Cross App Access, customers who use Okta need to create a custom app in Okta for your product before they can set up Enterprise Managed Auth.

## Related resources

* [Authentication for connectors](/docs/connectors/building/authentication): baseline OAuth requirements your server must already meet
* [Lazy authentication](/docs/connectors/building/lazy-authentication): ask users to sign in only when Claude reaches a tool that needs their account
* [Test your connector](/docs/connectors/building/testing): verify your connector works end to end in Claude
* [Troubleshoot your connector](/docs/connectors/building/troubleshooting): diagnose common authentication and connection issues

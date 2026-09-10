> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect an authorization server

> Let Claude exchange a short-lived identity token for an access token from an OAuth 2.0 authorization server you run, then call your APIs with it. Covers what your token endpoint receives and must check, what it returns, and how to register it in the console.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Authorization servers are connected at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation and use the **Authorization servers** section. Connecting a server needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

With an authorization server connection, Claude presents a short-lived identity token to an OAuth 2.0 authorization server you run, receives one of your access tokens in return, and calls your APIs with it. No long-lived credential for your systems is stored in Claude, and [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) holds each access token only until it expires. The identity token names your organization and the [agent](/docs/claude-tag/concepts/agent-identity) making the request (Claude's identity in one Slack channel), and your server decides whether to issue a token for it.

Choose this when you run an authorization server that issues tokens for your APIs. If your own service will verify the identity token on every request instead, [connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway). If a vendor's API gave you a private key to sign assertions with (Salesforce, for example), use the [OAuth 2.0 JWT bearer](/docs/claude-tag/admins/connections/custom#oauth-2-0-jwt-bearer) credential type instead; the console labels this page's connection **Authorization server**.

Two terms recur on this page. The **subject check** is what your server does to every identity token, confirming it belongs to your organization. The **connection check** is the probe the console runs when a gateway is connected; it doesn't run for token endpoints.

## Before you begin

* You're an organization Owner, or an admin with full Claude Tag management permission.
* Your authorization server's token endpoint is reachable from the internet over HTTPS at an address with a domain name, such as `https://auth.example.com/oauth2/token`. The console accepts an address that:
  * is at most 256 characters
  * may have a path, with no spaces or special characters in it
  * has no port number (the console drops `:443`), query, fragment, or sign-in details
  * isn't an IP address, a private-network name, an Anthropic-owned host, or a cloud token-exchange host
* The token endpoint is on a different host from the APIs Claude will call with the returned token, for example `auth.example.com` and `api.example.com`.
* Your server can reach `https://identity.anthropic.com` to fetch Anthropic's signing keys.
* An organization can register up to 5 [gateways](/docs/claude-tag/admins/federated-access/connect-a-gateway), and a token endpoint counts as one.

## Copy the values from the console

In **Authorization servers**, click **Connect an authorization server**, enter your token endpoint in the **Token endpoint** field, enter your authorization server's issuer identifier in the **Issuer URL** field (or leave it empty if your server requires the token endpoint URL as the audience), and copy the **Issuer**, **JWKS URL**, **Audience**, and **Subject prefix** rows from the **Set your authorization server to accept these values** card. Then click **Cancel**; you register the endpoint after configuring the server.

| Value          | What to configure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issuer         | `https://identity.anthropic.com/agents`, matched exactly. The OpenID Connect (OIDC) discovery document is at `https://identity.anthropic.com/agents/.well-known/openid-configuration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| JWKS URL       | The JSON Web Key Set (JWKS) named by `jwks_uri` in the discovery document, `https://identity.anthropic.com/agents/jwks.json`. Accept ES256 only. Select the key by `kid`, and refetch the JWKS on an unknown `kid` before rejecting the token.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Audience       | Your authorization server's issuer identifier, as you enter it in the **Issuer URL** field when you connect the server, for example `https://auth.example.com`. It must be an HTTPS URL on the same host as the token endpoint. If your server requires the token endpoint URL as the audience instead, leave **Issuer URL** empty and the audience is the token endpoint address as the console stores it (the host lowercased, a bare trailing slash dropped, the rest kept as entered). Either way, copy the **Audience** row into your verifier rather than typing it. The `aud` claim is a JSON array with one element. Accept only this exact value, not any address on your host. |
| Subject prefix | `wimse://identity.anthropic.com/org/<your organization ID>/agent/`. Every token's `sub` claim starts with this prefix and ends with one agent's ID; see the [subject](/docs/claude-tag/admins/federated-access/token-reference#subject) format. Agent IDs aren't shown in the console; your server learns them from the tokens it receives, and they change, for example when a Slack channel is deleted and recreated.                                                                                                                                                                                                                                                                       |
| Tenant         | Your organization ID, the value between `/org/` and `/agent/` in the **Subject prefix**, carried in every token as the `tenant` claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Expiry         | Tokens expire 10 minutes after they're issued. Check `exp`, allowing up to 60 seconds of clock skew.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Configure the authorization server

Claude sends a standard JWT bearer grant ([RFC 7523](https://www.rfc-editor.org/rfc/rfc7523)) to the token endpoint as an HTTPS `POST` with `Content-Type: application/x-www-form-urlencoded` and `Accept: application/json`. The form body contains these fields:

```text wrap theme={null}
grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=<identity token>[&resource=<resource>][&scope=<scopes>]
```

The `resource` ([RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)) and `scope` fields are present only if you set them when connecting the server. No `client_id` or `client_secret` is sent. Register one client for Anthropic's issuer that accepts this grant without client authentication; the subject check is what keeps other organizations out. The request doesn't follow redirects, and the exchange must complete within about 10 seconds.

Your server must:

* Verify the token with a standard JWT or OIDC library configured with the issuer, JWKS URL, audience, and expiry from [Copy the values from the console](#copy-the-values-from-the-console).
* Check the subject. Where your use case allows, accept only the full subjects of your own agents, and update that list when a Slack channel is deleted and recreated. At minimum, reject every token whose `sub` doesn't start with your **Subject prefix**, or equivalently pin `iss` and reject every token whose `tenant` isn't your organization ID. This check is required because every organization's tokens come from the same issuer; see [Authorize on the subject](/docs/claude-tag/admins/federated-access/token-reference#authorize-on-the-subject). The console's connection check doesn't run for token endpoints, so nothing tests this check for you.
* Decide what the agent may do, for example from the agent ID at the end of `sub`, and issue an access token for it. Tokens may carry additional opaque claims; ignore claims you don't recognize.
* Return `200` with a JSON body: `access_token`, `token_type` (`Bearer`, compared without regard to case, and may be omitted), and `expires_in` in seconds.

Each grant carries a fresh token with a new `jti`, so your server may reject a repeated `jti`.

Claude caches the access token when `expires_in` is between 5 minutes and 1 day, inclusive, and reuses it until about 5 minutes before it expires (for tokens shorter than 10 minutes, until half their lifetime has passed). The cache is per channel, so one channel's token is never used for another, and your server may still see more than one grant per channel within a token's lifetime. An `expires_in` outside that range, or none, makes Claude exchange a new token on every request to your APIs.

To refuse a grant, return a standard OAuth 2.0 error response, such as `400` with `{"error": "invalid_grant"}`. Any non-`2xx` status is a refusal. Claude reads only the `error` code and never shows `error_description` to anyone, so log the reason on your side. After a refusal, or any other failed exchange, the agent's request fails with an error, and Claude doesn't try the exchange again for a few seconds; your token endpoint's `Retry-After` header on a `429` or `503` response extends that wait. If one of your APIs answers `401`, or `403` with a `WWW-Authenticate: Bearer` challenge whose error is `invalid_token`, Claude drops the cached token (unless it was just issued) and exchanges a new one on the next request. A plain `403` doesn't trigger this.

## Register the endpoint and connect the server

<Steps>
  <Step title="Open the Connect an authorization server dialog">
    In **Authorization servers**, click **Connect an authorization server**.
  </Step>

  <Step title="Enter the token endpoint">
    In the **Token endpoint** field, enter the full address starting with `https://`, for example `https://auth.example.com/oauth2/token`. In the **Issuer URL** field, enter your authorization server's issuer identifier, the `iss` value it uses, for example `https://auth.example.com`. That value is the token's audience, and it must be an HTTPS URL on the same host as the token endpoint. Leave the field empty only if your server requires the token endpoint URL as the audience. Then the **Token endpoint** address is the audience. The **Audience** row of the card shows which one will be sent.
  </Step>

  <Step title="Confirm the subject check and register">
    Select the checkbox labeled **This authorization server checks that each token's subject belongs to your organization**. The **Register server** button stays disabled until you do. The checkbox is your confirmation that the server makes the subject check described under [Configure the authorization server](#configure-the-authorization-server), and a server that doesn't must not be connected. Then click **Register server**. The dialog notes that the automatic connection check doesn't run for token endpoints. The endpoint is registered as a gateway with the check marked **Skipped**, and the dialog moves to the second step.

    If you close the dialog at that point, the endpoint stays registered and counts toward the limit. To continue later, click **Connect an authorization server** again, enter the same address, and select the checkbox again, which returns you to the second step. Don't use **Add to bundle** on the endpoint's row in the **Gateways** table; that would connect the address as a gateway, after which the server can't be connected.
  </Step>

  <Step title="Choose the APIs and the Access bundle">
    Optionally enter a **Resource**, the API the returned token should be scoped to as an absolute URI (for example `https://api.example.com`), and a **Scope**, space-separated scopes to request. In **Allowed API hosts**, add the hosts Claude may call with the returned token, for example `api.example.com`. A wildcard as the leftmost label matches any subdomain; an entry or wildcard that covers the token endpoint's host is rejected. Then choose a bundle from the **Access bundle** list (or click **New bundle**, enter a **Bundle name**, and click **Create bundle**) and click **Connect server**.

    This creates a [connection](/docs/claude-tag/admins/add-connections) in that bundle, labeled **Authorization server** on its **Credentials** tab, with the API hosts under **Allowed hosts**. Agent Proxy attaches the access token as an `Authorization: Bearer` header to every request Claude makes to those hosts. A token endpoint can be connected once in your organization, in one bundle; to use it in several scopes (workspaces or channels), attach that bundle to each.
  </Step>
</Steps>

The **Authorization servers** table lists each server by its **Token endpoint**, with its **Access bundle**, its **Allowed hosts**, when it was **Added**, and a **Remove** action. The endpoint also appears in the **Gateways** table with its check marked **Skipped** and a note that a connected authorization server uses it.

## Let agents use the APIs

Claude uses the connection in channels whose scope has the bundle attached. [Attach the bundle to a workspace or channel](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) if it isn't attached already.

Claude also needs to know what the APIs are for. Add a line like this to the scope's [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions):

```text wrap theme={null}
The internal orders API is at https://api.example.com; see GET /openapi.json for what it offers. Authentication is already set up.
```

The exchange happens in Agent Proxy, outside Claude's sandbox, so neither the identity token nor your access token is visible to Claude, and Claude can't perform the exchange itself.

New threads pick up the connection on their own. In a thread already running, ask Claude to use the API and name its host. If Claude still can't, send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) at the channel's top level (not inside a thread) to start a fresh session with your organization's current configuration.

## Verify the connection

In a channel whose workspace or channel has the bundle attached, start a new thread and ask Claude to make a small read:

```text wrap theme={null}
@Claude call GET /openapi.json on https://api.example.com and tell me what the API offers.
```

Then check your authorization server's logs for a JWT bearer grant whose token has your **Subject prefix**, and your API's logs for a request carrying the access token it issued. If the grant was refused, your server's own error is the reason; Claude sees only that the request failed. See [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting) for the errors Claude shows.

## Remove the server

In the **Authorization servers** table, click **Remove** in the server's row, then **Remove server** in the confirmation. Claude stops using the connection within about a minute, in existing threads as well as new ones, and the connection is removed from its bundle. An access token your server already issued stays valid with your server until it expires, and Agent Proxy discards it with the connection. The endpoint stays registered as a gateway, so to free its place in the limit, also click **Remove** in its row of the **Gateways** table. To change the address, do both removals, then connect the server again with the new address.

## Common errors

Five messages come up while connecting:

* **"The issuer URL must be an https URL on the same host as the token endpoint. Leave it empty to use the token endpoint as the audience."**: the **Issuer URL** value is not an HTTPS URL on the token endpoint's host. Enter the issuer identifier your server uses there, or clear the field.
* **"This token endpoint is already connected in the bundle"**: the server already has its one connection. [Attach that bundle to the scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) instead.
* **"This organization has reached its limit of 5 registered gateways, which includes token endpoints"**: remove an unused row from the **Gateways** table first.
* **"The allowed hosts can't include the token endpoint's host"**: an **Allowed API hosts** entry, or a wildcard in it, covers the token endpoint's host. Put the token endpoint on a different host from the APIs.
* **"That address is already connected as a gateway. Enter your authorization server's own addresses, or remove the gateway first."**: the token endpoint, or the **Issuer URL** value, is the address of a gateway connected in one of your Access bundles. Enter the server's own addresses, or delete that gateway's connection from its bundle first.

For other dialog messages, see [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the Access bundle and connection model
* [Attach a bundle to a scope](/docs/claude-tag/admins/attach-to-scope): where a connection applies
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim in the token, lifetimes, and key rotation
* [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway): the alternative where your own service verifies the token on every request
* [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting): console and runtime errors for every connection type

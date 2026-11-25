---
title: OAuth endpoints and parameters
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters
description: The endpoints, parameters, scopes, OAuth tokens, lifetimes, and errors of Claude Platform OAuth, in the order a request uses them.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

In request order, this page lists the values that [Claude Platform OAuth](https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview) requests use and then the [terms used on these pages](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#terms).

## Endpoints

| Endpoint | URL |
| ----- | ----- |
| Authorization endpoint (the approval page) | `https://auth.claude.com/oauth/authorize` |
| Pushed authorization request (PAR) endpoint | `https://auth.claude.com/v1/oauth/par` |
| Token endpoint | `https://auth.claude.com/v1/oauth/token` |
| Revocation endpoint | `https://auth.claude.com/v1/oauth/revoke` |
| Claude API ([user profiles](https://platform.claude.com/docs/en/manage-claude/user-profiles) and requests that bill a customer) | `https://api.anthropic.com` |

## Client authentication

`auth.claude.com` authenticates your app with a variation of the `private_key_jwt` method ([RFC 7523](https://www.rfc-editor.org/rfc/rfc7523)). Your identity provider, not your app, issues and signs the client assertion. Its `iss` is your identity provider’s issuer. Its `aud` is your app’s configured audience, not your client ID or the full URL of the endpoint. `auth.claude.com` checks it against the keys registered for that issuer and your app’s settings.

Send these parameters in the body of every `POST` request to the PAR, token, and revocation endpoints.

| Parameter | Value |
| ----- | ----- |
| `client_id` | Your OAuth app’s client ID, required even with a client assertion |
| `client_assertion_type` | `urn:ietf:params:oauth:client-assertion-type:jwt-bearer` |
| `client_assertion` | A JWT from your identity provider with the claims in [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-assertion-claims) |

These rules apply to each request:

* **Body:** It can be JSON or form-encoded (`application/x-www-form-urlencoded`). Set the `Content-Type` header to match.
* **Query string:** `auth.claude.com` rejects credentials in a URL query string.
* **HTTP Basic:** Don’t send an HTTP Basic `Authorization` header. `auth.claude.com` doesn’t read credentials from it, and the PAR endpoint can refuse a request that has one.

### Client assertion claims

A client assertion must contain these claims. The values to match are in your app’s [client authentication settings](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication).

| Claim | Requirement |
| ----- | ----- |
| `iss` | Your identity provider’s issuer URL, exactly as registered through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) |
| `sub` | Your back end’s subject. If your app’s settings have a subject pattern, the subject must match it. |
| `aud` | Exactly one audience: the value in your app’s settings, not the full URL of the endpoint you call |
| `iat` | The time your identity provider issued the JWT |
| `exp` | The expiry time, no more than your issuer’s [maximum lifetime](https://platform.claude.com/docs/en/manage-claude/wif-reference#jwt-verification) after `iat` (1 hour by default) |

A client assertion’s header and signature must also meet these rules:

* **Algorithm:** `RS256`, `RS384`, `RS512`, `ES256`, `ES384`, `ES512`, `PS256`, `PS384`, or `PS512`, the same list as in the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference#jwt-verification). `auth.claude.com` rejects any other, including the HMAC algorithms (`HS256`, `HS384`, `HS512`) and `none`.
* **Key ID:** The header’s `kid` must name a key in your JWKS. If that key declares an `alg`, it must be the algorithm that signed the assertion.
* **Your JWKS:** Every signing key must have a `kid`. A key without one makes the whole set unusable.

An assertion’s payload looks like this. Its `aud` is your app’s own **Expected audience**, from the app’s **Client authentication** tab:

```json
{
  "iss": "https://idp.example.com",
  "sub": "workload:prod:claude-integration-backend",
  "aud": "https://auth.claude.com",
  "iat": 1791230000,
  "exp": 1791230300
}
```

`auth.claude.com` accepts any JWT from your identity provider that matches your app’s subject pattern and claim conditions. To narrow them, see [Set up client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#set-up-client-authentication).

## Authorization requests

To build the approval flow that uses these values, see [Send the customer to approve](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve).

### Authorization request parameters

Send these parameters and the ones in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-authentication) to the PAR endpoint.

| Parameter | Description |
| ----- | ----- |
| `response_type` | The value `code` |
| `client_id` | Your OAuth app’s client ID |
| `redirect_uri` | A URI that exactly matches a registered redirect URI, up to 2,048 characters |
| `scope` | `billing:attribution` or `billing:attribution offline_access`. See [what each scope allows](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#scopes). |
| `state` | A random, single-use value, up to 2,048 characters, that you check on the callback |
| `code_challenge` | `BASE64URL(SHA256(code_verifier))` without padding, where the `code_verifier` is 43 to 128 characters |
| `code_challenge_method` | The value `S256` |
| `connection_type` | The value `organization_shared`. An administrator approves the connection for a whole organization. |
| `connection_auth_target` | The value `platform`. The connection’s requests route to the owner of the OAuth app. |
| `user_profile_id` | The ID of a user profile in your organization that represents the customer and that isn’t archived |

The PAR endpoint returns HTTP 201 with `request_uri` and `expires_in`. Then, send the person’s browser to the authorization endpoint with only these two parameters:

| Parameter | Value |
| ----- | ----- |
| `client_id` | Your OAuth app’s client ID |
| `request_uri` | The value that the PAR endpoint returned |

After the person approves, `auth.claude.com` redirects the browser to your `redirect_uri` with these query parameters:

| Parameter | Value |
| ----- | ----- |
| `code` | The authorization code to exchange at the token endpoint |
| `state` | The `state` value that you sent. Check that it matches. |
| `iss` | `https://identity.anthropic.com/users`, which differs from the endpoints’ host. Check that it’s present and matches. |

### Scopes

| Scope | Description |
| ----- | ----- |
| `billing:attribution` | A connection that lets you bill a customer’s Claude organization for the Claude API requests that the customer directs you to make. Send it alone or with `offline_access`. |
| `offline_access` | Also gives your app a refresh token. On a billing connection, send it only together with `billing:attribution`. |
| `org:billing_attribution` | Deprecated: use `billing:attribution`. See [If you still use the deprecated scope](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#if-you-still-use-the-deprecated-scope). |

### Redirect URI rules

* Each `redirect_uri` must exactly match a URI registered on your app. There’s no wildcard or prefix matching. The one exception is a local-development URI registered with an asterisk as the port, such as `http://localhost:*/callback`, which matches any port.
* Every redirect URI must use HTTPS and must not contain a fragment. Local-development URIs on `localhost`, `127.0.0.1`, or `[::1]` may use HTTP.
* You can register up to 10 redirect URIs for each app.
* `auth.claude.com` sends errors to your redirect URI only when the `redirect_uri` matches a registered URI. For any other `redirect_uri`, it doesn’t redirect the browser.

## OAuth tokens

### Token request and response

To exchange a code, send these parameters to the [token endpoint](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#endpoints):

| Parameter | Value |
| ----- | ----- |
| `grant_type` | `authorization_code` |
| `code` | The code from the callback |
| `redirect_uri` | The same `redirect_uri` that you sent in the authorization request |
| `code_verifier` | The PKCE code verifier |
| `client_id`, `client_assertion_type`, `client_assertion` | As in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-authentication) |

To refresh, send `grant_type` set to `refresh_token`, the `refresh_token`, and the parameters in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-authentication). Each refresh token works once, and a billing connection has rules of its own: see the next section and [If a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails).

### OAuth tokens for a billing connection

For a `billing:attribution` connection, a refresh must not send a `scope` parameter. Both grants return these fields:

| Response field | Value |
| ----- | ----- |
| `access_token` | The connection’s access token |
| `token_type` | `Bearer` |
| `expires_in` | Seconds until the access token expires, at most `3600` |
| `scope` | Always `workspace:inference`, not the scope that you asked for |
| `connection_id` | The connection ID, for example `ocon_01HV9Z`. Only the `authorization_code` grant returns it. |
| `refresh_token` | Returned only when the customer approved `offline_access`. A refresh returns a new one, which replaces the one you sent. |
| `refresh_token_expires_in` | Seconds until `refresh_token` expires. Absent when there’s no `refresh_token`. |

The access token authenticates as your app’s [operator service account](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#terms), in the app’s [default workspace](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/set-up-your-app#default-workspace), which the API calls its `connection_token_workspace_id` setting. On `/v1/messages` and `/v1/chat/completions`, a request with it is billed to that connection’s customer. It works only on the endpoints listed in [Call Claude with a customer’s access token](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#call-claude-with-a-token), and any other endpoint refuses it. How to use, refresh, and recover these tokens is in [Use a separate credential for each customer](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer).

Each of these events revokes a `billing:attribution` connection’s tokens, the current access token included:

* The customer or you unlink.
* The customer approves a new authorization request with different scopes for the same user profile, and you exchange its code. The new connection replaces the earlier one.
* The workspace that the tokens run in is archived.
* A refresh token that a refresh replaced is sent again more than 30 seconds later.
* You revoke one of the connection’s tokens at the [revocation endpoint](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#revocation).

### Lifetimes

| Item | Lifetime |
| ----- | ----- |
| `request_uri` from the PAR endpoint | 10 minutes, single use |
| Authorization code | 5 minutes, single use |
| `access_token` | Up to 1 hour |
| `refresh_token` | Up to 1 year from the code exchange. A refresh doesn’t extend it. |

Where a response gives `expires_in` or `refresh_token_expires_in`, read the lifetime from it rather than from this table.

### Revocation

Send revocation requests to the revocation endpoint, `https://auth.claude.com/v1/oauth/revoke`. Besides tokens, it accepts connection and user profile IDs. To unlink a customer or link them again, see [Manage linked customers](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/manage-customers). Send the parameters in [Client authentication](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-authentication) and exactly one of these:

| Parameter | What it ends |
| ----- | ----- |
| `connection_id` | One of your app’s connections, given as an `ocon_` ID |
| `user_profile_id` | All of your app’s connections on one user profile, given as a `uprof_` ID |
| `token` | The connection that an access token or refresh token belongs to, and all of that connection’s tokens |

An access token from a connection approved with the deprecated `org:billing_attribution` scope is an exception: sending it ends only that token. To end that connection, send `connection_id` or `user_profile_id`.

`auth.claude.com` accepts `token_type_hint` and ignores it.

The endpoint returns HTTP 200 and the IDs of the connections that the request ended:

```json
{
  "revoked_connection_ids": ["ocon_01HV9Z"]
}
```

The list is empty in any of these cases, and the response doesn’t say which:

* The token or ID is unknown or belongs to another app.
* The connection has already ended.
* The request ended a token but no connection.

After a connection ends, the Claude API refuses requests that bill that customer with `user_profile_billing_not_authorized`, and the connection’s tokens stop working. An access token from a connection approved with the deprecated scope might instead work until it expires.

## Protocol errors

### Errors on the redirect

`auth.claude.com` returns errors as `error`, `error_description`, `state`, and `iss` query parameters on your redirect URI. They are standard OAuth 2.0 errors ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)), except `user_profile_already_linked`.

| Error | When |
| ----- | ----- |
| `access_denied` | The person declined or can’t approve this request. See [`access_denied`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#access-denied). |
| `server_error` | `auth.claude.com` failed to process the request. Ask the person to try again. |
| `user_profile_already_linked` | The customer’s organization is already linked to your app through a different user profile, or the user profile is already linked to your app through a different organization. See [`user_profile_already_linked`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#user-profile-already-linked). |

If the `request_uri` has expired or was already used, `auth.claude.com` displays an error page and doesn’t redirect the browser. Start again with a new pushed authorization request.

### Errors from the PAR and token endpoints

These endpoints return a JSON body with `error` and `error_description`.

| Error | When |
| ----- | ----- |
| `invalid_request` | A required parameter is missing or invalid, such as a missing `state`, a missing PKCE challenge, or a `user_profile_id` that isn’t an active user profile in your organization |
| `invalid_client` | The client ID is unknown, or the client assertion failed a check in [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-assertion-claims). Your app’s **Client authentication history** in the Claude Console says which check failed. |
| `invalid_scope` | The scope isn’t allowed for this app, a refresh of a billing connection sent a `scope` parameter, or `billing:attribution` was removed from your app. In the last case, a code exchange also uses up the code. |
| `invalid_grant` | At the code exchange: the code expired or was already used, the person who approved has signed out, or the code doesn’t match the `redirect_uri` or `code_verifier`. A mismatch uses up the code. |
| `invalid_grant` | At the code exchange: the customer approved again with the same scopes while their connection has a refresh token. See [If a customer approves again](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#if-a-customer-approves-again). |
| `invalid_grant` | On a refresh: see [If a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails) |
| `unauthorized_client` | Your app isn’t set up for this request. It uses up no code and revokes no refresh token. See [`unauthorized_client`](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#code-exchange-unauthorized-client) or, for a refresh, [If a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails). |
| `user_profile_already_linked` | From the token endpoint: between the approval and the exchange, the profile or the organization was linked another way |

Some responses come in another format, which might not be JSON. That happens when `auth.claude.com` rate-limits a request or has an outage. It also happens for an unknown `grant_type` or a parameter that’s too long. Handle a response without a string `error` by its status, using the first row that fits:

| Status | What to do |
| ----- | ----- |
| Any status, on a refresh | Follow [If a refresh fails](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/credential-for-each-customer#if-a-refresh-fails). |
| `501` | Anthropic has turned the endpoint off. Don’t retry. |
| `429` or `5xx` | Retry with backoff, and wait at least as long as any `retry-after` header says. Send each retry from your own code: an HTTP client’s automatic retries might not run for such a response. |
| Any other status | Treat it as a fault in the request. |

### Errors from the revocation endpoint

For most refusals, the revocation endpoint returns HTTP 400 and a JSON body with `error` and `error_description`.

| Error | When |
| ----- | ----- |
| `invalid_request` | A parameter is missing or invalid: none or more than one of `token`, `connection_id`, and `user_profile_id`, a malformed ID, or a credential in the URL query string |
| `invalid_request` | The user profile has too many connections for one request. It might have ended some, so end the rest with each `connection_id`. |
| `invalid_client` | `auth.claude.com` couldn’t authenticate your app. Check your client assertion against [Client assertion claims](https://platform.claude.com/docs/en/manage-claude/oauth-apps/endpoints-and-parameters#client-assertion-claims). Your app’s **Client authentication history** doesn’t record this endpoint. |
| `unauthorized_client` | Your app isn’t set up for this request. Contact [Anthropic support](https://support.claude.com/en/articles/9015913-how-to-get-support) or your Anthropic account team if you have one. |

Other refusals carry only a status, and their body might not be JSON. When such a body is JSON, its `error` is an object, not a string:

| Status | When | What to do |
| ----- | ----- | ----- |
| `400` | A parameter is longer than its limit | Correct the request. Don’t retry. |
| `429` | Too many failed requests came from your IP address | Retry with backoff. |
| `500` | `auth.claude.com` failed to process the request | Retry with backoff. If it keeps happening, contact support or your account team. |
| `501` | Anthropic has turned the endpoint off | Don’t retry. Contact support or your account team. |
| `503` | The request didn’t finish, and anything it ended stays ended | Retry with backoff. Use the same parameters and a new client assertion. |

A retry after a `503` finishes the rest, and its list leaves out connections that the earlier request ended. With `connection_id`, retry at any time. With `user_profile_id`, retry within a day. After a day, a retry still ends active connections. It doesn’t revoke what’s left of the connections that the failed request ended, such as their OAuth tokens. To revoke that, send each stored `connection_id`.

### Billing errors

The Claude API’s errors for requests that bill a customer or that use a customer’s access token are in [Linked billing errors](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/errors#while-billing).

## Standards

| Standard | Where it applies |
| ----- | ----- |
| [OAuth 2.0 (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749) | The authorization code flow, the token endpoint, and error responses |
| [PKCE (RFC 7636)](https://www.rfc-editor.org/rfc/rfc7636) | Required with `S256` on every authorization request |
| [Pushed authorization requests (RFC 9126)](https://www.rfc-editor.org/rfc/rfc9126) | Required for Linked billing |
| [Authorization server issuer identification (RFC 9207)](https://www.rfc-editor.org/rfc/rfc9207) | The `iss` parameter on every redirect to your app |
| [Token revocation (RFC 7009)](https://www.rfc-editor.org/rfc/rfc7009) | The revocation endpoint, which also takes connection and user profile IDs |
| [JWT client authentication (RFC 7523)](https://www.rfc-editor.org/rfc/rfc7523) | Client authentication at the PAR, token, and revocation endpoints |

## Terms used on these pages

These meanings apply only to Claude Platform OAuth.

| Term | Meaning |
| ----- | ----- |
| Claude organization | An organization account with Anthropic. Your company has one, and so does each customer that links its organization for billing. |
| Administrator | A member of a Claude organization with the Admin or Billing role |
| OAuth app | The registration in your Claude organization that identifies your product to `auth.claude.com`. It has a client ID, name, logo, homepage, and redirect URIs. |
| Identity provider | The service in your own infrastructure that signs short-lived JWTs for your back end and publishes its public keys as a JSON Web Key Set (JWKS). It’s never Anthropic. |
| Client assertion | A short-lived JWT that your identity provider signs and that your back end sends to authenticate your OAuth app |
| Pushed authorization request (PAR) | A request in which your back end sends the authorization parameters to `auth.claude.com` and gets a `request_uri` to use in the browser redirect |
| Workload Identity Federation | The Claude Console feature where your organization registers your identity provider so that Anthropic accepts JWTs signed with your keys |
| User profile | A record in your own Claude organization that stands for one of your customers |
| Connection | The record that ties a customer’s Claude organization to one of your user profiles, created when the customer links your app. Its ID starts with `ocon_`. |
| Service account | A non-human account in your Claude organization. Your app’s operator service account is the one your back end authenticates as to bill a customer. |
| Connection’s OAuth tokens | The access token that `auth.claude.com` returns for a connection and the refresh token it returns with `offline_access`. The access token can bill only that connection’s customer. |

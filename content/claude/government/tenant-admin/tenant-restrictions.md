> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant restrictions

> Restrict which Claude for Government tenants can be reached from your agency's network by having your network proxy inject an allowlist header.

> **Who this is for:** IT and network administrators who operate their agency's outbound web proxy or secure web gateway and want to prevent users on that network from signing in to Claude for Government with a different agency's account.

Tenant restrictions let you limit which Claude for Government tenants can be reached from your network. Your network appliance adds a header to every outbound request listing the tenants you allow, and Claude for Government refuses any request that authenticates as a tenant not on that list.

This is useful when people on your network may hold accounts in more than one agency's tenant (for example, a contractor who supports several agencies) and you need to ensure that work done from your network stays within your own tenant.

There is nothing to enable on the Claude for Government side. The restriction is activated entirely by the presence of the header on the request, so it takes effect the moment your proxy begins injecting it and only for traffic that passes through that proxy.

## How it works

Your agency's network appliance (a forward proxy, secure web gateway, or similar device that can inspect and modify HTTPS traffic) injects an `Anthropic-Allowed-Tenant-Ids` header on every request it forwards to Claude for Government. The header value is a comma-separated list of tenant IDs.

On each request, Claude for Government compares the authenticated user's tenant against the list in the header. When the header is present and the user's tenant is not on the list, the request is refused. When the header is absent, no restriction applies.

The check covers every way a user can reach Claude for Government:

* The web application, including the tenant and organization admin portals
* The desktop application
* Claude Code
* The Claude for Microsoft 365 add-ins
* Direct API calls
* SCIM directory provisioning and the [Compliance API](/docs/government/org-admin/compliance-api)

The same check applies at sign-in, so a user signing in to a tenant that is not on the list sees the refusal at the sign-in screen rather than after authentication completes.

<Note>
  A tenant restriction can only narrow access. A user still needs valid credentials for a tenant on the list; the header never grants access to a tenant the user does not already belong to.
</Note>

## Configure your network proxy

Configure your appliance to do both of the following on every request to your Claude for Government domains:

1. **Remove** any `Anthropic-Allowed-Tenant-Ids` header that arrived from the client.
2. **Set** a single `Anthropic-Allowed-Tenant-Ids` header to your allowlist value.

<Warning>
  Your appliance must remove the incoming header before setting its own. If the appliance only appends, ordinary traffic still works, so the misconfiguration is not obvious. A client that supplies its own value can then reach the server with both values, which either bypasses the restriction or causes that client's requests to fail, depending on how the appliance merges the two. Most secure web gateway products have a distinct "set" or "overwrite" action that removes and replaces in one step; use that rather than "append" or "add".
</Warning>

Apply the rule to requests for the Claude for Government domains provided to you during onboarding, as well as your agency's own custom domain if you have one. Because Claude for Government is served over HTTPS, your appliance must perform TLS inspection for these hosts so that it can add the header to the encrypted request.

Requests that do not pass through your appliance (for example, from a device that is off your network) do not carry the header and are not restricted. Pair this feature with your existing controls that ensure managed devices route through the appliance.

## Header format

The header name is `Anthropic-Allowed-Tenant-Ids`. Header names are not case-sensitive, so your appliance may send the name in any casing.

The value is one or more tenant IDs separated by commas. A tenant ID has the form `umb_` followed by a lowercase UUID with dashes. The `umb_` prefix is optional, and whitespace around each ID is ignored. The UUID must be lowercase; an uppercase or mixed-case value is rejected as invalid.

```text theme={null}
Anthropic-Allowed-Tenant-Ids: umb_00000000-0000-4000-8000-000000000000
```

For more than one tenant, separate the IDs with commas:

```text theme={null}
Anthropic-Allowed-Tenant-Ids: umb_00000000-0000-4000-8000-000000000000, umb_11111111-1111-4111-8111-111111111111
```

### Finding your tenant ID

Anthropic provides your tenant ID during onboarding. If you do not have it on hand, contact Anthropic support and ask for the tenant ID for your deployment.

## What a blocked user sees

A user who tries to sign in to a tenant that is not on your allowlist sees a refusal page titled **This account isn't permitted from this network**, with guidance to sign in with an authorized account or contact their IT administrator.

A user who is already signed in when the restriction takes effect, or whose application makes a request in the background, receives an error in the product reading **Your organization restricts which accounts can be used from this network. Contact your IT administrator.** Direct API calls return HTTP 403 with the error code `tenant_restriction_violation` and the message `Access restricted by network policy. Contact your IT administrator.`

The refusal does not tell the user which tenants are permitted. Keep a record of your allowlist alongside your proxy configuration so that your help desk can answer user questions without inspecting the appliance.

## How invalid headers are handled

Claude for Government rejects malformed headers so that a misconfigured proxy fails visibly rather than silently allowing everything through. A request is rejected with HTTP 400 and the error code `tenant_restriction_header_invalid` when any of the following is true:

* The header is present but empty, or contains only whitespace or commas.
* Any value in the list is not a valid tenant ID.
* The list contains more than 64 tenant IDs.
* The request carries more than one `Anthropic-Allowed-Tenant-Ids` header.

A request with no `Anthropic-Allowed-Tenant-Ids` header at all is not restricted.

## Verifying the configuration

You can confirm the restriction is working before rolling it out broadly.

To confirm a block, temporarily set the proxy's allowlist to a tenant ID you do not own (any validly formatted ID works), then sign in to your own tenant from a browser that routes through the proxy. You should see the **This account isn't permitted from this network** refusal page. A direct API request in the same configuration should return HTTP 403 with the error code `tenant_restriction_violation`.

To confirm normal access, set the proxy's allowlist to your real tenant ID and repeat the request. It should succeed.

To confirm the appliance is overwriting rather than appending, have the test client send its own `Anthropic-Allowed-Tenant-Ids` header with your real tenant ID while the proxy's allowlist is set to an ID you do not own. The request should still return 403 (the proxy's value wins), not 400 (two headers reached the server) or 200 (the client's value reached the server).

## Things to know

* Personal Claude accounts use `claude.ai`, which is a separate host from the Claude for Government service. A personal account cannot sign in to Claude for Government, and a Claude for Government account cannot sign in to `claude.ai`. The header-based restriction on this page applies only to Claude for Government traffic; it does not govern access to `claude.ai`.

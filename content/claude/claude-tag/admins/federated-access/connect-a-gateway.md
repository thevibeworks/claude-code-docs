> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect a gateway

> Connect a gateway you run so Claude Tag can call your internal services with a short-lived identity token instead of a stored credential. Covers what the gateway must check, how to register it in the console, and how to verify the connection.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Gateways are connected at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation and use the **Gateways** section. Connecting a gateway needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

A gateway is a service you run between Claude and your internal systems. Every request Claude sends it carries a signed identity token naming your organization and the [agent](/docs/claude-tag/concepts/agent-identity) making the request (Claude's identity in one Slack channel). The gateway checks the token, decides what that agent may do, and forwards the request with your own credentials. No long-lived credential for your systems is stored in Claude.

Two terms recur on this page. The **subject check** is what your gateway does to every token, confirming it belongs to your organization. The **connection check** is what the console does once, when you connect the gateway, confirming that your gateway performs the subject check.

## Before you begin

* You're an organization Owner, or an admin with full Claude Tag management permission.
* The gateway has a public HTTPS address with a domain name, such as `https://gateway.example.com`, on the standard HTTPS port. The console rejects a path, port, trailing slash, IP address, private-network name, Anthropic-owned host, or cloud token-exchange host.
* The gateway can reach `https://identity.anthropic.com` to fetch Anthropic's signing keys.
* If you start from Anthropic's [sample gateway](https://github.com/anthropics/claude-tag-wif-gateway-sample) (Python, Apache 2.0), terminate TLS in front of it, because it listens on plain HTTP, and set its `audience` to the public address you register.
* An organization can register up to 5 addresses, counting gateways and authorization-server token endpoints together.

## Copy the values and deploy the gateway

In **Gateways**, click **Connect a gateway** and copy the **Issuer**, **JWKS URL**, **Subject prefix**, and **Control subject** rows from the **Set your gateway to accept these values** card, which appears as soon as the dialog opens and doesn't depend on the address. Then click **Cancel**; you register the gateway after deploying it.

Claude authenticates with a JSON Web Token (JWT) in the `Authorization: Bearer` header of every request. It reuses one token for a session's requests for about five minutes, or until your gateway answers 401, and then requests a new one, so don't treat a repeated `jti` as a replay. Verify it with a standard JWT or OpenID Connect (OIDC) library configured with these values.

| Value           | What to configure                                                                                                                                                                                                              |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issuer          | `https://identity.anthropic.com/agents`, matched exactly. The OIDC discovery document is at `https://identity.anthropic.com/agents/.well-known/openid-configuration`.                                                          |
| Signing keys    | The JSON Web Key Set (JWKS) named by `jwks_uri` in the discovery document, `https://identity.anthropic.com/agents/jwks.json`. Accept ES256 only. On an unknown key ID, refetch the key set before rejecting the token.         |
| Audience        | Your gateway address as the console stores it (the console converts the host to lowercase), for example `https://gateway.example.com`. The `aud` claim is a JSON array with one element, so use the library's audience option. |
| Subject prefix  | `wimse://identity.anthropic.com/org/<your organization ID>/agent/`, copied from the dialog. Every token's `sub` claim names one agent in one organization.                                                                     |
| Tenant          | Your organization ID, the value between `/org/` and `/agent/` in the **Subject prefix**, carried in every token as the `tenant` claim.                                                                                         |
| Control subject | A reserved test identity in your organization, copied from the dialog. Anthropic uses it only for the connection check.                                                                                                        |
| Expiry          | Tokens expire 10 minutes after they're issued. Check `exp`, allowing up to 60 seconds of clock skew.                                                                                                                           |

The subject check is yours to implement, and it's required, because every organization's tokens come from the same issuer; see [Authorize on the subject](/docs/claude-tag/admins/federated-access/token-reference#authorize-on-the-subject). Implement the check in one of two forms, strongest first:

* Accept only an explicit list of your own agents' full subjects, when your use case allows it. The sample gateway does this by default and offers the prefix form below as an opt-in setting. Agent IDs change when a Slack channel is deleted and recreated, so you update the list when that happens.
* Otherwise, reject every token whose `sub` doesn't start with your **Subject prefix**, or pin `iss` and `tenant` together. The `tenant` claim is your organization ID, the same value the subject carries between `/org/` and `/agent/`, so checking it is the subject check in claim form. This is the minimum.

For the connection check, the gateway also needs a route at the address itself, with no path, that answers an empty `POST` by verifying the token and reporting whether the subject is accepted (2xx if it is, 401 or 403 if not) and does nothing else. Agents normally call a path; the root route exists for the connection check, and an agent that calls it gets the same accept-or-reject answer. The sample gateway calls this its readiness route. The check sends it two requests, and any other status from either one fails the check:

* A token valid in every other way (your audience, Anthropic's issuer and signature, unexpired) whose subject isn't your organization. The gateway must answer 401 or 403. Only the `tenant` or subject check can reject it.
* A token for the **Control subject**. The gateway must answer 2xx. A gateway that lists exact subjects must include the control subject in its list, and a prefix or `tenant` check accepts it on its own, because it belongs to your organization. Either way, map it to no service.

With the sample gateway, set `audience` in `config.yaml` to your registered address and add a `principals` entry for the **Control subject** with `allowed_services: []` (the example config ships with a placeholder organization ID). By default the sample accepts only the subjects listed under `principals`; an agent that isn't listed gets 403, and the sample logs its full subject so you can add it. To accept every agent in your organization instead, add an `organization_principals` entry keyed by your **Subject prefix**. The control subject still needs its exact `principals` entry either way.

Never forward the Claude Tag token downstream; replace the `Authorization` header with your own credential.

## Register the gateway in the console

<Steps>
  <Step title="Open the Connect a gateway dialog">
    In **Gateways**, click **Connect a gateway**.
  </Step>

  <Step title="Enter the gateway address">
    In the **Gateway address** field, enter the host only, in lowercase, starting with `https://`, for example `https://gateway.example.com`. This address is the token's audience.
  </Step>

  <Step title="Confirm the subject check">
    Select the **This gateway checks that each token's subject belongs to your organization** checkbox. The **Run check and connect** button stays disabled until you do. Select it only if the gateway rejects every subject outside your organization, by explicit list, by prefix, or by the `tenant` claim.
  </Step>

  <Step title="Run the connection check">
    Leave the **Run the check** option selected and click **Run check and connect**. The check can take up to a minute. If it fails, nothing is registered; see [Common errors](#common-errors). If the gateway can't be reached from the internet yet, select the **Skip the check** option, enter a **Reason for skipping**, and click **Connect without the check**. The reason is shown in the **Gateways** table. Entering an address that is already registered runs the check again (unless you skip it) without changing the stored result, then moves to the bundle step.
  </Step>

  <Step title="Add the gateway to an Access bundle">
    Choose a bundle from the **Access bundle** list, or click **New bundle**, enter a **Bundle name**, and click **Create bundle**. Then click **Add to bundle**. This creates a connection in that bundle, labeled **Gateway** on its **Credentials** tab, with the gateway's host as its allowed website. A gateway can be in one bundle only; to use it in several scopes, attach that bundle to each. Click **Not now** to finish without a bundle.
  </Step>
</Steps>

The **Gateways** table lists each gateway with its **Connection check** result (**Passed**, or **Skipped** with your reason), when it was added, and **Add to bundle** and **Remove** actions. For a gateway that is already registered, skip the dialog's first step: click **Add to bundle** in the gateway's row of the **Gateways** table, which opens the dialog at the bundle step. Entering the address again in **Connect a gateway** also reaches the bundle step, but unless you skip the check it runs again first, and that run counts toward the check limit.

## Let agents reach the gateway

Claude uses the gateway in channels whose scope has the bundle attached. [Attach the bundle to a workspace or channel](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) if it isn't attached already.

Claude also needs to know the gateway exists. Add a line like this to the scope's [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions):

```text wrap theme={null}
Internal APIs are behind https://gateway.example.com. Call GET /list-services there to see what is available.
```

The sample gateway serves `GET /list-services` for this; an OpenAPI document named in the instructions works as well.

New threads pick up the connection on their own. In a thread already running, ask Claude to use the gateway and include its address. If Claude still can't see the gateway, send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) at the channel's top level to start a fresh session with your organization's current configuration.

## Verify the connection

In a channel under the bundle's scope, start a new thread and ask Claude to make a small read through the gateway:

```text wrap theme={null}
@Claude call GET /list-services on https://gateway.example.com and tell me what it returns.
```

If your gateway logs subjects and decisions, confirm the request arrived with a token that passed every check and a subject starting with your **Subject prefix**. [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) attaches the token at the network boundary; the model and the sandbox are not given it.

To disconnect a gateway, click **Remove** in the gateway's row of the **Gateways** table. Claude stops using the gateway at once. A token issued before the removal stays valid until it expires, within 10 minutes.

## Common errors

Two messages come up while connecting:

* **"The check didn't pass"**: the gateway isn't reachable from the internet over HTTPS, its root route doesn't answer an empty `POST` directly, or the subject check is missing or rejects the **Control subject**. See [The check didn't pass](/docs/claude-tag/admins/federated-access/troubleshooting#the-check-didn%E2%80%99t-pass).
* **A bundle-step message that the gateway is already in a bundle**: a gateway can be in one bundle only. [Attach that bundle to the scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) instead.

For other dialog messages, see [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the Access bundle and connection model
* [Attach a bundle to a scope](/docs/claude-tag/admins/attach-to-scope): where a gateway connection applies
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim in the token, lifetimes, and key rotation
* [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting): console and runtime errors for every connection type
* [Sample gateway](https://github.com/anthropics/claude-tag-wif-gateway-sample): a reference gateway with offline tests

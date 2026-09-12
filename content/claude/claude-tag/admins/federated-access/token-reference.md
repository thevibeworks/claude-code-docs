> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Identity token reference

> The claims, issuer, signing keys, lifetime, and subject format of the identity token Claude Tag presents to a gateway, cloud provider, or authorization server.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

When Claude calls a system you connected through Federated cloud access, it proves who it is with a signed identity token instead of a stored credential. The token is a JSON Web Token (JWT) that names your organization and the agent making the request. A gateway you run receives it in the `Authorization: Bearer` header and verifies it directly. AWS, Google Cloud, or your authorization server receives it in a token exchange and returns one of its own credentials.

This page lists what the token contains so the engineer who configures the verifying side can pin the right values. For setup steps, see [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway), [Connect an AWS role](/docs/claude-tag/admins/federated-access/aws), [Connect a Google Cloud identity](/docs/claude-tag/admins/federated-access/gcp), or [Connect an authorization server](/docs/claude-tag/admins/federated-access/authorization-server).

## Issuer and signing keys

| Item                                       | Value                                                                                             |
| :----------------------------------------- | :------------------------------------------------------------------------------------------------ |
| Issuer (`iss`)                             | `https://identity.anthropic.com/agents`. Match it exactly, including the `/agents` path.          |
| OpenID Connect (OIDC) discovery document   | `https://identity.anthropic.com/agents/.well-known/openid-configuration`                          |
| Signing keys, as a JSON Web Key Set (JWKS) | `https://identity.anthropic.com/agents/jwks.json`, the `jwks_uri` named in the discovery document |
| Signing algorithm                          | ES256 only. Reject any other `alg`, including `none`.                                             |

Both documents are public and need no authentication to fetch. One issuer serves every Claude Tag organization, so the issuer and signature prove only that Anthropic issued the token. The [subject](#subject), or the `tenant` claim, is what ties a token to your organization.

### Key rotation

Signing keys rotate. If you run the verifier yourself, select the key by the token's `kid` header and refetch the JWKS when you see a `kid` you don't know, before rejecting the token. Most JWKS libraries do this by default. Don't pin a single key. AWS and Google Cloud manage their own key caches.

## Lifetime

| Claim | Value                                                                                     |
| :---- | :---------------------------------------------------------------------------------------- |
| `iat` | When the token was issued, in seconds since the Unix epoch                                |
| `nbf` | 15 seconds before `iat` (current behavior, may change). Libraries check it automatically. |
| `exp` | 10 minutes (600 seconds) after `iat`                                                      |
| `jti` | A unique ID for this token                                                                |

Allow up to 60 seconds of clock skew when you check `exp`, and treat `exp` as the earliest moment a token may stop working rather than an exact cutoff; cloud providers apply their own grace.

Tokens can't be revoked before they expire. There is no revocation list or introspection endpoint. When you remove a gateway in the console, Claude stops using it at once, and a token issued before the removal stays valid until it expires, within 10 minutes. When you remove a cloud role or authorization server, Claude stops using it within about a minute, and a credential from an earlier exchange stays valid with AWS, Google Cloud, or your server until it expires, held only by Agent Proxy, never by Claude's sandbox.

Claude reuses one token for a session's requests to the same gateway for about five minutes, half the token's lifetime, or until the gateway answers 401, and then requests a new one (current behavior, may change). A gateway therefore sees the same `jti` on many requests, so don't treat a repeated `jti` as a replay. AWS, Google Cloud, and an authorization server each see a token once per exchange.

## Subject

The `sub` claim names one agent in one organization:

```text theme={null}
wimse://identity.anthropic.com/org/<your organization ID>/agent/<agent ID>
```

* The organization ID starts with `org_` and the agent ID with `cagt_`. Both use only letters, digits, `_`, and `-`, so neither can contain `/` or `:`.
* The **Connect a gateway**, **Connect an AWS role**, **Connect a Google Cloud identity**, and **Connect an authorization server** dialogs show your organization's **Subject prefix**, `wimse://identity.anthropic.com/org/<your organization ID>/agent/`. Every one of your agents' subjects starts with this prefix.
* An agent belongs to one Slack channel. Deleting and recreating a channel creates a new agent with a new ID. The console doesn't show agent IDs; a verifier learns full subjects from the tokens it receives or from your cloud provider's logs.
* The console's connection check for a gateway presents a token for a reserved test agent in your organization, shown in the **Connect a gateway** dialog as the **Control subject**. Your gateway must answer that token with a 2xx status so the check can pass, and must grant that subject no access. See [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway).

The `wimse://` form follows the IETF WIMSE working group's workload identifier specification.

### Authorize on the subject

A token with a valid signature, issuer, audience, and expiry can still belong to another organization, because one issuer serves every Claude Tag organization and every organization's AWS tokens share one audience. Only the subject, or the `tenant` claim, says which organization a token belongs to, so every verifier, trust policy, and attribute condition must check it. Write the check in one of two forms, strongest first:

* **Pin the exact subjects.** Accept only the full subjects of your own agents. This is the strongest form, so use it whenever your use case allows. You update the rule when a Slack channel is deleted and recreated, because the new channel's agent has a new ID, and a gateway's list must also include the **Control subject**.
* **Require your organization.** If keeping a list of exact subjects isn't practical, require that `sub` start with your **Subject prefix**, including the `/agent/`, or pin `iss` together with `tenant`, which carries the same organization ID. This is the minimum, and it accepts every agent in your organization, including agents in channels created later.

## Audience

The `aud` claim is a JSON array with one element. Use your library's audience option rather than comparing the raw claim text; some libraries print a one-element array as a bare string.

| Where the token goes    | `aud`                                                                                                                                                                                                                                                                                                           |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A gateway you connected | The HTTPS address you registered, which the console accepts only as a bare host on the standard port and stores in lowercase, for example `https://gateway.example.com`                                                                                                                                         |
| AWS                     | `sts.amazonaws.com`                                                                                                                                                                                                                                                                                             |
| Google Cloud            | Your workload identity provider's full resource name, for example `//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/claude/providers/agents`                                                                                                                                      |
| An authorization server | Your server's issuer identifier as you entered it when connecting the server (an HTTPS URL on the token endpoint's host), for example `https://auth.example.com`, or the token endpoint URL exactly as registered, for example `https://auth.example.com/oauth2/token`, if you left the issuer identifier empty |

The audience identifies the destination, not your organization; every organization's AWS tokens share `sts.amazonaws.com`. Always check the [subject](#subject) too.

## Claims

These are the claims a token carries.

| Claim                | Value                                                                                                                                                                                                                           |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `iss`                | `https://identity.anthropic.com/agents`                                                                                                                                                                                         |
| `sub`                | The agent's subject; see [Subject](#subject)                                                                                                                                                                                    |
| `aud`                | One-element array; see [Audience](#audience)                                                                                                                                                                                    |
| `iat`, `nbf`, `exp`  | Issued-at, not-before, and expiry times; see [Lifetime](#lifetime)                                                                                                                                                              |
| `jti`                | Unique token ID                                                                                                                                                                                                                 |
| `tenant`             | Your Claude organization ID, the same value as the subject's `org/` segment. Together with `iss`, this is the pair a relying party pins to trust tokens from one organization. Not your cloud or identity provider's tenant ID. |
| `agent_id`           | The agent ID, the same value as the subject's `agent/` segment                                                                                                                                                                  |
| `profile_id`         | The ID of the Access bundle the connection belongs to, starting with `capp_`. Informational.                                                                                                                                    |
| `platform`           | `slack` when the request came from Slack. Present whenever `slack_workspace_id` is.                                                                                                                                             |
| `slack_workspace_id` | The ID of the Slack workspace Claude is acting in. Present when the request came from a Slack workspace your organization owns.                                                                                                 |
| `slack_channel_id`   | The ID of the Slack channel Claude is acting in. Present whenever `slack_workspace_id` is and Claude is acting in one channel rather than a whole workspace.                                                                    |

Tokens may carry additional claims Anthropic uses internally for audit; ignore any claim not listed here and never base an authorization decision on it.

Three claim names are reserved and absent from every token: `platform_user_id`, `actor_sub`, and `account_id`. Don't write a rule that depends on them. An absent claim is omitted from the token, never sent empty.

Anthropic sends the token only to the destinations you connect in **Federated cloud access**. When the request comes from Slack, the `slack_workspace_id` and `slack_channel_id` claims carry your Slack workspace and channel IDs to that destination along with your organization and agent IDs.

Authorize on `sub`, as described under [Authorize on the subject](#authorize-on-the-subject). A gateway or authorization server, which can read every claim, can use `tenant` and `agent_id` instead, because they repeat the subject's two parts. An AWS trust policy matches on `sub` and `aud` only; a Google Cloud attribute condition can read `sub` or `tenant`. The token carries no claim that names the person behind the request, and no `groups`, `roles`, or `scope` claims. A rule that needs `slack_workspace_id` or `slack_channel_id` should refuse a token that lacks them.

<Note>Anthropic may add claims to the token. A verifier must ignore claims it doesn't recognize and must never depend on a claim not listed here being present.</Note>

### Example payload

The decoded payload of a token sent to a gateway registered as `https://gateway.example.com`, for a request from a Slack channel, with made-up IDs. Opaque claims are left out.

```json theme={null}
{
  "iss": "https://identity.anthropic.com/agents",
  "sub": "wimse://identity.anthropic.com/org/org_01Hx7rQkPzT9sN3mVbJw2eYd/agent/cagt_01Mz4kVnXr8TqWb2pLsJ7hYe",
  "aud": ["https://gateway.example.com"],
  "iat": 1756600000,
  "nbf": 1756599985,
  "exp": 1756600600,
  "jti": "MX4KT2R7WBH5QZ3NDJ6PVA25FC",
  "tenant": "org_01Hx7rQkPzT9sN3mVbJw2eYd",
  "agent_id": "cagt_01Mz4kVnXr8TqWb2pLsJ7hYe",
  "profile_id": "capp_01Qw9tHnKj5Rz3mXb7PvL2cY",
  "platform": "slack",
  "slack_workspace_id": "T01HX7RQKPZT",
  "slack_channel_id": "C01MZ4KVNXRT"
}
```

## Verify a token

Use a maintained JWT or OIDC library for your language and confirm it performs all five checks. Most libraries check issuer and audience only when configured to.

1. **Signature**: verified against a key from the JWKS, ES256 only.
2. **Issuer**: exactly `https://identity.anthropic.com/agents`.
3. **Audience**: the value registered for your gateway, cloud provider, or authorization server.
4. **Expiry**: `exp` is in the future, allowing up to 60 seconds of clock skew.
5. **Subject**: `sub` is one of your own agents' full subjects, or at minimum starts with your organization's **Subject prefix** (or `tenant` is your organization ID). Libraries don't do this one for you.

Reject the token if any check fails, and answer with a generic 401 that doesn't echo the token.

To read a captured token's claims while debugging, decode its middle segment. JWT payloads are base64url-encoded, so a plain `base64 -d` often fails:

```bash theme={null}
python3 -c 'import base64,json,sys; p=sys.argv[1].split(".")[1]; print(json.dumps(json.loads(base64.urlsafe_b64decode(p + "=" * (-len(p) % 4))), indent=2))' "$TOKEN"
```

Decoding doesn't verify anything. Log the subject and your decision, never the token itself.

## Related resources

* [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway): verify the token yourself at a service you run
* [Connect an AWS role](/docs/claude-tag/admins/federated-access/aws): the trust policy that pins these values
* [Connect a Google Cloud identity](/docs/claude-tag/admins/federated-access/gcp): the attribute condition that pins these values
* [Connect an authorization server](/docs/claude-tag/admins/federated-access/authorization-server): accept the token as a JWT bearer grant
* [Limits](/docs/claude-tag/admins/federated-access/limits): lengths, counts, and lifetimes in one place
* [Sample gateway](https://github.com/anthropics/claude-tag-wif-gateway-sample): a Python gateway that verifies the token and pins subjects exactly or by organization, with offline tests

> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Federated cloud access

> Claude Tag proves its identity to your systems with a short-lived signed token instead of a credential stored in Claude. Learn how the token works and which of the four connection types to use.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Federated connections are managed at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation. Connecting a gateway, cloud role, or authorization server needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

In Slack channels, Claude Tag acts under its own [agent identity](/docs/claude-tag/concepts/agent-identity) rather than as any person. Federated cloud access lets that identity prove itself to your systems with a short-lived, signed identity token instead of a credential you store in Claude. Federated cloud access is in public beta.

In the console, you connect your gateway, AWS role, Google Cloud identity, or authorization server under **Federated cloud access** and add it to an [Access bundle](/docs/claude-tag/admins/add-connections) attached to the channels where Claude should use it. Your cloud or gateway administrator configures that system to trust Anthropic's issuer and to check that each token's subject belongs to your organization, and the system then decides what the agent may do. To confirm the connection works, ask Claude in one of those channels to make a small request, then check its reply and your system's logs.

Federated cloud access goes one way: Claude proves who it is to your systems. For your workloads proving who they are to the Claude API, see [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) on the Claude Developer Platform.

Your systems can accept the token in one of four ways. The table below says which to choose; the rest of the page explains what the token is and what to have ready.

## Choose a connection type

| Connection type           | Who accepts the token                                                                                                                                      | Choose it when                                                                                                                                             |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gateway**               | A service you run. It verifies the token, maps the agent to permissions, and forwards the request to your internal systems with credentials you hold.      | You want one entry point in front of internal APIs. The [sample gateway](https://github.com/anthropics/claude-tag-wif-gateway-sample) is a starting point. |
| **AWS role**              | AWS, through an IAM OIDC identity provider. AWS issues temporary credentials for a role whose trust policy names Anthropic's issuer and your organization. | Claude should call AWS APIs under a role you govern with IAM.                                                                                              |
| **Google Cloud identity** | Google Cloud, through a workload identity pool. Google issues an access token for the federated identity, acting as a service account if you name one.     | Claude should call Google Cloud APIs under an identity you govern with IAM.                                                                                |
| **Authorization server**  | Your OAuth 2.0 authorization server. It accepts the token as a JWT bearer grant (RFC 7523) and returns an access token for your APIs.                      | Your APIs are already protected by your own OAuth server and you'd rather issue its tokens than run a gateway.                                             |

In every case the system on your side decides what the agent may do in your systems. Each connection type has its own setup page: [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway), [Connect an AWS role](/docs/claude-tag/admins/federated-access/aws), [Connect a Google Cloud identity](/docs/claude-tag/admins/federated-access/gcp), and [Connect an authorization server](/docs/claude-tag/admins/federated-access/authorization-server).

## How it works

1. When a request from Claude's sandbox needs one of your systems, [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) matches it by destination to a federated connection in one of the channel's Access bundles. Until an admin connects a system in **Federated cloud access** and adds it to a bundle attached to the channel, nothing matches and no token is issued for Claude's requests.
2. Anthropic issues an identity token. The token is a JSON Web Token (JWT) signed by Anthropic and valid for 10 minutes. Its subject names your organization and the agent, in the form `wimse://identity.anthropic.com/org/<your organization ID>/agent/<agent ID>`, and its audience names the destination. Claude reuses one token for a session's requests to the same gateway for about five minutes, or until the gateway answers 401, and then requests a new one. The other connection types use a token once, in an exchange.
3. Your side accepts the token. A gateway verifies it directly. AWS or Google Cloud exchanges it for a short-lived cloud credential. Your authorization server exchanges it for an access token. Agent Proxy attaches the result to Claude's request, or signs the request with it for AWS, and forwards the request. The model and the sandbox are never given the token or the credential that comes back.

Whichever system accepts the token checks five things:

* **Signature**, against the public keys Anthropic publishes, and **issuer**. Together these prove Anthropic issued the token.
* **Audience**. This proves the token was issued for the destination it's presented to: your gateway, your authorization server, your Google Cloud provider, or AWS.
* **Expiry**. This proves the token is fresh.
* **Subject**. This is what names your organization. Every Claude Tag organization's tokens come from the same issuer, and every organization's AWS tokens share the same audience, so the first four checks can pass for a token that belongs to someone else. Every connection type therefore requires a subject check. The strongest form accepts only the exact subjects of your own agents. The minimum form requires the subject to start with your **Subject prefix**, `wimse://identity.anthropic.com/org/<your organization ID>/agent/`, including the `/agent/`; a gateway, authorization server, or Google Cloud attribute condition can pin `iss` and `tenant` instead, since `tenant` carries the same organization ID.

The console shows the issuer, the signing-key location, and your **Subject prefix** with copy buttons, and each setup page says where they go. The [identity token reference](/docs/claude-tag/admins/federated-access/token-reference) lists every value and claim and [compares the two forms of the subject check](/docs/claude-tag/admins/federated-access/token-reference#authorize-on-the-subject).

Anthropic stores no long-lived credential for your systems, and each call carries a short-lived signed token, so there is no key of yours to rotate or leak. Anthropic rotates its own signing keys, and the [token reference](/docs/claude-tag/admins/federated-access/token-reference#key-rotation) says how a verifier follows them.

To cut off access, remove the connection in the console. These lifetimes then apply:

| What                                           | How long it lasts                                                                                                    |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| A removed connection                           | Claude stops using a removed gateway at once, and a removed cloud role or authorization server within about a minute |
| An identity token already issued               | 10 minutes from when it was issued                                                                                   |
| AWS credentials already exchanged              | 1 hour, the role session length                                                                                      |
| A Google Cloud credential already exchanged    | As long as Google Cloud issued it for                                                                                |
| An access token from your authorization server | The `expires_in` your server returned                                                                                |

Anthropic doesn't review your gateway, trust policy, or authorization server. When you connect a gateway, the console offers a connection check that confirms the gateway rejects a token whose subject isn't your organization. The other connection types have no check in the console, so you verify them yourself with the steps on each setup page.

## Before you begin

* **Federated cloud access** appears in the console's left navigation. It's missing for organizations whose compliance configuration excludes federated cloud access.
* An organization Owner, or an admin with full Claude Tag management permission, makes the connection in the console.
* Your cloud or gateway administrator configures the system on your side: the gateway operator, your AWS or Google Cloud IAM administrator, or your authorization server's operator. Each setup page lists the values they configure.
* An [Access bundle](/docs/claude-tag/admins/add-connections) is attached to the [scope](/docs/claude-tag/concepts/glossary#scope) of the channels where Claude should use the connection. A connection can be in only one bundle, so to use a connection in several places, attach that bundle to each scope.

Federated connections work in Slack channels, where Claude acts under your organization's agent identity. They don't work in direct messages, which run under [the individual's own account](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

## Related resources

* [How agent identity works](/docs/claude-tag/concepts/agent-identity): the identity these tokens represent, and how Agent Proxy attaches credentials
* [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway): verify the token at a service you run
* [Connect an AWS role](/docs/claude-tag/admins/federated-access/aws): the IAM OIDC provider and trust policy
* [Connect a Google Cloud identity](/docs/claude-tag/admins/federated-access/gcp): the workload identity pool, provider, and attribute condition
* [Connect an authorization server](/docs/claude-tag/admins/federated-access/authorization-server): accept the token as a JWT bearer grant
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim, the lifetime, and key rotation
* [Limits](/docs/claude-tag/admins/federated-access/limits): counts, lengths, lifetimes, and unsupported configurations
* [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting): console messages, blocked requests, and rejections in your logs

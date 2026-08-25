> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network requirements

> Claude Tag reaches your services from a published egress range, over HTTP and HTTPS only. See the IP block to allowlist and how the allowlist relates to the allowed-websites setting on a connection.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

If a service you want to connect (a data warehouse, an internal API, a GitHub organization with an IP allow list) restricts access by source IP, add Anthropic's egress range to its allowlist. Hand this page to the team that manages it.

## Add Anthropic's egress range to your allowlist

Requests from Claude to your services originate from Anthropic's network. To let them through, add Anthropic's published egress range to the service's allowlist:

```text wrap theme={null}
160.79.104.0/21
```

The authoritative list is [Anthropic's published IP addresses](https://platform.claude.com/docs/en/api/ip-addresses); check it when you create the rule.

The range is shared across Anthropic services, and dedicated per-organization egress addresses aren't available, so the allowlist entry admits Anthropic's infrastructure as a whole. Your credential's [allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites) are what scope which of *your* systems Claude can call.

Allowlist changes on enterprise systems can take days to take effect, which is why the [setup overview](/docs/claude-tag/admins/setup-overview#before-you-start) sends you here before you start setup.

## Internet reachability

<Warning>A connected service must accept traffic from the internet (restricted by IP allowlist if you like). A service reachable only inside your private network can't be connected; private networking such as PrivateLink or VPC peering is not supported.</Warning>

Every request from a channel's sandbox to your service passes through [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy), which carries HTTP and HTTPS only. A service reachable only over another protocol, such as SSH or a database's native wire protocol, can't be connected; put an HTTP API in front of it instead.

## IP allowlist vs. allowed websites

The IP allowlist on your service and the [allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites) on a connection are opposite sides of the same boundary:

|                       | IP allowlist                         | Allowed websites                        |
| :-------------------- | :----------------------------------- | :-------------------------------------- |
| **Who configures it** | Your team, on your service           | You, on the connection in Claude        |
| **What it decides**   | Which networks may reach the service | Which hosts a credential may be sent to |

## Events and webhooks

Events from connected services, like GitHub activity, are delivered directly to Anthropic, so there is no inbound listener to configure on your side.

## Related resources

* [Add connections](/docs/claude-tag/admins/add-connections#set-allowed-websites): the allowed-websites setting (the other direction: what Claude is allowed to reach)
* [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential): how hosts become reachable from a channel, including [allow-all egress](/docs/claude-tag/admins/add-connections#allow-all-hosts)
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how credentials are injected at the network boundary
* [Setup overview](/docs/claude-tag/admins/setup-overview): back to the console flow once the allowlist is in place

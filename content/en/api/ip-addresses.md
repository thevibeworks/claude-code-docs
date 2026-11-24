---
title: IP addresses
url: https://platform.claude.com/docs/en/api/ip-addresses
description: Anthropic services use fixed IP addresses for both inbound and outbound connections. You can use these addresses to configure your firewall rules for secure access to the Claude API and Claude Console. These addresses will not change without notice.
---

## Inbound IP addresses

These are the IP addresses where Anthropic services receive incoming connections, such as your API requests. If your firewall restricts outgoing traffic, allow it to these addresses.

If you use Claude Models on Google Cloud (Anthropic managed) or Claude Platform on AWS, these addresses don’t apply to your API requests. See the [Cloud platforms](https://platform.claude.com/docs/en/api/ip-addresses#cloud-platforms) section.

### IPv4

`160.79.104.0/23`

`153.61.224.0/22`

### IPv6

`2607:6bc0::/48`

## Outbound IP addresses

These are the stable IP addresses that Anthropic uses for outbound requests (for example, when making MCP tool calls to external servers).

### IPv4

`160.79.104.0/21`

`153.61.208.0/20`

### Phased out IP addresses

The following IP addresses are no longer in use by Anthropic. If you have previously allowlisted these addresses, remove them from your firewall rules.

```text wrap
34.162.46.92/32
34.162.102.82/32
34.162.136.91/32
34.162.142.92/32
34.162.183.95/32
```

## Cloud platforms

On the following platforms, your API requests go to the cloud provider’s endpoint, not to Anthropic’s inbound IP addresses:

* **[Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws):** The endpoint (`aws-external-anthropic.{region}.api.aws`) resolves to [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html).
* **[Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed):** Requests go to Google Cloud’s gateway at `claude.googleapis.com`, which forwards them to Anthropic.

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Project Policies

> The standing policies that apply to everyone who takes part in the MCP project, and where each one is defined.

This page lists the policies that apply to everyone who takes part in the MCP project: in meetings, on Discord, and in every repository under the [`modelcontextprotocol`](https://github.com/modelcontextprotocol) organization. Group Leads and Facilitators link it from meeting agendas.

## Code of Conduct

The [Code of Conduct](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md) governs every channel, repository and meeting. Send reports to [mcp-coc@anthropic.com](mailto:mcp-coc@anthropic.com). The [Community Moderators](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md#community-moderators) handle them under the [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md#community-moderator) and escalate to Core Maintainers when needed.

## Antitrust

Participants often work for competing organizations. MCP is organized as Model Context Protocol a Series of LF Projects, LLC, so the [LF Projects policies](https://www.lfprojects.org/policies/), including its antitrust policy, apply to all participants. The project's own [Antitrust Policy](https://modelcontextprotocol.io/community/antitrust.md) sets out how meetings and standard-setting discussions are conducted.

## Licensing and intellectual property

Code and specification contributions are made under the Apache License 2.0 and other documentation under CC-BY-4.0, with no copyright assignment. The governing text is [General Project Policies](https://modelcontextprotocol.io/community/governance.md#general-project-policies).

## AI-assisted contributions

Any AI assistance used for a contribution must be disclosed in the pull request or issue, together with its extent. This includes AI-written review responses and comments; trivial spacing or typo fixes are the only exception. The full policy is [AI\_POLICY.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/AI_POLICY.md), which applies to every repository in the organization.

## Reporting a vulnerability

> [!WARNING]
>
> Do not report security issues in public issues, discussions or pull requests.

Open a private advisory on the affected repository at `github.com/modelcontextprotocol/<repo>/security/advisories/new`. Private vulnerability reporting is enabled on the specification repository and on every official SDK and project repository. Before filing, read [SECURITY.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md): it says [what to include](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#what-to-include), describes the [trust model and the behaviors that are intentional rather than vulnerabilities](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#intended-behaviors-and-trust-model) (stdio command execution, denial of service by a stdio peer, server side effects, LLM-driven tool invocation), and lists [what remains in scope](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#what-remains-in-scope).

The maintainers who receive a report coordinate the fix and advisory across every affected SDK so that advisories are released together, and raise it with the specification maintainers when the root cause is in the specification (see [SDK Vulnerability Disclosure](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#sdk-vulnerability-disclosure)). CVEs are assigned through GitHub's CNA. Questions that are not themselves a report, including which repository to file against, go to the [Security Interest Group](https://modelcontextprotocol.io/community/interest-groups/security.md) in `#security-ig`.

## Communication and records

[Communication](https://modelcontextprotocol.io/community/communication.md) sets out which channel is for what, when a channel may be private, and where decisions are recorded.

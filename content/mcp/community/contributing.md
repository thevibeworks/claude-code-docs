> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Contributing to MCP

> How to contribute to the Model Context Protocol specification, docs and SDKs.

MCP is an open source project that welcomes contributions from the community. You don't need a change ready to get involved.

You'll find the specification, these docs and Specification Enhancement Proposals (SEPs) in the [specification repository](https://github.com/modelcontextprotocol/modelcontextprotocol). Each SDK and tool has its own repository in the [`modelcontextprotocol`](https://github.com/modelcontextprotocol) organization.

To build with MCP, start with the [server](https://modelcontextprotocol.io/docs/develop/build-server.md) and [client](https://modelcontextprotocol.io/docs/develop/build-client.md) guides, the [SDK list](https://modelcontextprotocol.io/docs/sdk.md) or the [MCP Registry](https://modelcontextprotocol.io/registry/about.md).

If you want to invest some time in our discussions, the protocol work is organized in [working groups and interest groups](https://modelcontextprotocol.io/community/working-interest-groups.md). Their meetings are open to anyone and are listed on [meet.modelcontextprotocol.io](https://meet.modelcontextprotocol.io/). [Meetings and channels](https://modelcontextprotocol.io/community/working-interest-groups.md#meetings-and-channels) sets out how a meeting is announced and minuted. No invitation or role is needed to attend or speak at a meeting, to comment on a pull request, or to open an issue or a discussion.

These same working groups and interest groups are represented in the Discord space.

## Where to start

**1. Join Discord**

Contributors talk about the protocol on [Discord](https://modelcontextprotocol.io/community/communication.md#discord).

**2. Find your group**

Pick the [working group](https://modelcontextprotocol.io/community/working-interest-groups.md#current-groups) or Discord channel that covers your area. If none fits, use `#general`.

The specification repository also labels issues [`good first issue`](https://github.com/modelcontextprotocol/modelcontextprotocol/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) and `help wanted` when they are sized for a first change.

The sections below cover each kind of change.

**3. Talk to the lead**

Each group's page names its leads. Post what you want to work on in the group's channel.

Anyone can join a group meeting, comment on a pull request or open an issue. Check the [calendar](https://meet.modelcontextprotocol.io/) and read the [Antitrust Policy](https://modelcontextprotocol.io/community/antitrust.md) before you attend.

## Report a problem

[Report a vulnerability](https://modelcontextprotocol.io/community/policies.md#reporting-a-vulnerability) in private.

For a bug, typo or unclear text in the specification or these docs, open an [issue](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/new/choose). For an SDK or tool, open it in that repository.

Please don't post usage questions in the repositories. We stopped taking them there because of spam.

## Change the specification or docs

You need write access to open a pull request on the specification repository. We prefer you begin with an issue and follow the steps for a bug below.

**1. Raise the change**

Report a bug in an issue. Raise anything else in your group's channel or `#general`.

**2. Push a branch**

Push to a fork, or to a working group repository you can write to. Specification fixes go in `draft/`. Keep each change to one concern. [CONTRIBUTING.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md) covers setup and checks.

**3. Ask for a pull request**

Link the branch in that issue or channel and ask a maintainer to open a pull request that credits you.

A change to the protocol itself needs a [SEP](#propose-a-protocol-change).

## Work on an SDK or tool

Inspector and the reference servers accept issues only.

**1. Read the contributing guide**

Each repository sets its own rules, and some close pull requests that have no assigned issue. If a repository has no guide, ask in its channel, such as `#python-sdk-dev`.

**2. Pick an issue**

Look for [`good first issue`](https://github.com/search?q=org%3Amodelcontextprotocol+is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22\&type=issues) or `help wanted`, or open a new one. Ask to be assigned if the guide requires it.

**3. Open a pull request**

For anything larger than a small bug fix, agree on the approach in the issue before you write code.

The [SDK list](https://modelcontextprotocol.io/docs/sdk.md) shows each SDK's [tier](https://modelcontextprotocol.io/community/sdk-tiers.md), which sets its issue triage times.

## Propose a protocol change

Protocol changes go through a [SEP](https://modelcontextprotocol.io/community/sep-guidelines.md). Bug fixes and clarifications [do not need one](https://modelcontextprotocol.io/community/sep-guidelines.md#when-you-need-a-sep).

**1. Discuss the idea**

Raise it in your group's channel. The SEP pull request [must link to that discussion](https://modelcontextprotocol.io/community/sep-guidelines.md#before-you-write).

**2. Build a prototype**

See [Prototype Requirements](https://modelcontextprotocol.io/community/sep-guidelines.md#prototype-requirements). Consider shipping the idea as an [extension](https://modelcontextprotocol.io/extensions/overview.md) where its shape allows.

**3. Find a sponsor**

See [Sponsors](https://modelcontextprotocol.io/community/sep-guidelines.md#sponsors).

**4. Write the SEP**

Follow the [workflow](https://modelcontextprotocol.io/community/sep-guidelines.md#workflow). Without write access, ask your sponsor to open the pull request.

## Other ways to help

* Review open SEPs and draft specification pull requests.
* Reproduce reported bugs.
* Test SDK release candidates against the draft specification.
* Write [conformance](https://github.com/modelcontextprotocol/conformance) scenarios. A Standards Track SEP with observable protocol behavior [needs one](https://modelcontextprotocol.io/community/sep-guidelines.md#conformance-test-requirement) to reach Final.

## Growing your role

To take on a bigger role, see the [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md). [Governance](https://modelcontextprotocol.io/community/governance.md) covers who decides what, and [MAINTAINERS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) lists the current maintainers.

## Ground rules

* The [Code of Conduct](https://modelcontextprotocol.io/community/policies.md#code-of-conduct) applies in every repository, channel and meeting.
* [Disclose](https://modelcontextprotocol.io/community/policies.md#ai-assisted-contributions) any AI assistance in the pull request or issue.
* AI agents must follow [AGENTS.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/AGENTS.md), which limits when they can open issues and pull requests.
* Contributions are [licensed](https://modelcontextprotocol.io/community/policies.md#licensing-and-intellectual-property) under Apache-2.0 for code and specifications and CC-BY-4.0 for other documentation.

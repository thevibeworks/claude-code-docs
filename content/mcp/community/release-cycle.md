> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Release Cycle

> Release milestones and deadlines for SEP authors and SDK maintainers.

MCP specification releases are published every six months, generally on the last Tuesday of March and September.

## Schedule

Each release has an eight-month cycle. Planning for the next release starts **2 months** before the current release is published. [Release managers](https://modelcontextprotocol.io/community/contributor-ladder.md#release-managers) publish the exact milestone dates for each release on the [releases page](https://voting.modelcontextprotocol.io/p/releases) at the start of planning. Milestone intervals are measured in calendar months.

Specification versions use the release date in [`YYYY-MM-DD` format](https://modelcontextprotocol.io/docs/learn/versioning).

![March and September release cycles, each with planning, Core Maintainer review, and stabilization. The cycles overlap by two months, and releases are six months apart.](https://mintcdn.com/mcp/DlhTaFDK8kDED8OR/images/release-cycle-timeline-light.svg?fit=max\&auto=format\&n=DlhTaFDK8kDED8OR\&q=85\&s=6dc770fc8b4f5f5946565b53b831b99b)

Eight-month cycles overlap by two months. Releases are six months apart.

## Milestones

| Milestone | Before release | Outcome |
| - | - | - |
| Planning begins | 8 months | Core Maintainers propose a roadmap and gather feedback from maintainers and working groups. |
| Core Maintainer review opens | 6 months | Priorities are published and scheduled SEP reviews begin. |
| Soft freeze | 2.5 months | Review closes. Included SEPs must be [Final](https://modelcontextprotocol.io/community/sep-guidelines.md#workflow) and merged. |
| Next-cycle planning begins | 2 months | Planning for the following release starts. |
| SDK beta | 1.5 months | Tier 1 SDKs publish betas supporting the frozen specification. |
| Hard freeze | 1 month | Specification changes are restricted to critical fixes. |
| Release | 0 months | The specification, release notes, implementation and migration guidance, and SDK readiness summary are published. |

During planning, Core Maintainers publish priorities for the next six to twelve months in the [roadmap](https://modelcontextprotocol.io/development/roadmap.md), along with dependencies across working groups and SDKs. Proposals that align with the roadmap receive review priority, but a place on the roadmap does not guarantee acceptance or inclusion in a particular release.

### Soft freeze

At soft freeze, **2.5 months** before release, the release scope is fixed:

* Release managers publish the frozen scope and the list of deferred proposals.
* Until hard freeze, only bug fixes, polish, and clarifications within that scope can be merged.
* New features and substantial redesigns move to a later cycle.

### Hard freeze

At hard freeze, **1 month** before release, the specification changes only for critical fixes:

* A critical fix addresses a critical security vulnerability or a defect in correctness or interoperability that blocks the release.
* Each fix follows the [critical fix procedure](#critical-fixes).
* More than half of the [Core Maintainers](https://modelcontextprotocol.io/community/sep-guidelines.md#review-and-acceptance) must approve each fix in a recorded vote.

## SEP review and inclusion

Sponsorship, submission, and finalization follow the [SEP workflow](https://modelcontextprotocol.io/community/sep-guidelines.md#workflow). A working group lead or Core Maintainer submits proposals to the [SEP review queue](https://voting.modelcontextprotocol.io/p/seps). The queue accepts submissions year-round. Submitting a proposal does not guarantee review time or inclusion in a release.

### SEP review queue

Release managers maintain the SEP review queue. Each entry records:

* A link to the proposal
* The sponsoring group and its representative
* The sponsor, if one is assigned
* Whether the request is for formal review or pre-review
* The readiness date, roadmap alignment, and target review cycle

An entry for formal review links to the SEP pull request in the [specification repository](https://github.com/modelcontextprotocol/modelcontextprotocol). This includes [Extensions Track](https://modelcontextprotocol.io/community/sep-guidelines.md#sep-types) SEPs, which are proposed in the specification repository and not in an extension repository. An entry for pre-review can link to an early proposal anywhere, such as a working group or extension repository. That proposal does not need a SEP number or the sponsoring group's approval yet.

A working group lead or Core Maintainer can request a pre-review to discuss a proposal's direction, dependencies, and major concerns before the proposal is complete. A pre-review gives authors feedback but does not approve the proposal or reserve a place in a release.

### Review scheduling

Formal reviews take place at regular Core Maintainer meetings during the review window. Release managers build each meeting agenda from the SEP review queue in this order:

1. Proposals that are ready for formal review come before pre-reviews.
2. Within each of those two groups, roadmap-aligned proposals come first.
3. Among proposals with the same roadmap alignment, the proposal with the oldest readiness date comes first.

Release managers record the reason for any exception to this order in the queue. A proposal that is deferred only because the agenda was full keeps its readiness date. A proposal that was returned for substantive revision receives a new readiness date when it is resubmitted.

### Formal review

![Formal SEP review: the agenda is published 2 weeks before the meeting, reviewers comment on the pull request during the week before the meeting, the proposal is presented at the meeting, and the acceptance vote stays open for 7 calendar days.](https://mintcdn.com/mcp/DlhTaFDK8kDED8OR/images/sep-review-timeline-light.svg?fit=max\&auto=format\&n=DlhTaFDK8kDED8OR\&q=85\&s=de19ca755b0e8ec0c6140dfd1037f4ab)

A formal review takes three weeks, from the published agenda to the end of the vote.

1. **2 weeks before the meeting:** Release managers select ready proposals with the Core Maintainers and publish the agenda and proposal links. They invite each proposal's authors and its working group lead or sponsoring Core Maintainer to the meeting.
2. **1 week before the meeting:** During this week, reviewers leave comments on the pull request. Authors and sponsors respond and identify the questions that need discussion.
3. **At the meeting:** The author, working group lead, or sponsoring Core Maintainer presents the proposal, the remaining questions, and any implementation feedback.
4. **After the presentation:** The sponsor opens the [acceptance vote](https://modelcontextprotocol.io/community/sep-guidelines.md#review-and-acceptance), which remains open for **7 calendar days**.

### Inclusion in a release

A SEP reaches [Final status](https://modelcontextprotocol.io/community/sep-guidelines.md#workflow) when its sponsor has verified all required artifacts, including the specification changes, reference implementation, and any required conformance tests. To be included in a release, a SEP must reach Final and have its pull request merged by the soft freeze date.

The release date does not move for unfinished proposals. SEPs that miss soft freeze are considered for later releases:

* Accepted SEPs keep their status unless a substantial redesign requires another review.
* Proposals awaiting a decision keep their status and return to the SEP review queue.

Inclusion in a later release depends on the proposal's readiness and that cycle's scope. Changes for future releases remain in proposal branches or pull requests until the current release is published.

A freeze applies to everything that is not yet merged when it starts. A SEP that was already accepted, or whose vote was still open at that point, has to follow the freeze like any other change.

The review window applies to all SEP types. Process and Informational SEPs take effect after acceptance and implementation, independently of specification publication. Extensions follow their [publication lifecycle](https://modelcontextprotocol.io/extensions/overview.md#extension-lifecycle).

## SDK deadlines

SDK maintainers should begin implementation as soon as a SEP is accepted. They should report specification ambiguities to the author and sponsor while fixes can still be merged. SDK implementations are not required for a SEP to reach Final status.

[Tier 1 SDKs](https://modelcontextprotocol.io/community/sdk-tiers.md) publish beta versions **1.5 months** before the release and stable versions before the specification is published. The beta gives client and server developers half a month to report issues before hard freeze.

These deadlines cover the features required by the tiering policy, not experimental features or extensions. SDKs in other tiers are encouraged to publish betas on the same schedule.

Beta release notes identify the target specification release, the available functionality, known gaps, and where to report feedback. SDK maintainers work with release managers to keep the public readiness summary up to date with SDK versions, conformance results, gaps, owners, and expected resolution dates.

Release managers escalate a missed beta or stable milestone to the Core Maintainers and the [SDK Working Group](https://modelcontextprotocol.io/community/working-groups/sdk.md) and report it in the release guidance. SDK delays do not postpone the specification release or automatically change an SDK's tier.

## Critical fixes

After hard freeze, the primary release manager coordinates each critical fix through a regular pull request. A critical fix does not need a separate SEP, a sponsor, or a meeting presentation.

1. The primary release manager confirms that the change meets the [hard-freeze criteria](#hard-freeze). The pull request documents the defect, why the fix cannot wait for the next release, the smallest change that fixes the defect, and the effect on SDKs and release artifacts.
2. The primary release manager opens a recorded vote of all eligible Core Maintainers. The vote can take place outside the review window. The primary release manager can shorten the seven-day voting period, but must notify all eligible Core Maintainers of the deadline and the reason.
3. Maintainers of the affected implementations review the change, and the relevant regression and conformance checks are run. If the change alters observable protocol behavior, the conformance tests are updated.
4. After approval and validation, the pull request is merged. The primary release manager records the vote, decision, and validation results, notifies the affected SDK maintainers, and updates the readiness summary and release notes.

If a defect cannot be fixed safely before the release, the affected feature and the changes that depend on it can be removed from the release. Removal follows the same procedure and vote. The rest of the specification is released on schedule.

Security-sensitive details follow the [security disclosure process](https://modelcontextprotocol.io/community/policies.md#reporting-a-vulnerability). The decision and validation record stays in a restricted channel during an embargo and is published when disclosure permits.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
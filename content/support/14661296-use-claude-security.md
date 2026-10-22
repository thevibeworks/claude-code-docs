# Use Claude Security

## Overview

**[Claude Security](https://claude.com/product/claude-security)** is a capability built into Claude that continuously watches your codebases for security vulnerabilities, tracks each finding until it is fixed, and suggests targeted patches for human review. It helps teams find and fix issues that traditional methods often miss.

Claude Security is now available in public beta for users on Enterprise plans.

Learn how to get started and how leading enterprises use the tool here: **[Getting started with Claude Security](https://academy.claude.com/tutorials/getting-started-with-claude-security)**.

Claude Security allows you to:

1. **Scan your codebase holistically** — Claude Security understands how your code fits together, traces data flows across files and across the repositories in a project, and identifies complex, multi-component vulnerabilities and bugs that traditional rules-based scanners cannot detect.

2. **Deep Scan** — Create a project and connect up to eight repositories from GitHub or other Git providers. Claude reads the code, writes a threat model, and runs a deep baseline scan.

3. **Continuous Scanning** —  Claude Security runs an efficient scan when new commits land, and surfaces any new findings for quick remediation.

4. **Add what the code can’t show** — Tell Claude how your code is deployed, who can reach it, and which risks you’ve accepted. Each project keeps this in a threat model, and Claude uses it to decide what to flag and how to rate it.

5. **Validate findings** — Every finding goes through multi-stage verification, with Claude critically reviewing its own findings before they’re surfaced. The result: fewer false positives, less noise.

6. **Review and patch** — Seamlessly move from a finding into a Claude Code session to generate a targeted fix. Resolve vulnerabilities quickly instead of growing a backlog.

7. **Track fixes** — Claude checks open findings against the code that changed and marks them fixed when the fix lands.

8. **Integrate into your workflow** — Read and resolve findings through the Claude Security API or the Claude Security connector (MCP) in Claude and Claude Code, and get a webhook when a new finding is added.

9. **Control access** — Share each project with a Full, Triage, or View role. Admins can decide who can create projects and who can view, triage, or manage all projects with RBAC.

---

## Finding types

Findings fall into these example categories below.

**Injection (SQL, Command, Code, XSS):** Untrusted input changes query structure or gets executed. E.g., `' OR 1=1--, ; rm -rf /`, `<script>` in a comment.

**Injection (XXE, ReDoS):** Parsers or regex abused by crafted input. E.g., XML `<!ENTITY>` reading `/etc/passwd`.

**Path & Network (Path traversal, SSRF, Open redirect):** Input controls file paths, request destinations, or redirects. E.g., `../../etc/passwd`, fetching `http://169.254.169.254/`.

**Auth & Access (AuthN bypass, PrivEsc, IDOR/BOLA, CSRF, Race):** Access checks missing, skippable, or racy. E.g., `GET /orders/123` returns someone else's order.

**Memory Safety (Buffer/integer overflow, UAF, unsafe misuse):** Input writes past bounds, wraps arithmetic, or hits freed memory. Mostly C/C++/Rust `unsafe`.

**Cryptography (Timing leaks, algorithm confusion, weak primitives):** Secret-dependent branches, JWT `alg=none`, or MD5/SHA-1/DES/ECB in security paths.

**Deserialization (Arbitrary type instantiation):** Untrusted bytes drive object construction — pickle, Java `readObject`, YAML load. Often equals RCE.

**Protocol & Encoding (Cache safety, encoding confusion, length-prefix trust):** Layers disagree or trust declared sizes. E.g., cache poisoning via `Host` header.

---

## Severities

Severity is assigned per finding based on how exploitable it is in your codebase, not the category itself—so the same category can land at different severities in different repos. Claude uses the project’s threat model to assess the severity.

| **Severity** | **Criteria**                                                                                                                                                      | **Typical example**                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Critical     | Exploitable over the network by anyone, with no login, no action by a victim, and no special conditions. It lets the attacker both read and change data.          | Unauthenticated remote code execution in an internet-facing service.       |
| High         | Serious impact, but short of Critical: the attacker needs a login or a victim's action, or the damage is partial (for example, data can be read but not changed). | SQL injection behind a login that lets an attacker read and change data.   |
| Medium       | Limited impact (for example, a small amount of non-sensitive data), with one realistic precondition such as a login.                                              | SQL injection behind a login that exposes only a few non-sensitive fields. |
| Low          | Limited impact, and needs a login or network proximity plus special conditions outside the attacker’s control.                                                    | Timing side-channel requiring network proximity and thousands of requests. |

---

## Finding structure

Each finding contains the following fields:

- Title — short descriptive name of the finding

- Severity — Critical / High / Medium / Low

- Category — finding type, with its CWE ID when one applies

- Location — file path and line range, linked to the source. A finding can cite several files and repositories.

- Status — Open or Resolved, with the date it was found.

- Assignee — the person the finding is assigned to, if any

- What Claude found — description of what the finding is and why it matters. It can include a diagram of the attack path.

- How to fix — guidance on how to resolve it

- Evidence — the files and line ranges Claude cites, grouped by repository, with the branch and commit that were scanned

- How the attack works — how an attacker would reach and exploit the issue

- Why Claude believes it — Claude’s assessment, covering the exploit scenario, its preconditions, and the impact

- History — every change to the finding, newest first

- Shown only if the finding was resolved:

  - Resolution — Marked fixed, Fixed by a merged pull request, or Dismissed as a false positive, an accepted risk, a duplicate, or for another reason

  - Triage note — optional

---

## Troubleshooting

### The security page keeps redirecting to "Install GitHub App"

The claude.ai/security page runs a per-user check against your own connected GitHub account, so this can fail for you even though the organization-wide installation is working for others. There are a few potential causes:

- **No GitHub account connected in Claude.** Go to[**Customize > Connectors**](https://claude.ai/customize/connectors) to check this.

- **The connected GitHub account isn’t a member of the GitHub organization** where the app is installed. Connect the account that belongs to that organization.

- **SSO isn't authorized for that organization.** If your GitHub organization requires SSO, you must authorize the Claude app for it separately. Follow the steps in **[Use the GitHub integration](https://support.claude.com/en/articles/10167454-use-the-github-integration#h_e169a34a57)**.

- **Your GitHub organization's IP allow list is blocking the check.** GitHub's "Enable IP allow list configuration for installed GitHub Apps" setting covers traffic from the App itself, such as Code Review, but it doesn't cover this per-user check. To allow it, manually add 160.79.104.0/21 as an organization-level allow list entry. For the full list of ranges, see **[IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)**.

---

## Frequently asked questions

### Getting started

**What do I need before I can use Claude Security?**

An active Claude Enterprise plan, a premium seat for each user, and usage credits enabled for consumption billing. An owner enables Claude Security in **[Organization settings > Claude Security](https://claude.ai/admin-settings/claude-security)**. See the **[getting started guide](https://academy.claude.com/tutorials/getting-started-with-claude-security)** for setup steps.

**How do I give Claude Security access to my repositories?**

For GitHub.com and GitHub Enterprise Server, an owner installs the **[Claude GitHub App](https://github.com/apps/claude)** and grants it access to the repositories you want to scan. For other Git providers, such as GitLab and Bitbucket, you need the repository’s address and an auth token.

**Can I scan repositories that aren’t on GitHub?**

Yes. Projects can be created with repositories hosted on GitHub.com and GitHub Enterprise Server, or repositories hosted on other Git servers with an auth token (including publicly accessible self-hosted Git servers).

**Which IP addresses do I need to allow?**

Use the **[Anthropic guide for IP address allowlisting](https://platform.claude.com/docs/en/api/ip-addresses)**. If you use GitHub Enterprise Server or another Git provider, your instance must allow inbound traffic from these IP addresses so Claude Security can reach your repositories.

**Does Claude Security support Zero Data Retention (ZDR)?**

No. Anthropic may retain data where required by law or to address Usage Policy violations.

**What happens to my existing projects with the latest update?**

Existing projects keep running as they do today and are still available from the Claude Security home page. New projects use the new experience.

**Can I migrate my existing projects?**

Yes, if you own the project. Open it and click "Migrate project", or click "Migrate your projects" on the Claude Security home page to migrate every project you own. Claude Security creates a new project, copies the findings to it, and archives the original. Members, webhooks, excluded directories, scan history, and scheduled scans aren't copied. GitHub Enterprise projects can't be migrated.

### Continuous monitoring

**How long does the first scan take?**

Depending on the size of the repositories, the baseline scan may take several minutes or hours. You can leave the page while it runs. If you have enabled email notifications for Claude Security, you will receive an email when your project’s scan completes and it has new findings.

**How long does a follow-up scan take?**

Scan time varies based on the repository and the agent’s actions.

**How often does Claude scan after the baseline scan?**

Claude checks for new commits and scans changes regularly, based on their risk and complexity. There is no fixed schedule.

**Why can two scans of the same code return different results?**

Scans are stochastic by design. Unlike traditional static analyzers, Claude Security uses an agent that adapts its analysis to each run, reasoning over code context rather than applying fixed pattern matches. This enables the depth of analysis needed to catch logic-level vulnerabilities.

**How should I set up a large repository or monorepo?**

Set a folder scope on the repository rather than scanning the full repository, and exclude folders you don’t need covered. Claude can still pull context from the rest of the codebase as needed.

**How many repositories can a project have?**

Up to eight. A repository can be in scope, so Claude scans it and reports findings, or used for context only, so Claude reads it during scans but reports no findings in it. Both count toward the limit. Manage a project's repositories on its Resources tab.

**How do I tell Claude about my environment?**

Open the project’s Knowledge tab to edit the threat model and add documents such as architecture docs. Claude uses them to decide what to flag and how to rate it.

**Which models does Claude Security use?**

Claude Security scans are powered by Claude Mythos model. Users receive findings without direct model access. Each project’s chat with Claude uses a model your team picks from the ones your organization allows. Certain subcomponents of Claude Security may use other models when Mythos-class reasoning is not required, for example to enumerate a project directory.

### Findings and fixes

**How is severity assigned, and can I change it?**

Claude rates each finding against the project’s threat model, which your team can edit and correct.

**What if a finding describes an attack that isn’t possible in my environment?**

Claude writes the threat model from your code, so it can miss deployment context and the patterns your company has accepted. In the project’s chat, tell Claude why the finding is wrong and ask it to update the threat model. Claude uses the threat model to decide what to flag and how to rate it.

**How do I fix a finding?**

Click “Fix” on a finding to open Claude Code and fix that specific vulnerability. Without **[Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)**, you copy a prompt into your own Claude Code.

**How does fix tracking work?**

Claude re-checks findings when the code changes on the repository. A finding marked fixed reopens automatically if Claude later finds the issue again.

**What happens when I dismiss a finding?**

Dismissed findings will not reappear in future scans. You can dismiss a finding as a false positive, an accepted risk, a duplicate, or for another reason, and add a triage note.

### Integrations and notifications

**How do I export findings to my own tools?**

To export findings into your own tracking and notification systems, use the Claude Security API, the Claude Security connector, or webhooks.

**How do I use the Claude Security API?**

Create a personal access token under Claude Security settings. A token acts as you: it can see and change only what you can. With the API, you can list and read projects and findings, resolve and reopen findings, and create and manage projects and their repositories.

**What can the Claude Security connector (MCP) do?**

With the Claude Security connector, Claude and Claude Code can list and read your projects and findings and resolve or reopen a finding when you ask.

**How do I get notified when there is a new finding?**

Create a webhook under Claude Security settings to push new-finding events into your own systems, such as Slack or Jira.

### Access and sharing

**How do admins control who can use Claude Security?**

Admins can decide which RBAC roles can create projects and which can view, triage, or manage all projects by configuring the capabilities in **[custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

**How do I share a project, and what can each role do?**

In a project, click “Share” to give members a role: Full (manage findings, settings, and who has access), Triage (view findings, update their status, and start fixes), or View. You can also share a project with your whole organization.

### Pricing

**How much does Claude Security cost?**

Claude Security is charged at direct token cost only. There is no additional platform fee. Usage covers scans and other work Claude Security does in a project: writing a threat model, the project chat, and checking fixes.

**How do I control and track what Claude Security costs?**

You can set a separate spend limit for Claude Security. Open Usage in a project’s settings to see its cost for the month to date and per day.

**Is there a launch offer for the updated Claude Security?**

Yes, eligible Claude Enterprise organizations receive free usage credits up to $25,000 a month, for two months, through Dec 31, 2026. Full **[launch offer terms](#h_07eed9f41c)** below.

**Does the launch offer also apply to the old experience?**

No, the launch offer only applies to projects created with the new experience.

### Claude Security plugin for Claude Code

**What is the Claude Security plugin for Claude Code?**

The Claude Security plugin for Claude Code is a separate feature, based on the same technology as Claude Security. It is available for users who wish to directly integrate the scanner into their workflows without relying on Anthropic’s hosted agent infrastructure, who have Zero Data Retention (ZDR) requirements, or who need model access through a third-party provider. Learn more here: **[Scan your codebase for vulnerabilities](https://code.claude.com/docs/en/claude-security)**.

**Does the Claude Security plugin for Claude Code use the same model?**

Not necessarily. The plugin uses whichever models are available in your Claude Code account.

**Scope of use:** You will only use Claude Security to scan code that you or your company owns and to which you or your company holds all necessary rights to scan. You will not use Claude Security to scan code owned by or licensed from third parties, including but not limited to open source projects or repositories other than those included in your company's codebase(s).

## Claude Security launch offer terms

**Who is eligible:** Claude Enterprise organizations, including Claude Enterprise purchased through AWS Marketplace.

**What you get:** Up to $25,000 in promotional credits for Claude Security usage in each of two consecutive months. Each month runs from your organization's start date to the same date the following month. Unused credits from a month don't carry over.

**How to get it:** No sign-up is needed. Credits apply automatically to usage in the new Claude Security. Usage in projects from the earlier version isn't covered until they're migrated.

**When it starts:** Organizations that already have Claude Enterprise start on October 21, 2026. Organizations that sign up for Claude Enterprise after that date start on the day they sign up. The two months run whether or not your organization uses Claude Security.

**When it ends:** The offer ends at the end of the day on December 31, 2026 (UTC), even if your two months haven't finished. Organizations that sign up after November 1, 2026 won't get two full months.

**How credits apply:** Credits are used before your organization's committed spend or usage credits, and are separate from any prepaid usage credits. After the credits are used or the offer ends, Claude Security usage is charged at direct token cost.

**Where to see it:** Organization admins can see the promotional balance in **[Organization Settings > Usage](https://claude.ai/admin-settings/usage)**, under **Services**, or in **Organization Settings > Claude Security**, under **Spend limit**.

The **[Claude Promotional Credit Offer Terms](https://www.anthropic.com/legal/promotion-credit-terms)** also apply, including when credits can be forfeited and when the offer can change. If they differ from this article on this offer, this article controls.
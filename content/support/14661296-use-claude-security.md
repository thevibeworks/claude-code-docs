# Use Claude Security

## Overview

Claude Security is a capability built into Claude that scans codebases for security vulnerabilities and suggests targeted patches for human review. It helps teams find and fix issues that traditional methods often miss. Learn more **[about Claude security](https://claude.com/product/claude-security)**.

Claude Security is now available in public beta for users on Enterprise plans.

Claude Security allows you to:

1. **Scan your code in parallel** — Claude Security understands context, traces data flows across files, and identifies complex, multi-component vulnerability patterns that traditional scanners might not detect.

2. **Validate findings** — Every finding goes through multi-stage verification, with Claude challenging its own results before surfacing them. The result: more real issues reported and fewer false positives.

3. **Review and patch** — Move from a finding into a Claude Code session to review the proposed fix. Resolve vulnerabilities quickly instead of growing a backlog.

Learn how to get started and how leading enterprises use the tool here: **[Getting started with Claude Security](https://claude.com/resources/tutorials/getting-started-with-claude-security)**.

---

## Enable Claude Security

An organization owner can enable Claude Security by going to **[Organization settings > Claude Security](https://claude.ai/admin-settings/claude-security)** and switching the **Turn on for your organization** toggle on.

---

## Finding types

Finding falls into these example categories below.

**Injection (SQL, Command, Code, XSS):** Untrusted input changes query structure or gets executed. E.g., ' OR 1=1--, ; rm -rf /, <script> in a comment.

**Injection (XXE, ReDoS):** Parsers or regex abused by crafted input. E.g., XML <!ENTITY> reading /etc/passwd.

**Path & Network (Path traversal, SSRF, Open redirect):** Input controls file paths, request destinations, or redirects. E.g., ../../etc/passwd, fetching <http://169.254.169.254/>.

**Auth & Access (AuthN bypass, PrivEsc, IDOR/BOLA, CSRF, Race):** Access checks missing, skippable, or racey. E.g., GET /orders/123 returns someone else's order.

**Memory Safety (Buffer/integer overflow, UAF, unsafe misuse):** Input writes past bounds, wraps arithmetic, or hits freed memory. Mostly C/C++/Rust unsafe.

**Cryptography (Timing leaks, algorithm confusion, weak primitives):** Secret-dependent branches, JWT alg=none, or MD5/SHA-1/DES/ECB in security paths.

**Deserialization (Arbitrary type instantiation):** Untrusted bytes drive object construction — pickle, Java readObject, YAML load. Often equals RCE.

**Protocol & Encoding (Cache safety, encoding confusion, length-prefix trust):** Layers disagree or trust declared sizes. E.g., cache poisoning via Host header.

---

## Severities

Severity is assigned per finding based on exploitability in your codebase, not the category itself—so the same category can land at different severities in different repos.

| **Severity** | **Criteria**                                                                                                                | **Typical example**                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| High         | Exploitable by an unauthenticated remote attacker against a default deployment, with no meaningful preconditions            | Unauthenticated command injection in a public API endpoint                |
| Medium       | Exploitable behind authentication, or needs 1–2 realistic preconditions (specific role, known identifier, user interaction) | SQL injection behind auth requiring knowledge of table schema             |
| Low          | Needs 3+ preconditions, local-only access, or lacks a concrete demonstrated attack path                                     | Timing side-channel requiring network proximity and thousands of requests |

---

## Finding structure

Each finding contains the following fields:

- Title — short descriptive name of the finding

- Details — description of what the finding is and why it matters

- Location — file path and line number, linked to the source

- Impact — what could go wrong if this isn’t addressed

- Reproduction steps — ordered list of steps to reproduce or observe the issue

- Recommended fix — guidance on how to resolve it

- Severity — HIGH / MEDIUM / LOW

- Status — Open / Dismissed / Resolved

- Category — finding type

- Repository — repository identifier

- Branch — branch name the finding was produced against

- Date created — date the finding was created

- Shown only if the finding was dismissed:

  - Dismissal reason

  - Dismissal note — optional

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

- **Product price and cost** — Scans are charged at direct token cost only. There is no additional platform fee for Claude Security.

- **Scan length** — Scan time varies based on the repository and the agent's actions.

- **Severity configuration** — as of today, severity is not configurable.

- **Non-GitHub repositories** — Only repositories hosted on GitHub can be scanned today.

- **No Zero Data Retention (No ZDR)** — Anthropic may retain data where required by law or to address Usage Policy violations.

- **Scan consistency** — Scans are stochastic by design. Unlike traditional static analyzers, Claude Security uses an agent that adapts its analysis to each run, reasoning over code context rather than applying fixed pattern matches. This enables the depth of analysis needed to catch logic-level vulnerabilities.

- **Exporting findings** — You can copy findings, download them as CSV or Markdown, or push them to your own tracking and notification systems via per-project webhooks. See the “getting started” guide.

- **Feedback** — Please share your feedback using the in-product feedback icon on the right.

- **IP addresses for Github** — Use the following Anthropic guide for IP addresses allowlisting: **[IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)**.

**Scope of use:** You will only use Claude Security to scan code that you or your company owns and to which you or your company holds all necessary rights to scan. You will not use Claude Security to scan code owned by or licensed from third parties, including but not limited to open source projects or repositories other than those included in your company's codebase(s).
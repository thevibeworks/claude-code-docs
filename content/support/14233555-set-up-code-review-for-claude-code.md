Title: Set up Code Review for Claude Code

URL Source: https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code

Markdown Content:
Code Review analyzes your GitHub pull requests and posts findings as inline comments on the lines of code where it found issues. A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and regressions.

This article covers how to enable Code Review, configure review triggers, customize what gets flagged, and troubleshoot common setup issues.

## How Code Review works

Once an organization enables Code Review, it can trigger automatically when a pull request opens, on every push, or only when someone manually requests a review. When a review runs, multiple agents analyze the diff and surrounding code in parallel. Each agent looks for a different class of issue, then a verification step checks results against actual code behavior to filter out false positives.

Findings are deduplicated, ranked by severity, and posted as inline comments on the specific lines where issues were found. If no issues are found, Claude posts a short confirmation comment on the PR. Reviews don’t approve or block your PR, so existing review workflows stay intact.

Reviews scale in cost with PR size and complexity, completing in 20 minutes on average.

### Severity levels

Each finding is tagged with a severity level:

**Marker****Severity****Meaning**
🔴Normal A bug that should be fixed before merging
🟡Nit A minor issue, worth fixing but not blocking
🟣Pre-existing A bug that exists in the codebase but wasn’t introduced by this PR

Findings include a collapsible extended reasoning section you can expand to see why Claude flagged the issue and how it verified the problem.

### What Code Review checks

By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage. You can expand what it checks by adding guidance files to your repository.

## Set up Code Review

The steps below cover setup for repositories on github.com. If your repositories are on a self-hosted GitHub Enterprise Server (GHES) instance, see **[Claude Code with GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server)** for the full setup guide.

Owners and Primary Owners of Team and Enterprise plans can enable Code Review once for the organization and select which repositories to include. In addition to an owner role within your Claude organization, you’ll need permission to install GitHub Apps in your GitHub organization.

To verify setup, open a test PR. If you chose an automatic trigger, a check run named **Claude Code Review** should appear within a few minutes. If you chose Manual, comment “@claude review” on the PR to start the first review.

## Choose a review trigger

After setup, the **Code Review** section shows your repositories in a table. For each repository, choose when reviews run:

The repositories table also shows the average cost per review for each repo based on recent activity.

## Manually trigger reviews

Comment “@claude review” on a pull request to start a review and opt that PR into push-triggered reviews going forward. This works regardless of the repository’s configured trigger.

For the comment to trigger a review:

If a review is already running, the request is queued until the in-progress review completes.

## Customize reviews

Code Review reads two files from your repository to guide what it flags. Both are additive on top of the default correctness checks.

### CLAUDE.md

Code Review reads your repository’s CLAUDE.md files and treats newly introduced violations as nit-level findings. If your PR changes code in a way that makes a CLAUDE.md statement outdated, Claude flags that the docs need updating too.

Claude reads CLAUDE.md files at every level of your directory hierarchy, so rules in a subdirectory’s CLAUDE.md apply only to files under that path.

### REVIEW.md

Add a REVIEW.md file to your repository root for review-specific rules. Use it to encode:

Claude auto-discovers REVIEW.md at the repository root. No configuration is needed.

## Pricing and usage

Code Review is billed based on token usage. Each review averages $15–25 in cost, scaling with PR size, codebase complexity, and how many issues require verification.

Code Review usage is billed separately through usage credits and doesn’t count against your plan’s included usage. The review trigger you choose affects total cost:

Costs appear on your Anthropic bill regardless of whether your organization uses AWS Bedrock or Google Vertex AI for other Claude Code features.

To set a monthly spend cap, go to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)** and configure the limit for the Claude Code Review service.

Monitor spend via the weekly cost chart in the analytics dashboard or the per-repo average cost column in admin settings.

### View usage

## Troubleshooting

### Repositories don’t appear after installing the GitHub App

If you’ve installed the Claude GitHub App but your repositories don’t appear in the admin panel:

### Code Review doesn’t start on a new PR

If no check run appears after opening a PR:

### GitHub Enterprise Cloud with IP restrictions

### GitHub Enterprise Server (self-hosted)

Common GHES setup issues:

## Frequently asked questions

### Is Code Review available as a capability when creating a custom role?

No, Code Review is not available to add to a **[custom role](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)** at this time.

## Related resources

* * *

Related Articles

[Automated Security Reviews in Claude Code](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[Claude Code on the web](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)[Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)

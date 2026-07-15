# Use the Claude Agent SDK with your Claude plan

**Update June 15:** We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits. The previously announced monthly credit, which would have been available to eligible claimants in connection with these changes, isn't available. We’re working to update the plan to better support how users build with Claude subscriptions. When we have an update, we'll share it before anything takes effect.

---

**The content below reflects the page before June 15. It's preserved for reference but is no longer taking effect on June 15.**

Claude subscription plans are now eligible to receive a monthly Agent SDK credit. This credit covers Claude Agent SDK usage, the `claude -p` command, and third-party apps built on the Agent SDK. This article explains what the credit covers, how it works, and how to claim it.

Available on Pro, Max, Team, and Enterprise plans starting on June 15, 2026. Claude Platform accounts using an API key don’t receive a credit. Pay-as-you-go billing continues as before.

## What’s changing

Starting **June 15, 2026**, Claude Agent SDK and `claude -p` usage no longer counts toward your Claude plan’s usage limits. Your subscription usage limits stay the same and stay reserved for interactive use of Claude Code, Claude Cowork, and Claude.

To support Agent SDK use, eligible Pro, Max, Team, and Enterprise plan users can claim a separate monthly credit. The credit applies only to Agent SDK usage and refreshes with your billing cycle.

## Monthly credit by plan

| **Plan**                                | **Monthly credit** |
| --------------------------------------- | ------------------ |
| Pro                                     | $20                |
| Max 5x                                  | $100               |
| Max 20x                                 | $200               |
| Team (Standard seats)                   | $20                |
| Team (Premium seats)                    | $100               |
| Enterprise (usage-based)                | $20                |
| Enterprise (seat-based Premium seats\*) | $200               |

*Members of seat-based Enterprise plans on Standard seats aren’t eligible to claim the Agent SDK monthly credit.

---

## What the credit covers

The Agent SDK monthly credit applies to:

- Claude Agent SDK usage in your own projects (Python or TypeScript)

- The `claude -p` command in Claude Code (non-interactive mode)

- The Claude Code GitHub Actions integration

- Third-party apps that authenticate with your Claude subscription through the Agent SDK

The credit doesn’t apply to:

- Interactive Claude Code in the terminal or IDE

- Claude conversations on the web, desktop, or mobile apps

- Claude Cowork

- Other features that draw from usage credits

---

## How the credit works

**Per-user, not pooled.** Credits belong to individual accounts. They can’t be shared or pooled across teammates.

**Refreshes monthly.** Your credit resets at the start of each billing cycle. Unused credits don't roll over to the next billing cycle.

**One-time opt-in.** You claim your credit through your Claude account once. After that, it refreshes automatically each cycle.

**Drains first.** Agent SDK usage draws from your monthly credit before any other source.

**Past the credit, usage moves to usage credits.** When your monthly credit runs out, additional Agent SDK usage flows to usage credits at standard API rates—but only if you've enabled usage credits. If usage credits aren't enabled, Agent SDK requests stop until your credit refreshes.

---

## What stays the same

This change doesn’t affect:

- **Subscription usage limits.** Your plan usage limits haven’t changed as part of this update.

- **Interactive Claude Code.** Using Claude Code in the terminal or your IDE continues to use your subscription usage limits exactly as before.

- **Claude conversations.** Web, desktop, and mobile chat continue to use subscription usage limits.

- **API key users.** If you use the Agent SDK with an API key from the Claude Platform, nothing changes. Pay-as-you-go billing continues, and you don’t receive an Agent SDK monthly credit.

---

## For Team and Enterprise admins

If you administer a Team or Enterprise account, here’s what to know:

**Credits are per-user.** Each eligible user on your team claims their own credit. Credits can’t be pooled, transferred, or shared across the organization.

**Production automation at scale.** The Agent SDK monthly credit is sized for individual experimentation and automation. Teams running shared production automation should use Claude Platform with an API key for predictable pay-as-you-go billing.

**What you need to do.** Nothing right now. Eligible users on your team will receive an email with details and instructions to claim their credit before June 15, 2026.
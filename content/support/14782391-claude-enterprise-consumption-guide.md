# Claude Enterprise consumption guide

Claude Enterprise gives your organization access to powerful AI across chat, Claude Code, and Claude Cowork. With that access comes the responsibility of managing consumption effectively—ensuring your team gets maximum value while keeping usage predictable and within budget.

This guide walks Enterprise admins through the key levers available to control and optimize token consumption: setting spend caps, configuring role-based access controls, educating users, and choosing the right model and effort level for the right task.

---

## Why consumption management matters

Claude Enterprise is priced on a per-seat, usage-based model. Your org's consumption pool is shared across all users, and some surfaces—particularly Claude Code and Cowork—consume tokens at a significantly higher rate than standard chat.

Admins who proactively configure spend limits and educate users can reduce waste and ensure that high-value use cases get the capacity they need.

---

## Understanding token intensity across surfaces

| **Surface**   | **Token intensity and what drives it**                                                                                                                         |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core Chat     | Lower intensity. Standard back-and-forth conversation, summarization, drafting, and Q&A. Token usage scales with message length and conversation history.      |
| Claude Code   | Higher intensity. Each coding session includes system prompts, file context, tool calls, and multi-turn reasoning—more tokens per session than chat.           |
| Claude Cowork | Higher intensity. Agentic workflows, multi-step task execution, and Skills generate significant intermediate token usage that may not be visible to end users. |

**Admin tip: Set expectations with your team**

Users running Claude Code or Cowork workflows may not realize how token-intensive their sessions are. A single Cowork task or Claude Code debug session can consume many more tokens than chat. Include this context in any user onboarding you send.

---

## Role-based access controls

Role-based access controls (RBAC) let you group users and manage their access to Claude surfaces and consumption budgets as a unit rather than individual by individual. This is the most scalable way to govern usage in larger organizations.

### How to structure groups

Think about groups in terms of job function and use case, not organizational hierarchy. A few principles:

- Create groups that map to distinct usage patterns, not org chart boxes. "Engineering" and "Sales" are more useful than "North America" and "EMEA" for consumption management.

- Limit group proliferation. More than 8–10 groups becomes hard to manage. Start with 4–6 and split only if usage patterns clearly diverge.

- Use groups to gate access to high-intensity surfaces. For example: only members of the "Engineering" group can access Claude Code; other users see Chat and Cowork only.

- Assign group-level spend caps as a starting point, then override at the user level for outliers (e.g., a non-technical PM who needs Claude Code for a specific project).

### Group spend management

Once groups are configured:

- Review group consumption weekly during initial rollout, monthly thereafter.

- When a group consistently approaches its cap, investigate before automatically raising it—the right response might be model guidance (use Sonnet instead of Opus) rather than more budget.

- Consider assigning a "group owner" in each department who is responsible for reviewing usage and fielding questions from their team. This distributes the admin burden and puts someone with business context in the loop. Please note, this would entail providing these individuals admin rights, which may not be desired.

**Governance tip: Surface access as a first gate**

Before worrying about token-level limits, make sure the right people have access to the right surfaces. Giving everyone Claude Code and Cowork access on day one is the fastest way to generate unexpected consumption. Roll out higher-intensity surfaces in waves, starting with the teams most likely to use them productively.

---

## Set spend limits

Spend limits are your primary tool for controlling consumption. Claude Enterprise lets admins set limits at three levels: the organization level, the group level (with RBAC), and the individual user level. **Our recommended approach is to start with RBAC group-level limits and per-user limits**—these give you precise, targeted control without the risk of cutting off your entire org if a limit is hit.

### Org-level spend limits

The org-level limit is available as a hard ceiling across all users and surfaces, but use it carefully: hitting it affects everyone simultaneously, which can be disruptive. Most admins find that managing consumption at the group and user level gives them better outcomes with less operational risk.

### Group spend limit

Group spend limits let you assign a per-user monthly spend limit to an entire group, so every member of that group inherits the same limit without setting it individually. This is the most scalable way to manage consumption in mid-to-large orgs, and it's where admins should start.

Note the following precedence rules:

- **Individual limits always override group limits**, regardless of which is higher.

- **If a user belongs to multiple groups with different limits**, the **Multi-group spend limit** setting under **Spending defaults** controls whether the higher or lower limit applies. The seat-type default limit is included in this comparison.

- **Org-wide limits remain the hard ceiling.**

- **No limit anywhere = no limit.** If a member has no individual limit and none of their groups have a limit, their spend isn't capped.

**How to configure:** Organization settings → Usage → By group. Set limits to either a specific dollar amount or "Unlimited."

### User-level spend caps

User-level caps let you set consumption limits for individual accounts. These are essential for organizations where usage varies significantly across roles—a developer using Claude Code daily has very different needs than a marketer using chat for copywriting.

**Best practices for user-level caps:**

- Define consumption tiers based on role type before rollout. A tiered structure—e.g., light, standard, power—makes it easier to assign and adjust caps consistently.

- Start conservatively. It's easier to increase a cap based on a user's request than to walk back an overage conversation.

- Give power users (engineers, data scientists, researchers) higher or uncapped individual limits, but offset this by ensuring they use the right Claude model for the right task.

- Monitor individual usage reports monthly to identify outliers—both users consistently hitting their cap (may need more) and users consuming very little (may not be activated yet).

**Recommended starting points**

| **User type**   | **Code** | **Cowork** | **Chat** |
| --------------- | -------- | ---------- | -------- |
| Power (Top 10%) | $500     | $100       | $90      |
| Typical (Mean)  | $215     | $40        | $30      |
| Light (Median)  | $40      | $10        | $5       |

**These figures are rough planning estimates. Actual consumption will vary based on your team's size, workflows, and usage patterns.*

---

## Model selection guidance

One of the most impactful things an admin can do is set clear guidance for users on which model to use for which tasks. Model choice has a direct and significant impact on token consumption—Opus can consume several times more tokens than Sonnet for the same task.

Effort level is a second consumption lever. Users can choose how much thinking Claude applies to each response, and higher effort levels consume more tokens than lower ones. Encourage users to reserve Max effort for only the most demanding tasks and to use lower effort for routine tasks.

### The right model for the right task

| **Model**     | **Best for**                                      | **Token intensity** | **Recommended use**                                                                                         |
| ------------- | ------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------- |
| Claude Fable  | Days-long agentic coding work and reasoning tasks | Very High           | Reserve for your highest-value, most complex agentic work. Premium pricing and faster usage draw than Opus. |
| Claude Opus   | Complex reasoning, research, multi-step tasks     | High                | Reserve for power users or specific workflows only                                                          |
| Claude Sonnet | Everyday tasks, writing, analysis, Q&A            | Moderate            | Default model for all users—set as your org-wide default (see below)                                        |
| Claude Haiku  | Simple lookups, summaries, fast responses         | Low                 | High-volume, lightweight automation tasks                                                                   |

### Set your organization's default model (beta)

Beyond guiding users toward the right model, you can set the model that new conversations start with for everyone in your org. This is one of the most direct consumption levers available—the default shapes what the majority of users run day to day.

You have two options:

- **Anthropic recommended** — automatically updates as new models ship, so your org always starts on our current recommended general-purpose model with no manual upkeep.

- **Choose your own** — sets a specific model as the org default and holds it there until you change it. Use this when you want to standardize on a known model for consumption predictability (for example, defaulting to Sonnet rather than Opus).

This setting applies to chat and Cowork only. Claude Code model defaults are managed separately through managed settings.

You can also set model defaults by role through Custom Roles, so different groups can start on different models—for example, defaulting your engineering group to one model and the rest of the org to another. This pairs naturally with the RBAC groups you've already configured (see Section 2).

**How to configure:** Organization settings → Models.

**Note:** Users' current model selection for new conversations may be cleared, so they'll pick up the org default on their next conversation.

### Manage model access for your organization

Beyond setting a default, you can restrict which models are available at all—a firmer lever than guidance alone. This works at two levels:

- **Organization level:** each model is enabled or disabled for everyone, including Owners and Admins. Disabling a model here removes it from every picker org-wide.

- **Custom role level:** for members on Custom roles, each role grants access to a *subset* of what's enabled at the org level. A role can't grant a model the org has disabled — the org setting is always the ceiling.

**Note:** Haiku models are always available to every member and can't be disabled, so there's always a fallback model.

If a member belongs to multiple groups with different custom roles, access is **additive** — they get every model any of their roles grants (as long as it's enabled org-wide).

**Capping effort level by role**

Beyond restricting which models a role can use, you can cap the **maximum effort level** members on that role can select per model — a more granular version of the effort guidance already covered above. This only applies to Custom roles, not at the org level. If a member has multiple roles, the highest effort cap across those roles wins.

**Admin tip: Pair model + effort restrictions**

If model guidance (the "Sonnet is your default" messaging) isn't landing and you're still seeing heavy Opus consumption, restricting Opus access to specific roles—or capping effort to Medium/High instead of Max for non-power-user roles—is the next lever. Reserve full access for the roles where deep reasoning actually pays off.

**Where this applies**

Model access and effort restrictions are enforced in chat (web, desktop, mobile), Claude Cowork, Office Agents, and Claude Code (CLI 2.1.199+—earlier versions still show restricted options but requests using them are rejected). Claude in Chrome, Claude Design, and Claude Security don't support this yet.

**How to configure:** Organization settings → Roles → select a role → Models tab. Set model access, an optional effort cap per model, and an optional role-level default model. To manage configuration across the org, go to **Organization settings → Models**.  More details in **[Manage model access for your organization](https://support.claude.com/en/articles/15694740)**.

### Admin configuration recommendations

- If you have high-volume, low-complexity workflows (e.g., summarizing support tickets, generating first-draft emails), evaluate whether Haiku is a better fit—it can significantly reduce consumption for these use cases.

- Periodically audit which models your users are actually selecting. If most of your consumption is on Opus, that's a signal that your model guidance isn't landing.

### What to tell your users about model choice

**Sonnet is your daily driver.** It's fast, highly capable, and is designed for the vast majority of tasks—writing, analysis, coding help, and Q&A.

**Opus is for the harder, more complex work.** Use it when you're working on a genuinely complex multi-step problem, or when quality matters more than speed.

**When in doubt, start with Sonnet.** You can always switch the model mid conversation to Opus if you need more depth.

---

## Using org preferences to shape user behavior

Org Preferences let admins inject standing guidance into every Claude conversation across your organization—effectively giving Claude a system prompt that reflects your team's norms, best practices, and guardrails. This is a high-leverage tool for shifting user behavior without adding friction, because the guidance shows up in-product at the moment of use rather than in documentation users have to go find.

A few ways you can use Org Preferences to manage consumption and usage patterns:

- **Nudge-against token-intensive output formats**. If you've noticed proliferation of a particular artifact type (e.g., HTML dashboards being shared in cross-functional threads where a simpler format would do), you can instruct Claude to confirm with the user before generating one. This adds a lightweight check without removing the capability entirely.

- **Point users to internal resources.** Reference your team's wiki, best-practices docs, or usage guidelines directly in the preference. Claude will surface them when relevant—steering users toward the right internal context instead of reinventing it each time.

- **Reinforce model selection norms.** Remind Claude (and by extension, users) that Sonnet is the default and Opus is reserved for specific workflows. This complements user education without requiring everyone to internalize it up front.

---

## Tracking usage and spend

### Analytics page

The Analytics page within the user menu (**claude.ai/analytics**) is the fastest way to get a read on your org. It shows weekly active users, seat utilization, top connectors, total spend (MTD/QTD/YTD), spend by model, and a top-10 users-by-spend leaderboard. Product-specific views for Claude.ai, Claude Code, and Cowork break down activity for each surface. **[Learn more](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)**.

### Spend report CSV export

If you need a one-off detailed breakdown, you can export a per-user, per-model spend report as a CSV from **Analytics → All Activity → Spend → Export Spend**. Choose MTD, last month, last 90 days, or a custom range up to 90 days back. The CSV includes user email, user ID, account UUID, product, model, request count, prompt and completion tokens, and net and gross spend in USD.

### Analytics chat

Analytics chat lets you ask questions about your org's usage in plain language. Type a question—"show me daily spend for the last 30 days," "who are our top spenders," "what's our seat utilization rate"—and Claude returns a chart and a short written summary of what it found. You can follow up to refine, drill in, or pivot without starting over.

Use this when you have a specific question and don't want to navigate the dashboard, or when you're exploring trends and want fast back-and-forth. Results cover the last 30 days by default; specify a different range in your question if you need it. Data refreshes daily. **[Learn more](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage)**.

### Analytics API

For programmatic access, use the Claude Enterprise Analytics API. Pull a ranked list of users by tokens used or dollars spent, or look at usage and cost trends over time broken down by product, model, context window, or region. Each request is capped at 31 days wide, starting within the last 365 days, and no earlier than Jan 1, 2026.

Your Primary Owner can generate an admin API key. Data refreshes every four hours; for invoicing-grade totals, query dates 30+ days in the past so late events have time to reconcile. **[Learn more](https://platform.claude.com/docs/en/manage-claude/analytics-api)** and review the **[API reference guide](https://platform.claude.com/docs/en/api/admin/analytics)**.

---

## End user education

Technology controls will get you most of the way, but user behavior drives the rest. A team that understands how consumption works will make better choices independently—and surface fewer edge cases for you to troubleshoot.

### What to communicate to end users

When you onboard users, share the following:

**How Claude is billed**

- Usage is measured in tokens. Long prompts and long conversations consume more tokens.

- Claude Code and Cowork sessions are significantly more token-intensive than chat. A single long coding session can use many more tokens than a typical chat session.

- Check your usage in settings by toggling to **Settings → Usage**.

**How to choose a model**

- Sonnet is the default and handles most tasks well. Use Opus only when Sonnet isn't getting you where you need to go.

- Your org has a default model set for new conversations; you can still switch models mid-conversation when a task needs it.

- The model selector is visible in the interface—remind users to check it, especially if they're running complex tasks.

- The model selector is sticky, so make it a practice to check that it's the model you want to use.

- The effort level appears next to the model name. Higher effort means more thorough responses but higher token consumption, so match it to the task.

**What happens when they hit a cap**

- If a user hits their individual cap, they can contact their group owner or the IT/admin team to request an increase.

- They won't lose work in progress—Claude will complete the current turn before limiting further usage.
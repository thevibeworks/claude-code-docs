> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Claude Tag

> Set up Claude Tag for your organization: pair your Slack workspace, give Claude access to your tools, set a spending limit, and launch. See prerequisites and each step in detail.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag is Claude working in your team's Slack channels, with its own accounts in your tools.

Open [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). The page opens on setup until your first workspace is paired. It shows a step list, an FAQ, and a **Start setup** button (**Resume setup** if you started earlier without finishing). If you see **View setup guide** and **Go to chat** buttons instead, your signed-in account can't run setup; start at [Common setup issues](#common-setup-issues). Setup walks you through each step:

* **[Pair your Slack workspace](#pair-your-slack-workspace)**: install the Slack app and link it with a pairing code
* **[Choose Claude's first tools](#choose-claude%E2%80%99s-first-tools)**: pick two apps Claude will work in
* **[Connect GitHub](#connect-github)**: install the Claude GitHub App, or grant repositories if it's already linked
* **[Create accounts for Claude's other tools](#create-accounts-for-the-tools-you-chose)**: give Claude its own account in each tool you picked and connect the credentials
* **[Launch Claude Tag](#launch-claude-tag)**: set a spending limit and turn on Claude Tag

The rest of this page covers [what to have ready before you start](#before-you-start), [each step in detail](#setup-steps), and [common setup issues](#common-setup-issues).

<Note>If your team already uses the earlier Claude in Slack, the same steps apply and your existing app stays; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) for what changes.</Note>

## Before you start

| Prerequisite                                                              | Why you need it                                                                                                                                                                       | If you don't have it                                                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A **Team or Enterprise plan** on claude.ai                                | Claude Tag is available on Team and Enterprise plans, on Anthropic's first-party service. It isn't available on individual plans (Free, Pro, or Max), or for third-party deployments. | Start a Team or Enterprise plan at [claude.com/pricing](https://claude.com/pricing)                                                                                                                                                                                                                                               |
| A Claude organization **without Zero Data Retention (ZDR)**               | Claude Tag stores channel memory and session transcripts, which ZDR doesn't permit.                                                                                                   | Claude Tag isn't available to ZDR organizations                                                                                                                                                                                                                                                                                   |
| **Routines** enabled for your Claude organization                         | Claude Tag requires Routines to be enabled for your organization. Until it is, Claude answers every mention and DM with a reply that it's unavailable and does no work.               | An admin enables Routines at [`claude.ai/admin-settings/claude-code`](https://claude.ai/admin-settings/claude-code)                                                                                                                                                                                                               |
| **Owner** role in the Claude organization you're setting up               | Pairing a workspace and creating Access bundles are Owner-only writes. Roles are per organization, so being an Owner elsewhere doesn't carry over.                                    | Ask an Owner to run setup, or have one promote you at [`claude.ai/admin-settings/members`](https://claude.ai/admin-settings/members)                                                                                                                                                                                              |
| A **Slack workspace admin**                                               | Running `@Claude connect` requires a Slack workspace admin; installing the app usually does too (most workspaces require admin approval for new apps)                                 | If that's someone else, [send them the install request](/docs/claude-tag/admins/pair-workspace#send-the-install-request-to-your-slack-admin) early (app approval can take time), and plan to be online together when you [pair your Slack workspace](#pair-your-slack-workspace); pairing codes expire 15 minutes after they're issued |
| **Usage credits** (Team plans)                                            | Channel work draws from your organization's usage balance; on a Team plan nothing runs until credits are loaded                                                                       | Check whether your organization has a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) before buying; otherwise, buy credits at [`claude.ai/admin-settings/usage`](https://claude.ai/admin-settings/usage)                                           |
| *(Optional)* The **Claude GitHub App** linked to your Claude organization | Linking GitHub before you start turns setup's GitHub step into repository selection, so you can grant repositories there instead of installing the app mid-setup                      | [Link your GitHub organization](/docs/claude-tag/admins/configure-github#link-your-github-organization) first, or grant repository access after setup                                                                                                                                                                                  |
| *(Optional)* A **channel to test in**                                     | You'll invite Claude to a channel to [test](#test-that-setup-worked) that setup worked                                                                                                | Create a private Slack channel for the pilot, or pick any existing one                                                                                                                                                                                                                                                            |

If any of your services restrict traffic by IP, file the [network requirements](/docs/claude-tag/admins/network-requirements) request with your network team early; in many organizations, IP allowlist changes take days to approve.

## Setup steps

All steps run on one page. Everything you set is saved automatically, so you can leave and resume setup later. Each section below shows what you'll see and what to do.

### Pair your Slack workspace

A Slack workspace is your team's space in Slack, at an address like `your-team.slack.com`; it contains all your channels. Pairing links one workspace to your Claude organization so `@Claude` can run in its channels and usage bills to your organization.

This step shows four numbered substeps. The code is created in Slack and redeemed back on this setup page:

<Steps>
  <Step title="Add the Claude app to Slack">
    Click **Add the Claude app** to open the Slack Marketplace listing, then click **Add to Slack** there and approve the permissions.
  </Step>

  <Step title="Send `@Claude connect` as a new channel message">
    Copy the message shown and send it in any channel of the workspace you just installed in, with no other text, as a new top-level message or in a thread where Claude isn't already working. Claude replies with a pairing code valid for 15 minutes.

    Pick a channel that belongs to just that workspace. Claude can decline to reply in [guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels).

    Only a Slack workspace admin (or Grid org admin) can run `@Claude connect`; anyone else gets a message naming who to ask. If that's not you, [send them the install request](/docs/claude-tag/admins/pair-workspace#send-the-install-request-to-your-slack-admin) and have them return the code.
  </Step>

  <Step title="Paste the pairing code">
    Back on the setup page, paste the code into the input field (the placeholder reads `workspace_…`).
  </Step>

  <Step title="Choose where Claude runs">
    Under **Choose where Claude can reply when tagged**, select **Entire workspace (recommended)** or **Specific channel** (which asks for channel IDs).
  </Step>
</Steps>

Click **Pair workspace**. A confirmation screen shows the pairing worked; select **Next: Choose Claude's tools**.

See [Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace) for the Slack-admin handoff template, what to do if `@Claude connect` fails, and pairing on Enterprise Grid.

### Choose Claude's first tools

Claude works in your tools with its own accounts, so everything it does is recorded under its own name. On this step you pick those tools; connecting them happens in a [later step](#create-accounts-for-the-tools-you-chose).

GitHub isn't in the list. You connect it in the [next step](#connect-github). The list suggests widely used tools; check the ones your team works in, or use **Search all tools** for a service that isn't shown. Pick two to unlock **Next: Connect GitHub**. You can add more at any time.

You can skip connecting the tools you pick and finish that after setup. Without any connected tools, Claude still works in Slack conversations and can use web search and a [default set of network hosts](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential); it can't act in a tool until that tool is connected.

See [Give Claude access](/docs/claude-tag/admins/add-connections) for which services to connect first, and the [per-service connection guides](/docs/claude-tag/admins/connections/overview) for credential fields per tool.

### Connect GitHub

GitHub is managed through the Claude GitHub App rather than a credential, so it has its own step. What the step shows depends on whether the app is already linked to your Claude organization.

* **Not linked yet**: the step walks through installing the Claude GitHub App, with a message you can copy for the GitHub organization owner if that isn't you.
* **Already linked**: the step is titled **Choose your GitHub repos** and lists each installation, so you can grant every repository or only specific ones.

These grants apply to every channel Claude is in. You can [add repositories to specific channels later](/docs/claude-tag/admins/attach-to-scope), or skip this step and [configure GitHub access](/docs/claude-tag/admins/configure-github) after setup instead.

### Create accounts for the tools you chose

Claude needs its own account in each tool you picked, so you can always see what it did and limit what it reaches. [How agent identity works](/docs/claude-tag/concepts/agent-identity) explains this model.

<Steps>
  <Step title="Create an email address for Claude">
    Create an address like `claude@yourcompany.com` with your email provider. Some tools support service accounts (tool-managed identities that don't need an email) instead.
  </Step>

  <Step title="Invite Claude to each tool">
    In each tool you picked, create an account for that address, the same way you would for a new team member.
  </Step>

  <Step title="Connect each tool with Claude's credentials">
    Each tool you picked is listed. Click **Connect** and enter the credential for the account you created (not your personal login).
  </Step>
</Steps>

To finish this step later, select **Skip** and confirm past the warning that Claude won't be able to act in the unconnected tools.

See [Give Claude access](/docs/claude-tag/admins/add-connections) for how to create the accounts and what access to give them.

You can use any address. The setup flow shows `claude@` followed by your own domain only as an example; Claude Tag never asks for the address and keeps only the credential you enter for each tool.

### Launch Claude Tag

Channel work draws from your organization's usage balance, not from individual seats; the spend limit you set here caps how much of that balance Claude Tag can use each billing period. (DMs run on the user's own claude.ai account and aren't capped by this limit.)

<Steps>
  <Step title="Set monthly spend limits">
    Choose from `$500`, `$1,000`, `$2,500` (the default), `$5,000`, **Unlimited**, or **Custom** (a US-dollar amount up to `$1,000,000`).
  </Step>

  <Step title="Let members know they can now tag Claude">
    Choose whether Claude sends a DM to everyone in your Slack workspace after launch.
  </Step>

  <Step title="Click Launch Claude Tag">
    Claude Tag turns on, and a confirmation screen summarizes what's connected. Claude is now reachable in the workspace you paired.
  </Step>
</Steps>

To leave setup without turning Claude Tag on, select **Finish later**; everything you've set is saved, and the admin page shows a resume card that brings you back to where you left off.

If your organization buys usage credits by card in US dollars and has none loaded, a **Buy usage credits** step appears before launch instead of the spend limit picker; load credits, or select **Skip** to continue without. Invoiced organizations and those billing in other currencies get the spend limit picker regardless of balance.

See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for what counts toward the cap, per-channel limits, and what users see when it's reached.

## Change a setting after setup

Everything you set during setup can be changed afterward on the [Claude Tag admin page](https://claude.ai/admin-settings/claude-tag).

| To change                                                                       | Go to                                                                                                                                                         |
| :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pair another workspace, or disconnect one                                       | The Slack row's **⋮** menu under **Where Claude Tag works** (**Disconnect** is under **Manage**); see [Manage workspaces](/docs/claude-tag/admins/workspaces)      |
| The Access bundle's name, connections, domains, repos, plugins, or instructions | **Access bundles** in the left navigation, or any scope's panel on the **Slack** tab; see [Give Claude access](/docs/claude-tag/admins/add-connections)            |
| The spending limit                                                              | [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag); see [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) |
| Whether Claude Tag is enabled at all                                            | The **Enable Claude Tag for your organization** toggle at the top of the admin page                                                                           |

## Test that setup worked

In Slack, in your pilot channel, run `/invite @Claude` and then `@Claude summarize this channel`.

An *is thinking…* status under your message means the app is installed and listening. A reply means the workspace is paired and the channel is on the new version. This task doesn't touch any connection, so it isolates pairing from credential issues.

The [See it work](/docs/claude-tag/admins/test-it) page has more prompts that run with no connections, and a per-connection test that proves each credential works.

## After setup

After your test passes, you can DM Claude in Slack with setup questions. These guides cover what's not part of initial setup:

| Guide                                                                                                     | Do this when                                                                                                                                        |
| :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Give Claude access](/docs/claude-tag/admins/add-connections)                                                  | You skipped connections during setup, or a team needs another tool connected                                                                        |
| [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) | Claude reports a blocked host, or a channel needs to reach a site or API that doesn't take a credential                                             |
| [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope)                                        | One channel needs more (or different) access than the default. Keep elevated credentials in private-channel scopes; the org baseline stays minimal. |
| [Configure GitHub access](/docs/claude-tag/admins/configure-github)                                            | You didn't grant repository access during setup, or you need to add more repositories                                                               |
| [Restrict where Claude operates](/docs/claude-tag/admins/restrict-access)                                      | Governance review: guest channels, member access, DM policy                                                                                         |
| [Customize](/docs/claude-tag/admins/customize)                                                                 | Standing instructions, plugins, and what channel members can change                                                                                 |

There are two common ways to roll out from here:

| Pattern                  | What you do                                                    | What channel members experience                                                                |
| :----------------------- | :------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| Pilot first              | One bundle on one workspace or channel; widen after validating | Claude appears in a few channels first, with capability growing as scopes are attached         |
| Single bundle everywhere | One broad bundle at organization defaults                      | Every channel gets the same capability on day one. Fits orgs that already grant tools broadly. |

## Common setup issues

| You expected                                                                                           | But got                                                                                                                                     | Do this                                                                                                                                                                                                                                                                                                                                                                                                             |
| :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) | A page titled **Set up Claude Tag** with **View setup guide** and **Go to chat** buttons                                                    | Your signed-in account can't run setup, and **View setup guide** leads back to this guide. On a personal account (Free, Pro, or Max), [start a Team or Enterprise plan](https://claude.com/pricing) first. In a Team or Enterprise organization, ask an Owner to run setup. When the page shows a workspace switcher, your account also belongs to another Team or Enterprise organization; switch to it and retry. |
| A pairing code from `@Claude connect`                                                                  | “Only Slack workspace admins (or Enterprise Grid org admins) can link this workspace to a Claude organization…”                             | The person who sent `@Claude connect` isn't a Slack workspace admin or Grid org admin. See [Only Slack workspace admins or Grid org admins can link this workspace](/docs/claude-tag/admins/troubleshooting#only-slack-workspace-admins-or-grid-org-admins-can-link-this-workspace).                                                                                                                                     |
| A pairing code                                                                                         | “…installation is out of date”                                                                                                              | A Slack admin approves the update or reinstalls the app, then sends `@Claude connect` again. See [This workspace's Claude app installation is out of date](/docs/claude-tag/admins/troubleshooting#this-workspace%E2%80%99s-claude-app-installation-is-out-of-date).                                                                                                                                                     |
| The Slack row under **Where Claude Tag works** to show your workspace as connected                     | It still shows **Not connected**                                                                                                            | The code may have expired (codes last 15 minutes) or come from a different workspace. Send `@Claude connect` again for a fresh code.                                                                                                                                                                                                                                                                                |
| A pairing code                                                                                         | A message about guests, or about the channel being shared across workspaces                                                                 | Send `@Claude connect` again in a channel with no guests that belongs to a single workspace. Match the exact message in [Guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels) for the fix that fits it.                                                                                                                                                                         |
| A connected tool to work in your test                                                                  | “I can't reach…”                                                                                                                            | Claude isn't told about a connection added after the thread started. Ask it to use the service by name, or start a fresh thread.                                                                                                                                                                                                                                                                                    |
| The **Where Claude Tag works** section with a **+ Connect** button                                     | Only the legacy Claude in Slack toggles                                                                                                     | Your organization isn't enabled for Claude Tag. Contact your account team.                                                                                                                                                                                                                                                                                                                                          |
| Claude to respond in Slack                                                                             | "Claude Tag has been turned off for your Claude organization…"                                                                              | The **Enable Claude Tag for your organization** toggle is off. An Owner turns it on at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). See [the troubleshooting entry](/docs/claude-tag/admins/troubleshooting#claude-tag-is-turned-off-for-your-organization).                                                                                                                    |
| Claude to respond in Slack                                                                             | "Claude Tag is unavailable because Routines aren't enabled for your organization…"                                                          | Routines isn't enabled for your Claude organization, which Claude Tag requires. An admin enables Routines at [`claude.ai/admin-settings/claude-code`](https://claude.ai/admin-settings/claude-code), then anyone can mention `@Claude` again. See [the troubleshooting entry](/docs/claude-tag/admins/troubleshooting#claude-tag-is-unavailable-because-routines-are-not-enabled).                                       |
| Claude to respond in Slack                                                                             | "Claude in Slack is not available for your organization" or "Claude isn't available for organizations with restricted compliance settings." | The paired Claude organization has a restricted compliance configuration, such as Zero Data Retention (ZDR), that Claude Tag can't run under. No setting lifts this; contact your account team. See [the troubleshooting entry](/docs/claude-tag/admins/troubleshooting#restricted-compliance-settings-block-claude-tag).                                                                                                |
| The **Slack** tab to list your scopes                                                                  | "Couldn't load Slack scopes. Reload the page to try again."                                                                                 | Reload the page. See [Couldn't load Slack scopes](/docs/claude-tag/admins/troubleshooting#couldn%E2%80%99t-load-slack-scopes).                                                                                                                                                                                                                                                                                           |
| A reply in your test channel                                                                           | "Couldn't check this channel just now"                                                                                                      | Mention `@Claude` again. See [Couldn't check this channel just now](/docs/claude-tag/admins/troubleshooting#couldn%E2%80%99t-check-this-channel-just-now).                                                                                                                                                                                                                                                               |
| A reply in your test channel                                                                           | "Something went wrong starting a session"                                                                                                   | Retry first. If it persists, see [the session-start entries](/docs/claude-tag/admins/troubleshooting#something-went-wrong-starting-a-session).                                                                                                                                                                                                                                                                           |

## Related resources

* [Network requirements](/docs/claude-tag/admins/network-requirements): what your services must allowlist so Claude can reach them
* [Claude Tag in production at Anthropic](https://claude.com/blog/ai-ci-cd-on-call): how Anthropic runs Claude Tag as its first responder for CI/CD failures

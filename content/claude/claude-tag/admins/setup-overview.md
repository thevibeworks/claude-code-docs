> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Claude Tag

> Set up Claude Tag for your organization: pair your Slack workspace, choose and connect Claude's tools, set a spending limit, launch, and test that it works. Every step on one page.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag is Claude working in your team's Slack channels. It can also act in your other tools, like your issue tracker or data warehouse, through accounts you create for it during setup.

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and click **Start setup** (**Resume setup** if you started earlier). The setup page walks you through these steps in order. This page covers each one in the same order, and each section says what to have ready before the step and what each choice means.

1. [Pair your Slack workspace](#pair-your-slack-workspace): install the Slack app and redeem a pairing code
2. [Choose Claude's first tools](#choose-claude%E2%80%99s-first-tools): select at least two tools
3. [Connect GitHub](#connect-github): install the Claude GitHub App and grant repositories
4. [Create accounts for Claude's other tools](#create-accounts-for-claude%E2%80%99s-other-tools): one account and API key per tool
5. [Launch Claude Tag](#launch-claude-tag): set the monthly spend limit and turn Claude Tag on

The console saves your progress, so you can leave and come back to where you stopped. When you've launched, [verify your setup](#verify-your-setup).

<Accordion title="Before you start: check that you have what setup needs">
  | Prerequisite                                                              | Why you need it                                                                                                                                                                       | If you don't have it                                                                                                                                                                                                                                                                    |
  | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | A **Team or Enterprise plan** on claude.ai                                | Claude Tag is available on Team and Enterprise plans, on Anthropic's first-party service. It isn't available on individual plans (Free, Pro, or Max), or for third-party deployments. | Start a Team or Enterprise plan at [claude.com/pricing](https://claude.com/pricing)                                                                                                                                                                                                     |
  | A Claude organization **without Zero Data Retention (ZDR)**               | Claude Tag stores channel memory and session transcripts, which ZDR doesn't permit.                                                                                                   | Claude Tag isn't available to ZDR organizations                                                                                                                                                                                                                                         |
  | **Routines** enabled for your Claude organization                         | Until it is, Claude answers every mention and DM with a reply that it's unavailable and does no work.                                                                                 | An admin enables Routines at [`claude.ai/admin-settings/claude-code`](https://claude.ai/admin-settings/claude-code)                                                                                                                                                                     |
  | **Owner** role in the Claude organization you're setting up               | Pairing a workspace and creating Access bundles are Owner-only writes. Roles are per organization, so being an Owner elsewhere doesn't carry over.                                    | Ask an Owner to run setup, or have one promote you at [`claude.ai/admin-settings/members`](https://claude.ai/admin-settings/members)                                                                                                                                                    |
  | A **Slack workspace admin**                                               | Running `@Claude connect` requires a Slack workspace admin; installing the app usually does too.                                                                                      | If that's someone else, [send them the install request](#if-you-re-not-the-slack-workspace-admin) early (app approval can take time), and plan to be online together when you pair; pairing codes expire 15 minutes after they're issued                                                |
  | **Usage credits** (Team plans)                                            | Channel work draws from your organization's usage balance; on a Team plan nothing runs until credits are loaded.                                                                      | Check whether your organization has a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) before buying; otherwise, buy credits at [`claude.ai/admin-settings/usage`](https://claude.ai/admin-settings/usage) |
  | *(Optional)* The **Claude GitHub App** linked to your Claude organization | Linking GitHub first turns setup's GitHub step into repository selection instead of an app install.                                                                                   | [Link your GitHub organization](/docs/claude-tag/admins/configure-github#link-your-github-organization) first, or grant repository access after setup                                                                                                                                        |
  | *(Optional)* A **channel to test in**                                     | You'll invite Claude to a channel to [verify your setup](#verify-your-setup).                                                                                                         | Create a private Slack channel for the pilot, or pick any existing one                                                                                                                                                                                                                  |

  If any of your services restrict traffic by IP, file the [network requirements](/docs/claude-tag/admins/network-requirements) request with your network team early; in many organizations, IP allowlist changes take days to approve.

  If you see **View setup guide** and **Go to chat** buttons instead of **Start setup**, your signed-in account can't run setup. See [Common setup issues](#common-setup-issues).
</Accordion>

<Note>If your team already uses the earlier Claude in Slack, the same steps apply and your existing app stays; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) for what changes.</Note>

## Pair your Slack workspace

Install the Claude app in Slack, get a pairing code from Slack, and paste it on the setup page.

<Steps>
  <Step title="Add the Claude app to Slack">
    **Where:** the Slack Marketplace, at [claude.com/claude-for-slack](https://claude.com/claude-for-slack).

    Click **Add the Claude app** on the setup page to open the listing, then click **Add to Slack** and approve the permissions. If the app is already installed, click **Add to Slack** anyway: you reinstall over the existing app with its current permissions and keep your settings.
  </Step>

  <Step title="Send @Claude connect in any channel">
    **Where:** Slack, in the workspace you just installed the app in.

    Open any channel and add Claude to it with `/invite @Claude`. Claude posts a short welcome message when it joins. Then send `@Claude connect` as a new message with no other text. Claude replies in the channel with a message only you can see, containing the pairing code:

    > Connect **this workspace** (Acme) to your Claude organization for billing: have a Claude **organization admin** redeem this code in Claude admin settings. The code works once and expires in 15 minutes.

    > `workspace_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`

    > *Once connected, Claude usage in this workspace is billed to that organization.*

    Only a Slack workspace admin (or Grid org admin) can run this command; anyone else gets a message naming who to ask.

    If you skip the invite, Slack shows you a notice that Claude isn't in the channel, with an **Add Them** button. Click it, then send `@Claude connect` again.
  </Step>

  <Step title="Paste the pairing code">
    **Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

    Paste the pairing code Claude sent into the **Paste the pairing code** field. **Connected to** followed by your workspace name appears under it when the code is accepted.
  </Step>

  <Step title="Choose where Claude can reply when tagged">
    Select **Entire workspace (recommended)** or **Specific channel**.

    If you select **Specific channel**, enter each channel's ID in the **Channel IDs** field, separated by commas, like `C0B1SLDGBPG, C0ARH08HQCA`. To find a channel's ID in Slack, right-click the channel, choose **Copy**, then **Copy link**; the ID is the part after the last slash. For a private channel, invite `@Claude` to it in Slack first.

    If you aren't asked where Claude can reply, Claude replies across the whole workspace once you [launch](#launch-claude-tag).
  </Step>

  <Step title="Click Pair workspace">
    You see a confirmation that the pairing worked. Select **Next: Choose Claude’s tools**.
  </Step>
</Steps>

Claude doesn't answer mentions in Slack until you finish [Launch Claude Tag](#launch-claude-tag); a mention before then gets "Claude is disabled in this channel."

<Accordion title="If you're not the Slack workspace admin">
  Only a Slack workspace admin can run `@Claude connect`, and in most workspaces only an admin can install the app. If that's not you, send the Slack admin the message below and have them return the pairing code:

  ```text wrap theme={null}
  Please install the Claude app (https://claude.com/claude-for-slack) in [workspace]. When that's done, let me know a time that works for the next part: in any channel, run /invite @Claude, then post "@Claude connect" with no other text and send me the code it returns. Pick a channel that belongs to just [workspace]. The code expires 15 minutes after Claude posts it, so I'll redeem it right away. What it can access: https://claude.com/docs/claude-tag/admins/for-slack-admins
  ```
</Accordion>

<Accordion title="If your Slack is on Enterprise Grid">
  When a Grid org admin sends `@Claude connect`, the reply includes two codes: a `workspace_` code that pairs only that workspace, and an `enterprise_` code that pairs every workspace in the Grid that doesn't already have its own pairing. Paste the `enterprise_` code if Claude should work across the Grid; DMs for users homed in other Grid workspaces only work with a Grid-wide pairing. See [Pair an Enterprise Grid](/docs/claude-tag/admins/workspaces#pair-an-enterprise-grid).
</Accordion>

## Choose Claude's first tools

**Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

Select at least two tools your team uses, then click **Next: Connect GitHub**. Selecting a tool here doesn't connect it. In [Create accounts for Claude's other tools](#create-accounts-for-claude%E2%80%99s-other-tools), you create an account for Claude in each tool you selected and paste that account's API key on the setup page.

The list shows widely used tools; use **Search all tools** for one that isn't shown. GitHub isn't in the list; you set it up in [Connect GitHub](#connect-github). You can add more tools any time after setup.

See [Give Claude access](/docs/claude-tag/admins/add-connections) for which services to connect first.

## Connect GitHub

**Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). If the app isn't installed yet, the step sends you to github.com to install it.

Claude reaches GitHub through the [Claude GitHub App](/docs/claude-tag/admins/configure-github) rather than an account and credential, so GitHub has its own step. The setup page shows one of three things, depending on where the Claude GitHub App is installed:

* **Install the Claude GitHub App**, when the app isn't linked to your Claude organization yet. Only an owner of your GitHub organization can install it. If that's you, follow the steps shown. If not, send the message the step shows to a GitHub organization owner, skip this step, and continue with setup. After they install the app, [grant repositories](/docs/claude-tag/admins/configure-github#grant-repository-access) from the admin page.
* **Choose your GitHub repos**, when the app is already linked. Grant every repository or pick specific ones.
* **The Claude app is installed on \[username], a personal account**, when the app was installed on someone's personal GitHub account rather than an organization. Claude Tag connects to a GitHub organization only. A GitHub organization owner installs the app on the organization that owns your repositories (see [Link your GitHub organization](/docs/claude-tag/admins/configure-github#link-your-github-organization)). You can skip the step and continue with setup while that happens, then [grant repositories](/docs/claude-tag/admins/configure-github#grant-repository-access) from the admin page afterward.

The repositories you grant apply to every channel Claude is in. If your team won't hand Claude code work, skip this step.

## Create accounts for Claude's other tools

**Where:** your company's email admin console and each tool you selected, then the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

Treat Claude like a new hire. You give it an email address, add it to each tool as a member, and then, signed in as Claude, create an API key in that tool. The setup page asks you for those keys, one per tool. Claude's own account in each tool is what lets you see exactly what it did in that tool's logs and cut off its access without touching anyone else's. [How agent identity works](/docs/claude-tag/concepts/agent-identity) has the full model.

Work through one tool end to end before starting the next.

<Steps>
  <Step title="Create an email address for Claude">
    In your company's email admin console, create a new user for Claude, for example `claude@yourcompany.example.com`, the same way you'd create a mailbox for a new hire. Every tool invitation and verification email for Claude lands in that inbox. Any address works; the setup page shows `claude@` followed by your domain only as an example, and Claude Tag never stores the address itself.
  </Step>

  <Step title="Add Claude to the tool as a member">
    In the tool's member or user settings, invite `claude@yourcompany.example.com` the way you'd add a new teammate. Open the invitation from Claude's inbox and finish creating the account, including a password. Give the account the narrowest role that covers the work; read-only where the tool offers it.

    For a tool that offers service accounts, create one in the tool's admin settings instead of inviting the email address, scoped read-only or to the specific project.
  </Step>

  <Step title="Create an API key in Claude's account">
    Sign in to the tool as Claude and create the credential that tool's [connection guide](/docs/claude-tag/admins/connections/overview) names, usually an API key or personal access token from the tool's settings. Copy it; it belongs to Claude's account, so Claude's actions show up in the tool's audit log under Claude's name.
  </Step>

  <Step title="Paste the key on the setup page">
    Back on the setup page, each tool you selected is listed. Click **Connect** next to the tool and paste the key you just created. Then repeat the last three steps for the next tool you selected: add Claude as a member, create an API key in Claude's account, and paste it here. Claude keeps the one email address for every tool.
  </Step>
</Steps>

To finish this step later, select **Skip** and confirm past the warning that Claude won't be able to act in the unconnected tools. Claude still works from what's in Slack: it can catch a team up on a channel, turn a thread into a doc, and search the web. It can't act in a tool until that tool is connected. See [Give Claude access](/docs/claude-tag/admins/add-connections) for what access to give each account, and the [per-service connection guides](/docs/claude-tag/admins/connections/overview) for the credential fields per tool.

## Launch Claude Tag

**Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

Channel work draws from your organization's usage balance, not from individual seats; the spend limit caps how much of that balance Claude Tag can use each billing period. DMs run on the user's own claude.ai account and aren't capped by this limit. If your organization has a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise), the launch screen shows the amount and the date it runs through, and after launch the admin page shows it under **Included usage** with how much is used. You're billed for usage beyond it, up to the spend limit.

If the setup page shows a **Buy usage credits** step before Launch, buy credits on that step to continue. The launch screen then doesn't include **Set monthly spend limits**, so set a limit after launch at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag).

<Steps>
  <Step title="Set monthly spend limits">
    Choose from `$500`, `$1,000`, `$2,500`, `$5,000`, **Unlimited**, or **Custom** (a US-dollar amount up to `$1,000,000`). Usage bills against your organization's balance up to that amount each month. See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for what counts toward the cap, per-channel limits, and what users see when it's reached.
  </Step>

  <Step title="Let members know they can now tag Claude">
    The toggle is on by default: after launch, Claude DMs each member of the workspace to help them get started. Those DMs don't count toward your usage. Turn the toggle off to skip them. The same setting appears on the admin page afterward as **Let people know they can talk to Claude**, marked **Members notified** once the DMs have gone out.
  </Step>

  <Step title="Click Launch Claude Tag">
    Claude Tag turns on and you return to the Claude Tag admin page, which now shows your workspace under **Where Claude Tag works**. Claude answers mentions in the workspace you paired from here on. If you skipped connecting tools, a **Finish setting up Claude Tag** card sits at the top of the admin page; its **Finish setup** button reopens the steps you skipped.
  </Step>
</Steps>

To leave setup without turning Claude Tag on, select **Finish later**. Everything you've set is saved, and the admin page shows a resume card that brings you back here. Until you launch, the Claude app is in your Slack workspace but every mention gets "Claude is disabled in this channel."

## Verify your setup

**Where:** Slack, in any channel of the workspace you paired.

Run the first check, then the ones that match what you connected.

### Check that Claude responds

Add Claude to the channel, then mention it:

```text wrap theme={null}
/invite @Claude
```

```text wrap theme={null}
@Claude summarize what this channel decided this week and list any open questions
```

**Passed when:** Claude replies in a thread under your message. The reply ends with a footer naming the model and a **Configure** link.

**If not:** "Claude is disabled in this channel" means you haven't finished [Launch Claude Tag](#launch-claude-tag). No reply at all means the channel isn't covered; check that the workspace appears under **Claude Tag's access** on the **Slack** tab in admin settings, then see [Nothing responds](/docs/claude-tag/admins/troubleshooting#nothing-responds).

### Check a tool you connected

Skip this check if you skipped [Create accounts for Claude's other tools](#create-accounts-for-claude%E2%80%99s-other-tools). Otherwise, in a new thread, ask what the channel can reach:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Then ask one tool for something small that a read-only account can do. If you connected an issue tracker:

```text wrap theme={null}
@Claude pull the five most recent issues from our issue tracker and post them here
```

For a data warehouse, ask for a row count from one table. For a support tool, ask for the newest open tickets. For a document store, ask it to find a file by name.

**Passed when:** the first reply lists the tools you connected, the second comes back with data, and the request appears in that tool's audit log under Claude's account.

**If not:** a tool missing from the list means its connection didn't save; open the Access bundle in admin settings and [connect it again](/docs/claude-tag/admins/add-connections#add-a-connection). "I can't reach…" in a thread you started before connecting means Claude wasn't told about the new connection; start a fresh thread. Anything else, see [Access and connections](/docs/claude-tag/admins/troubleshooting#access-and-connections).

### Check GitHub

Skip this check if you skipped [Connect GitHub](#connect-github). Otherwise, ask about a repository you granted:

```text wrap theme={null}
@Claude list the open pull requests in your-org/your-repo and who each one is waiting on
```

**Passed when:** Claude lists the pull requests.

**If not:** see [GitHub doesn't work in this channel](/docs/claude-tag/admins/troubleshooting#github-doesn%E2%80%99t-work-in-this-channel).

For more tasks to hand Claude once the checks pass, see the [use case library](/docs/claude-tag/users/use-cases).

## After setup

After launch, you change anything about Claude Tag from the admin page:

1. Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).
2. Under **Claude Tag's access**, open the **Slack** tab.
3. In the list on the left, select **Default Slack** to change how Claude works everywhere, or select a workspace or channel to change it in that one place.

What you connected during setup is attached to the workspace you paired, or to each channel you listed if you chose **Specific channel**. **Default Slack** is the layer above that: anything you add there applies in every workspace and channel, and each entry below it adds to that for one place.

Every entry has the same sections: **Connectors**, **Repositories**, **Plugins**, **Custom instructions**, **Access bundles**, and, under **Advanced**, the **Default model**. An [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) is a named set of connections, repositories, plugins, and instructions that you can attach to more than one place. Setup created one on your workspace's entry, named after the workspace (for example, **Tag Test default**), holding the tools you connected.

| To do this                                            | Go to                                                                                                                        | Learn more                                                                                                |
| :---------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| Change the model Claude replies with                  | The entry's **Advanced** section, **Default model**. Set it on **Default Slack** to change it everywhere, or on one channel. | [Choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope)                 |
| Give Claude standing instructions                     | The **Custom instructions** field on **Default Slack** for every channel, or on one channel's entry for that channel only.   | [Customize](/docs/claude-tag/admins/customize)                                                                 |
| Connect another tool, or one you skipped              | **Connectors** on the entry, or the bundle named after your workspace under **Access bundles**.                              | [Give Claude access](/docs/claude-tag/admins/add-connections)                                                  |
| Let Claude reach a site or API that has no credential | The **Domains** list of the Access bundle, under **Access bundles**.                                                         | [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) |
| Grant more repositories                               | **Repositories** on the entry.                                                                                               | [Configure GitHub access](/docs/claude-tag/admins/configure-github)                                            |
| Give one channel more than the default                | Select the channel and add to it.                                                                                            | [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope)                                        |
| Limit where Claude works or who can use it            |                                                                                                                              | [Restrict where Claude operates](/docs/claude-tag/admins/restrict-access)                                      |
| Pair another workspace, or disconnect one             | The Slack row's **⋮** menu under **Where Claude Tag works**.                                                                 | [Manage workspaces](/docs/claude-tag/admins/workspaces)                                                        |
| Change the spend limit                                | [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag).                            | [Set a spend limit](/docs/claude-tag/admins/set-spend-limit)                                                   |
| Turn Claude Tag off                                   | The **Enable Claude Tag for your organization** toggle at the top of the admin page.                                         |                                                                                                           |
| Bring in the first users                              |                                                                                                                              | [Getting started for users](/docs/claude-tag/users/getting-started)                                            |

## Common setup issues

Every message setup can show instead of the next step, matched to its fix, is in [Setup errors](/docs/claude-tag/admins/troubleshooting#setup-errors) on the troubleshooting page.

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): what happens between a mention and a reply
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why Claude gets its own accounts, and what that means for audit logs and access
* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope#how-scopes-inherit): how Default Slack, workspaces, and channels inherit Access bundles
* [Claude Tag settings map](/docs/claude-tag/concepts/settings-map): every setting, and whether admins, channel members, or users control it
* [Glossary](/docs/claude-tag/concepts/glossary): Access bundle, scope, session, and the other terms on this page
* [Network requirements](/docs/claude-tag/admins/network-requirements): what your services must allowlist so Claude can reach them
* [Claude Tag in production at Anthropic](https://claude.com/blog/ai-ci-cd-on-call): how Anthropic runs Claude Tag as its first responder for CI/CD failures

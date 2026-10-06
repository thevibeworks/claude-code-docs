> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Claude Tag

> Set up Claude Tag for your organization: pair your Slack workspace, add Claude to channels, launch, give Claude access to your tools, and check that it works.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag is Claude working in your team's Slack channels. Setup connects Claude to your Slack workspace and turns Claude Tag on. Claude gets access to your other tools, like your issue tracker or data warehouse, after setup. Running setup requires the Owner role in a Claude organization on a Team or Enterprise plan.

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and click **Start setup** (**Resume setup** if you started earlier). The setup page walks you through these steps in order.

1. [Pair your Slack workspace](#pair-your-slack-workspace): install the Slack app and redeem a pairing code
2. [Connect GitHub](#connect-github): appears only when your organization hasn't installed the Claude GitHub App, and you can skip it
3. [Buy usage credits](#buy-usage-credits): appears only when your organization pays by card in US dollars and has no credits
4. [Launch Claude Tag](#launch-claude-tag): add Claude to channels and turn Claude Tag on

If you leave after pairing a workspace, click **Resume setup** to continue from the next step. Your choices on the launch step aren't saved until you click **Launch Claude Tag**.

When you've launched, [give Claude access to your tools](#give-claude-access-to-your-tools) and [verify your setup](#verify-your-setup).

<Accordion title="Before you start: check that you have what setup needs">
  | Prerequisite | Why you need it | If you don't have it |
  | :- | :- | :- |
  | A **Team or Enterprise plan** on claude.ai | Claude Tag is available on Team and Enterprise plans, on Anthropic's first-party service. It isn't available on individual plans (Free, Pro, or Max), or for third-party deployments. | Start a Team or Enterprise plan at [claude.com/pricing](https://claude.com/pricing) |
  | A Claude organization **without Zero Data Retention (ZDR), customer-managed encryption (CMEK), or the HIPAA configuration for Claude Code (local mode) and Cowork (local mode)** | Claude Tag stores channel memory and session transcripts, which ZDR doesn't permit. A CMEK policy and the HIPAA configuration don't allow Claude Tag either. | Claude Tag isn't available to organizations with any of these. See [Healthcare organizations](/docs/claude-tag/admins/healthcare#plan-and-organization-requirements) |
  | **Routines** enabled for your Claude organization | Until it is, Claude answers every mention and DM with a reply that it's unavailable and does no work. | An admin turns on [**Admin settings > Capabilities > Remote sessions > Routines**](https://claude.ai/admin-settings/capabilities) |
  | **Owner** role in the Claude organization you're setting up | Setup pairs a workspace and turns Claude Tag on, and only an Owner can do either. Roles are per organization, so being an Owner elsewhere doesn't carry over. | Ask an Owner to run setup, or have one promote you at [`claude.ai/admin-settings/members`](https://claude.ai/admin-settings/members) |
  | A **Slack workspace admin** | Running `@Claude connect` requires a Slack workspace admin; installing the app usually does too. | If that's someone else, [send them the install request](#if-you-re-not-the-slack-workspace-admin) early (app approval can take time), and plan to be online together when you pair; pairing codes expire 15 minutes after they're issued |
  | **Usage credits** (Team plans) | Channel work draws from your organization's usage balance; on a Team plan nothing runs until credits are loaded. | Buy credits at [`claude.ai/admin-settings/usage`](https://claude.ai/admin-settings/usage) |
  | A **public channel** for Claude to join | The launch step asks you to select at least one public channel, and you can [verify your setup](#verify-your-setup) there. | Create a public Slack channel for the pilot, or pick any existing one |

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

    On Slack Enterprise Grid, installing takes two Slack actions. See [Set up Claude Tag on Enterprise Grid](/docs/claude-tag/admins/workspaces#set-up-claude-tag-on-enterprise-grid) for the steps.
  </Step>

  <Step title="Send @Claude connect in any channel">
    **Where:** Slack, in the workspace you just installed the app in.

    Open any channel and add Claude to it with `/invite @Claude`. Claude posts a short welcome message when it joins. Then send `@Claude connect` as a new message with no other text. Claude replies in the channel with a message only you can see, containing the pairing code:

    > Connect **this workspace** (Acme) to your Claude organization for billing: have a Claude **organization admin** redeem this code in Claude admin settings. The code works once and expires in 15 minutes.
    >
    > `workspace_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`
    >
    > *Once connected, Claude usage in this workspace is billed to that organization.*

    Only a Slack workspace admin (or Grid org admin) can run this command; anyone else gets a message naming who to ask.

    If you skip the invite, Slack shows you a notice that Claude isn't in the channel, with an **Add Them** button. Click it, then send `@Claude connect` again.
  </Step>

  <Step title="Paste the pairing code">
    **Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

    Paste the pairing code Claude sent into the **Paste the pairing code** field. **Connected to** followed by your workspace name appears under it when the code is accepted.
  </Step>

  <Step title="Click Pair workspace">
    The setup page continues to the next step that applies to your organization.
  </Step>
</Steps>

Pairing covers the whole workspace. Claude doesn't answer mentions in Slack until you finish [Launch Claude Tag](#launch-claude-tag). A mention before then gets a notice that starts "Claude isn't on in this channel yet."

After launch, people can tag Claude in any channel it has joined. To keep Claude to certain channels, see [Limit Claude Tag to specific channels](/docs/claude-tag/admins/restrict-access#limit-claude-tag-to-specific-channels).

<Accordion title="If you're not the Slack workspace admin">
  Only a Slack workspace admin can run `@Claude connect`, and in most workspaces only an admin can install the app. If that's not you, send the Slack admin the message below and have them return the pairing code:

  ```text wrap theme={null}
  Please install the Claude app (https://claude.com/claude-for-slack) in [workspace]. When that's done, let me know a time that works for the next part: in any channel, run /invite @Claude, then post "@Claude connect" with no other text and send me the code it returns. Pick a channel that belongs to just [workspace]. The code expires 15 minutes after Claude posts it, so I'll redeem it right away. What it can access: https://claude.com/docs/claude-tag/admins/for-slack-admins
  ```
</Accordion>

<Accordion title="If your Slack is on Enterprise Grid">
  When a Slack Org Owner or Org Admin sends `@Claude connect`, the reply includes two codes. One begins `workspace_` and pairs only the workspace the admin sent the command in, and one begins `enterprise_` and pairs the whole Grid. Paste the `enterprise_` code. See [Pair an Enterprise Grid](/docs/claude-tag/admins/workspaces#pair-an-enterprise-grid).
</Accordion>

## Buy usage credits

**Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

Claude's work in channels draws from your organization's usage balance, and this step adds credits to that balance. The setup page shows the step only when your organization is on a Team or self-serve Enterprise plan, pays by card in US dollars, and has no usage credits.

Enter an amount and click **Buy now** to charge your organization's saved payment method. To continue without buying, click **Skip**, then buy credits at [`claude.ai/admin-settings/usage`](https://claude.ai/admin-settings/usage) before your team starts tagging Claude.

## Launch Claude Tag

**Where:** the Claude Tag setup page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

On the launch step, you add Claude to channels and turn Claude Tag on. You also set a monthly spend limit here, unless setup included the [**Buy usage credits**](#buy-usage-credits) step.

The spend limit caps how much of your organization's usage balance Claude Tag can use each month.

* **Channel work**: draws from that balance, not from individual seats
* **Direct messages (DMs)**: One-to-one DMs from members who have connected a Claude account run on the member's own claude.ai account and aren't capped by this limit. For members who haven't connected one, see [Direct messages from members without a Claude account](/docs/claude-tag/admins/restrict-access#direct-messages-from-members-without-a-claude-account).

<Steps>
  <Step title="Set monthly spend limits">
    If setup included the [**Buy usage credits**](#buy-usage-credits) step, the launch step has no spend limit picker. Set a limit after launch at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag).

    Otherwise, choose from `$500`, `$1,000`, `$2,500`, `$5,000`, **Unlimited**, or **Custom** (a US-dollar amount up to `$1,000,000`). `$2,500` is preselected unless your organization already has a Claude Tag spend limit. Usage bills against your organization's balance up to that amount each month. See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for what counts toward the cap, per-channel limits, and what users see when it's reached.
  </Step>

  <Step title="Add Claude to your channels">
    Choose which channels Claude joins when you launch.

    * **If the launch step lists public channels from the workspace you paired**: select at least one. **Launch Claude Tag** stays unavailable until you do. Claude joins the channels you selected when you launch, so people can tag it there right away.
    * **If the launch step shows no channel list**: launch, then run `/invite @Claude` in a channel in Slack.

    To add Claude to a private channel, or to more channels later, run `/invite @Claude` in that channel.
  </Step>

  <Step title="Let members know they can now tag Claude">
    If you paired a whole Enterprise Grid, skip this step. The launch step doesn't show the toggle, launching doesn't send the DMs, and the admin page has no row for them.

    Otherwise, the **Let members know they can now tag Claude** toggle is on by default. After launch, Claude DMs each member of the workspace to help them get started. Those DMs don't count toward your usage. Turn the toggle off to skip them.

    The admin page has a matching row, **Let people know they can talk to Claude**. To send the DMs from the admin page, select **Notify members now** on that row and confirm. The row reads **Members notified** once the DMs have gone out.
  </Step>

  <Step title="Click Launch Claude Tag">
    Claude Tag turns on. From here on, Claude answers mentions in the workspace you paired. The setup page shows **You're set**. Click **Done** to open the Claude Tag admin page.
  </Step>
</Steps>

To stop before launching, leave the setup page. Your pairing is saved, and your choices on the launch step aren't.

## Give Claude access to your tools

After launch, Claude reaches your other tools through personal connectors and through access you give Claude itself.

* **Personal connectors**: Claude can use a member's own claude.ai connectors for that member's requests in a channel. You don't connect anything for these. See [Personal connectors in channels](/docs/claude-tag/concepts/personal-connectors) for how members approve that use.
* **Access you give Claude**: you connect a tool on the Claude Tag admin page with credentials that belong to Claude rather than to a person. Claude then works in that tool and can use it for [work it starts on its own](/docs/claude-tag/users/proactivity).

### Connect GitHub

When your organization hasn't installed the Claude GitHub App, the setup page offers a **Connect GitHub** step after you pair your workspace. To connect GitHub later, click **Skip** on that step.

Connect GitHub if your team will give Claude code work. Claude reaches GitHub through the [Claude GitHub App](/docs/claude-tag/admins/configure-github). Only an owner of your GitHub organization can install it.

[Link your GitHub organization](/docs/claude-tag/admins/configure-github#link-your-github-organization) to install the app, then [grant repositories](/docs/claude-tag/admins/configure-github#grant-repository-access).

### Create accounts for Claude's other tools

**Where:** your company's email admin console and each tool you're connecting, then the Claude Tag admin page at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

In each tool other than GitHub, Claude works through an account of its own, so you can see what it did in that tool's logs and cut off its access without touching anyone else's. You give Claude an email address, add it to each tool as a member, then sign in as Claude and create an API key. [How agent identity works](/docs/claude-tag/concepts/agent-identity) has the full model.

Work through one tool end to end before starting the next.

<Steps>
  <Step title="Create an email address for Claude">
    In your company's email admin console, create a new user for Claude with any address, for example `claude@yourcompany.example.com`, the same way you'd create a mailbox for a new hire. Every tool invitation and verification email for Claude lands in that inbox.
  </Step>

  <Step title="Add Claude to the tool as a member">
    In the tool's member or user settings, invite `claude@yourcompany.example.com` the way you'd add a new teammate. Open the invitation from Claude's inbox and finish creating the account, including a password. Give the account the narrowest role that covers the work, read-only where the tool offers it.

    For a tool that offers service accounts, create one in the tool's admin settings instead of inviting the email address, scoped read-only or to the specific project.
  </Step>

  <Step title="Create an API key in Claude's account">
    Sign in to the tool as Claude and create the credential that tool's [connection guide](/docs/claude-tag/admins/connections/overview) names, usually an API key or personal access token from the tool's settings. Copy it. The credential belongs to Claude's account, so Claude's actions show up in the tool's audit log under Claude's name.
  </Step>

  <Step title="Add the key as a connector">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Connectors** tab and click **Add**. Then [add a connector](/docs/claude-tag/admins/add-connections#add-a-connection) for the tool and paste the key you created. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector.

    For the next tool, start again from **Add Claude to the tool as a member**. Claude keeps the one email address for every tool.
  </Step>
</Steps>

See [Give Claude access](/docs/claude-tag/admins/add-connections) for which services to connect first and what access to give each account, and the [per-service connection guides](/docs/claude-tag/admins/connections/overview) for the credential fields per tool.

## Verify your setup

**Where:** Slack, in a channel you added Claude to at launch or any other channel of the workspace you paired.

Run the first check after you launch, then the ones that match what you connected.

### Check that Claude responds

If you didn't select this channel at launch, add Claude to it. Then mention Claude:

```text wrap theme={null}
/invite @Claude
```

```text wrap theme={null}
@Claude summarize what this channel decided this week and list any open questions
```

**Passed when:** Claude replies in a thread under your message. The reply ends with a footer naming the model and a **Configure** link.

**If not:** a notice that starts "Claude isn't on in this channel yet" means you haven't finished [Launch Claude Tag](#launch-claude-tag). No reply at all means the channel isn't covered. Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), check that the workspace appears on the **Channels** tab under **Claude's access**, then see [Nothing responds](/docs/claude-tag/admins/troubleshooting#nothing-responds).

### Check a tool you connected

Run this check after you [connect a tool with Claude's own account](#create-accounts-for-claude%E2%80%99s-other-tools). In a new thread, ask what the channel can reach:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Then ask one tool for something small that a read-only account can do. If you connected an issue tracker:

```text wrap theme={null}
@Claude pull the five most recent issues from our issue tracker and post them here
```

For a data warehouse, ask for a row count from one table. For a support tool, ask for the newest open tickets. For a document store, ask it to find a file by name.

**Passed when:** the first reply lists the tools you connected, the second comes back with data, and the request appears in that tool's audit log under Claude's account.

**If not:** when a tool is missing from the list, go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and open the **Connectors** tab under **Claude's access**. If the tool isn't there, [connect it again](/docs/claude-tag/admins/add-connections#add-a-connection). If it is, open its page and check that it applies to the channel you asked in. "I can't reach…" in a thread you started before connecting means Claude wasn't told about the new connector; start a fresh thread. Anything else, see [Access and connections](/docs/claude-tag/admins/troubleshooting#access-and-connections).

### Check GitHub

Run this check after you [connect GitHub](#connect-github). Ask about a repository you granted:

```text wrap theme={null}
@Claude list the open pull requests in your-org/your-repo and who each one is waiting on
```

**Passed when:** Claude lists the pull requests.

**If not:** see [GitHub doesn't work in this channel](/docs/claude-tag/admins/troubleshooting#github-doesn%E2%80%99t-work-in-this-channel).

For more tasks to hand Claude once the checks pass, see the [use case library](/docs/claude-tag/users/use-cases).

## After setup

After launch, you change Claude Tag from [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). Organization-wide settings such as **Enable Claude Tag in Slack**, **Direct messages**, and **Model** sit at the top of the page. Below them, **Claude's access** holds what Claude can reach, in four tabs:

* **Bundles**: named sets of connectors, repositories, domains, plugins, and instructions that you add to more than one place. See [bundle](/docs/claude-tag/concepts/glossary#access-bundle) in the glossary.
* **Connectors**: each service Claude connects to, its credentials, and where Claude may use each one
* **Skills and plugins**: the skills and plugins Claude uses anywhere in Slack
* **Channels**: **Slack**, whose page holds the settings for every workspace and channel, then each connected workspace with its channel rules and channels

On the **Channels** tab, select **Slack** to change how Claude works everywhere, or select a workspace or channel to change it in that one place. A workspace or channel inherits what's set above it. Its own instructions and access add to what it inherits, and its own model replaces the inherited one.

| To do this | Go to | Learn more |
| :- | :- | :- |
| Change the model Claude replies with | **Model** at the top of the Claude Tag page to change the default everywhere, or **Model** on a workspace's or channel's page. | [Choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope) |
| Give Claude standing instructions | **Slack instructions** on the **Slack** page for every channel, or **Channel instructions** on one channel's page for that channel only. | [Customize](/docs/claude-tag/admins/customize) |
| Connect a tool | **Add** on the **Connectors** tab. | [Give Claude access](/docs/claude-tag/admins/add-connections) |
| Let Claude reach a site or API that has no credential | **Add > Domain** under **What's in it** on a bundle's page. | [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) |
| Grant more repositories | The **GitHub** page, which you open from the **Connectors** tab. | [Configure GitHub access](/docs/claude-tag/admins/configure-github) |
| Give one channel more than the default | The channel's page, from the **Channels** tab: **Add** under **Claude's access**, then pick what to add, such as **Connector**, **Domain**, or **Bundle**. | [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope) |
| Limit where Claude works or who can use it | | [Restrict where Claude operates](/docs/claude-tag/admins/restrict-access) |
| Require review of personal connector results | On the Enterprise plan, the **Personal connectors** section of the admin page. | [Admin controls for personal connectors](/docs/claude-tag/concepts/personal-connectors#admin-controls-for-personal-connectors) |
| Pair another workspace, or disconnect one | **Connected workspaces** on the **Slack** page. Disconnecting permanently deletes the workspace's Claude data. See [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle). | [Manage workspaces](/docs/claude-tag/admins/workspaces) |
| Change the spend limit | [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag). | [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) |
| Turn Claude Tag off | The **Enable Claude Tag in Slack** switch at the top of the Claude Tag page. It also turns off direct messages. | [Turn Claude Tag on or off](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) |
| Bring in the first users | | [Getting started for users](/docs/claude-tag/users/getting-started) |

## Common setup issues

Every message setup can show instead of the next step, matched to its fix, is in [Setup errors](/docs/claude-tag/admins/troubleshooting#setup-errors) on the troubleshooting page.

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): what happens between a mention and a reply
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why Claude gets its own accounts, and what that means for audit logs and access
* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope#how-scopes-inherit): how Slack, workspaces, and channels inherit bundles
* [Claude Tag settings map](/docs/claude-tag/concepts/settings-map): every setting, and whether admins, channel members, or users control it
* [Glossary](/docs/claude-tag/concepts/glossary): bundle, scope, session, and the other terms on this page
* [Network requirements](/docs/claude-tag/admins/network-requirements): what your services must allowlist so Claude can reach them
* [Claude Tag in production at Anthropic](https://claude.com/blog/ai-ci-cd-on-call): how Anthropic runs Claude Tag as its first responder for CI/CD failures

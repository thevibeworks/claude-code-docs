> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Work with Claude Tag

> Claude Tag puts Claude in your Slack channels with admin-governed access. See what to hand it, how setup works, and where to start as an admin or end user.

<div className="tm-hero">
  <div className="tm-hero-copy">
    <span className="tm-pill">Public Beta</span>
    <p className="tm-hero-title">Tag <span className="tm-hero-at">@Claude</span> in. Get results back in the thread.</p>
    <p className="tm-hero-lede">Anyone in a channel can tag Claude into a problem and hand it work: reproduce a bug and open a pull request, turn a decision thread into a doc, assemble the state of a project. It posts a checklist in the thread as it goes, and the whole exchange stays visible to the channel.</p>

    <div className="tm-hero-ctas">
      <a className="tm-btn tm-btn-dark" href="/docs/docs/claude-tag/admins/setup-overview">I'm setting it up →</a>
      <a className="tm-btn tm-btn-light" href="#put-claude-tag-to-work">Use it in your channel ↓</a>
    </div>
  </div>

  <div className="tm-slack">
    <div className="tm-slack-head">
      <span className="tm-slack-chan"># platform-eng</span>
      <span className="tm-slack-members">38 members</span>
    </div>

    <div className="tm-slack-body">
      <div className="tm-msg">
        <span className="tm-avatar tm-avatar-user" aria-hidden="true">D</span>

        <div className="tm-msg-col">
          <div className="tm-msg-meta"><span className="tm-msg-name">Dana</span><span className="tm-msg-time">2:14 PM</span></div>
          <p>checkout has felt slow all morning — anyone else seeing it?</p>
        </div>
      </div>

      <div className="tm-msg">
        <span className="tm-avatar tm-avatar-user tm-avatar-b" aria-hidden="true">L</span>

        <div className="tm-msg-col">
          <div className="tm-msg-meta"><span className="tm-msg-name">Leo</span><span className="tm-msg-time">2:15 PM</span></div>
          <p>same. <span className="tm-mention">@Claude</span> can you investigate? Compare latency against this morning's deploy and find what's causing it.</p>
        </div>
      </div>

      <div className="tm-msg">
        <span className="tm-avatar tm-avatar-claude">
          <img src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12" alt="" noZoom width="94" height="94" data-path="images/claude-tag/logo/clay-spark.svg" />
        </span>

        <div className="tm-msg-col">
          <div className="tm-msg-meta"><span className="tm-msg-name">Claude</span><span className="tm-msg-app">APP</span><span className="tm-msg-time">2:15 PM</span></div>
          <p>On it. I'll compare latency before and after the deploy, track down the cause, and report back here.</p>

          <div className="tm-tasklist">
            <span className="tm-task-done"><span className="tm-sr">Done: </span>Pulled p99 latency from Datadog</span>
            <span className="tm-task-done"><span className="tm-sr">Done: </span>Diffed deploy 4f2c1 against main</span>
            <span className="tm-task-done"><span className="tm-sr">Done: </span>Reproduced the slow query locally</span>
            <span className="tm-task-doing"><span className="tm-sr">In progress: </span>Opening a pull request with the fix…</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

## Plans that include Claude Tag

Claude Tag is available on Team and Enterprise plans, on Anthropic's first-party service. It isn't available on individual plans (Free, Pro, or Max), or for third-party deployments. To use it, your organization pairs its Slack workspace with its Claude organization; see [the setup overview](/docs/claude-tag/admins/setup-overview) for the full prerequisites.

If you're choosing between Claude products for Slack-shaped work, [how Claude Tag differs from Cowork and Claude Code](/docs/claude-tag/concepts/how-it-works#how-claude-tag-differs-from-cowork-and-claude-code) compares them directly: team work in shared channels is Claude Tag; personal work on your own files is Cowork or Claude Code.

## Where Claude Tag runs

Claude Tag works in Slack. You interact with it by writing in a Slack channel, thread, or direct message, and it replies there. Mention `@Claude` in a channel to guarantee it picks the message up.

When Claude works on a task, it runs in an ephemeral sandbox, not on your computer. The sandbox is created when a conversation starts, holds any code or files Claude is working with, and is discarded when the conversation goes idle. See [how Claude Tag works](/docs/claude-tag/concepts/how-it-works) for the full lifecycle.

You extend what Claude can reach, like your repositories, ticketing systems, data warehouses, and custom tools, through [connections](/docs/claude-tag/admins/add-connections), [plugins, and skills](/docs/claude-tag/admins/customize). An Owner configures these per scope (a channel, a workspace, or the whole organization), separately from any connectors an individual user has set up in their own claude.ai account.

<div className="tm-route-grid">
  <div className="tm-card">
    <a className="tm-band tm-band-admins" href="/docs/docs/claude-tag/admins/setup-overview">
      <span className="tm-band-text">
        <span className="tm-band-label">For administrators</span>
        <span className="tm-band-title">Set up Claude Tag</span>
      </span>

      <img src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/illustrations/Hand-Key.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=1b7a9675728f971bc7a4663c7f1ea599" alt="" noZoom width="1000" height="1000" data-path="images/claude-tag/illustrations/Hand-Key.svg" />
    </a>

    <div className="tm-qrows">
      <a className="tm-qrow" href="/docs/docs/claude-tag/admins/setup-overview">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">Where do I start?</span>
          <span className="tm-qrow-sub">Pair your Slack workspace, connect the services Claude will work in, launch, and test that it works</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/concepts/agent-identity">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">What can Claude Tag access?</span>
          <span className="tm-qrow-sub">How admins set access per channel, and where credentials are stored</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/admins/add-connections">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">How do I connect each service?</span>
          <span className="tm-qrow-sub">Credential types, allowed hosts, and what each connection lets Claude reach</span>
        </span>
      </a>
    </div>
  </div>

  <div className="tm-card">
    <a className="tm-band tm-band-users" href="#put-claude-tag-to-work">
      <span className="tm-band-text">
        <span className="tm-band-label">For end users</span>
        <span className="tm-band-title">Put Claude Tag to work</span>
      </span>

      <img src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/illustrations/Hand-NodePair.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=c64df4c6d27a6da752aa32c9e0622781" alt="" noZoom width="1000" height="1000" data-path="images/claude-tag/illustrations/Hand-NodePair.svg" />
    </a>

    <div className="tm-qrows">
      <a className="tm-qrow" href="/docs/docs/claude-tag/users/getting-started">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">How do I hand Claude Tag a task?</span>
          <span className="tm-qrow-sub">Mention Claude in any channel it's in, with nothing to install</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/users/use-cases">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">What is Claude Tag good at?</span>
          <span className="tm-qrow-sub">Use cases for coding, data, incidents, and go-to-market</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/users/good-habits">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">How do I get good results?</span>
          <span className="tm-qrow-sub">Good habits for scoping and reviewing work</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/users/memory">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">What does Claude Tag remember?</span>
          <span className="tm-qrow-sub">Channel memory, what's shared across the workspace, and who can see what</span>
        </span>
      </a>

      <a className="tm-qrow" href="/docs/docs/claude-tag/users/proactivity">
        <span className="tm-qrow-text">
          <span className="tm-qrow-q">Can Claude Tag run tasks on a schedule?</span>
          <span className="tm-qrow-sub">Scheduled jobs, channel watching, and triggers</span>
        </span>
      </a>
    </div>
  </div>
</div>

## Billing and spend limits

Adding Claude to Slack doesn't add a per-seat charge. Channel and thread work is billed by usage instead: it draws from a **usage balance**, an amount in your organization's billing currency that an Owner funds. A [spend limit](/docs/claude-tag/admins/set-spend-limit) caps how much of that balance Claude Tag can use each billing period.

Direct messages don't draw from this balance. A DM runs on the sender's own claude.ai account and follows that seat's usual usage limits, so the organization spend limit doesn't apply to it.

To learn what your team's usage costs, run a pilot with a spend limit set and watch the per-channel breakdown on the [usage page in your admin settings](https://claude.ai/admin-settings/usage/claude-tag). Your organization may already have a [launch usage credit](https://support.claude.com/en/articles/15575654-claude-tag-launch-promo-for-claude-team-and-enterprise) to run that pilot against before it funds the balance itself.

[Set a spend limit](/docs/claude-tag/admins/set-spend-limit) covers how to fund the balance on each plan, set the limit, and what happens when usage reaches it.

<div className="tm-eyebrow"><span className="tm-swatch tm-swatch-users" />For end users</div>

## Put Claude Tag to work

If Claude Tag is in your channel, you can use it now. (If it isn't there yet, an Owner in your Claude organization runs setup: see [Set up Claude Tag](/docs/claude-tag/admins/setup-overview).) Anyone in the channel can hand it work, and channel work bills to the organization, not to you.

What it can reach depends on the channel you're in, not on who you are. The fastest way to find out is to ask it: `@Claude what can you access from this channel?` Or, if you're signed in to your Claude organization, click **Configure** in the footer of a Claude reply in the channel to see its [connections](/docs/claude-tag/concepts/glossary#connection), the external services an admin has connected for that channel. Replies in org-shared channels have no Configure link.

The one exception is a DM, where it runs on your own claude.ai account instead of the channel's setup. Owners can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

### Common uses

The list below covers common ways teams use Claude Tag. Each link opens a guide with the prompts to paste and the connections the task needs.

* [Watch monitors and alerts](/docs/claude-tag/users/use-cases/watch-monitors): scheduled dashboard checks, and alerts investigated as they arrive. Needs a monitoring connection like Datadog, Sentry, or PagerDuty.
* [Triage requests](/docs/claude-tag/users/use-cases/triage-requests): an intake channel where Claude answers what it can, flags duplicates, and routes the rest. Works on Slack content alone.
* [Find answers in your docs](/docs/claude-tag/users/use-cases/find-answers): policy and runbook questions answered with the source. Needs a docs connection like Google Drive, Notion, or Confluence.
* [Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions): a plain-language question becomes a warehouse query and a chart. Needs a data warehouse connection.
* [Track projects and chase approvals](/docs/claude-tag/users/use-cases/track-projects): standing status digests and follow-ups that run until an approval lands
* [Turn threads into docs and tickets](/docs/claude-tag/users/use-cases/create-artifacts): a settled discussion becomes the decision doc, the customer reply, or the filed tickets
* [Fix bugs](/docs/claude-tag/users/use-cases/fix-bugs): a bug reported in the channel comes back as a draft pull request. Needs GitHub.
* [Work from your own channel](/docs/claude-tag/users/use-cases/your-own-channel): scratch questions, digests of channels you don't follow, and follow-ups on what you said you'd do

[Get started](/docs/claude-tag/users/getting-started) covers your first message, what you see while Claude works, and how to shape Claude's behavior in your channel.

<div className="tm-eyebrow"><span className="tm-swatch tm-swatch-admins" />For administrators</div>

## Set Claude Tag up once for everyone

You set up Claude Tag once, at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and you must be an Owner in your Claude organization to do it. The setup page at that URL walks you through it:

* **Pair your Slack workspace**: send `@Claude connect` in Slack to get a pairing code, then enter it on the setup page.
* **Connect the services Claude will work in**: for each one, such as your issue tracker or data warehouse, create an account for Claude and enter its credential.
* **Grant repositories**: choose which repositories the Claude GitHub App can reach.
* **Set a monthly spend limit and launch**.

Claude Tag starts with no access to your external systems. The services you connect during setup form an [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle), the set of tools Claude can reach, attached to the workspace or channels you paired. Once you launch, everyone in a channel Claude is in can use Claude Tag immediately, with no per-user setup.

[Set up Claude Tag](/docs/claude-tag/admins/setup-overview) walks through those steps with what to have ready, what each choice means, and how to verify Claude Tag works once you launch.

<div className="tm-strip">
  <div className="tm-strip-head">
    <p className="tm-strip-title">Security review</p>
    <a className="tm-strip-all" href="/docs/docs/claude-tag/concepts/security-and-data">Security and data handling</a>
  </div>

  <p>The security model, what admins can and can't restrict, audit trails, and network requirements.</p>
</div>

## Where to start with Claude Tag

<CardGroup cols={2}>
  <Card title="Set up Claude Tag" icon="gear" href="/docs/claude-tag/admins/setup-overview" horizontal arrow>
    Admins: pair your Slack workspace, connect the services Claude will work in, and launch
  </Card>

  <Card title="Hand Claude Tag your first task" icon="paper-plane" href="/docs/claude-tag/users/getting-started" horizontal arrow>
    It's already in your channel: send your first message
  </Card>

  <Card title="How Claude Tag works" icon="diagram-project" href="/docs/claude-tag/concepts/how-it-works" horizontal arrow>
    The session model, what it can read, and how memory follows places
  </Card>

  <Card title="Use case library" icon="list" href="/docs/claude-tag/users/use-cases" horizontal arrow>
    Prompts to paste, by team and connection
  </Card>
</CardGroup>

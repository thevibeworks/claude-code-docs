> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Claude Tag for on-call

> Put Claude on call for incident response in Slack: run setup at claude.ai/oncall, pick or auto-join incident channels, cap spend, and deploy.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag on-call puts Claude on call with your team for incident response in Slack. Claude watches your monitoring tools and posts what it finds, or joins your incident channels and investigates alongside your team. Your team keeps its own on-call rotation, and Claude works alongside whoever is on call. You set up on-call for your whole organization at [`claude.ai/oncall`](https://claude.ai/oncall).

On-call is available on the Team and Enterprise plans. Who can open [`claude.ai/oncall`](https://claude.ai/oncall) and run setup depends on your plan.

* **Team plan:** any member of your organization. A change that affects the whole organization saves only if your account has permission to make it.
* **Enterprise plan:** an Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration), meaning a member whose custom role sets **Claude Tag Admin** to **Can manage**. Other members, including those with the built-in **Admin** role and [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers), don't see **On-call** in the **Code** sidebar and can't open setup.

## What an on-call is

Your organization's on-call is an [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) carrying the connections, repositories, and skills Claude uses for incident work. The bundle attaches to the channels you pick during setup, and any [routines](/docs/claude-tag/concepts/glossary#routine) you schedule in those channels, like a morning incident digest, run alongside it. Setup builds the bundle, and after you deploy you edit it like any other bundle in [Give Claude access](/docs/claude-tag/admins/add-connections).

Setup offers two ways for Claude to work, and you can use either or both.

* **Watch your alerts.** Claude watches your monitoring tools and posts what it finds in a channel you choose.
* **Join incident channels.** Claude joins the incident channels you pick and investigates alongside your team, without waiting to be tagged. A channel-name prefix, like `incident-`, has Claude join new public channels that match.

On-call work is billed to your organization as usage. You can cap it with a monthly spend limit. [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) covers what counts toward the limit and what happens when it's reached.

## Run setup

Go to [`claude.ai/oncall`](https://claude.ai/oncall), or open [**Code**](https://claude.ai/code) in claude.ai and click **On-call** in its sidebar. The page shows one on-call for your whole organization, so anyone else who can open it sees the same settings.

The page opens on setup cards for your organization's shared on-call. The cards cover what Claude needs for incident work, such as connecting monitoring and alerting tools, granting repositories, and picking the Slack channels Claude works in. Act on each card, then click the **Deploy on-call** button to put Claude on call in the channels you chose.

If you'd rather be interviewed than work through the cards yourself, click the **Chat to set up on-call** button. Claude asks how your team runs incidents and sets up the on-call from your answers.

## Channels Claude joins

During setup you pick the Slack channels where Claude does its on-call work. You can name channels directly, set a channel-name prefix, or both.

* **Pick channels.** Choose the channels Claude should work in. To add a private channel, type `/invite @Claude` in that channel in Slack.
* **Set a channel-name prefix.** A prefix, like `incident-`, has Claude join matching channels automatically, so a channel opened mid-incident gets Claude without anyone adding it.

A prefix applies to new public channels only. Claude joins when a channel is created with a matching name or renamed to one, and the joined channel gets the on-call's connections, repositories, and skills. A prefix never adds Claude to a private channel or to a channel shared with another organization. A private channel whose name matches gets the on-call's access once someone invites Claude to it.

A prefix matches channel names literally, so wildcards aren't accepted. It takes lowercase letters, numbers, hyphens, periods, and underscores, runs 3 to 79 characters, and starts with a letter or number.

## Let your team know

Setup includes an option to have Claude introduce itself to your team after you deploy. Leave it on, and Claude sends a direct-message introduction to each member of your Slack workspace who has a Claude account in your organization, and to no one else. Each of those members gets the introduction once, as up to three messages, with no follow-ups, and the messages don't count toward your usage. Turn the option off to skip the introductions. Members can use Claude either way once the on-call is live.

## After you deploy

Claude is on call in the channels you chose, and, if you set a channel-name prefix, it joins new public channels that match as they're created. The on-call's connections, repositories, and skills make up its [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle). To change the on-call later, go to [`claude.ai/oncall`](https://claude.ai/oncall). Outside setup, these roles manage the on-call's Access bundle:

* **Owner:** edit the bundle in [Give Claude access](/docs/claude-tag/admins/add-connections), [set per-channel access](/docs/claude-tag/admins/attach-to-scope), and [change the monthly spend limit](/docs/claude-tag/admins/set-spend-limit)
* **[Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration), on the Enterprise plan:** edit the bundle and set per-channel access

## Related resources

* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): the standard setup steps, and how to verify your setup afterward
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why Claude gets its own accounts in your tools
* [Watch monitors and alerts](/docs/claude-tag/users/use-cases/watch-monitors): what Claude's monitoring work looks like in a channel

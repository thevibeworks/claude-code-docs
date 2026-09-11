> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Personal connectors in channels

> Claude can use your own claude.ai connectors, called personal connectors, for your tasks in a Slack channel. See how you approve connector use, when Claude asks you to review a result before posting it, and what other people in the channel can reach.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Personal connectors are the tools you add to your own claude.ai account, like your calendar or your email. When a task you ask for in a Slack channel needs one of your own tools, Claude can offer to use your connector for it.

Connector use in channels is available to a limited number of organizations. If Claude never offers to use your connectors in a channel, connector use in channels may not be available to your organization, and the channel works with admin-attached connections as described in [how agent identity works](/docs/claude-tag/concepts/agent-identity).

## Where your connectors apply

In a channel, an admin decides the shared access. The channel uses the connections an admin attached to it, and everyone who asks there gets the same access. In organizations where connector use in channels is available, Claude can also use the connectors on your own claude.ai account in that channel. When you ask Claude there for something that needs one of your own tools, it can use your connector for your task.

In a direct message (DM), your connectors apply on their own, because a DM runs on [your own claude.ai account](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

[Routines](/docs/claude-tag/users/proactivity) and other work Claude starts on its own in a channel use the channel's connections, never your connectors. Claude uses your connectors only while working on a request you made yourself.

Your connectors serve only you. When someone else in the channel asks Claude for something, their request doesn't control or use your connectors, even in a shared channel. Claude works with your permissions, reaches only what your account can reach, and records what it does under your name.

To add or remove connectors on your account, open the **Customize > Connectors** page on claude.ai; see [connectors on claude.ai](/docs/connectors/overview) for setup.

## Control connector use

### Approve connector use

By design, Claude asks before it starts using your connectors in a channel. The first time a task calls for one of your connectors, Claude shows you a prompt in the thread that only you can see, with three choices:

* **Allow** starts the work in auto mode. Claude uses your connectors as the task needs them and checks with you before posting anything that looks sensitive.
* **Allow with review** starts the work and shows you every result to approve before it posts to the channel.
* **Don't allow** declines this request, and Claude doesn't use your connectors. A later request can prompt you again.

To save **Allow** or **Allow with review** for future tasks in every channel, select the **Use this choice for future requests** checkbox on the prompt before you choose. Once you've saved a choice, Claude starts a task you @-mention it for without showing the prompt.

To change a saved answer, open the Claude app in Slack and select its **Home** tab. The **Home** tab offers **Auto mode**, **Ask every time**, and **Allow with review**. **Ask every time** is the setting before you save a choice.

### Review results before posting

Claude can hold a result and show it to you before anything posts to the channel. When you chose **Allow with review**, Claude holds every result. When you chose **Allow**, Claude holds a result when the content looks sensitive and posts the rest directly. Once you approve a held result, Claude posts it in the thread where you asked.

On the Enterprise plan, an Owner can set the review rule for a scope with the **Delegated task results** setting, at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → the scope → **Advanced** → **Delegated task results**. **Require review** removes **Allow** from the prompt and **Auto mode** from the **Home** tab, so Claude holds every result for your review. **Share without review** removes **Allow with review** from both.

### Stop connector use

To stop a task that's using your connectors, select **Stop** under the message in the task's thread where Claude says it's going to use your connectors. Only you can see the **Stop** button.

## What other people in the channel see

Results stay visible in the channel. What Claude posts back to a channel thread is readable by everyone there, like any other work Claude does in a channel. Claude's detailed work on a task you approved lives in a session only you can open. The work runs with your permissions and is recorded under your name.

Other people can't use your connectors. Requests other people make to Claude in your task's thread run with the channel's own access, not with yours.

While Claude works on your connector task, it is designed to take direction from you and to treat what other people post in the thread as information for the task rather than as instructions.

## Related resources

* [How agent identity works](/docs/claude-tag/concepts/agent-identity): whose identity and access Claude uses in channels and DMs
* [Connectors](/docs/connectors/overview): set up and manage connectors on your claude.ai account
* [Get started](/docs/claude-tag/users/getting-started): hand Claude your first task in a channel

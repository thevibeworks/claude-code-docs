> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Tag at a healthcare organization

> Claude Tag is not covered by Anthropic's Business Associate Agreement. Configure it so protected health information never reaches a channel, direct message, or tool Claude can read: limit Claude to approved channels, turn off direct messages, and connect only PHI-free tools. Also covers what to do if PHI is posted where Claude can read it.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag, the Claude app that works in your Slack channels, is not covered by Anthropic's Business Associate Agreement (BAA). A healthcare organization can use it for work that doesn't involve protected health information (PHI) by configuring it so that PHI never enters a channel, direct message, or connected tool that Claude can read.

This page is for the Claude organization Owner and the compliance lead deciding where Claude works. It describes how to configure Claude Tag so PHI stays out of Claude's reach. It is not legal advice. Review your setup with your legal and compliance teams before you turn Claude on.

## What Claude can read in Slack

Claude reads Slack with the same visibility a member of your workspace has. In a Slack workspace connected to your Claude organization, Claude can:

* Read and post in the channels it has been added to
* Search every public channel by keyword, including public channels it hasn't been added to. [No admin setting turns this search off](/docs/claude-tag/admins/restrict-access#controls-that-aren%E2%80%99t-available)
* Read a private channel only after someone in that channel invites it

Claude never searches private channels, and it doesn't reply in [Slack Connect channels](/docs/claude-tag/admins/restrict-access#slack-connect-channels), the channels your workspace shares with another company.

For a healthcare organization, the rule that follows is to keep PHI out of every public channel in the connected workspace, not only the channels where Claude responds, because Claude's keyword search reaches all of them. Keep PHI out of any private channel Claude has been invited to as well.

For how Claude's work in each thread is isolated, how connection credentials are held, and where network traffic can go, see [Security and data handling](/docs/claude-tag/concepts/security-and-data).

## Plan and organization requirements

Keeping PHI out of Claude's reach needs two things beyond the [general prerequisites for Claude Tag](/docs/claude-tag/admins/setup-overview):

* **An Enterprise plan.** Limiting Claude to a list of approved channels uses the **Claude Tag version** setting, which you set separately for the whole workspace and for each channel. Each of those is a [scope](/docs/claude-tag/admins/attach-to-scope). Per-scope version settings are available on the Enterprise plan.
* **A Claude organization without Zero Data Retention (ZDR) or customer-managed encryption keys.** Claude Tag stores session transcripts and channel memory, so it [isn't available to an organization with either policy](/docs/claude-tag/concepts/security-and-data). If your organization needs ZDR or customer-managed keys for other Claude products, ask your account team about creating a separate Claude organization without those policies and connecting your Slack workspace to that organization instead.

## Limit Claude to PHI-free channels

An Owner turns Claude off everywhere by default, turns it on only in channels approved as PHI-free, turns off direct messages, and blocks channel names that signal PHI. Every setting in these steps is at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag).

<Steps>
  <Step title="Turn Claude off by default">
    Go to **Claude Tag's access** → **Slack** → **Default Slack** → **Advanced** → **Claude Tag version** and set it to **Off**. [Limit Claude Tag to specific channels](/docs/claude-tag/admins/restrict-access#limit-claude-tag-to-specific-channels) has the full procedure.
  </Step>

  <Step title="Reset workspace and channel entries that override Off">
    A workspace or channel entry's own **Claude Tag version** setting takes precedence over **Default Slack**, so an entry left on **New** or **Legacy** from an earlier pilot keeps Claude active there. Under **Claude Tag's access** → **Slack**, open each workspace and channel entry whose **Claude Tag version** is **New** or **Legacy** and set it to **Inherit**.
  </Step>

  <Step title="Turn Claude on in each approved channel">
    Go to **Claude Tag's access** → **Slack**, select the entry for the approved channel, then go to **Advanced** → **Claude Tag version** and set it to **New**. **New** turns Claude on in that channel. If the channel isn't listed under **Slack**, [add the channel with **Add channel**](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) first.
  </Step>

  <Step title="Turn off direct messages">
    On the same [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) page, turn off the [**Allow direct messages** toggle](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages). Claude is then reachable only in channels.
  </Step>

  <Step title="Block channel names that signal PHI">
    Go to **Claude Tag's access** → **Slack** → **Default Slack** → **Advanced** → **Blocked channel patterns** and add the naming patterns your workspace uses for clinical or patient channels, for example `*-patient-*`. Claude won't read or respond in a matching channel even if someone invites it. See [Block or auto-join channels by name](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name).
  </Step>
</Steps>

Any member of the workspace can still invite `@Claude` to a channel that isn't approved. Claude stays silent there, and an @-mention gets a notice that Claude is disabled in that channel instead of a reply. Only an Owner of your Claude organization can change a **Claude Tag version** setting or the **Allow direct messages** toggle.

## Connect only PHI-free tools

In a channel, Claude signs in to tools outside Slack only through the connections an Owner adds, and each connection is attached to specific channels through an [access bundle](/docs/claude-tag/admins/attach-to-scope). For a healthcare organization, apply these rules when deciding what to connect:

* Connect only tools that never hold PHI, such as your code host, issue tracker, and internal documentation
* Leave electronic health record systems, clinical systems, and patient communication tools unconnected
* Treat email and calendar as PHI-bearing unless your compliance team has confirmed otherwise, and leave them unconnected until then
* Attach each bundle to the approved channels that need it, not to **Default Slack** (the entry whose settings apply to every channel in every connected workspace), so a connection never reaches a channel it wasn't reviewed for

Members' own claude.ai connectors, such as their email or calendar, are a separate path to tools outside Slack. In a direct message, Claude works on the member's own Claude account and can use those connectors, so keep the **Allow direct messages** toggle off as described in [Limit Claude to PHI-free channels](#limit-claude-to-phi-free-channels). In channels, [personal connector use](/docs/claude-tag/concepts/personal-connectors) is available to a limited number of organizations. Ask your account team whether it is enabled for yours before you turn Claude on, and if it is, include members' claude.ai connectors in the tools that must stay PHI-free.

## Train your workspace and monitor approved channels

Settings keep Claude out of unapproved channels and tools. They don't stop a person from typing PHI where Claude can read it. Train everyone in the workspace that patient information never goes in a public channel, in a channel Claude has been added to, or in a tool Claude is connected to. Run your data loss prevention tooling on the approved channels to catch mistakes.

## What Claude Tag stores

Anthropic stores two things for the conversations Claude works in. The first is a transcript of each conversation, which includes everything Claude read while working. The second is the memory notes Claude keeps for each channel.

Memory from public channels goes into one store for the whole workspace, so something Claude noted in one public channel can inform its replies in another channel. Memory from a private channel stays in that channel's own store and isn't read anywhere else.

Anyone in a channel can ask Claude what it remembers there and tell it to correct or delete a note. An Owner can view, edit, and delete the memory notes of a channel or of the workspace at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → the channel's or workspace's entry → options menu → **View memory files**.

By default, your Slack conversations with Claude aren't used to train Anthropic's models. Anthropic's [model training policy](https://privacy.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training) describes when data is used. Claude Tag data is kept until one of the admin actions in [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle) deletes it, and during the beta you can't set a shorter retention period.

For the full list of what is stored and what each admin action deletes, see [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle) and [What Claude Tag remembers](/docs/claude-tag/users/memory).

## If PHI is posted where Claude can read it

Anthropic keeps a transcript of each conversation Claude works in, including the messages Claude read. Deleting a message in Slack doesn't remove it from a transcript that already includes it. If PHI is posted in a channel where Claude is turned on, in any public channel of the connected workspace, or in a private channel Claude has been invited to:

1. Report it to your organization's HIPAA privacy officer and follow your incident process.
2. Delete the message in Slack.
3. If the message was posted in a channel where Claude is turned on, have an Owner delete that channel's transcripts and memory immediately by [removing the channel's entry](/docs/claude-tag/concepts/data-lifecycle#delete-data-or-request-deletion) under **Claude Tag's access** → **Slack**.
4. If that channel is public, have an Owner also check workspace memory, because notes Claude saved from a public channel are stored with the workspace and aren't deleted with the channel's entry. Go to **Claude Tag's access** → **Slack** → your workspace's entry → options menu → **View memory files**, and delete any note that contains the information. Deleting a note removes it from what Claude reads in every channel right away.
5. Email [privacy@anthropic.com](mailto:privacy@anthropic.com) to request deletion of the data Claude Tag retained that the admin controls in steps 3 and 4 don't delete, including the workspace's stored memory and any transcript in another channel whose session found the message through search. Include the workspace, the channel, and the time of the message.

Removing a channel's entry also turns Claude off in that channel, because the channel then inherits the **Off** you set on **Default Slack**. To turn Claude back on later, add the channel again under **Claude Tag's access** → **Slack** and set its **Claude Tag version** to **New**.

## Related resources

* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): every control that narrows where Claude responds and who can use it
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): sandbox isolation, credential handling, and network egress
* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): what Anthropic stores and how to delete it

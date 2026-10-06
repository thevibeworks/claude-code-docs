> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Tag at a healthcare organization

> Claude Tag is not covered by Anthropic's Business Associate Agreement. Configure it so protected health information never reaches a channel, direct message, or tool Claude can read: limit Claude to approved channels, turn off direct messages, and connect only PHI-free tools. Also covers what to do if PHI is posted where Claude can read it.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag, the Claude app that works in your Slack channels, is not covered by Anthropic's Business Associate Agreement (BAA). A healthcare organization can use it for work that doesn't involve protected health information (PHI) by configuring it so that PHI never enters a channel, direct message, or connected tool that Claude can read.

If your Claude organization has the [HIPAA configuration](https://support.claude.com/en/articles/17318731) applied to Claude Code (local mode) and Cowork (local mode), Claude Tag isn't available in that organization. [Plan and organization requirements](#plan-and-organization-requirements) describes the alternative.

This page is for the Claude organization's Owners and the compliance lead deciding where Claude works. It describes how to configure Claude Tag so PHI stays out of Claude's reach. It is not legal advice. Review your setup with your legal and compliance teams before you turn Claude on.

## What Claude can read in Slack

Claude reads Slack with the same visibility a member of your workspace has. In a Slack workspace connected to your Claude organization, Claude can:

* Read and post in the channels it has been added to
* Search every public channel by keyword, including public channels it hasn't been added to. [No admin setting turns this search off](/docs/claude-tag/admins/restrict-access#controls-that-aren%E2%80%99t-available). An Owner can [limit it to channels Claude is in](/docs/claude-tag/admins/restrict-access#limit-which-channels-claude-can-search).
* Read a private channel only after someone in that channel invites it

Claude never searches private channels, and it doesn't reply in [Slack Connect channels](/docs/claude-tag/admins/restrict-access#slack-connect-channels), the channels your workspace shares with another company.

For a healthcare organization, the rule that follows is to keep PHI out of every public channel in the connected workspace, not only the channels where Claude responds, because Claude's keyword search reaches all of them by default. Keep PHI out of any private channel Claude has been invited to as well.

For how Claude's work in each thread is isolated, how connection credentials are held, and where network traffic can go, see [Security and data handling](/docs/claude-tag/concepts/security-and-data).

## Plan and organization requirements

Limiting Claude to approved channels needs an [Enterprise plan](https://claude.com/pricing), in addition to the [general prerequisites for Claude Tag](/docs/claude-tag/admins/setup-overview). The Enterprise plan has a [setting that turns Claude on or off for an individual channel](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope).

Claude Tag [isn't available in a Claude organization](/docs/claude-tag/concepts/security-and-data) that has any of these:

* Zero Data Retention (ZDR)
* Customer-managed encryption keys
* The HIPAA configuration applied to Claude Code (local mode) and Cowork (local mode)

Ask your account team about creating a separate Claude organization without those policies and connecting your Slack workspace to the separate organization instead.

## Limit Claude to PHI-free channels

An Owner turns Claude off everywhere by default, turns it on only in channels approved as PHI-free, turns off direct messages, and blocks channel names that signal PHI. Every setting in these steps is at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), and the workspace and channel settings are on the **Channels** tab under **Claude's access**.

<Steps>
  <Step title="Turn Claude off by default">
    Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack) and turn off the **Respond in all channels** switch at the top of the **General** tab. [Limit Claude Tag to specific channels](/docs/claude-tag/admins/restrict-access#limit-claude-tag-to-specific-channels) has the full procedure.
  </Step>

  <Step title="Reset workspaces and channels that have their own setting">
    A workspace's or channel's own **Enable Claude Tag** setting takes precedence over the **Slack** page, so a workspace or channel switched on during an earlier pilot keeps Claude active there. On the **Channels** tab, open each workspace's and channel's page that has its own setting, and click the **Use inherited setting** link under its switch.
  </Step>

  <Step title="Turn Claude on in each approved channel">
    On the **Channels** tab, open the approved channel's page and turn on its **Enable Claude Tag in this channel** switch. If the channel isn't listed on the **Channels** tab, [set it up](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) first.
  </Step>

  <Step title="Turn off direct messages">
    On the same [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) page, select **Edit** on the **Direct messages** row and turn off the [**Allow direct messages** toggle](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages). Claude is then reachable only in channels.
  </Step>

  <Step title="Block channel names that signal PHI">
    Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack), open the **Advanced** tab, and under **Channels** add the naming patterns your workspace uses for clinical or patient channels to **Blocked channel patterns**, for example `*-patient-*`. Claude won't read or respond in a matching channel even if someone invites it. See [Block or auto-join channels by name](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name).
  </Step>
</Steps>

Any member of the workspace can still invite `@Claude` to a channel that isn't approved. Claude stays silent there, and an @-mention gets a notice that Claude is disabled in that channel instead of a reply.

Only an Owner of your Claude organization or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) can change the **Respond in all channels** switch or an **Enable Claude Tag** switch, and only an Owner can change the **Allow direct messages** toggle. Give the **Claude Tag Admin** permission only to people you trust to approve a channel as PHI-free.

## Connect only PHI-free tools

In a channel, Claude signs in to tools outside Slack only through Claude Tag connectors. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you add a connector.

For a healthcare organization, apply these rules when deciding what to connect:

* Connect only tools that never hold PHI, such as your code host, issue tracker, and internal documentation
* Leave electronic health record systems, clinical systems, and patient communication tools unconnected
* Treat email and calendar as PHI-bearing unless your compliance team has confirmed otherwise, and leave them unconnected until then
* Add connectors inside bundles, and add each bundle to the approved channels that need it, not to the **Slack** page (whose settings apply to every channel in every connected workspace), so a connector never reaches a channel it wasn't reviewed for

Members' own claude.ai connectors, such as their email or calendar, are a separate path to tools outside Slack. In a one-to-one direct message from a member who has connected a Claude account, Claude works on that member's own Claude account and can use those connectors, so keep the **Allow direct messages** toggle off as described in [Limit Claude to PHI-free channels](#limit-claude-to-phi-free-channels). In channels, Claude can [use a member's own connectors for that member's requests](/docs/claude-tag/concepts/personal-connectors) after the member allows it, and no organization setting turns off personal connectors in channels entirely. These controls apply:

* **Block a connector for everyone.** A connector you restrict for your organization on the [**Connectors** admin page](https://claude.ai/admin-settings/connectors) stays restricted when Claude uses a member's connectors in a channel.
* **Require human review.** On the Enterprise plan, go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), select **Edit** on the **Personal connectors** row, and turn on **Require human review of every message**, so a member reviews every result before it posts to the channel.
* **Treat the rest as PHI-bearing.** Include members' remaining claude.ai connectors in the tools that must stay PHI-free.

## Train your workspace and monitor approved channels

Settings keep Claude out of unapproved channels and tools. They don't stop a person from typing PHI where Claude can read it. Train everyone in the workspace that patient information never goes in a public channel, in a channel Claude has been added to, or in a tool Claude is connected to. Run your data loss prevention tooling on the approved channels to catch mistakes.

## What Claude Tag stores

Anthropic stores two things for the conversations Claude works in. The first is a transcript of each conversation, which includes everything Claude read while working. The second is the memory notes Claude keeps for each channel.

Claude keeps separate notes for each channel. From a public channel it can also save workspace notes, and those inform its replies in every channel in the workspace. Notes from a private channel stay in that channel's own store and aren't read anywhere else.

Anyone in a channel can ask Claude what it remembers there and tell it to correct or delete a note. An Owner can view, edit, and delete the memory notes of the workspace or of a channel. Go to [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels), open the workspace's page (or a channel's page, when that channel has memory of its own), open its **⋯** menu, and select **View memory files**. The **Memory** tab of the [**Activity** page](/docs/claude-tag/admins/audit) opens the same files.

By default, your Slack conversations with Claude aren't used to train Anthropic's models. Anthropic's [model training policy](https://privacy.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training) describes when data is used. Claude Tag data is kept until one of the admin actions in [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle) deletes it, and during the beta you can't set a shorter retention period.

For the full list of what is stored and what each admin action deletes, see [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle) and [What Claude Tag remembers](/docs/claude-tag/users/memory).

## If PHI is posted where Claude can read it

Anthropic keeps a transcript of each conversation Claude works in, including the messages Claude read. Deleting a message in Slack doesn't remove it from a transcript that already includes it. If PHI is posted in a channel where Claude is turned on, in any public channel of the connected workspace, or in a private channel Claude has been invited to:

1. Report it to your organization's HIPAA privacy officer and follow your incident process.
2. Delete the message in Slack.
3. If the message was posted in a channel where Claude is turned on, have an Owner delete that channel's transcripts and memory immediately by [removing the channel's scope](/docs/claude-tag/concepts/data-lifecycle#delete-data-or-request-deletion). On the **Channels** tab under **Claude's access**, open the channel's page and choose **Remove this scope** from its **⋯** menu, if the menu lists it.
4. If that channel is public, have an Owner also check the workspace's memory, because workspace notes Claude saved from that channel are stored with the workspace and aren't deleted with the channel's scope. On the **Channels** tab, open your workspace's page, choose **View memory files** from its **⋯** menu, and delete any note that contains the information. Deleting a note removes it from what Claude reads in every channel right away.
5. Email [privacy@anthropic.com](mailto:privacy@anthropic.com) to request deletion of the data Claude Tag retained that the admin controls in steps 3 and 4 don't delete, including the workspace's stored memory and any transcript in another channel whose session found the message through search. Include the workspace, the channel, and the time of the message.

Removing a channel's scope also turns Claude off in that channel, because the channel then inherits the off setting from the **Slack** page. To turn Claude back on later, [set the channel up again](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) on the **Channels** tab and turn on its **Enable Claude Tag in this channel** switch.

## Related resources

* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): every control that narrows where Claude responds and who can use it
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): sandbox isolation, credential handling, and network egress
* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): what Anthropic stores and how to delete it

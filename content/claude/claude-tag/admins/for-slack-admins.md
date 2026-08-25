> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What the Claude Slack app can access

> What the Claude app reads and posts in Slack, the OAuth scopes it requests, and what installing it does not grant. Written for the Slack admin approving the install.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

You're approving the Claude app install for someone who's setting up Claude Tag. This page covers what the app can do in your Slack workspace. The rest of setup happens on their side, in the Claude console; you don't need a Claude account.

## Where Claude reads and posts

Claude reads and posts only in channels it has been added to, and in direct messages. Any workspace member who opens a direct message with Claude receives its welcome message, whether or not they've linked a Claude account. Installing the app does not add it to any channel.

A member can add Claude to a channel in one of two ways:

* Invite it with `/invite @Claude` in the channel
* Select **Add to channel** on a channel Claude suggests in a direct message. Claude's welcome message, the introduction it posts when a member first opens a direct message with it, suggests public channels this way.

A Claude organization admin can also set [auto-join channel patterns](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name), so Claude joins a public channel whose name matches when the channel is created or renamed.

When a member selects **Add to channel** or an auto-join pattern matches, Claude adds itself to that channel using its `channels:join` scope. Slack's audit log records the join as the Claude app, with no inviter shown; neither the member's selection nor the matched pattern is visible in Slack's log. If you see a join in the audit log that no one can explain, a member selected one of these buttons or an auto-join pattern matched. Outside those two paths, Claude does not join channels on its own.

Reading a channel's full history requires being added there. Workspace search can surface public-channel content, the same as any app with the search scope.

Slack Connect channels (shared with another company) are always excluded, regardless of configuration.

## Requested scopes

The app requests bot scopes for reading and posting in channels it's a member of, reactions, files, canvases, user lookup, and public-channel search. Slack's install consent screen shows the full current list; treat that as the canonical reference, since the set can change between releases.

Two scopes a Slack admin commonly asks about:

* `channels:join` lets Claude add itself to a public channel when a member selects one of its suggested-channel buttons, or when the channel's name matches an [auto-join channel pattern](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) an admin set. It cannot join private channels this way.
* `users:read.email` lets Claude read a member's profile email. Claude uses it for checks such as the email domain when a member connects their Claude account. It does not connect accounts; a member still runs the Connect step in Slack.

## What installing does not grant

Credentials for GitHub, Google Drive, a data warehouse, or anything else are provisioned separately by a Claude organization Owner and live on Anthropic's side rather than in Slack.

It responds when @-mentioned, and may respond to other messages it judges warrant a reply.

## After you install

Post `@Claude connect` in any channel with no other text, or send `connect` on its own in a direct message with Claude, and give the code it returns to whoever asked you to install. That code is what pairs your workspace to their Claude organization; it expires after 15 minutes.

Pick a channel that belongs to just your workspace. Claude can decline to reply in [guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels).

## Related resources

* [Security and data handling](/docs/claude-tag/concepts/security-and-data): where credentials are stored and what leaves your workspace
* [Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace): what the Claude Owner does with the code you send

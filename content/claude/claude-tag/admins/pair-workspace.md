> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pair your Slack workspace

> Connect your Slack workspace to your Claude organization. See what to send your Slack admin, where to paste the pairing code, and whether to enable the entire workspace or specific channels first.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<div className="tm-stepbar">
  <a className="tm-stepbar-seg tm-current" href="/docs/docs/claude-tag/admins/pair-workspace">1 · Pair workspace</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/add-connections">2 · Give access</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/configure-github">3 · Connect GitHub</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/set-spend-limit">4 · Spend limit</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/test-it">5 · See it work</a>
</div>

<div className="tm-stepmeta">
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Role you need</span><span>Owner in your Claude organization, plus a Slack workspace admin to install the app and generate the pairing code. These can be the same person or two people.</span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Before this step</span><span>The <a href="/docs/docs/claude-tag/admins/setup-overview#before-you-start">prerequisites</a>: confirm your role and decide where you'll pilot</span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Do I need this?</span><span><span className="tm-meta-pill tm-meta-pill-req">Required</span>Nothing else in setup works until a workspace is paired.</span></div>
</div>

## Install and pair

Pairing has three parts: install the app in Slack, get a code from Slack, and paste it in the Claude console.

<Steps>
  <Step title="Install the Claude app in Slack">
    Open [claude.com/claude-for-slack](https://claude.com/claude-for-slack), click **Add to Slack**, and approve the permissions Slack shows. Skip if the app is already installed.
  </Step>

  <Step title="Run @Claude connect in Slack">
    Send `@Claude connect` in any channel, with no other text, as a new top-level message or in a thread where Claude isn't already working. Claude replies with a pairing code valid for 15 minutes. In a thread where Claude is already working, it treats the message as a normal request instead.

    Pick a channel that belongs to just your workspace. Claude can decline to reply in [guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels).

    In a DM with Claude, send `connect` on its own. Sending `link` works in place of `connect` in both cases.

    Only a Slack workspace admin (or Grid org admin) can run this command. If that's not you, [send them the install request](#send-the-install-request-to-your-slack-admin) and have them return the code.

    If your install is missing a permission, the reply names it (and may still issue a code with a warning); see [the section below](#if-@claude-connect-says-the-installation-is-out-of-date).
  </Step>

  <Step title="In the console: complete the pairing step">
    At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), setup opens as a full page until your first workspace is paired; click **Start setup** to reach **Pair your Slack workspace**. Paste the code, choose where Claude can reply (**Entire workspace (recommended)** or **Specific channel**), and click **Pair workspace**. To pair a workspace after your first, select **+ Connect** next to **Where Claude Tag works** instead, as described in [Manage workspaces](/docs/claude-tag/admins/workspaces#pair-another-workspace).
  </Step>
</Steps>

Setup confirms the pairing and moves on to choosing Claude's tools, so there's nothing to check at this point; continue with [Give Claude access](/docs/claude-tag/admins/add-connections). After setup finishes, the Slack row under **Where Claude Tag works** shows your workspace as connected, and a [scope](/docs/claude-tag/concepts/glossary#scope) for it (the entry where you'll bind tool access) appears on the **Slack** tab under **Claude Tag's access**.

## Send the install request to your Slack admin

Steps 1–2 above need a Slack workspace admin; step 3 needs an Owner in your Claude organization. If those are two people, send the Slack admin this and have them return the code:

```text wrap theme={null}
Please install the Claude app (https://claude.com/claude-for-slack) in [workspace]. When that's done, let me know a time that works for the next part: you post "@Claude connect" in any channel with no other text and send me the code it returns. Pick a channel that belongs to just [workspace]. The code expires 15 minutes after Claude posts it, so I'll redeem it right away. What it can access: https://claude.com/docs/claude-tag/admins/for-slack-admins
```

### If `@Claude` doesn't respond at all

On Enterprise Grid, an earlier install can lose its connection and stop responding in every workspace. See [Claude is silent everywhere on Enterprise Grid](/docs/claude-tag/admins/troubleshooting#claude-is-silent-everywhere-on-enterprise-grid) for the reinstall that refreshes it without uninstalling, then send `@Claude connect` again in a channel of that workspace.

### If `@Claude connect` says the installation is out of date

Your Slack install predates a permission the app now requests. The workspace keeps its old grant until a Slack admin approves the update. Replies name the missing permissions until then. The reply links both remedies; either one clears the error.

* **Approve the updated permissions.** A Slack workspace admin opens Slack's installed-apps page, `https://app.slack.com/apps-manage/<team-id>/integrations/installed`, finds the Claude app, and approves its requested permissions. The **approves its updated permissions** link in the reply lands on that page directly. On Enterprise Grid with an org-wide install, a Slack org admin uses `https://app.slack.com/manage/<grid-id>/integrations/installed` instead.
* **Reinstall the app.** A Slack workspace admin clicks the **reinstalls the Claude app** link in the reply and approves the consent screen Slack shows. Opening [claude.com/claude-for-slack](https://claude.com/claude-for-slack) and clicking **Add to Slack** again does the same thing. This installs over the existing app with the current permissions; do not uninstall first.

Then run `@Claude connect` again. Slack's **Manage apps** page lists the scopes the app requests, not the scopes your workspace has granted. Seeing a permission listed there does not by itself mean it is approved. The grant happens when an admin approves the update or completes the consent screen.

### If Claude says Claude in Slack is not available for your organization

The reply "Claude in Slack is not available for your organization" means your Slack workspace is paired to a Claude organization with a restricted compliance configuration, such as Zero Data Retention (ZDR). Claude Tag retains channel memory and session transcripts, so it can't run under that configuration.

Check which Claude organization the workspace is paired to. If your company has more than one, for example a trial org alongside the main one, the workspace may be paired to the wrong one. An Owner in that organization can [revoke the pairing](/docs/claude-tag/admins/workspaces#revoke-a-pairing) so you can pair the workspace to the right one here.

If the pairing already points to the intended organization, no admin setting lifts the restriction; contact your account team.

If the reply instead says Claude Tag has been turned off for your Claude organization, the cause is the **Enable Claude Tag for your organization** toggle, and an Owner can turn it back on. See [Claude Tag is turned off for your organization](/docs/claude-tag/admins/troubleshooting#claude-tag-is-turned-off-for-your-organization).

### If the console says "already connected to a different organization"

A Slack workspace can pair with only one Claude organization at a time, and this one is already paired elsewhere. An Owner in the Claude organization that currently holds the pairing must [disconnect it](/docs/claude-tag/admins/workspaces#revoke-a-pairing) from their **Connected workspaces** list before your code can be redeemed here. If your company has more than one Claude organization, check the others; the existing pairing is often in a test or trial org.

### If the console says "claim code is invalid, expired, or already used"

Pairing codes are single-use and expire 15 minutes after they're issued. Ask the Slack admin to send `@Claude connect` again and paste the fresh code; reinstalling the app is not required. On Enterprise Grid, a Grid org admin's reply includes a Grid-wide code (starting with `enterprise_`) alongside the workspace code (starting with `workspace_`).

### If DMs never respond on Enterprise Grid

On Enterprise Grid, direct messages with Claude follow each user's home workspace, not the workspace you paired. When a user is homed in a grid workspace the pairing doesn't cover, their DMs answer with a redirect to setup instructions even after their account connects, while channels in the paired workspace work normally.

The fix is to pair the whole grid rather than one workspace. Claude's reply to a Grid Org Owner or Org Admin's `@Claude connect` includes two codes; redeem the one starting with `enterprise_` (not the `workspace_` one) in the pairing step to cover DMs for users in every workspace of the grid.

## After pairing: where Claude is enabled

Once a workspace is paired, where Claude responds depends on what you chose when pairing (entire workspace or specific channels), the **Enable Claude Tag for your organization** toggle, and your [access restriction](/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude) setting.

* **What Claude can reach** in each channel depends on which Access bundles you bind; see [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope).
* **Nothing runs until usage is funded** on Team plans; see [Set a spend limit](/docs/claude-tag/admins/set-spend-limit).
* **DMs work separately** from channels and run on each user's own claude.ai account. On Enterprise Grid, DMs follow each user's home workspace; see [If DMs never respond on Enterprise Grid](#if-dms-never-respond-on-enterprise-grid).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): create an Access bundle and add connections
* [What the Claude Slack app can access](/docs/claude-tag/admins/for-slack-admins): the page to send a Slack admin who's approving the install

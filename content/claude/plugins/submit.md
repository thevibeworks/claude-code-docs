> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit your plugin

> Submit a plugin from a GitHub repository to Anthropic's directory through the developer portal, follow its review, publish it, and release updates.

To list a plugin in [Anthropic's directory](/docs/directory/publish), you submit it from a GitHub repository through the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage). Anthropic checks each version before it can go live, and people can then add the plugin from claude.ai and use it in chat, Cowork, and Claude Code.

Use this page if your plugin is already in a GitHub repository and you want it listed. If the plugin references a remote MCP server you run, submit that server as an MCP connector too, as [Submit your plugin, and your MCP server as a connector](/docs/directory/publish#submit-your-plugin-and-your-mcp-server-as-a-connector) explains.

<Note>
  * To build the plugin first, see [Plugin structure and testing](/docs/plugins/build)
  * To share it without a public listing, see [Share a plugin with teammates](/docs/plugins/share) or [Roll out a plugin to your whole organization](/docs/plugins/org-rollout)
  * If you submitted through the earlier Claude Console form, see [Move an earlier submission to the developer portal](/docs/directory/publish#move-an-earlier-submission-to-the-developer-portal)
</Note>

## Before you submit a plugin

You need the following to submit from the developer portal on claude.ai:

* **A GitHub repository that holds the plugin, and your GitHub account connected on claude.ai.** The directory reads plugins from repositories on github.com. The portal checks that your connected GitHub account can push to the repository, so [connect it first](#connect-your-github-account). The repository can stay private while you validate and submit, and must be public before the listing goes live. See [Submit from a private repository](#submit-from-a-private-repository)
* **A plan and role that can submit.** See [who can submit to the directory](/docs/directory/publish#confirm-you-can-submit-to-the-directory)

Every plugin in the directory must comply with the [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) and the [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).

Before you open the portal, work through the [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist). It covers what the directory's checks look for in `plugin.json`, the README, the license, and the rest of the plugin folder. In your terminal, from the folder that contains the plugin folder, run `claude plugin validate ./<plugin-folder>` first to catch formatting and structure problems. The portal's **Validate** step runs more checks than the command does.

## Submit a plugin

Each plugin folder is its own submission in the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage), so a repository that holds several plugins needs one submission for each.

<Steps>
  <Step title="Open the portal">
    1. Open the [developer portal](https://claude.ai/directory/manage) and select **Submit new**.
    2. When the portal asks **What would you like to submit?**, select **Plugin bundle**.

    <Note>
      The other option, **MCP connector**, submits one remote MCP server as its own connector listing. If your plugin references an MCP server you built and you haven't submitted that server yet, submit it separately with **MCP connector** by following [Submit your connector](/docs/connectors/building/submission). [Submit your plugin, and your MCP server as a connector](/docs/directory/publish#submit-your-plugin-and-your-mcp-server-as-a-connector) explains why you submit both.
    </Note>
  </Step>

  <Step title="Enter the source and validate">
    On the **Source** step, fill in the fields:

    * **Repository**: the GitHub repository's URL, or `owner/repo`. If you paste a link to a folder on a branch, the portal fills in the path and branch for you
    * **Plugin path (optional)**: the folder that holds `.claude-plugin/plugin.json`, if the plugin isn't at the repository root
    * **Branch or tag (optional)**: the branch or tag that the directory follows for new versions. The portal calls this the tracked branch or tag. Leave the field empty to follow the repository's default branch. A tag stays on its commit until you change the tag. If the branch name contains a slash, type the name in this field or enter `owner/repo@branch` in **Repository**, instead of pasting a folder link

    Then validate the plugin:

    1. Select **Validate** to run the directory's validation checks on the plugin.
    2. If a finding blocks submission, fix it in the repository and push the fix.
    3. Validate again.

    The [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) explains what each kind of finding means.

    A validation result applies to one commit. If you push to the branch after validating, validate again before you continue.
  </Step>

  <Step title="Check the listing details">
    The **Listing details** step shows how the plugin appears in the directory, read from `plugin.json` and the README. To change a field before you submit, edit `plugin.json` or the README in the repository and validate again. Once the plugin is listed, its name and short description follow the version that's live, so to change them later, edit `plugin.json` or the README and publish a new version.
  </Step>

  <Step title="Answer the data handling questions">
    On the **Data handling** step, answer each question: whether the plugin reads or stores personal data, whether it sends data to services other than its declared connectors, how long it keeps data, and whether it's intended for people under 18.
  </Step>

  <Step title="Complete the compliance step">
    On the **Compliance** step, check the contact email and select the acknowledgements:

    1. Check that the contact email is an address where Anthropic can reach you about the submission.
    2. Select all four acknowledgements.
  </Step>

  <Step title="Review and submit">
    On the **Review and submit** step, confirm the details, choose how new versions arrive, and submit:

    1. Confirm the details.
    2. Under **How new versions reach the directory**, choose **GitHub push webhook**, which is selected by default, or **Scheduled check only**. With either option, the directory also checks the tracked branch or tag for new commits on a schedule.
    3. Select **Submit for review**.

    If you kept **GitHub push webhook**, the **Plugin submitted for review** page offers **Set up push updates**. You need admin access to the repository on GitHub to set up the webhook.

    To set it up later, open the plugin from **Submissions** in the developer portal and select **Set up** under **Updates** on the **Settings** tab.
  </Step>
</Steps>

### Submission limits and duplicates

An organization can create up to 10 submissions in any 24-hour period, and saved drafts and withdrawn submissions count toward the limit. When your organization reaches the limit, the portal shows **Daily submission limit reached**.

Your organization can have one submission for each repository and folder. To continue an existing submission, open it from **Submissions** in the developer portal instead of creating a second one.

If another organization has already submitted the same repository and folder, the portal refuses **Submit for review** with **Already submitted by another organization**. If your organization owns the repository, email `directory@anthropic.com`. If the earlier submission is one you made through the Claude Console form, see [Move an earlier submission to the developer portal](/docs/directory/publish#move-an-earlier-submission-to-the-developer-portal).

### Connect your GitHub account

The portal checks your GitHub access before it lets you create a submission, submit it, publish the plugin, [relist](#withdraw-or-delist-a-plugin) it, or turn on [auto-publish](#publish-a-passing-version). It uses the GitHub account you connected to claude.ai in the organization you're submitting from, and asks GitHub whether that account can push to the repository. A GitHub connection you made in another Claude organization doesn't carry over. If the portal can't confirm push access, the action stops and you see one of these messages:

* **GitHub isn’t connected for this Claude organization**: select **Connect GitHub** in the message to connect your account, then try again
* **The connected GitHub account can’t push to this repository**: ask an admin of the repository to give your GitHub account write access, then try again

Validating a public repository doesn't run this check, so **Validate** can pass before you've connected GitHub; the check happens when you create or submit.

## Submit from a private repository

You can validate and submit a plugin while its repository is private, so review can start before you publish your code. The directory scans it while it's private. Publishing and relisting still need the repository to be public.

The portal reads a private repository only when these conditions hold:

* **Your connected GitHub account can push to the repository.** This is the same check as [Connect your GitHub account](#connect-your-github-account)
* **You agree to the source upload.** The portal shows **This repository is private.** and asks you to confirm that the repository's source is uploaded to Anthropic for automated scanning and is visible to Anthropic reviewers
* **The Claude GitHub App is installed on the repository** and connected to your Claude organization. If it isn't, the portal shows **The Claude GitHub App can’t reach this repository** with an **Install the Claude GitHub App** link. Install it, then validate again

Before you've agreed to the source upload, **Validate** shows only **Couldn’t find that repository, branch, tag, or commit** while your GitHub account isn't connected, can't see the repository, or can't push to it. The portal doesn't confirm that a private repository exists to someone who can't see it.

When you're ready to publish, make the repository public on GitHub, then select **Check for new commits** on the plugin's page. Until then, the page shows **Publishing needs a public repository**.

## After you submit a plugin

When you select **Submit for review**, the directory scans the newest commit on the tracked branch or tag. Each scan validates the plugin against the directory's rules again and runs a security scan. [Prepare for the security scan](/docs/plugins/pre-submission-checklist#prepare-for-the-security-scan) describes what the security scan looks for.

To follow the submission, open the plugin from **Submissions** in the [developer portal](https://claude.ai/directory/manage). The **Versions** tab on the plugin's page lists each scanned commit with the result of its checks. When the newest version isn't live, the plugin's page says why. [Track your directory submission](/docs/directory/submission-status#plugin-bundle-statuses) explains what each status in the portal means and who acts next.

A finished scan leaves the version in one of these states:

* **Passes every check:** the version can be published, as described in [Publish a passing version](#publish-a-passing-version)
* **Held for a reviewer:** an Anthropic reviewer reads the version, and it can go live only after the reviewer clears it. The [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) lists the findings that hold a version
* **Doesn't pass:** the portal lists the rules that the version breaks. For a failed security scan, the portal shows the category of the finding when the scan recorded one, such as **Sends data to an undisclosed destination**

If the directory can't fetch a commit, or a scan ends without a result, the plugin's page says whether the directory retries on its own or whether something in the repository needs fixing. After any fix, select **Check for new commits** on the plugin's page to run the scan again.

### Fix a failed version

To fix a version that doesn't pass, first check whether the submission was rejected. A rejected submission says that the version was not approved, and only a rejected submission shows **Resubmit for review** on its **Review** tab. A reviewer's decision rejects a submission, and so does a failed security scan on a plugin that has never been published.

* **If the submission was rejected:** the directory stops scanning it. To resubmit:
  1. Read any changes that the reviewer asked for under **Requested changes** on the **Review** tab.
  2. Update the plugin and push the fix.
  3. Select **Resubmit for review** on the **Review** tab. Resubmitting runs every check again.
* **If the submission wasn't rejected:** push a fix to the tracked branch, then select **Check for new commits** on the plugin's page. Without that step, the directory finds the new commit at its next scheduled check

### Publish a passing version

A version that passes every check isn't live until it's published. When the version passes, select **Publish** on the plugin's page. By default, the portal records this as a request for an Anthropic reviewer, who then publishes the version.

The **Auto-publish** row on the plugin's **Overview** tab says which publish setting Anthropic has applied to your plugin. The settings include:

* **An Anthropic reviewer publishes each version**: the default. For every version that passes, you select **Publish** and a reviewer publishes it
* **The reviewer publishes only the first version**: you select **Publish** for the first version and a reviewer publishes it. Later versions that pass go live by themselves unless you turn auto-publish off or the plugin is waiting for a reviewer
* **You publish the first version**: an Anthropic reviewer can apply this setting when they approve the plugin. You select **Publish** for the first version and it goes live. Later versions that pass go live by themselves unless you turn auto-publish off or the plugin is waiting for a reviewer

You set auto-publish with the **Auto-publish passing versions** toggle on the **Review and submit** step. After you submit, change it with the **Publish new versions automatically** toggle on the plugin's **Settings** tab. Auto-publish doesn't apply while a reviewer publishes each version.

If a submission is stuck, [Contact Anthropic about a submission](/docs/directory/submission-status#contact-anthropic-about-a-submission) gives the channel for a plugin.

## Update a published plugin

After the first submission, you keep the listing current by releasing the way you already do. Merge to the tracked branch, and the directory picks up the commit, checks it, and publishes it. You don't return to the portal unless a version is held or you want to change a setting. If the submission follows a tag, release a new version by changing the tag, as described in [Change the tracked branch or tag](#change-the-tracked-branch-or-tag).

The directory checks the tracked branch for new commits on a schedule. If you set up the GitHub push webhook, the directory also checks when you push, without waiting for the schedule.

* **To set up the webhook after you submit:** select **Set up** under **Updates** on the plugin's **Settings** tab
* **To check right away:** open the plugin from **Submissions** in the [developer portal](https://claude.ai/directory/manage) and select **Check for new commits**

The repository doesn't have to be dedicated to the plugin. If the plugin is one folder in a larger repository, give that folder as the plugin path when you submit; the directory reads and scans only that folder.

A new version that passes is published according to the plugin's [publish setting](#publish-a-passing-version). The listing keeps serving the last published version until a new version is published, including when a new version doesn't pass or is held for a reviewer. If the security scan fails a new version, later versions also wait until an Anthropic reviewer clears the plugin.

If your `plugin.json` sets `version`, raise it with every release.

### Change the tracked branch or tag

The tracked branch or tag is where the directory checks for new versions of your plugin. To follow a different one, edit the **Tracked branch or tag** field on the plugin's **Settings** tab and select **Save**. The directory then scans the newest commit there as a new version; when it passes, select **Publish** again, or **Publish update** if a version is already live.

A version that is already live stays up when you change the tracked branch or tag, and the directory cancels a publish request that is still waiting. You can't change the branch or tag while the plugin is with a reviewer.

You can't change a submission's repository and folder after you submit. To list a plugin from a different repository or folder, create a new submission.

## Withdraw or delist a plugin

You can take a submission back at any stage from its page in the developer portal. Open the plugin from **Submissions** at [claude.ai/directory/manage](https://claude.ai/directory/manage); which control you see depends on how far the submission got:

* **A draft you haven't submitted**: select **Delete draft**. The draft leaves your list.
* **A submission that's in review and was never published**: select **Withdraw submission**, in the page header or on the **Settings** tab. The submission leaves your list and drops out of scanning and review, and nothing is published. To try again later, submit the same repository and path, which reopens it. A withdrawn submission still counts toward the [10 submissions per 24 hours](#submission-limits-and-duplicates) limit.
* **A plugin that's live in the directory**: open the menu in the page header and select **Delist plugin**. This asks the directory to stop listing it, which can take time to reach every Claude app. People who already installed the plugin stop getting updates, and their copy may be removed. While the request is pending, the menu shows **Delist requested**.

To bring a delisted plugin back, select **Relist plugin** on its page. Relisting is a request, not an instant switch: the directory may apply it directly or send it to a reviewer, and it can be declined. To change what's listed rather than remove it, [update the published plugin](#update-a-published-plugin) instead.

## Next steps

* [Track your submission](/docs/directory/submission-status#plugin-bundle-statuses): check what the status next to your plugin's name means and who acts next
* [Plugin pre-submission checklist](/docs/plugins/pre-submission-checklist): fix each validation and scan finding
* [After publishing](/docs/connectors/building/after-publishing): update your plugin and listing, and delist
* [Track published plugin usage](/docs/connectors/building/after-publishing#track-published-plugin-usage): see installs, versions, runs, and error rates on the plugin's **Usage** tab
* [Manage your directory listing](/docs/connectors/building/managing-your-listing): for an MCP connector, check health and usage metrics and edit the listing

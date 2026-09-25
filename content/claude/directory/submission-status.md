> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track your directory submission

> Look up the status the developer portal shows for a plugin bundle or MCP connector submission: what it means, who acts next, and who to contact.

After you submit to the directory, the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage) shows one status for each submission. The status tells you whether Anthropic is working on the submission, whether it's waiting on you, or whether it's live.

This page is for anyone with a submission in the portal. Review time isn't fixed.

<Note>
  If you haven't submitted yet, see [Publish to the directory](/docs/directory/publish).
</Note>

Find your status in the table for your submission's kind: [plugin bundle](#plugin-bundle-statuses) or [MCP connector](#mcp-connector-statuses). If nothing is waiting on you and you still need an answer, see [Contact Anthropic about a submission](#contact-anthropic-about-a-submission).

## Plugin bundle statuses

Open the plugin from **Submissions** in the developer portal. The status appears next to the plugin's name, and the card under it says what happens next.

| Status            | What it means                                                                                                                                                                                                                           | Who acts next                                                                                                                 |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Draft**         | Nothing has been sent to Anthropic yet                                                                                                                                                                                                  | You. Select **Continue submission**.                                                                                          |
| **Scanning**      | You submitted, and the security scan is waiting to start or running. If a scan attempt fails on Anthropic's side or GitHub's, the directory retries it.                                                                                 | Anthropic. There's nothing to do on your side.                                                                                |
| **Needs changes** | The newest version didn't pass, or the scanner couldn't fetch or accept the plugin. The plugin's page names what to change.                                                                                                             | You. [Fix a failed version](/docs/plugins/submit#fix-a-failed-version) covers pushing a fix and resubmitting.                      |
| **In review**     | An Anthropic reviewer is checking the listing. When the version was held, the card names the category it's held for. The reviewer's decision appears on the plugin's page.                                                              | Anthropic                                                                                                                     |
| **Approved**      | The version passed, and it isn't live yet. The card says who publishes it: an Anthropic reviewer, you, or the directory by itself.                                                                                                      | Whoever the card names. [Publish a passing version](/docs/plugins/submit#publish-a-passing-version) explains the publish settings. |
| **Published**     | A version is live in the directory. The card also says what is happening with any newer version, such as being scanned, waiting with a reviewer, or not passing. A newer version that doesn't pass leaves the published one unaffected. | Nobody, unless the card names a newer version that needs changes                                                              |
| **Not live yet**  | The submission is marked published, and nothing is listed yet. The directory team has to list it.                                                                                                                                       | Anthropic                                                                                                                     |
| **Delisted**      | The plugin isn't visible in the directory. Select **Relist plugin** to ask for it back.                                                                                                                                                 | You, if you want it listed again                                                                                              |
| **Withdrawn**     | Nothing is under review or listed                                                                                                                                                                                                       | Nobody                                                                                                                        |

**Approved** doesn't mean people can install the plugin. A plugin is installable only once its status is **Published**.

## MCP connector statuses

Open the connector from the developer portal's list of submissions. A card at the top of the connector's page shows the status, one sentence about it, and the next step when there is one.

A submission doesn't pass through every status in the table. Anthropic scans each connector submission automatically and, by default, lists it as a Community connector with no action from you. Some submissions also get a review from a person, and the statuses that mention a reviewer apply to those. [How Anthropic reviews directory submissions](/docs/directory/publish#prepare-for-review) describes both.

| Status                | What it means                                                                                                                                                                                                                | Who acts next            |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------- |
| **Draft**             | Nothing has been sent to Anthropic yet. A draft can have a reviewer's note if it was sent back and saved again.                                                                                                              | You                      |
| **In review**         | A reviewer is checking the listing. Anthropic emails your primary contact if it needs anything.                                                                                                                              | Anthropic                |
| **Changes requested** | The reviewer left a note. Select **View feedback** on the card to read it, then address it and resubmit.                                                                                                                     | You                      |
| **Not approved**      | The reviewer's notes say why. Select **View feedback** to read them. You can edit the listing and resubmit.                                                                                                                  | You                      |
| **Approved**          | The review team cleared the listing, and it isn't in the directory yet. It goes live when someone who can edit the listing publishes it. If you edit the listing before you publish, it returns to draft for another review. | You. Select **Publish**. |
| **Published**         | The connector is live in the directory. If you submitted an edit, the card says whether that edit is in review, and the live listing stays until the edit is approved.                                                       | Nobody                   |

[Manage your directory listing](/docs/connectors/building/managing-your-listing) covers reviewer feedback, listing edits, and the health and usage metrics for a published connector.

## Contact Anthropic about a submission

Check the status first. **Scanning** and **In review** mean Anthropic acts next and nothing is waiting on you. When you need to reach Anthropic, use the channel for your submission's kind:

* **Plugin bundle**: open the plugin in the developer portal, open its menu, and select **Get help** or **Contact Anthropic**. A plugin that wasn't approved shows **Appeal this decision** on its page. You can also email `directory@anthropic.com`, where replies can be delayed
* **MCP connector**: email `mcp-review@anthropic.com`

Include the listing's name, the organization you submitted from, and the status the portal shows.

## After your listing is published

A published listing appears in the directory that claude.ai, the Claude desktop and mobile apps, and Cowork share. [Plugin feature support across platforms](/docs/plugins/platform-support) lists which of a plugin's components load on each surface.

A published connector is listed with the **Community** label by default. There's no application for the **Verified** label. [Connector verification](/docs/connectors/verification#list-your-own-connector) explains how a listing becomes Verified and what each label means to people installing it.

## Next steps

* [After publishing](/docs/connectors/building/after-publishing): update your server or plugin, and delist
* [Submit your plugin](/docs/plugins/submit#after-you-submit-a-plugin): follow each new plugin version through the scan, review, and publishing
* [Manage your directory listing](/docs/connectors/building/managing-your-listing): for a connector, read reviewer feedback, edit the listing, and check its metrics

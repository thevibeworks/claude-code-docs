> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a plugin with Claude

> Make a plugin for your own workflow from claude.ai or the desktop app without writing files: choose Create with Claude and answer Claude's questions.

A [plugin](/docs/plugins/overview) packages skills, commands, and connectors. You can make one for yourself in claude.ai or the Claude desktop app without writing files: from [**Customize > Plugins**](https://claude.ai/customize/plugins), select **Add > Create with Claude**, describe what you need, and save the plugin Claude produces to your account.

A plugin you create this way is for you. It lives on your account, and on a Team or Enterprise plan you can [share it](/docs/plugins/share) with specific people or your whole organization from its page in Customize. It isn't a directory listing; if you later want that, see [Submit a plugin you created with Claude](#submit-a-plugin-you-created-with-claude) at the end of this page.

<Note>
  * If you'd rather write the files yourself, see [Plugin structure and testing](/docs/plugins/build)
  * If you want to make a plugin available to everyone in your organization, see [Publish a plugin to your organization](/docs/plugins/share#publish-a-plugin-to-your-organization)
</Note>

To begin, [start a new plugin from the Add menu](#start-from-the-add-menu), [describe it to Claude and save it](#describe-and-save-the-plugin), then [review the plugin Claude made](#review-what-claude-made).

## Create the plugin with Claude's help

When you create a plugin with Claude, you start a conversation from the **Add** menu on [**Customize > Plugins**](https://claude.ai/customize/plugins), describe the task you want the plugin to handle, and save the plugin that Claude produces.

### Start from the Add menu

To start a new plugin:

<Steps>
  <Step title="Open the Add menu">
    Go to [**Customize > Plugins**](https://claude.ai/customize/plugins) in claude.ai or the desktop app and select **Add**.
  </Step>

  <Step title="Choose how to create it">
    Choose one of these:

    * **Create with Claude**: start a new conversation, or a new Cowork task in the desktop app, with a request to create a plugin already filled in for you to send. Choose this when you can describe the task you want the plugin to handle but don't want to write skill files
    * **Create a plugin**: fill in a form with the plugin's name and what it helps with, then write its skills, commands, and connectors in an editor. Choose this when you already know what each piece should say
  </Step>
</Steps>

If neither item appears in the **Add** menu, plugin creation isn't available on your account. Your organization can turn it off, and so can your IT department's configuration of the desktop app. [Manage plugins for your organization](/docs/plugins/admin#control-what-members-add-themselves) covers the organization setting.

### Describe and save the plugin

After you choose **Create with Claude**, a conversation opens where you tell Claude what the plugin is for, and Claude assembles it as a `.plugin` file that you save to your account:

<Steps>
  <Step title="Describe what the plugin is for">
    Tell Claude the job the plugin should help with, in the same words you'd use to explain it to a colleague: the task, when it comes up, and what a good result looks like.
  </Step>

  <Step title="Answer Claude's questions">
    Answer Claude's follow-up questions, such as which of your connectors the plugin should use. You can change any of it later.
  </Step>

  <Step title="Save the plugin Claude assembles">
    Claude writes the skills and commands, includes the connectors you chose, and shows the result as a file card in the conversation. Select **Save plugin** on that card to add it to your account. It's then listed under **Customize > Plugins**, on the **Yours** view.
  </Step>
</Steps>

### Review what Claude made

Check the plugin before you rely on it:

<Steps>
  <Step title="Open the plugin">
    Open **Customize > Plugins** and select the new plugin.
  </Step>

  <Step title="Read what it contains">
    Read the skills, commands, and connectors it contains.
  </Step>

  <Step title="Sign in to its connectors">
    Sign in to any bundled connector from the plugin's page.
  </Step>

  <Step title="Try it on a real request">
    Start a chat, or a Cowork task in the desktop app, with the kind of request the plugin is for, and check that Claude follows the plugin's skills.
  </Step>
</Steps>

## Use, disable, or remove your plugin

The plugin is on your account for the organization you created it in, so it's available in your chats, in Cowork, and in Claude Code as a synced plugin.

Open the plugin from **Customize > Plugins** to disable or remove it:

* **Disable it**: turn off the plugin's toggle
* **Remove it**: open its menu and select **Remove** to delete it from your account

To give the plugin to other people in your organization, see [Share a plugin with teammates](/docs/plugins/share). It covers sharing with specific people and publishing to your organization's library, both on Team and Enterprise plans.

## Submit a plugin you created with Claude

Anthropic's directory reads plugins from a GitHub repository, so a plugin that lives only on your account can't be submitted as it is. If you decide you want it listed, get its files from the same conversation and go through the normal submission route:

<Steps>
  <Step title="Ask Claude for the plugin as a folder">
    In the conversation where Claude made the plugin, ask for it "as a plugin folder I can push to GitHub for the directory", download the zip Claude produces, and check that it has `.claude-plugin/plugin.json`, the `skills/` folder, a `README.md`, and a `LICENSE`.
  </Step>

  <Step title="Check the manifest and README">
    Unzip the folder and compare `plugin.json` with [Write the manifest](/docs/plugins/build#write-the-manifest). Claude may include fields the manifest doesn't use and leaves placeholders such as your name for you to fill in. If you have Claude Code installed, run `claude plugin validate` on the folder, as [Check the plugin on your machine](/docs/plugins/pre-submission-checklist#check-the-plugin-on-your-machine-optional) describes.
  </Step>

  <Step title="Push and submit">
    Push the folder to a public GitHub repository, then follow [Submit a plugin](/docs/plugins/submit).
  </Step>
</Steps>

## Next steps

* [Plugins](/docs/plugins/overview#manage-installed-plugins): turn off, remove, or update plugins on your account
* [Plugin feature support across platforms](/docs/plugins/platform-support): check which of the plugin's components work in chat, Cowork, and Claude Code
* [Share a plugin with teammates](/docs/plugins/share): give the plugin to specific people or your organization

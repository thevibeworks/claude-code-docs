> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Science on more than one computer

> What to expect when you sign in on another computer, or under another sign-in on the same computer.

Claude Science runs on your own computer by design, and your projects, artifacts, and conversation history live there with it, under your control rather than in your Claude account. Each computer you install it on keeps its own projects, so a new or different computer starts fresh when you sign in, and your earlier work stays on the first computer. On one computer, Claude Science also keeps the work from each sign-in in its own folder. Signing in to a different organization or personal account starts fresh too, and you can access the earlier work (see [Access work from another sign-in on your computer](#access-work-from-another-sign-in-on-your-computer)).

## Your work stays on your computer

Anthropic doesn't sync your projects, artifacts, or conversation history to your Claude account, so there's no cloud copy for you to browse or sync from another computer. Claude reads and writes your files in place, in the folders you grant, and your work sits alongside them on your computer, where your own backup tools can cover it like any other application data. Your prompts, Claude's responses, and the file content Claude reads to answer them still go to Anthropic as part of each conversation, and Anthropic retains them as [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) describes.

You can install Claude Science on more than one computer and sign in to each with the same Claude account. Your account carries your plan and usage limits to every computer. Skills from your organization, along with any you published from the app, also reappear when you sign in on another computer (to the same organization, if your account belongs to more than one). Memory, settings, and the connectors you added in the app stay with each computer.

Because the only copy is on your computer, include the app's data folder in your regular backups. In the app, **Settings > Storage > Data location** shows where the folder is.

To take a single result to another computer, choose **Download** from the artifact's menu. A file saved with **Export session** is for technical support and troubleshooting, and can't be loaded into Claude Science on another computer. To reach the same projects from several computers instead, you can install Claude Science once on a Linux server you control and connect to it through an SSH tunnel from the browser on each computer. See [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).

## Access work from another sign-in on your computer

Claude Science keeps the work from each sign-in in its own folder on your computer. When you sign in to a different organization or personal account on that computer (for example, a Team plan after a personal plan), a banner at the top of the home screen offers to import the earlier work. Select the **Review** button on the banner, select the folders to access, choose **Copy** (the original folder keeps the work too) or **Move** (what's accessed is then removed from the original folder), and select **Import**. To access later instead, select **Review** next to **Import work on this computer** under **Settings** > **General** > **Account**.

The access happens entirely on your computer and uploads nothing. Credentials such as API keys and connector sign-ins aren't copied or moved and stay in their original folder. On Team and Enterprise plans, your admin controls whether the app offers importing (it's off by default on Enterprise plans). Content your organization doesn't allow, such as memory, isn't copied or moved and stays in its original folder (see [Previously saved Claude Science work](/docs/claude-science/admin-controls#previously-saved-claude-science-work)).

> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Science on more than one computer

> What to expect when you sign in on another computer.

Claude Science runs on your own computer by design, and your projects, artifacts, and conversation history live there with it, under your control rather than in your Claude account or on Anthropic's servers. Each computer you install it on keeps its own projects, so a new or different computer starts fresh when you sign in, and your earlier work stays on the first computer.

## Your work stays on your computer

Anthropic doesn't host your projects, artifacts, or conversation history, so there's no cloud copy of them to browse or sync. Claude reads and writes your files in place, in the folders you grant, and your work sits alongside them on your computer, where your own backup tools can cover it like any other application data. Your prompts, Claude's responses, and the file content Claude reads to answer them still go to Anthropic as part of each conversation and are handled under Anthropic's standard retention policy, as [Core concepts](/docs/claude-science/core-concepts#files-stay-on-your-computer) explains.

You can install Claude Science on more than one computer and sign in to each with the same Claude account. Your account carries your plan and usage limits to every computer. Skills from your organization, along with any you published from the app, also reappear when you sign in on another computer (to the same organization, if your account belongs to more than one). Memory, settings, and the connectors you added in the app stay with each computer.

Because the only copy is on your computer, include the app's data folder in your regular backups. In the app, **Settings > Storage > Data location** shows where the folder is.

To take a single result to another computer, choose **Download** from the artifact's menu. A file saved with **Export session** is for technical support and troubleshooting, and can't be loaded into Claude Science on another computer. To reach the same projects from several computers instead, you can install Claude Science once on a Linux server you control and connect to it through an SSH tunnel from the browser on each computer. See [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).

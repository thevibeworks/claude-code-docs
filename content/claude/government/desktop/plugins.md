> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins in Claude Desktop

> Find, install, create, and remove plugins in Claude Desktop for Claude for Government, and understand what plugins add in this deployment.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government and wants to find, install, or create plugins.

A plugin is a package that adds capabilities to Claude in a single step, such as skills, slash commands, sub-agents, and hooks. Plugins work in Cowork and in Code. See the [Plugins overview](/docs/plugins/overview) for more on what a plugin can contain.

<Frame caption="Video: Connectors, plugins, and skills from your agency (2 min 6 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/user-04-connectors-plugins-and-skills.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=953d050db0ec38bd9d0db7399e96cf40" aria-label="Video walkthrough: Connectors, plugins, and skills from your agency" data-path="images/government/videos/user-04-connectors-plugins-and-skills.mp4" />
</Frame>

<Accordion title="Transcript">
  Open Customize in the sidebar for your skills, connectors, and plugins. A connector lets Claude reach another service. The ones you can use come from your organization: here, Microsoft 365 and Web Search.

  If your organization has set up Microsoft 365, select Connect and sign in with your Microsoft work account. Claude can then search your mail, calendar, files, and Teams chats, reaching only what you can already open.

  In a chat, ask about your mail, and Claude asks before it searches. The card shows the search it wants to run. Allow it once, allow it for this task, or deny it.

  A plugin packages skills and commands from your organization. Plugins lists the ones already installed. Some install automatically. Open one to see its skills and switch it on or off.

  To find the rest, select Browse and open the Organization tab, which lists everything your organization offers you. Each plugin's plus sign installs it, and it then appears under Plugins.

  A skill teaches Claude one task your way, set up once and reused. If your organization allows it, select Add under Skills. Upload skill takes a skill file you have, and Create a skill lets you write one.

  The skill appears in your list, switched on. Skills you add stay on this computer. To give one to colleagues, your administrators package it in a plugin.

  Back in Chat, ask for something the skill covers and Claude loads it on its own. Here it rewrites a sentence in plain language.

  If Microsoft 365, web search, or a plugin you expect is missing, ask your organization's owner, who decides what is turned on for you.
</Accordion>

## Where plugins come from

In Claude for Government, plugins reach you in three ways:

* Your administrators add plugins for your organization, and some of them install automatically.
* If your administrators let you add your own plugins, you can upload a plugin file or ask Claude to create a plugin with you.
* If your administrators let you add plugin marketplaces, you can add a marketplace and install plugins from it.

Claude for Government does not include a public plugin marketplace; your administrators add your organization's plugins. Whether a marketplace you add can be downloaded depends on your agency's network and on the settings your administrators choose.

## Find and install plugins

Open **Customize** in the sidebar, then **Plugins**, to see the plugins you have installed. To find the rest, select **Discover** (**Browse** on Claude Desktop versions earlier than 2.2553.0) and open the **Organization** tab, which lists every plugin your administrators have made available to you.

A plugin your administrators set to install automatically is already installed. A plugin they offer for you to choose stays available on the **Organization** tab until you install it.

If your administrators let you add your own plugins, you can install a plugin from a file or have Claude build one. To install from a file, select **Add**, then **Upload plugin**, and choose the plugin's `.zip` file. Claude Desktop shows a notice reminding you to install only plugins you trust, since uploaded plugins are not controlled by Anthropic. To have Claude build one, select **Add**, then **Create with Claude**, and describe the plugin you want. Claude builds it for you, and you install the result.

If your administrators let you add plugin marketplaces, you can add a marketplace of your own. To add one, select **Discover**, then select the **+** button (**Add marketplace**) at the top right of the **Directory** that opens.

## Manage installed plugins

Open an installed plugin to see the skills, slash commands, sub-agents, and hooks it provides, and turn the plugin on or off. To remove a plugin, open it, select the three-dot menu, then **Remove**. Plugins you remove stay removed on this device, including ones your administrators set to install automatically.

A plugin you upload or create is added only on the device you are using.

## What plugins add in Claude for Government

A plugin adds its skills, slash commands, sub-agents, and hooks, and its hooks run on your machine at defined points during a session. The connectors your administrators provide appear under **Customize**, then **Connectors**. Connectors declared by a plugin you add yourself are not added to Claude Desktop's connectors.

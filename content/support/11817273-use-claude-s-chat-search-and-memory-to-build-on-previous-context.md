Title: Use Claude’s chat search and memory to build on previous context

URL Source: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context

Markdown Content:
You can now prompt Claude to search through your previous conversations to find and reference relevant information in new chats. Additionally, Claude can remember context from previous chats, creating continuity across your conversations. This article introduces Claude’s chat search and memory capabilities and explains how they work, what Claude can and can’t remember, and how you can toggle the features on/off.

## Search past chats with Claude

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

## What Claude can search

You can prompt Claude to search conversations within these boundaries:

## Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

## Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and find the **Preferences** section. Switch the toggle next to “Search and reference chats” off:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1780230600&signature=2df170c708989054fde90a6f8db058ca09239fd27eae01f679003c7c2710a8cb&req=dScmH859nYlXUPMW1HO4zRzXH18yIDHEJG68qZhl781OqKy6h%2BSBL9SyL5fL%0AoIIC9YjmsiDdTG5PVSM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1780230600&signature=2df170c708989054fde90a6f8db058ca09239fd27eae01f679003c7c2710a8cb&req=dScmH859nYlXUPMW1HO4zRzXH18yIDHEJG68qZhl781OqKy6h%2BSBL9SyL5fL%0AoIIC9YjmsiDdTG5PVSM%3D%0A)

## Can I exclude a specific past chat from searches?

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen:

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1780230600&signature=8fca596faaeca88c3419fb82ec49937c6ebac53f9a4234fdc3ac749bf082408d&req=dScmH859nYlWWvMW1HO4za54sKNuP4a9XDpzhlKsgjNvUfnRh11ion6hyDpZ%0ABcQZJrDGECfIIh5ph3s%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1780230600&signature=8fca596faaeca88c3419fb82ec49937c6ebac53f9a4234fdc3ac749bf082408d&req=dScmH859nYlWWvMW1HO4za54sKNuP4a9XDpzhlKsgjNvUfnRh11ion6hyDpZ%0ABcQZJrDGECfIIh5ph3s%3D%0A)

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

## What is Claude's memory?

Claude can now generate memory based on your chat history. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

## How does Claude’s memory work?

In addition to searching past chats, enabling Claude’s memory feature adds several capabilities.

### Memory summary

Claude will automatically summarize your conversations and create a synthesis of key insights across your chat history (not including chats in projects). This synthesis is updated every 24 hours and provides context for every new standalone conversation.

### Project memory and summary

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

## Enable Claude’s memory

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1780230600&signature=de4b381d4f5038687ea54420d51e6f0c37b08bc0c70ad061456c8b25fdcf852f&req=dScmH859nYlWW%2FMW1HO4zTD5MMHkdORDBq9N9dRTKYcPOLW%2B7JJDOk6w2w%2F6%0AiC%2FMIu2evTyZLt7pVoQ%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1780230600&signature=de4b381d4f5038687ea54420d51e6f0c37b08bc0c70ad061456c8b25fdcf852f&req=dScmH859nYlWW%2FMW1HO4zTD5MMHkdORDBq9N9dRTKYcPOLW%2B7JJDOk6w2w%2F6%0AiC%2FMIu2evTyZLt7pVoQ%3D%0A)

If you want to disable Claude’s memory, click the toggle to see two options:

## What does Claude remember?

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

## What Claude doesn't remember

### Incognito chats

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

## Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

## User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

### View and manage your memory summary

See exactly what Claude remembers about you by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and clicking “View and edit memory.” The **Manage memory** modal displays everything Claude remembers about you. In addition to asking Claude to edit the existing summary, you can also tell Claude what you want it to remember. To add custom instructions to Claude’s memory, click the pencil icon in the lower left corner of the summary.

You can also update your memory summary directly from your chats. Simply tell Claude what you'd like it to remember, and it will update your memory summary without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation, so you don’t need to wait for the daily synthesis to run.

### Past chat citations

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

### Toggle search past chats and memory on/off

You maintain control over Claude’s ability to search past chats and use memory – you can always disable these features and enable them again when needed in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**.

### Importing your memory from other AI tools

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

## Controls for Enterprise plan owners

Enterprise plan Owners and Primary Owners have specific controls for managing memory features across their organization.

### Organization-level memory controls

The organization-wide **Generate memory from chat history** toggle is enabled by default. When enabled, individual users can manage their own memory settings. Owners can disable the memory summary feature for their entire organization by navigating to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. When disabled by an Owner, it immediately deletes all existing memory synthesis data for all users, and individual users cannot modify or access the memory synthesis setting.

### Data handling and compliance

### Audit logging and data exports

### Team plan limitations

Team plans do not have organization-level controls for memory features. Individual Team plan members manage their own memory settings directly.

* * *

Related Articles

[Import and export your memory from Claude](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude)[Using incognito chats](https://support.claude.com/en/articles/12260368-using-incognito-chats)[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Use analytics chat to ask Claude about usage](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage)

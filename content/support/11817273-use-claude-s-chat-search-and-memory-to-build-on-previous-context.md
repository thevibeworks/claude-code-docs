# Use Claude’s chat search and memory to build on previous context

You can now prompt Claude to search through your previous conversations to find and reference relevant information in new chats. Additionally, Claude can remember context from previous chats, creating continuity across your conversations. This article introduces Claude’s chat search and memory capabilities and explains how they work, what Claude can and can’t remember, and how you can toggle the features on/off.

**Important:** We are gradually introducing an improved experience for memory from chats. The new experience will be the default for new users, and users on free, Pro and Max plans will be migrated to the new experience. Team and Enterprise plan admins will receive more information about a rollout in the coming weeks. In the interim, users on Team and Enterprise plans will stay on the legacy experience.

- If you see **[Settings > Memory](https://claude.ai/new#settings/customize-memory)**, you’re using the new memory experience, and the main sections that follow apply to you.

- If you see **Memory** in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**, you’re using the legacy memory experience and can skip to **[Information for legacy memory users](#h_89fe1c2710)**.

---

## Search past chats with Claude

Searching past chats is available to users on paid plans (Pro, Max, Team, and Enterprise plans) on the web, Claude Desktop, and Claude Mobile apps.

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

## What Claude can search

You can prompt Claude to search conversations within these boundaries:

- All chats outside of projects.

- Individual project conversations (searches are limited to within each specific project).

## Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

- "What did we discuss about [topic]?"

- "Can you find our conversation about [subject]?"

- "Let's continue where we left off with [project]."

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

## Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Memory](https://claude.ai/new#settings/customize-memory)** and switch the toggle next to "Search and reference chats" off:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482439/4dee2d7b267f865205feefc8f4f3/cb60c334-d1e2-4828-a01d-dfb36bbaa7eb?expires=1784810700&amp;signature=8f4236deb342ccf2d9c2d91a5847b9b497eafbc53b38d6f2331c31a868c3767d&amp;req=diUkFc12n4VcUPMW1HO4zY9IRA5kVNFwYNcz5nFaZkHe54lOVJ7C2oQDdQcO%0ASOpdznOV7tii4wzC1xc%3D%0A)

## Can I exclude a specific past chat from searches?

Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans). See **[Use incognito chats](https://support.claude.com/en/articles/12260368)** for more information.

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen.

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

**Important:** If you’re using an Enterprise or Team plan account, incognito chats are included in standard data exports and follow your organization's data retention policies. You can't search past chats if your organization uses customer-managed encryption keys on an Enterprise plan because conversation content is encrypted.

---

## What is Claude's memory?

The new memory experience is available for Claude users on free, Pro, and Max plans. Memory applies to chats on the web, Claude Desktop, and Claude Mobile, and is not currently available for Cowork.

Claude can now generate memory based on your chats. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

## How does Claude’s memory work?

In addition to searching past chats, enabling Claude's memory feature adds several capabilities.

### How Claude stores memory

Claude builds memory as a set of individual entries that are organized into categories. Claude reads, writes and updates these entries in real time as you chat rather than on a fixed daily schedule.

We apply safeguards and conduct evaluations to memory to help keep users safe.

### Project memory and summary

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

## Enable Claude’s memory

**Note:** Members of Enterprise plans can only enable this feature individually when it’s enabled by an Owner for their organization. See **[Controls for Enterprise plan Owners](#h_f7d6b307e2)** for more information.

You can toggle Claude’s memory on by navigating to **[Settings > Memory](https://claude.ai/new#settings/customize-memory)** and turning on **Generate memory from chats**:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482441/b5c806a8e3f68bf34c4a70724d38/d30be013-d099-4c93-99d1-23d404792f08?expires=1784810700&amp;signature=994c984f75f449361c41d335dcfc029f261552e549e1bd228711797e82e5f753&amp;req=diUkFc12n4VbWPMW1HO4zRlYrp9l41ArNshWSMEMw9dy%2BTaqgnqtKFJ1tj5J%0AwQCZRc9GSf%2Fs0Y94YgE%3D%0A)

If you want to disable Claude’s memory, click the toggle and you'll see two options:

- **Pause memory:** Claude keeps its existing memory but won’t use memory or make new memories. Conversations with Claude while memory is paused will not be summarized into its memory should you turn the feature back on.

- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click "Reset memory," this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

## What Claude remembers

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

- Your role, projects, and professional context

- Communication preferences and working style

- Technical preferences and coding style

- Project details and ongoing work
​

## What Claude doesn't remember

### Incognito chats

Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans).

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

---

## Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

- Claude’s memory reflects changes to your conversations as they happen.

- When a conversation expires or is deleted, related memory entries generated from it won’t be removed, but you can delete individual memories at any time.

- All memory data is included in data exports.

- Enterprise data retention policies apply to all memory-related data, including incognito chats.
​

---

## User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

### View and manage your memory

See exactly what Claude remembers about you by navigating to **[Settings > Memory](https://claude.ai/new#settings/customize-memory).** The Memory panel lists everything Claude remembers, grouped by category. Select any entry to see its summary and details.

To change an entry, use the "Tell Claude what to change or remove" box. To remove an entry entirely, select "Delete." You can also update your memory directly from your chats. Simply tell Claude what you'd like it to remember, and it will update Claude’s memory of you without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation.

### Past chat citations

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

### Toggle search past chats and memory on/off

You maintain control over Claude’s ability to search past chats and use memory–you can always disable these features and enable them again when needed in **[Settings > Memory](https://claude.ai/new#settings/customize-memory).**

### Importing your memory from other AI tools

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

---

## Information for legacy memory users

**Important:** We are gradually introducing an improved experience for memory from chats. The sections below only apply to people who have the legacy memory experience and see **Memory** in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**. If you see **[Settings > Memory](https://claude.ai/new#settings/customize-memory)**, you’re using the new memory experience and the sections above apply to you.

### Search past chats with Claude

Searching past chats is available to users on paid plans (Pro, Max, Team, and Enterprise plans) on the web, Claude Desktop, and Claude Mobile apps.

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

### What Claude can search

You can prompt Claude to search conversations within these boundaries:

- All chats outside of projects.

- Individual project conversations (searches are limited to within each specific project).

### Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

- "What did we discuss about [topic]?"

- "Can you find our conversation about [subject]?"

- "Let's continue where we left off with [project]."

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

### Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and find the **Preferences** section. Switch the toggle next to “Search and reference chats” off:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1784810700&amp;signature=b9247a226a5f62a6d1e6aac3c16e53e3092fe71075a01a2dc04dc89f16986844&amp;req=dScmH859nYlXUPMW1HO4zRzXH1s4IjHFJG68qZhl783g1KJ7G5mVmgotrMbD%0Acmwk4QXXpOGcQFdhb3Y%3D%0A)

### Can I exclude a specific past chat from searches?

Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans). See **[Use incognito chats](https://support.claude.com/en/articles/12260368)** for more information.

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1784810700&amp;signature=dbdbc723ca1df0c6e65bbb0c60e8e8fb9ed0469465ea3d50924b44dd42d017e2&amp;req=dScmH859nYlWWvMW1HO4za54sKdkPYa8XDpzhlKsgjNdUvWfnggQ4NWlxH9w%0Ajy15lo%2FFQsq07Af8quQ%3D%0A)

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

**Important:** If you’re using an Enterprise or Team plan account, incognito chats are included in standard data exports and follow your organization's data retention policies. You can’t search past chats if your organization uses customer-managed encryption keys on an Enterprise plan because conversation content is encrypted.

---

### What is Claude's memory?

The legacy memory from chats experience is available for Enterprise plans. Memory applies to chats on the web, Claude Desktop, and Claude Mobile, and is not currently available for Cowork.

Claude can now generate memory based on your chat history. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

### How does Claude’s memory work?

In addition to searching past chats, enabling Claude’s memory feature adds several capabilities.

**Memory summary**

Claude will automatically summarize your conversations and create a synthesis of key insights across your chat history (not including chats in projects). This synthesis is updated every 24 hours and provides context for every new standalone conversation.

**Project memory and summary**

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

### Enable Claude’s memory

**Note:** Members of Enterprise plans can only enable this feature individually when it’s enabled by an Owner for their organization. See **[Controls for Enterprise plan Owners](#h_f7d6b307e2)** for more information.

You can toggle Claude’s memory on by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)**:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1784810700&amp;signature=033c789b76c0e76fcbbd9b694932a963ba5b910b2e0bed52049b182be2fc82e3&amp;req=dScmH859nYlWW%2FMW1HO4zTD5MMXuduRCBq9N9dRTKYd3CSP5s%2BhaeV8e0xT6%0APrG3cWktVrqBdJd6Zr0%3D%0A)

If you want to disable Claude’s memory, click the toggle to see two options:

- **Pause memory:** Claude keeps its existing memory but won’t use memory or make new memories. Conversations with Claude while memory is paused will not be summarized into its memory should you turn the feature back on.

- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click “Reset memory,” this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

**Note:** Pausing or resetting memory also hides your monthly recap, since Claude builds the recap from the same chat history. Learn more about **[the monthly recap](https://support.claude.com/en/articles/15672559)**.

### What does Claude remember?

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

- Your role, projects, and professional context

- Communication preferences and working style

- Technical preferences and coding style

- Project details and ongoing work

### What Claude doesn't remember

**Incognito chats**

Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans).

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

---

### Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

- Deleted conversations are removed from memory synthesis.

- Claude’s memory is updated within 24 hours when conversations are created, modified, or deleted.

- All memory data is included in data exports.

- Enterprise data retention policies apply to all memory-related data, including incognito chats.

---

### User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

**View and manage your memory summary**

See exactly what Claude remembers about you by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and clicking “View and edit memory.” The **Manage memory** modal displays everything Claude remembers about you. In addition to asking Claude to edit the existing summary, you can also tell Claude what you want it to remember. To add custom instructions to Claude’s memory, click the pencil icon in the lower left corner of the summary.

You can also update your memory summary directly from your chats. Simply tell Claude what you'd like it to remember, and it will update your memory summary without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation, so you don’t need to wait for the daily synthesis to run.

**Past chat citations**

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

**Toggle search past chats and memory on/off**

You maintain control over Claude’s ability to search past chats and use memory – you can always disable these features and enable them again when needed in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**.

**Importing your memory from other AI tools**

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

---

### Controls for Enterprise plan owners

Enterprise plan Owners and Primary Owners have specific controls for managing memory features across their organization.

**Organization-level memory controls**

The organization-wide **Generate memory from chat history** toggle is enabled by default. When enabled, individual users can manage their own memory settings. Owners can disable the memory summary feature for their entire organization by navigating to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. When disabled by an Owner, it immediately deletes all existing memory synthesis data for all users, and individual users cannot modify or access the memory synthesis setting.

**Important:** Disabling Claude's memory at the organization level will automatically and permanently delete all memory data for all users in your organization.

**Data handling and compliance**

- **Chat summaries** are stored alongside conversation data and follow your organization's existing data retention policies. When a conversation is deleted, its summary is also deleted.

- **Memory synthesis** is stored with encryption at rest and is tied to underlying conversations. As conversations expire or are deleted according to your retention settings, the synthesis updates accordingly.

- **Incognito chats** don't contribute to memory and aren't visible in users' chat histories, but they remain available to Owners through data export features and are subject to your existing data retention policies (retained for at least 30 days for safety purposes).

**Audit logging and data exports**

- **Audit logging:** The system logs when org-level memory toggles are enabled or disabled by Owners. Standard conversation access logging applies to memory synthesis. Individual user memory edits are not logged.

- **Data exports:** Memory synthesis and chat summaries are included in standard conversation history exports. Incognito chats are included in organizational data exports. All exported chat summaries remain tied to their source conversations.

**Important:** All memory will be retained and exportable by admins in accordance with existing enterprise chat data retention policies.

**Team plan limitations**

Team plans do not have organization-level controls for memory features. Individual Team plan members manage their own memory settings directly.
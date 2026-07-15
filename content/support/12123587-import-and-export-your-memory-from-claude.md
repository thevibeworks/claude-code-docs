# Import and export your memory from Claude

Memory imports are available for Free, Pro, Max, and Team plans on the web and Claude Desktop.

You can transfer your memory between Claude and other AI providers. This lets you import memories from other AI providers into Claude, or export your Claude memory for backup or migration.

## Import memory into Claude

You can bring your memory over from other AI providers using Claude's built-in import flow.

### Step 1: Export your memory from your current AI service

We recommend using the following prompt. It’s written specifically to help you get all of your context in one chat.

*I'm moving to another service and need to export my data. List every memory you have stored about me, as well as any context you've learned about me from past conversations. Output everything in a single code block so I can easily copy it. Format each entry as: [date saved, if available] - memory content. Make sure to cover all of the following — preserve my words verbatim where possible: Instructions I've given you about how to respond (tone, format, style, 'always do X', 'never do Y'). Personal details: name, location, job, family, interests. Projects, goals, and recurring topics. Tools, languages, and frameworks I use. Preferences and corrections I've made to your behavior. Any other stored context not covered above. Do not summarize, group, or omit any entries. After the code block, confirm whether that is the complete set or if any remain.*

You can customize this prompt to exclude any sensitive information before importing into Claude. If your current service supports generating files, you can also ask it to export your memory as a Markdown file so you can save a copy for your records.

### Step 2: Open the import flow in Claude

There are two ways to start the import:

- Go to **[Settings > Capabilities](http://claude.ai/settings/capabilities)**, find the **Memory** section, and select “Start import.”

- From the home screen, click “Get started” on the "Import memory to Claude" card.

The import flow will display the prompt shown above, along with a text box where you can paste the results.

### Step 3: Paste your exported memory and import

Paste the exported text from your previous AI provider into the text box and click the “Add to memory” button to submit it. Claude will extract key information and store it as individual memory edits. You can review these edits by clicking “Manage edits.”

Once the import is complete, you'll see your updated memory within 24 hours. Click the “See what Claude learned about you” button to start a new conversation using this prompt: "I updated my memory. What did you learn about me?"

Claude's memory is designed to focus on work-related topics to enhance its effectiveness as a collaborator. As a result, Claude may not retain imported personal details unrelated to work. If you want to add specific information into Claude's memory, go to **[Settings > Capabilities](http://claude.ai/settings/capabilities)**, click “View and edit your memory,” and add that information as an edit.

**Important:** Memory imports are **experimental and still in active development,** and at this stage,  Claude may not always successfully incorporate imported memories.

## Export memory from Claude

To view your memory exactly how Claude sees it, go to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and click “View and edit your memory.” Alternatively, you can access memory directly in a chat with Claude by asking it, "Write out your memories of me verbatim, exactly as they appear in your memory." You can save this exported memory as a backup or bring it to another AI service by copying and pasting it into a local file on your computer.
> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Comments

> Comments in Claude Science pin a note to a specific part of an artifact, such as selected text or a point on a figure, and send the note to Claude.

In Claude Science, comments let you pin notes to specific parts of an artifact instead of describing a location in prose. Select text in a Markdown, plain-text, LaTeX, or code file; select text in a PDF; click a point on an image or figure; or turn on **Comment** and click an element in a rendered HTML report. You can also comment on session transcripts. You can't comment on tables or other artifact types.

<Note>
  This page covers comments on [artifacts in the Claude Science app](/docs/claude-science/artifacts). For artifacts in a claude.ai chat, see [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) in the help center.
</Note>

## Leaving a comment

* Select content in an artifact and click **Comment**.
* Type your comment and press Enter (or click **Save**). Press Shift+Enter for a new line.
* The comment appears as a highlighted badge (text) or numbered pin (images). Hover to read it; click to **Edit** or **Delete**.

## Sending comments to Claude

Saving a comment doesn't send it. Pending comments appear above the message box and are sent with your next message. This lets you batch several comments and send them together, or send them one at a time. Claude receives each comment with its filename, the quoted selection (or marked image), and your note.

On an image, you can click **Ask** instead of **Save** to send the comment to a side chat, a separate conversation that starts from the current one. The new comment goes with any other comments waiting above the message box:

* If the conversation has messages and no side chat is open, a side chat starts and the comments are sent right away.
* If a side chat is already open, the comments appear above the side chat's message box and are sent with your next message there.
* If the conversation has no messages yet, no side chat starts, and the comments are sent with your next message.

If you click **Ask** without typing a comment, the comment reads "What's going on here?"

Once sent, comments leave the artifact and appear as cards on the message. Comments don't have threads or a resolve state. To revise an artifact again after Claude updates it, comment on the new version.

Limits: comment text is capped at 1,000 characters. Comments aren't included in downloads and don't appear in **Files**.

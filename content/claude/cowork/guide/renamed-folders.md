> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Keep a folder connected after it's renamed or moved

> On macOS, Claude Desktop can find a connected folder at its new location and ask whether to keep it connected to your session.

When you connect a folder on your computer to a session that runs in the cloud, Claude reaches the folder by its location. If the folder is renamed or moved, Claude no longer finds it there. On a Mac with Apple silicon, Claude Desktop can find the folder at its new location and ask whether to keep it connected, so you don't have to connect it again. Some versions of Claude Desktop don't have this prompt. If you don't see it, update Claude Desktop to the latest version.

## Answer the prompt

The prompt appears in Claude Desktop when Claude next runs a shell command in a session that uses the folder. It shows the folder's new location first, then its old location. Check both before you answer.

* **Keep connected**: Claude can read and modify files at the new location, and run commands that access it, in the session that tried to use the folder. Permission to delete files doesn't carry over. Any other session that uses the folder isn't changed, and asks separately.
* **Not now**: that session won't use the folder until you connect it again. Claude Desktop can ask again after you restart it.

Claude can rename and move folders inside the folders you connect. If you didn't rename or move the folder yourself, and didn't ask Claude to, click **Not now**.

You answer by clicking a button. Pressing Return does nothing, and pressing Escape is the same as **Not now**. If you don't answer within 10 minutes, the prompt closes and the session stays without the folder.

If the Claude Desktop window is minimized or another folder prompt is open, the prompt doesn't appear. Claude Desktop tries again when Claude next runs a shell command, after at least a minute.

## When Claude Desktop doesn't ask

Claude Desktop asks only when it can tell that the folder is the same one and can show both locations in full. In these cases it doesn't ask, and Claude can't reach the folder:

* You use Windows or a Mac with an Intel processor.
* You connected the folder with a version of Claude Desktop that doesn't have this prompt.
* The folder moved to another drive or volume or to the Trash, or its drive is disconnected.
* The folder is on a network drive, or on a drive that isn't in a Mac format.
* You connected the folder through a symbolic link, or moved it into a protected folder or one your organization doesn't allow.
* Claude is running a scheduled task, or your organization deploys Claude Desktop with its own model provider.
* The folder's old or new location is very long, or has symbols, emoji, or many spaces in it.

To use the folder again, connect it to the session from its new location.

## Related

These pages cover related topics.

* [Organize work with projects](https://claude.com/docs/cowork/guide/projects.md) for the folders a task can read and write
* [Cowork overview](https://claude.com/docs/cowork/overview.md) for an introduction to Cowork

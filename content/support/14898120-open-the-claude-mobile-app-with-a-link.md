# Open the Claude mobile app with a link

The Claude mobile apps for iOS and Android respond to the `claude://` URL scheme. Third-party apps, shortcuts, and web pages can use these links to open the Code tab, jump to an existing session, or prefill the new-session composer. All parameter values must be URL-encoded.

These links require Claude Code access on your account. If you don't have access to Claude Code, the links won't work.

## Open the Code tab

`claude://code`

Opens the Code tab on the session list.

## Open an existing Code session

`claude://code/{session-id}`

Opens an existing Claude Code session by ID. If the ID is unknown, you'll land on the session list.

## Open a new Code session

`claude://code/new`

With optional parameters: `claude://code/new?q=Fix%20the%20failing%20test&repo=anthropics%2Fclaude-code&branch=main`

Opens the new-session composer, optionally prefilled. All parameters are optional.

| **Parameter** | **Required** | **Description**                                                                                                                        |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `q`           | No           | Text to prefill in the composer. `prompt` is accepted as an alias.                                                                     |
| `mode`        | No           | Pre-selects the session mode. Accepts `plan` or `code`. Ignored if the mode isn't available on your plan.                              |
| `repo`        | No           | Pre-selects a GitHub repository in `owner/name` format (case-insensitive). Ignored if the repo isn't in your connected GitHub account. |
| `branch`      | No           | Pre-selects a branch. Requires `repo`.                                                                                                 |

The **[desktop-only folder and file parameters](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link)** are ignored on mobile.

## Universal links

The same Code routes are also reachable via **<https://claude.ai/code/>...** universal links. If the app is installed, the operating system opens it; otherwise the link opens in the browser.

| **URL**                                                                                                 | **Opens**                                                                                       |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **<https://claude.ai/code>**                                                                            | New-session composer                                                                            |
| **[https://claude.ai/code/{session-id}](https://claude.ai/code/%7Bsession-id%7D)**                      | Existing session                                                                                |
| **<https://claude.ai/code/new?q=Fix%20the%20failing%20test&repo=anthropics%2Fclaude-code&branch=main>** | New-session composer, prefilled with the GitHub repository, branch, and "Fix the failing test." |
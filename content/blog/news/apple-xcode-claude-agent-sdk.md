Title: Apple’s Xcode now supports the Claude Agent SDK

URL Source: https://www.anthropic.com/news/apple-xcode-claude-agent-sdk

Markdown Content:
Apple's Xcode is where developers build, test, and distribute apps for Apple platforms, including iPhone, iPad, Mac, Apple Watch, Apple Vision Pro, and Apple TV.

In September, [we announced](https://www.anthropic.com/news/claude-in-xcode) that developers would have access to Claude Sonnet 4 in Xcode 26. Claude could be used to write code, debug, and generate documentation—but it was limited to helping with individual, turn-by-turn requests.

Now, Xcode 26.3 introduces a native integration with the [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), the same underlying harness that powers Claude Code. Developers get the full power of Claude Code directly in Xcode—including subagents, background tasks, and plugins—all without leaving the IDE.

[Video 3](https://cdn.sanity.io/files/4zrzovbb/website/d5b483d2e9f92f93e24d087b5becfe39abc3a47d.mov)

Claude Agent in Xcode

## **Using Claude for long-running, autonomous work in Xcode**

With the Claude Agent SDK, Claude can now work autonomously on much more sophisticated, long-running coding tasks inside Xcode. Specifically, this integration supports:

*   **Visual verification with Previews.** With the new integration, Claude can capture Xcode Previews to see what the interface it’s building looks like in practice, identify any issues with what it sees, and iterate from there. This is particularly useful when building SwiftUI views, where the visual output is the thing that matters most. Claude can close the loop on its own implementation, allowing it to build higher-quality interfaces that are much closer to developers’ design intent on the first try.
*   **Reasoning across projects.** Building for Apple platforms means working with a wide range of frameworks and technologies, like SwiftUI, UIKit, Swift Data, and many more. Claude can explore a project's full file structure, understand how these pieces connect, and identify where changes need to be made before it starts writing code. When given a task, it works with an understanding of the whole app and its architecture – not just whichever file is currently open.
*   **Autonomous task execution.** Claude can be given a _goal_, rather than a set of specific instructions. It’ll then break the task down itself, decide which files to modify, make the changes, and iterate if something doesn't work. When Claude needs to understand how an Apple API works, or how a specific framework is meant to be used, it can search Apple's documentation directly. And it can update the project as needed and continue until the task is complete or it needs a user’s input—a meaningful time saver for developers who are often working alone or on small teams.
*   **Interface through the Model Context Protocol.** In addition to accessing Claude Agent directly within the IDE, Xcode 26.3 also makes its capabilities available through the Model Context Protocol. Developers using Claude Code can integrate with Xcode over MCP and capture visual Previews without leaving the CLI.

## **Availability**

Xcode 26.3 is available as a release candidate for all members of the Apple Developer Program starting today, with a release coming soon on Apple’s App Store. See Apple’s announcement [here for more](https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/).

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)

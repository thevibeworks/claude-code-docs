> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors and Skills

> Extend Claude for Excel, PowerPoint, Word, and Outlook with external context and reusable task recipes.

Connectors and Skills work the same way across Claude for Excel,
PowerPoint, Word, and Outlook. Both are enabled in your Claude settings.

<Note>
  Connectors and Skills are available when you sign in with your Claude
  account directly. When connecting through a third-party platform such
  as Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM
  gateway, these capabilities may not be available. See the feature
  comparison in
  [Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms)
  for the current status by connection mode.
</Note>

## Connectors

Connect external tools to give Claude context beyond what's in the file
or email you have open. In any Claude for M365 add-in, click the **+** button below
the chat input and select **Connectors** to see available options.

Common connectors used with Claude for M365 include S\&P Global, LSEG, and
Daloopa for financial data, plus any custom connectors your
organization has enabled.

<Warning>
  Custom connectors can introduce security risks. Before enabling one,
  review [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
  for guidance on what to consider.
</Warning>

## Skills

Skills you've enabled in your Claude settings are available in all
Claude for M365 add-ins. Claude applies relevant Skills automatically
based on what you're doing.

You can also invoke a Skill directly: type `/` in the sidebar to see
Skills available for the app you're in, then select one, such as
`/deck-check` in PowerPoint. Skills that aren't relevant to the current
app are excluded from this list.

See [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
for details on enabling and managing Skills.

## Related

See the per-app guides for setup and feature details.

* [Use Claude for Excel](/docs/office-agents/excel)
* [Use Claude for PowerPoint](/docs/office-agents/powerpoint)
* [Use Claude for Word](/docs/office-agents/word)
* [Use Claude for Outlook](/docs/office-agents/outlook)

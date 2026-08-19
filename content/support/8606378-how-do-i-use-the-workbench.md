# How do I use the playground?

**Workbench is now the playground**. Playground enables developers to try out Claude models and API features directly in the Claude Console, but does not support saving prompt history or evaluating prompts.

If you have saved data from **Workbench (legacy)** that you wish to export, you can do so until **September 1, 2026** in **[Console settings](https://platform.claude.com/settings/privacy)**. This data will no longer be recoverable after September 1, 2026. See **[How do I export my Workbench data from Console?](#h_ce935c603b)** for more.

## What is the playground?

The playground is built directly on the public **[Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)**, so the request you build in the playground is the same request you will send in your code.

Use it to:

- Try a model or a new API feature before you write any code

- Iterate on a prompt and inspect the full response

- Learn how API requests and responses are structured

- Export your work as a code snippet you can run in your own application

Playground doesn't store your prompts or conversations on Anthropic's servers. Your current draft stays in your browser, and you can go to the “code" tab to keep a copy of any request.

## Open the playground

1. Log in to the **[Claude Console](https://platform.claude.com/)**.

2. Select "Playground" in the navigation.

3. If your organization uses workspaces, choose the workspace you want to work in.

## Write and run a request

1. Enter a user message in the prompt area. You can also add a system prompt to set instructions or context.

2. Click "Run" to send the request.

3. Review Claude's response, along with the token counts and usage shown for the request.

4. Edit your prompt and run it again to keep iterating.

Playground also includes example templates you can load and modify.

## Choose a model and adjust settings

Use the model selector to switch between Claude models, and open the model settings to adjust parameters like temperature and maximum output tokens.

Running the same prompt with different models or settings is a quick way to see how the response changes. As you think about building your application with the Messages API, use the playground to understand the power of the models.

## Use tools and structured outputs

Add tool definitions to your request to test tool use, and use structured outputs to have Claude return data in a shape you define. Playground shows tool calls and tool results in the response, so you can see exactly how they're represented in the API.

## View the raw request and response

Playground can show the raw API request and response, including the full message structure, stop reason, and usage. This is the same shape your application sends and receives and is a practical way to try out the features of the Messages API.

## Turn your work into code

Click the "code" toggle to export your current request as a code snippet. The snippet reflects exactly what you've tested in the playground, so you can paste it into your project and run it with your own API key.

Code examples in our documentation include an "Open in Playground" option, which loads the example into the playground so you can run and modify it.

---

## How do I export my Workbench data from Console?

1. Go to **[Claude Console](https://platform.claude.com/settings/privacy)**.

2. In the **Export Workbench data** dialog, choose what to include alongside your prompts:

  1. **Model completions** — saved responses from past runs

  2. **Uploaded files** — images and PDFs attached to your prompts
​
​**Note:** Including either may significantly increase the export size.

Primary Owners or Admins also have the option to export data for their entire organization.

3. Select "Export." Your data is packaged as JSON, and we'll email you a download link when it's ready.

Export your data before **September 1, 2026**. It won't be accessible after this date.

---

## Frequently asked questions

### What happened to Workbench (legacy)?

**Workbench (legacy) is now retired.** The playground replaces it for trying Claude models and API features in the Console.  It does not support saving prompt history or evaluating prompts.

### What's the difference between Workbench (legacy) and the playground?

The playground is a simpler, stateless way to try Claude models and API features in the Console. The main differences is that it now:

- It doesn't store your work on Anthropic's servers. Your current draft stays in your browser, and you can export any request as code. With Workbench (legacy) you were able to save prompts, prompt history, and run evals.

- It is built directly on the public Messages API and shows the full request and response, so what you see matches what your code sends and receives.

- Saved prompts, prompt versions, evals, and prompt sharing aren't part of the playground. Use the export function in the legacy version to download your data.

### How do I get access to my existing data from Workbench (legacy)?

You can no longer access this data directly in Console. You can export it as JSON in **[Claude Console](https://platform.claude.com/settings/privacy)** until September 1, 2026. After this date, it will no longer be recoverable.

### Can I import my Workbench data into the playground?

No. The playground doesn't save prompts or conversations, so there's nothing to import into. The export gives you a copy of your Workbench data so you can keep it or move it into your own tools.
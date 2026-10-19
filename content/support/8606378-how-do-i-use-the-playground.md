# How do I use the playground?

Playground enables developers to try out Claude models and API features directly in the Claude Console, but doesn't support saving prompt history or evaluating prompts. The playground replaces Workbench, which was previously used to create and test prompts in the Claude Console.

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

2. Go to the playground (platform.claude.com/playground).

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

## Frequently asked questions

### What happened to Workbench?

**Workbench is now retired.** The playground replaces it for trying Claude models and API features in the Console.  It does not support saving prompt history or evaluating prompts.

### What's the difference between Workbench and the playground?

The playground is a simpler, stateless way to try Claude models and API features in the Console. The main differences is that it now:

- It doesn't store your work on Anthropic's servers. Your current draft stays in your browser, and you can export any request as code. With Workbench (legacy) you were able to save prompts, prompt history, and run evals.

- It is built directly on the public Messages API and shows the full request and response, so what you see matches what your code sends and receives.

- Saved prompts, prompt versions, evals, and prompt sharing aren't part of the playground. Use the export function in the legacy version to download your data.
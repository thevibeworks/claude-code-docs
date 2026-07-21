# How do I use the Workbench?

We’ve recently updated Workbench. The new Workbench enables developers to try out Claude models and API features directly in the Claude Console, but no longer supports saving prompt history or evaluating prompts.

**Workbench (legacy) is no longer available to new users and will be retired for all users on August 17, 2026**. If you're still using the legacy version, see the section below, **[How do I use Workbench (legacy)?](#h_b659fc7faa)**, and if there are prompts, completions, or evals you wish to retain, **consider exporting your data before August 17, 2026.**

## What is Workbench?

Workbench is built directly on the public **[Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)**, so the request you build in Workbench is the same request you'll send in your code.

Use it to:

- Try a model or a new API feature before you write any code

- Iterate on a prompt and inspect the full response

- Learn how API requests and responses are structured

- Export your work as a code snippet you can run in your own application

Workbench doesn't store your prompts or conversations on Anthropic's servers. Your current draft stays in your browser, and you can go to the "code" tab to keep a copy of any request.

## Open Workbench

1. Log in to the **[Claude Console](https://platform.claude.com/)**.

2. Select "Workbench" in the navigation.

3. If your organization uses workspaces, choose the workspace you want to work in.

## Write and run a request

1. Enter a user message in the prompt area. You can also add a system prompt to set instructions or context.

2. Click "Run" to send the request.

3. Review Claude's response, along with the token counts and usage shown for the request.

4. Edit your prompt and run it again to keep iterating.

Workbench also includes example templates you can load and modify.

## Choose a model and adjust settings

Use the model selector to switch between Claude models, and open the model settings to adjust parameters like temperature and maximum output tokens.

Running the same prompt with different models or settings is a quick way to see how the response changes. As you think about building your application with the Messages API, use the workbench to understand the power of the models.

## Use tools and structured outputs

Add tool definitions to your request to test tool use, and use structured outputs to have Claude return data in a shape you define. Workbench shows tool calls and tool results in the response, so you can see exactly how they're represented in the API.

## View the raw request and response

Workbench can show the raw API request and response, including the full message structure, stop reason, and usage. This is the same shape your application sends and receives and is a practical way to try out the features of the Messages API.

## Turn your work into code

Click the "code" toggle to export your current request as a code snippet. The snippet reflects exactly what you've tested in the Workbench, so you can paste it into your project and run it with your own API key.

Code examples in our documentation include an "Open in Workbench" option, which loads the example into Workbench so you can run and modify it.

---

## How do I use Workbench (legacy)?

**Note: Workbench (legacy) is no longer available to new users and will be retired for all users on August 17, 2026.** After this date, Workbench (legacy) and any saved prompts, prompt versions, and evals stored in it will no longer be accessible. Use the Export option to download your data before then.

Workbench (legacy) allows you to create and test prompts within your Claude Console account. You can enter your prompt into the "Human" dialogue box and click "Run" to test Claude's output. Click on the + icon in the upper left to create a new prompt, or click on the bulleted list icon to see prompts you've tested in the past:

![](https://downloads.intercomcdn.com/i/o/888021849/31a22a0dc4d1fc4b605cc8ee/Screenshot+2023-11-19+at+4.21.51+PM.png?expires=1784655000&amp;signature=863111ab16ad533abe676e6210bf3a9e872cfaccdf763f7f8e2aa9f7ae3856e9&amp;req=fCgvFst%2FlYVWFb4f3HP0gKWhcD0J10ZbOkmmaOsi7IBWoag1aPGygfP5TnrV%0AkG8GjEwTNF06oP9U2A%3D%3D%0A)

Workbench (legacy) also allows you to configure several settings when prompting Claude. You can click on the slider icon to review your model settings. This allows you to select the model, temperature, and max tokens to sample:

![](https://downloads.intercomcdn.com/i/o/888023061/61e26396355f6f6cd506d7e4/Screenshot+2023-11-19+at+4.09.28+PM.png?expires=1784655000&amp;signature=e44618373168605faeb9db649b048b091773fa63095ca2781ae0087344a6faba&amp;req=fCgvFst9nYdeFb4f3HP0gN55XdTVPIS3DUq7%2BRvcmSMtY6n%2BWecBm6eo7Sw6%0Abhz5eimwvh1yx3Vkzg%3D%3D%0A)

After crafting your prompt, click on the "Get code" button to generate a sample using our Python and Typescript SDKs:

![](https://downloads.intercomcdn.com/i/o/888023545/b12afe07f16f079daff7587d/Screenshot+2023-11-19+at+4.28.27+PM.png?expires=1784655000&amp;signature=8799051dba7614d9e41a5d4d33ab537167f70778e2dea49a9bb3ceae5dbbe3b8&amp;req=fCgvFst9mIVaFb4f3HP0gEZTsD6b5%2BTrRWixPJbjiQcbYniGiDRi3G7ppK0r%0AerXnmLVoMmkI%2B%2B3o%2BQ%3D%3D%0A)

## How can I access my previous work and prompt history in Workbench (legacy)?

You can access your previous Workbench prompts on your Console account by following these steps:

1. Log in at platform.claude.com.

2. Navigate to your [Workbench](https://platform.claude.com/workbench).

3. Click the "List prompts" button on the upper left corner of the page, next to the "+" button to create a new prompt:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1945992985/45a8969fb6cec956bd44fb5c4ba7/CleanShot+2026-01-15+at+12_07_22%402x.png?expires=1784655000&amp;signature=0fe7aa533216b90f6f3b9e93202e95f7ec4f184c519959199d29e8a1a4748cc7&amp;req=dSkjE8B3n4hXXPMW1HO4zQQ9sFUPMna4TyGSpkcb8MVr2LQlonAJH3qXLMUg%0A1S4V12ajN%2F62BL%2BMdqM%3D%0A)

4. A list of your previously-saved prompts will appear.

5. You can use the search bar at the top of the prompt list if you're looking for something specific.

**Important:** When you run a prompt on Workbench (legacy), Claude's response is not saved by default. You need to manually add responses from Claude to your current prompt on the Workbench by clicking "Add to Conversation" at the bottom of the output. If you aren't seeing something in your history that you were expecting, it's possible that it wasn't added to the conversation.

## How do I export my data from Workbench (legacy)?

1. Open **[Workbench (legacy)](https://platform.claude.com/workbench)** in the Claude Console.

2. In the banner at the top of the page, select "Export data."

3. In the **Export Workbench data** dialog, choose what to include alongside your prompts:

  - **Model completions** — saved responses from past runs

  - **Uploaded files** — images and PDFs attached to your prompts
​
​**Note:** Including either may significantly increase the export size.

4. Select "Export." Your data is packaged as JSON, and we'll email you a download link when it's ready.

Export your data before **August 17, 2026**. It will not be accessible after Workbench (legacy) is retired.

---

## Frequently asked questions

### What’s changing in Workbench?

We’re refreshing Workbench to be a simpler, stateless way to try Claude models and API features in the Console. The main differences are that it now:

- It doesn't store your work on Anthropic's servers. Your current draft stays in your browser, and you can export any request as code. With Workbench (legacy) you were able to save prompts, prompt history, and run evals.

- It is built directly on the public Messages API and shows the full request and response, so what you see matches what your code sends and receives.

- Saved prompts, prompt versions, evals, and prompt sharing aren't part of the refreshed Workbench. Use the export function in the legacy version to download your data.

### Will Workbench (legacy) keep working for me right now?

**Workbench (legacy) is no longer available to new users and will be retired for all users on August 17, 2026.** If you used Workbench (legacy) prior to **June 16, 2026**, you'll continue to have access until the retirement date and will see a banner in Workbench linking to the legacy version so you can export your data. Accounts that started using Workbench on or after June 16, 2026 do not have access to Workbench (legacy). After August 17, 2026, Workbench (legacy) will no longer be available to anyone.

### What happens to my saved prompts and evals?

They remain in Workbench (legacy) until it is retired on August 17, 2026. Use the Export option in Workbench (legacy) to download them before that date. The refreshed Workbench doesn't include saved prompts or evals, so keep your exported copies in your own tools, such as the repository where your application code lives.

### How do I get access to my existing data from Workbench (legacy)?

Your saved prompts and completions are available in Workbench (legacy) until August 17, 2026. You'll see an Export option in Workbench (legacy) that lets you download your saved prompts, prompt revisions, and completions. Export your data before the retirement date, as it will not be accessible afterward.

### Can I import my Workbench (legacy) data into refreshed Workbench?

No. The refreshed version of Workbench doesn't save prompts or conversations, so there's nothing to import into. The export gives you a copy of your Workbench data so you can keep it or move it into your own tools.
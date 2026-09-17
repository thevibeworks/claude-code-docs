> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Safeguards

> What happens when a model's safeguards flag a message, how to switch models automatically, and how to choose a use case under the Life Sciences Verification Program (beta).

Claude models include safeguards that can flag a message and stop the response. Some are intentionally broad and can flag legitimate coding, cybersecurity, and biology work. See [Our Approach to User Safety](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety) for more about these safeguards.

## When safeguards flag a message

When a model's safeguards flag a message, Claude Science pauses the session and shows a **Chat paused** card above the composer. If another model can continue, select **Retry with `<model>`** to retry on the model the card names. That model has its own safeguards. The session stays on it until you choose a different model in the composer.

## Switch models automatically

To have Claude Science retry without stopping at the **Chat paused** card, turn on the **Automatically switch models when a message is flagged** switch under **Settings** > **General** > **Model**. You can also select it on the card before you retry. Claude Science then retries a flagged message on another model right away and shows a notice that names the model it switched to. If no other model can continue, or after several automatic switches in one session, you see the **Chat paused** card instead. Automatic switching is off by default and applies to every session on this computer.

## Life Sciences Verification Program (beta)

Under Anthropic's Life Sciences Verification Program (beta), verified organizations on Team and Enterprise plans can use Claude models with fewer life sciences restrictions. Protections against the most serious misuse stay in place, and safeguards can still flag a message. [What is the Life Sciences Verification Program?](https://support.claude.com/en/articles/16975617) has the details, including which models it applies to and how an organization applies.

## Choose a use case

If you have access through the Life Sciences Verification Program (beta), your organization specified one or more approved research use cases. Claude Science sends a session's use case with the requests it makes for that session, so Claude's safeguards can apply the access approved for that work. Anthropic also monitors program usage against the scope your organization shared when it applied. See [What is the Life Sciences Verification Program?](https://support.claude.com/en/articles/16975617) for data retention and safety review.

With one use case, Claude Science applies it to every session.

With more than one use case, you choose one for each session:

* Claude Science asks you to choose the one that matches your work when you first send a message in a session, unless you've set a default. Everyday tasks like writing or coding are allowed with any use case.
* To switch during a session, open the model picker in the composer and select **Use case**.
* To set a default on this computer, select **Set as default** when Claude Science offers it, or choose one from the **Default use case** menu under **Settings** > **General** > **Model**.

The use case controls need version 0.1.49 or later of the Claude Science app. If you're up to date and don't see a use case, ask your organization's admin.

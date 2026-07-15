# Set organization instructions

Organization instructions let Admins and above on Team and Enterprise plans set custom instructions that Claude follows in every conversation across your organization. Use them to apply communication standards, formatting requirements, compliance guidance, or domain-specific context that should show up everywhere your team works with Claude.

Organization instructions are available to Admins, Owners, and Primary Owners on Team and Enterprise plans.

## How organization and user instructions interact

Claude supports two levels of instructions. Understanding how they interact helps admins and the people on your team get the most out of both.

| **Level**                    | **Set by**                         | **Scope**                                           | **Visibility**                         |
| ---------------------------- | ---------------------------------- | --------------------------------------------------- | -------------------------------------- |
| Organization instructions    | Admins, Owners, and Primary Owners | All people in your organization, every conversation | Only Admins and above can view or edit |
| Individual user instructions | Each user                          | That individual’s conversations only                | Only that user can view or edit        |

When both are set, organization instructions take precedence. If an individual instruction directly contradicts an organization instruction, Claude favors the organization-level instruction. For example, if an organization instruction says “Always respond in formal English” but an individual instruction says “use a casual tone,” Claude responds formally.

Individual instructions still apply for anything the organization instructions don’t address.

**Note:** Instruction prioritization relies on prompt-level instructions. In rare edge cases involving directly contradictory instructions, behavior may vary. Test your instructions to confirm they produce the results you expect.

## Set up organization instructions

You need at least an Admin role to configure organization instructions.

1. Go to **[Organization settings > Organization and access](http://claude.ai/admin-settings/organization)**.

2. Find the **Organization instructions** section.

3. Enter your instructions in the text area. The maximum length is 3,000 characters.

4. Click “Save.”

5. Changes may take up to an hour to take effect across Claude products.

To remove instructions entirely, clear the text area and click “Save.”

---

## Best practices

**Keep instructions concise and clear.** Organization instructions are included in every message sent by everyone in your organization, so shorter instructions help keep conversations efficient. Aim for direct, specific guidance rather than lengthy explanations.

**Be specific about what you want.** Instead of vague instructions like “be professional,” give concrete direction such as “Respond in formal English. Don’t use contractions, slang, or emojis.”

**Focus on consistent behaviors.** Organization instructions work best for instructions that should apply uniformly across every conversation—response formatting standards, tone requirements, or organization-wide context.

**Avoid conflicting instructions.** If your organization instructions contradict each other, Claude may not follow either one reliably. Review your instructions as a whole to make sure they’re consistent.

**Don’t try to override safety behaviors.** Organization preferences can’t disable Claude’s built-in safety guidelines or content policies. Instructions that conflict with Claude’s core training won’t be followed.

**Test your instructions.** After saving, start a new conversation to verify Claude is following your instructions. Try a few different types of questions to confirm the instructions work across a range of topics.

**Review and update regularly.** As your organization’s needs change, revisit your instructions to make sure they’re still relevant. Removing outdated instructions keeps Claude’s responses focused.

---

## Example instructions

**Team identity.** “Address the team as the Acme Platform team. When users ask about ‘our product,’ they mean Acme Cloud.”

**Communication standards.** “Respond in formal English. Use active voice. Avoid contractions and emojis.”

**Response formatting.** “Prefer concise responses under 300 words. Use bullet points for lists with three or more items.”

**Domain context.** “Our team works in healthcare claims processing. When users mention ‘claims,’ they’re referring to insurance claims, not legal claims.”

**Referral guidance.** “When users ask about HR policies, direct them to **<hr@acme.com>** rather than giving specific policy advice.”

**Data handling reminders.** “Don’t include customer names, account numbers, or other personally identifiable information in responses or generated artifacts.”
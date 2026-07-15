# Organization instructions in Claude for Government

Organization instructions allow administrators to define custom instructions that Claude follows in every conversation for all users in the organization. Use this to set compliance guidance, communication standards, formatting requirements, or domain-specific context.

## How organization and user instructions interact

Claude supports two levels of instructions. Understanding how they interact helps administrators and users get the most out of both.

| **Level**                    | **Set by**     | **Scope**                      | **Visibility**                       |
| ---------------------------- | -------------- | ------------------------------ | ------------------------------------ |
| Organization instructions    | Administrators | All users, all conversations   | Only administrators can view or edit |
| Individual user instructions | Each user      | That user's conversations only | Only that user can view or edit      |

When both are set, organization preferences take precedence. If a user preference directly contradicts an organization preference, Claude will strongly favor the organization-level instruction. For example, if an organization preference says "Always respond in formal English" but a user preference says "Use casual tone," Claude will respond formally.

Individual user instructions still apply for anything not addressed by the organization instructions.

**Note**: Instruction prioritization relies on prompt-level instructions. In rare edge cases involving directly contradictory instructions, behavior may vary. Test your instructions to confirm they produce the expected results.

## Set up organization instructions

To configure organization instructions, you must have an Owner or Admin role for your organization.

1. Click the gear icon in the lower left corner and select "Organization settings."

2. Select **Organization**.

3. Locate the **Organization instructions** section.

4. Enter your instructions in the text area. You can include guidance such as compliance rules, formatting requirements, communication standards, or domain-specific context. The maximum length is 3,000 characters.

5. Click "Save." Your instructions take effect immediately for all users in the organization.

To remove instructions entirely, clear the text area and click "Save."

---

## Best practices

**Keep instructions concise and clear.** Organization instructions are included in every message sent by every user in your organization, so shorter instructions help keep conversations efficient. Aim for direct, specific guidance rather than lengthy explanations.

**Be specific about what you want**. Instead of vague instructions like "be professional," provide concrete direction such as "Respond in formal English. Do not use contractions, slang, or emojis."

**Focus on consistent behaviors**. Organization instructions work best for instructions that should apply uniformly across all conversations, such as compliance requirements, response formatting standards, or classification handling rules.

**Avoid conflicting instructions.** If your organization instructions contradict each other, Claude may not follow either one reliably. Review your instructions as a whole to ensure they are consistent.

**Do not attempt to override safety behaviors.** Organization instructions cannot disable Claude's built-in safety guidelines or content policies. Instructions that conflict with Claude's core training will not be followed.

**Test your instructions.** After saving, start a new conversation to verify Claude is following your instructions as expected. Try a few different types of questions to make sure the instructions work well across a range of topics.

**Review and update regularly.** As your organization's needs change, revisit your instructions to ensure they remain relevant and accurate. Removing outdated instructions keeps Claude's responses focused.

---

## Example instructions

**Compliance and classification guidance** — "Treat all responses as CUI. Do not include controlled unclassified information in web search queries or file names."

**Communication standards** — "Always respond in formal English. Use active voice."

**Domain-specific context** — "Users are federal agency employees. When they reference 'the system,' they mean our grants management platform."

**Response formatting** — "Prefer concise responses under 300 words. Use bullet points for lists with three or more items."

**Referral guidance** — "When users ask about HR policies, direct them to <hr@example.com> rather than providing specific policy advice."
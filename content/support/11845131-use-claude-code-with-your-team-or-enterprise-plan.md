# Use Claude Code with your Team or Enterprise plan

This article applies to members of Team or Enterprise plan organizations using their subscription plans to access Claude Code. If you’re an individual consumer using a Pro or Max plan subscription, see **[Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)**.

## What is Claude Code?

Claude Code is a coding tool that gives you access to Claude models directly in your terminal or supported IDE, allowing you to delegate complex coding tasks while maintaining transparency and control.

Claude Code is included with every Team plan seat. Premium seats offer more usage for team members with heavier workloads. For Enterprise plans, Claude Code is included with the single Enterprise seat on new and self-serve plans. On older Enterprise plans, Claude Code is available on Chat + Claude Code seats (usage-based billing) and Premium seats (seat-based billing).

With a Team or Enterprise plan, you can access Claude on the web, desktop, and mobile apps, plus Claude Code in your terminal—all with one unified subscription.

### Why use Claude and Claude Code?

Combine two powerful AI products in one unified subscription:

- Use Claude for writing, research, analysis, and collaboration across teams.

- Use Claude Code for terminal-based coding workflows and development tasks.

---

## Connect Claude Code to your Team or Enterprise plan

### Step 1: Confirm Claude Code access (Enterprise plans only)

If your organization is on a new or self-serve Enterprise plan, Claude Code is already included with every Enterprise seat—no additional purchase is needed. Proceed to Step 2.

**Note:** If your organization has a HIPAA-ready Enterprise plan, Claude Code is included in your seat but is not covered under the HIPAA-ready offering. See **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)** for details.

If your organization is on an older Enterprise plan with Chat and Chat + Claude Code seats, or Standard and Premium seats, you'll need to ensure you have a seat type that includes Claude Code. Owners can purchase or reassign **Chat + Claude Code / Premium seats** in **[Organization settings > Organization](https://claude.ai/admin-settings/organization)**. See **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)** for details.

### Step 2: Download and install Claude Code

**Note:** If you already have Claude Code installed on your computer, proceed to Step 3.

Once you confirm you have access, follow the installation instructions in our **[Claude Code Docs](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)** for the environment you're using.

### Step 3: Authenticate with the Team or Enterprise account

1. Type `claude` within your Terminal window to start a Claude Code session.

2. When prompted during setup or first use, select a login method.

  1. If you're already logged in to Claude Code via a different account, run /login to select a different login method.

3. Select “Claude account with subscription” to be routed to an OAuth prompt.

4. Select your Team or Enterprise plan and click “Authorize.”

5. Your premium seat subscription will be linked to Claude Code.

### Having trouble using your Team or Enterprise account to access Claude Code?

If you're not seeing the option to authenticate with your preferred account, follow these steps to update Claude Code:

1. Log out of your active session completely using the `/logout` command.

2. Run `claude update`.

3. Restart your terminal completely for the change to take effect.

4. Run `claude` and select the correct account to use Claude Code.

## Use Claude Code in your IDE

Your seat also covers Claude Code in supported IDEs, including VS Code, Cursor and other VS Code forks, and JetBrains IDEs like IntelliJ and PyCharm. Log in with the same Team or Enterprise account you use in the terminal. IDE usage is limited and billed the same way as terminal usage on your plan.

To install and set up the extension for your IDE, see **[Platforms and integrations](https://code.claude.com/docs/en/platforms)** in our Claude Code Docs.

---

## What happens when you hit usage limits

If your organization is on a **usage-based Enterprise plan** (including self-serve Enterprise), there are no per-seat usage limits—usage is based on consumption and billed at API rates. See **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)** for details on how usage billing works.

If your organization is on a Team plan or a seat-based Enterprise plan, you can enable usage credits to allow team members to continue working with Claude, Cowork, and Claude Code after reaching their included usage limits. For more information, see **[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-)**.
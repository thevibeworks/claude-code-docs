# Get started with 1Password for Claude

1Password for Claude lets Claude complete browser tasks that require signing in, using logins you've stored in 1Password. 1Password fills the credential directly on the page, so Claude never sees your password or one-time code.

1Password for Claude is in beta for paid plans (Pro, Max, Team, Enterprise) using Claude Desktop on macOS. It's available to 1Password customers on individual, family, and business plans, and requires Claude in Chrome. 1Password for Claude is off by default for Team and Enterprise plans.

## How it works

When Claude reaches a login page during a task, it requests the credential from 1Password instead of asking you to type it. 1Password shows you exactly which item Claude is requesting, and you approve, swap, or deny the request in a single prompt confirmed with biometrics.

After you approve, 1Password fills the login directly on the page. Claude knows which login it used, but the password and any one-time code never enter Claude's context, memory, or Anthropic's systems. Access is scoped to the current task and ends when the task is complete.

After filling a login, 1Password checks that no credentials were exposed on the page. If a submission fails, 1Password clears the filled values before returning control.

## Requirements

To use 1Password for Claude, you'll need:

- A Mac

- **[Claude Desktop](https://support.claude.com/en/articles/10065433)**

- **[Claude in Chrome](https://support.claude.com/en/articles/12012173)**

- A 1Password account (individual, family, or business plan)

- **[The 1Password desktop app](https://1password.com/downloads/mac)**

- **[The 1Password browser extension](https://1password.com/downloads/browser-extension)**

If you're on a Team or Enterprise plan, an Owner must also enable the integration for your organization. See **[Enable 1Password for Claude for your organization](#h_f7c663d5a2)** below.

## Connect 1Password to Claude

Once the requirements are in place, you can set up 1Password from a few places in Claude:

- A banner in Claude Desktop when 1Password is detected

- An in-chat prompt that appears when a task needs a login

- By navigating to **Settings > Connectors** (under **Customize**) in Claude Desktop and clicking “Connect” next to 1Password.

## Enable 1Password for Claude for your organization

1Password for Claude is off by default for Team and Enterprise organizations. To enable it:

1. Sign in to Claude with your Owner or Primary Owner account.

2. Navigate to **[Organization settings > Claude in Chrome](https://claude.ai/admin-settings/browser-extension)**.

3. Toggle on **Enable for your team** if it isn't already on.

4. Toggle on **Password managers**:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2546126596/ba71ca47e2df21cec62c243831f8/5b1c67e1-607d-4c73-8f61-d1ceb081082a?expires=1784262600&amp;signature=a78b5ac375bafa4d1cdbe2ed479d81e39443c360d1188432be20df9b873dd9f9&amp;req=diUjEMh8m4RWX%2FMW1HO4zU5lnm9sq8dlGkiu4hEpcPX2YjvVsLGGmyj6MHL%2B%0AFbPNkJ7wpyFqGeq%2FWE8%3D%0A)

Once enabled, eligible users will see the discovery options above. Users still need to install and set up the required apps and extensions themselves.

## Approve credential requests

Each time Claude needs a login during a task:

1. 1Password shows which vault item Claude is requesting.

2. Review the request. You can approve it, swap in a different login, or deny it.

3. Confirm your choice with biometrics.

1Password then fills the credential directly on the page. You approve credential use per task, so Claude never has standing access to your vault.

## Agentic Mode

Agentic Mode is a feature of the 1Password browser extension that protects your vault whenever an AI agent controls the browser. When Claude takes over, the 1Password extension locks down automatically. The extension's interface is hidden, and Claude can only use the logins and one-time codes you've approved for the current task. The rest of your vault stays out of reach.

Agentic Mode is on by default at the extension level and works even if you haven't set up 1Password for Claude. Open the 1Password extension at any time to confirm it's active or to cancel the current task.

## What Claude can and can't see

Claude can see which login it used to complete a task. Claude can't see:

- Your passwords

- Your one-time codes

- The contents of your 1Password vault

Credentials are injected through a secure channel handled by 1Password, outside of Claude's view. They stay encrypted in 1Password and under your control.

## Supported item types

1Password for Claude supports logins and one-time codes (TOTP). Other item types, like credit cards and identities, aren't supported.

## Stay safe

1Password for Claude reduces credential exposure, but browser-based AI still carries risk. Check each approval prompt so you know which credential Claude is requesting before it's used, and review **[Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428)** before working with sensitive accounts.
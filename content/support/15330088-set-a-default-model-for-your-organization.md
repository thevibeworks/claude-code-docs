# Set a default model for your organization

This guide explains how to choose the Claude model that new conversations start on across your organization. You can set one default for your whole organization, or set different defaults for specific custom roles.

Default model settings are available for Enterprise plan organizations. Primary Owners, Owners, and members whose custom role grants the Identity & Access permission can manage them in **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

You can also set the default effort level that new conversations start on, or leave it on Anthropic's recommended default effort. To control which models members can use and cap the effort level they can select, see **[Manage model access for your organization](https://support.claude.com/en/articles/15330089)**.

---

## How default models work

When you set or change a default model, it replaces the model currently selected in each member’s model picker. New conversations in chat, Claude Cowork, Claude Code, and Office Agents then start on the model you’ve chosen.

**Note:** Not all models are available in every product. If the selected model is not available in the product, Anthropic’s recommendation is used as default.

Members can still select a different model for any conversation. Claude remembers each member’s last selection, so their next conversation starts on whichever model they last used. When you update the default again, the new default replaces their selection.

For example: you set the organization default to Claude Sonnet 4.6, and every member’s new conversations start on Sonnet 4.6. A member switches a conversation to Claude Opus 4.7, so their next conversations start on Opus 4.7. When you later change the organization default, the new default replaces their selection again.

You can set a default at two levels:

- Organization default: applies to every member of your organization.

- Custom role default: applies to members assigned to that role and takes precedence over the organization default.

Alongside the default model, you can set a default effort level. New conversations on the default model start at that effort level. Members can still change the effort level for any conversation, within the organization's effort cap for that model and any cap set by their custom role. If the default effort is higher than a cap that applies to a member, their conversations start at the highest level they're allowed.

**Note:** Members on Claude Code CLI versions earlier than 2.1.199 won't pick up the organization default. Versions 2.1.196 through 2.1.198 also had a bug where setting a specific organization default caused other enabled models to disappear from the model picker in the CLI and VS Code extension; updating to 2.1.199 or later resolves both.

For member-facing CLI instructions, see **[Claude Code model configuration](https://support.claude.com/en/articles/11940350)**.

For member-facing instructions on switching models, see **[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)**.

---

## Set the organization default model

The organization default applies to every member. To set it:

1. Navigate to **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

2. Under **Default model**, select an option under the model dropdown list:

  1. “Use Anthropic’s recommended default”: Anthropic’s recommended model that updates automatically when new models are released.

  2. “Choose a specific model”: a specific model that won’t change when new models are released.

3. If you select “Choose a specific model,” choose a model from the list. Only models enabled under **Model access** on the same page can be selected.

4. Click “Save changes.”

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514722139/d05c94072a41ea9090ecf386c53e/c32ee31d-954a-4551-a2da-91677fbd0b6f?expires=1788586200&amp;signature=a54024b39ca656252e608c7d5fe81fa58a4ab175e0f4f790f33bb6ce845c9aaf&amp;req=diUmEs58n4BcUPMW1HO4zelOdzpFJU5FfdGVZ664dGEMFogCeoQ1nJOby4zY%0AUG0H3CDcdvf1I9hryG0%3D%0A)

---

## Set the default effort level

The default effort level applies to new conversations on the organization default model. To set it:

1. Navigate to **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

2. Under **Default model**, select an option under the effort level dropdown list:

  1. "Use Anthropic's recommended default effort": Anthropic's recommended effort level for the default model, which updates automatically when recommendations change.

  2. Choose a level from the list. Available effort levels differ depending on the model, and some models don't support effort level settings at all.

3. Click "Save changes."

The default effort level can't be higher than the organization's effort cap for the default model. If you lower that cap below the current default effort, the default effort is lowered to match.

---

## Set a default model for a custom role

Custom role defaults let you set different starting models for different teams. For example, you can keep most of your organization on the recommended default while a specific group starts on a different model.

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit, or create a new role.

3. Select the **Models** tab, then under **Default model**, select a model. Roles are set to “None selected” unless you choose a specific model. Only models the role has access to can be selected.

4. Click “Save role” to save your changes.

A role’s default model takes precedence over the organization default for members assigned to that role.

If a member belongs to multiple groups whose custom roles set different default models, the most capable model will be the default. Capability is determined first by model family (Haiku, Sonnet, Opus), then release date, so more capable model families take precedence, and newer models within the same family take precedence.

The role's effort cap for the default model, if any, still applies. A role can't set an effort cap higher than the organization's cap for that model. For details, see **[Limit the maximum effort level for a custom role](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization#h_e693614582)**.

**Note:** Custom roles only affect members whose role is set to “Custom.” Members with the User, Admin, or Owner roles get the default model from the organization setting, not from custom roles.

For details on creating roles and assigning them to groups, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

---

## Default model and Claude Code managed settings

If your organization also configures Claude Code through `managed-settings.json`, the model setting there takes precedence. When model is set in managed settings, Claude Code CLI and IDE start on that model and ignore the default you set in **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

If `managed-settings.json` specifies `availableModels` that doesn't contain the default model, Claude CLI bypasses `availableModels` and starts on the selected default model unless `enforceAvailableModels` is set.

Managed settings for models apply only to Claude Code CLI and IDE, not to Claude Code on web or desktop. For consistent behavior across all Claude Code surfaces, we recommend setting the default here alone. For more on managed settings, see **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.
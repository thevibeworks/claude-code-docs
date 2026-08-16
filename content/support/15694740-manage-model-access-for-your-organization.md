# Manage model access for your organization

This guide explains how to control which Claude models members of your organization can use, and how to cap the effort level each role can select per model. You can manage model access for your whole organization or for specific custom roles.

Model access settings are available for Enterprise plan organizations. Primary Owners, Owners, and members whose custom role grants the Identity & Access permission can manage them in **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

To set the model new conversations start on, see **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

---

## How model access works

Model access is determined at two levels:

- **Organization level:** each model is enabled or disabled for everyone in your organization. Disabling a model here removes it for every member, including Owners and Admins.

- **Custom role level:** for members on custom roles, each role grants access to a subset of the models enabled at the organization level. A role can also cap the maximum effort level members can select on each model.

The organization setting is the ceiling, so a role can’t grant access to a model that’s disabled for the organization. When the feature first becomes available, every model is enabled at both levels, so nothing changes for your members until you adjust these settings.

**Note:** Haiku models are always available to every member and can’t be disabled. This guarantees members always have at least one model to fall back to.

## Who each level affects

- Disabling a model at the organization level affects every member, including Primary Owners, Owners, Admins, and Users.

- Role-level model access and effort limits affect only members whose role is set to “Custom.” Members with the User, Admin, or Owner roles can use every model enabled at the organization level, at any effort level.

---

## Enable or disable a model for your organization

1. Navigate to **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

2. Under **Model access**, find the model you want to change.

3. To enable a model, switch the toggle next to it on, then click the role dropdown to select the roles that can access it.

4. To disable a model, click the role dropdown and deselect the roles before switching the toggle off.

5. Click "Save."

If any custom role uses the model you’re disabling as its default, you’ll be prompted to change that role’s default before the change can be saved.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693921/02ea72756f5163f14e5d158516dc/69102088-cd86-498e-97aa-c8a6e0004419?expires=1786862700&amp;signature=1149c69043ada33fdc865fa210a411afc871e1981969e1f77be6794b14fc2b85&amp;req=diUmEs93nohdWPMW1HO4zXlxEuGxUdNQQf5Pb7M2Q0t8sb5XpmeC0rZBJ%2Bvc%0AW%2BRTIVQouKkG1nBxmZA%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693922/bfc5de6626eb19dca1d7caf818ca/c3cd8bb6-f86c-4d01-92da-6ae4ca966662?expires=1786862700&amp;signature=794ef1c20f3104616c35e5885715cbc383045ef35fa08b80edccf6151db30b73&amp;req=diUmEs93nohdW%2FMW1HO4zTqNsY%2FNQFpQAod9uc510lzXX%2FKn0iNH3qyTLzxU%0AWMp0uMydF7gtGe8JRH8%3D%0A)

---

## Set model access for a custom role

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit, or click “Add role” to create one.

3. Select the "Models" tab.

4. Under **Model access**, switch each model on or off. Models disabled at the organization level appear but can’t be enabled until you turn them on for the organization.

5. Click “Save.”

Only models the role grants access to can be selected as that role’s default model.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693923/880665a87dbd4776cf19d6063a37/29d30c6d-f9fc-408c-8c72-4320c6d88d14?expires=1786862700&amp;signature=fb4551a184d1b186d45791cf840921383992b768729f3fb72a364743459747ad&amp;req=diUmEs93nohdWvMW1HO4zYj9SfML64O6XsqpNqvyFRJZLvakI4NkE2d6Kz0K%0ALEUMkRY2xgD%2BO3EDpzk%3D%0A)

---

## Limit the maximum effort level for a custom role

Effort limits determine how much computation members on a role can apply per response on each model. Higher effort levels produce more thorough responses but consume more usage. Effort limits can only be set per role, not at the organization level.

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit.

3. Select the "Models" tab.

4. Next to a model, click the gear icon and choose a level.

5. Click "Save" to save your changes.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693927/7a25673b3b075d72adb3cdc371e3/d2d7cd8d-a713-4e91-a706-f589ac46a9fe?expires=1786862700&amp;signature=6e9bf72fa3a20bcb095dcf366d157219e3a0c365a0bccba3abbba5c888ec1dcc&amp;req=diUmEs93nohdXvMW1HO4ze1xBjW0dbseDeA1RkowXUFG75dVf9ulEQqqN3B%2B%0AHL%2F3o56qd%2BINLeCyG3w%3D%0A)

Members on the role see only effort levels at or below the cap in their model menu. Note that available effort levels differ depending on the model, and some models don’t support effort level settings at all. For an explanation of each level, see **[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678)**.

---

## How access combines across multiple roles

If a member belongs to multiple groups with different custom roles, model settings combine like other role permissions:

- **Model access is additive.** The member can use every model granted by any of their roles, as long as it’s enabled at the organization level.

- **Effort limits take the highest cap.** For each model, the member gets the highest maximum effort level any of their roles allows.

For how default models are chosen across multiple roles, see **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

For details on creating roles and assigning them to groups, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

---

## What users see

In every covered product, the model picker shows only the models the member has access to. Effort levels above a role’s cap don’t appear in the effort menu.

Model availability also depends on the product. Each product supports a different set of models, so an enabled model appears only in the products that support it.

If you disable a model a member is using in an open conversation or session, that conversation falls back to the member’s default model the next time they open it. If the member sends a message while you’re making the change, they’ll see an error that the model isn’t available and be prompted to switch.

---

## Where model access settings apply

Model access settings are enforced across these products:

| **Product**                        | **Model access settings apply** |
| ---------------------------------- | ------------------------------- |
| Chat (web, desktop, mobile)        | ✅                               |
| Claude Cowork                      | ✅                               |
| Claude Code (CLI, remote, desktop) | ✅ CLI version 2.1.199 or later  |
| Claude for Microsoft 365           | ✅                               |
| Claude Tag                         | ✅                               |
| Claude Design                      | ✅                               |
| Claude in Chrome                   | Not yet supported               |
| Claude Security                    | Not yet supported               |

**Note:** Members on Claude Code CLI versions earlier than 2.1.199 still see disabled models and effort levels in the picker, but requests using them are rejected.

## Model access and Claude Code managed settings

If your organization also configures Claude Code through `managed-settings.json`, the `availableModels` setting and model access work together. In Claude Code CLI and IDE, members see only models that appear in `availableModels` *and* are enabled by their model access settings—a model removed by either one is unavailable.

Managed settings for models apply only to Claude Code CLI and IDE, not to Claude Code on web or desktop. For consistent behavior across all Claude Code surfaces, we recommend using model access settings alone. For more on managed settings, see **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.
# Manage model access for your organization

This guide explains how to control which Claude models members of your organization can use, and how to cap the effort level members can select on each model. Model access and effort limits can be set for your whole organization or for specific custom roles.

Model access settings are available for Enterprise plan organizations. Primary Owners, Owners, and members whose custom role grants the Identity & Access permission can manage them in **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

To set the model new conversations start on, see **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

---

## How model access works

Model access and effort limits are determined at two levels:

- **Organization level:** each model is enabled or disabled for everyone in your organization. Disabling a model here removes it for every member, including Owners and Admins. You can also set a maximum effort level for each enabled model, which applies to every member.

- **Custom role level:** for members on custom roles, each role grants access to a subset of the models enabled at the organization level. A role can also cap the maximum effort level members can select on each model, at or below the organization's cap for that model.

The organization setting is the ceiling. A role can't grant access to a model that's disabled for the organization, and a role can't allow an effort level higher than the organization's cap. When the feature first becomes available, every model is enabled and set to its highest effort level at both levels, so nothing changes for your members until you adjust these settings.

**Note:** Haiku models are always available to every member and can’t be disabled. This guarantees members always have at least one model to fall back to.

## Who each level affects

- Disabling a model or capping its effort level at the organization level affects every member, including Primary Owners, Owners, Admins, and Users.

- Role-level model access and effort limits affect only members whose role is set to "Custom." Members with the User, Admin, or Owner roles can use every model enabled at the organization level, up to the organization's effort cap for that model.

---

## Enable or disable a model for your organization

1. Navigate to **[Organization settings > Models](https://claude.ai/admin-settings/models)**.

2. Under **Model access**, find the model you want to change.

3. To enable a model, switch the toggle next to it on, then click the role dropdown to select the roles that can access it.

4. To disable a model, click the role dropdown and deselect the roles before switching the toggle off.

5. Click "Save."

If any custom role uses the model you’re disabling as its default, you’ll be prompted to change that role’s default before the change can be saved.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693921/02ea72756f5163f14e5d158516dc/69102088-cd86-498e-97aa-c8a6e0004419?expires=1788534000&amp;signature=6e153cf46b8bf19d707777e323d4ce5ed0e55788bdbea202f639d75f55161bd6&amp;req=diUmEs93nohdWPMW1HO4zXlxEu%2B8VNVXQf5Pb7M2Q0tALihy%2BbRnbDj3GG%2B9%0As5ptxhDb7ZbB79yhpYI%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693922/bfc5de6626eb19dca1d7caf818ca/c3cd8bb6-f86c-4d01-92da-6ae4ca966662?expires=1788534000&amp;signature=4ffa874ae1ad8bfe8f29894f14ec06e5cac22651df6acff3b4572893200984a3&amp;req=diUmEs93nohdW%2FMW1HO4zTqNsYHARVxXAod9uc510lwSz1%2BUJbsWzUIyEmkK%0A%2F%2BOCbavr4zcgHSb3Prg%3D%0A)

---

## Limit the maximum effort level for your organization

Effort limits determine how much computation members can apply per response on each model. Higher effort levels produce more thorough responses but consume more usage. An organization-level effort cap applies to every member and is the highest level any custom role can allow.

1. Navigate to **[Organization settings > Model](https://claude.ai/admin-settings/models)**[s](https://claude.ai/admin-settings/models).

2. Under **Model access**, find the model you want to change.

3. Click the effort level dropdown to select the maximum level.

4. Click "Save."

If any custom role has an effort cap higher than the new organization cap for that model, the role's cap is lowered to match. Members see only effort levels at or below the organization cap in their model menu. Available effort levels differ depending on the model, and some models don't support effort level settings at all. For an explanation of each level, see **[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678)**.

---

## Set model access for a custom role

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit, or click “Add role” to create one.

3. Select the "Models" tab.

4. Under **Model access**, switch each model on or off. Models disabled at the organization level appear but can’t be enabled until you turn them on for the organization.

5. Click “Save.”

Only models the role grants access to can be selected as that role’s default model.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693923/880665a87dbd4776cf19d6063a37/29d30c6d-f9fc-408c-8c72-4320c6d88d14?expires=1788534000&amp;signature=300ff103f79b816ac93dbf243186d1309d9262128c8f50be08a75dc8622cbec4&amp;req=diUmEs93nohdWvMW1HO4zYj9Sf0G7oW9XsqpNqvyFRKypaCZufwcU0Qn6YF6%0AENeiW5KK6klFVfdtHX8%3D%0A)

---

## Limit the maximum effort level for a custom role

Effort limits determine how much computation members on a role can apply per response on each model. Higher effort levels produce more thorough responses but consume more usage. Effort limits can only be set per role, not at the organization level.

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit.

3. Select the "Models" tab.

4. Next to a model, click the gear icon and choose a level.

5. Click "Save" to save your changes.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2514693927/7a25673b3b075d72adb3cdc371e3/d2d7cd8d-a713-4e91-a706-f589ac46a9fe?expires=1788534000&amp;signature=06e12c06cc64c5d6aafc7b132a659af621ecc9873de1de698395a79842a32e8b&amp;req=diUmEs93nohdXvMW1HO4ze1xBju5cL0ZDeA1RkowXUHFR2X2w03fAOqgYeNi%0AAPecAoU%2BKiULrOB4JTw%3D%0A)

Members on the role see only effort levels at or below the cap in their model menu. Note that available effort levels differ depending on the model, and some models don’t support effort level settings at all. For an explanation of each level, see **[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678)**.

---

## How access combines across multiple roles

If a member belongs to multiple groups with different custom roles, model settings combine like other role permissions:

- **Model access is additive.** The member can use every model granted by any of their roles, as long as it’s enabled at the organization level.

- **Effort limits take the highest cap.** For each model, the member gets the highest maximum effort level any of their roles allows, never exceeding the organization's cap for that model.

For how default models are chosen across multiple roles, see **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

For details on creating roles and assigning them to groups, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

---

## What users see

In every covered product, the model picker shows only the models the member has access to. Effort levels above the organization's cap, or above a role's cap, don't appear in the effort menu.

Model availability also depends on the product. Each product supports a different set of models, so an enabled model appears only in the products that support it.

If you disable a model a member is using in an open conversation or session, that conversation falls back to the member's default model the next time they open it. If the member sends a message while you're making the change, they'll see an error that the model isn't available and be prompted to switch. If you lower a model's effort cap while a member has a higher level selected, their next message on that model uses the new maximum.

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
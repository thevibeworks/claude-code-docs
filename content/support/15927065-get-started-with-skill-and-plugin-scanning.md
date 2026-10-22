# Get started with skill and plugin scanning

Skill and plugin scanning automatically checks third-party skills and plugins for malicious content when someone uploads or edits them, before they can run in your organization. This article explains what scanning checks for, how to turn it on, and what the results mean.

Skill and plugin scanning is available on Enterprise plans in Claude, Claude Cowork, and Enterprise plugin marketplaces.

## What skill and plugin scanning does

Skills and plugins can come from outside your organization, and a file that looks helpful could be built to quietly misuse the access it's given. Skill and plugin scanning adds a security check at the moment a third-party skill or plugin is uploaded or edited. Claude reviews the contents, looks for signs of malicious behavior, and returns one of three results: pass, warn, or fail.

Scanning runs in the background, and most scans finish in about one to two minutes. Results are cached, so uploading the same skill again returns a result almost instantly.

## What gets scanned

Scanning applies to third-party skills and plugins that a member or owner uploads. This includes standalone skills, plugins, and the skills bundled inside a plugin. Hooks are scanned when they're shipped as part of a plugin.

Scanning doesn't apply to:

- Skills and plugins that were already in your organization before scanning was turned on. Existing skills and plugins keep working, so nothing you already use stops working when you enable scanning.

- Skills you create with Claude, which rely on Claude's built-in safeguards.

- Skills shared through a connected MCP server. These follow the same trust model as other MCP tools and aren't covered by scanning.

- MCP servers, which aren't scanned at this time.

- Organizations using customer-managed encryption keys (CMEK), zero data retention (ZDR), or HIPAA configurations. These organizations install skills and plugins the same way they do today, without the added scan.

## Turn on skill and plugin scanning

Skill and plugin scanning is on by default for Enterprise organizations that hadn't chosen a setting before October 2, 2026. If it's off for your organization, Owners and Primary Owners can turn it on in their settings:

1. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and select the “Policy” tab.

2. Turn on **Skill and plugin security scanning**.

Once it's on, every new skill and plugin upload or edit in your organization is scanned automatically, at no extra cost.

## Control which roles scanning applies to

Turning on skill and plugin scanning in organization settings applies it across your whole organization. If you use custom roles, you can further define who scanning applies to. When you create or edit a custom role, turn on the **Skill and plugin security scanning** capability for roles that should have access to skill scanning. Learn more about **[managing custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

## What you'll see after an upload

Admins can also see each item's scan result in the “Inventory” and “Requests” tabs in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**.

### Pass

If nothing concerning is found, the skill or plugin installs normally, with no extra message.

### Warn

A warn result means Claude couldn't fully verify the skill or plugin, and it may carry risk depending on where it came from. It stays usable behind a caution banner that you acknowledge before continuing. Review it carefully, and only use it if you trust the source.

### Fail

A fail result means the scan detected malicious content. The skill or plugin is blocked and can't be used unless someone with the right permission in your organization allows it. The banner explains the specific reason it was flagged. Learn more about **[what to do if your skill or plugin is blocked](#h_03c1d22133)**.

## If your skill or plugin is blocked or has a warning

A blocked skill can't be overridden by the person who uploaded it, unless they're an Owner, Primary Owner, or have a role with **Libraries** permission that's set to "Can manage." If you have that permission, you can select "Allow anyway" on a skill or plugin that scanning blocked or warned about, where the option is shown. You'll find this option in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** or the **[Customize](https://claude.ai/customize/skills)** tab. Select "Revoke" to undo this later.

Selecting "Allow anyway" applies only to that version, and each new version is scanned again. Allowing a version removes the scan's banner for everyone with access to it, whether it was blocked or had a warning. Only allow a version if you've reviewed it and trust the source.

**Note:** "Allow anyway" is rolling out to organizations gradually, so you may not see it yet.

If you think a skill was blocked by mistake, edit and upload it again. Uploading the same skill again without changes returns the same result, so any fix needs to address what was flagged.

## How your content is handled

When a skill or plugin is scanned, its contents are processed in a secure, isolated environment that's kept separate from your normal Claude sessions. The scanned copy is deleted after the scan finishes, and only the result and basic metadata are kept.

**Note:** Scanning runs outside your normal Claude session, so it doesn't change how Claude responds to you.

## What scanning doesn't cover

Skill scanning looks for one kind of risk: third-party skills and plugins that are built to misuse the access they're given, such as quietly moving your data somewhere it shouldn't go. A pass result means the scan didn't find that kind of threat. It isn't a guarantee that a skill is safe in every respect, and it won't catch a skill that behaves in ways you didn't intend without being malicious.

Because of that, choose what you add carefully, and install skills and plugins only from sources you trust.
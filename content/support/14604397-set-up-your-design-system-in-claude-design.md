# Set up your design system in Claude Design

A design system captures your colors, typography, components, and layout patterns, so Claude applies them to every new design and deck. Claude extracts them from the assets you provide, like codebases, slide decks, or other design references.

Design systems are available in beta on Pro, Max, Team, and Enterprise plans. They're on by default on Pro, Max, and Team plans. On Enterprise plans, they're off until an owner turns on **Design systems** in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. Standalone Claude Design at claude.ai/design has its own separate setting.

This guide is for the designer or brand owner who will set up the design system. On Team and Enterprise plans, you only need to do this once, and everyone's work picks it up after that.

## Before you start

- On Team and Enterprise plans, **Design systems** needs to be on for your organization, and an owner may limit who can publish or set the default.

- You’ll need at least one of the following as source material:

  - A codebase with your design system or component library

  - A slide deck or document that reflects your visual identity

  - Brand guideline assets (logos, color palettes, typography specs)

---

## Create a design system

### From a chat

Ask Claude to build a design system from your connected apps, uploaded files, Figma files, decks, logos, and fonts. This works best for brand design systems with fonts, colors, and guidelines.

### From Claude Code

If your design system already exists as React components, run /design-sync in Claude Code. It reads your tokens and components directly, and works best for product design systems in code.

### Bring over a design system from claude.ai/design

1. Open the "Design" tab at the bottom of the sidebar.

2. Click "Migrate team design systems" in the banner.

Each design system becomes an artifact Claude can use in any chat, including in Claude Code. Migrated design systems may need some cleanup, so each one shows a banner where you can click "Let Claude clean it up," and Claude tidies its guide, tokens, and components.

## Manage your design systems

Manage your design systems in **[Settings > Design systems](https://claude.ai/settings/design-systems)**. On Enterprise plans, admins can reserve publishing, setting the organization default, and deleting design systems for specific users. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.

---

## Set up a design system at claude.ai/design

These steps use standalone Claude Design.

### Create or switch to your organization

1. Open **[Claude Design](https://claude.ai/design)**.

2. In the lower left corner of the project picker, click the current organization name.

3. Select your organization, or create a new one.

4. Complete the onboarding flow you're redirected to.

### Upload your brand and product assets

During onboarding, or afterward from your organization settings, upload the assets that define your brand and product. Claude analyzes them and extracts a reusable design system.

- **Codebases:** If your design system lives in code, like a React component library, link or upload the repository. Claude reads the components and styles.

- **Prototypes:** Screenshots, web flows, and existing design files.

- **Slide decks or documents:** Even a well-designed PowerPoint or PDF that reflects your brand can work. Claude extracts colors, layout patterns, and typographic choices.

- **Individual assets:** Logos, color palette files, typography specimens.

You only need one source to get started, but more sources give Claude more to work with.

### Review the generated design system

After uploading, Claude generates a design system for your organization. This typically includes:

- **Color palette:** Primary, secondary, and accent colors extracted from your assets.

- **Typography:** Font families, sizes, and weights.

- **Components:** Buttons, cards, navigation elements, and other reusable UI patterns.

- **Layout patterns:** Spacing, grid systems, and page structures.

To validate it, create a test project and check whether the output matches your brand. Try prompts like:

- "Create a landing page for [your product]."

- "Design a dashboard showing [relevant metrics]."

- "Make a one-pager about [a topic your team commonly presents on]."

### Make it available to your team

When you're happy with the design system, turn on the "Published" toggle. After publishing, projects created from the Claude Design home screen in your organization use your design system instead of the default.

## Update your design system

When your design system changes, you can update it within Claude Design. From your Claude Design organization settings, click the “Open” button next to the design system you want to edit. Click the “Remix” button in the upper right corner to open the chat interface on the left side of the window. From here, you can work with Claude to change your design system.

---

## Tips for best results

- **Include real examples, not just specs.** A finished landing page or marketing site tells Claude more about your brand’s feel than a color palette alone.

- **Iterate.** If the first extraction doesn’t capture your brand well, try uploading additional or different assets.
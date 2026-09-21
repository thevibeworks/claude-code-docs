# Set up your design system in Claude Design

Creating a design system allows Claude Design to produce outputs that fit your specifications. It extracts reusable components, colors, typography, and patterns from the assets you provide—codebases, slide decks, or other design references—and uses them as the foundation for every project created within your account.

Claude Design is available in beta on Pro, Max, Team, and Enterprise plans. It isn't available on the Free plan. It's on by default on Pro and Max plans, and you can turn it off in Settings > Capabilities. It's also on by default on Team plans. On Enterprise plans, it's off by default until an owner turns it on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. The standalone Claude Design experience at claude.ai/design keeps working and has its own separate setting.

This guide is for the designer or brand owner who will set up the design system. You only need to do this once; after setup, all team members’ projects automatically use it (for Team and Enterprise plans).

**Note:** When you use Claude Design outside claude.ai/design, you manage design systems in **[Settings > Design systems](https://claude.ai/settings/design-systems)**. To bring over an existing design system, click "Migrate team design systems" in the banner on the **Design** tab. Migrated design systems may need some cleanup, so each one shows a banner where you can click "Let Claude clean it up," and Claude tidies its guide, tokens, and components. The steps below use standalone Claude Design at claude.ai/design.

## Prerequisites

- Permissions granted by your organization admin for design system setup.

- At least one of the following as source material:

  - A codebase with your design system or component library

  - A slide deck or document that reflects your visual identity

  - Brand guideline assets (logos, color palettes, typography specs)

---

## Step 1: Create or switch to your organization

To set up your organization’s design system:

1. Open **[Claude Design](https://claude.ai/design)**.

2. In the lower-left corner of the project picker, click the current organization name.

3. Select your organization, or create a new one.

4. You’ll be redirected to the onboarding flow. Complete it.

## Step 2: Upload your brand and product assets

During onboarding (or afterward from your organization settings), upload the assets that define your brand and product. Claude will analyze them and extract a reusable design system.

**What to upload:**

- **Codebases:** If your design system lives in code (for example, a React component library), you can link or upload the repository. Claude will read the components and styles.

- **Prototypes:** Screenshots, web flows, and existing design files.

- **Slide decks or documents:** Even a well-designed PowerPoint or PDF that reflects your brand can work. Claude extracts colors, layout patterns, and typographic choices.

- **Individual assets:** Logos, color palette files, typography specimens.

You only need one source to get started, but providing multiple gives Claude more to work with.

## Step 3: Review the generated design system

After uploading, Claude generates a design system (UI kit) for your organization. This typically includes:

- **Color palette:** Primary, secondary, and accent colors extracted from your assets.

- **Typography:** Font families, sizes, and weights.

- **Components:** Buttons, cards, navigation elements, and other reusable UI patterns.

- **Layout patterns:** Spacing, grid systems, and page structures.

To validate your design system, create a test project and see if the output matches your brand expectations. Try prompts like:

- “Create a landing page for [your product].”

- “Design a dashboard showing [relevant metrics].”

- “Make a one-pager about [a topic your team commonly presents on].”

## Step 4: Make it available to your team

Once you’re satisfied with the design system quality, make sure the “Published” toggle is switched on. After publishing, any projects created from the Claude Design homescreen while in your organization will use your design system instead of the default.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2287527007/b1c46cb8dba4cd7e8bbea85fb0c3/2819c6cf-9ce1-4df5-84c8-feae0164bf2e?expires=1789970400&amp;signature=5b36b6f54796cb57a7786e1b67644f3d0e99d36ed63903ef3326df68d1767a21&amp;req=diIvEcx8moFfXvMW1HO4zWNHF%2FuCCTsTIQKNMXlu0T%2BCXyd%2B1KrQ2dqSzVqp%0ARA4Cf3id2iZquAV0260%3D%0A)

## Other ways to create a design system

- **From Claude Code:** If your design system already exists as React components, run /design-sync in Claude Code. It reads your tokens and components directly, and works best for product design systems in code.

- **From a conversation:** Ask Claude to build a design system from your connected apps, uploaded files, Figma files, decks, logos, and fonts. This works best for brand design systems with fonts, colors, and guidelines.

---

## Tips for best results

- **Include real examples, not just specs.** A finished landing page or marketing site tells Claude more about your brand’s feel than a color palette alone.

- **Iterate.** If the first extraction doesn’t capture your brand well, try uploading additional or different assets.

## Update your design system

Brands evolve. When your design system changes, you can update it within Claude Design. From your Claude Design organization settings, click the “Open” button next to the design system you want to edit. Click the “Remix” button in the upper right corner to open the chat interface on the left side of the window. From here, you can work with Claude to change your design system.
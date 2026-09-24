# Claude Design admin guide for Team and Enterprise plans

Claude Design lets your team create on-brand designs, prototypes, and interactive microsites through conversation with Claude. Presentations now have their own tool, Claude Slides.

Claude Design is available in beta on Pro, Max, Team, and Enterprise plans. It's on by default on Team plans. On Enterprise plans, it's off by default until an owner turns it on.

**Note:** Settings for artifacts, templates (including **Design**), design systems, and sharing live in one place now. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**. This guide covers standalone Claude Design at **claude.ai/design** and how to roll out Claude Design with a design system in place.

Claude Design works best when a **design system** is set up for your organization first. This ensures every project your team creates stays true to your brand, typography, color palette, and component patterns. This guide walks you through enabling Claude Design, setting up the right foundation, and rolling it out to your team.

**[Create an artifact with Claude](https://claude.ai/artifacts)**

---

## Turn on Claude Design for your organization

Your team can use Claude Design in two places, and each has its own setting. Turning one on doesn't turn on the other.

### Claude Design in conversations and the Artifacts tab

To turn on the **Design** template, see the instructions in **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.

### Standalone Claude Design at claude.ai/design

1. Go to **[Organization settings > Claude Design](https://claude.ai/admin-settings/claude-design)**.

2. Find the **Enable for your organization** toggle under **Claude Design [standalone]** and switch it on.

On Enterprise plans, you can control access to standalone Claude Design with **[custom roles](https://support.claude.com/en/articles/13930452)**.

Before you turn on broad access, read through the rollout approach below. Turning on Claude Design without a design system in place means your team gets functional but generic output.

---

## The design system: why it comes first

The single most important thing you can do before rolling out Claude Design is have an experienced designer set up your organization’s design system. Once in place, every project your team creates automatically reflects your brand.

This means your rollout has a natural sequence: design system setup first, then broader access.

### Who should set up the design system

For best results, we recommend pulling in designers across both brand and product design. Together they can ensure the design system covers both brand identity and product UI patterns.

### What they’ll do

1. Create your organization in Claude Design (see **[Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)**).

2. Complete the onboarding flow.

3. Upload brand assets (codebases, slide decks, or other design references).

4. Validate that Claude generates designs consistent with your brand.

Any member with Claude Design access can create and edit design systems. On the Enterprise plan, you can restrict who can publish design systems, set the organization default, and delete design systems.

---

## Recommended rollout phases

A phased rollout lets you validate your design system and build internal expertise before broad adoption. On Enterprise plans, you can phase access to standalone Claude Design using **[custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**. You can phase access to Claude Design in conversations and the Artifacts tab the same way, with the Design capability (under **Artifacts**).

### Phase 1: Design system setup

- **Who:** 2–4 trusted designers and design leads across brand and product design.

- **Goal:** Create and validate your organization’s design system, including product templates everyone can use as a starting point.

- **Checkpoint:** Review generated output for brand consistency before proceeding.

### Phase 2: Design team onboarding

- **Who:** Full design team.

- **Goal:** Build familiarity with Claude Design; stress-test the design system across real projects.

- **Checkpoint:** Gather feedback on design quality and refine the design system if needed.

### Phase 3: Product and UX onboarding

- **Who:** Product managers, UX researchers, and adjacent functions.

- **Goal:** Enable faster prototyping and design collaboration beyond the design team.

- **Checkpoint:** Observe usage throughout the organization and gather feedback on usability.

### Phase 4: Broader organization

- **Who:** Entire organization or specific departments.

- **Goal:** Make design creation available widely while maintaining brand consistency.

- **Checkpoint:** Observe usage throughout the organization and gather feedback on usability.

### Rollout tips

- Announce each phase clearly so people know when their turn is coming.

- Consider running a short training session or office hours during early phases.

- Establish a feedback channel for design system improvements.

- Share examples of creative uses of Claude Design internally to help foster creativity.

---

## What your team can do with Claude Design

Once set up, your team can use Claude Design to:

- **Create prototypes and mockups:** Describe a UI and get a working interactive prototype.

- **Build presentations with Claude Slides:** Make on-brand decks from notes, reports, or an existing conversation, and export them to PowerPoint or PDF. Claude Slides has its own setting in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

- **Design microsites and landing pages:** Create polished single-page sites.

- **Iterate with inline comments:** Annotate designs directly on the canvas and ask Claude to implement changes.

- **Hand off to engineering:** Export design intent for use with Claude Code or your existing development workflow.

---

## Preview sandbox isolation

Claude Design project previews run inside a sandboxed iframe on a separate content domain that Anthropic operates. These sandboxed iframes help each project preview stay in its own space, separate from others. The code in a preview can't reach your Claude account, your login, or the editor.
​
Access to a preview is controlled by signed tokens—short-lived passes that prove someone's allowed in. Claude re-checks these tokens against your sharing permissions every time someone opens the preview, so when you remove someone's access, they're locked out right away.

---

## Frequently asked questions

### Do all team members need to upload brand assets?

No. Once a designer sets up your organization’s design system, all projects created within that organization automatically use it. Team members just start creating.

### Can we have multiple design systems for different brands or sub-teams?

Yes. Organizations can have multiple design systems.

### What happens if someone starts using Claude Design before the design system is set up?

They’ll get functional designs, but the designs won’t reflect your brand. We strongly recommend completing design system setup first for the best team experience.

### How many users can we onboard at once?

There are no strict limits, but we recommend the phased approach outlined above to ensure quality and successful adoption across your organization.

### Can we export or archive generated designs?

Claude Design currently supports export to HTML bundles, PPTX, and PDF, hand-off to Claude Code, and sending designs to the partner tools listed in **[Get started with Claude Design](https://support.claude.com/en/articles/14604416)**.
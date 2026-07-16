# Get started with Claude Design

**[Claude Design](http://claude.ai/design)** lets you create designs, interactive prototypes, presentations, and more by having a conversation with Claude. This guide walks you through creating your first project, iterating on designs, and getting the most out of the tool.

Claude Design is now available in beta to Pro, Max, Team, and Enterprise plans. This capability is default off for Enterprise plans. You can use it on the web at claude.ai/design or from the sidebar in Claude Desktop.

This guide assumes your organization’s design system has already been set up, so everything you create will automatically use your brand’s colors, typography, and component patterns. If you’re a design lead who needs to set up or modify the design system itself, see **[Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)**.

---

## How Claude Design works

Claude Design has two main areas: a chat interface on the left and a canvas on the right. You describe what you want in the chat, and Claude generates a working design on the canvas. From there, you iterate—refining through conversation, inline comments, and directly on the canvas until it’s right.

The typical flow is:

1. Create a project.

2. Attach or import the design system you want Claude to build with.

3. Add any relevant context (screenshots, a codebase).

4. Describe what you want to build.

5. Review what Claude generates on the canvas.

6. Refine through chat, edit directly on the canvas, or leave inline comments.

7. Export or share when you’re happy with the result.

### Move between Claude Design and Claude Code

You can move between working in Claude Design and Claude Code while keeping your work synced. Use `/design-sync` to pull in your design system, so everything you build in Claude Design starts from your existing components. When a design is ready to become software, you can hand it off to Claude Code, which continues from your existing work instead of starting over from a screenshot.

If you prefer to work from Claude Code, connect the Claude Design MCP server to create and edit designs without leaving your terminal:

1. Add the server:
`claude mcp add --scope user --transport http claude-design https://api.anthropic.com/v1/design/mcp`

2. Run `/design-login` to sign in.

Once you're connected, you can import a design into your codebase, export your code as a live prototype, or let Claude build the whole thing from start to finish.

---

## Create a new project

When you create a project, it automatically inherits your organization’s design system. You don’t need to upload brand assets or configure anything—your brand colors, fonts, and components are already in place.

### Attach or import your design system

Bring in one or several design systems from a GitHub repo, design files, raw uploads, or your local codebase using the `/design-sync` command in Claude Code. Claude builds with your real design system components, checks its own output against your design system, and makes corrections before you see them.

For larger teams, the Claude Design Admin custom role lets an admin approve a standard system and lock down edits, so the work always matches your company guidelines.

### Add context to your project

The more context you give Claude, the better your output will be. You can attach reference material at any point during a project.

- **Screenshots, images, or existing assets:** Upload screenshots of existing designs, competitor products, wireframes, or visual inspiration. You can also attach an existing slide deck or document with a design style you want to replicate. Useful for “make it look like this” requests.

- **Codebases and existing design files:** Link a code repository so Claude understands your existing components, architecture, and styling patterns. This makes prototypes more production-ready from the start. Import also supports multiple ways to upload existing product design work.

### Write effective prompts

You don’t need to be a designer to get great results. Be specific about what you’re building, who it’s for, and what matters most.

A good prompt includes the **goal** (what you’re building), the **layout** (how things should be arranged), the **content** (what information to display), and the **audience** (who will use it). Claude will also ask clarifying questions if it needs more information.

Here are some examples of prompts that work well:

- “Create a dashboard showing monthly revenue with filters for region and product line.”

- “Design a mobile app onboarding flow with 4 screens that walks users through our core features.”

- “Build a landing page for our new API product with a hero section, code examples, and pricing.”

- “Create a form for collecting customer feedback with conditional questions based on category.”

- “Design an internal tool for our ops team to review and approve content submissions.”

---

## Refine your design

The first generation is a starting point. The real value comes from iterating.

### Using chat

Chat is best for broad changes that affect the overall design:

- “Make the color scheme darker and more minimal.”

- “Rearrange the dashboard so metrics are in the top row and the chart is below.”

- “Add a settings panel on the right side.”

- “Show me 2–3 alternative layouts for this page.”

You can also ask Claude to explain its design decisions, suggest improvements, or review the design for accessibility.

### Using inline comments

Inline comments let you click directly on a specific part of the canvas and request a targeted change. This is faster than describing the location in chat.

Examples of good inline comments:

- “Make this button padding larger.”

- “Change this to a dropdown instead of radio buttons.”

- “Use the primary brand color here.”

- “Make this section collapsible.”

**Note:** If your comments aren’t being picked up, paste the feedback directly into the chat instead. This is a known workaround for an intermittent issue where comments can disappear before Claude reads them.

### Edit directly on the canvas

Use rich layout controls for quick visual and aesthetic shifts, specifically to drag, resize, and align elements directly.

### When to use chat vs. comments vs. edit directly

Use **comments** for targeted, component-level changes (“fix this button,” “adjust this spacing”). Use **chat** for structural changes, new sections, or anything that requires explanation or context. **Edit directly** for quick visual and aesthetic changes.

## Manage versions and revisions

If you want to explore a different direction without losing your current work, tell Claude: “Save what we have and try a completely different approach.” Claude will save your current project and confirm where it’s saved, so you can reference earlier iterations in the conversation easily.

---

## Export and share

Once your design is ready, you can share it with colleagues or export it for use elsewhere. The right format depends on your use case—whether you’re getting stakeholder feedback, handing off to engineering, or presenting to a group.

Use the “Export” button in the upper right corner when viewing your project to choose from the following export formats.

- Download as .zip

- Export as PDF

- Export as PPTX

- Send to Canva

- Export as standalone HTML

- Send to the tools you already use, including Adobe, Base44, Canva, Gamma, Lovable, Miro, Replit, Vercel, and Wix, with more destinations coming soon.

- Handoff to Claude Code

  - Send to local coding agent

  - Send to Claude Code Web

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2287510952/553a03eec5cea7b9eff53b473552/6dc33363-38b1-444e-96bb-f8218b588173?expires=1784223000&amp;signature=694669d278d2715bb3912f591d15960892d1bd4b82935c60cc0ce8cfa8c087fb&amp;req=diIvEcx%2FnYhaW%2FMW1HO4zQFD4ShYmW50nfz9ljnuyXSLkyCHr0rIZm1mKsaE%0AEY8j71aTX8JCyhTVXQc%3D%0A)

You can also share projects within your organization using a shareable link. Sharing options include view-only, comment, and edit access.

---

## Usage and pricing

Claude Design counts toward the same usage limits as the rest of Claude. Design activity draws from the shared pool you use for chat, Claude Code, and Cowork, so there's no separate Claude Design allowance to track. Complex projects with large codebases or many iterations consume more usage.

If you reach your usage limits, Claude Design is unavailable until your limits reset. If you've enabled usage credits, you can keep working after reaching your included limits. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**.

**Note:** Claude Design previously had its own weekly allowance, separate from your other usage limits. All Claude Design activity now counts toward your plan's shared limits.

---

## Tips for best results

- **Import a complete design system.** Import a complete design system that includes your styles, fonts, and components.

- **Start simple, then layer in complexity.** Begin with the core layout and content, then add interactions, edge cases, and polish. Claude responds well to incremental requests.

- **Be specific in your feedback.** “This doesn’t look right” is hard to act on. “Tighten the spacing between form fields to 8px” gives Claude exactly what it needs.

- **Reference your design system.** If you know a component exists in your brand’s system, mention it by name: “Use the Primary Button component” or “Apply the Card layout pattern.”

- **Think about responsiveness early.** Mention whether your design needs to work on mobile, tablet, and desktop, or just one of those.

- **Ask for variations.** If you’re unsure about a direction, ask Claude to show you 2–3 options. Comparing alternatives is much faster than guessing.

- **Ask Claude for feedback.** Claude can review your design for accessibility, contrast ratios, information hierarchy, and general usability. Treat it as a design collaborator, not just a generator.

---

## Known limitations

Claude Design is now available in beta. A few things to be aware of:

- **Comment persistence:** Inline comments occasionally don't appear on the page, but you can still see them by opening the comments view.

- **Large codebases:** Consider  linking very large repositories from Claude Code to avoid lag or browser issues. To sync a design system, use `/design-sync` from Claude Code.

- **Chat errors:** If you hit a "chat upstream error," try starting a new chat tab within the same project.

- **Availability:** Claude Design is available on web and desktop only.

- **Multi-person editing:** Two or more people editing a design project at the same time is still basic and may not work reliably.

- **Design system import:** Design system import is only as good as its source. A messy codebase or an incomplete file will show up in the output.
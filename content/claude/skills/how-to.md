> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create custom skills

> Create a custom skill for Claude: write the SKILL.md file, add resources and scripts, package the skill, and test it.

export const Piece = ({id, children}) => <div className="pe-piece" data-piece={id}>{children}</div>;

export const PluginExplorer = ({children, variant}) => {
  const SKILL_PIECES = [{
    id: 'skillmd',
    required: 'Required',
    name: 'SKILL.md',
    path: 'brand-guidelines/SKILL.md',
    lines: [{
      depth: 0,
      kind: 'file',
      text: 'SKILL.md'
    }],
    href: '/skills/how-to#create-a-skillmd-file',
    linkText: 'Go to Create a SKILL.md file'
  }, {
    id: 'references',
    name: 'Reference file',
    path: 'brand-guidelines/references/voice-and-tone.md',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: 'references/'
    }, {
      depth: 1,
      kind: 'file',
      text: 'voice-and-tone.md'
    }],
    href: '/skills/how-to#add-resources',
    linkText: 'Go to Add resources'
  }, {
    id: 'assets',
    name: 'Asset',
    path: 'brand-guidelines/assets/slide-template.md',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: 'assets/'
    }, {
      depth: 1,
      kind: 'file',
      text: 'slide-template.md'
    }],
    href: '/skills/how-to#add-resources',
    linkText: 'Go to Add resources'
  }, {
    id: 'scripts',
    name: 'Script',
    path: 'brand-guidelines/scripts/check_contrast.py',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: 'scripts/'
    }, {
      depth: 1,
      kind: 'file',
      text: 'check_contrast.py'
    }],
    href: '/skills/how-to#add-scripts',
    linkText: 'Go to Add scripts'
  }];
  const PLUGIN_PIECES = [{
    id: 'manifest',
    required: 'Required',
    name: 'Manifest',
    path: '.claude-plugin/plugin.json',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: '.claude-plugin/'
    }, {
      depth: 1,
      kind: 'file',
      text: 'plugin.json'
    }],
    href: '/plugins/build#write-the-manifest',
    linkText: 'Go to Write the manifest'
  }, {
    id: 'skills',
    name: 'Skill',
    path: 'skills/file-expense/SKILL.md',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: 'skills/'
    }, {
      depth: 1,
      kind: 'folder',
      text: 'file-expense/'
    }, {
      depth: 2,
      kind: 'file',
      text: 'SKILL.md'
    }],
    href: '/skills/how-to',
    linkText: 'Go to Create custom skills'
  }, {
    id: 'references',
    name: 'Skill reference file',
    path: 'skills/file-expense/references/categories.md',
    lines: [{
      depth: 2,
      kind: 'folder',
      text: 'references/'
    }, {
      depth: 3,
      kind: 'file',
      text: 'categories.md'
    }],
    href: '/skills/how-to#add-resources',
    linkText: 'Go to Add resources'
  }, {
    id: 'scripts',
    name: 'Skill script',
    path: 'skills/file-expense/scripts/total.py',
    lines: [{
      depth: 2,
      kind: 'folder',
      text: 'scripts/'
    }, {
      depth: 3,
      kind: 'file',
      text: 'total.py'
    }],
    href: '/skills/how-to#add-scripts',
    linkText: 'Go to Add scripts'
  }, {
    id: 'commands',
    name: 'Command',
    path: 'commands/summarize.md',
    lines: [{
      depth: 0,
      kind: 'folder',
      text: 'commands/'
    }, {
      depth: 1,
      kind: 'file',
      text: 'summarize.md'
    }],
    href: '/plugins/platform-support#compare-component-support-by-app',
    linkText: 'Go to component support by app'
  }, {
    id: 'mcp',
    name: 'MCP connector',
    path: '.mcp.json',
    lines: [{
      depth: 0,
      kind: 'file',
      text: '.mcp.json'
    }],
    href: '/plugins/build#bundle-an-mcp-connector-with-its-skill',
    linkText: 'Go to Bundle an MCP connector with its skill'
  }, {
    id: 'readme',
    required: 'Required to publish',
    name: 'README',
    path: 'README.md',
    lines: [{
      depth: 0,
      kind: 'file',
      text: 'README.md'
    }],
    href: '/plugins/pre-submission-checklist#readme-and-license',
    linkText: 'Go to README and license checks'
  }, {
    id: 'license',
    required: 'Required to publish',
    name: 'License',
    path: 'LICENSE',
    lines: [{
      depth: 0,
      kind: 'file',
      text: 'LICENSE'
    }],
    href: '/plugins/pre-submission-checklist#readme-and-license',
    linkText: 'Go to README and license checks'
  }];
  const isSkill = variant === 'skill';
  const PIECES = isSkill ? SKILL_PIECES : PLUGIN_PIECES;
  const rootLabel = isSkill ? 'brand-guidelines/' : 'expense-reports/';
  const title = isSkill ? 'What goes in the skill folder' : 'What goes in the plugin folder';
  const treeCaption = isSkill ? 'Skill folder' : 'Plugin folder';
  const [selectedId, setSelectedId] = useState(isSkill ? 'skillmd' : 'manifest');
  const [isFullscreen, setIsFullscreen] = useState(false);
  const rootRef = useRef(null);
  useEffect(() => {
    const onFsChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', onFsChange);
    return () => document.removeEventListener('fullscreenchange', onFsChange);
  }, []);
  const toggleFullscreen = () => {
    if (!rootRef.current) return;
    if (document.fullscreenElement) document.exitFullscreen(); else rootRef.current.requestFullscreen().catch(() => {});
  };
  const selected = PIECES.find(p => p.id === selectedId) || PIECES[0];
  const onTreeKeyDown = e => {
    const keys = ['ArrowDown', 'ArrowUp', 'Home', 'End'];
    if (keys.indexOf(e.key) === -1) return;
    const i = PIECES.findIndex(p => p.id === selectedId);
    let next = i;
    if (e.key === 'ArrowDown') next = Math.min(PIECES.length - 1, i + 1);
    if (e.key === 'ArrowUp') next = Math.max(0, i - 1);
    if (e.key === 'Home') next = 0;
    if (e.key === 'End') next = PIECES.length - 1;
    e.preventDefault();
    if (next === i) return;
    const id = PIECES[next].id;
    setSelectedId(id);
    const el = document.getElementById('pe-node-' + id);
    if (el) el.focus();
  };
  const FolderIcon = () => <svg className="pe-icon" width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.3" strokeLinejoin="round" aria-hidden="true">
      <path d="M1.5 4.5a1 1 0 0 1 1-1h3.2l1.3 1.5h6a1 1 0 0 1 1 1V12a1 1 0 0 1-1 1h-10.5a1 1 0 0 1-1-1z" />
    </svg>;
  const FileIcon = () => <svg className="pe-icon" width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.3" strokeLinejoin="round" aria-hidden="true">
      <path d="M4 1.5h5.5L13 5v9.5H4z" />
      <path d="M9.5 1.5V5H13" />
    </svg>;
  return <div ref={rootRef} className={isFullscreen ? 'pe-root pe-fullscreen not-prose' : 'pe-root not-prose'} data-selected={selected.id}>
      <style>{`
        .pe-root {
          --pe-mono: var(--font-mono, ui-monospace, SFMono-Regular, Menlo, monospace);
          --pe-accent: #D97757;
          --pe-accent-text: #A8502F;
          --pe-accent-bg: rgba(217,119,87,0.10);
          --pe-bg: #FFFFFF;
          --pe-surface: #FAFAF7;
          --pe-hover: #F0EEE6;
          --pe-border: #E8E6DC;
          --pe-text: #141413;
          --pe-text-2: #3D3D3A;
          --pe-text-3: #5E5D59;
          font-family: inherit;
          background: var(--pe-bg);
          color: var(--pe-text);
          border: 1px solid var(--pe-border);
          border-radius: 12px;
          margin: 1.5rem 0;
          overflow: hidden;
          box-sizing: border-box;
        }
        .dark .pe-root {
          --pe-accent-text: #EBA98F;
          --pe-accent-bg: rgba(217,119,87,0.18);
          --pe-bg: #1A1918;
          --pe-surface: #232221;
          --pe-hover: #2E2D2B;
          --pe-border: #3A3936;
          --pe-text: #F1EFE9;
          --pe-text-2: #D6D4CA;
          --pe-text-3: #B8B5AD;
        }
        .pe-root *, .pe-root *::before, .pe-root *::after { box-sizing: border-box; }
        .pe-head { display: flex; align-items: flex-start; gap: 12px; padding: 18px 24px 16px; border-bottom: 1px solid var(--pe-border); }
        .pe-head-text { flex: 1; min-width: 0; }
        .pe-fs-btn { flex-shrink: 0; width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--pe-border); border-radius: 6px; background: var(--pe-surface); color: var(--pe-text-2); font-size: 15px; line-height: 1; cursor: pointer; }
        .pe-fs-btn:hover { background: var(--pe-hover); }
        .pe-fs-btn:focus-visible { outline: 2px solid var(--pe-accent); outline-offset: 2px; }
        .pe-fullscreen { border-radius: 0; height: 100vh; display: flex; flex-direction: column; overflow: auto; }
        .pe-fullscreen .pe-body { flex: 1; }
        .pe-title { font-size: 19px; font-weight: 600; line-height: 1.3; color: var(--pe-text); margin: 0; }
        .pe-sub { font-size: 15px; line-height: 1.5; color: var(--pe-text-3); margin: 4px 0 0; }
        .pe-sub code { font-family: var(--pe-mono); font-size: 0.88em; padding: 1px 5px; border-radius: 4px; background: var(--pe-surface); border: 1px solid var(--pe-border); }
        .pe-body { display: flex; align-items: stretch; }
        .pe-tree-pane { width: 270px; flex-shrink: 0; background: var(--pe-surface); border-right: 1px solid var(--pe-border); padding: 16px 0 12px; }
        .pe-panel { flex: 1; min-width: 0; padding: 16px 24px 24px; }
        .pe-caption { font-size: 13px; font-weight: 600; color: var(--pe-text-3); margin: 0 0 10px; }
        .pe-tree-pane .pe-caption { padding: 0 16px; }
        .pe-rootline { display: flex; align-items: center; gap: 7px; padding: 3px 16px; font-family: var(--pe-mono); font-size: 13.5px; color: var(--pe-text-3); }
        .pe-node {
          display: block; width: 100%; margin: 0; padding: 3px 16px 3px 30px; text-align: left; cursor: pointer;
          background: transparent; color: var(--pe-text-2);
          border: none; border-left: 3px solid transparent;
          font-family: var(--pe-mono); font-size: 13.5px; line-height: 1.4;
        }
        .pe-node:hover { background: var(--pe-hover); }
        .pe-node:focus-visible { outline: 2px solid var(--pe-accent); outline-offset: -2px; }
        .pe-node[aria-pressed="true"] { background: var(--pe-accent-bg); border-left-color: var(--pe-accent); color: var(--pe-accent-text); font-weight: 600; }
        .pe-line { display: flex; align-items: center; gap: 7px; padding: 2px 0; }
        .pe-line span { overflow-wrap: anywhere; }
        .pe-line > span:not(.pe-req) { white-space: nowrap; flex-shrink: 0; }
        .pe-req { flex-shrink: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; margin-left: 8px; padding: 0 6px; border-radius: 999px; font-size: 11px; line-height: 18px; font-family: var(--pe-sans, inherit); letter-spacing: .02em; color: var(--pe-accent-text); border: 1px solid var(--pe-border); background: var(--pe-surface); white-space: nowrap; }
        .pe-piece { display: none; font-size: 16px; line-height: 1.6; color: var(--pe-text-2); }
        ${PIECES.map(p => '.pe-root[data-selected="' + p.id + '"] .pe-piece[data-piece="' + p.id + '"]').join(',\n        ')} { display: block; }
        .pe-piece p { margin: 0 0 10px; }
        .pe-piece p:last-child { margin-bottom: 0; }
        .pe-piece ul { list-style: disc; padding-left: 1.25em; margin: 0 0 10px; }
        .pe-piece li { margin: 2px 0; }
        .pe-piece code { font-family: var(--pe-mono); font-size: 0.88em; padding: 1px 5px; border-radius: 4px; background: var(--pe-surface); border: 1px solid var(--pe-border); }
        .pe-piece .code-block { margin: 12px 0 0; }
        .pe-piece pre code { padding: 0; border: none; background: none; }
        .pe-piece a { color: var(--pe-accent-text); }
        .pe-line-compact { display: none; }
        .pe-icon { flex-shrink: 0; }
        .pe-name { font-size: 22px; font-weight: 600; line-height: 1.25; letter-spacing: -0.2px; color: var(--pe-text); margin: 0; }
        .pe-path { font-family: var(--pe-mono); font-size: 13.5px; color: var(--pe-accent-text); margin: 4px 0 0; overflow-wrap: anywhere; }
        .pe-block { margin: 20px 0 0; }
        .pe-link {
          display: inline-block; margin: 24px 0 0; padding: 8px 14px; border-radius: 8px;
          font-size: 14.5px; font-weight: 600; text-decoration: none;
          color: var(--pe-accent-text); background: var(--pe-accent-bg); border: 1px solid var(--pe-accent);
        }
        .pe-link:hover { filter: brightness(0.97); }
        .pe-link:focus-visible { outline: 2px solid var(--pe-accent); outline-offset: 2px; }
        @media (max-width: 700px) {
          .pe-head { padding: 16px 16px 14px; }
          .pe-body { flex-direction: column; }
          .pe-tree-pane { width: 100%; border-right: none; border-bottom: 1px solid var(--pe-border); }
          .pe-line-tree { display: none; }
          .pe-line-compact { display: flex; }
          .pe-panel { padding: 16px 16px 20px; }
        }
      `}</style>

      <div className="pe-head">
        <div className="pe-head-text">
          <div className="pe-title">{title}</div>
          {isSkill ? <div className="pe-sub">This example skill, <code>brand-guidelines</code>, has one of each kind of file a skill can carry. Select a file to read what it's for and see a minimal example.</div> : <div className="pe-sub">This example plugin, <code>expense-reports</code>, has one of each file that chat, Cowork, and Claude Code all load, plus the README and license the directory requires. Select a file to read what it’s for and see a minimal example.</div>}
        </div>
        <button type="button" className="pe-fs-btn" onClick={toggleFullscreen} aria-label={isFullscreen ? 'Exit fullscreen' : 'Fullscreen'} title={isFullscreen ? 'Exit fullscreen' : 'Fullscreen'}>
          {isFullscreen ? '⤡' : '⛶'}
        </button>
      </div>

      <div className="pe-body">
        <div className="pe-tree-pane">
          <div className="pe-caption" id="pe-tree-caption">{treeCaption}</div>
          <div role="group" aria-labelledby="pe-tree-caption" onKeyDown={onTreeKeyDown}>
            <div className="pe-rootline"><FolderIcon /><span>{rootLabel}</span></div>
            {PIECES.map(p => <button key={p.id} id={'pe-node-' + p.id} type="button" className="pe-node" aria-pressed={p.id === selected.id} aria-label={p.name + ', ' + p.path} onClick={() => setSelectedId(p.id)}>
                {p.lines.map((line, i) => <span key={i} className="pe-line pe-line-tree" style={{
    paddingLeft: line.depth * 18 + 'px'
  }}>
                    {line.kind === 'folder' ? <FolderIcon /> : <FileIcon />}
                    <span>{line.text}</span>
                    {p.required && i === p.lines.length - 1 ? <span className="pe-req" title={p.required}>Required</span> : null}
                  </span>)}
                <span className="pe-line pe-line-compact">
                  <FileIcon />
                  <span>{p.path}</span>
                  {p.required ? <span className="pe-req" title={p.required}>Required</span> : null}
                </span>
              </button>)}
          </div>
        </div>

        <div className="pe-panel" role="region" aria-labelledby="pe-panel-caption" aria-live="polite" aria-atomic="true">
          <div className="pe-caption" id="pe-panel-caption">Selected file</div>
          <div className="pe-name">{selected.name}{selected.required ? <span className="pe-req">{selected.required}</span> : null}</div>
          <div className="pe-path">{selected.path}</div>

          <div className="pe-block">{children}</div>

          <a className="pe-link" href={selected.href}>{selected.linkText}</a>
        </div>
      </div>
    </div>;
};

A custom skill is a folder with a `SKILL.md` file of instructions, and optionally scripts and reference files, that Claude loads when a task matches the skill's description. This guide is for anyone writing a skill of their own. It explains how to create, structure, and test one.

If you already know what the skill should do, start with the [directory structure](#directory-structure). If you're not sure a skill is the right tool, read [Decide what skill to create](#decide-what-skill-to-create) first.

<Note>
  Skills follow the [Agent Skills specification](https://agentskills.io/specification). See the specification for more in-depth information.
</Note>

## Decide what skill to create

A skill pays off when Claude does a task for you repeatedly and you want it done the same way every time. Good candidates are tasks where you find yourself correcting Claude with the same instructions, such as a report format your team uses, a review checklist, a multi-step procedure, or work that needs a reference file or a script to come out right. A skill can also teach Claude how your team uses a tool you've connected, such as which project new issues go in and which labels and template to use in your issue tracker. Write the skill once, and Claude applies it whenever a request matches the skill's description, for you and for anyone you share it with.

A skill isn't the right tool for everything:

* **A one-off task**: describe what you want in the conversation instead
* **Live data from another service**: that's what an [MCP connector](/docs/connectors/getting-started) provides. A skill can tell Claude how to use a connector, but it can't reach the service itself
* **Instructions for every conversation**: put those in your [personal preferences or project instructions](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) rather than a skill, which loads only when a task matches

To start, write down the task in one sentence and what a good result looks like. That sentence becomes the skill's `description`, and the rest becomes the instructions. If you'd rather have Claude draft the skill with you, ask it to use the [skill-creator skill](#measure-whether-the-skill-improves-the-output), then edit what it produces.

## Directory structure

A skill is a folder named after the skill. The only required file is `SKILL.md`; the other folders are optional and hold material that `SKILL.md` points Claude to. Select a file in the explorer to see what goes in it and what Claude does with it.

<PluginExplorer variant="skill">
  <Piece id="skillmd">
    <p>The one required file. Its frontmatter names and describes the skill, and Claude reads the <code>description</code> to decide when the skill applies. The body holds the instructions Claude follows once it does.</p>
    <p>In this example, the skill applies Acme's brand guidelines and tells Claude where the supporting files are:</p>

    ```markdown SKILL.md theme={null}
    ---
    name: brand-guidelines
    description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
    ---
    Use these guidelines whenever you produce a document or deck for Acme.

    1. Use the colors and fonts in the sections below.
    2. For wording, follow `references/voice-and-tone.md`.
    3. For slides, start from `assets/slide-template.md`.
    4. Before you finish, run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_contrast.py` on any color pairs you chose.
    ```
  </Piece>

  <Piece id="references">
    <p>Longer background that Claude reads only when a step calls for it, so it doesn't crowd <code>SKILL.md</code>. Mention the file by path at the step where Claude needs it.</p>
    <p>In this example, the file holds the writing rules the instructions point to in step 2:</p>

    ```markdown references/voice-and-tone.md theme={null}
    # Voice and tone
    - Write in the second person and the present tense.
    - Prefer short sentences. Avoid exclamation marks.
    - Product names are always capitalized: Acme Cloud, Acme Sync.
    ```
  </Piece>

  <Piece id="assets">
    <p>Templates, images, and data files that Claude copies or fills in rather than reads for guidance.</p>
    <p>In this example, the asset is the slide outline that step 3 tells Claude to start from:</p>

    ```markdown assets/slide-template.md theme={null}
    # [Deck title]
    ## Agenda
    ## [Section 1]
    ## [Section 2]
    ## Next steps
    ```
  </Piece>

  <Piece id="scripts">
    <p>Code that Claude runs while following the skill, for work that is more reliable as a program than as instructions. Reference it from `SKILL.md` with `${CLAUDE_SKILL_DIR}` so the path resolves wherever the skill is installed.</p>
    <p>In this example, the script checks that a text and background color pair has enough contrast:</p>

    ```python scripts/check_contrast.py theme={null}
    import sys

    def luminance(hex_color):
        r, g, b = (int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

    fg, bg = sys.argv[1], sys.argv[2]
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    ratio = (l1 + 0.05) / (l2 + 0.05)
    print(f"{ratio:.2f}", "OK" if ratio >= 4.5 else "LOW")
    ```
  </Piece>
</PluginExplorer>

The directory name must match the `name` field in your `SKILL.md`.

## Create a `SKILL.md` file

The `SKILL.md` file must start with YAML frontmatter containing required metadata, followed by markdown instructions.

### Required fields

A `SKILL.md` file starts with YAML frontmatter that names and describes the skill:

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---
```

Both frontmatter fields are required:

| Field         | Type   | Description                                                                                                                                                                                             |
| :------------ | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`        | string | Lowercase letters, numbers, and hyphens only, up to 64 characters. Must match the skill's directory name                                                                                                |
| `description` | string | What the skill does and when to use it. Claude reads this to decide when to load the skill. Up to 1,024 characters, the limit in the [Agent Skills specification](https://agentskills.io/specification) |

### Write the instructions

After the frontmatter, the rest of the file is the instructions Claude follows when the skill loads, written as ordinary text. You can add headings, lists, and bold with Markdown formatting, the lightweight markup many note-taking apps use, but plain paragraphs work too. Useful things to include:

* Step-by-step procedures
* Examples of inputs and outputs
* Templates or formatting requirements
* Edge cases to handle

Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

### Complete example

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---

# Brand Guidelines

Apply these standards when creating presentations, documents, or marketing materials for Acme Corp.

## Brand colors

- Primary: #FF6B35 (Coral)
- Secondary: #004E89 (Navy Blue)
- Accent: #F7B801 (Gold)
- Neutral: #2E2E2E (Charcoal)

## Typography

- Headers: Montserrat Bold
- Body text: Open Sans Regular
- Size guidelines: H1 32pt, H2 24pt, Body 11pt

## Logo usage

Use the full-color logo on light backgrounds, white logo on dark backgrounds. Maintain minimum spacing of 0.5 inches around the logo.

## When to apply

Apply these guidelines when creating:
- PowerPoint presentations
- Word documents for external sharing
- Marketing materials
- Reports for clients

See the [assets/](assets/) folder for logo files and font downloads.
```

## Add resources

Claude reads all of `SKILL.md` every time the skill loads, so anything long that Claude needs only some of the time is better kept in a separate file that `SKILL.md` points to. Claude then opens that file only when a step calls for it, which keeps the skill quick to load and leaves more of the conversation for your actual task. Separate files also let a skill carry things that aren't instructions at all, such as a template to fill in or a table to look values up in. Put them in folders next to `SKILL.md`:

* **`references/`**: Additional documentation Claude can read when needed
* **`assets/`**: Templates, images, lookup tables, schemas
* **`scripts/`**: Executable code, which [Add scripts](#add-scripts) covers

Mention each file in `SKILL.md` at the step where Claude should use it, for example "Fill in `assets/report-template.md`", so Claude knows when to open it. Keep each file focused on one thing.

## Add scripts

A skill can include scripts that Claude runs while following it, in any language available where the skill runs: in Claude Code that's whatever is installed on your machine, and in chat on claude.ai it's what the code-execution environment provides. Put scripts in a `scripts/` folder inside the skill's own folder, next to `SKILL.md`. In a plugin, that looks like this:

```text theme={null}
my-plugin/
└── skills/
    └── render-chart/
        ├── SKILL.md
        └── scripts/
            └── render.py
```

In `SKILL.md`, write the script's path with `${CLAUDE_SKILL_DIR}`, for example `python3 ${CLAUDE_SKILL_DIR}/scripts/render.py`. Claude Code and Cowork replace `${CLAUDE_SKILL_DIR}` with the skill's folder when the skill loads. It's a placeholder in the skill text, not an environment variable. In chat on claude.ai, the skill's whole folder, scripts included, is copied into the code execution sandbox, so also keep the path readable relative to `SKILL.md`, such as `scripts/render.py`.

In Claude Code, running a script is a Bash tool call, so it needs your permission. When you test with [`claude -p`](https://code.claude.com/docs/en/headless), which can't stop to ask, allow the script on the command line, for example `--allowedTools "Bash(python3 /path/to/my-plugin/skills/render-chart/scripts/render.py *)"`, using the script's absolute path. Claude runs the script by its absolute path, and `Bash()` rules match the whole command line, so a rule that names the exact path approves only that script; a wildcard before the path would approve more than you intend.

Don't put API keys, passwords, or other credentials in a script or anywhere else in the skill: everyone you share the skill with receives its files. When a script needs to reach an outside service, have Claude use a [connector](/docs/connectors/getting-started) for that service instead, so each person signs in with their own account.

## Package your skill

You upload a skill to Claude as a ZIP file. The ZIP must contain the skill directory itself as its top level, because Claude looks for `<skill-name>/SKILL.md` inside the archive; a `SKILL.md` sitting at the root of the ZIP isn't recognized as a skill. The packaged file looks like this:

```
my-skill.zip
└── my-skill/
    ├── SKILL.md
    └── scripts/
```

<Steps>
  <Step title="Check the directory name">
    Make sure the directory name matches the `name` field in `SKILL.md`.
  </Step>

  <Step title="Zip the directory from its parent folder">
    Where the `zip` command is available, such as on macOS and Linux, run it from the folder that contains the skill directory, so the directory becomes the top level of the archive:

    ```bash theme={null}
    zip -r my-skill.zip my-skill/
    ```

    If you use another tool to create the ZIP, compress the skill folder itself rather than the files inside it.
  </Step>

  <Step title="Confirm the structure">
    List the archive and check that every entry starts with `my-skill/`:

    ```bash theme={null}
    unzip -l my-skill.zip
    ```

    If `SKILL.md` appears without the `my-skill/` prefix, you zipped the contents instead of the folder; zip again from the parent folder.
  </Step>
</Steps>

To check the skill's contents rather than the archive shape, [validate it before uploading](#before-uploading) with `skills-ref validate` or `claude plugin validate`, or ask Claude to review the folder against the [Agent Skills specification](https://agentskills.io/specification).

## Test your skill

Test the skill's files before you upload it, try it in Claude Code if you have it, confirm that Claude loads it after you upload, and then measure whether it improves Claude's output.

### Before uploading

Before you upload the ZIP, check the skill's files:

<Steps>
  <Step title="Review SKILL.md">
    Review `SKILL.md` for clarity.
  </Step>

  <Step title="Check the description">
    Verify the description accurately reflects when Claude should use the skill.
  </Step>

  <Step title="Check referenced files">
    Check that all referenced files exist.
  </Step>

  <Step title="Validate the skill">
    Check the frontmatter against the Agent Skills specification with the [`skills-ref` reference tool](https://github.com/agentskills/agentskills/tree/main/skills-ref). It isn't preinstalled: clone that repository and install it into a Python virtual environment as its README describes, which puts `skills-ref` on your `PATH` while the environment is active. Then, from the folder that contains the skill directory, run:

    ```bash theme={null}
    skills-ref validate ./my-skill
    ```

    A skill that passes prints `Valid skill: ./my-skill`. Otherwise the command lists each problem, such as a `name` that doesn't match the directory or a frontmatter field the specification doesn't define.

    If the skill is inside a plugin folder, running `claude plugin validate ./my-plugin` in your terminal also parses each skill's frontmatter: it reports a `SKILL.md` whose frontmatter doesn't parse, and prints `✔ Validation passed` when the plugin passes.
  </Step>
</Steps>

### In Claude Code

If you use [Claude Code](https://code.claude.com/docs/en/overview), you can try the skill from your terminal without uploading it. Copy the skill folder into `~/.claude/skills/`, so the file sits at `~/.claude/skills/my-skill/SKILL.md`, then start `claude` in any project. Describe a task the skill's `description` covers and check that Claude uses it, or type `/my-skill` to run it directly. If Claude doesn't pick the skill up on its own, revise the description. [Extend Claude with skills](https://code.claude.com/docs/en/skills) covers the other places Claude Code loads skills from, including a project's `.claude/skills/` folder and plugins.

### After uploading

After you upload, confirm that Claude loads the skill when it should:

<Steps>
  <Step title="Turn the skill on">
    Go to [**Customize > Skills**](https://claude.ai/customize/skills) in claude.ai or the desktop app and turn the skill on.
  </Step>

  <Step title="Try prompts that should trigger it">
    Send prompts that should trigger the skill, and review Claude's thinking to confirm it's loading the skill.
  </Step>

  <Step title="Iterate on the description">
    Iterate on the description if Claude isn't using it when expected.
  </Step>
</Steps>

### Measure whether the skill improves the output

Trying a few prompts tells you the skill loads, not whether Claude's answers are better with it. To check that, use [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator), a skill from Anthropic that runs your skill on test prompts you agree on, shows you the results, and helps you revise it. On claude.ai, turn it on under [**Customize > Skills**](https://claude.ai/customize/skills), where it's listed as from Anthropic, then ask Claude to evaluate your skill.

`skill-creator` does more in Cowork and Claude Code than in chat:

* **Chat**: `skill-creator` works through the test prompts one at a time and shows you the results in the conversation
* **Cowork and Claude Code**: it also runs the same prompts without the skill as a baseline, runs everything in parallel, and adds pass rates, timing, and token counts so you can compare the two. In Claude Code you install it as a plugin, as [Run evals with skill-creator](https://code.claude.com/docs/en/skills#run-evals-with-skill-creator) describes

If the skill is part of a plugin, you can also test the whole plugin from the Claude Code command line with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals), which grades eval cases you write and compares against a run without the plugin.

## Best practices

Follow these practices when you write a skill:

* **Keep it focused**: create separate skills for different workflows. Several focused skills combine better than one large skill, and Claude can use more than one in a conversation
* **Write a specific description**: say when the skill applies and include the words a request for that task would use. The description is the only part Claude reads before deciding to load the skill
* **Start with instructions**: begin with Markdown instructions and add scripts only when a step needs code
* **Show the output you expect**: include example inputs and outputs so Claude can match them
* **Test after each change**: run the skill on a real request after each significant edit, as [Test your skill](#test-your-skill) describes

For more, the Agent Skills site covers [best practices for skill creation](https://agentskills.io/skill-creation/best-practices) and [writing descriptions that trigger reliably](https://agentskills.io/skill-creation/optimizing-descriptions) in depth.

## Example skills

Anthropic's [skills repository](https://github.com/anthropics/skills/tree/main/skills) has working skills you can read and copy. These four cover the common shapes, from instructions only to instructions with reference files and scripts:

* **[brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)**: a single `SKILL.md` with no scripts or reference files. A good model for a skill that is only instructions, such as a style or formatting rule
* **[internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)**: instructions plus an `examples/` folder of sample documents that `SKILL.md` tells Claude to consult, the pattern from [Add resources](#add-resources)
* **[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)**: instructions, two reference files for less common tasks, and a `scripts/` folder Claude runs to fill forms and extract tables, the pattern from [Add scripts](#add-scripts)
* **[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)**: the skill that helps you write and test other skills, described in [Measure whether the skill improves the output](#measure-whether-the-skill-improves-the-output)

Copy a skill's structure rather than its contents: keep the folder layout and frontmatter, and replace the instructions with your own.

## Share or package your skill

After your skill works, you can give it to other people on its own or as part of a plugin. People you share it with should be able to read what it does, so keep the instructions and scripts plain enough to review.

* **Share or publish one skill**: on Team and Enterprise plans, open the skill from **Customize > Skills** and use the same **Share** and **Publish to org** controls that a plugin has. They work the way [sharing a plugin with specific people](/docs/plugins/share#share-a-plugin-with-specific-people) and [publishing a plugin to your organization](/docs/plugins/share#publish-a-plugin-to-your-organization) describe
* **Package skills and connectors together**: when you want several skills, or a skill plus the connector it uses, installed together, [build a plugin](/docs/plugins/build) that contains them

## Next steps

* [Skills in Claude Code](https://code.claude.com/docs/en/skills): create and test skills from the Claude Code CLI, including the `/skills` manager
* [Plugin structure and testing](/docs/plugins/build): package your skill as a plugin so other people can install it
* [Submit your plugin](/docs/plugins/submit): submit the plugin to the directory, where Anthropic reviews it before it's listed

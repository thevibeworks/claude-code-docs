> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin structure and testing

> Reference for the plugin folder: what each file is, the manifest fields every app reads, bundling an MCP connector with its skill, and testing on each app.

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

A plugin is a folder that packages skills, MCP connectors, commands, and agents, in any combination, so that people add them together. This page is the reference for that folder: what each file is and contains, the manifest fields every app reads, how an MCP connector and its skill fit together, and how to test the plugin on claude.ai, in Cowork, and in Claude Code.

[Build your first plugin](/docs/plugins/quickstart) walks you through making one end to end.

<Note>
  * If you want a plugin for your own use without writing files, see [Create a plugin with Claude](/docs/plugins/create-with-claude), which makes one from a conversation
  * If you're building for Claude Code only, see its [plugin authoring docs](https://code.claude.com/docs/en/plugins/create). Claude Code supports more component types than the other surfaces, and those docs are the full reference for anything Claude Code-only
  * If you're deciding which pieces your plugin needs, see [Decide what to include in your plugin](/docs/connectors/building/what-to-build)
</Note>

## Lay out the plugin folder

A plugin folder has a manifest at `.claude-plugin/plugin.json` and any combination of component directories beside it.

### Folder layout

Put only the manifest inside `.claude-plugin/`. Everything else goes at the plugin's top level.

Select a file to see what it's for and a minimal example; components that only some apps load, such as agents and hooks, are listed after the explorer.

<PluginExplorer>
  <Piece id="manifest">
    <p>The manifest identifies the plugin to every app and to Anthropic's directory, which doesn't accept a plugin without one. To publish the plugin in Anthropic's directory you also need [a README and a license](/docs/plugins/pre-submission-checklist#readme-and-license); select those files in the tree to see what each needs.</p>

    <p>Its `name` is the plugin's permanent identity: people install and refer to the plugin by this value, so make it specific to your product and never change it after release. Change `displayName` when you want a different label.</p>

    <p>This manifest has the fields that every app and the directory read:</p>

    ```json theme={null}
    {
      "name": "expense-reports",
      "displayName": "Expense Reports",
      "version": "1.0.0",
      "description": "File, track, and approve expense reports from a conversation, using your finance system's connector and your company's approval rules.",
      "author": { "name": "Example Corp", "url": "https://example.com" },
      "license": "MIT"
    }
    ```
  </Piece>

  <Piece id="skills">
    <p>A skill is a `SKILL.md` file in its own folder under `skills/`, and the folder name matches the skill's `name` field. Claude decides when to load the skill from its `description`, so write the description as the situations a user would be in. Skills load in chat, Cowork, and Claude Code.</p>

    <p>This skill files an expense from a receipt:</p>

    ```markdown theme={null}
    ---
    name: file-expense
    description: File an expense report. Use when the user mentions a receipt, reimbursement, or expense, or asks to submit spending for approval.
    ---

    To file an expense:

    1. Read the amount, date, merchant, and currency from the receipt.
    2. Call the expenses connector's `create_report` tool with those fields.
    3. Reply with the report number and its approval status.
    ```
  </Piece>

  <Piece id="references">
    <p>A skill folder can hold [supporting files](/docs/skills/how-to#add-resources) that are too detailed for `SKILL.md`:</p>

    <ul>
      <li>`references/` for documentation Claude reads when needed</li>
      <li>`assets/` for templates, images, and data files</li>
      <li>`scripts/` for code</li>
    </ul>

    <p>Mention each file in `SKILL.md` so Claude knows when to load it, for example "Pick the category from `references/categories.md`".</p>

    <p>This reference file lists the expense categories:</p>

    ```markdown theme={null}
    # Expense categories

    - Travel: flights, hotels, taxis, and mileage
    - Meals: client meals and team events
    - Software: subscriptions and licenses
    ```
  </Piece>

  <Piece id="scripts">
    <p>A skill can include scripts in a `scripts/` folder next to `SKILL.md`.</p>

    <p>In `SKILL.md`, refer to a script by its path under `${CLAUDE_SKILL_DIR}`, for example `python3 ${CLAUDE_SKILL_DIR}/scripts/total.py receipts.csv`. [Add scripts](/docs/skills/how-to#add-scripts) explains how each app resolves that path.</p>

    <p>This script totals the amounts in a CSV file of receipts:</p>

    ```python theme={null}
    import csv
    import sys

    with open(sys.argv[1], newline="") as f:
        total = sum(float(row["amount"]) for row in csv.DictReader(f))
    print(f"{total:.2f}")
    ```
  </Piece>

  <Piece id="commands">
    <p>A command is a single Markdown file under `commands/` with a `description` in its frontmatter. In Cowork and Claude Code, you run it by typing its name, here `/expense-reports:summarize`. In chat, a command loads as a skill, and Claude applies it when the task fits.</p>

    <p>This command summarizes a month's expenses:</p>

    ```markdown theme={null}
    ---
    description: Summarize this month's expense reports
    ---

    List this month's expense reports with their totals and approval status, then summarize them in three sentences.
    ```
  </Piece>

  <Piece id="mcp">
    <p>`.mcp.json` at the plugin root references your remote MCP server by URL. On claude.ai and in Cowork, the entry is listed on the plugin's **Connectors** tab, where each user adds or connects it and signs in through your server's OAuth flow. Claude Code loads it with the plugin.</p>

    <p>Don't put API keys or other secrets in this file, because every person who installs the plugin receives its files.</p>

    <p>This one points at the expenses server:</p>

    ```json theme={null}
    {
      "mcpServers": {
        "expenses": {
          "type": "http",
          "url": "https://mcp.example.com/mcp"
        }
      }
    }
    ```
  </Piece>

  <Piece id="readme">
    <p>A plugin loads without a README, but you need one to publish it: Anthropic's directory shows the README as the listing's description, and [validation](/docs/plugins/pre-submission-checklist#readme-and-license) blocks a submission that has none.</p>

    <p>Write at least 40 words, not counting words inside code blocks, and say what the plugin does, how to use it, and what data it sends.</p>

    <p>This README covers those three points:</p>

    ```markdown theme={null}
    # Expense Reports

    File, track, and approve expense reports from a conversation with Claude.

    ## Use it

    Attach a receipt and ask Claude to file it. Claude reads the amount, date,
    and merchant, files the report through the Expense Reports connector, and
    replies with the report number. Ask what's waiting on you to list the
    reports that need your approval.

    ## Data

    The plugin sends receipt details and report fields to your Example Corp
    account through mcp.example.com. It stores nothing itself.
    ```
  </Piece>

  <Piece id="license">
    <p>A plugin loads without a license, but you need one to publish it: Anthropic's directory doesn't list a plugin until it has a license, and [validation](/docs/plugins/pre-submission-checklist#readme-and-license) blocks a submission that has neither a `LICENSE` file nor a `license` field.</p>

    <p>Add a `LICENSE` file to the plugin folder, or set `license` in `plugin.json`.</p>
  </Piece>
</PluginExplorer>

<Note>
  The explorer is the scaled-down set: the pieces that chat, Cowork, and Claude Code all load, plus the README and license that Anthropic's directory requires. For every other folder and field a plugin can contain, including the pieces only Claude Code loads, see [Plugin components](https://code.claude.com/docs/en/plugins/components) and the [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) in the Claude Code docs.
</Note>

### Check what each app loads

A plugin can carry more than the explorer shows, but not every Claude app uses all of them. Design for the narrowest app you care about:

* **Skills and commands** load everywhere. In chat, a command loads as a skill that Claude applies when it fits
* **A remote MCP server** in `.mcp.json` appears on the plugin's **Connectors** tab in chat and Cowork, and works once the person adds or connects it there; Claude Code connects to it directly
* **Agents and hooks** load in Cowork and Claude Code; chat ignores them without an error
* **A local MCP server**, one the app starts as a command, loads in Claude Code and in Cowork sessions that run on the person's computer; chat ignores it
* **A top-level `bin/` directory** stops claude.ai and Cowork from installing the plugin at all

[Plugin support by app](/docs/plugins/platform-support#compare-component-support-by-app) has the full table, including LSP servers, output styles, and `${user_config.*}` references, and compares where installs are stored and what an organization controls on each app.

### Start from an example

Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) repository holds the role plugins listed in the directory, and each one is a working instance of this layout. The [productivity](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) plugin is a compact one to read first. It has a short manifest, an `.mcp.json`, and four skills, with no build step. Most plugins need no build step either, because they're only Markdown and JSON.

Copy the example plugin's structure rather than its contents.

## Write the plugin

The examples in this section build a plugin named `expense-reports` for a fictional finance product whose MCP server is at `mcp.example.com`. If you plan to submit the plugin to Anthropic's directory, keep the [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) open while you write: the developer portal validates the manifest, README, license, and scripts when you submit, and building with those checks in mind means validation passes the first time.

### Write the manifest

Create `.claude-plugin/plugin.json` with the fields every surface and the directory read:

```json theme={null}
{
  "name": "expense-reports",
  "displayName": "Expense Reports",
  "version": "1.0.0",
  "description": "File, track, and approve expense reports from a conversation, using your finance system's connector and your company's approval rules.",
  "author": { "name": "Example Corp", "url": "https://example.com" },
  "license": "MIT"
}
```

* **`name`**: the plugin's permanent identity. People install and refer to it by this value, so use lowercase words joined by hyphens, make it specific to your product, and never change it after release. Change `displayName` when you want a different label
* **`version`**: the release number people see for the plugin. Raise it on every release
* **`description`**: what people read in the directory and in [**Customize > Plugins**](https://claude.ai/customize/plugins) before installing
* **`license`**: give it here or as a `LICENSE` file. The directory requires one or the other, and a README of at least 40 words

If you have Claude Code installed, run `claude plugin validate ./expense-reports` from the folder's parent. It prints `✔ Validation passed` when the manifest and any component files parse, and names the field to fix when they don't. The [full manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) lists every optional field.

### Bundle an MCP connector with its skill

A plugin for your own product pairs an MCP server that gives Claude your product's tools with a skill that tells Claude when and how to use them. A connector alone leaves Claude to work out your workflow from tool names. The skill is where you put the sequence, the defaults, and what good output looks like.

Reference your server by URL in `.mcp.json` at the plugin root:

```json theme={null}
{
  "mcpServers": {
    "expenses": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

On claude.ai and in Cowork, that entry is listed on the plugin's **Connectors** tab, where the user [adds or connects it](/docs/plugins/overview#bundled-connectors) and signs in through your server's OAuth flow. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.

Don't put API keys or other secrets in this file, because every person who installs the plugin receives its files. If your server is already listed in the directory, use the same URL here, so that someone who has both your connector and your plugin sees one set of tools rather than two.

Then write the skill that uses it, at `skills/file-expense/SKILL.md`:

```markdown theme={null}
---
name: file-expense
description: File an expense report. Use when the user mentions a receipt, reimbursement, or expense, or asks to submit spending for approval.
---

To file an expense:

1. Ask for the receipt if the user hasn't attached one, and read the amount, date, merchant, and currency from it.
2. Call the expenses connector's `create_report` tool with those fields. Default the category from the merchant type; ask only if it's ambiguous.
3. If the amount is over the user's approval limit (check with `get_policy`), add their manager as approver before submitting.
4. Reply with the report number and its approval status. Don't paste the full API response.
```

Claude decides when to load the skill from the `description` line, so write it as the situations a user would be in, not as a summary of the file. [Create custom skills](/docs/skills/how-to) covers the frontmatter fields, resource files, scripts, and testing.

## Test the plugin on each surface

Test on each surface your users will use.

* **Claude Code**: run `claude --plugin-dir ./expense-reports` to start a session with the plugin loaded from your working copy. Your skills appear as `/expense-reports:file-expense`, and `/mcp` shows the server's connection state
* **claude.ai and Cowork**: upload the plugin to your own account, then check each component:
  1. Zip the plugin folder. The archive can hold the folder as its single top-level entry or the folder's contents directly. If the upload says `plugin.json must be at .claude-plugin/plugin.json at the zip root (or inside a single top-level directory)`, the manifest is nested more than one folder deep or the archive has other files beside the plugin folder.
  2. In claude.ai, go to **Customize > Plugins > Add > Upload plugin** and select the zip. The plugin then appears on your own account.
  3. Open a chat and ask Claude which skills it has from plugins.
  4. Connect the bundled connector from the plugin's **Connectors** tab.
  5. If your plugin has agents, start a Cowork task to confirm they load.
* **A team testing together**: push the folder to a Git repository set up as a [marketplace](https://code.claude.com/docs/en/plugins/create-marketplace), and have each tester add it from **Customize > Plugins > Add > Add marketplace** with the repository URL instead, so everyone installs the same copy

Loading the plugin shows that its parts appear. To measure whether its skills improve Claude's output, write eval cases and run [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) in Claude Code, which grades the results and compares them against a run without the plugin. To test one skill by itself on any surface, see [Measure whether the skill improves the output](/docs/skills/how-to#measure-whether-the-skill-improves-the-output).

Before you submit the plugin to the directory, run `claude plugin validate ./expense-reports`, then select **Validate** in the [developer portal](https://claude.ai/directory/manage). The portal runs every validation check, and [Run the checks before you submit](/docs/plugins/pre-submission-checklist#run-the-checks-before-you-submit) explains each result.

When something is missing on one surface and present on another, check it against [Check what each app loads](#check-what-each-app-loads) before debugging. An agent that never appears in chat, or a local server that chat doesn't start, is the surface behaving as designed.

## Add Claude Code-only components

Claude Code loads everything on this page and also supports components the other apps skip, such as language servers, executables in `bin/`, per-user configuration prompts, output styles, and dependencies between plugins. A plugin that includes them still installs on claude.ai and in Cowork, except that a top-level `bin/` directory stops claude.ai and Cowork from installing it at all. The Claude Code docs cover [each component](https://code.claude.com/docs/en/plugins/components) and [testing and debugging](https://code.claude.com/docs/en/plugins/create#test-and-debug) there.

## Next steps

Once the plugin works, you can distribute it through your organization, your own marketplace, or the directory:

* [Manage plugins for your organization](/docs/plugins/admin): on Team and Enterprise plans, an Owner can make the plugin available or installed by default for members
* [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace): list the plugin in a Git repository's `marketplace.json`, which anyone you give the URL to can add from **Customize > Plugins** or the Claude Code command line
* [Publish to the directory](/docs/directory/publish): submit the plugin from the [developer portal](https://claude.ai/directory/manage) so people on Pro, Max, Team, and Enterprise plans can find and add it on claude.ai and in Cowork, and use it in Claude Code. Anyone on a paid plan can submit without applying to a partner program first; on Team and Enterprise, an Owner submits

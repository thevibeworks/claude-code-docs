> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin pre-submission checklist

> Fix every finding before you submit a plugin to the Claude plugin directory: what the developer portal's validation and scan check, and what each result means.

Before the [Claude plugin directory](/docs/directory/publish) lists your plugin, the developer portal checks the plugin's files at two points. Validation runs in the plugin submission form at [claude.ai/directory/manage](https://claude.ai/directory/manage) when you select the **Validate** button. A scan runs after you submit, on each new commit that the directory picks up from the branch or tag that it follows. The scan checks the plugin's files again and runs a security scan.

Use this checklist to fix problems before you [submit your plugin](/docs/plugins/submit) from the developer portal on claude.ai. The checklist covers the automated checks only, and every plugin in the directory also has to follow the [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy). Start by [running the checks](#run-the-checks-before-you-submit) and [reading a validation result](#read-a-validation-result). Then use the tables in [what validation and the scan check](#review-what-validation-and-the-scan-check) to fix each finding, and [prepare for the security scan](#prepare-for-the-security-scan) that runs after you submit.

## Run the checks before you submit

Checking a plugin before you submit it takes three steps:

1. Optional: [check the plugin on your machine](#check-the-plugin-on-your-machine-optional) with Claude Code's `claude plugin validate` command, which catches syntax and schema errors before you push
2. [Validate in the developer portal](#validate-in-the-developer-portal), which runs every directory check in the tables on this page
3. [Read the result](#read-a-validation-result), fix every finding that the report marks **Blocking**, and then submit

The portal is open to the people who [can submit](/docs/directory/publish#confirm-you-can-submit-to-the-directory). If you can't submit, ask someone who can to run **Validate**.

### Check the plugin on your machine (optional)

If you have [Claude Code](https://code.claude.com/docs/en/setup), Anthropic's command-line coding tool, installed, you can catch syntax and schema errors before you push. Open a terminal in the folder that contains your plugin folder and run:

```bash theme={null}
claude plugin validate ./your-plugin
```

A plugin with no problems prints `✔ Validation passed`. Otherwise the output lists each error or warning with the file and field it's in; fix those and run the command again.

The `claude plugin validate` command only checks that your files are well-formed. It doesn't check the directory's requirements, such as whether you have a README and license or whether the name is taken; the portal's **Validate** checks those. [`plugin validate`](https://code.claude.com/docs/en/plugins/cli-reference#plugin-validate) in the Claude Code docs lists exactly what the command checks.

### Validate in the developer portal

The portal's **Validate** button runs every check in this page's tables against your repository and gives you a report before you submit anything.

<Steps>
  <Step title="Start a submission">
    Open the [developer portal](https://claude.ai/directory/manage) and select **Submit new**.
  </Step>

  <Step title="Choose Plugin bundle">
    When the portal asks **What would you like to submit?**, select **Plugin bundle**.
  </Step>

  <Step title="Enter the repository">
    On the **Source** step, enter the repository. [Submit your plugin](/docs/plugins/submit#submit-a-plugin) describes each field.
  </Step>

  <Step title="Validate">
    Select **Validate**. The report lists each finding with its result and, for many findings, a fix.
  </Step>

  <Step title="Fix blocking findings and validate again">
    The report covers only the commit that validation read, so it doesn't change when you push a fix. Push the fix, then select **Re-validate** on the **Source** step of the same form. When the new report has no findings with the **Blocks** result, continue through the form to submit the plugin.
  </Step>
</Steps>

### Read a validation result

Validation produces a report in the submission form, and the scan's results appear on the plugin's page in the developer portal. Each finding has one of these results:

* **Blocks:** the report marks the finding **Blocking**. You can't submit the plugin until you fix the problem and validate again
* **Held for a reviewer:** the report marks the finding **Policy hold**. You can submit, and an Anthropic reviewer reads the held version before it can go live. A hold isn't a rejection. The scan can raise the same hold again on each new version.
* **Warning:** the report shows the finding, and you can submit without fixing it. The plugin still has to follow the Anthropic Software Directory Policy
* **Note:** the report gives information, and nothing needs fixing

Some problems with the repository stop validation before there is a report. The submission form then shows one error, such as **Couldn’t validate that repository**, and no findings. The tables in [what validation and the scan check](#review-what-validation-and-the-scan-check) mark those checks as "Validation stops".

[Submit your plugin](/docs/plugins/submit#after-you-submit-a-plugin) explains how review and publishing proceed after you submit.

## Review what validation and the scan check

The plugin folder is the folder that contains `.claude-plugin/plugin.json`, the plugin's manifest. It can be the repository root or a subfolder. People who install the plugin get only the plugin folder, so everything the plugin runs has to be inside it.

Most checks read the plugin folder, and a few also read the rest of the repository. Fix every row marked **Blocks** before you submit.

Each table gives the result at validation, unless a row says that the result comes after you submit. For a finding with no title in the report, the report states the rule in words instead.

### Repository and folder layout

The repository and folder layout checks cover the plugin's location in the repository and what the repository as a whole contains.

| What to do                                                                                                                                                                                                                                                 | [Result if you don't](#read-a-validation-result)                      | Title in the report, if it has one                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Submit a folder that contains `.claude-plugin/plugin.json`                                                                                                                                                                                                 | Blocks                                                                |                                                                                                                                                        |
| Submit one plugin at a time. In a [marketplace repository](https://code.claude.com/docs/en/plugins/create-marketplace) with several plugins, validate and submit each plugin folder on its own.                                                            | Blocks                                                                | **Pick one plugin first**, when you select **Submit for review**                                                                                       |
| Keep every file that a hook, an MCP server command, or a script uses inside the plugin folder, and point every component path in `plugin.json` inside it                                                                                                   | Blocks for a `plugin.json` path that points outside the plugin folder |                                                                                                                                                        |
| Commit regular files and folders for everything the plugin loads, not symbolic links, Git submodules, or Git LFS pointer files                                                                                                                             | Blocks where the plugin loads the entry. Warning elsewhere.           |                                                                                                                                                        |
| Remove `.DS_Store`, `Thumbs.db`, `desktop.ini`, and `__MACOSX` entries from the plugin folder                                                                                                                                                              | Blocks                                                                | In validation, a message that begins "This is a macOS or Windows system file". After you submit, **Files in the repository the scanner won’t accept**. |
| Use file and folder names that are valid on both Windows and macOS: no colon, no trailing dot or space, no Windows device name such as `con.md` or `prn`, and no two names that differ only by capitalization                                              | Validation stops                                                      | **Couldn’t validate that repository**                                                                                                                  |
| Name each folder on the path to the plugin with letters, digits, dots, hyphens, and underscores only, and enter the plugin path with the same capitalization as the repository                                                                             | Validation stops                                                      | **Couldn’t validate that repository**                                                                                                                  |
| Keep `export-ignore` and `export-subst` out of every `.gitattributes` file. Keep `filter`, Git LFS included, and other attributes that rewrite file contents out of `.gitattributes` files at the repository root, above the plugin folder, and inside it. | Validation stops                                                      | **Couldn’t validate that repository**                                                                                                                  |
| Keep the repository under 50 MiB as GitHub archives it and under 256 MiB unpacked, with fewer than 10,000 files and folders, and keep every file in the plugin folder under 5 MiB                                                                          | Validation stops                                                      | **Repository too large to validate**                                                                                                                   |

The file-name, plugin-path, and `.gitattributes` checks all produce **Couldn’t validate that repository**. The error doesn't say which cause applies, so check each of them. [Files in the plugin folder](#files-in-the-plugin-folder) has tighter file limits that hold a version for a reviewer.

### Manifest and plugin name

`plugin.json` is the plugin's manifest. Beyond the syntax and schema errors that `claude plugin validate` catches, the directory runs the checks in this table. Settle the name before you submit, and raise `version` with every release, as [version management](https://code.claude.com/docs/en/plugins/loading#versions-and-updates) describes.

| What to do                                                                                                                                                                                                                                                                                                                                                       | [Result if you don't](#read-a-validation-result)                                                                | Title in the report, if it has one                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use a `name` made of lowercase letters, digits, and hyphens, up to 64 characters, that starts and ends with a letter or digit                                                                                                                                                                                                                                    | Blocks for non-ASCII characters. Warning for any other name that breaks the pattern, such as uppercase letters. | **Non-ASCII identifier** when blocked                                                                                                                   |
| Build the name around your own distinctive product or project name: not a reserved word such as `claude`, `anthropic`, `official`, `plugin`, `mcp`, or `test` as the whole name, not a [marketplace name reserved for Anthropic](https://code.claude.com/docs/en/plugins/marketplace-reference#reserved-names), and nothing that presents the plugin as official | Blocks. Held for a reviewer for a name made only of generic words, such as `test-plugin`.                       | **Name is taken** when blocked. **Name may be confused with an existing listing** when held.                                                            |
| Choose a name that no other organization's plugin uses. A name that differs only in capitalization or punctuation counts as the same name.                                                                                                                                                                                                                       | Blocks for the same name. Held for a reviewer for a look-alike.                                                 | **Name is taken** when blocked. **Name may be confused with an existing listing** when held.                                                            |
| Choose a name, `displayName`, and `author.name` that can't be mistaken for an existing plugin, publisher, connector, or well-known brand that isn't yours                                                                                                                                                                                                        | Held for a reviewer                                                                                             | **Name matches a known brand**, **Name may be confused with an existing listing**, or **Publisher name may be confused with another** for `author.name` |
| In a fork, give the plugin a name of its own. Forks are allowed.                                                                                                                                                                                                                                                                                                 | Held for a reviewer                                                                                             | **Fork uses the upstream project’s name**                                                                                                               |
| Write `displayName` and `author.name` in one writing system, without look-alike letters or invisible characters                                                                                                                                                                                                                                                  | Blocks                                                                                                          |                                                                                                                                                         |
| Spell the keys that declare components, such as `hooks` and `mcpServers`, exactly as the [plugins reference](https://code.claude.com/docs/en/plugins/manifest-reference) does, and keep them out of the `experimental` object                                                                                                                                    | Blocks                                                                                                          |                                                                                                                                                         |
| Set `description`, `author`, and `version`                                                                                                                                                                                                                                                                                                                       | Warning                                                                                                         |                                                                                                                                                         |

### README and license

The directory shows your README as the listing's description and requires a license before it lists the plugin.

| What to do                                                                                                                  | [Result if you don't](#read-a-validation-result) | Title in the report, if it has one       |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| Put a README of at least 40 words in the plugin folder, preferably named `README.md`. Words inside code blocks don't count. | Blocks                                           | **README missing**, **README too short** |
| Add a `LICENSE` file to the plugin folder, or set `license` in `plugin.json`                                                | Blocks                                           | **License missing**                      |

### Files in the plugin folder

The file checks apply to every file in the plugin folder, including images and documents.

| What to do                                                                                                                                                                                           | [Result if you don't](#read-a-validation-result)             | Title in the report, if it has one                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Keep every file that isn't an image or font under 256 KiB                                                                                                                                            | Held for a reviewer                                          | **Files or downloads the validator couldn’t inspect** |
| Keep the plugin to 512 files or fewer                                                                                                                                                                | Held for a reviewer                                          | **Files or downloads the validator couldn’t inspect** |
| Include only text files, SVG included, complete PNG, JPEG, GIF, and WebP images, and font files. Any other binary file, such as an `.ico`, `.pdf`, or `.zip` file or a compiled executable, is held. | Held for a reviewer                                          | **Files or downloads the validator couldn’t inspect** |
| To show a bundled image in the README, use Markdown image syntax. Don't refer to bundled images or fonts from commands, hooks, or scripts, or write their paths in backticks or a code block.        | Held for a reviewer                                          |                                                       |
| Declare each MCP server with `command` and `args` or with `url`, not a `.mcpb` or `.dxt` bundle                                                                                                      | Held for a reviewer. Blocks for a bundle fetched from a URL. | **Bundled MCP server not inspected** when held        |

### Review what the plugin runs and connects to

A package launcher is a command that downloads a package and runs it: `npx`, `bunx`, `pnpm dlx`, `yarn dlx`, `uvx`, `pipx run`, and `uv run` all count. `${CLAUDE_PLUGIN_ROOT}` is the variable that Claude Code sets to the plugin's installation directory.

| What to do                                                                                                                                                                                                                                                                                           | [Result if you don't](#read-a-validation-result)                        | Title in the report, if it has one                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Pin every package that a launcher runs to an exact version, such as `npx <package>@1.2.3` or `uvx <package>==1.2.3`, not a range or `@latest`. Run `uv run` with `--locked` or `--frozen`.                                                                                                           | Blocks                                                                  | **Unpinned npx launcher**, **Unpinned uvx launcher**                  |
| In a plugin that uses a launcher or runs a package install, don't include a package-manager configuration file that sets a registry, index, proxy, or other package source, such as `.npmrc`, `bunfig.toml`, or `uv.toml`                                                                            | Blocks with a launcher. Held for a reviewer with a package install.     | **Install may use a custom registry or package source** when held     |
| Keep real credentials out of every file, documentation and examples included. Ask for each value through a `userConfig` entry in `plugin.json` with `sensitive: true`, and refer to it as `${user_config.KEY}`.                                                                                      | Blocks                                                                  | **Secret in MCP headers** for a credential in an MCP server's headers |
| Don't read a credential that is already set in the user's environment, such as `$GITHUB_TOKEN`, and send it to a server, even in a README example. Ask for it through `userConfig` instead.                                                                                                          | Held for a reviewer. Blocks for an HTTP hook that sends the credential. | **Uses a credential from the user’s machine** when held               |
| Make `.mcp.json` valid JSON in which every server entry matches the schema in the [MCP documentation](https://code.claude.com/docs/en/mcp)                                                                                                                                                           | Blocks                                                                  | **.mcp.json can’t be parsed** for invalid JSON                        |
| Give each remote MCP server a `type` of `http`, `sse`, or `ws` and a `url` that is an absolute `https://` or `wss://` URL, a `${user_config.KEY}` reference, or `""` when the plugin has no fixed endpoint                                                                                           | Blocks                                                                  | **MCP server URL is not https** for a URL with another scheme         |
| Start each local MCP server by running a file in the plugin with plain arguments, such as `node ${CLAUDE_PLUGIN_ROOT}/server.js`, not through a shell, an inline program such as `-c`, or a package-manager script such as `npm run`                                                                 | Held for a reviewer                                                     | **MCP server command wasn’t read**                                    |
| In the command of a hook or an MCP server, write each path in full from `${CLAUDE_PLUGIN_ROOT}`, with no other variable, command substitution, wildcard, or inline program such as `python3 -c`                                                                                                      | Blocks when the plugin folder is a subfolder of the repository          |                                                                       |
| Keep launchers and package installs out of each script that a hook or an MCP server runs. When the plugin folder is a subfolder of the repository, also keep shell variables other than `${CLAUDE_PLUGIN_ROOT}`, command substitutions, and calls to other files in the plugin out of those scripts. | Held for a reviewer                                                     | **Scripts the validator couldn’t follow**                             |

### Choices a reviewer always checks

These choices are held for a reviewer even when the plugin meets every other check:

* **A package from a registry:** a launcher that runs a package pinned to an exact version, or `uv run` with `--locked` or `--frozen`, is still held, because the package's own dependencies resolve at install time. The finding is **Runs a pinned npx or uvx package**
* **A lockfile install:** `package.json` beside `package-lock.json`, `npm-shrinkwrap.json`, `bun.lock`, or `bun.lockb` in the root of the plugin folder is held, because Claude Code [installs the packages in that lockfile](https://code.claude.com/docs/en/plugins/loading#node-js-package-dependencies) when a user installs the plugin. The finding is **Dependencies install from a lockfile**
* **A program the validator can't read through, when the plugin folder is a subfolder of the repository:** the validator follows only plain shell scripts. When a hook, an MCP or LSP server command, or a `` !`…` `` line in a skill or command runs a non-shell file from the plugin, passes a whole directory to an interpreter, or runs a shell script that itself runs another file, that file is held. A script that `SKILL.md` only tells Claude to run isn't part of this check. To avoid the hold, keep the plugin at the root of its own repository, or keep the logic a hook or server runs in shell scripts that name each path as `${CLAUDE_PLUGIN_ROOT}/<file>`. The finding is **Scripts the validator couldn’t follow**

If you bundle a package's code into the plugin instead, the launcher or install finding no longer applies, and a reviewer hold can still apply. Validation and the scan check the bundled file like every other file in the plugin folder, including the 256 KiB limit in [Files in the plugin folder](#files-in-the-plugin-folder).

### Hooks, skills, commands, and agents

The component checks confirm that Claude Code can load each hook, skill, command, and agent file in the plugin.

| What to do                                                                                                                                                                                                       | [Result if you don't](#read-a-validation-result)                                                                                | Title in the report, if it has one         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Make `hooks/hooks.json` valid JSON with a top-level `hooks` object, only the hook events and hook types in the [hooks reference](https://code.claude.com/docs/en/hooks), and an `https://` URL on each HTTP hook | Blocks                                                                                                                          | **hooks.json is invalid** for invalid JSON |
| Leave `hooks/hooks.json` out of the `hooks` field in `plugin.json`, because Claude Code loads that file automatically                                                                                            | Warning                                                                                                                         |                                            |
| Write valid YAML front matter in each skill, command, and agent file, with `description` as a single text value, not a list                                                                                      | Blocks for front matter that doesn't parse or a `description` that isn't text. Warning for no front matter or no `description`. |                                            |
| Name component folders and files with the exact spelling and capitalization Claude Code expects, such as `hooks/`, `skills/`, and `SKILL.md`                                                                     | Blocks                                                                                                                          |                                            |

## Prepare for the security scan

The security scan looks for behavior that a plugin doesn't disclose, such as sending data elsewhere, running hidden code, or changing Claude's permission settings.

A first submission that fails the security scan is rejected, and a later version that fails can't go live. A new version that the scan flags can be held for a reviewer. The **Versions** tab on the plugin's page in the developer portal shows **Didn’t pass the security scan**, or the category of the finding, such as **Sends data to an undisclosed destination**. [Submit your plugin](/docs/plugins/submit#fix-a-failed-version) explains what to do when a version doesn't pass.

To prepare, make the plugin's behavior visible in its README and its source:

* Describe in the README everything the plugin runs, sends, or fetches. A complete README doesn't make a behavior allowed. The [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) sets what a plugin is allowed to do
* Commit readable source instead of compiled, packed, or minified code. Code that the security scan can't read is held for a reviewer

## Test the plugin's behavior before you submit

Validation and the scan check how the plugin is built. They don't check whether the plugin helps the people who install it. Before you submit, test the plugin's output and how it loads on the surfaces your users will use:

<Steps>
  <Step title="Compare output with and without the plugin">
    Run the plugin's skills on real prompts and compare the output with what Claude produces without the plugin. [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) runs that comparison for the whole plugin in Claude Code, and [Measure whether the skill improves the output](/docs/skills/how-to#measure-whether-the-skill-improves-the-output) covers one skill at a time.
  </Step>

  <Step title="Load the plugin on each surface">
    Load the plugin on each surface your users will use, as [Test the plugin on each surface](/docs/plugins/build#test-the-plugin-on-each-surface) describes.
  </Step>
</Steps>

## Next steps

* [Submit your plugin](/docs/plugins/submit): enter the repository in the developer portal, follow the review, and publish
* [Publish to the directory](/docs/directory/publish): confirm your plan and role can submit, and see what Anthropic's review involves

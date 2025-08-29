import { readFile, readdir, access, mkdir } from "fs/promises";
import { join } from "path";
import { execSync } from "child_process";
import { homedir } from "os";

export interface DocumentationResource {
  uri: string;
  name: string;
  description: string;
  mimeType: string;
}

export async function getDocsPath(): Promise<string> {
  // Try ~/.claude/claude-code-docs first, then $(pwd)/.claude/claude-code-docs
  const homeDocsPath = join(homedir(), ".claude", "claude-code-docs");
  const pwdDocsPath = join(process.cwd(), ".claude", "claude-code-docs");

  try {
    await access(join(homeDocsPath, "content"));
    return homeDocsPath;
  } catch {
    try {
      await access(join(pwdDocsPath, "content"));
      return pwdDocsPath;
    } catch {
      // Fallback to relative path for development
      return join(process.cwd(), "..");
    }
  }
}

export async function ensureDocsInstalled(): Promise<void> {
  const homeDocsPath = join(homedir(), ".claude", "claude-code-docs");

  try {
    await access(join(homeDocsPath, "content"));
    console.error("[INFO] Documentation found at ~/.claude/claude-code-docs");
    return;
  } catch {
    // Docs not found, try to install
    console.error(
      "[INFO] Documentation not found, installing to ~/.claude/claude-code-docs",
    );

    try {
      await mkdir(join(homedir(), ".claude"), { recursive: true });

      // Clone the repository
      execSync(
        "git clone https://github.com/thevibeworks/claude-code-docs.git claude-code-docs",
        {
          cwd: join(homedir(), ".claude"),
          stdio: "inherit",
        },
      );

      console.error("[INFO] Documentation installed successfully");
    } catch (error) {
      console.error("[WARN] Failed to auto-install documentation:", error);
      throw new Error(
        "Could not install documentation. Please run: git clone https://github.com/thevibeworks/claude-code-docs.git ~/.claude/claude-code-docs",
      );
    }
  }
}

export async function getDocumentationResources(): Promise<
  DocumentationResource[]
> {
  const resources: DocumentationResource[] = [];
  const docsPath = await getDocsPath();
  const contentDir = join(docsPath, "content", "claude-code-docs");

  try {
    const files = await readdir(contentDir);
    const markdownFiles = files.filter((f) => f.endsWith(".md"));

    for (const file of markdownFiles) {
      const uri = `claude-code-docs://docs/${file}`;
      const name = file.replace(".md", "");
      const description = getDocumentationDescription(name);

      resources.push({
        uri,
        name,
        description,
        mimeType: "text/markdown",
      });
    }

    // Add release notes
    const releaseNotesDir = join(docsPath, "content", "release-notes");
    try {
      const releaseFiles = await readdir(releaseNotesDir);
      for (const file of releaseFiles.filter((f) => f.endsWith(".md"))) {
        resources.push({
          uri: `claude-code-docs://release-notes/${file}`,
          name: `release-notes/${file.replace(".md", "")}`,
          description: "Claude Code release notes and changelog",
          mimeType: "text/markdown",
        });
      }
    } catch {
      // Release notes dir may not exist
    }
  } catch (error) {
    console.error("Error reading documentation resources:", error);
  }

  return resources;
}

export async function readDocumentationResource(uri: string): Promise<string> {
  if (!uri.startsWith("claude-code-docs://")) {
    throw new Error(`Invalid URI: ${uri}`);
  }

  const docsPath = await getDocsPath();
  const path = uri.replace("claude-code-docs://", "");
  const filePath = join(docsPath, "content", path);

  try {
    const content = await readFile(filePath, "utf-8");
    return content;
  } catch (error) {
    throw new Error(`Failed to read file: ${path}`);
  }
}

function getDocumentationDescription(name: string): string {
  const descriptions: Record<string, string> = {
    overview: "Claude Code overview and capabilities",
    quickstart: "Getting started guide for Claude Code",
    setup: "Installation and setup instructions",
    settings: "Configuration and permissions setup",
    "common-workflows": "Common usage patterns and workflows",
    memory: "Memory management and CLAUDE.md usage",
    "interactive-mode": "Interactive mode features and keyboard shortcuts",
    "slash-commands": "Available slash commands reference",
    hooks: "Hooks configuration and examples",
    troubleshooting: "Common issues and solutions",
    "cli-reference": "Command line interface reference",
    "ide-integrations": "IDE integrations and setup",
    mcp: "Model Context Protocol integration",
    "github-actions": "GitHub Actions integration",
    sdk: "SDK usage and development",
    "third-party-integrations": "Third-party tool integrations",
    devcontainer: "Development container setup",
    security: "Security considerations and best practices",
    iam: "Authentication and permissions management",
    "monitoring-usage": "OpenTelemetry monitoring setup",
    costs: "Cost management and tracking",
    "data-usage": "Data usage policies and guidelines",
    "legal-and-compliance": "Legal and compliance information",
    "amazon-bedrock": "Amazon Bedrock integration",
    "google-vertex-ai": "Google Vertex AI integration",
    "corporate-proxy": "Corporate proxy configuration",
    "llm-gateway": "LLM gateway setup and usage",
  };

  return descriptions[name] || `Claude Code documentation: ${name}`;
}

import { readFile, readdir } from "fs/promises";
import { join } from "path";

export interface RemoteDocumentationResource {
  uri: string;
  name: string;
  description: string;
  mimeType: string;
}

// Cache for fetched documentation
const docCache = new Map<string, string>();
const cacheExpiry = 5 * 60 * 1000; // 5 minutes
const cacheTimestamps = new Map<string, number>();

export async function getRemoteDocumentationResources(): Promise<
  RemoteDocumentationResource[]
> {
  const resources: RemoteDocumentationResource[] = [];

  // Define available documentation files
  const docFiles = [
    "overview.md",
    "quickstart.md",
    "setup.md",
    "settings.md",
    "common-workflows.md",
    "memory.md",
    "interactive-mode.md",
    "slash-commands.md",
    "hooks.md",
    "troubleshooting.md",
    "cli-reference.md",
    "ide-integrations.md",
    "mcp.md",
    "github-actions.md",
    "sdk.md",
    "third-party-integrations.md",
    "devcontainer.md",
    "security.md",
    "iam.md",
    "monitoring-usage.md",
    "costs.md",
    "data-usage.md",
    "legal-and-compliance.md",
    "amazon-bedrock.md",
    "google-vertex-ai.md",
    "corporate-proxy.md",
    "llm-gateway.md",
  ];

  for (const file of docFiles) {
    const uri = `claude-code-docs://remote/docs/${file}`;
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
  resources.push({
    uri: "claude-code-docs://remote/release-notes/CHANGELOG.md",
    name: "release-notes/CHANGELOG",
    description: "Claude Code release notes and changelog",
    mimeType: "text/markdown",
  });

  return resources;
}

export async function readRemoteDocumentationResource(
  uri: string,
): Promise<string> {
  if (!uri.startsWith("claude-code-docs://remote/")) {
    throw new Error(`Invalid remote URI: ${uri}`);
  }

  const resourcePath = uri.replace("claude-code-docs://remote/", "");

  // Check cache first
  const cached = docCache.get(resourcePath);
  const timestamp = cacheTimestamps.get(resourcePath);
  if (cached && timestamp && Date.now() - timestamp < cacheExpiry) {
    return cached;
  }

  try {
    // Fetch from GitHub raw content
    const githubUrl = `https://raw.githubusercontent.com/thevibeworks/claude-code-docs/main/content/claude-code-docs/${resourcePath}`;

    const response = await fetch(githubUrl);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const content = await response.text();

    // Cache the result
    docCache.set(resourcePath, content);
    cacheTimestamps.set(resourcePath, Date.now());

    return content;
  } catch (error) {
    throw new Error(
      `Failed to fetch remote resource ${resourcePath}: ${error instanceof Error ? error.message : "Unknown error"}`,
    );
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

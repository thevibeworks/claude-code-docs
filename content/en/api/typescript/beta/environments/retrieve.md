---
title: Get Environment
url: https://platform.claude.com/docs/en/api/typescript/beta/environments/retrieve
---

# Get Environment

- Signature: `client.beta.environments.retrieve(environmentID: string, params?: EnvironmentRetrieveParams, options?: RequestOptions): BetaEnvironment`
- Endpoint: `GET /v1/environments/{environment_id}`

Retrieve a specific environment by ID.

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.retrieve(
  "env_011CZkZ9X2dpNyB7HsEFoRfW"
);

console.log(betaEnvironment.id);
```

## Example response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [],
      "cargo": [],
      "gem": [],
      "go": [],
      "npm": [],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Parameters

```ts
environmentID: string; // path parameter

interface EnvironmentRetrieveParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** Unified Environment resource for both cloud and self-hosted environments. */
interface BetaEnvironment {
  /** The type of object (always 'environment') */
  type: "environment";
  /** Environment identifier (e.g., 'env_...') */
  id: string;
  /** RFC 3339 timestamp when environment was archived, or null if not archived */
  archived_at: string | null;
  /**
   * Environment configuration (either Anthropic Cloud or self-hosted)
   * - `BetaSelfHostedConfig`: beta header: managed-agents-2026-04-01
   */
  config: BetaCloudConfig | BetaSelfHostedConfig;
  /** RFC 3339 timestamp when environment was created */
  created_at: string;
  /** User-provided description for the environment; null when unset */
  description: string | null;
  /** User-provided metadata key-value pairs */
  metadata: Record<string, string>;
  /** Human-readable name for the environment */
  name: string;
  /** RFC 3339 timestamp when environment was last updated */
  updated_at: string;
  /** The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account. */
  scope?: "organization" | "account"; // beta header: managed-agents-2026-04-01
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

/** `cloud` environment configuration. */
interface BetaCloudConfig {
  /** Environment type */
  type: "cloud";
  /**
   * Network configuration policy.
   * - `BetaLimitedNetwork`: beta header: managed-agents-2026-04-01
   */
  networking: BetaUnrestrictedNetwork | BetaLimitedNetwork;
  /** Package manager configuration. */
  packages: BetaPackages; // beta header: managed-agents-2026-04-01
}

/** Configuration for self-hosted environments. */
interface BetaSelfHostedConfig {
  /** Environment type */
  type: "self_hosted";
}

/** Unrestricted network access. */
interface BetaUnrestrictedNetwork {
  /** Network policy type */
  type: "unrestricted";
}

/** Limited network access. */
interface BetaLimitedNetwork {
  /** Network policy type */
  type: "limited";
  /** Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. */
  allow_mcp_servers: boolean;
  /** Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. */
  allow_package_managers: boolean;
  /** Specifies domains the container can reach. */
  allowed_hosts: Array<string>;
}

interface BetaPackages {
  /** Package configuration type */
  type?: "packages"; // default: packages
  /** Ubuntu/Debian packages to install */
  apt: Array<string>;
  /** Rust packages to install */
  cargo: Array<string>;
  /** Ruby packages to install */
  gem: Array<string>;
  /** Go packages to install */
  go: Array<string>;
  /** Node.js packages to install */
  npm: Array<string>;
  /** Python packages to install */
  pip: Array<string>;
}
```

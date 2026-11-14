---
title: Versions
url: https://platform.claude.com/docs/en/api/typescript/beta/skills/versions
---

# Versions

## Create Skill Version

- Signature: `client.beta.skills.versions.create(skillID: string, params: VersionCreateParams, options?: RequestOptions): BetaSkillVersion`
- Endpoint: `POST /v1/skills/{skill_id}/versions`

### Example request

```ts
import fs from "fs";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSkillVersion = await client.beta.skills.versions.create("skill_id", {
  files: [fs.createReadStream("path/to/file")]
});

console.log(betaSkillVersion.id);
```

### Example response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

/** Unique identifier for the skill. The format and length of IDs may change over time. */
skillID: string; // path parameter

interface VersionCreateParams {
  /** Files to upload for the skill. All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory. */
  files: Array<Uploadable>;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
interface BetaSkillVersion {
  /** Object type. For Skill Versions, this is always `"skill_version"`. */
  type: "skill_version";
  /** Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references. */
  id: string;
  /** ISO 8601 timestamp of when the skill was created. */
  created_at: string; // format: date-time
  /** Description of the skill version. This is extracted from the SKILL.md file in the skill upload. */
  description: string;
  /** The Skill's immutable kebab-case slug, set at creation from the first upload's SKILL.md frontmatter `name` (or its enclosing directory). Every later upload must resolve to the same value. Also the top-level directory of the Skill's mounted files and the base name of a downloaded archive. */
  name: string;
  /** Unique identifier for the skill. The format and length of IDs may change over time. */
  skill_id: string;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `CMEKContextUnavailableError` (HTTP status 503, error code `cmek_context_unavailable`)

  The workspace's encryption settings could not be read, so the request was refused. Retry in a few minutes.

### Types

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
```

## List Skill Versions

- Signature: `client.beta.skills.versions.list(skillID: string, params?: VersionListParams, options?: RequestOptions): PageCursor<BetaSkillVersion>`
- Endpoint: `GET /v1/skills/{skill_id}/versions`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaSkillVersion of client.beta.skills.versions.list("skill_id")) {
  console.log(betaSkillVersion.id);
}
```

### Example response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

### Parameters

```ts
/** Unique identifier for the skill. The format and length of IDs may change over time. */
skillID: string; // path parameter

interface VersionListParams {
  /** Number of results to return per page. Ranges from `1` to `1000`. Defaults to `20`. */
  limit?: number | null; // query parameter, minimum: 1, maximum: 1000
  /** Optionally set to the `next_page` token from the previous response. */
  page?: string | null; // query parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Download Skill Version Content

- Signature: `client.beta.skills.versions.download(version: string, params: VersionDownloadParams, options?: RequestOptions): Response`
- Endpoint: `GET /v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const response = await client.beta.skills.versions.download("version", {
  skill_id: "skill_id"
});

console.log(response);

const content = await response.blob();
console.log(content);
```

### Parameters

```ts
/** Identifies the skill version by its version ID. Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129"). */
version: string; // path parameter

interface VersionDownloadParams {
  /** Unique identifier for the skill. The format and length of IDs may change over time. */
  skill_id: string; // path parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Get Skill Version

- Signature: `client.beta.skills.versions.retrieve(version: string, params: VersionRetrieveParams, options?: RequestOptions): BetaSkillVersion`
- Endpoint: `GET /v1/skills/{skill_id}/versions/{version}`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSkillVersion = await client.beta.skills.versions.retrieve("version", {
  skill_id: "skill_id"
});

console.log(betaSkillVersion.id);
```

### Example response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### Parameters

```ts
/** Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version. Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129"). */
version: string; // path parameter

interface VersionRetrieveParams {
  /** Unique identifier for the skill. The format and length of IDs may change over time. */
  skill_id: string; // path parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Delete Skill Version

- Signature: `client.beta.skills.versions.delete(version: string, params: VersionDeleteParams, options?: RequestOptions): BetaDeletedSkillVersion`
- Endpoint: `DELETE /v1/skills/{skill_id}/versions/{version}`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDeletedSkillVersion = await client.beta.skills.versions.delete("version", {
  skill_id: "skill_id"
});

console.log(betaDeletedSkillVersion.id);
```

### Example response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

### Parameters

```ts
/** Identifies the skill version by its version ID. Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129"). */
version: string; // path parameter

interface VersionDeleteParams {
  /** Unique identifier for the skill. The format and length of IDs may change over time. */
  skill_id: string; // path parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
interface BetaDeletedSkillVersion {
  /** Deleted object type. For Skill Versions, this is always `"skill_version_deleted"`. */
  type: "skill_version_deleted";
  /** Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references. */
  id: string;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

# Projects

## List projects

**GET** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

### Query parameters

- `created_at: optional object`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gt: optional string`

    Filter projects updated after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects updated at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects updated before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects updated at or before this time (RFC 3339 format)

    format: date-time

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Headers

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

    format: date-time

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

    format: date-time

  - `user: object or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

## Get project details

**GET** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Headers

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

  format: date-time

- `deleted_at: string or null`

  Timestamp when the project was deleted by an end user, or null otherwise

  format: date-time

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

  format: date-time

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

- `organization_id: string`

  **Deprecated**

  Organization identifier (tagged ID)

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

## Delete project

**DELETE** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Headers

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  default: claude_project_deleted

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

## Domain types

### Project List Response

- `ProjectListResponse object`

  Project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

    format: date-time

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

    format: date-time

  - `user: object or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization identifier (tagged ID)

### Project Retrieve Response

- `ProjectRetrieveResponse object`

  Detailed project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `attachments_count: number`

    Number of attachments contained within this project

  - `chats_count: number`

    Number of chats contained within this project

  - `created_at: string`

    Project creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

    format: date-time

  - `description: string`

    Project description

  - `instructions: string`

    Project's custom instructions / prompt

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

    format: date-time

  - `user: object or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization identifier (tagged ID)

### Project Delete Response

- `ProjectDeleteResponse object`

  Response for deleting a Claude project.

  - `id: string`

    The ID of the Claude project that was deleted

  - `type: optional "claude_project_deleted"`

    Constant string confirming deletion.

    default: claude_project_deleted

## Projects › Attachments

### List project attachments

**GET** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object or object`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference object`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `mime_type: string`

      MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `type: "project_file"`

      Discriminator marking this as a binary file

      default: project_file

  - `ComplianceProjectDocReference object`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      default: text/plain

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      default: project_doc

    - `updated_at: string or null`

      Last-modified timestamp of the document. Reserved for future use — currently always null.

      format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Projects › Collaborators

### List project collaborators

**GET** `/v1/compliance/apps/projects/{project_id}/collaborators`

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object or object or object or object`

  List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

  - `ComplianceProjectUserCollaborator object`

    An individual user granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      default: user

    - `user_id: string or null`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object`

    An RBAC group granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "group"`

      Discriminator marking this as a group collaborator

      default: group

  - `ComplianceProjectOrganizationCollaborator object`

    An entire organization granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      default: organization

  - `ComplianceProjectOrganizationRoleCollaborator object`

    All holders of an organization-level role granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      default: organization_role

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Projects › Documents

### Get project document content

**GET** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Get project document metadata

**GET** `/v1/compliance/apps/projects/documents/{document_id}/metadata`

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `claude_project_id: string`

  The project this document belongs to

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `md5: string`

  Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

- `mime_type: "text/plain"`

  MIME type of the document content, always plain text

  default: text/plain

- `size_bytes: number`

  Size in bytes of the document content (UTF-8 encoded)

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Delete project document

**DELETE** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the project document that was deleted

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  default: claude_project_document_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

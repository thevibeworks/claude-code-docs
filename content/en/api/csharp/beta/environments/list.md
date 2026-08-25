# List Environments

`EnvironmentListPageResponse Beta.Environments.List(parameters, cancellationToken = default)`

**GET** `/v1/environments`

List environments with pagination support.

## Parameters

- `EnvironmentListParams parameters`

  - `bool includeArchived`

    Query param: Include archived environments in the response

  - `long limit`

    Query param: Maximum number of environments to return

    maximum: 1000, minimum: 1

  - `string? page`

    Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

## Returns

- `class EnvironmentListPageResponse:`

  Response when listing environments.

  This response model uses opaque cursor-based pagination. Use the `page`
  query parameter with the value from `next_page` to fetch the next page.

  - `required IReadOnlyList<BetaEnvironment> Data`

    List of environments.

    - `required string ID`

      Environment identifier (e.g., 'env_...')

    - `required string? ArchivedAt`

      RFC 3339 timestamp when environment was archived, or null if not archived

    - `required Config Config`

      Environment configuration (either Anthropic Cloud or self-hosted)

      - `class BetaCloudConfig:`

        `cloud` environment configuration.

        - `required Networking Networking`

          Network configuration policy.

          - `class BetaUnrestrictedNetwork:`

            Unrestricted network access.

            - `JsonElement Type constant`

              Network policy type

          - `class BetaLimitedNetwork:`

            Limited network access.

            - `required bool AllowMcpServers`

              Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

            - `required bool AllowPackageManagers`

              Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

            - `required IReadOnlyList<string> AllowedHosts`

              Specifies domains the container can reach.

            - `JsonElement Type constant`

              Network policy type

        - `required BetaPackages Packages`

          Package manager configuration.

          - `required IReadOnlyList<string> Apt`

            Ubuntu/Debian packages to install

          - `required IReadOnlyList<string> Cargo`

            Rust packages to install

          - `required IReadOnlyList<string> Gem`

            Ruby packages to install

          - `required IReadOnlyList<string> Go`

            Go packages to install

          - `required IReadOnlyList<string> Npm`

            Node.js packages to install

          - `required IReadOnlyList<string> Pip`

            Python packages to install

          - `Type Type`

            Package configuration type

        - `JsonElement Type constant`

          Environment type

      - `class BetaSelfHostedConfig:`

        Configuration for self-hosted environments.

        - `JsonElement Type constant`

          Environment type

    - `required string CreatedAt`

      RFC 3339 timestamp when environment was created

    - `required string? Description`

      User-provided description for the environment; null when unset

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs

    - `required string Name`

      Human-readable name for the environment

    - `JsonElement Type constant`

      The type of object (always 'environment')

    - `required string UpdatedAt`

      RFC 3339 timestamp when environment was last updated

    - `Scope Scope`

      The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

      - `Organization`

      - `Account`

  - `required string? NextPage`

    Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

## Example

```csharp
EnvironmentListParams parameters = new();

var page = await client.Beta.Environments.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

### Response (200)

```json
{
  "data": [
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
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

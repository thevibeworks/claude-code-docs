# Delete File

`$ ant beta:files delete`

**DELETE** `/v1/files/{file_id}`

Delete File

## Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_deleted_file: object`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

## Example

```bash
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

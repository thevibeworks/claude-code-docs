# Download File

**GET** `/v1/files/{file_id}/content`

Download File

## Path parameters

- `file_id: string`

  ID of the File.

## Example

```bash
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

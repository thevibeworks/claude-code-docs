# Anthropic legal and policy pages

Fetched by `uv run scripts/fetcher.py --section legal` from
`https://www.anthropic.com/legal/*`. This file is written by hand; the fetcher
does not touch it.

- `<slug>.md` -- the text the page shows today, with the page's version list at
  the end. Its git log is the change record, including edits Anthropic makes
  without a new version.
- `<slug>/<effective date>.md` -- every version that list names, from
  `https://www.anthropic.com/legal/archive/<version id>`. Front matter holds the
  version id, effective time, the previous version and the PDF, when one exists.

A version that disappears from the list is kept and recorded in
`tombstones.json` ("dropped from versionHistory"). It is never deleted.

## The version list is Anthropic's account, not a record

The fetcher refetches old versions on every run, because Anthropic does rewrite
them. The clear case is the Supported Regions Policy:

- The version labelled effective 2026-05-12 was created in the CMS on
  2026-10-13. It holds the text of 2026-10-08: one list of 185 countries for all
  products, and three unsupported categories (located in, incorporated or
  headquartered in, majority-owned or controlled from).
- The Wayback Machine capture of 2026-05-16 shows a different page: 184
  countries, no Democratic Republic of the Congo, and the older ownership clause.

What the page actually said before 2026-10 exists only in the Wayback Machine
(`/legal/supported-countries`, which redirected to `/legal/supported-regions`
on 2026-10-13 and now answers 404). Dated by the captures on either side:

| First seen | Change |
|---|---|
| 2023-05-12 | One list, 159 countries |
| 2024-04-02 | Separate lists: API 161, Claude.ai 97 |
| by 2024-06-12 | Claude.ai 174, API 175 |
| by 2024-08-03 | Claude.ai adds Brazil; both lists 175 |
| 2025-09-02..05 | Majority-ownership clause; Ukraine also excludes Kherson and Zaporizhzhia |
| 2026-04-22..30 | +9: CAR, Eritrea, Ethiopia, Libya, Mali, Nicaragua, Somalia, South Sudan, Sudan (184) |
| 2026-09-21..22 | + Democratic Republic of the Congo (185) |
| 2026-10-08 | One list for all products; three unsupported categories |
| 2026-11-12 | Current version effective |

Captures: `https://web.archive.org/cdx/search/cdx?url=anthropic.com/legal/supported-countries`.

Also stale: `content/en/api/supported-regions.md` (from platform.claude.com)
still lists 175 countries and the pre-2025-09 Ukraine wording as of 2026-11-15.

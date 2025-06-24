#!/bin/bash

# Fetch Claude Code docs from Anthropic sitemap
# Usage: ./fetchccdocs.sh [--format md] [--out dir]

set -euo pipefail

FORMAT="md"
OUTPUT_DIR="references/claude-code-docs"
SITEMAP_URL="https://docs.anthropic.com/sitemap.xml"

while [[ $# -gt 0 ]]; do
    case $1 in
    --format)
        FORMAT="$2"
        shift 2
        ;;
    --out)
        OUTPUT_DIR="$2"
        shift 2
        ;;
    -h | --help)
        echo "Usage: $0 [--format md] [--out dir]"
        exit 0
        ;;
    *)
        echo "Unknown option: $1"
        exit 1
        ;;
    esac
done

echo "Fetching Claude Code docs to $OUTPUT_DIR"

mkdir -p "$OUTPUT_DIR"

METADATA_FILE="$OUTPUT_DIR/.metadata.json"
FETCH_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CLAUDE_VERSION="unknown"
if command -v claude &>/dev/null; then
    CLAUDE_VERSION=$(claude --version 2>/dev/null || echo "unknown")
fi

download_doc() {
    local url=$1
    local output_file=$2

    mkdir -p "$(dirname "$output_file")"

    for i in {1..3}; do
        if curl -sS -f -L "${url}.${FORMAT}" -o "$output_file" 2>/dev/null; then
            echo "[OK] $(basename "$output_file")"
            return 0
        else
            [ $i -lt 3 ] && sleep 2
        fi
    done

    echo "[FAIL] $(basename "$output_file")"
    return 1
}

# Get sitemap
SITEMAP_CONTENT=$(curl -sS "$SITEMAP_URL")

# Extract claude-code URLs (English only)
URLS=$(echo "$SITEMAP_CONTENT" |
    grep -oE '<loc>https://docs\.anthropic\.com/en/[^<]*claude-code[^<]*</loc>' |
    sed 's/<[^>]*>//g' | sort -u)

TOTAL=$(echo "$URLS" | wc -l | tr -d ' ')
echo "Found $TOTAL pages"

SUCCESS=0
FAIL=0

TMPFILE=$(mktemp)
echo "0 0" >"$TMPFILE"

echo "$URLS" | while IFS= read -r url; do
    [ -z "$url" ] && continue

    relative_path=${url#https://docs.anthropic.com/en/}

    if [[ "$relative_path" == docs/claude-code/* ]]; then
        file_path=${relative_path#docs/claude-code/}
    else
        file_path="$relative_path"
    fi

    output_file="$OUTPUT_DIR/${file_path}.${FORMAT}"

    read SUCCESS FAIL <"$TMPFILE"
    if download_doc "$url" "$output_file"; then
        echo "$((SUCCESS + 1)) $FAIL" >"$TMPFILE"
    else
        echo "$SUCCESS $((FAIL + 1))" >"$TMPFILE"
    fi
done

read SUCCESS FAIL <"$TMPFILE"
rm -f "$TMPFILE"

cat >"$METADATA_FILE" <<EOF
{
  "fetch_date": "$FETCH_DATE",
  "claude_version": "$CLAUDE_VERSION",
  "total_urls": $TOTAL,
  "downloaded": $SUCCESS,
  "failed": $FAIL,
  "format": "$FORMAT",
  "source": "$SITEMAP_URL"
}
EOF

echo -e "\nTotal: $TOTAL, Success: $SUCCESS, Failed: $FAIL"
echo "Saved to: $OUTPUT_DIR"

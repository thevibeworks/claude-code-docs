#!/bin/bash

# Fetch Claude Code docs from Anthropic sitemap
# Usage: ./fetchccdocs.sh [--format md] [--out dir]

set -uo pipefail

FORMAT="md"
OUTPUT_DIR="claude-code-docs"
SITEMAP_URL="https://docs.anthropic.com/sitemap.xml"
ANTHROPIC_SITEMAP_URL="https://www.anthropic.com/sitemap.xml"

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

echo "[INFO] Fetching Claude Code docs to $OUTPUT_DIR"
echo "[INFO] Using sitemaps: $SITEMAP_URL and $ANTHROPIC_SITEMAP_URL"

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
    local method=$3
    local fetch_url

    echo "[DEBUG] Downloading: $url -> $output_file (method: $method)" >&2
    mkdir -p "$(dirname "$output_file")"

    case $method in
    "jina")
        fetch_url="https://r.jina.ai/${url}"
        echo "[DEBUG] Using jina.ai proxy: $fetch_url" >&2
        ;;
    "direct")
        fetch_url="${url}.${FORMAT}"
        echo "[DEBUG] Direct fetch: $fetch_url" >&2
        ;;
    *)
        echo "[ERROR] Unknown fetch method: $method" >&2
        return 1
        ;;
    esac

    for i in {1..3}; do
        echo "[DEBUG] Attempt $i/3 for $(basename "$output_file")" >&2
        if curl -sS -f -L "$fetch_url" -o "$output_file" 2>/dev/null; then
            echo "[OK] $(basename "$output_file")" >&2
            return 0
        else
            echo "[WARN] Attempt $i failed for $(basename "$output_file")" >&2
            [ $i -lt 3 ] && sleep 2
        fi
    done

    echo "[FAIL] $(basename "$output_file")" >&2
    return 1
}

process_sitemap() {
    local sitemap_url=$1
    local sitemap_name=$2
    local url_pattern=$3
    local fetch_method=$4
    local path_prefix=$5

    echo "[INFO] Processing $sitemap_name sitemap: $sitemap_url" >&2

    local sitemap_content
    if ! sitemap_content=$(curl -sS "$sitemap_url" 2>/dev/null); then
        echo "[ERROR] Failed to fetch $sitemap_name sitemap, skipping..." >&2
        echo "0 0"
        return
    fi

    echo "[INFO] Extracting claude-code URLs from $sitemap_name..." >&2
    local urls
    urls=$(echo "$sitemap_content" |
        grep -oE "<loc>$url_pattern</loc>" 2>/dev/null |
        sed 's/<[^>]*>//g' 2>/dev/null || true)

    local url_count
    url_count=$(echo "$urls" | grep -c . 2>/dev/null || echo "0")
    echo "[DEBUG] Found $url_count URLs from $sitemap_name" >&2

    if [[ $url_count -eq 0 ]]; then
        echo "0 0"
        return
    fi

    local success=0 fail=0

    while IFS= read -r url; do
        [[ -z "$url" ]] && continue

        echo "[DEBUG] Processing $sitemap_name URL: $url" >&2

        local relative_path file_path output_file
        if [[ "$sitemap_name" == "docs" ]]; then
            relative_path=${url#https://docs.anthropic.com/en/}
            if [[ "$relative_path" == docs/claude-code/* ]]; then
                file_path=${relative_path#docs/claude-code/}
            else
                file_path="$relative_path"
            fi
        else
            relative_path=${url#https://www.anthropic.com/}
            file_path="$path_prefix/$relative_path"
        fi

        output_file="$OUTPUT_DIR/${file_path}.${FORMAT}"
        echo "[DEBUG] Output file: $output_file" >&2

        if download_doc "$url" "$output_file" "$fetch_method"; then
            ((success++))
        else
            ((fail++))
        fi
    done <<<"$urls"

    echo "$success $fail"
}

# Process each sitemap
echo "[INFO] Processing sitemaps..."
DOCS_RESULT=$(process_sitemap "$SITEMAP_URL" "docs" "https://docs\\.anthropic\\.com/en/[^<]*claude-code[^<]*" "direct" "")
ANTHROPIC_RESULT=$(process_sitemap "$ANTHROPIC_SITEMAP_URL" "anthropic" "https://www\\.anthropic\\.com/[^<]*claude-code[^<]*" "jina" "anthropic-blog")

# Parse results with defaults
read DOCS_SUCCESS DOCS_FAIL <<<"${DOCS_RESULT:-0 0}"
read ANTHROPIC_SUCCESS ANTHROPIC_FAIL <<<"${ANTHROPIC_RESULT:-0 0}"

# Ensure variables have numeric values
DOCS_SUCCESS=${DOCS_SUCCESS:-0}
DOCS_FAIL=${DOCS_FAIL:-0}
ANTHROPIC_SUCCESS=${ANTHROPIC_SUCCESS:-0}
ANTHROPIC_FAIL=${ANTHROPIC_FAIL:-0}

# Calculate totals
SUCCESS=$((DOCS_SUCCESS + ANTHROPIC_SUCCESS))
FAIL=$((DOCS_FAIL + ANTHROPIC_FAIL))
TOTAL=$((SUCCESS + FAIL))

echo "[INFO] Found $TOTAL total pages processed"

if [[ $TOTAL -eq 0 ]]; then
    echo "[WARN] No URLs found to fetch, exiting gracefully"
    cat >"$METADATA_FILE" <<EOF
{
  "fetch_date": "$FETCH_DATE",
  "claude_version": "$CLAUDE_VERSION",
  "total_urls": 0,
  "downloaded": 0,
  "failed": 0,
  "format": "$FORMAT",
  "sitemaps": {
    "docs": {
      "url": "$SITEMAP_URL",
      "downloaded": 0,
      "failed": 0
    },
    "anthropic": {
      "url": "$ANTHROPIC_SITEMAP_URL", 
      "downloaded": 0,
      "failed": 0
    }
  },
  "error": "No URLs found in sitemaps"
}
EOF
    echo "[INFO] Created metadata file with error status"
    exit 0
fi

cat >"$METADATA_FILE" <<EOF
{
  "fetch_date": "$FETCH_DATE",
  "claude_version": "$CLAUDE_VERSION",
  "total_urls": $TOTAL,
  "downloaded": $SUCCESS,
  "failed": $FAIL,
  "format": "$FORMAT",
  "sitemaps": {
    "docs": {
      "url": "$SITEMAP_URL",
      "downloaded": $DOCS_SUCCESS,
      "failed": $DOCS_FAIL
    },
    "anthropic": {
      "url": "$ANTHROPIC_SITEMAP_URL",
      "downloaded": $ANTHROPIC_SUCCESS,
      "failed": $ANTHROPIC_FAIL
    }
  }
}
EOF

echo
echo "[INFO] ========== FETCH SUMMARY =========="
echo "[INFO] Total URLs: $TOTAL"
echo "[INFO] Successfully downloaded: $SUCCESS"
echo "[INFO] Failed downloads: $FAIL"
if [[ $TOTAL -gt 0 ]]; then
    echo "[INFO] Success rate: $((SUCCESS * 100 / TOTAL))%"
else
    echo "[INFO] Success rate: N/A (no URLs to fetch)"
fi
echo "[INFO] Output directory: $OUTPUT_DIR"
echo "[INFO] ================================="

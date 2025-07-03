#!/bin/bash

# Fetch Claude Code docs from Anthropic sitemap
# Usage: ./fetchccdocs.sh [--format md] [--out dir]

set -uo pipefail

FORMAT="md"
OUTPUT_DIR="."
SITEMAP_URL="https://docs.anthropic.com/sitemap.xml"
ANTHROPIC_SITEMAP_URL="https://www.anthropic.com/sitemap.xml"
GITHUB_REPO_URL="https://github.com/anthropics/claude-code"

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

# Create directory structure
mkdir -p "$OUTPUT_DIR/claude-code-docs"
mkdir -p "$OUTPUT_DIR/anthropic-blog"

METADATA_FILE="$OUTPUT_DIR/.metadata.json"
MANIFEST_FILE="$OUTPUT_DIR/claude-code-manifest.json"
FETCH_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Get latest version from npm registry
LATEST_NPM_VERSION="unknown"
if command -v curl &>/dev/null && command -v jq &>/dev/null; then
  LATEST_NPM_VERSION=$(curl -sSL "https://registry.npmjs.org/-/package/@anthropic-ai/claude-code/dist-tags" 2>/dev/null | \
    jq -r '.latest' 2>/dev/null || echo "unknown")
elif command -v curl &>/dev/null; then
  # Fallback without jq
  LATEST_NPM_VERSION=$(curl -sSL "https://registry.npmjs.org/-/package/@anthropic-ai/claude-code/dist-tags" 2>/dev/null | \
    grep -o '"latest":"[^"]*"' | cut -d'"' -f4 || echo "unknown")
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
  local current=0

  while IFS= read -r url; do
    [[ -z "$url" ]] && continue
    ((current++))

    echo "[INFO] Processing $sitemap_name [$current/$url_count]: $(basename "$url")" >&2
    echo "[DEBUG] Processing $sitemap_name URL: $url" >&2

    local relative_path file_path output_file
    if [[ "$sitemap_name" == "docs" ]]; then
      relative_path=${url#https://docs.anthropic.com/en/}
      if [[ "$relative_path" == docs/claude-code/* ]]; then
        file_path="claude-code-docs/${relative_path#docs/claude-code/}"
      else
        file_path="claude-code-docs/$relative_path"
      fi
    else
      relative_path=${url#https://www.anthropic.com/}
      file_path="anthropic-blog/$relative_path"
    fi

    output_file="$OUTPUT_DIR/${file_path}.${FORMAT}"
    echo "[DEBUG] Output file: $output_file" >&2

    if download_doc "$url" "$output_file" "$fetch_method"; then
      ((success++))
      echo "[PROGRESS] $sitemap_name: $success/$url_count completed" >&2
    else
      ((fail++))
      echo "[PROGRESS] $sitemap_name: $success/$url_count completed, $fail failed" >&2
    fi
  done <<<"$urls"

  echo "$success $fail"
}

fetch_github_content() {
  local output_dir=$1
  local github_success=0
  local github_fail=0

  echo "[INFO] Fetching GitHub content..." >&2

  local changelog_file="$output_dir/claude-code/CHANGELOG.md"
  echo "[DEBUG] Fetching CHANGELOG.md..." >&2
  if curl -sS -f -L "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md" -o "$changelog_file"; then
    echo "[OK] CHANGELOG.md" >&2
    ((github_success++))
  else
    echo "[FAIL] CHANGELOG.md" >&2
    ((github_fail++))
  fi

  echo "$github_success $github_fail"
}

fetch_npm_manifest() {
  local manifest_file=$1
  
  echo "[INFO] Fetching Claude Code npm manifest..." >&2
  
  if command -v jq &>/dev/null; then
    if curl -sSL "https://registry.npmjs.org/@anthropic-ai/claude-code/latest" 2>/dev/null | \
       jq '.' > "$manifest_file" 2>/dev/null; then
      echo "[OK] NPM manifest saved to $manifest_file (formatted)" >&2
    else
      echo "[FAIL] Could not fetch npm manifest" >&2
      return 1
    fi
  else
    if curl -sSL "https://registry.npmjs.org/@anthropic-ai/claude-code/latest" -o "$manifest_file" 2>/dev/null; then
      echo "[OK] NPM manifest saved to $manifest_file (raw - jq not available)" >&2
    else
      echo "[FAIL] Could not fetch npm manifest" >&2
      return 1
    fi
  fi
}

# Process each sitemap
echo "[INFO] Processing sitemaps..."
DOCS_RESULT=$(process_sitemap "$SITEMAP_URL" "docs" "https://docs\\.anthropic\\.com/en/[^<]*claude-code[^<]*" "direct" "")
ANTHROPIC_RESULT=$(process_sitemap "$ANTHROPIC_SITEMAP_URL" "anthropic" "https://www\\.anthropic\\.com/[^<]*claude-code[^<]*" "jina" "anthropic-blog")

# Fetch GitHub content
echo "[INFO] Fetching GitHub content..."
GITHUB_RESULT=$(fetch_github_content "$OUTPUT_DIR")

# Fetch npm manifest
fetch_npm_manifest "$MANIFEST_FILE"

# Parse results with defaults
read DOCS_SUCCESS DOCS_FAIL <<<"${DOCS_RESULT:-0 0}"
read ANTHROPIC_SUCCESS ANTHROPIC_FAIL <<<"${ANTHROPIC_RESULT:-0 0}"
read GITHUB_SUCCESS GITHUB_FAIL <<<"${GITHUB_RESULT:-0 0}"

# Ensure variables have numeric values
DOCS_SUCCESS=${DOCS_SUCCESS:-0}
DOCS_FAIL=${DOCS_FAIL:-0}
ANTHROPIC_SUCCESS=${ANTHROPIC_SUCCESS:-0}
ANTHROPIC_FAIL=${ANTHROPIC_FAIL:-0}
GITHUB_SUCCESS=${GITHUB_SUCCESS:-0}
GITHUB_FAIL=${GITHUB_FAIL:-0}

# Calculate totals
SUCCESS=$((DOCS_SUCCESS + ANTHROPIC_SUCCESS + GITHUB_SUCCESS))
FAIL=$((DOCS_FAIL + ANTHROPIC_FAIL + GITHUB_FAIL))
TOTAL=$((SUCCESS + FAIL))

echo "[INFO] Found $TOTAL total pages processed"

if [[ $TOTAL -eq 0 ]]; then
  echo "[WARN] No URLs found to fetch, exiting gracefully"
  cat >"$METADATA_FILE" <<EOF
{
  "metadata": {
    "version": "1.0",
    "fetch_date": "$FETCH_DATE",
    "format": "$FORMAT"
  },
  "versions": {
    "latest_npm": "$LATEST_NPM_VERSION",
    "npm_package": "@anthropic-ai/claude-code"
  },
  "sources": {
    "docs": {
      "name": "Anthropic Documentation",
      "url": "$SITEMAP_URL",
      "pattern": "claude-code",
      "output_dir": "claude-code-docs",
      "stats": { "downloaded": 0, "failed": 0, "total": 0 }
    },
    "blog": {
      "name": "Anthropic Blog", 
      "url": "$ANTHROPIC_SITEMAP_URL",
      "pattern": "claude-code",
      "output_dir": "anthropic-blog",
      "stats": { "downloaded": 0, "failed": 0, "total": 0 }
    },
    "github": {
      "name": "GitHub Repository",
      "url": "$GITHUB_REPO_URL",
      "files": ["CHANGELOG.md"],
      "output_dir": "claude-code",
      "stats": { "downloaded": 0, "failed": 0, "total": 0 }
    }
  },
  "summary": {
    "total_sources": 3,
    "total_files": 0,
    "total_downloaded": 0,
    "total_failed": 0,
    "success_rate": 0,
    "error": "No URLs found in sitemaps"
  }
}
EOF
  echo "[INFO] Created metadata file with error status"
  exit 0
fi

# Calculate success rate
SUCCESS_RATE=0
if [[ $TOTAL -gt 0 ]]; then
  SUCCESS_RATE=$(echo "scale=1; $SUCCESS * 100 / $TOTAL" | bc 2>/dev/null || echo "$((SUCCESS * 100 / TOTAL))")
fi

cat >"$METADATA_FILE" <<EOF
{
  "metadata": {
    "version": "1.0",
    "fetch_date": "$FETCH_DATE",
    "format": "$FORMAT"
  },
  "versions": {
    "latest_npm": "$LATEST_NPM_VERSION",
    "npm_package": "@anthropic-ai/claude-code"
  },
  "sources": {
    "docs": {
      "name": "Anthropic Documentation",
      "url": "$SITEMAP_URL",
      "pattern": "claude-code",
      "output_dir": "claude-code-docs",
      "stats": { "downloaded": $DOCS_SUCCESS, "failed": $DOCS_FAIL, "total": $((DOCS_SUCCESS + DOCS_FAIL)) }
    },
    "blog": {
      "name": "Anthropic Blog",
      "url": "$ANTHROPIC_SITEMAP_URL", 
      "pattern": "claude-code",
      "output_dir": "anthropic-blog",
      "stats": { "downloaded": $ANTHROPIC_SUCCESS, "failed": $ANTHROPIC_FAIL, "total": $((ANTHROPIC_SUCCESS + ANTHROPIC_FAIL)) }
    },
    "github": {
      "name": "GitHub Repository",
      "url": "$GITHUB_REPO_URL",
      "files": ["CHANGELOG.md"],
      "output_dir": "claude-code",
      "stats": { "downloaded": $GITHUB_SUCCESS, "failed": $GITHUB_FAIL, "total": $((GITHUB_SUCCESS + GITHUB_FAIL)) }
    }
  },
  "summary": {
    "total_sources": 3,
    "total_files": $TOTAL,
    "total_downloaded": $SUCCESS,
    "total_failed": $FAIL,
    "success_rate": $SUCCESS_RATE
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

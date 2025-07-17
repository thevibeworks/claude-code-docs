#!/bin/bash

# Check for meaningful changes in Claude Code documentation
# Usage: ./scripts/check-changes.sh [--verbose|-v]
# Returns: 0 if meaningful changes found, 1 if not

set -uo pipefail

# Ensure we're in git repo
if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Error: Not in a git repository" >&2
  exit 1
fi

# Add all changes to staging
git add .

MEANINGFUL=false
REASONS=()

# Check for verbose flag
VERBOSE=false
[[ "${1:-}" == "--verbose" || "${1:-}" == "-v" ]] && VERBOSE=true

$VERBOSE && echo "Checking for meaningful changes..."

# 1. Check version changes in manifest
if git diff --cached --name-only | grep -q "content/claude-code-manifest.json"; then
  $VERBOSE && echo "Manifest file changed, checking version..."
  
  OLD_VERSION=$(git show HEAD:content/claude-code-manifest.json 2>/dev/null | jq -r '.version // ""' 2>/dev/null || echo "")
  NEW_VERSION=$(jq -r '.version // ""' content/claude-code-manifest.json 2>/dev/null || echo "")
  
  # Handle empty old version
  [[ -z "$OLD_VERSION" ]] && OLD_VERSION="(new)"
  
  if [[ -n "$NEW_VERSION" && "$OLD_VERSION" != "$NEW_VERSION" ]]; then
    [[ "$VERBOSE" == "true" ]] && echo "Version change: $OLD_VERSION → $NEW_VERSION"
    
    # Check if it's major/minor change
    if [[ "$OLD_VERSION" =~ ^[0-9]+\.[0-9]+ ]] && [[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+ ]]; then
      OLD_MAJOR_MINOR=$(echo "$OLD_VERSION" | cut -d. -f1-2)
      NEW_MAJOR_MINOR=$(echo "$NEW_VERSION" | cut -d. -f1-2)
      
      if [[ "$OLD_MAJOR_MINOR" != "$NEW_MAJOR_MINOR" ]]; then
        [[ "$VERBOSE" == "true" ]] && echo "Major/minor version change detected - meaningful!"
        MEANINGFUL=true
        REASONS+=("Version update: $OLD_VERSION → $NEW_VERSION")
      else
        [[ "$VERBOSE" == "true" ]] && echo "Patch version change - not considered meaningful"
      fi
    else
      [[ "$VERBOSE" == "true" ]] && echo "Version format unrecognized - considering meaningful"
      MEANINGFUL=true
      REASONS+=("Version update: $OLD_VERSION → $NEW_VERSION")
    fi
  fi
fi

# 2. Check CHANGELOG for new features
if git diff --cached --name-only | grep -E "(CHANGELOG|changelog)" >/dev/null 2>&1; then
  [[ "$VERBOSE" == "true" ]] && echo "CHANGELOG updated, checking for new features..."
  
  if git diff --cached | grep -E "^\+.*(\[feat\]|\[feature\]|### Added|### Changed)" >/dev/null 2>&1; then
    [[ "$VERBOSE" == "true" ]] && echo "CHANGELOG updated with new features - meaningful!"
    MEANINGFUL=true
    REASONS+=("CHANGELOG updated with new features")
  else
    [[ "$VERBOSE" == "true" ]] && echo "CHANGELOG updated but no new features detected"
  fi
fi

# 3. Check for substantial documentation changes
OTHER_CHANGES=$(git diff --cached --name-only | grep -v -E 'content/(\.metadata|claude-code-manifest)\.json$' || true)

if [[ -n "$OTHER_CHANGES" ]]; then
  LINES_CHANGED=$(git diff --cached --numstat | grep -v -E 'content/(\.metadata|claude-code-manifest)\.json$' | awk '{sum += $1 + $2} END {print sum+0}')
  FILES_CHANGED=$(echo "$OTHER_CHANGES" | wc -l)
  
  [[ "$VERBOSE" == "true" ]] && echo "Documentation changes: $FILES_CHANGED files, $LINES_CHANGED lines"
  
  if [[ "$LINES_CHANGED" -gt 10 ]]; then
    [[ "$VERBOSE" == "true" ]] && echo "Substantial documentation changes ($LINES_CHANGED lines) - meaningful!"
    MEANINGFUL=true
    REASONS+=("$FILES_CHANGED documentation files changed ($LINES_CHANGED lines)")
  else
    [[ "$VERBOSE" == "true" ]] && echo "Minor documentation changes ($LINES_CHANGED lines) - not substantial enough"
  fi
fi

# Final decision and summary
if [[ "$MEANINGFUL" == "true" ]]; then
  if [[ ${#REASONS[@]} -gt 0 ]]; then
    echo "Meaningful changes: $(IFS='; '; echo "${REASONS[*]}")"
  else
    echo "Meaningful changes detected"
  fi
  exit 0
else
  echo "No meaningful changes detected"
  if [[ -n "$OTHER_CHANGES" ]]; then
    echo "Reason: Documentation changes ($LINES_CHANGED lines) below threshold (100+ lines required)"
  else
    echo "Reason: Only metadata/manifest changes detected"
  fi
  git reset HEAD .
  exit 1
fi

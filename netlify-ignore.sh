#!/usr/bin/env bash
# Skip Netlify build if only docs or non-site-impact files changed
# Exit 0 to skip, exit 1 to build

# No previous commit on first deploy
if [ -z "$(git rev-parse --verify HEAD^ 2>/dev/null)" ]; then
  exit 1
fi

CHANGED=$(git diff --name-only HEAD^ HEAD)

# If any of these paths changed, we DO want to build
MUST_BUILD_REGEX='^(content/|layouts/|static/|src/|config\.toml|netlify\.toml|hugo\.toml|package\.json)$'

# If only docs changed, skip
ONLY_DOCS=true
for f in $CHANGED; do
  if [[ $f =~ $MUST_BUILD_REGEX ]]; then
    ONLY_DOCS=false
    break
  fi
  # anything outside documentation/, README, or *.md, tests, tooling docs should force build
  if [[ ! $f =~ ^documentation/ ]] && [[ ! $f =~ README\.md$ ]] && [[ ! $f =~ \.md$ ]] && [[ ! $f =~ ^tests/ ]] && [[ ! $f =~ ^tools/ ]]; then
    ONLY_DOCS=false
    break
  fi
done

if $ONLY_DOCS; then
  echo "Netlify: skipping build (doc-only changes)"
  exit 0
fi

exit 1

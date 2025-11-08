# Build Credits Strategy (Netlify Free Tier)

You have ~300 credits/month. Each deploy costs 15 → 20 deploys total. Traffic does NOT consume credits; deploy frequency does.

## Core Principles
1. Batch changes locally; deploy after meaningful increments.
2. Avoid utility commits ("typo", "spacing"). Fix multiple issues together.
3. Skip builds for doc-only edits (handled by `netlify-ignore.sh`).
4. Use feature branches; merge to `main` only when ready.
5. Limit deploy previews (disable for non-critical branches).

## Recommended Weekly Cadence
- Mon: Layout or style iteration → 1 deploy.
- Wed: Content additions (batch 2–4 devotionals) → 1 deploy.
- Fri: Polish + documentation update → 1 deploy.
That pattern ≈ 12 deploys / month (180 credits) leaving buffer.

## When to Trigger a Deploy
Deploy only if one or more of:
- Public layout or CSS changed.
- New content visible on site.
- Config (`config.toml`) modified.
- Critical fix (broken navigation, 404 issue).

## Safe Local Workflow
```
# Work locally
hugo server -D
# Optional: check broken links or HTML (future enhancement)
# Stage your grouped changes
git add -p
# Write clear commit message
git commit -m "Homepage hero refinement + 3 new devotionals"
# Push once
git push origin main
```

## Pre-Push Hook Behavior (optional)
Warn when pushing very small commits to encourage batching.

## Importing Archive Content
- Prepare content files locally.
- Add images & excerpts.
- Single commit for each batch of 3–6 posts.

## Monitoring
- Track deploy count manually in README or a simple log.
- If you approach 18 deploys mid-month, reduce pushes.

## Migration Trigger Points
Consider Cloudflare Pages if ANY of these:
- Need > 25 deploys / month consistently.
- Want instant preview for many branches.
- Plan scheduled (automatic) daily builds for feeds/search.

## Anti-Patterns
- Pushing after every single markdown file.
- Committing just to “see if something deploys.” Use local preview.
- Redundant tiny style tweaks across multiple commits.

## Checklist Before Push
- Combined small edits?
- No obvious unused debug code?
- Built locally without errors?
- Content front matter validated?
- One descriptive commit message?

---
Revision: v1.0

# The Anchor — Hugo Site

This is the Hugo-powered website for The Anchor (gettheanchor.org). Write devotionals in Markdown and deploy automatically to Netlify.

## Local Development

```powershell
# From the hugo-site directory
hugo server -D --disableFastRender
# Visit http://localhost:1313
```

## Build

```powershell
hugo
# Output in /public
```

## Netlify Deployment

- Build command: `hugo`
- Publish directory: `public`
- Environment variable (recommended):
  - `HUGO_VERSION = 0.152.2`

## Content Structure

- `content/devotionals/*.md` — each devotional with front matter, e.g.

```yaml
---
title: "When the Fight Feels Hard: Running with Endurance"
date: 2025-11-01
type: "friday" # or "monday"
scripture: "Hebrews 12:1–3"
readingTime: "12 min read"
featured: true
image: "/images/devotionals/fight-feels-hard-hero.jpg"
excerpt: "Short summary used on cards and SEO."
---
```

## Theming

- `layouts/` — templates (home, list, single)
- `static/css/` — CSS files
- `static/js/` — JavaScript
- `static/images/` — assets served at `/images/...`

## Domain

- Base URL is set to `https://gettheanchor.org/` in `hugo.toml`.
- Configure DNS in Cloudflare to point `gettheanchor.org` and/or `www.gettheanchor.org` to Netlify after connecting the repo.

# Migrate Hugo site to Cloudflare Pages

This guide moves the site from Netlify to Cloudflare Pages to remove per-deploy credit limits while keeping your current workflow.

## 1) Prepare repository
- Ensure `hugo-site/` is your project root where `config.toml` lives.
- Confirm Hugo version (currently 0.152.2). Cloudflare Pages supports `HUGO_VERSION` env var.

## 2) Create Pages project
1. Go to Cloudflare Dashboard → Pages → Create a project
2. Connect to GitHub and select your repository
3. Build settings:
   - Framework preset: None
   - Build command: `hugo --config config.toml --gc --minify`
   - Build output directory: `public`
   - Environment variables:
     - `HUGO_VERSION = 0.152.2`
     - Optional: `HUGO_ENV = production`

## 3) Set custom domain
- Add `gettheanchor.org` (or subdomain) under Pages → Custom domains
- Update DNS in Cloudflare (Pages automatically suggests CNAME records)

## 4) Redirect/Headers
- The `_headers` file in `static/` is compatible and will be deployed.

## 5) Asset & image strategy
- Keep Substack-hosted images if you want to offload bandwidth
- Or store images under `static/images/` and rely on Cloudflare’s global cache
- For advanced optimization: enable Cloudflare Polish/Resize (paid features), or use `images.gettheanchor.org` via Cloudflare Images

## 6) Local workflow
- Develop locally with `hugo server -D`
- Push to main when ready; Pages will build without metered per-deploy credits

## 7) Rollback plan
- Netlify site remains intact; you can flip DNS back if needed
- Keep both for a week to confirm parity

## 8) Optional: Branch previews
- Pages builds previews for PR branches; you can disable to save build time

## 9) Gotchas
- Pages uses Ubuntu images; if you use Hugo pipes (extended), ensure version is extended (Cloudflare uses extended by default when `HUGO_VERSION` is set)
- Ensure `relativeURLs = true` and paths use `relURL` helpers (already set)

## 10) Success criteria
- First build on Pages matches current Netlify build output
- DNS cutover with HTTPS active and zero downtime
- Subsequent pushes build successfully without per-deploy credit charges

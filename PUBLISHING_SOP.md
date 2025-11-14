# SOP: Publishing New Devotionals to gettheanchor.org

## Overview
---

## Environment & Prerequisites
- **Operating System:** Windows 10/11
- **Shell:** PowerShell
- **Site Source:** `hugo-site` subdirectory (Hugo v0.152.2)
- **Deployment:** Netlify (auto-deploys on push to `main` branch)
---
- **Content Location:** `hugo-site/content/devotionals/`


## Step-by-Step SOP & Checklist
  title: "Your Title"
  scripture: "Scripture Reference"
  readingTime: "X min read"
  featured: true
  ---
  ```
### 2. Create Websafe Images
- [ ] Place source image in `hugo-site/static/images/devotionals/`
  ```powershell
  # Example usage
  python ..\..\tools\create_websafe_image.py "input.jpg" "hugo-site/static/images/devotionals/your-image.webp"
  ```
- [ ] Confirm image is optimized and loads correctly
### 3. Preview Locally
- [ ] Open PowerShell
  cd hugo-site
  hugo server -D --disableFastRender
  # Visit http://localhost:1313
  ```

### 4. Commit & Push
  git add .
  git commit -m "Add new devotional: [Title]"
  git push origin main
  ```

- [ ] Wait 1-2 minutes for deployment
- [ ] Visit https://gettheanchor.org to verify post is live
---

## Verification Checklist
- [ ] Markdown file created with correct front matter
- [ ] Websafe image (.webp) created and referenced
- [ ] Local preview successful (formatting, images, metadata)
- [ ] All changes committed and pushed
- [ ] Post visible on live site

---

## Troubleshooting & Best Practices
- Preview locally before pushing
- For multiple posts, add all before pushing
- Rollback with `git revert` if needed
```powershell
```

date: 2025-11-14
scripture: "Hebrews 12:1-3"
readingTime: "12 min read"
featured: true
image: "/images/devotionals/running-endurance.webp"
excerpt: "How to keep going when the fight feels hard."
---

```

---
## Automation Scripts
- **End-of-Day Automation:**
  ```powershell
  # From the root directory
  powershell -ExecutionPolicy Bypass -File .\scripts\finalize.ps1 -CommitMessage "Add new devotional: [Title]"
  ```
- **Manual Workflow:**
  ```powershell
  git commit -m "Add new devotional: [Title]"
  git push origin main
  ```


## Summary
This SOP and checklist ensure all models and contributors follow a consistent, reliable process for publishing new devotionals to gettheanchor.org, including websafe image creation and verification steps.

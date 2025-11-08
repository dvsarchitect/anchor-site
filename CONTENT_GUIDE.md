# The Anchor - Content Management Guide

## Content Organization System

### Sections (Content Types)

Your site uses Hugo sections to organize different content types:

- **`devotionals/`** - Monday & Friday Bible studies
- **`articles/`** - Longer-form essays, cultural commentary
- **`social/`** - Twitter threads, quick takes, short posts
- **`series/`** - Multi-part deep dives

### Taxonomies (Filtering & Discovery)

#### Categories (Broad themes)
- Bible Study
- Cultural Commentary  
- Masculinity
- Faith & Politics
- Personal Reflections

#### Tags (Specific topics)
Flexible, add as needed:
- Prayer, Endurance, Armor of God
- Hebrews, Ephesians, Joshua
- Fatherhood, Marriage, Work
- Politics, Culture, Men

#### Series (Multi-part content)
Group related posts:
- "Armor of God Series"
- "Exodus Study"
- "Biblical Masculinity"

---

## Front Matter Template

```yaml
---
title: "Your Post Title"
date: 2025-11-08
type: "friday"  # monday | friday | article | social

# Taxonomy
categories: ["Bible Study", "Masculinity"]
tags: ["Hebrews", "Endurance", "Prayer"]
series: "Armor of God Series"  # Optional

# Display
scripture: "Hebrews 12:1-3"
featured: false
image: "https://substackcdn.com/image/fetch/..."
image_alt: "Descriptive alt text"
excerpt: "Short summary for cards and social sharing."

# Optional
social_source: "substack"  # twitter | facebook | substack
featured_quote: "Pullquote for social cards"
---
```

---

## Content Workflow

### Adding a New Post from Substack

1. **Create the file**
   ```powershell
   cd c:\Users\dvsar\Projects\the-anchor\hugo-site
   New-Item -Path "content\devotionals\your-slug.md" -ItemType File
   ```

2. **Add front matter** (see template above)

3. **Paste content** below the `---` closing

4. **Commit and push**
   ```powershell
   git add content/devotionals/your-slug.md
   git commit -m "content: add [Post Title]"
   git push
   ```

5. **Netlify auto-deploys** in ~1 minute

### Adding Social Media Content

For Twitter threads or Facebook posts:

```yaml
---
title: "Thread: Why Men Need the Church"
date: 2025-11-08
type: "social"
categories: ["Personal Reflections"]
tags: ["Church", "Community"]
social_source: "twitter"
excerpt: "A quick thread on why isolated faith doesn't work."
---

Thread content here...
```

### Creating a Series

1. **Add `series` to each post's front matter:**
   ```yaml
   series: "Armor of God Series"
   ```

2. **Hugo auto-generates:**
   - `/series/armor-of-god-series/` (list page)
   - Series navigation on single pages

---

## Future Features (Optional)

- **List templates** for articles, social, series sections
- **Tag/category archive pages** with filtering
- **Series navigation** (previous/next in series)
- **Related posts** based on tags/categories
- **Search** (Algolia or Pagefind)

---

## Quick Commands

### Create new devotional
```powershell
hugo new devotionals/my-post.md
```

### Create new article
```powershell
hugo new articles/my-article.md
```

### List all tags used
```powershell
hugo list all | Select-String "tags:"
```

---

## Best Practices

1. **Consistent naming:** Use lowercase slugs with hyphens
2. **Always add excerpt:** Improves cards and social sharing
3. **Tag strategically:** 3-5 tags per post, reuse existing tags
4. **Featured sparingly:** Only 1-2 posts featured at a time
5. **Images:** Substack CDN is fine; local images go in `static/images/`

---

## Questions?

This system scales from dozens to thousands of posts. Tags and categories make content discoverable. Series groups related studies. Sections keep different content types organized.

As your library grows, we can add:
- Archive pages by year/month
- Tag clouds
- Series indexes
- Full-text search

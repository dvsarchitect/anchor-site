# Homepage layout options

This document captures two layout variants for the homepage and the rationale behind each. Both emphasize clarity, content discovery, and conversion (subscribe).

## Variant A — Content-first (current baseline)

Order:
1. Banner image
2. Value proposition (title + subtitle + CTA)
3. Featured devotional (one highlighted card)
4. Latest tweets (social proof)
5. Recent devotionals (grid)
6. About
7. Subscribe panel

Pros:
- Clear focus on content freshness and Scripture-first message
- Social proof via X widget adds “alive” feel
- Lower friction to scroll and sample before subscribing

Cons:
- Subscribe is lower; conversion relies on CTA + footer
- Banner takes vertical space above the fold

When to use:
- Editorial cadence is a key part of the value
- You want readers to sample before committing

## Variant B — Conversion-first

Order:
1. Banner image (reduced height or full-bleed)
2. Value proposition with side-by-side subscribe embed (above the fold)
3. Featured devotional
4. Recent devotionals (grid)
5. Latest tweets (side column on desktop, stacked on mobile)
6. About

Pros:
- Subscribe is top-of-page on desktop
- Strong visual focus on becoming a subscriber

Cons:
- Slightly more complex layout on smaller screens
- Social proof is a bit lower

When to use:
- You want to maximize email list growth

## Visual polish / palette suggestions

- Keep primary text #1A1A1A; consider accent #2C5282 (current) or a deeper teal #1F5A7A for callouts
- Introduce a soft section background (#F7FAFC) alternating with white to create rhythm
- Subtle shadows (8–16px blur) only on interactive cards; keep hero clean
- Consider using system serif for titles + Inter for body (already in use)

## Navigation UX

- Use root-based hashes (/#about, /#subscribe) so menu links work globally
- On mobile, close menu on navigation and apply smooth scroll on home
- Keep logo clickable and readable at 40–48px with rounded square or circle

## Next steps

- If you want Variant B, I’ll draft a new `layouts/index_conversion.html` and wire a config flag to switch between them.
- Optionally add a full-bleed banner (edge-to-edge) with a subtle dark gradient to allow text overlay if desired.

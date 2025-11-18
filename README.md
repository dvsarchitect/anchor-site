# Hugo Site - The Anchor Website

This directory contains the source code and content for The Anchor's official Hugo static website.

## Purpose

This is the active development and deployment environment for the website. All changes made here directly impact the live website.

## Key Subdirectories

*   **`content/`:** All markdown content for the website pages and posts.
*   **`static/`:** Static assets like images, CSS, and JavaScript that are not processed by Hugo.
*   **`layouts/`:** HTML templates that define the structure and appearance of the website.
*   **`config.toml` / `hugo.toml`:** Main configuration files for the Hugo site.

## Getting Started

1.  **Install Hugo:** Follow the official Hugo documentation for installation.
2.  **Run Development Server:** `hugo server`
3.  **Build for Production:** `hugo`

## Deployment

This site is deployed via Netlify. Configuration is in `netlify.toml`.

---
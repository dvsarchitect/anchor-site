# Security Documentation for The Anchor Website

**Last Updated**: 2025-11-11
**Site**: getanchored.org (formerly gettheanchor.org)
**Hosting**: Netlify
**Framework**: Hugo Static Site Generator

---

## Security Status: GOOD ✓

This site is a static Hugo website with minimal attack surface. No database, no server-side processing, no user authentication.

---

## Current Security Measures

### 1. Static Architecture
- Hugo generates static HTML files
- No server-side code execution
- No database = no SQL injection risk
- All content pre-rendered at build time

### 2. No User Input
- No forms or user-submitted content
- No comment systems
- No search functionality requiring server processing
- Eliminates XSS via user input

### 3. JavaScript Security
- Clean, minimal JavaScript in `static/js/script.js`
- Proper encoding with `encodeURIComponent()` for URL parameters
- No use of dangerous functions: `eval()`, `innerHTML`, `dangerouslySetInnerHTML`
- Theme toggle uses safe localStorage access with try/catch

### 4. External Resources
- Google Fonts (preconnected with crossorigin)
- Twitter widgets (official Twitter CDN)
- YouTube embeds (iframe sandboxing)
- All from trusted, established CDNs

---

## Security Recommendations

### PRIORITY 1: Add Security Headers

**Current state**: Only caching headers exist in `static/_headers`

**Required addition**: Create/update `static/_headers` with:

```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://platform.twitter.com https://www.youtube.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; frame-src https://www.youtube.com https://platform.twitter.com; connect-src 'self'

/css/*
  Cache-Control: public, max-age=31536000, immutable

/js/*
  Cache-Control: public, max-age=31536000, immutable

/images/*
  Cache-Control: public, max-age=31536000

/fonts/*
  Cache-Control: public, max-age=31536000, immutable
```

**Why this matters**:
- **X-Frame-Options**: Prevents clickjacking attacks
- **X-Content-Type-Options**: Prevents MIME-type sniffing
- **CSP**: Defines allowed sources for scripts, styles, images
- **Referrer-Policy**: Controls referrer information leakage
- **Permissions-Policy**: Restricts browser features

### PRIORITY 2: HTTPS Enforcement

**Action**: Verify in Netlify Dashboard
1. Go to Domain Management → HTTPS
2. Ensure "Force HTTPS" is enabled
3. Verify SSL/TLS certificate is active

### PRIORITY 3: Dependency Monitoring

**Current**: No package.json or dependencies to monitor

**Action**: If you add npm packages in the future:
- Use `npm audit` regularly
- Enable Dependabot on GitHub
- Keep Hugo version updated (currently 0.152.2)

### PRIORITY 4: Content Security

**Hugo config.toml line 44**: `unsafe = true` for markdown rendering

**Why it exists**: Allows raw HTML in markdown files (needed for iframes, custom styling)

**Risk**: If someone gains write access to your content repo, they could inject malicious HTML

**Mitigation**:
- Keep GitHub repo private or restrict write access
- Review all content before publishing
- Consider moving to `unsafe = false` and use Hugo shortcodes instead

---

## Resource Limits & Optimization

### Current Usage (as of 2025-11-11)
- **Total repository**: 14MB
- **Static files**: 4.4MB
- **Built output**: 3.4MB
- **Total files**: 512
- **Images**: 9 files (1 PNG @ 1.8MB, rest WebP)

### Netlify Free Tier Limits
| Resource | Limit | Current Usage | Headroom |
|----------|-------|---------------|----------|
| Bandwidth | 100GB/month | ~1GB/month | 99GB |
| Build minutes | 300/month | ~5 min/month | 295 min |
| Storage | Unlimited | 4.4MB | Unlimited |
| Max deploy size | 125MB | 14MB | 111MB |

### Safe to Add
✅ **50-100MB of images** (optimize to WebP first)
✅ **PDFs and downloadable resources** (keep individual files <10MB)
✅ **JavaScript tools/calculators** (static only)
✅ **More devotional content** (minimal storage impact)
✅ **YouTube embeds** (no storage cost)

### Optimization Recommendations

**Image Optimization**:
```bash
# Install imagemagick or sharp
# Convert PNG to WebP (saves ~70% size)
convert when-the-world-feels-unreal.png -quality 80 when-the-world-feels-unreal.webp

# Or use Hugo's built-in image processing in templates:
{{ $image := resources.Get "images/devotionals/example.png" }}
{{ $webp := $image.Resize "800x webp q80" }}
<img src="{{ $webp.RelPermalink }}" alt="...">
```

**Current large files to optimize**:
- `static/images/devotionals/when-the-world-feels-unreal.png` (1.8MB)
- `static/images/devotionals/when-fight-feels-hard-new.png` (1.3MB)
- `static/images/banner.png` (1.2MB)

---

## Monitoring & Maintenance

### Regular Security Checks

**Monthly**:
- [ ] Review Netlify deploy logs for errors
- [ ] Check Netlify Analytics for unusual traffic patterns
- [ ] Verify HTTPS certificate hasn't expired (auto-renewed by Netlify)

**Quarterly**:
- [ ] Update Hugo version in `netlify.toml`
- [ ] Review and update security headers
- [ ] Audit external script sources (Twitter, YouTube, Google Fonts)
- [ ] Run Lighthouse security audit

**Annually**:
- [ ] Review CSP policy for overly permissive rules
- [ ] Check for deprecated HTML/CSS/JS usage
- [ ] Evaluate new security header standards

### Tools for Security Testing

```bash
# Run Hugo's built-in server with security headers
hugo server --appendPort=false

# Check for broken links
hugo --gc --minify && find public -name "*.html" -exec grep -l 'href=' {} \;

# Lighthouse CI for security audit
npm install -g @lhci/cli
lhci autorun --collect.url=https://getanchored.org
```

**Online Tools**:
- [Mozilla Observatory](https://observatory.mozilla.org/) - Security header checker
- [SecurityHeaders.com](https://securityheaders.com/) - Header analysis
- [SSL Labs](https://www.ssllabs.com/ssltest/) - SSL/TLS configuration

---

## Incident Response

### If Compromised

**Signs of compromise**:
- Unexpected changes in GitHub repo
- Netlify deploy triggered without your action
- Unusual traffic patterns in Netlify Analytics
- Site content changed without authorization

**Immediate actions**:
1. **Revoke access**: Reset GitHub tokens, revoke Netlify API keys
2. **Review logs**: Check Netlify deploy logs and GitHub commit history
3. **Rollback**: Use Netlify's instant rollback feature to previous good deploy
4. **Audit**: Review all content files for malicious injections
5. **Enable 2FA**: On GitHub and Netlify accounts if not already enabled

### Contact Information
- **GitHub Support**: https://support.github.com/
- **Netlify Support**: https://www.netlify.com/support/
- **Domain Registrar**: [Add your registrar support link]

---

## Development Workflow Security

### Git Security
```bash
# Never commit sensitive data
# Add to .gitignore:
.env
.env.local
*.key
*.pem
secrets/
```

### Local Development
```bash
# Use Hugo's development server (not production)
hugo server -D

# Build for production (minified, secure)
hugo --gc --minify
```

### Pre-Deploy Checklist
- [ ] No hardcoded API keys or secrets
- [ ] All images optimized (WebP preferred)
- [ ] No console.log() statements in production JS
- [ ] All external links use `rel="noopener"` or `rel="noreferrer"`
- [ ] Social media embeds use official widgets only

---

## Notes

- **Hugo's `unsafe = true`**: Necessary for Substack embeds and YouTube iframes. Acceptable risk given controlled content.
- **No CDN integrity hashes**: Google Fonts don't provide SRI hashes; trusted source acceptable.
- **Twitter widget**: Loads external script but from official Twitter CDN with async loading.

---

## Additional Resources

- [Hugo Security Model](https://gohugo.io/about/security-model/)
- [Netlify Security](https://docs.netlify.com/security/secure-access-to-sites/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [Content Security Policy Reference](https://content-security-policy.com/)

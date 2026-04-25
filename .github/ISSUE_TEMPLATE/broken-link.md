---
name: Broken link
about: Report a URL in this repo that 404s, redirects to junk, or no longer resolves
title: "[broken-link] "
labels: broken-link
---

## Where

- **File:** `path/to/file.md`
- **Line (approx.):**
- **Broken URL:**

## What happens

<!-- e.g. "404 Not Found", "redirects to a parked domain", "loads but the content is gone" -->

## Suggested replacement (optional)

<!-- Link to the new location if you know it. -->

## How to verify

```bash
curl -I '<url>'
```

<!-- Notes for maintainers: link-check workflow runs every Monday and on PRs touching .md files. -->

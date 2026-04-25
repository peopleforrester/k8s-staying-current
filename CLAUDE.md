# k8s staying current

Companion repository for the KubeCon EU 2026 talk *"How Kubernetes Actually Ships: An Educator's Guide to Core Releases, SIGs, and Staying Current"* — Mumshad Mannambeth & Michael Forrester (KodeKloud), delivered Tuesday, March 24, 2026.

**Stack:** Documentation / Markdown.

## Purpose

A living reference for Kubernetes practitioners staying current after certification. Curated, not exhaustive — every link, tool, and channel listed must be verified working at the time of the most recent commit touching it.

## Editorial Standards

- **Tone:** practical, concise, no marketing language. Match the voice already established in `README.md` and `channels/essential-five.md`.
- **Factual sourcing:** every non-obvious factual claim links to an official source (kubernetes.io, cncf.io, GitHub, mailing list archives). No second-hand recaps without a primary link.
- **No vendor promotion.** Tools are listed because they solve a problem, not because of relationships.
- **Verified stamps.** Every file under `reference/` carries an HTML comment of the form `<!-- Verified: YYYY-MM-DD — ... -->` near the top. When a fact in that file is re-verified, bump the date. When a fact is updated, the comment moves to the new date in the same edit.
- **Date hygiene.** When you update content that mentions "as of" a date, also update the README disclaimer (line 16), the README footer "Content current as of" line, and the verified badge on line 4. The verification script asserts the README disclaimer is within 30 days of the current date.

## Repository Layout

See README.md "Repository Map" — that map is canonical. Update it whenever a directory's contents change.

## Verification Harness

`scripts/verify_repo.py` encodes every editorial invariant we care about and exits 0 when the repo is clean. `tests/test_verify_repo.py` is the pytest wrapper. Run before every commit:

```bash
python scripts/verify_repo.py
```

When you add a new editorial rule, add a corresponding check (`v18_*`) to the script first, watch it fail, then make it pass — TDD applies to docs too.

## Talk Archive Policy

The active talk script lives at `talk/script.md` (gitignored — internal-only). After a talk has been delivered, rename to `talk/YYYY-MM-DD-script.md` to preserve the historical record. Update `.gitignore` if the archived script should remain private.

## Branching

- All work happens on `staging`. Direct pushes to `main` are blocked by branch protection.
- Merges to `main` require the link-check workflow (under `.github/workflows/link-check.yml`) to be green.

## What Not to Do

- Don't add subjective "best of" rankings. The repo is a directory of verified resources, not a leaderboard.
- Don't introduce content for events that haven't happened yet. Future events live in `PROJECT_STATE.md` (gitignored) until they occur.
- Don't trust training data or stale tool output for version numbers, dates, or membership lists. Always verify against the source linked in the file's `Verified:` comment.

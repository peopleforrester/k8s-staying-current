<!-- ABOUTME: Phased plan to resolve issues raised by the post-talk senior review. -->
<!-- ABOUTME: TDD: a verification script encodes each issue as an assertion; phases drive it green. -->

# Post-Talk Cleanup Plan

This plan addresses every finding from the post-talk senior review of `k8s-staying-current`. It is organised by priority (P0–P3) and executed phase-by-phase. No timelines — each phase ships when its tests pass.

## Method: TDD for Documentation

Documentation has tests. They live in `scripts/verify_repo.py` and assert observable properties of the repo (file presence, string contents, date stamps). The workflow:

1. Encode each review finding as one or more failing assertions in the verification script.
2. Run the script; confirm every relevant assertion fails.
3. Make the smallest change that turns one assertion green. Re-run.
4. Repeat until the script exits 0.
5. Commit per phase to `staging`. Never push directly to `main`.

The script exits non-zero on any failure and prints a checklist of what's pending. It is the source of truth — not this document.

## Out of Scope (Pending Michael's Decision)

These items from the review need a call before action and will not be auto-applied:

- **QR code resize to 512×512.** Mobile phones already scan the 164×164 PNG; resizing requires a regenerator script and a paper-trail decision.
- **Adding `r/kubernetes` to `channels/`.** The talk did not call it out; adding it expands editorial scope.
- **Transferring repo to KodeKloud org.** Tracked in `PROJECT_STATE.md` as a pending org transfer; not a content fix.
- **Slide-deck binary canonical version.** The plan deletes the stray `v8` Windows-download artifact and keeps the tracked `v14`. If `v8` is actually the post-talk refreshed deck, Michael should say so before Phase 1 runs — see Phase 1 step 1.

## Phase 0 — Verification Harness (TDD)

Add `scripts/verify_repo.py` and `tests/test_verify_repo.py`.

`verify_repo.py` checks:

| ID  | Assertion                                                                 | Source review item |
|-----|---------------------------------------------------------------------------|--------------------|
| V1  | No `slides/kubecon-cnu-stage-deck-v8.pptx` (or sidecar) in working tree   | #2 |
| V2  | No `*:Zone.Identifier` files anywhere                                     | #2 |
| V3  | `PROJECT_STATE.md` exists locally and references talk in past tense       | #3 |
| V4  | `CONTRIBUTING.md` line 4 uses "How Kubernetes Actually Ships" title       | #6 |
| V5  | `channels/social-media.md` uses "Official" not "Primary" as the heading   | #5 |
| V6  | `what-changed-2025/2025-landscape-changes.md` says "official" not "primary social channel" | #5 |
| V7  | `reference/release-calendar.md` shows v1.36 as **released** (Apr 22 2026, "Haru"), not target | #8 |
| V8  | `reference/release-calendar.md` "Current Support Window" shows v1.33 oldest, v1.32 EOL'd | #8 |
| V9  | `README.md` disclaimer date is within 30 days of file mtime               | #7 |
| V10 | `.gitignore` does not contain the dead `!slides/*.pptx` line              | #9 |
| V11 | Slide deck file referenced in `README.md` repo map exists on disk         | #4, #2 |
| V12 | `CLAUDE.md` is not stub-length (>= 30 lines, mentions editorial standards)| #12 |
| V13 | Each `reference/*.md` has a `<!-- Verified: YYYY-MM-DD -->` header        | #14 |
| V14 | `.github/workflows/link-check.yml` exists                                 | #11 |
| V15 | `.github/ISSUE_TEMPLATE/` has at least `broken-link.md` and `outdated-fact.md` | #19 |
| V16 | `CONTRIBUTING.md` mentions CC BY 4.0 license for contributions            | #17 |
| V17 | `talk/script.md` is either gitignored OR archived under a dated filename  | #10 |

Each assertion prints `PASS`/`FAIL` with the file path and a one-line explanation.

`tests/test_verify_repo.py` is a thin pytest wrapper that asserts the script exits 0. CI can run either.

**Exit criteria:** Script runs end-to-end (no crashes). All P0/P1/P2/P3-bound checks fail with clear messages. Tests fail with a known failure list.

## Phase 1 — P0 Critical Fixes

Drives V1, V2, V3 green.

1. **Slide deck resolution.** Default action: delete `slides/kubecon-cnu-stage-deck-v8.pptx` and its `:Zone.Identifier` sidecar; keep `slides/k8s-staying-current-stage-deck-v14.pptx` as the canonical deck (already tracked, matches README map). If Michael identifies `v8` as the post-talk refreshed deck instead, swap: track v8, delete v14. Phase pauses for confirmation if there is any doubt.
2. **Zone.Identifier sweep.** `find . -name '*:Zone.Identifier' -delete` (already covered by `.gitignore`, but the existing file pre-dates that rule).
3. **Rewrite `PROJECT_STATE.md`.** Convert pre-talk checklist to post-talk record:
   - Status: post-talk, content-maintenance phase.
   - What was verified during the talk week (kept as historical record).
   - Outstanding follow-ups: org transfer, link-check automation, holdover-seat re-check, deck retention policy.
   - File stays gitignored (private to local working copy) — the existing `.gitignore` rule is intentional per commit `3f57655`.

**Exit criteria:** V1, V2, V3 green.

## Phase 2 — P1 High Priority Fixes

Drives V4–V10 green.

1. **`CONTRIBUTING.md` title drift** — line 4 → "How Kubernetes Actually Ships: An Educator's Guide to Core Releases, SIGs, and Staying Current".
2. **Bluesky wording reconciliation.**
   - `channels/social-media.md` heading "Primary: Bluesky" → "Official: Bluesky" (matching the talk-prep correction in `talk/script.md:386`).
   - `what-changed-2025/2025-landscape-changes.md` line 35: "Bluesky is the primary official social channel" → "Bluesky is an official social channel (listed before X on kubernetes.io/community)".
   - "Promoted to primary official channel" row in same file → "Listed first on kubernetes.io/community as official channel".
   - Cross-check `README.md` 2025-landscape table: already says "Bluesky is official" — leave.
3. **Release calendar update.** v1.36 shipped April 22, 2026, codename **Haru**. Per official blog. Update:
   - Table line 15: change "Apr 22, 2026 (target)" → "Apr 22, 2026" and codename TBD → **Haru**.
   - "Current Support Window" table line 36 → drop v1.32, mark v1.33 as oldest supported.
   - Statement line 38 → "v1.36 (Haru) shipped April 22, 2026; v1.33 is now the oldest supported version."
   - HTML provenance comment: bump verified date to today.
4. **README disclaimer.** Update lines 4 (badge), 16, 260 → today's verification date. Re-state the maintenance commitment: dates auto-checked by CI is the goal in Phase 3.
5. **`.gitignore` cleanup.** Delete the dead `!slides/*.pptx` negation (no positive pattern matches `.pptx`, so this line is a no-op). Keep the `*:Zone.Identifier` rule.

**Exit criteria:** V4–V10 green. Manual spot-check: rendered README on a mock GitHub viewer (or `glow`) shows correct dates.

## Phase 3 — P2 Medium Priority Improvements

Drives V12, V13, V14, V15 green.

1. **CLAUDE.md expansion.** Encode editorial standards:
   - Tone: practical, concise, no marketing.
   - Factual sourcing: link official sources for claims.
   - "Last verified" stamp policy for `reference/`.
   - "When you change a date, update all date stamps" rule.
   - Talk archive policy: dated filename per year (`talk/2026-03-24-script.md`).
2. **`reference/*.md` "Verified:" headers.** Add an HTML comment immediately after the H1 of each file: `<!-- Verified: 2026-04-26 — see verify_repo.py -->`. Files: `all-24-sigs.md`, `cncf-tags.md`, `governance-quick-ref.md`, `release-calendar.md`, `working-groups.md`.
3. **Link-check workflow.** Add `.github/workflows/link-check.yml` running `lychee-action` weekly + on PR. Fails on broken links. Open issues automatically on schedule failure.
4. **Issue templates.** `.github/ISSUE_TEMPLATE/broken-link.md` and `.github/ISSUE_TEMPLATE/outdated-fact.md`. Each has a `--` frontmatter block, prompt fields for URL/file path, and label assignment.
5. **TOC holdover re-verify.** Web-check current TOC membership; if no replacement elections have shipped, bump the "Note (April 2026)" stamp to today's check date. If they have shipped, update the table.

**Exit criteria:** V12–V15 green. Workflow YAML lints clean (`actionlint` if available).

## Phase 4 — P3 Polish

Drives V16, V17 green.

1. **`CONTRIBUTING.md` license notice.** Add a "License" section: "By contributing, you agree your contribution is licensed under CC BY 4.0 (matching the repository LICENSE)."
2. **Talk script archival.** `git mv talk/script.md talk/2026-03-24-script.md` (locally only — the file is gitignored). Update `.gitignore` to include `talk/*.md` so future scripts stay private by default. Drop the specific `talk/script.md` rule.

Skipped (per Out of Scope): QR resize, r/kubernetes, KodeKloud org transfer.

**Exit criteria:** V16, V17 green. Verification script exits 0.

## Final — Commit & Push

1. Confirm each phase has its own commit on `staging`. Suggested messages:
   - `Add post-talk cleanup plan and verification harness`
   - `Resolve P0: drop stray v8 deck, refresh PROJECT_STATE post-talk`
   - `Resolve P1: title, Bluesky wording, v1.36 Haru shipped, dates`
   - `Resolve P2: CLAUDE.md standards, verified stamps, link-check CI, issue templates`
   - `Resolve P3: contributor license note, archive talk script`
2. Run `python scripts/verify_repo.py` — must exit 0.
3. `git push origin staging`. **Do not** merge to `main` in this session — wait for CI link-check to pass.
4. Open PR `staging → main` separately when ready.

## Findings Not Acted On (with rationale)

- **Senior review #4 (deck version confusion across files):** the v7/v8 reference in `talk/script.md:434` lives in a gitignored file. Updating it improves the historical record but isn't required for public-facing consistency; addressed in Phase 4 archival rename.
- **Senior review #9 (PROJECT_STATE.md / talk/script.md tracked in git):** false claim. Both were intentionally untracked in commits `ba0206a` and `3f57655`. The dead negation in `.gitignore` is the only real bug there, fixed in Phase 2.
- **Senior review #11 (no link check):** this is genuinely missing; addressed in Phase 3.
- **Senior review #18 ("24 SIGs" count unverified):** addressed by the V13 "Verified:" header policy in Phase 3.
- **Senior review #20 (Reddit absent):** flagged in Out of Scope. Editorial decision for Michael.

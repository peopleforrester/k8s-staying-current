#!/usr/bin/env python3
# ABOUTME: Verification harness for k8s-staying-current. Each check encodes a finding from
# ABOUTME: the post-talk senior review. Exits 0 only when all checks pass. See docs/post-talk-cleanup-plan.md.

from __future__ import annotations

import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable, List, Tuple

REPO = Path(__file__).resolve().parent.parent

# A check returns (passed, message). The message is shown either way.
Check = Tuple[str, Callable[[], Tuple[bool, str]]]


def _read(rel: str) -> str:
    return (REPO / rel).read_text(encoding="utf-8")


def _exists(rel: str) -> bool:
    return (REPO / rel).exists()


# ---------- P0 ----------

def v1_no_v8_deck() -> Tuple[bool, str]:
    p = REPO / "slides" / "kubecon-cnu-stage-deck-v8.pptx"
    if p.exists():
        return False, f"stray deck still present: {p.relative_to(REPO)}"
    return True, "no stray v8 deck"


def v2_no_zone_identifier() -> Tuple[bool, str]:
    hits = list(REPO.rglob("*:Zone.Identifier"))
    hits = [h for h in hits if ".git" not in h.parts]
    if hits:
        return False, f"Zone.Identifier files: {[str(h.relative_to(REPO)) for h in hits]}"
    return True, "no Zone.Identifier sidecars"


def v3_project_state_post_talk() -> Tuple[bool, str]:
    p = REPO / "PROJECT_STATE.md"
    if not p.exists():
        return False, "PROJECT_STATE.md missing"
    text = p.read_text(encoding="utf-8")
    if "Pre-Talk Checklist" in text:
        return False, "PROJECT_STATE.md still contains pre-talk checklist"
    if not re.search(r"(post[- ]talk|talk delivered|talk complete)", text, re.IGNORECASE):
        return False, "PROJECT_STATE.md does not mention post-talk status"
    return True, "PROJECT_STATE.md reflects post-talk reality"


# ---------- P1 ----------

def v4_contributing_title() -> Tuple[bool, str]:
    text = _read("CONTRIBUTING.md")
    if "How Kubernetes Actually Ships" not in text:
        return False, "CONTRIBUTING.md missing current talk title"
    if "Every Channel You Need" in text:
        return False, "CONTRIBUTING.md still references old talk title"
    return True, "CONTRIBUTING.md uses current title"


def v5_bluesky_heading() -> Tuple[bool, str]:
    text = _read("channels/social-media.md")
    if re.search(r"^##\s*Primary:\s*Bluesky", text, re.MULTILINE):
        return False, "channels/social-media.md still has '## Primary: Bluesky' heading"
    if not re.search(r"^##\s*Official:\s*Bluesky", text, re.MULTILINE):
        return False, "channels/social-media.md missing '## Official: Bluesky' heading"
    return True, "Bluesky heading uses 'Official'"


def v6_landscape_bluesky_wording() -> Tuple[bool, str]:
    text = _read("what-changed-2025/2025-landscape-changes.md")
    if "primary official social channel" in text.lower():
        return False, "2025-landscape-changes.md still says 'primary official social channel'"
    if "Promoted to primary official channel" in text:
        return False, "2025-landscape-changes.md table still says 'Promoted to primary official'"
    return True, "landscape doc uses 'official' wording"


def v7_v136_released() -> Tuple[bool, str]:
    text = _read("reference/release-calendar.md")
    if "Apr 22, 2026 (target)" in text or "Apr 22, 2026** (target)" in text:
        return False, "release-calendar.md still marks v1.36 as target"
    if "Haru" not in text:
        return False, "release-calendar.md missing v1.36 codename 'Haru'"
    return True, "release-calendar.md shows v1.36 (Haru) shipped"


def v8_support_window_v133_oldest() -> Tuple[bool, str]:
    text = _read("reference/release-calendar.md")
    # Once v1.36 has shipped, the "Current Support Window" table should not list v1.32
    # at all (it's EOL'd) and should list v1.36.
    section = re.search(
        r"### Current Support Window.*?(?=^---|^##|\Z)", text, re.DOTALL | re.MULTILINE
    )
    if not section:
        return False, "Current Support Window section missing"
    block = section.group(0)
    if re.search(r"\|\s*v1\.32\s*\|", block):
        return False, "Support Window still has a v1.32 row (should be removed post-EOL)"
    if "v1.36" not in block:
        return False, "Support Window does not yet list v1.36"
    return True, "Support window reflects v1.36 shipped, v1.33 oldest"


def v9_readme_disclaimer_fresh() -> Tuple[bool, str]:
    text = _read("README.md")
    m = re.search(r"current as of ([A-Z][a-z]+ \d{1,2},\s*\d{4})", text)
    if not m:
        return False, "README.md disclaimer date not found"
    try:
        d = datetime.strptime(m.group(1).replace(",", ""), "%B %d %Y").date()
    except ValueError:
        return False, f"could not parse disclaimer date: {m.group(1)}"
    age = (date.today() - d).days
    if age > 30:
        return False, f"README disclaimer date is {age} days old (> 30)"
    return True, f"README disclaimer date is {age} days old"


def v10_gitignore_no_dead_rule() -> Tuple[bool, str]:
    text = _read(".gitignore")
    if "!slides/*.pptx" in text:
        return False, ".gitignore still contains dead '!slides/*.pptx' negation"
    return True, ".gitignore has no dead negations"


def v11_readme_deck_exists() -> Tuple[bool, str]:
    text = _read("README.md")
    pptx_refs = re.findall(r"([\w\-.]+\.pptx)", text)
    if not pptx_refs:
        return False, "README.md does not reference any .pptx file"
    missing = [name for name in pptx_refs if not (REPO / "slides" / name).exists()]
    if missing:
        return False, f"README references missing decks: {missing}"
    return True, f"README deck reference(s) resolve: {pptx_refs}"


# ---------- P2 ----------

def v12_claude_md_substantive() -> Tuple[bool, str]:
    text = _read("CLAUDE.md")
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) < 15:
        return False, f"CLAUDE.md has only {len(lines)} non-blank lines (< 15)"
    if not re.search(r"editorial|tone|factual|verified", text, re.IGNORECASE):
        return False, "CLAUDE.md missing editorial-standards content"
    return True, f"CLAUDE.md is substantive ({len(lines)} non-blank lines)"


def v13_reference_verified_stamps() -> Tuple[bool, str]:
    missing = []
    for f in (REPO / "reference").glob("*.md"):
        text = f.read_text(encoding="utf-8")
        if not re.search(r"<!--\s*Verified:\s*\d{4}-\d{2}-\d{2}", text):
            missing.append(f.name)
    if missing:
        return False, f"reference files missing Verified stamp: {missing}"
    return True, "all reference/*.md files have Verified stamps"


def v14_link_check_workflow() -> Tuple[bool, str]:
    p = REPO / ".github" / "workflows" / "link-check.yml"
    if not p.exists():
        return False, ".github/workflows/link-check.yml missing"
    text = p.read_text(encoding="utf-8")
    if "lychee" not in text.lower() and "markdown-link-check" not in text.lower():
        return False, "link-check workflow exists but uses no known link-checker"
    return True, "link-check workflow present"


def v15_issue_templates() -> Tuple[bool, str]:
    base = REPO / ".github" / "ISSUE_TEMPLATE"
    needed = ["broken-link.md", "outdated-fact.md"]
    missing = [n for n in needed if not (base / n).exists()]
    if missing:
        return False, f"missing issue templates: {missing}"
    return True, "issue templates present"


# ---------- P3 ----------

def v16_contributing_license_notice() -> Tuple[bool, str]:
    text = _read("CONTRIBUTING.md")
    if not re.search(r"CC BY 4\.0", text):
        return False, "CONTRIBUTING.md missing CC BY 4.0 contributor notice"
    return True, "CONTRIBUTING.md has CC BY 4.0 notice"


def v17_talk_script_archived_or_ignored() -> Tuple[bool, str]:
    # Either talk/script.md doesn't exist (renamed to dated form),
    # OR it's listed in .gitignore (private until archive).
    script_present = (REPO / "talk" / "script.md").exists()
    archive = list((REPO / "talk").glob("*-script.md"))
    gi = _read(".gitignore")
    if script_present and "talk/script.md" not in gi and "talk/*.md" not in gi:
        return False, "talk/script.md present but not gitignored or archived"
    if not script_present and not archive:
        return False, "no talk script and no dated archive"
    return True, "talk script gitignored or archived"


CHECKS: List[Check] = [
    ("V1  no stray v8 deck", v1_no_v8_deck),
    ("V2  no Zone.Identifier sidecars", v2_no_zone_identifier),
    ("V3  PROJECT_STATE.md is post-talk", v3_project_state_post_talk),
    ("V4  CONTRIBUTING title current", v4_contributing_title),
    ("V5  Bluesky heading 'Official'", v5_bluesky_heading),
    ("V6  landscape doc 'official' wording", v6_landscape_bluesky_wording),
    ("V7  v1.36 Haru shipped", v7_v136_released),
    ("V8  support window correct", v8_support_window_v133_oldest),
    ("V9  README disclaimer fresh", v9_readme_disclaimer_fresh),
    ("V10 .gitignore no dead rule", v10_gitignore_no_dead_rule),
    ("V11 README deck file exists", v11_readme_deck_exists),
    ("V12 CLAUDE.md substantive", v12_claude_md_substantive),
    ("V13 reference Verified stamps", v13_reference_verified_stamps),
    ("V14 link-check workflow", v14_link_check_workflow),
    ("V15 issue templates", v15_issue_templates),
    ("V16 CONTRIBUTING CC BY 4.0", v16_contributing_license_notice),
    ("V17 talk script archived/ignored", v17_talk_script_archived_or_ignored),
]


def main() -> int:
    failures = 0
    print(f"Running {len(CHECKS)} checks against {REPO}\n")
    for label, fn in CHECKS:
        try:
            ok, msg = fn()
        except Exception as exc:
            ok, msg = False, f"check raised {type(exc).__name__}: {exc}"
        marker = "PASS" if ok else "FAIL"
        print(f"  [{marker}] {label}: {msg}")
        if not ok:
            failures += 1
    print(f"\n{len(CHECKS) - failures}/{len(CHECKS)} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate repository structure, links, metadata, and hygiene.

Uses only the Python standard library and makes no network requests.
Usage: python3 scripts/validate.py [repo_root]  (default: the repository containing this script)
Exit status is 0 when all checks pass and 1 otherwise.
"""

import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from check_skill import check_skill_dir

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTENT_LICENSE.md",
    "NOTICE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "MAINTENANCE.md",
    ".gitignore",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/documentation-issue.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "docs/getting-started.md",
    "docs/delegating-a-task.md",
    "docs/before-you-delegate.md",
    "examples/before-you-delegate/inputs/room-booking.md",
    "examples/before-you-delegate/inputs/coordinator-update.md",
    "examples/before-you-delegate/expected-brief.md",
    "docs/permissions-and-modes.md",
    "docs/scheduled-tasks-and-remote-access.md",
    "docs/instructions-projects-and-memory.md",
    "docs/skills.md",
    "docs/plugins.md",
    "docs/browser-and-computer-use.md",
    "docs/microsoft-365.md",
    "docs/safety.md",
    "docs/team-and-enterprise.md",
    "docs/troubleshooting.md",
    "exercises/README.md",
    "resources/official-links.md",
    "resources/sources-and-verification.md",
    "scripts/check_skill.py",
]

DISCLAIMER = (
    "Independent educational resource. Not affiliated with, sponsored by, or "
    "endorsed by Anthropic or Claude Academy. Claude and associated product "
    "names belong to their respective owners."
)

EXERCISE_HEADINGS = [
    "Objective",
    "Prerequisites",
    "Input data",
    "Copy-ready prompt",
    "Expected result characteristics",
    "Verification checklist",
    "Common failure modes",
    "Follow-up",
]
MIN_EXERCISES = 5

ALLOWED_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".csv", ".txt", ""}
ALLOWED_NO_SUFFIX = {"LICENSE", ".gitignore"}

# Patterns are written so that this file does not match its own checks.
HYGIENE_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    "Anthropic API key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}"),
    "AWS access key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "home directory path": re.compile(r"/(?:Users|home)/[a-z][a-z0-9_.-]+/", re.I),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[A-Za-z]", re.I),
    "AI co-author trailer": re.compile(r"Co-Authored-[B]y:", re.I),
    "AI generation attribution": re.compile(r"Generated (?:with|by) \[?Claude", re.I),
    "personal email address": re.compile(
        r"\b[A-Za-z0-9._-]+@(?:gmail|icloud|outlook|hotmail|yahoo)\.com\b"
    ),
}

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
EM_DASH = "\u2014"
PROSE_EXEMPT = {"CONTENT_LICENSE.md"}
FENCE = re.compile(r"^\s*```")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REF_DEF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)", re.M)
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".csv", ".txt"}
DATE = re.compile(r"^Last reviewed: \d{4}-\d{2}-\d{2}\s*$", re.M)


def _git_files(root: Path):
    """Tracked plus untracked-but-not-ignored files, or None outside a checkout."""
    if not (root / ".git").exists():
        return None
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            capture_output=True, check=True, timeout=30,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    return [root / n for n in out.decode("utf-8").split("\0") if n]


def list_candidates(root: Path):
    listed = _git_files(root)
    if listed is None:
        listed = root.rglob("*")
    return [
        path for path in sorted(listed)
        if not (set(path.relative_to(root).parts) & SKIP_DIRS)
    ]


def list_files(root: Path):
    return (path for path in list_candidates(root) if not path.is_symlink() and path.is_file())


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def strip_fences(text: str) -> str:
    out, inside = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def heading_slugs(text: str) -> set:
    """GitHub-style anchors, including the -1, -2 suffixes for repeated headings."""
    slugs = set()
    for line in strip_fences(text).splitlines():
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            s = re.sub(r"[^\w\- ]", "", m.group(1).lower()).strip().replace(" ", "-")
            slug, suffix = s, 0
            while slug in slugs:
                suffix += 1
                slug = f"{s}-{suffix}"
            slugs.add(slug)
    return slugs


def check_required_files(root: Path, required=REQUIRED_FILES):
    return [f"missing required file: {f}" for f in required if not (root / f).is_file()]


def check_disclaimer(root: Path):
    errors = []
    for name in ("README.md", "NOTICE.md"):
        path = root / name
        if path.is_file():
            flat = " ".join(path.read_text(encoding="utf-8").split())
            if DISCLAIMER not in flat:
                errors.append(f"{name}: disclaimer text missing or altered")
    return errors


def check_links(root: Path):
    root = root.resolve()
    errors = []
    for path in list_files(root):
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        body = strip_fences(text)
        for target in LINK.findall(body) + REF_DEF.findall(body):
            target = target.strip("<>")
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # external or mailto; not checked offline
            file_part, _, anchor = target.partition("#")
            file_part = unquote(file_part)
            if file_part.startswith("/"):
                dest = (root / file_part.lstrip("/")).resolve()
            else:
                dest = path if not file_part else (path.parent / file_part).resolve()
            if file_part and not dest.is_relative_to(root):
                errors.append(f"{rel(path, root)}: link leaves the repository {target}")
                continue
            if file_part and not dest.exists():
                errors.append(f"{rel(path, root)}: broken link {target}")
                continue
            if anchor and dest.suffix == ".md" and dest.is_file():
                if unquote(anchor).lower() not in heading_slugs(dest.read_text(encoding="utf-8")):
                    errors.append(f"{rel(path, root)}: missing anchor {target}")
    return errors


def check_prose_style(root: Path):
    """Reject the em dash in authored text files. Third-party license text is exempt."""
    errors = []
    for path in list_files(root):
        if path.suffix not in TEXT_SUFFIXES or path.name in PROSE_EXEMPT:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if EM_DASH in line:
                errors.append(f"{rel(path, root)}:{number}: em dash; use a period, comma, colon, or parentheses")
    return errors


def check_review_dates(root: Path):
    errors = []
    for folder in ("docs", "exercises", "resources"):
        for path in sorted((root / folder).glob("*.md")):
            if not DATE.search(path.read_text(encoding="utf-8")):
                errors.append(f"{rel(path, root)}: missing 'Last reviewed: YYYY-MM-DD' line")
    return errors


def check_docs_have_reference(root: Path):
    errors = []
    for path in sorted((root / "docs").glob("*.md")):
        if "## Official reference" not in path.read_text(encoding="utf-8"):
            errors.append(f"{rel(path, root)}: missing '## Official reference' section")
    return errors


def check_exercises(root: Path):
    errors = []
    files = sorted(p for p in (root / "exercises").glob("[0-9][0-9]-*.md"))
    if len(files) < MIN_EXERCISES:
        errors.append(f"exercises: found {len(files)}, need at least {MIN_EXERCISES}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        for heading in EXERCISE_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(heading)}\b", text, re.M):
                errors.append(f"{rel(path, root)}: missing section '{heading}'")
    index = root / "exercises" / "README.md"
    if index.is_file():
        body = index.read_text(encoding="utf-8")
        for path in files:
            if f"]({path.name})" not in body:
                errors.append(f"exercises/README.md: does not link {path.name}")
    return errors


def check_duplicates(root: Path):
    errors = []
    seen = {}
    paragraphs = {}
    for path in list_files(root):
        if path.suffix != ".md" or path.name in ("CONTENT_LICENSE.md",):
            continue
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest in seen:
            errors.append(f"duplicate file content: {rel(path, root)} == {seen[digest]}")
        seen[digest] = rel(path, root)
        for para in strip_fences(data.decode("utf-8")).split("\n\n"):
            norm = " ".join(para.split())
            if len(norm) >= 200 and not norm.startswith("|"):
                first = paragraphs.setdefault(norm, rel(path, root))
                if first != rel(path, root):
                    errors.append(
                        f"duplicated paragraph in {rel(path, root)} and {first}: {norm[:50]}..."
                    )
    return errors


def check_code(root: Path):
    errors = []
    for path in list_files(root):
        name = rel(path, root)
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(f"{name}: Python syntax error: {exc}")
        elif path.suffix == ".md":
            lines = path.read_text(encoding="utf-8").splitlines()
            lang, buf, start = None, [], 0
            for i, line in enumerate(lines, 1):
                if FENCE.match(line):
                    if lang is None:
                        info = line.strip()[3:].strip().lower().split()
                        lang = info[0] if info else ""
                        buf, start = [], i
                    else:
                        errors += _check_block(name, lang, "\n".join(buf), start)
                        lang = None
                elif lang is not None:
                    buf.append(line)
            if lang is not None:
                errors.append(f"{name}:{start}: unclosed code fence")
    return errors


def _check_block(name, lang, code, line):
    try:
        if lang in ("python", "py"):
            ast.parse(code)
        elif lang == "json":
            json.loads(code)
    except (SyntaxError, ValueError) as exc:
        return [f"{name}:{line}: invalid {lang} block: {exc}"]
    return []


def check_symlinks(root: Path):
    return [
        f"{rel(path, root)}: symbolic links are not allowed"
        for path in list_candidates(root)
        if path.is_symlink()
    ]


def check_hygiene(root: Path):
    errors = check_symlinks(root)
    for path in list_files(root):
        name = rel(path, root)
        if path.suffix not in ALLOWED_SUFFIXES or (
            path.suffix == "" and path.name not in ALLOWED_NO_SUFFIX
        ):
            errors.append(f"{name}: file type not allowed in this repository")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{name}: not valid UTF-8 text")
            continue
        for label, pattern in HYGIENE_PATTERNS.items():
            m = pattern.search(text)
            if m:
                errors.append(f"{name}: possible {label}")
    return errors


def check_workflow(root: Path):
    errors = []
    folder = root / ".github/workflows"
    files = sorted(folder.glob("*.y*ml")) if folder.is_dir() else []
    for path in files:
        name = rel(path, root)
        text = path.read_text(encoding="utf-8")
        if "pull_request_target" in text:
            errors.append(f"{name}: pull_request_target is not allowed")
        top = re.search(r"^permissions:[ \t]*\n((?:[ \t]+\S.*\n?)+)", text, re.M)
        if not top or [ln.strip() for ln in top.group(1).splitlines() if ln.strip()] != ["contents: read"]:
            errors.append(f"{name}: top-level permissions must be exactly 'contents: read'")
        if re.search(r"^\s*permissions:\s*(write-all|read-all)?\s*$", text, re.M) and text.count("permissions:") > 1:
            errors.append(f"{name}: job-level permissions are not allowed")
        if re.search(r":\s*write\b", text):
            errors.append(f"{name}: write permission is not allowed")
        if "persist-credentials: false" not in text:
            errors.append(f"{name}: checkout must set persist-credentials: false")
        if "timeout-minutes:" not in text:
            errors.append(f"{name}: timeout-minutes required")
        for use in re.findall(r"uses:\s*(\S+)", text):
            if not re.search(r"@[0-9a-f]{40}$", use):
                errors.append(f"{name}: action not pinned to a full commit SHA: {use}")
    return errors


def check_example_skills(root: Path):
    errors = []
    folder = root / "examples" / "skills"
    skills = sorted(p for p in folder.iterdir() if p.is_dir()) if folder.is_dir() else []
    if not skills:
        errors.append("examples/skills: no example skill found")
    for skill in skills:
        errors += [e.replace(str(root) + "/", "") for e in check_skill_dir(skill)]
    return errors


CHECKS = [
    ("required files", check_required_files),
    ("disclaimer", check_disclaimer),
    ("relative links", check_links),
    ("prose style", check_prose_style),
    ("review dates", check_review_dates),
    ("official reference sections", check_docs_have_reference),
    ("exercises", check_exercises),
    ("duplicates", check_duplicates),
    ("code blocks and syntax", check_code),
    ("example skills", check_example_skills),
    ("hygiene", check_hygiene),
    ("workflow security", check_workflow),
]


def main(argv):
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent.parent
    symlink_errors = check_symlinks(root)
    if symlink_errors:
        print("FAIL  hygiene")
        for error in symlink_errors:
            print(f"      {error}")
        return 1

    failed = 0
    for label, fn in CHECKS:
        errors = fn(root)
        status = "PASS" if not errors else "FAIL"
        print(f"{status}  {label}")
        for err in errors:
            print(f"      {err}")
        failed += bool(errors)
    print(f"\n{len(CHECKS) - failed}/{len(CHECKS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

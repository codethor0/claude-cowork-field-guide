#!/usr/bin/env python3
"""Check a skill folder's skill.md frontmatter against documented limits.

Per the Claude Help Center (How to create custom skills, checked 2026-11-22),
skill.md starts with YAML frontmatter holding a required name (64 characters
maximum) and description (200 characters maximum), and the skill folder name
must match the skill's name.

Only simple one-line "key: value" frontmatter is supported. Multi-line YAML
values (such as "description: >") are reported as errors; write them on one line.

Uses only the Python standard library and makes no network requests.
Usage: python3 scripts/check_skill.py SKILL_DIR [SKILL_DIR ...]
Exit status is 0 when every folder passes and 1 otherwise.
"""

import sys
from pathlib import Path

NAME_MAX = 64
DESCRIPTION_MAX = 200
SKILL_FILE = "skill.md"


def parse_frontmatter(text: str):
    """Return (fields, body) or raise ValueError. Supports simple 'key: value' lines."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("skill.md must start with a '---' frontmatter line")
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter is not closed with '---'") from None
    fields = {}
    for number, line in enumerate(lines[1:end], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep or not key.strip():
            raise ValueError(f"line {number}: expected 'key: value'")
        if value.strip() in (">", "|", ">-", "|-"):
            raise ValueError(f"line {number}: multi-line values are not supported; use one line")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, "\n".join(lines[end + 1:])


def check_skill_dir(folder: Path):
    """Return a list of error strings for one skill folder."""
    path = folder / SKILL_FILE
    if not path.is_file():
        return [f"{folder}: missing {SKILL_FILE}"]
    try:
        fields, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        return [f"{path}: {exc}"]
    errors = []
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append(f"{path}: 'name' is required")
    elif len(name) > NAME_MAX:
        errors.append(f"{path}: 'name' is {len(name)} characters; maximum is {NAME_MAX}")
    elif name != folder.resolve().name:
        errors.append(f"{path}: folder name '{folder.resolve().name}' does not match skill name '{name}'")
    if not description:
        errors.append(f"{path}: 'description' is required")
    elif len(description) > DESCRIPTION_MAX:
        errors.append(
            f"{path}: 'description' is {len(description)} characters; maximum is {DESCRIPTION_MAX}"
        )
    if not body.strip():
        errors.append(f"{path}: instructions body is empty")
    return errors


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip().splitlines()[-2])
        return 2
    failed = False
    for arg in argv[1:]:
        errors = check_skill_dir(Path(arg))
        if errors:
            failed = True
            for err in errors:
                print(f"FAIL  {err}")
        else:
            print(f"OK    {arg}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

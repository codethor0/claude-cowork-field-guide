import tempfile
import unittest
from pathlib import Path

import validate as v


def make(root: Path, files: dict):
    for name, content in files.items():
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_missing_required_file_reported(self):
        errs = v.check_required_files(self.root, ["README.md"])
        self.assertEqual(errs, ["missing required file: README.md"])

    def test_required_file_present(self):
        make(self.root, {"README.md": "x"})
        self.assertEqual(v.check_required_files(self.root, ["README.md"]), [])

    def test_disclaimer_must_match(self):
        make(self.root, {"README.md": "no disclaimer", "NOTICE.md": v.DISCLAIMER})
        errs = v.check_disclaimer(self.root)
        self.assertEqual(len(errs), 1)
        self.assertIn("README.md", errs[0])

    def test_disclaimer_survives_line_wrapping(self):
        wrapped = v.DISCLAIMER.replace(". ", ".\n")
        make(self.root, {"README.md": wrapped, "NOTICE.md": wrapped})
        self.assertEqual(v.check_disclaimer(self.root), [])

    def test_broken_link_and_anchor(self):
        make(
            self.root,
            {
                "a.md": "[ok](b.md) [bad](nope.md) [anchor](b.md#missing) [good](b.md#title)",
                "b.md": "# Title\n",
            },
        )
        errs = v.check_links(self.root)
        self.assertEqual(len(errs), 2)
        self.assertTrue(any("nope.md" in e for e in errs))
        self.assertTrue(any("#missing" in e for e in errs))

    def test_links_must_stay_inside_repository(self):
        outside = self.root.parent / "outside_target.md"
        outside.write_text("x", encoding="utf-8")
        try:
            make(self.root, {"docs/a.md": f"[up](../../{outside.name}) [abs]({outside})"})
            errs = v.check_links(self.root)
            self.assertEqual(len(errs), 2, errs)
        finally:
            outside.unlink()

    def test_root_relative_link_resolves_against_repository_root(self):
        make(self.root, {"docs/a.md": "[ok](/README.md) [bad](/missing.md)", "README.md": "# R\n"})
        errs = v.check_links(self.root)
        self.assertEqual(len(errs), 1)
        self.assertIn("missing.md", errs[0])

    def test_em_dash_reported_with_file_and_line(self):
        dash = "\u2014"
        make(self.root, {"docs/a.md": f"fine\nbad {dash} here\n", "CONTENT_LICENSE.md": f"legal {dash} text\n"})
        errs = v.check_prose_style(self.root)
        self.assertEqual(len(errs), 1)
        self.assertTrue(errs[0].startswith("docs/a.md:2:"))

    def test_links_in_code_fences_ignored(self):
        make(self.root, {"a.md": "```\n[x](missing.md)\n```\n"})
        self.assertEqual(v.check_links(self.root), [])

    def test_external_links_not_checked(self):
        make(self.root, {"a.md": "[x](https://example.invalid/page)"})
        self.assertEqual(v.check_links(self.root), [])

    def test_review_date_required(self):
        make(self.root, {"docs/a.md": "# A\n", "docs/b.md": "# B\n\nLast reviewed: 2026-11-20\n"})
        errs = v.check_review_dates(self.root)
        self.assertEqual(len(errs), 1)
        self.assertIn("docs/a.md", errs[0])

    def test_exercise_sections_and_count(self):
        body = "".join(f"## {h}\n\n" for h in v.EXERCISE_HEADINGS)
        make(self.root, {"exercises/01-a.md": body, "exercises/README.md": "01-a.md"})
        errs = v.check_exercises(self.root)
        self.assertTrue(any("need at least" in e for e in errs))
        make(self.root, {"exercises/02-b.md": "## Objective\n"})
        errs = v.check_exercises(self.root)
        self.assertTrue(any("02-b.md: missing section 'Prerequisites'" in e for e in errs))
        self.assertTrue(any("does not link 02-b.md" in e for e in errs))

    def test_duplicate_file_detected(self):
        make(self.root, {"a.md": "same", "b.md": "same"})
        self.assertTrue(any("duplicate file" in e for e in v.check_duplicates(self.root)))

    def test_duplicate_paragraph_detected(self):
        para = "word " * 60
        make(self.root, {"a.md": f"one\n\n{para}\n", "b.md": f"two\n\n{para}\n"})
        self.assertTrue(any("duplicated paragraph" in e for e in v.check_duplicates(self.root)))

    def test_fence_with_extra_info_string_is_checked(self):
        make(self.root, {"d.md": "```python title=x\nx = (\n```\n"})
        self.assertEqual(len(v.check_code(self.root)), 1)

    def test_hygiene_case_insensitive_paths_and_attribution(self):
        make(self.root, {"a.md": "/Us" + "ers/Someone/x\n", "b.md": "Generated " + "with Claude Code\n"})
        self.assertEqual(len(v.check_hygiene(self.root)), 2)

    def test_exercise_index_requires_link_not_substring(self):
        body = "".join(f"## {h}\n\n" for h in v.EXERCISE_HEADINGS)
        files = {f"exercises/0{i}-x.md": body for i in range(1, 6)}
        files["exercises/README.md"] = "0".join("") + " ".join(f"mention 0{i}-x.md" for i in range(1, 6))
        make(self.root, files)
        self.assertEqual(len([e for e in v.check_exercises(self.root) if "does not link" in e]), 5)

    def test_python_syntax_errors(self):
        make(
            self.root,
            {
                "bad.py": "def f(:\n",
                "doc.md": "```python\nx = (\n```\n\n```json\n{\"a\": 1,}\n```\n",
            },
        )
        errs = v.check_code(self.root)
        self.assertEqual(len(errs), 3)

    def test_valid_code_passes(self):
        make(self.root, {"ok.py": "x = 1\n", "d.md": "```python\nprint(1)\n```\n```json\n{}\n```\n"})
        self.assertEqual(v.check_code(self.root), [])

    def test_unclosed_fence(self):
        make(self.root, {"d.md": "```python\nx = 1\n"})
        self.assertTrue(any("unclosed" in e for e in v.check_code(self.root)))

    def test_hygiene_detects_secrets_and_paths(self):
        make(
            self.root,
            {
                "a.md": "token gh" + "p_" + "A" * 36 + "\n",
                "b.md": "see /Us" + "ers/someone/project\n",
                "c.md": "mail someone@gm" + "ail.com\n",
                "d.md": "Co-Authored-" + "By: Tool <x@example.com>\n",
            },
        )
        errs = v.check_hygiene(self.root)
        self.assertEqual(len(errs), 4)

    def test_hygiene_rejects_binary_types(self):
        (self.root / "img.png").write_bytes(b"\x89PNG")
        self.assertTrue(any("not allowed" in e for e in v.check_hygiene(self.root)))

    def test_clean_files_pass_hygiene(self):
        make(self.root, {"a.md": "plain text\n", "LICENSE": "MIT\n"})
        self.assertEqual(v.check_hygiene(self.root), [])

    def test_workflow_rules(self):
        good = (
            "permissions:\n  contents: read\njobs:\n  j:\n    timeout-minutes: 5\n"
            "    steps:\n      - uses: actions/checkout@" + "a" * 40 + "\n"
            "        with:\n          persist-credentials: false\n"
        )
        make(self.root, {".github/workflows/validate.yml": good})
        self.assertEqual(v.check_workflow(self.root), [])
        wider = good.replace("contents: read", "contents: read\n  issues: write")
        make(self.root, {".github/workflows/validate.yml": wider})
        self.assertTrue(any("exactly" in e for e in v.check_workflow(self.root)))
        make(self.root, {".github/workflows/validate.yml": good})
        make(self.root, {".github/workflows/other.yml": good.replace("a" * 40, "v4")})
        self.assertTrue(any("other.yml" in e and "not pinned" in e for e in v.check_workflow(self.root)))
        (self.root / ".github/workflows/other.yml").unlink()
        bad = good.replace("a" * 40, "v4") + "on: pull_request_target\n"
        make(self.root, {".github/workflows/validate.yml": bad})
        errs = v.check_workflow(self.root)
        self.assertTrue(any("pull_request_target" in e for e in errs))
        self.assertTrue(any("not pinned" in e for e in errs))


if __name__ == "__main__":
    unittest.main()

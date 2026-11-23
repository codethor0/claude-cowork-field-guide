import tempfile
import unittest
from pathlib import Path

import check_skill as cs
import validate as v

GOOD = "---\nname: s\ndescription: Turns notes into a status report.\n---\n\n# Steps\n\n1. Read.\n"


def write(folder: Path, text: str):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / cs.SKILL_FILE).write_text(text, encoding="utf-8")


class CheckSkillTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_valid_skill_passes(self):
        write(self.root / "s", GOOD)
        self.assertEqual(cs.check_skill_dir(self.root / "s"), [])

    def test_missing_file(self):
        (self.root / "s").mkdir()
        self.assertIn("missing skill.md", cs.check_skill_dir(self.root / "s")[0])

    def test_frontmatter_required(self):
        write(self.root / "s", "# No frontmatter\n")
        self.assertIn("must start", cs.check_skill_dir(self.root / "s")[0])

    def test_unclosed_frontmatter(self):
        write(self.root / "s", "---\nname: x\ndescription: y\n")
        self.assertIn("not closed", cs.check_skill_dir(self.root / "s")[0])

    def test_name_and_description_required(self):
        write(self.root / "s", "---\nname:\n---\nbody\n")
        errs = cs.check_skill_dir(self.root / "s")
        self.assertTrue(any("'name' is required" in e for e in errs))
        self.assertTrue(any("'description' is required" in e for e in errs))

    def test_limits_enforced_at_boundary(self):
        ok_name = "n" * cs.NAME_MAX
        ok = "---\nname: " + ok_name + "\ndescription: " + "d" * cs.DESCRIPTION_MAX + "\n---\nbody\n"
        write(self.root / ok_name, ok)
        self.assertEqual(cs.check_skill_dir(self.root / ok_name), [])
        long_name = "n" * (cs.NAME_MAX + 1)
        long = "---\nname: " + long_name + "\ndescription: " + "d" * (cs.DESCRIPTION_MAX + 1) + "\n---\nbody\n"
        write(self.root / long_name, long)
        errs = cs.check_skill_dir(self.root / long_name)
        self.assertEqual(len(errs), 2)
        self.assertTrue(all("maximum" in e for e in errs))

    def test_quotes_are_not_counted(self):
        write(self.root / "quoted", '---\nname: "quoted"\ndescription: x\n---\nbody\n')
        self.assertEqual(cs.check_skill_dir(self.root / "quoted"), [])

    def test_empty_body_reported(self):
        write(self.root / "s", "---\nname: s\ndescription: b\n---\n\n")
        self.assertIn("body is empty", cs.check_skill_dir(self.root / "s")[0])

    def test_malformed_line_reported(self):
        write(self.root / "s", "---\nname a\n---\nbody\n")
        self.assertIn("expected 'key: value'", cs.check_skill_dir(self.root / "s")[0])

    def test_folder_name_must_match(self):
        write(self.root / "other", GOOD)
        errs = cs.check_skill_dir(self.root / "other")
        self.assertEqual(len(errs), 1)
        self.assertIn("does not match", errs[0])

    def test_multiline_value_reported(self):
        write(self.root / "s", "---\nname: s\ndescription: >\n  folded text\n---\nbody\n")
        self.assertIn("multi-line", cs.check_skill_dir(self.root / "s")[0])

    def test_main_exit_codes(self):
        write(self.root / "good", GOOD.replace("name: s", "name: good"))
        (self.root / "bad").mkdir()
        self.assertEqual(cs.main(["check_skill.py", str(self.root / "good")]), 0)
        self.assertEqual(cs.main(["check_skill.py", str(self.root / "bad")]), 1)
        self.assertEqual(cs.main(["check_skill.py"]), 2)

    def test_validator_requires_an_example_skill(self):
        self.assertTrue(v.check_example_skills(self.root))
        write(self.root / "examples" / "skills" / "s", GOOD)
        self.assertEqual(v.check_example_skills(self.root), [])
        write(self.root / "examples" / "skills" / "t", "---\nname: t\n---\nbody\n")
        errs = v.check_example_skills(self.root)
        self.assertEqual(len(errs), 1)
        self.assertNotIn(str(self.root), errs[0])


if __name__ == "__main__":
    unittest.main()

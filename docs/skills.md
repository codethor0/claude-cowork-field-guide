# Skills

Last reviewed: 2026-11-22

## What a skill is

A skill is a folder of instructions, and optionally files or code, that teaches Claude a repeatable procedure. Claude reads a short description first and loads the full instructions only when the skill is relevant. Per the Help Center, skills are available on all plans and require code execution and file creation to be enabled.

Good candidates are tasks you repeat with the same steps and the same expected output: a weekly status report, a meeting recap format, a file naming convention.

## Anatomy

The [custom-skills Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) documents lowercase `skill.md`. The [organization provisioning guide](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization) and Claude Code instructions require uppercase `SKILL.md` for their respective surfaces. The example here follows the custom-skill upload instructions. Verify the target surface's current packaging and metadata rules before reusing it elsewhere.

The Help Center describes a skill as a directory with a `skill.md` file that starts with YAML frontmatter:

| Field | Required | Limit | Purpose |
|---|---|---|---|
| `name` | Yes | 64 characters | The skill's name. Per the Help Center, the folder name must match it, or the upload can fail. |
| `description` | Yes | 200 characters | What it does and when to use it. Claude uses this to decide when to invoke the skill. |
| `dependencies` | No | | Software packages the skill needs |

The Markdown body below the frontmatter holds the procedure. A complete example is in [examples/skills/weekly-status](../examples/skills/weekly-status/skill.md).

## Ways to create one

- Write the folder by hand, package it as a ZIP, and upload it in Customize > Skills.
- Record a skill: per the Help Center, on Pro, Max, Ultra, and Team plans in Cowork for Mac, you can record your screen while doing a task (about 10 minutes maximum) and Claude proposes a skill. Do not show passwords, secrets, or private conversations while recording.
- Ask Claude to draft one from a description of your process, then edit it.

## Writing a good description

The description decides when the skill runs. It should name the task, the trigger, and the output. Compare:

| Weak | Strong |
|---|---|
| Helps with reports | Turns a week of meeting notes into a one-page status report with decisions, risks, and next steps. Use for weekly status requests. |

## Test before you rely on it

The Help Center advises testing a skill with a few different prompts after you upload it. This guide uses a small, repeatable test set:

1. Two prompts that should trigger the skill, worded differently.
2. One prompt that should not trigger it.
3. One prompt with incomplete input, to see how it handles gaps.
4. For each, write down the expected result before you run it, then compare.

Rerun the same set after every change to the skill. A sample set is in [examples/skills/weekly-status/test-prompts.md](../examples/skills/weekly-status/test-prompts.md), and `scripts/check_skill.py` checks a skill's frontmatter limits and folder name offline. Practice with [Exercise 5](../exercises/05-build-and-test-a-skill.md).

## Official reference

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

# Exercise 5: Build and test a skill

Last reviewed: 2026-11-22

## Objective

Package a recurring procedure as a skill, check it offline, upload it, and validate it with a fixed set of test prompts.

## Prerequisites

Code execution and file creation enabled (see [Skills](../docs/skills.md)). Python 3.9 or later to run the offline check.

## Input data

- [examples/skills/weekly-status/skill.md](../examples/skills/weekly-status/skill.md)
- [examples/skills/weekly-status/test-prompts.md](../examples/skills/weekly-status/test-prompts.md)
- [examples/meeting-notes/week-47.md](../examples/meeting-notes/week-47.md)

## Copy-ready prompt

1. Check the skill's frontmatter from the repository root:

   ```sh
   python3 scripts/check_skill.py examples/skills/weekly-status
   ```

2. Zip the `weekly-status` folder and upload it in Customize > Skills.
3. Disable the skill. Run the four prompts below, one per fresh task, and record the outputs as the baseline.
4. Enable the skill and repeat with the same model, files, and settings. For both passes, attach `week-47.md` for prompts 1 to 3. For prompt 4, use a fresh task with no attachment and turn Memory off.

```text
Write this week's status from the attached notes.
```

```text
Give me a recap of the week for Lee.
```

```text
Draft the December newsletter intro.
```

```text
Weekly status please.
```

## Expected result characteristics

- `check_skill.py` prints `OK` for the folder.
- Prompts 1 and 2 produce the skill's format with the same facts.
- Prompt 3 does not produce a status report.
- Prompt 4 asks for notes or reports none found; it does not invent content.

## Verification checklist

- [ ] Each prompt scored Pass, Partial, or Fail against the table in the test set.
- [ ] The resolved risk (photographer) is shown as resolved, not as an open risk.
- [ ] No owner or due date appears that is not in the notes.
- [ ] Compare both passes on factual accuracy, omissions, and treatment of missing input. Use the trigger column to assess the skill-enabled pass. Keep the skill only if it improves the intended task while preserving unrelated behavior. Repeat an uncertain case in a fresh task before drawing a conclusion.

## Common failure modes

- A vague description, so the skill triggers on prompt 3 or misses prompt 2.
- Testing with one prompt only.
- Editing the skill and not rerunning the full test set.

## Follow-up

Change one line of the description, rerun all four prompts, and compare scores. Keep the version that scores better.

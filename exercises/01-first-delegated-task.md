# Exercise 1: First delegated task

Last reviewed: 2026-11-22

## Objective

Run a complete Cowork task end to end on safe, synthetic files: brief, clarifying questions, steering, and review.

## Prerequisites

A paid Claude plan and the Claude Desktop app (this task uses a local folder). Read [Getting started](../docs/getting-started.md) and [Delegating a task](../docs/delegating-a-task.md).

## Input data

[examples/practice-folder/file-list.csv](../examples/practice-folder/file-list.csv): twelve invented file names with dates and a hint about each one's content. Create a new, empty folder called `cowork-practice` and connect only that folder.

## Copy-ready prompt

Part A, build the practice files:

```text
In the cowork-practice folder, create one small placeholder file for each
row of the attached file-list.csv. Use the exact file name. Put the
content_hint text inside each file. Do not create anything else.
```

Part B, the real task. Attach `file-list.csv` again:

```text
Outcome: the cowork-practice folder organized so I can find things quickly.
Inputs: the files in cowork-practice, plus the attached file-list.csv for dates.
Constraints: do not delete any file. Do not touch anything outside this folder.
Format: subfolders Photos, Receipts and invoices, Budgets, Notes and
agendas, Other. Rename files to YYYY-MM-DD description.ext using the date
in file-list.csv.
Done when: every original file is in exactly one subfolder and a file
named changes.md lists each old name and new name.
Ask me before: anything that would overwrite a file.
```

## Expected result characteristics

- Five subfolders exist and every file is in one of them.
- Both budget files are kept; Claude points out they may be versions of one budget.
- `untitled.txt` lands in Other, not deleted.
- `changes.md` maps every old name to a new name.

## Verification checklist

- [ ] Count files before and after: twelve originals before; the same twelve plus `changes.md` after.
- [ ] Open `changes.md` and spot-check three rows against the folder.
- [ ] Confirm no file outside `cowork-practice` changed.
- [ ] Note any question Claude asked and whether your brief could have answered it.

## Common failure modes

- Deleting the empty or duplicate-looking file. Your brief forbids it; if it happens, stop and check the mode you used.
- Guessing dates from file names instead of the CSV.
- Creating extra folders not in the format.

## Follow-up

Run Part B again in a fresh copy of the folder with a vaguer prompt ("tidy this folder"). Compare the two results and list which brief part made the difference.

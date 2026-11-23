# Exercise 3: Design a scheduled briefing

Last reviewed: 2026-11-22

## Objective

Write a self-contained scheduled task that is low risk, produces a useful weekly output, and is easy to review.

## Prerequisites

A paid Claude plan. Read [Scheduled tasks and working from anywhere](../docs/scheduled-tasks-and-remote-access.md).

## Input data

[examples/meeting-notes/week-47.md](../examples/meeting-notes/week-47.md). Save it to your Claude account or a project so a cloud task can read it.

## Copy-ready prompt

Create the task from "Scheduled" > "New task" > "Set up manually", approval mode Manual, frequency weekly, and use this prompt:

```text
Every Friday, read the meeting notes saved for this week. Write a briefing
with these sections: Decisions, Risks, Actions (owner and due date when
stated), Open questions. If a risk or question was resolved later in the
week, show it as resolved. If no notes exist for this week, write a
one-line briefing that says so and stop. Save the briefing as
briefing-YYYY-MM-DD.md. Do not send, share, or email anything.
```

Then click "Run" (run on demand) once instead of waiting for Friday.

## Expected result characteristics

- One file named with the run date.
- The launch date change (Nov 28 to Dec 5) under Decisions.
- The photographer risk shown as resolved; the consent question still open.
- No messages sent.

## Verification checklist

- [ ] The prompt names its input, output, and what to do if input is missing.
- [ ] The task contains no send, share, purchase, or delete step.
- [ ] Approval mode is Manual for the first runs.
- [ ] You found the run in the Scheduled page and read its output.
- [ ] You know how to pause and delete the task.

## Common failure modes

- Choosing a folder, which ties the task to your computer being on.
- Leaving out the "no notes" case, so Claude summarizes stale material.
- Adding an email step before the output has been reviewed for several weeks.

## Follow-up

After two weekly runs, decide whether to keep, change, or delete the task. Pause it if you are not reading the briefings.

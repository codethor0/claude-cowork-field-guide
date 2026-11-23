# Exercise 3: Design a scheduled briefing

Last reviewed: 2026-11-22

## Objective

Write a self-contained scheduled task that is low risk, produces a useful weekly output, and is easy to review.

## Prerequisites

A paid Claude plan. Read [Scheduled tasks and working from anywhere](../docs/scheduled-tasks-and-remote-access.md).

## Input data

[examples/meeting-notes/week-47.md](../examples/meeting-notes/week-47.md). Create a Cowork project called `Team briefings`, add `week-47.md` to it, and create the scheduled task inside that project (projects have their own scheduled tasks).

## Copy-ready prompt

Inside the project, create a scheduled task: approval mode Manual, frequency weekly. Use this prompt:

```text
Every Friday, read the newest weekly notes file in this project (today that
is week-47.md). Write a briefing
with these sections: Decisions, Risks, Actions (owner and due date when
stated), Open questions. If a risk or question was resolved later in the
week, show it as resolved. If no notes file is newer than the last
briefing, write a one-line briefing that says so and stop. Save the briefing as
briefing-YYYY-MM-DD.md. Do not send, share, or email anything.
```

Then run it on demand once instead of waiting for Friday. In Manual mode the run may pause for your approval; check the task if it seems stuck.

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
- Leaving out the "no new notes" case, so Claude summarizes stale material.
- Adding an email step before the output has been reviewed for several weeks.

## Follow-up

After two weekly runs, decide whether to keep, change, or delete the task. Pause it if you are not reading the briefings.

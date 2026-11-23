# Delegating a task

Last reviewed: 2026-11-22

## The idea

Delegating to Cowork works like briefing a capable colleague who has never seen your files. The quality of the result depends on the brief, the questions you answer, how you steer, and how carefully you review. This page is the method used in this guide; it is not an official procedure.

One rule sits above the rest: Claude does the drafting, you do the editing. Claude can produce in minutes a deliverable that would take you hours, and it can produce a wrong one just as fast. Whoever sends, publishes, or acts on the output owns it.

## Write the brief

A Cowork prompt is a work order, not a chat message. Three parts carry most of the weight:

1. **Deliverable**: exactly what to produce, including format, length, audience, and tone.
2. **Inputs**: the specific files, folders, connectors, and time ranges to use.
3. **Context**: what only you know. The purpose, the decision it supports, constraints, and what to ignore. This is the part most often skipped.

Compare "Draft a board update" with "Draft a one-page Q2 board update using last quarter's update as the structure, metrics from the Q2 sheet in my Finance folder, and the tone of my last three weekly notes. Lead with the recommendation. No jargon."

For larger tasks, expand those three parts into a full brief:

| Part | Question it answers | Example |
|---|---|---|
| Outcome | What should exist when Claude is done? | "A spreadsheet of last quarter's expenses, one row per receipt" |
| Inputs | Where is the material? | "The receipts in the `Receipts Q3` folder" |
| Context | Why, for whom, and what matters? | "For my accountant; she only needs business expenses" |
| Constraints | What must it not do? | "Do not move or rename the original files" |
| Format | What shape is the output? | "Columns: date, vendor, amount, category; a total row" |
| Done check | How will you both know it is right? | "Totals match the sum of the receipt amounts" |

Template:

```text
Outcome: <what should exist at the end>
Inputs: <folders, files, connected apps to use>
Context: <purpose, audience, what to ignore>
Constraints: <what to leave alone, what not to do>
Format: <file type, structure, naming>
Done when: <how to check the result>
Ask me before: <any action you want to approve first>
```

Front-load all of it. A missing part means Claude either asks or, worse, assumes.

## Align before it starts

For anything non-trivial, add one line to the end of the brief:

```text
Before you start, restate the task in your own words and ask me any
clarifying questions you have.
```

It costs one turn and can save a full redo.

## Answer clarifying questions

Claude may ask questions before it starts. Short, specific answers save rework. If a question shows Claude misunderstood the task, fix the brief rather than answering around it.

## Steer mid-task

Progress indicators show what Claude is doing. Step in when:

- It opens files or sites you did not mention.
- The scope grows beyond what you asked.
- It is about to take an action you cannot easily undo.

You can add direction in the same session, from desktop, web, or mobile.

## Review the deliverable

Treat the output as a draft until you have checked it:

1. Open the file. Confirm it is the format you asked for.
2. Check the done condition from your brief.
3. Spot-check details against the source: a few numbers, names, dates.
4. Look for silent gaps: skipped files, rows, or sections.
5. Confirm nothing outside the brief changed.

Asking Claude "is this correct?" is not verification, because it can confirm its own mistakes. Asking it to list its assumptions and anything it was unsure of is useful, and a second, separate session can cross-check facts. Neither replaces your own review. For high-stakes deliverables, add a human reviewer, and keep a record of what you checked.

## When to split a task

Split work into separate tasks when the parts are unrelated, when one part needs approval before the next, or when a single task would mix sensitive and non-sensitive material.

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) (what to expect during a task)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) (monitor tasks, not just commands)

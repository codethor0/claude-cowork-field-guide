# Exercise 2: Choose the permission mode

Last reviewed: 2026-11-22

## Objective

Decide which permission mode and connector settings fit a task, and explain why, before running anything.

## Prerequisites

Read [Permissions and modes](../docs/permissions-and-modes.md) and [Safety](../docs/safety.md). No Claude account is needed for the first part.

## Input data

Six synthetic scenarios:

| # | Scenario |
|---|---|
| A | Rename 40 photos in a practice folder you created today |
| B | Draft replies to this week's customer emails using your mail connector, for you to send |
| C | Every Monday, summarize public news about your industry into a document |
| D | Pay three supplier invoices through a banking site |
| E | Install a new plugin from an unfamiliar publisher and try its skills |
| F | Clean up a shared team drive using a connector with delete permission |

## Copy-ready prompt

After writing your own answers, compare them with Claude in a normal chat:

```text
I am choosing permission settings for Claude Cowork. For each scenario,
recommend Manual, Auto, or Skip mode, say which connector tools (if any)
should be set to "Always ask" or "Blocked", and say whether the task
should be delegated at all. Explain each choice in one sentence.

A: Rename 40 photos in a practice folder I created today.
B: Draft replies to this week's customer emails for me to send myself.
C: Every Monday, summarize public industry news into a document.
D: Pay three supplier invoices through a banking site.
E: Install an unfamiliar plugin and try its skills.
F: Clean up a shared team drive with a connector that can delete files.
```

## Expected result characteristics

- A: Auto is reasonable for a low-risk, reversible task.
- B: Manual or "Always ask" on the send tool; drafting only.
- C: a scheduled task with no write tools beyond saving the document.
- D: not delegated; the Help Center advises against sensitive financial actions in the browser.
- E: Manual, in a test folder, after reviewing the plugin.
- F: Manual with delete set to "Always ask", or split into a read-only audit first.

## Verification checklist

- [ ] Every answer names a mode and a reason.
- [ ] Every scenario with a write tool says how that tool is controlled.
- [ ] Scenario D is declined, not just set to Manual.
- [ ] Your answers and Claude's differ in at most one scenario, or you can explain why.

## Common failure modes

- Choosing Skip because the task "seems simple".
- Forgetting that "Always ask" covers only one tool, not the whole connector.
- Treating Auto mode's automated check as a guarantee.

## Follow-up

Pick scenario A or C and run it for real in a practice folder with the mode you chose.

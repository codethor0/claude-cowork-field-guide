# Before You Delegate: Your First Safe Agentic Workflow

Last reviewed: 2026-11-22

You coordinate volunteers at a tool library. You have a room booking and a later update. You want one short brief that volunteers can use on the day. A request like “summarize these notes” leaves the agent to guess which details matter and which source wins when they disagree.

## The completed task specification

| Decision | What to specify |
|---|---|
| Deliverable | Save a one-page draft named `output/volunteer-brief.md`. Include where and when to arrive, what to bring, what needs confirmation, and where each fact came from. |
| Audience | Volunteers preparing for the December 5 orientation. Use plain language they can scan on a phone. |
| Inputs | Read only `inputs/room-booking.md` and `inputs/coordinator-update.md`. The coordinator's later update takes precedence for any detail it changes. |
| Uncertainty | Flag anything the inputs leave open. If either file is missing or a disagreement cannot be resolved, stop and ask. |
| Permission | Create one draft in the empty output folder. Leave both inputs untouched. Keep the draft in the practice folder and ask before replacing any file. |
| Done when | The room, arrival time, doors, materials, and outstanding question match the sources. You can trace each fact to a named input. |

## Set up the folder

On desktop, create a fresh folder named `volunteer-brief-practice` with two subfolders named `inputs` and `output`. Save copies of [room-booking.md](../examples/before-you-delegate/inputs/room-booking.md) and [coordinator-update.md](../examples/before-you-delegate/inputs/coordinator-update.md) in `inputs`. Keep `output` empty. The examples are synthetic.

```text
volunteer-brief-practice/
  inputs/
    room-booking.md
    coordinator-update.md
  output/
```

For the live run, use Claude Desktop with a paid plan and access to Cowork. Select only this practice folder. Use Manual approval and turn off computer use if it is enabled. Decline requests to open a browser or add folders or connectors. If the interface has changed, check [Getting started](getting-started.md) before granting access.

The prompt gives the agent instructions. The folder you share, the tools you enable, and the approvals you give control its access. Keep your original files outside the practice folder.

## Copy-ready prompt

```text
Prepare a draft for tool library volunteers attending the December 5 orientation.

Read only inputs/room-booking.md and inputs/coordinator-update.md. Use
the later coordinator update for any facts it changes. If a file is
missing or a conflict remains, stop and ask me. Leave unknowns open.

Save one page to output/volunteer-brief.md with sections Where and when,
Bring, Confirm before sharing, and Sources. Give the source filename
and date where available so I can check the facts.

Do not edit the inputs, overwrite files, open websites, connect other
apps, or send anything. First tell me which files you will read and
what you will write. Wait for my go-ahead.
```

Review the plan and confirm it names exactly the two inputs and one output. If the agent asks to use other tools, decline and restate the task. After the run, open the draft yourself.

## Verify the result

1. Open the November 16 booking and the November 19 update side by side. Check the event date, doors, and materials against both. Confirm that the update replaces the room and arrival time.
2. Find December 5, Maple Room, 9:15 a.m. arrival, 9:30 a.m. doors, a blank sign-in sheet, and name tags in the draft. Look for a note that step-free access is still unconfirmed and needs an owner.
3. Check the sources section against the two filenames. Open the original example files and compare them with the copies. The only new file in the practice folder should be the draft.
4. Compare with the [worked brief](../examples/before-you-delegate/expected-brief.md). Use the worked brief to check facts and omissions, even if the wording differs.

You can do the whole review offline with a text editor. Write a brief using the two inputs before opening the worked brief. Then try reviewing a deliberately incorrect version with Cedar Room or an assurance that access is step-free. Find the exact line in the input that contradicts or fails to support the claim.

## Decide what to do next

| If you find | Decision |
|---|---|
| Every fact checks out and the scope was respected | Accept the draft. Leave the access question visible until the coordinator confirms it. |
| The draft uses Cedar Room or the old arrival time | Revise. Point to the November 19 update and ask for a corrected draft, then verify it again. |
| The draft promises step-free access | Revise. Ask for the claim to be marked unconfirmed. Assign the follow-up yourself. |
| The agent changed inputs, used an unapproved tool, or tried to send the draft | Reject the run. Stop it, review what happened, and start again with fresh copies and narrower access. |

Next, try [Exercise 1](../exercises/01-first-delegated-task.md) to practice reviewing file changes, or use the [delegation template](delegating-a-task.md#write-the-brief) for a task of your own.

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

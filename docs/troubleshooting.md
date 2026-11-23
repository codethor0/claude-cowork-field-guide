# Troubleshooting

Last reviewed: 2026-11-22

Check the symptom, then the most likely cause. Each row comes from the Help Center unless marked otherwise.

| Symptom | Likely cause | What to do |
|---|---|---|
| "Setting up Claude's workspace" when starting | Cowork is updating to the latest version | Wait; this is expected |
| No "Cowork" option in the message box | Older app version, or you have the newer combined experience | Update the app. In the combined experience, describe the task in any conversation |
| Task cannot reach local files or the browser | Desktop app closed or offline | Open the desktop app on the computer that has the files |
| Scheduled run finished without using a tool | That connector tool is set to "Always ask" | Edit the task: set its approval mode to Manual and allow the tool for scheduled runs |
| Scheduled task only runs when the computer is on | A folder was chosen, which ties it to that computer | Remove the folder or keep the computer awake with the app open |
| A plugin works on desktop but not on web | It includes a local MCP server, which is desktop-only | Use it on desktop |
| Auto mode or "Always allow" is missing | Your organization's admin turned it off | Ask your admin (see [Team and Enterprise](team-and-enterprise.md)) |
| Dispatch is not in the sidebar | Limited beta, not available to new users | Use cloud sessions from the web or mobile app instead |
| Usage runs out quickly | Multi-step tasks use more usage per step | Group related work, start new conversations for unrelated work, check Settings > Usage |
| Output is wrong or incomplete | Brief was missing inputs, constraints, or a done check (this guide's diagnosis) | Rewrite the brief with [Delegating a task](delegating-a-task.md) |
| Claude acts outside the brief | Scope creep or prompt injection | Stop the task; see [Safety](safety.md) |

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) (troubleshooting and limitations)
- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)

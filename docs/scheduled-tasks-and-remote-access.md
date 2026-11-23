# Scheduled tasks and working from anywhere

Last reviewed: 2026-11-22

## Scheduled tasks

A scheduled task saves a prompt as instructions and runs it on a cadence or on demand. Per the Help Center, each run is its own Cowork session with the same capabilities as a regular task: connectors, skills, and plugins. Scheduled tasks run in the cloud, so they keep running when your computer is asleep or the desktop app is closed. They are available on all paid plans.

Ways to create one:

- Type `/schedule` in a Cowork task.
- Click "Scheduled" in the left sidebar, then "New task", and choose "Create with Claude" or "Set up manually".
- In the newer combined experience, describe the task and its timing in any conversation, review the proposal, and click "Schedule".

A manual setup asks for a name, the prompt, the approval mode, the frequency (hourly, daily, weekly, weekdays, or manual), and optionally a model and a folder. Choosing a folder ties the task to your computer: it then runs only while the computer is awake and the desktop app is open.

From the Scheduled page you can review past and upcoming runs, edit, pause, resume, delete, or run a task on demand.

## Designing a safe scheduled task

Nobody watches a scheduled run as it happens. The Help Center advises:

- Start with low-risk work such as summaries.
- Avoid sensitive data and consequential actions: sending messages, purchases, anything hard to undo.
- Review the output of each run.
- Pause or delete tasks you no longer use.

A good scheduled prompt is self-contained: it states the inputs, the output location, and what to do when an input is missing. Practice with [Exercise 3](../exercises/03-design-a-scheduled-briefing.md).

If a connector tool is set to "Always ask", a scheduled run may wait for your answer or finish without that tool.

## Working from your phone or any browser

Cowork sessions live with your Claude account. You can start a task on one surface and check on it, answer questions, or steer it from another (desktop, web, or mobile). Tasks that need local files or the browser still require the desktop app to be open and online.

## Dispatch

Dispatch is a single continuous thread you message from your phone, and it runs work on your desktop computer with your local files and apps. Per the Help Center (checked 2026-11-22), it is in limited beta on some Pro, Max, and Ultra plans and is not available to new users. It needs the desktop app open and the computer awake. Because instructions from a phone can trigger real actions on a computer, only connect it if you are comfortable with everything the chain could do.

## Official reference

- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) (be cautious with scheduled tasks)

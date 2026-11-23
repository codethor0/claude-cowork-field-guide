# Instructions, projects, and memory

Last reviewed: 2026-11-22

## Standing context

Repeating the same background in every task wastes time and invites inconsistency. Cowork offers three places to put context once.

| Layer | Scope | Good for |
|---|---|---|
| Global instructions | Every Cowork session | Your role, preferred tone, output defaults |
| Folder instructions | Tasks on a selected local folder (desktop) | Conventions for that folder's files |
| Project instructions | Tasks inside one project | Rules, audience, and format for one body of work |

## Global instructions

Set them in Settings > Cowork > Global instructions > Edit (per the Help Center). In the newer combined experience they are part of the instructions in your personal settings and apply to every conversation. Keep them short and durable: who you are, how you like output formatted, what to avoid. Task-specific rules belong in the task or the project.

## Folder instructions

When you select a local folder on desktop, folder instructions add context for that folder. The Help Center notes that Claude can also update them during a session, so review them from time to time.

## Projects

A project groups related tasks into a workspace with its own instructions, scheduled tasks, context (a local folder, a linked chat project, or a URL), and memory. Per the Help Center, you can create one from scratch, import an existing chat project (one at a time), or start from an existing folder. Projects are saved to your Claude account and work the same way in Cowork and chat.

On Team and Enterprise plans, projects can be shared with "Can view" or "Can edit" access.

## Memory

Cowork in the cloud shares memory with chat, so Claude can start from what it knows about how you work. Things to know, per the Help Center:

- Memory learned in one project does not carry to other projects.
- A project also shares memory with your chats outside projects unless you turn off "Use account memory" for that project.
- To run a single task without memory, turn "Memory" off in the "+" menu before the first message. It cannot be changed after the task starts.
- You can view, edit, and delete memory.

## Organization instructions

On Team and Enterprise plans, owners can set organization instructions that apply across the organization. See the linked Help Center article.

## Instructions, skills, and plugins

| Layer | What it is | When it applies |
|---|---|---|
| Instructions | Standing rules and preferences | Always, at their scope |
| [Skill](skills.md) | One repeatable procedure | Loaded when relevant |
| [Plugin](plugins.md) | Several skills plus connectors and sub-agents | Installed as one package |

General rules go in instructions. A repeatable process goes in a skill. A complete setup for a role or team goes in a plugin.

## A layering rule of thumb

Put each instruction in the narrowest layer that needs it. If a rule only matters for the quarterly report, it does not belong in global instructions. Practice with [Exercise 4](../exercises/04-write-standing-instructions.md); sample files are in [examples/instructions](../examples/instructions/global-instructions.md).

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) (global and folder instructions)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Set organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions)

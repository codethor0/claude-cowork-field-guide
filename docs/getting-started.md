# Getting started with Claude Cowork

Last reviewed: 2026-11-22

## What it is

Claude Cowork is the part of Claude that carries out multi-step work for you instead of answering one prompt at a time. Per the Help Center, it uses the same agentic architecture as Claude Code, with no terminal required. You describe an outcome, Claude plans the work, runs it, and hands back finished files: documents, spreadsheets, organized folders, research summaries.

The shift to keep in mind: in chat you get an answer to read. In Cowork you get work done on your behalf, which means you are also responsible for what it does.

## When to use it

| | Chat | Cowork | Claude Code |
|---|---|---|---|
| Best for | Questions, writing help, brainstorming, one uploaded document | Multi-file and folder work, deliverables saved back as files, recurring tasks, work across connectors | Software repositories: code changes, tests, debugging |
| Your role | In the conversation | Brief, steer, review | Brief, review diffs |
| Runs while you are away | No | Depends on the task and where it runs | Depends on setup |

A short way to say it: chat answers you, Cowork works for you. Where the message box no longer shows separate options, the choice is about what you ask Claude to do rather than which button you press.

## Where it runs

Per the Help Center (checked 2026-11-22):

- Cowork is available on paid plans (Pro, Max, Ultra, Team, Enterprise).
- Desktop app on macOS, Windows, and Linux (beta): all paid plans. Desktop is the full experience, including local files and the browser.
- Web and mobile: Pro, Max, Ultra, and Team (beta on Team), and Enterprise when an owner enables it.
- Chrome side panel: all paid plans, per the Cowork getting-started article; on Enterprise an owner must enable both Claude in Chrome and Cowork in the cloud. Opening the panel starts a Cowork session directly.
- Cloud sessions run in an isolated environment on Anthropic's servers. They can continue with your laptop closed when the task uses cloud inputs and tools. Local folders and the built-in browser need Claude Desktop online. Team owners can turn cloud sessions off. On Enterprise, cloud sessions are off by default and need both an organization setting and access for your group. Local sessions run code in an isolated virtual machine on your computer.
- Computer use also needs Claude Desktop and an awake computer. See [browser setup](browser-and-computer-use.md#two-browsers) for the separate Chrome requirements.

Some accounts have a newer combined experience where the message box no longer shows separate "Chat" and "Cowork" options. In that case any conversation can take on a Cowork task. The steps below describe the separate-option layout.

## Your first session

1. Open Claude on the web, in the desktop app, or in the mobile app.
2. In the message box, select "Cowork".
3. Describe the outcome you want (see [Delegating a task](delegating-a-task.md) for how to write it).
4. Read Claude's plan before it starts. Answer any questions it asks.
5. Watch the progress indicators, steer if it drifts, and review the output before you use it.

Use a practice folder with copies of files for the first few tasks. Start with [Before You Delegate](before-you-delegate.md), then try [Exercise 1](../exercises/01-first-delegated-task.md).

## What happens during a task

- Claude makes a plan and may split the work into subtasks or parallel sub-agents.
- Code and shell commands run in the isolated environment for that session, whether in the cloud or in a local virtual machine.
- Progress indicators show each step. You can add direction at any time, from any surface.
- Claude asks for explicit permission before permanently deleting files.

## Usage

Multi-step tasks use more of your plan's usage than a quick question, because each step uses tokens. The Help Center suggests grouping related work into one task, starting a new conversation for unrelated work, and saying when you only need a quick answer.

Two habits from this guide also help: use chat for quick questions and save Cowork for work that needs files and several steps, and split large jobs into batches you review between runs instead of one enormous session.

## Current limitations

- Sessions cannot be shared with other people. Individual artifacts can be.
- Some features are desktop-only, such as plugins that include local MCP servers.
- Features and plan availability change. Check the official page before relying on a detail.

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- [Introduction to Claude Cowork course](https://academy.claude.com/courses/introduction-to-claude-cowork)

# Claude Cowork Field Guide

[![Validate](https://github.com/codethor0/claude-cowork-field-guide/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/codethor0/claude-cowork-field-guide/actions/workflows/validate.yml)

A practical, independently written guide to delegating real work to Claude Cowork: how to brief a task, choose permissions, schedule recurring work, give Claude standing context, build and test skills, review plugins, and stay safe in the browser. It includes seven hands-on exercises with synthetic data and small validation scripts for the documentation itself.

> Independent educational resource. Not affiliated with, sponsored by, or endorsed by Anthropic or Claude Academy. Claude and associated product names belong to their respective owners.

The guide is a companion to Anthropic's Claude Academy course [Introduction to Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork), written by the maintainer after taking it. It contains original explanations and exercises, not course material. See [NOTICE.md](NOTICE.md).

## Who it is for

| Reader | Start with | Then |
|---|---|---|
| **New to Cowork** | [Getting started](docs/getting-started.md) | [Delegating a task](docs/delegating-a-task.md), [Exercise 1](exercises/01-first-delegated-task.md) |
| **Daily user**: wants repeatable work | [Instructions, projects, and memory](docs/instructions-projects-and-memory.md) | [Skills](docs/skills.md), [Scheduled tasks](docs/scheduled-tasks-and-remote-access.md), [Exercise 5](exercises/05-build-and-test-a-skill.md) |
| **Team lead or admin** | [Team and Enterprise](docs/team-and-enterprise.md) | [Plugins](docs/plugins.md), [Safety](docs/safety.md), [Exercise 6](exercises/06-review-a-plugin.md) |

## Five-minute quick start

1. Read [Getting started](docs/getting-started.md).
2. Copy the brief template from [Delegating a task](docs/delegating-a-task.md).
3. Make an empty practice folder and do [Exercise 1](exercises/01-first-delegated-task.md).

No installation is needed to read or follow the guides.

## Learning path

| Step | Guide | Question it answers |
|---|---|---|
| 1 | [Getting started](docs/getting-started.md) | What is Cowork, and when should I use it? |
| 2 | [Delegating a task](docs/delegating-a-task.md) | How do I brief, steer, and review a task? |
| 3 | [Permissions and modes](docs/permissions-and-modes.md) | How much should Claude check with me? |
| 4 | [Scheduled tasks and working from anywhere](docs/scheduled-tasks-and-remote-access.md) | How do I automate recurring work safely? |
| 5 | [Instructions, projects, and memory](docs/instructions-projects-and-memory.md) | Where do standing rules and context belong? |
| 6 | [Skills](docs/skills.md) | How do I package and test a repeatable procedure? |
| 7 | [Plugins](docs/plugins.md) | How do I evaluate, install, and share bundles? |
| 8 | [Browser and computer use](docs/browser-and-computer-use.md) | How does Claude work on websites and desktop apps? |
| 9 | [Microsoft 365 add-ins](docs/microsoft-365.md) | How does Claude fit with Excel, PowerPoint, Word, and Outlook? |
| 10 | [Safety](docs/safety.md) | What are the real risks, and what controls them? |
| 11 | [Team and Enterprise](docs/team-and-enterprise.md) | What can admins control? |
| Ref | [Troubleshooting](docs/troubleshooting.md) | Something went wrong. What do I check? |

## Hands-on exercises

Seven original exercises. Each has an objective, prerequisites, input data, a copy-ready prompt, expected result characteristics, a verification checklist, common failure modes, and a follow-up; the validator enforces these headings. Index: [exercises/README.md](exercises/README.md).

1. [First delegated task](exercises/01-first-delegated-task.md)
2. [Choose the permission mode](exercises/02-choose-the-permission-mode.md)
3. [Design a scheduled briefing](exercises/03-design-a-scheduled-briefing.md)
4. [Write standing instructions](exercises/04-write-standing-instructions.md)
5. [Build and test a skill](exercises/05-build-and-test-a-skill.md)
6. [Review a plugin before installing](exercises/06-review-a-plugin.md)
7. [Plan a safe browser task](exercises/07-plan-a-safe-browser-task.md)

Generated output varies between runs. The exercises describe what to look for, not exact text.

## Author background

The maintainer completed the Claude Academy course Introduction to Claude Cowork and earned its completion badge on 2026-11-22: [badge verification page](https://academy.claude.com/verify/df01266593c12fa76621eefb31dd6eff). The badge shows course completion only. It is not a professional certification, and it does not mean Anthropic reviewed or endorses this repository.

## Prerequisites

- To read: a web browser.
- To do exercises: a paid Claude plan. Exercise 1 also needs the Claude Desktop app.
- To run the repository checks: Python 3.9 or later (standard library only; no packages to install) and Git.

## Running the checks

From the repository root:

```sh
python3 -m unittest discover -s scripts   # tests for the scripts
python3 scripts/validate.py               # structure, links, hygiene, skills, code syntax
python3 scripts/check_skill.py examples/skills/weekly-status   # one skill's frontmatter
```

The validator makes no network requests. It checks required files, the disclaimer, relative links and anchors, review dates, exercise structure, duplicated content, code-block syntax, example skill frontmatter, forbidden file types, secret-like strings, em dashes in prose, and the CI workflow's security settings. GitHub Actions runs the same commands on pull requests and pushes to `main`.

External links are reviewed by hand before releases and are not checked in CI.

## Official links

- [Introduction to Claude Cowork course](https://academy.claude.com/courses/introduction-to-claude-cowork)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

The full annotated list is in [resources/official-links.md](resources/official-links.md). How claims were checked, and what was left out, is in [resources/sources-and-verification.md](resources/sources-and-verification.md).

## Security and safety

Read [Safety](docs/safety.md) before connecting folders, connectors, or the browser. The short version: you are the editor and Claude is the writer, so review before you ship; use a dedicated working folder; match the permission mode to the stakes; treat web and email content as untrusted; and keep sensitive accounts out of browser and computer use. To report a problem with this repository, see [SECURITY.md](SECURITY.md).

## Known limitations

- Cowork is changing quickly, including a gradual rollout that merges chat and Cowork. Each page has a review date; check the linked official source before relying on a detail.
- Microsoft 365 add-in statements come from Anthropic's product page and were not tested hands-on.
- Exercises were written against documented behavior on 2026-11-22 and have not been tested on every plan or admin configuration.
- Anthropic has not reviewed or approved this repository's use of its names. See [NOTICE.md](NOTICE.md).
- This is not a substitute for the official documentation or for professional advice.

## Licensing and attribution

- Code and scripts: [MIT](LICENSE).
- Original written content: [CC BY 4.0](CONTENT_LICENSE.md).
- Anthropic's course materials, trademarks, and product assets are not covered by these licenses and are not included.

Scope details are in [NOTICE.md](NOTICE.md).

## Contributing

Corrections are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). Do not submit Academy lesson text, quiz questions, or screenshots.

## Maintainer

[codethor0](https://github.com/codethor0)

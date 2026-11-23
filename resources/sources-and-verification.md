# Sources and verification

Last reviewed: 2026-11-22

How the claims in this repository were checked, and what was not.

## Method

- Product statements come from official pages (support.claude.com, academy.claude.com, claude.com), read on 2026-11-22.
- The content brief was the author's own notes from taking Introduction to Claude Cowork and reviewing its quiz. The notes were not copied into the repository, and no lesson text or quiz content is included. Explanations, examples, and exercises were written fresh.
- Where a statement depends on plan or rollout, the page says "per the Help Center" and carries a review date.
- Methods presented as this guide's own (the brief template, the skill test set, the plugin review, the rollout pattern) are labeled as such.

## Verified statements

| Statement | Source | Status on 2026-11-22 |
|---|---|---|
| Cowork uses the same agentic architecture as Claude Code, no terminal required | [Get started](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) | Confirmed |
| Paid plans only; surface availability by plan; sessions run in the cloud | Get started; [Web, desktop, mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile) | Confirmed |
| Local files, browser, and computer use need the desktop app open | Get started | Confirmed |
| Manual, Auto, and Skip modes and their behavior; "Always ask" connector tool setting | Get started | Confirmed |
| Explicit permission before permanent deletion; not covered for computer use | Get started; [Computer use](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) | Confirmed |
| Prompt injection needs both untrusted reading and harmful action; risk is not zero | [Use Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) | Confirmed |
| Isolation limits where code runs, not what Claude can read or do | Use Cowork safely | Confirmed |
| Scheduled tasks: cloud execution, creation options, frequencies, folder ties to computer | [Scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) | Confirmed |
| Dispatch is limited beta, not available to new users | [Dispatch](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork) | Confirmed |
| Projects: instructions, scheduled tasks, context, memory; sharing on Team and Enterprise | [Projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) | Confirmed |
| Organization instructions for Team and Enterprise owners | [Organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions) | Confirmed |
| Skill structure: `skill.md`, name 64 and description 200 character limits; record a skill on Mac | [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) | Confirmed |
| Plugins bundle skills, connectors, sub-agents; local MCP servers run with your permissions | [Use plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Confirmed |
| Plugin sharing, publishing, and marketplaces on Team and Enterprise | Use plugins; [Manage plugins](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) | Confirmed |
| Built-in browser vs Claude in Chrome; logins persist in the built-in browser | [Built-in browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork) | Confirmed |
| Computer use availability, per-app permissions, app-type limits | Computer use | Confirmed |
| Team and Enterprise admin controls and defaults | [Team and Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans) | Confirmed |
| Microsoft 365 add-in descriptions | [Product page](https://claude.com/claude-for-microsoft-365) | Confirmed on the page. Feature claims are Anthropic's and were not tested here |

## Not confirmed and left out

These appeared in the author's study notes but were not found in the official pages above, so the guide does not state them:

| Item | Notes |
|---|---|
| A specific date on which Cowork merged into every conversation | The Help Center describes a gradual rollout of the combined experience, without a single date |
| Plan prices | Not needed for the guide; check the official pricing page |
| Auto mode using more usage than other modes | Not stated in the articles reviewed |
| Reports of large local file deletions during testing | Not found in official sources |
| A dedicated "skill evals" feature | The Help Center says to test a skill with a few prompts. The test-set method in [Skills](../docs/skills.md) is this guide's own |

## Other limits

| Item | Notes |
|---|---|
| Permission to use Anthropic names | The [Trademark Guidelines](https://www.anthropic.com/legal/trademark-guidelines) allow use only as Anthropic permits and contain no stated exception for descriptive references. No permission has been requested. See [NOTICE.md](../NOTICE.md) |
| Hands-on testing | Exercises were written against documented behavior; not every plan or admin configuration was tested |
| Badge details | The README links the maintainer's public badge verification page, which was read in a browser on 2026-11-22 |

## Link review

All entries in [official-links.md](official-links.md) returned HTTP 200 on 2026-11-22. A 200 shows the page was reachable, not that its content still matches. External links are checked by hand before each release, not in CI.

## Re-review

Date-sensitive pages: [getting-started.md](../docs/getting-started.md), [team-and-enterprise.md](../docs/team-and-enterprise.md), [browser-and-computer-use.md](../docs/browser-and-computer-use.md), [scheduled-tasks-and-remote-access.md](../docs/scheduled-tasks-and-remote-access.md). Re-check them first.

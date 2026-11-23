# Permissions and modes

Last reviewed: 2026-11-22

## What you control

Per the Help Center, you decide:

- Which local folders Claude can read and write. Claude works only in folders you connect.
- Which connectors Claude can use, and how each connector tool is approved.
- How much Claude checks with you, through the permission mode.

Claude asks for explicit permission before permanently deleting files. That protection does not cover computer use (see [Browser and computer use](browser-and-computer-use.md)).

## The three modes

You can change the mode at any time from the mode selector in the message box.

| Mode | Older name | Behavior per the Help Center |
|---|---|---|
| Manual (Manually approve) | Ask before acting | Claude pauses and asks before actions. You choose Allow or Deny. |
| Auto (Automatically approve) | | Claude keeps working and an automated check reviews actions before they run, blocking ones it judges unsafe. The check can miss risky actions. |
| Skip (Skip all approvals) | Act without asking | Claude does not pause and nothing checks actions automatically. Use only when you fully trust every file, connector, app, and site involved. |

In Auto mode, connector tools set to "Needs approval" can run without asking you (the automated check reviews them instead), and tools set to "Always allow" are not screened, except tools the connector marks as destructive. To approve a tool yourself in every mode, set it to "Always ask".

Defaults, per the Help Center: in the newer combined experience, Auto is rolling out as the default on Pro, Max, Ultra, and Team plans, and Manual is the default on Enterprise. Check the mode selector before a task instead of assuming you start in Manual.

On Team and Enterprise plans, an admin can remove Auto mode. Write-capable connector tools need approval per task unless the admin turns on "Allow 'Always allow' for connector tools", which is off by default. See [Team and Enterprise](team-and-enterprise.md).

## Connector tool permissions

Each connector tool can be set to Always allow, Needs approval, Always ask, or Blocked (Customize > Connectors > the connector > Permissions). "Always ask" makes Claude ask before each use of that tool in every mode. The Help Center notes it applies only to the tool you choose: another tool may reach the same information without asking, so set related tools too.

## Choosing a mode

| Situation | Suggested mode |
|---|---|
| First time with a tool, plugin, site, or folder | Manual |
| Task touches sensitive files, accounts, or money | Manual, or do not delegate it |
| Well-defined, low-risk task you have run before | Auto |
| Fully trusted, reversible, closed environment | Skip, rarely |

This table is this guide's recommendation, based on the Help Center's advice to switch to Manual for sensitive material, new tools, and hard-to-undo actions. Practice with [Exercise 2](../exercises/02-choose-the-permission-mode.md).

## Folder hygiene

- Make a dedicated working folder for Claude instead of connecting your whole home or documents folder.
- Keep financial documents, credentials, and personal records out of it.
- Work on copies when the task rewrites or reorganizes files.

## Official reference

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) (Choose how Claude checks with you)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

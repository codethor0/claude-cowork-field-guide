# Safety

Last reviewed: 2026-11-22

## The core idea

Per the Help Center, when something goes wrong in Cowork the impact depends on two things: what Claude can read and what Claude is allowed to do. Every safety habit in this guide reduces one or the other.

## Read tools and write tools

| Kind | Examples | Risk |
|---|---|---|
| Read | Reading an inbox, a folder, a web page; taking a screenshot | Exposure of what is read |
| Write | Sending a message, creating an event, deleting a file, running a command, clicking | Real actions, possibly hard to undo |

Human oversight matters most for write tools in high-stakes work.

## Prompt injection

A prompt injection hides instructions in content Claude reads as part of a legitimate task, such as an email, a document, or a web page. The Help Center explains that an attack needs two conditions at once: Claude can read content from outside your trust boundary, and Claude can take actions that could harm you. Remove either one and the attack gets much harder.

Anthropic describes several protections (model training, content classifiers, action screening in Auto mode, deletion protection, an isolated cloud environment). It also states that the chance of an attack is not zero.

## Where the work runs

Cloud sessions run in an isolated, temporary environment on Anthropic's servers that cannot reach your home or company network and is removed when the session ends. The Help Center is explicit that isolation limits where code runs, not what Claude can read or do through the access you granted.

## Checklist before a task

- [ ] The folder holds only what the task needs, ideally copies.
- [ ] Connectors are limited to what the task needs; sensitive write tools are set to "Always ask".
- [ ] The mode matches the stakes (see [Permissions and modes](permissions-and-modes.md)).
- [ ] Sites are ones you trust; no banking, health, or other people's personal data in the browser.
- [ ] Computer use is off or limited to approved, non-sensitive apps. On some accounts the toggle is on by default, so check Settings.

## Watch during a task

Monitor the pattern, not every command. Stop the task if Claude:

- opens files or sites you did not mention,
- grows the scope beyond the brief,
- starts discussing unrelated topics or asks for sensitive information unprompted.

The Help Center asks users to report suspicious behavior through the in-app feedback button or the address it lists.

## Your responsibility

You remain responsible for what Claude does on your behalf: content published, messages sent, purchases, data changed, scheduled runs, computer use actions, and respecting websites' terms of service.

## Official reference

- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely)

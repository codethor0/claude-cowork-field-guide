# Browser and computer use

Last reviewed: 2026-11-22

## How Claude reaches your tools

Per the Help Center, Cowork picks the most precise route first:

1. A connector, if one exists for the service (fastest and most reliable).
2. A browser, if there is no connector.
3. Computer use, clicking and typing in desktop apps, as a last resort.

When you can, connect the tools you use most. Screen interaction is slower and more error-prone.

## Two browsers

| | Built-in browser | Claude in Chrome |
|---|---|---|
| Where it runs | A browser inside the Claude Desktop app, shown in a side panel | Your own Chrome, through the extension |
| Your logins | None unless you import cookies or sign in inside it | The accounts you are already signed in to |
| Best for | Handing off the web part of a task | Work on a page that is already in front of you |

If you already use Claude in Chrome, it stays the default; otherwise Cowork uses the built-in browser. Change it in the desktop app under Settings > Cowork > Preferred browser. For tasks started on web or mobile, the built-in browser needs the desktop app open and online. With Claude in Chrome, those tasks use the extension directly; per the Help Center, the session must be connected to a desktop, but the app does not have to be open.

Anything you sign in to inside the built-in browser stays available to Claude in later sessions on that computer. Import cookies site by site and clear the ones you do not need.

## Browser safety

Both browsers run the same safeguards per the Help Center: Claude asks before acting on a new site, high-risk sites are blocked, and actions are checked against what you asked for. Prompt injection, instructions hidden in a web page, remains possible. Keep financial accounts, medical information, and other people's personal data out of both browsers, as the Help Center advises.

Build trust in steps: ask Claude to read a page and report before you ask it to act on one. "Read this page and summarize the pricing table" comes before "fill in this form".

Practice with [Exercise 7](../exercises/07-plan-a-safe-browser-task.md).

## Computer use

Computer use lets Claude see your screen and operate desktop apps. Per the Help Center (checked 2026-11-22):

- Available on Pro, Max, and Ultra in the desktop app on macOS and Windows. On Team and Enterprise it is a beta that an owner must turn on, and it works only in the newer combined experience.
- On some Pro, Max, and Ultra accounts the Enable computer use toggle is already on. Check Settings rather than assuming it is off.
- Claude asks permission before using each app. You can block apps.
- In browsers and many trading or crypto apps, Claude can see but not click or type. In terminals and code editors it can click and scroll but not type. Most other apps get full access.
- Computer use is not limited to connected folders, and Cowork's deletion protection does not apply to it.
- Claude takes screenshots to see the screen, so anything visible may be captured. Close sensitive apps and files first.
- The computer must be awake and the desktop app open.

Recommendations from the Help Center: keep sensitive apps (banking, healthcare, government) off limits, start with simple tasks, and write specific prompts.

## Official reference

- [Use the built-in browser in Claude Cowork](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork)
- [Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely)
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

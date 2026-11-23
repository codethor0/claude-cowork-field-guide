# Exercise 6: Review a plugin before installing

Last reviewed: 2026-11-22

## Objective

Apply a repeatable review to a plugin so you know what it adds before it can act on your behalf.

## Prerequisites

A paid Claude plan. Read [Plugins](../docs/plugins.md) and [Safety](../docs/safety.md).

## Input data

Any plugin listed in Customize > Plugins > Discover. Do not install it until the review is done.

## Copy-ready prompt

Ask in a normal chat, pasting the plugin's description and its list of skills and connectors:

```text
I am deciding whether to install this plugin. From the description below,
list: (1) every connector it adds and whether each can write or only read,
(2) whether it includes a local MCP server, (3) every skill and what
triggers it, (4) anything it claims that the listed parts do not explain.
Then give a recommendation: install, install in a test setup first, or
do not install, with one sentence of reasoning.

<paste the plugin description and contents>
```

## Expected result characteristics

- A table of connectors with read or write access.
- A clear yes or no on local MCP servers, or "not stated".
- Any gap between the plugin's claims and its contents is called out.
- A recommendation that matches the risk.

## Verification checklist

- [ ] You compared Claude's list against the plugin page yourself.
- [ ] You know who publishes the plugin.
- [ ] Write-capable connector tools have a planned permission setting.
- [ ] You know how to remove the plugin.

## Common failure modes

- Trusting the plugin's summary without checking its parts.
- Missing a local MCP server, which runs on your computer with your permissions.
- Installing first and reviewing later.

## Follow-up

If you install it, run its first task in Manual mode in a practice folder and note every permission prompt.

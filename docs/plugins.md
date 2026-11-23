# Plugins

Last reviewed: 2026-11-22

## What a plugin is

Per the Help Center, a plugin bundles skills, connectors, and sub-agents into one package for a role, team, or company. Plugins are available on all paid plans. A plugin you add is saved to your account and also works in chat and in Claude Code.

Installing a plugin can expand what Claude can do in one step, so review it the way you would review new software.

## Install and use

1. Open Customize in the left sidebar (in Cowork, open the Cowork tab first).
2. Open Plugins, then Discover.
3. Select a plugin and click "Add". You can also upload a plugin file you built.
4. Type "/" or click "+" to see the plugin's skills and commands.

## Customize

While viewing an installed plugin in Cowork, click "Customize" to open a task where Claude adjusts the plugin's skills and connectors with you. Anthropic also provides a "Plugin Create" plugin for building one from scratch.

## Review before installing

Use this checklist before adding a plugin, especially from outside your organization:

| Check | Why |
|---|---|
| Who publishes it, and do you trust them? | A plugin can add connectors and code |
| Which connectors does it add, with read or write tools? | Write tools can act on your behalf |
| Does it include a local MCP server? | Per the Help Center, local MCP servers run on your computer with the same permissions as any program you run |
| Do its skills match what it claims to do? | Unexpected skills widen scope |
| Can you remove it cleanly? | You may need to back out |

On Enterprise plans, skill and plugin scanning checks plugins for malicious content when they are installed or updated. It is on by default for Enterprise organizations that had not chosen a setting before 2026-10-02. Practice with [Exercise 6](../exercises/06-review-a-plugin.md).

## Sharing with a team

On Team and Enterprise plans, after an owner turns on sharing:

- Share a plugin with specific colleagues (Team and Enterprise) or a group (Enterprise). Recipients get view-only access that stays off until they enable it, and they receive your updates automatically. Plugins you added from a marketplace cannot be shared.
- Publish a plugin to the organization library. If review is required, an owner approves it, and updates go through the same review.
- Owners can run plugin marketplaces: curated sets of plugins distributed to the organization. Anthropic provides built-in marketplaces, and a Knowledge Work marketplace is added by default.

## Official reference

- [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)
- [Get started with skill and plugin scanning](https://support.claude.com/en/articles/15927065-get-started-with-skill-and-plugin-scanning)

# Team and Enterprise plans

Last reviewed: 2026-11-22

## Who this is for

Owners and admins rolling Cowork out to an organization, and members who want to know why their options differ from an individual plan. Statements below are from the Help Center on 2026-11-22. Admin settings change often; confirm in the linked article.

## Main controls

| Control | Where | Default |
|---|---|---|
| Cowork on or off for the organization | Organization settings > Cowork | On (off in organizations that enabled HIPAA) |
| Run Cowork in the cloud | Organization settings > Cowork | On for Team; off for Enterprise until an owner turns it on and grants the capability |
| Built-in browser | Organization settings > Capabilities | On, unless turned off |
| Claude in Chrome | Organization settings > Claude in Chrome | Extension must also be deployed |
| Allow "Automatically approve" mode | Organization settings > Capabilities | On |
| Allow "Always allow" for connector tools | Organization settings > Cowork (Permissions) | Off: write-capable connector tools need approval per task |
| Computer use | Owner setting | Beta, off until turned on; newer combined experience only |

On Enterprise plans, groups and custom roles can limit Cowork to specific teams.

## Plugins and skills for the organization

- Owners turn on skill and plugin sharing and publishing under Organization settings > Plugins & skills > Policy.
- Owners create plugin marketplaces to distribute curated plugins. Cowork and Skills must both be enabled first.
- Enterprise organizations can use skill and plugin scanning. It is on by default for Enterprise organizations that had not chosen a setting before 2026-10-02.

See [Plugins](plugins.md) for the member side.

## Monitoring

Per the Help Center, Cowork sessions in Claude on the web, Claude Desktop, and Claude Mobile are captured in the Compliance API, and Team and Enterprise owners can stream Cowork events to their own tools through OpenTelemetry.

## A rollout pattern

This is a suggested pattern, not an official one:

1. Pilot with a small group in Manual mode.
2. Publish two or three reviewed plugins through a marketplace before allowing open installs.
3. Decide whether to turn on "Always allow" for any write-capable connector tools; by default they need approval per task.
4. Write a short internal guide based on [Safety](safety.md).
5. Expand access, then revisit Auto mode once the pilot is stable.

## Official reference

- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

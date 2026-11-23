# Exercise 4: Write standing instructions

Last reviewed: 2026-11-22

## Objective

Split your preferences into global instructions and project instructions so each rule lives in the narrowest layer that needs it.

## Prerequisites

A paid Claude plan. Read [Instructions, projects, and memory](../docs/instructions-projects-and-memory.md).

## Input data

- [Sample global instructions](../examples/instructions/global-instructions.md)
- [Sample project instructions](../examples/instructions/project-instructions.md)
- A list you write of ten rules you often repeat to Claude.

## Copy-ready prompt

After sorting your own list, ask Claude to check it in a normal chat:

```text
Here are rules I give Claude. Sort each into: global instructions (every
task), project instructions (one body of work), or task brief (one task).
Flag any rule that conflicts with another or is too vague to follow.

1. <rule>
2. <rule>
...
10. <rule>
```

Then create a project, paste the project-level rules into its instructions, and run one small task in it.

## Expected result characteristics

- Global instructions hold only durable preferences: role, tone, formats, approval habits.
- Project instructions hold audience, structure, and content rules for one body of work.
- Task-specific details stay out of both.
- At least one vague rule is rewritten into something checkable.

## Verification checklist

- [ ] Global instructions are under about ten lines.
- [ ] No project-specific rule is in global instructions.
- [ ] The test task in the project followed a project rule without you repeating it.
- [ ] You checked whether the project should share account memory, and chose deliberately.

## Common failure modes

- Putting everything in global instructions, so unrelated tasks inherit irrelevant rules.
- Rules that cannot be checked ("be professional").
- Conflicting rules across layers, such as two different date formats.

## Follow-up

Turn off "Use account memory" for a test project and compare how the first task behaves.

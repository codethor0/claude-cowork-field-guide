# Test prompts for the weekly status skill

Synthetic test set for Exercise 5. Write the expected result before running each prompt, then compare.

| # | Prompt | Should the skill trigger? | Expected result |
|---|---|---|---|
| 1 | "Write this week's status from the attached notes." (week-47.md attached) | Yes | Report for week 47; launch moved to Dec 5; reshoot risk shown as resolved; consent question still open |
| 2 | "Give me a recap of the week for Lee." (week-47.md attached) | Yes | Same content as prompt 1 in the skill's format |
| 3 | "Draft the December newsletter intro." (week-47.md attached) | No | A newsletter draft, not a status report |
| 4 | "Weekly status please." (nothing attached, Memory off) | Yes | Asks for the notes or says none were found; does not invent content |

## Scoring

- Pass: the trigger behavior and every point in "Expected result" match.
- Partial: correct trigger, but a point is missing or wrong.
- Fail: wrong trigger, invented content, or wrong week.

Rerun all four prompts after every change to the skill and record the results.

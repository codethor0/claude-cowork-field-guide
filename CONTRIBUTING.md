# Contributing

Corrections and improvements are welcome, especially fixes for outdated or inaccurate product statements.

## What fits

- Factual corrections with an official source link.
- Clarity improvements and fixes to broken links.
- Exercise improvements that keep them original, reproducible, and based on synthetic data.
- Validator improvements with tests.

## What does not

- Text, screenshots, quiz questions, or answer keys copied from Claude Academy or other copyrighted sources.
- Promotional or speculative claims about product capability.
- New dependencies, build tools, or services without a documented need.
- Personal data, credentials, or confidential material.

## Writing standards

- Be clear, concise, and direct. No filler, hype, emojis, or em dashes (the validator rejects em dashes).
- State what is verified and what is an assumption. Cite the official page for product claims.
- Add or update `Last reviewed: YYYY-MM-DD` when you verify a page.
- Do not repeat definitions that already exist elsewhere; link to them.

## Workflow

1. Fork the repository and create a branch.
2. Make a focused change.
3. Run the checks from the repository root:

   ```sh
   python3 -m unittest discover -s scripts
   python3 scripts/validate.py
   ```

4. Open a pull request describing what changed and why. Link the source for any factual change.

By contributing, you agree that your contribution is licensed under the licenses described in [NOTICE.md](NOTICE.md) (MIT for code, CC BY 4.0 for written content).

Report security problems as described in [SECURITY.md](SECURITY.md), not in a public issue.

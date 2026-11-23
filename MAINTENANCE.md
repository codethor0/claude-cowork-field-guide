# Maintenance

Last reviewed: 2026-11-22

This repository is intentionally small: original Markdown, synthetic examples, and Python standard-library checks. It has no server, production credentials, or package dependencies.

## Checks that run automatically

- Every pull request and push to `main` runs the unit tests, repository validator, and example skill checker through [Validate](.github/workflows/validate.yml).
- The same workflow also runs monthly as a low-cost health check. GitHub may disable scheduled workflows after prolonged repository inactivity. Check the Actions tab if scheduled runs stop.
- Jobs run with read-only repository permission, an SHA-pinned checkout action, and a five-minute timeout.
- Workflows never change documentation, merge pull requests, create issues, send data to external endpoints, or publish releases.

## Checks that still require judgment

- Anthropic may change feature availability, permission behavior, integration details, or URLs. A successful test does not prove every product statement is current.
- External links are reviewed manually when factual documentation is changed. Automated CI validates local links and headings, not external websites.
- A changed product claim needs a current official source and a fresh `Last reviewed` date for the page actually checked. Do not bulk-update dates without verifying the sources.
- Security and licensing reports still require review. See [SECURITY.md](SECURITY.md) and [NOTICE.md](NOTICE.md).

## How to maintain the guide

From a fresh checkout of the latest `main`:

```sh
python3 -m unittest discover -s scripts
python3 scripts/validate.py
python3 scripts/check_skill.py examples/skills/weekly-status
```

For a factual correction, cite the official source, change only the affected content, run the checks, and open a signed pull request. Never push directly to protected `main`.

For security reports, follow [SECURITY.md](SECURITY.md). Do not place sensitive reports or secrets in a public issue.

## Release policy

- Keep `CHANGELOG.md` accurate. Published GitHub releases and version tags require an explicit owner decision.
- Do not automatically merge dependency changes or bot contributions.
- Keep the examples synthetic and the licenses separate: MIT for code, CC BY 4.0 for original prose.
- Favor stable, documented behavior over speculative new features.

A product documentation repository cannot remain correct forever without human review. The goal is quiet, useful automation and an obvious path for necessary corrections.

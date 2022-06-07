# Typed event handling for GitHub Webhooks

[![CI](https://github.com/k2bd/gh-webhooks/actions/workflows/ci.yml/badge.svg)](https://github.com/k2bd/gh-webhooks/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/k2bd/gh-webhooks/branch/main/graph/badge.svg?token=NE813K6GET)](https://codecov.io/gh/k2bd/gh-webhooks)

This library provides types for using GitHub Webhook events in Python, and a class for registering event handlers for each event type.

An example using FastAPI:

```python
from fastapi import FastAPI, Request
from gh_webhooks import GhWebhookEventHandler
from gh_webhooks.types import BranchProtectionRuleCreated

app = FastAPI()
event_handler = GhWebhookEventHandler()

@event_handler.on(BranchProtectionRuleCreated)
async def handle_new_branch_protection_rule(event: BranchProtectionRuleCreated):
    print(event.repository.name)


@app.post("/payload")
async def handle_webhook_payload(request: Request):
    await event_handler.handle_event(request.json())
```

Multiple handlers can be registered to the same event type, and they'll run concurrently.

The types are auto-generated using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator).
A GitHub action maintains these types automatically.

Integration tests are also auto-generated from the [example events](https://github.com/octokit/webhooks/tree/master/payload-examples) in the GitHub Webhook events spec docs.

## Developing

Install [Poetry](https://python-poetry.org/) and `poetry install` the project

### Useful Commands

Note: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`

- `poe autoformat` - Autoformat code
- `poe lint` - Lint code
- `poe test` - Run tests
- `poe docs` - Build docs
- `poe codegen` - Generate types

### Release

Release a new version by manually running the release action on GitHub with a 'major', 'minor', or 'patch' version bump selected.
This will create an push a new semver tag of the format `v1.2.3`.

Pushing this tag will trigger an action to release a new version of your library to PyPI.

Optionally create a release from this new tag to let users know what changed.

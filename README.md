# Types for GitHub Webhook Events

This library provides types for GitHub Webhook events in Python.
These types are auto-generated using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator).

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

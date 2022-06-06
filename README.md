# Python + Poetry Library Template

This template will get you ready to deploy a library to PyPI.

## Getting started from the template
1. Rename the `src/poetry_library_template` package.
1. Globally replace instances of `poetry-library-template` and `poetry_library_template` with your project and package name.
1. Set your repo up on [CodeCov](https://app.codecov.io/) and add a codecov token to your repo under the `CODECOV_TOKEN` action secret.
1. Create a new repo-scoped personal access token and add it as the `RELEASE_TOKEN` action secret. This is so we can [trigger further workflows on release](https://github.community/t/action-does-not-trigger-another-on-push-tag-action/17148/8).
1. Create a PyPI token with write access for this package, and add it as the `PYPI_PASSWORD` action secret.
1. Create and test your library.
1. Update the distribution information such as classifiers and repo location in `pyproject.toml`.
1. Write docs in `docs/`, including updating the project information in `docs/conf.py`
1. When you're ready to release the first version, run the release GitHub action with the "major", "minor", or "patch" option.
1. Remove this section from `README.md`.
1. Happy hacking!

### Like this template?
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png)](https://www.buymeacoffee.com/k2bd)


## Developing

Install [Poetry](https://python-poetry.org/) and `poetry install` the project

### Useful Commands

Note: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`

- `poe autoformat` - Autoformat code
- `poe lint` - Linting
- `poe test` - Run Tests
- `poe docs` - Build docs

### Release

Release a new version by manually running the release action on GitHub with a 'major', 'minor', or 'patch' version bump selected.
This will create an push a new semver tag of the format `v1.2.3`.

Pushing this tag will trigger an action to release a new version of your library to PyPI.

Optionally create a release from this new tag to let users know what changed.

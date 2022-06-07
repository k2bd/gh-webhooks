from typing import Any, Dict, List

import pytest
import requests

EXAMPLE_EVENTS_URL = (
    "https://octokit.github.io/webhooks/payload-examples/api.github.com/index.json"
)


def get_example_events() -> List[Dict[str, Any]]:
    """
    Get the latest example events from the GitHub Webhooks spec documentation.

    See https://github.com/octokit/webhooks/tree/master/payload-examples
    """
    r = requests.get(EXAMPLE_EVENTS_URL)
    events = [
        example
        for kind in r.json()
        for example in kind["examples"]
        if "examples" in kind
    ]
    return events

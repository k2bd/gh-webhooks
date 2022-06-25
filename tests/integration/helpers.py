from collections import defaultdict
from typing import Any, Dict, List

import requests

EXAMPLE_EVENTS_URL = (
    "https://octokit.github.io/webhooks/payload-examples/api.github.com/index.json"
)


def get_example_events() -> Dict[str, List[Any]]:
    """
    Get the latest example events from the GitHub Webhooks spec documentation.

    See https://github.com/octokit/webhooks/tree/master/payload-examples
    """
    r = requests.get(EXAMPLE_EVENTS_URL)
    result = defaultdict(list)
    for group in r.json():
        kind = group["name"]
        examples = group["examples"]
        result[kind].extend(examples)

    return result

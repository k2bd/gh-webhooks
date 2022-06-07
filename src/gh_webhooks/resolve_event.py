from typing import Any, Dict

from gh_webhooks.types import Model


def resolve_event(event: Dict[str, Any]):
    """
    Resolve a webhook event into a concrete model
    """
    result = Model.parse_obj(event)
    while "__root__" in result.dict():
        result = result.__root__  # type: ignore
    return result

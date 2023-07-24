import inspect
import logging
from typing import Any, Dict, Type

import stringcase

import gh_webhooks.types as generated_types
from gh_webhooks.exceptions import NoMatchingModel
from gh_webhooks.types import Model

logger = logging.getLogger(__name__)


def _get_cls(kind: str) -> Type[Model]:
    class_name = stringcase.pascalcase(kind) + "Event"
    matches = [
        obj for name, obj in inspect.getmembers(generated_types) if name == class_name
    ]

    if len(matches) != 1:
        raise NoMatchingModel(f"No event matching kind {kind!r}")

    (cls,) = matches
    return cls


def resolve_event(event: Dict[str, Any], kind: str):
    """
    Try to match an event to a concrete model given the kind provided in the
    X-Github-Event header.

    Raises
    ------
    gh_webhooks.exceptions.NoMatchingModel
        If the event can't be matched to a model
    """
    cls = _get_cls(kind)
    logger.info(f"Matching event to {cls!r}")

    result = Model.model_validate(event)
    while hasattr(result, "root") and result.root is not None:
        result = result.root  # type: ignore
    return result

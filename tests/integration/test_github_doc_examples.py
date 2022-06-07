from typing import Any, Dict, List

import pytest

from gh_webhooks.models import Model
from gh_webhooks.resolve_event import resolve_event
from tests.integration.helpers import get_example_events

EVENTS = get_example_events()


@pytest.mark.parametrize("event", EVENTS)
def test_example_events_parse_from_dict(event: Dict[str, Any]):
    """
    Test that all example events from the GitHub Webhook events documentation
    get properly parsed.
    """
    try:
        resolve_event(event)
    except Exception as e:
        raise ValueError(event) from e


# @pytest.mark.parametrize("event", EVENTS)
# def test_example_events_parse_from_model(event: Dict[str, Any]):
#     """
#     Test that all example events from the GitHub Webhook events documentation
#     get properly parsed if they've been translated into a Model by, e.g.,
#     FastAPI.
#     """
#     try:
#         resolve_event(Model.parse_obj(event))
#     except Exception as e:
#         raise ValueError(event) from e

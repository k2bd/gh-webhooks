from typing import Any, Dict

import pytest

from gh_webhooks import GhWebhookEventHandler
from gh_webhooks.resolve_event import resolve_event
from gh_webhooks.types import BranchProtectionRuleCreated
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


@pytest.mark.xfail(reason="See k2bd/gh-webhooks#7")
def test_example_events_parse_from_dict_with_extra_fields():
    """
    Test that adding a new field (e.g. when the spec is updated in a
    non-breaking way) doesn't break parsing
    """
    event = {**(EVENTS[0]), "another_random_field_not_in_spec": 123}

    try:
        resolve_event(event)
    except Exception as e:
        raise ValueError(event) from e


@pytest.mark.asyncio
async def test_event_handler():
    """
    Test that the event handler will consume events and properly call
    registered handlers
    """

    handler = GhWebhookEventHandler()

    branch_protection_rule_events = 0

    @handler.on(BranchProtectionRuleCreated)
    async def handle_branch_protection_rule_created(event: BranchProtectionRuleCreated):
        nonlocal branch_protection_rule_events
        branch_protection_rule_events += 1

    for event in EVENTS:
        await handler.handle_event(event)

    assert branch_protection_rule_events > 0

from typing import Any, Dict, Union
from unittest import mock

import pytest
from pydantic import BaseModel

from gh_webhooks import GhWebhookEventHandler
from gh_webhooks.handler import __name__ as HANDLER_NAME


@pytest.mark.asyncio
async def test_event_handler():
    class A(BaseModel):
        a: int

    class B(BaseModel):
        b: str

    class Model(BaseModel):
        __root__: Union[A, B]

    def fake_resolve_event(event: Dict[str, Any], kind: str):
        return Model.parse_obj(event).__root__

    a_calls = 0
    b_calls = 0

    with mock.patch(HANDLER_NAME + ".resolve_event", fake_resolve_event):
        handler = GhWebhookEventHandler()

        @handler.on(A)
        async def handle_a(event: A):
            nonlocal a_calls
            a_calls += 1

        @handler.on(B)
        async def handle_b(event: B):
            nonlocal b_calls
            b_calls += 1

        await handler.handle_event({"a": 1}, "a")

        assert a_calls == 1
        assert b_calls == 0

        await handler.handle_event({"b": "hello"}, "b")

        assert a_calls == 1
        assert b_calls == 1

        second_b_calls = 0

        @handler.on(B)
        async def another_b_handler(event: B):
            nonlocal second_b_calls
            assert isinstance(event, B)
            assert event.b == "hello again"
            second_b_calls += 1

        await handler.handle_event({"b": "hello again"}, "b")

        assert a_calls == 1
        assert b_calls == 2
        assert second_b_calls == 1

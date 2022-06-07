gh-webhooks
=======================

``gh-webhooks`` is a library for building typed event handlers for GitHub webhook events.

Its primary offering is the class to register event handlers and process event JSON payloads:

.. autoclass:: gh_webhooks.GhWebhookEventHandler
   :members:

It autogenerates the types of the webhook payloads, which are available in ``gh_webhooks.types``.

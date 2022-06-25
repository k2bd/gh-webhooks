class GhWebhooksException(Exception):
    """
    Base Exception
    """


class NoMatchingModel(GhWebhooksException):
    """
    Raised when the event could not be matched to a model
    """

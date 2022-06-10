from pydantic import BaseModel, Extra


class GhWebhooksModel(BaseModel):
    class Config:
        extra = Extra.allow

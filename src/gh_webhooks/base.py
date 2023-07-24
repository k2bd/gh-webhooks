from pydantic import BaseModel


class GhWebhooksModel(BaseModel):
    class Config:
        extra = "allow"

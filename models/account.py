from beanie import Document
from typing import Literal
from datetime import datetime
from pydantic import Field
from bson import ObjectId

class Account(Document):
    user_id: ObjectId
    account_type: Literal["savings", "current"]
    balance: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "accounts"

    class Config:
        arbitrary_types_allowed = True

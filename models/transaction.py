from beanie import Document
from typing import Literal
from datetime import datetime
from bson import ObjectId
from pydantic import Field

class Transaction(Document):
    account_id: ObjectId
    transaction_type: Literal["deposit", "withdrawal"]
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "transactions"

    class Config:
        arbitrary_types_allowed = True

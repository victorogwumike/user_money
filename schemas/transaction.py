from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class TransactionCreate(BaseModel):
    transaction_type: Literal['deposit', 'withdrawal']
    amount: float


class TransactionResponse(BaseModel):
    id: str
    account_id: str
    transaction_type: str
    amount: float
    date: datetime

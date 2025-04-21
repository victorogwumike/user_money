from pydantic import BaseModel
from typing import Literal


class AccountCreate(BaseModel):
    account_type: Literal['savings', 'current']


class AccountResponse(BaseModel):
    id: str
    user_id: str
    account_type: str
    balance: float
    created_at: str

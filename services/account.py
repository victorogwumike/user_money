from models.account import Account
from fastapi import HTTPException
from beanie import PydanticObjectId


async def get_account_by_id(account_id: str, user_id: str):
    account = await Account.get(account_id)
    if not account or str(account.user_id) != user_id:
        raise HTTPException(status_code=403, detail="Account not found or unauthorized")
    return account

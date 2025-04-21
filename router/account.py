from fastapi import APIRouter, HTTPException, Depends
from models.account import Account
from schemas.account import AccountCreate, AccountResponse
from dependencies import get_current_user
from serialisers import account_serializer

router = APIRouter(prefix="/accounts", tags=["Account"])


@router.post("", response_model=AccountResponse)
async def create_account(account_data: AccountCreate, current_user=Depends(get_current_user)):
    new_account = Account(
        user_id=current_user.id,
        account_type=account_data.account_type,
        balance=0.0,
    )
    await new_account.insert()
    return account_serializer(new_account)


@router.get("/{id}", response_model=AccountResponse)
async def get_account(id: str, current_user=Depends(get_current_user)):
    account = await Account.get(id)
    if not account or str(account.user_id) != str(current_user.id):
        raise HTTPException(status_code=403, detail="Account not found or not authorized")
    return account_serializer(account)

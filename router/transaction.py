from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_current_user
from schemas.transaction import TransactionCreate, TransactionResponse
from services.transaction import perform_withdrawal
from services.account import get_account_by_id
from beanie import PydanticObjectId

router = APIRouter(prefix="/accounts", tags=["Transaction"])


@router.post("/{account_id}/withdraw", response_model=TransactionResponse)
async def withdraw(account_id: str, data: TransactionCreate, user=Depends(get_current_user)):
    if data.transaction_type != "withdrawal":
        raise HTTPException(status_code=400, detail="Invalid transaction type")

    account = await get_account_by_id(account_id, str(user.id))
    transaction = await perform_withdrawal(account, data.amount)
    return TransactionResponse(
        id=str(transaction.id),
        account_id=str(transaction.account_id),
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
        date=transaction.date
    )

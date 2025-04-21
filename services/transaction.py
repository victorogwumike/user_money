from beanie import PydanticObjectId
from datetime import datetime, timedelta
from models.transaction import Transaction
from models.account import Account
from fastapi import HTTPException


async def perform_withdrawal(account: Account, amount: float):
    if account.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    # Check withdrawal count today
    start_of_day = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)

    withdrawal_count = await Transaction.find(
        {
            "account_id": account.id,
            "transaction_type": "withdrawal",
            "date": {"$gte": start_of_day, "$lt": end_of_day}
        }
    ).count()

    if withdrawal_count >= 2:
        raise HTTPException(status_code=400, detail="Daily withdrawal limit reached (2 per day)")

    account.balance -= amount
    await account.save()

    transaction = Transaction(
        account_id=account.id,
        transaction_type="withdrawal",
        amount=amount,
        date=datetime.utcnow()
    )
    await transaction.insert()
    return transaction

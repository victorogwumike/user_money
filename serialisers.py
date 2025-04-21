from models.user import User
from models.account import Account
from models.transaction import Transaction


def user_serializer(user: User) -> dict:
    return {
        "id": str(user.id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "bvn": user.bvn,
    }


def account_serializer(account: Account) -> dict:
    return {
        "id": str(account.id),
        "user_id": str(account.user_id),
        "account_type": account.account_type,
        "balance": account.balance,
        "created_at": account.created_at.isoformat(),
    }


def transaction_serializer(transaction: Transaction) -> dict:
    return {
        "id": str(transaction.id),
        "account_id": str(transaction.account_id),
        "transaction_type": transaction.transaction_type,
        "amount": transaction.amount,
        "date": transaction.date.isoformat(),
    }

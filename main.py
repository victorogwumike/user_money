from fastapi import FastAPI
from database import init_db
import router.user as user_router
import router.account as account_router
import router.transaction as transaction_router

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

app.include_router(user_router.router)
app.include_router(account_router.router)
app.include_router(transaction_router.router)



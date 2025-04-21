import motor.motor_asyncio
from beanie import init_beanie
from models.user import User
from pymongo import mongo_client
from models.account import Account
from models.transaction import Transaction
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["wallet_app"]


async def init_db():
    await init_beanie(database=db, document_models=[User, Account, Transaction])

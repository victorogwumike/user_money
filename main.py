from pymongo import MongoClient
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()  # This loads environment variables from a .env file

import logging
import time

app = FastAPI()

# Retry logic to connect to MongoDB
def get_mongo_client():
    retries = 5
    while retries > 0:
        try:
            client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=500000)
            client.admin.command('ping')  # Test if MongoDB is responsive
            return client
        except Exception as e:
            logging.error(f"MongoDB connection failed: {e}")
            retries -= 1
            time.sleep(5)  # Wait before retrying

    raise Exception("Failed to connect to MongoDB after several attempts")

# Establish MongoDB connection
client = get_mongo_client()
db = client['mydatabase']

@app.get("/")
async def root():
    return {"message": "MongoDB connected successfully"}

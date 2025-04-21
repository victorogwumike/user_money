from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(Document):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    bvn: str
    password: str

    class Settings:
        name = "users"

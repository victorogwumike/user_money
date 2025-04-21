# routers/auth_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserLogin
from models.user import User
from services.auth import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/login")
async def login(user: UserLogin):
    db_user = await User.find_one(User.email == user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": str(db_user.id)}, 
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": token, "token_type": "bearer"}

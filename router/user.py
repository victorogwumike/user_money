from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from schemas.user import UserCreate
from auth import create_access_token
from passlib.hash import bcrypt
from serialisers import user_serializer
from services.user import get_user_by_email
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register")
async def register_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = bcrypt.hash(user.password)
    new_user = User(**user.dict(exclude={"password"}), password=hashed_password)
    await new_user.insert()
    return {"message": "User registered successfully"}


@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(form_data.username)
    if not user or not bcrypt.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/{id}")
async def get_user_info(id: str, current_user=Depends(lambda: None)):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_serializer(user)

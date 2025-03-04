from fastapi import APIRouter, Depends, HTTPException
from .services import AuthService, UserCreate
from .repository import InMemoryAuthRepository
from .aggregates import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

auth_repo = InMemoryAuthRepository()
auth_service = AuthService(auth_repo)

@router.post("/register")
async def register(user_data: UserCreate) -> User:
    try:
        return auth_service.register_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(username: str, password: str):
    user = auth_service.authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
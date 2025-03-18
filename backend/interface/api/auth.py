from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.authentication import UserAuthenticationService
from interface.dependencies import get_user_repository
from domain.repositories.user import UserRepository

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, user_repository: UserRepository = Depends(get_user_repository)):
    auth_service = UserAuthenticationService(user_repository)
    token = await auth_service.login(request.username, request.password)
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenResponse(access_token=token)

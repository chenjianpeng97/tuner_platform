from .aggregates import User, Role
from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class AuthService:
    def __init__(self, user_repository):
        self.user_repo = user_repository

    def register_user(self, user_data: UserCreate) -> User:
        hashed_password = f"hashed_{user_data.password}"  # 实际应使用密码哈希库
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password
        )
        return self.user_repo.save(new_user)

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = self.user_repo.find_by_username(username)
        if user and user.hashed_password == f"hashed_{password}":
            return user
        return None
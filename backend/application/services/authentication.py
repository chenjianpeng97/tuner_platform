from typing import Optional
from datetime import timedelta
from domain.models.user.entity import User
from domain.services.authentication import AuthenticationService
from domain.repositories.user import UserRepository

class UserAuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.auth_service = AuthenticationService()

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = await self.user_repository.get_by_username(username)
        if not user or not user.verify_password(password):
            return None
        return user

    def create_user_token(self, user: User) -> str:
        access_token = self.auth_service.create_access_token(
            data={"sub": str(user.id), "username": user.user_name}
        )
        return access_token

    async def login(self, username: str, password: str) -> Optional[str]:
        user = await self.authenticate_user(username, password)
        if not user:
            return None
        return self.create_user_token(user)

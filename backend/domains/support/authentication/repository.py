from typing import Optional
from .aggregates import User
from .services import UserCreate

class AuthRepository:
    def save(self, user: User) -> User:
        raise NotImplementedError
    
    def find_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError

class InMemoryAuthRepository(AuthRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User) -> User:
        if user.username in self.users:
            raise ValueError("Username already exists")
        self.users[user.username] = user
        return user

    def find_by_username(self, username: str) -> Optional[User]:
        return self.users.get(username)
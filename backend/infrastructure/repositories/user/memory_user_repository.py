from typing import Optional
from domain.models.auth.entity import User
from domain.repositories.user_repository import UserRepository

class MemoryUserRepository(UserRepository):
    def __init__(self,fake_data:dict):
        self.users = fake_data

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        # 先将列表形式的fake_data转换为以id为键的字典
        user_dict = {user['id']: user for user in self.users}
        return user_dict.get(user_id)
    def save(self,user:User)->Optional[None]:
        self.users.append(user)
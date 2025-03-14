from abc import ABC, abstractmethod
from typing import Optional
from domain.models.auth.entity import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass
    @abstractmethod
    def save(self,user:User)->Optional[None]:
        pass
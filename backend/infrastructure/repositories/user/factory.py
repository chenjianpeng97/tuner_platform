from typing import Optional
from infrastructure.repositories.user.sql_user_repository import SqlAlchemyUserRepository
from infrastructure.repositories.user.memory_user_repository import MemoryUserRepository
from infrastructure.repositories.base import BaseRepositoryFactory

from domain.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session




class UserRepositoryFactory(BaseRepositoryFactory):
    @classmethod
    def get_sql_repository(cls, session):
        return SqlAlchemyUserRepository(session)

    @classmethod
    def get_memory_repository(cls):
        return MemoryUserRepository()
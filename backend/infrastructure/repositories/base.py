from abc import ABC, abstractmethod
from setup.config import settings
class BaseRepositoryFactory(ABC):
    @classmethod
    def create(cls, session=None):
        if settings.ENVIRONMENT == 'production':
            return cls.get_sql_repository(session)
        return cls.get_memory_repository()

    @classmethod
    @abstractmethod
    def get_sql_repository(cls, session):
        pass

    @classmethod
    @abstractmethod
    def get_memory_repository(cls):
        pass

from typing import Optional
from sqlalchemy.orm import Session
from domain.models.auth.entity import User
from domain.repositories.user_repository import UserRepository
from infrastructure.database.models import UserDBModel

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        db_user = self.session.query(UserDBModel).filter_by(id=user_id).first()
        if db_user:
            return User(id=db_user.id, user_name=db_user.user_name)
        return None
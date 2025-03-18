from pydantic import BaseModel, Field, model_validator, PrivateAttr
from passlib.context import CryptContext


class User(BaseModel):
    id: int | None = None
    user_name: str = Field(..., description="用户名")
    password: str = Field(..., description="密码")
    _pwd_context: CryptContext = PrivateAttr(default=CryptContext(schemes=["bcrypt"], deprecated="auto"))

    def verify_password(self, plain_password: str) -> bool:
        return self._pwd_context.verify(plain_password, self.password)

    def hash_password(self, password: str) -> str:
        return self._pwd_context.hash(password)

    @model_validator(mode='before')
    def hash_password_before_save(cls, values):
        if isinstance(values, dict) and 'password' in values:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            values['password'] = pwd_context.hash(values['password'])
        return values

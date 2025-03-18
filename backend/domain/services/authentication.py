from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from domain.models.user.entity import User

SECRET_KEY = "your-secret-key"  # 在生产环境中应该从环境变量获取
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthenticationService:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise ValueError("Could not validate credentials")

    @staticmethod
    def get_current_user(authorization: str) -> int:
        try:
            token = authorization.split(" ")[1]  # Bearer token
            payload = AuthenticationService.verify_token(token)
            user_id = payload.get("sub")
            if user_id is None:
                raise ValueError("Token is invalid")
            return int(user_id)
        except Exception as e:
            raise ValueError("Invalid authentication credentials")
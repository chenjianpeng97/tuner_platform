from pydantic import BaseModel,Field,model_validator,PrivateAttr

class User(BaseModel):
    id: int | None = None
    user_name: str = Field(..., description="用户名")
    
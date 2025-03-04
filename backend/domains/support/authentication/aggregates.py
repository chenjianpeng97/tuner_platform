from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Role(BaseModel):
    name: str
    permissions: list[str]

class User(BaseModel):
    model_config = {'arbitrary_types_allowed': True}
    
    username: str
    email: str
    hashed_password: str
    roles: list[Role] = []
    is_active: bool = True
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def add_role(self, role: Role):
        if role not in self.roles:
            self.roles.append(role)
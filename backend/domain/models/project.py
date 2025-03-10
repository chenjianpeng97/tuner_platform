from uuid import UUID

from pydantic import BaseModel,Field,model_validator

# from domain.vo import Name,Description
# from exceptions import ProjectError

class Project(BaseModel):
    id: int | None = None
    name: str = Field(..., description="项目名称")
    description: str = Field(..., description="项目描述")

    @model_validator(mode="after")
    def validate_name(self):
        if len(self.name) > 100:
            raise ProjectError("项目名称过长")
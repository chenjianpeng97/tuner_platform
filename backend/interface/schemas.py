from pydantic import BaseModel, Field
from typing import Optional

class CreateProjectRequest(BaseModel):
    """创建项目请求模型"""
    project_name: str = Field(..., description="项目名称")
    description: Optional[str] = Field(None, description="项目描述")

class ProjectResponse(BaseModel):
    """项目响应模型"""
    id: int
    project_name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True
"""project related entity"""
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field, model_validator
from domain.exceptions import ProjectError

from domain.models.user.entity import User
from domain.models.test.entity import TestRun
from domain.models.test.vo import TestRunStatus


class Project(BaseModel):
    """project entity"""
    id: int | None = None
    project_name: str = Field(..., description="项目名称")
    description: str | None = Field(None, description="项目描述")
    creator_id: int = Field(..., description="创建人ID")
    test_runs: list[TestRun] | None = Field(None, description="项目下的测试情况")

    @model_validator(mode="after")
    def validate_project_name(self):
        """验证项目名称长度是否合法
        Raises:
            ProjectError: 当项目名称长度超过100个字符时抛出异常
        """
        if len(self.project_name) > 100:
            raise ProjectError("项目名称过长")
        return self
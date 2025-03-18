"""project related entity"""
from typing import Optional

from pydantic import BaseModel, Field, model_validator
from domain.exceptions import ProjectNameError

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

    def get_last_test_run_status(self) -> Optional[TestRunStatus]:
        """获取项目下最后一次测试的状态
        Returns:
            TestRunStatus: 项目下最后一次测试的状态
        """
        if self.test_runs is None or len(self.test_runs) == 0:
            return None
        return self.test_runs[-1].test_run_status

    @model_validator(mode="after")
    def validate_project_name(self):
        """验证项目名称长度是否合法
        Raises:
            ProjectError: 当项目名称长度超过100个字符时抛出异常
        """
        if len(self.project_name) > 100:
            raise ProjectNameError("项目名称过长")
        return self


from pydantic import BaseModel,Field,model_validator
from typing import TYPE_CHECKING
from exceptions import ProjectError
from domain.models.test.vo import TestRunStatus
# from domain.vo import Name,Description
# from exceptions import ProjectError
if TYPE_CHECKING:
    from domain.models.test_run import TestRuns

class Project(BaseModel):
    id: int | None = None
    project_name: str = Field(..., description="项目名称")
    description: str | None = Field(None, description="项目描述")
    last_test_run_statuses: TestRunStatus | None = Field(None, description="测试执行情况")
    creator_id: int = Field(..., description="创建人ID")
    @model_validator(mode="after")
    def validate_name(self):
        if len(self.name) > 100:
            raise ProjectError("项目名称过长")
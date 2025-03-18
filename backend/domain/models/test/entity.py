from pydantic import BaseModel, Field, model_validator
from domain.models.test.vo import TestRunStatus


class TestRun(BaseModel):
    id: int = None
    test_run_name: str
    test_run_status: TestRunStatus

    class Config:
        orm_mode = True

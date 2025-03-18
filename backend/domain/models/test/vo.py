from pydantic import BaseModel


class TestRunStatus(BaseModel):
    passed: int = 0
    failed: int = 0
    undefined: int = 0

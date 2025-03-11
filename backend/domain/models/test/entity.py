from pydantic import BaseModel,Field,model_validator

class TestRuns(BaseModel):
    id:int = None
    test_run_name:str
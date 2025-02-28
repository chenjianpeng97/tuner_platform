from pydantic import BaseModel,Field,model_validator
from typing import List, Optional
class Background(BaseModel):
    """Background content"""
    name: str = Field(..., title="Background name")
    description: Optional[str] = Field(None, title="Background description")
    tags: List[str] = Field([], title="Background tags")
    steps: List[str] = Field([], title="Background steps")
    attachment: Optional[List[str]] = Field(None, title="Attachment")
class Scenario(BaseModel):
    """Scenario content"""
    name: str = Field(..., title="Scenario name")
    description: Optional[str] = Field(None, title="Scenario description")
    tags: List[str] = Field([], title="Scenario tags")
    steps: List[str] = Field([], title="Scenario steps")
    attachment: Optional[List[str]] = Field(None, title="Attachment")
class ScenarioOutline(BaseModel):
    """Scenario outline content"""
    name: str = Field(..., title="Scenario outline name")
    description: Optional[str] = Field(None, title="Scenario outline description")
    tags: List[str] = Field([], title="Scenario outline tags")
    steps: List[str] = Field([], title="Scenario outline steps")
    examples: List[str] = Field([], title="Scenario outline examples")
    attachment: Optional[List[str]] = Field(None, title="Attachment")
class Rule(BaseModel):
    """Rule content"""
    name : str = Field(..., title="Rule name")

class Feature(BaseModel):
    """Feature content"""
    name: str = Field(..., title="Feature name")
    description: Optional[str] = Field(None, title="Feature description")
    tags: List[str] = Field([], title="Feature tags")
    sub_features: Optional[List['Feature']] = Field([], title="Sub features")
    attachment: Optional[List[str]] = Field(None, title="Attachment")
    
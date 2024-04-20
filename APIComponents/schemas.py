from pydantic import BaseModel, field_validator
from datetime import datetime

class Todo(BaseModel):
    
    task: str
    description: str
    done: bool
    
from pydantic import BaseModel, field_validator
from datetime import datetime

class Todo(BaseModel):
    
    task: str
    description: str
    done: bool


class ShowToDo(Todo):
    task: str
    description: str
    done: str
    class Config():
        orm_mode = True
    
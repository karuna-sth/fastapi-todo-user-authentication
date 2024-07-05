from pydantic import BaseModel
from typing import List

class TodoBase(BaseModel):
    
    task: str
    description: str
    done: bool

class Todo(TodoBase):
    class Config():
        from_attributes = True 

class User(BaseModel):
    username: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    username: str
    email: str
    todos: List[Todo] = []
    class Config():
        from_attributes = True


class ShowToDo(Todo):
    task: str
    description: str
    done: bool
    created_by: ShowUser
    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

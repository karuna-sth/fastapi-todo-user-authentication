from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


from APIComponents.database import base

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    description = Column(String)
    done = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("Users", back_populates="todos")
    

class Users(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String )
    email = Column(String)
    password = Column(String)

    todos = relationship("Todo", back_populates="created_by")
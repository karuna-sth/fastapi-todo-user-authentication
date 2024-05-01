from sqlalchemy import Column, Integer, String, Boolean
from APIComponents.database import base

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    description = Column(String)
    done = Column(Boolean)



    
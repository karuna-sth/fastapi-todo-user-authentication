from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str
    description: str
    published: bool
    published_date: datetime = datetime.now()
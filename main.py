import uvicorn
from fastapi import FastAPI

import APIComponents.models as models
from APIComponents.database import engine
from APIComponents.routers import todo, users, authentication

models.base.metadata.create_all(engine)

app = FastAPI()

app.include_router(todo.router)
app.include_router(users.router)
app.include_router(authentication.router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
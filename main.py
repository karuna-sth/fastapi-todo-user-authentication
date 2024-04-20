import uvicorn
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session


from APIComponents.schemas import Todo
import APIComponents.models as models
from APIComponents.database import engine, sessionLocal

models.base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create-todo", status_code=status.HTTP_201_CREATED )
def create_todo(request: Todo, db: Session = Depends(get_db)):
    new_todo = models.Todo(task=request.task, description= request.description, done=request.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    print(todos)
    return todos


@app.get("/todo/{id}", status_code=200)
def show_selected_todo(id, response: Response, db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detial': f"The todo with {id} not available."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The todo with {id} not available.")
    return todo


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_selected_todo(id, db:Session = Depends(get_db)):
    db.query(models.Todo).filter(models.Todo.id==id).delete(synchronize_session=False)
    db.commit()
    return 'Delete Successfull'

@app.put("/todo/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(id, request: Todo, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} todo not Found")
    todo.update(request.model_dump())
    db.commit()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
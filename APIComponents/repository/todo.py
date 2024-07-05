from sqlalchemy.orm import Session
from fastapi import  HTTPException, status


from APIComponents import models, schemas


def create(db: Session, request: schemas.Todo):
    new_todo = models.Todo(task=request.task, description= request.description, done=request.done, user_id = 1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_selected(id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'detial': f"The todo with {id} not available."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The todo with {id} not available.")
    return todo

def get_all(db: Session):
    todos = db.query(models.Todo).all()
    return todos

def delete_selected(id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The todo of id {id} not found")
    todo.delete(synchronize_session=False)
    db.commit()
    return 'Delete Successfull'

def update(id:int, db: Session, request: schemas.Todo):
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} todo not Found")
    todo.update(request.model_dump())
    db.commit()
    return "Updated Sucessfull"
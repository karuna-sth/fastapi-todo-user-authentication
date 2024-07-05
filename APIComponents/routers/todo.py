from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from APIComponents.routers import oauth2

from APIComponents import  database, schemas
from APIComponents.repository import todo


router = APIRouter(
    prefix="/todo",
    tags=["todos"]
)

@router.get("/{id}", status_code=200, response_model=schemas.ShowToDo)
def show_selected_todo(id, response: Response, db:Session=Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.get_selected(id=id, db=db)
   

@router.post("/create", status_code=status.HTTP_201_CREATED )
def create_todo(request: schemas.Todo, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.create(db=db, request=request)

@router.get("/", response_model=List[schemas.ShowToDo])
def get_todos(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.get_all(db=db)



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_selected_todo(id, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.delete_selected(id=id, db=db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(id, request: schemas.Todo, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.update(id=id, db=db, request=request)


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from APIComponents import database, schemas
from APIComponents.repository import user

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(db=db, request=request)

@router.get("/{id}", status_code=200, response_model=schemas.ShowUser)
def show_selected_user(id, db:Session=Depends(database.get_db)):
    return user.get_user(id=id, db=db)
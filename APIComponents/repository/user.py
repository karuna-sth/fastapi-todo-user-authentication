from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from APIComponents import models, hashing, schemas



def create(db:Session, request: schemas.User):
    new_user = models.Users(username = request.username, email=request.email, password=hashing.Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db:Session):
    user = db.query(models.Users).filter(models.Users.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail=f"No user with id {id}")
    return user
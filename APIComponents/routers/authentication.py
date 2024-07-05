from fastapi  import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import  timedelta
from fastapi.security import OAuth2PasswordRequestForm

from APIComponents import schemas, models, database, hashing
from APIComponents.routers import JWTtoken

router = APIRouter(
    prefix="/authenticate",
    tags=["Authnetication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credentials not found")
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password not correct")
    
    access_token_expires =  timedelta(minutes=JWTtoken.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token  = JWTtoken.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return schemas.Token(access_token=access_token, token_type="bearer")

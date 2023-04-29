from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from settings import get_db

from user.models import *
from user.schemas import *

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/create', status_code=201, response_model=UserOut)
def create_user(request: UserIn, db: Session=Depends(get_db)):
    new_user = UserModel(full_name=request.full_name, email=request.email, password=hashPassword(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        'detail': 'User created successfully', 
        'data': new_user
        }
    
    
    
@router.get('/detail/{id}', status_code=200, response_model=UserOut)
def get_user(id, db: Session=Depends(get_db)):  
    user = db.query(UserModel).filter(UserModel.id==id).first() 
    
    if not user:
        raise HTTPException(status_code=404, detail="No user found")
    return user



@router.patch('/update/{id}', status_code=200, response_model=UserOut)
def update_user(id, full_name: str, db: Session=Depends(get_db)):  
    user = db.query(UserModel).filter(UserModel.id==id)
    if not user.first():
        raise HTTPException(status_code=404, detail="No user found")
    user.update({'full_name': full_name})
    db.commit()
    return user.first()
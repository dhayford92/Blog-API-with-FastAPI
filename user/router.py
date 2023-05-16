from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from user.models import *
from user.schemas import *



router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/create', status_code=201, response_model=UserPydantic)
async def create_user(request: UserPydanticAuth):
    pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")
    
    # if User.filter(email=request.email).first():
    #     raise HTTPException(status_code=404, detail="Email already registered")
    
    user = await User.create(**request.json(exclude_unset=True))
    return {'message': 'Account created successfully', 'data': UserPydantic.from_tortoise_orm(user)}



@router.post('/login', status_code=200)
def login(request: UserLogin):
    pass



@router.get('/detail/{id}', status_code=200, response_model=UserOut)
async def get_user(id): 
    try: 
        user = await User.get(id=id)
    except:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch('/update/{id}', status_code=200, response_model=UserOut)
async def update_user(id, full_name: str):  
    try: 
        user = await User.get(id=id)
        user.full_name = full_name
        user.save()
    except:
        raise HTTPException(status_code=404, detail="User not found")
    return {'message': 'User updated successfully', 'data': user }


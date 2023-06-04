from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from user.models import *
from user.schemas import *
from fastapi_jwt_auth import AuthJWT



router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/create', status_code=201)
async def create_user(request: UserRegister):
    pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

    users = await User.filter(email=request.email).all()
    if users:
        raise HTTPException(status_code=404, detail="Email already registered")

    user = User(full_name=request.full_name, email=request.email)
    user.password = pwd_cxt.hash(request.password)

    await user.save()
    return {'message': 'Account created successfully'}



@router.post('/login', status_code=200)
async def login(req: UserLogin, authenticate: AuthJWT=Depends()):
    try:
        user = await User.get(email=req.email)
    except:
        raise HTTPException(status_code=401, detail="User does not exist")
    if user.verify_password(req.password):
        if user.is_active:
            user_data = await UserOutPydantic.from_tortoise_orm(user)
            user_data_tokens = user.tokens(authenticate)
            user_data_dict = user_data.dict()
            user_data_dict.update(user_data_tokens)
            return user_data_dict
        else:
            raise HTTPException(status_code=401, detail="Account not activated")
    raise HTTPException(status_code=401, detail="Invalid Credentials")
     


@router.get('/refresh-token', status_code=200)
async def reset_token(authorization: AuthJWT=Depends()):
    try:
        authorization.jwt_refresh_token_required()
    except:
        raise HTTPException(status_code=401, detail='User not authorized')
    user = authorization.get_jwt_subject()
    access_token = await authorization.create_access_token(subject=user)
    return {'access_token': access_token}



@router.get('/detail/{id}', status_code=200, response_model=UserOut)
async def get_user(id, auth: AuthJWT= Depends()): 
    try:
        auth.get_jwt_subject()
    except:
        raise HTTPException(status_code=401, detail="Unauthorized access")
    try: 
        user = await User.get(id=id)
        return user
    except:
        raise HTTPException(status_code=404, detail="User not found")
    





@router.patch('/update/{id}', status_code=200)
async def update_user(id, full_name: str):  
    try: 
        user = await User.get(id=id)
        user.full_name = full_name
        await user.save()
    except:
        raise HTTPException(status_code=404, detail="User not found")
    return {'message': 'User updated successfully', 'data': user}


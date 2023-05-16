from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from typing import Union, Any
# from settings import *
# from jose import jwt, JWTError
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator





class User(models.Model):
    full_name = fields.CharField(max_length=200)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=200, null=True)
    is_active = fields.BooleanField(default=True, null=True)
    created = fields.DatetimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        table = "users"
        
    def verify_password(self, password: str) -> bool:
        pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")
        return pwd_cxt.verify(password, self.password)
    
    

UserPydantic = pydantic_model_creator(User, name="User")
UserPydanticAuth = pydantic_model_creator(User, name="UserAuth", exclude_readonly=True)   



    
    

# def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
#     return encoded_jwt


# def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
#     return encoded_jwt
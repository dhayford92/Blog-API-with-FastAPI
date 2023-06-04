from passlib.context import CryptContext
from tortoise import fields, models
from fastapi_jwt_auth import AuthJWT
from tortoise.contrib.pydantic import pydantic_model_creator



class Auth:
    
    def get_current_user():
        pass
    
    def get_admin_current_user():
        pass







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
    
    def tokens(self, auth = AuthJWT):
        access_token = auth.create_access_token(subject=self.email)
        refresh_token = auth.create_refresh_token(subject=self.email)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

    
    

UserOutPydantic = pydantic_model_creator(User, name="User", exclude=('password', 'created', ))
UserPydanticAuth = pydantic_model_creator(User, name="UserAuth", exclude_readonly=True)   

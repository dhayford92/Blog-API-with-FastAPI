from pydantic import BaseModel, EmailStr




class UserRegister(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    
    class Config():
        orm_mode = True

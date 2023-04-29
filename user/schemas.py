from pydantic import BaseModel, EmailStr




class UserIn(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    

class UserOut(BaseModel):
    email: str
    full_name: str | None = None
    
    class Config():
        orm_mode = True

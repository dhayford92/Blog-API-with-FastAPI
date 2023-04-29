from pydantic import BaseModel
from user.schemas import UserOut





# blog base model
class Blog(BaseModel):
    title: str
    author: str
    body: str | None = None
    published: bool = True
    
    
class ShowBlog(BaseModel):
    title: str
    author: UserOut
    body: str | None = None
    
    class Config():
        orm_mode = True

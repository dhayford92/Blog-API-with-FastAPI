from pydantic import BaseModel
from blog.models import *
from user.schemas import UserOut
from fastapi import UploadFile, File
from tortoise.contrib.pydantic import pydantic_model_creator as serializer



class CategoryIn(BaseModel):
    image: UploadFile = File(...)
    name: str
    

CategorySerializer = serializer(
    Category, name="Category"
)


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

from fastapi import APIRouter, Depends, HTTPException
from .models import *



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.post('/category/', status_code=201)
async def create_category(req: CategoryInSerializer):
    await Category.create(name=req.name)
    return {
        'message': 'Category created successfully'
    }





@router.post('/blog', status_code=201)
def create_blog():
    pass




@router.get('/blog', status_code=200)
def all_blogs():
    pass




@router.get('/blog/{id}', status_code=200)
def detail_blog(id):
    pass




@router.put('blog/update/{id}', status_code=200)
def update_blog(id):
    pass
    
    
    
@router.delete('blog/delete/{id}', status_code=204)
def delete_blog(id):
    pass
    
    
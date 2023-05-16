from fastapi import APIRouter, Depends, HTTPException
from .schemas import Blog, ShowBlog
from .models import *



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router('/category/', status_code=201)
async def create_category(req: CategoryInSerializer):
    category = await Category.create(**req.json(exclude_unset=True))
    return {
        'message': 'Category created successfully',
        'data': ''
    }










@router.post('/create', status_code=201)
def create_blog(blog: Blog):
    pass




@router.get('/', status_code=200)
def all_blogs():
    pass




@router.get('/detail/{id}', status_code=200)
def detail_blog(id):
    pass




@router.put('/update/{id}', status_code=202, response_model=ShowBlog)
def update_blog(id, new_blog: Blog):
    pass
    
    
    
@router.delete('/delete/{id}', status_code=204)
def delete_blog(id):
    pass
    
    
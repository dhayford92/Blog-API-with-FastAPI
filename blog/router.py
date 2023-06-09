from typing import List
from fastapi import APIRouter, Depends, HTTPException

from blog.schemas import CategoryIn, CategorySerializer
from blog.utils import remove_file
from user.router import get_current_user
from .utils import upload_file
from .models import *



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


# --- create category post ---
@router.post('/category/', status_code=201)
async def create_category(req: CategoryIn = Depends(), auth_user: get_current_user = Depends()):
    catData = req.dict(exclude_unset=True)
    try:
        catData['image'] = await upload_file('category', catData['image'])
    except Exception as e:
        raise e
    await Category.create(**catData)
    return {
        'message': 'Category created successfully'
    }


@router.get('/category/', status_code=201, response_model = List[CategorySerializer])
async def get_categories(auth_user: get_current_user = Depends()):
    categories = await Category.all()
    return categories


@router.delete('/category/{category_id}', status_code=204)
async def delete_category(category_id: int, auth_user: get_current_user = Depends()):
    try:
        category = await Category.get(id=category_id)
    except:
        raise HTTPException(status_code=404, detail='Category not found')
    remove_file(category.image)
    await category.delete()




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
    
    
from fastapi import APIRouter, Depends, HTTPException
from settings import get_db
from .schemas import Blog, ShowBlog
from .models import BlogModel
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)



@router.post('/create', status_code=201)
def create_blog(blog: Blog, db: Session = Depends(get_db)):
    
    new_blog = BlogModel(title=blog.title, body=blog.body, author=blog.author, publish=blog.published)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog




@router.get('/', status_code=200)
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs




@router.get('/detail/{id}', status_code=200)
def detail_blog(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail='Blog not found')
    
    return blog




@router.put('/update/{id}', status_code=202, response_model=ShowBlog)
def update_blog(id, new_blog: Blog, db: Session=Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail='Blog not found')
    
    blog.update(new_blog)
    db.commit()
    
    return blog.first()
    
    
    
@router.delete('/delete/{id}', status_code=204)
def update_blog(id, db: Session=Depends(get_db)):
    db.query(BlogModel).filter(BlogModel.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted successfully"}
    
    
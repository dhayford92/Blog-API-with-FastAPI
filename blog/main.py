from fastapi import FastAPI, Depends, HTTPException
from .schemas import Blog
from .models import Base, BlogModel
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()




@app.post('/blog/create', status_code=201)
def create_blog(blog: Blog, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=blog.title, body=blog.body, author=blog.author, publish=blog.published)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog




@app.get('/blog/', status_code=200)
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs




@app.get('/blog/{id}', status_code=200)
def detail_blog(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail='Blog not found')
    
    return blog
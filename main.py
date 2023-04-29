from fastapi import FastAPI, Depends
from settings import Base, engine
from blog.router import router as blog_router
from user.router import router as user_router


Base.metadata.create_all(engine)


app = FastAPI(
    title="Blog API",
    description="Something about my blog application build with FastAPI",
    version="1.0"
)


app.include_router(user_router)
app.include_router(blog_router)
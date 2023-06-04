from fastapi import FastAPI
from blog.router import router as blog_router
from user.router import router as user_router
from tortoise.contrib.fastapi import register_tortoise
from settings import SecretKey, model_apps
from fastapi_jwt_auth import AuthJWT



app = FastAPI(
    title="Blog API",
    description="Something about my blog application build with FastAPI",
    version="1.0"
)

@AuthJWT.load_config
def get_config():
    return SecretKey()

app.include_router(user_router)
app.include_router(blog_router)


register_tortoise(
    app, 
    db_url='sqlite://db.sqlite3',
    modules={'models': model_apps}, 
    generate_schemas=True,
    add_exception_handlers=True
)
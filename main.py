from fastapi import FastAPI
from blog.router import router as blog_router
from user.router import router as user_router
from tortoise.contrib.fastapi import register_tortoise
from settings import SecretKey, model_apps, tortoise_config
from fastapi_jwt_auth import AuthJWT
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Blog API",
    description="Something about my blog application build with FastAPI",
    version="1.0",
    contact = {
        "name": "Denzel Hayford",
        "url": "http://example.com/contact/",
        "email": "denkin.dh@gmail.com",
    },
)

@AuthJWT.load_config
def get_config():
    return SecretKey()

# ---- middleware ------
origins = [
    "http://localhost:8080",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(blog_router)

app.mount("/media", StaticFiles(directory="media"), name="media")



# -- database connection setup --- 
register_tortoise(
    app, 
    # db_url='sqlite://db.sqlite3',
    modules={'models': model_apps}, 
    config=tortoise_config,
    generate_schemas=True,
    add_exception_handlers=True
)
from tortoise import Tortoise
from pydantic import BaseModel


# -----Created models ------
model_apps = [
    'user.models',
    'blog.models'
]

# ---- Auth Key -----
AUTH_SECRET_KEY = '05f592048b7da6b40cd3d16f3b894490feae1823c334f6ff06edc27b8cc765b6'
class SecretKey(BaseModel):
    authjwt_secret_key: str = AUTH_SECRET_KEY
    



tortoise_config = {
    "apps": {
        "models": {
            "models": model_apps,
            "default_connection": "default",
        },
    },
    "connections": {
        "default": {
            "engine": "tortoise.backends.sqlite",
            "credentials": {
                "file_path": "db.sqlite3",
            },
        },
    },
}
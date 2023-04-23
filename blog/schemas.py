from pydantic import BaseModel




# blog base model
class Blog(BaseModel):
    title: str
    author: str
    body: str | None = None
    published: bool = True
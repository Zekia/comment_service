from typing import Optional
from pydantic import BaseModel, Field

class CommentUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    content: Optional[str]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Terrible place",
                "author": "f_r_gaudry",
                "content": "Found hair in plate",
                "image": "hair.png"
            }
        }

class ThreadPost(BaseModel):
    title: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Pizzeria pepperoni",
            }
        }


class CommentPost(BaseModel):
    thread_id: str = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    content: str = Field(...)
    image: str = Field(...)
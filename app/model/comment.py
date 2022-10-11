import uuid

from pydantic import BaseModel, Field


class Comment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    content: str = Field(...)
    image: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Delicious place",
                "author": "f_r_gaudry",
                "content": "Amazing meals and service",
                "image": "meal.png"
            }
        }

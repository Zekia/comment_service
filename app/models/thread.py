import uuid
from typing import List

from pydantic import BaseModel, Field

from app.models.comment import Comment


class Thread(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    comments: List[Comment] = []

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Pizzeria pepperoni",
                "comments": []
            }
        }
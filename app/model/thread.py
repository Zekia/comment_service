import uuid
from typing import List

from pydantic import BaseModel, Field

from app.model.comment import Comment


class Thread(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    comments: List[Comment] = []

    def has_comment(self, comment: Comment):
        for i in range(len(self.comments)):
            if self.comments[i].id == comment.id:
                return True
        return False

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Pizzeria pepperoni",
                "comments": []
            }
        }
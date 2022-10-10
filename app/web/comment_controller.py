import json

from fastapi import APIRouter, Body, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder

from app.dtos import CommentPost
from app.models.comment import Comment

router = APIRouter()


@router.post("/", response_description="Create a new comment", status_code=status.HTTP_201_CREATED, response_model=Comment)
def create_comment(request: Request, comment_post: CommentPost = Body(...)):
    new_comment = Comment(title=comment_post.title,
                          content=comment_post.content,
                          author=comment_post.author,
                          image=comment_post.image
                          ),
    new_comment_as_json = jsonable_encoder(new_comment)[0]
    update_result = request.app.database["threads"].update_one(
        {"_id": comment_post.thread_id},
        {"$push": {"comments": new_comment_as_json}}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Thread with ID {comment_post.thread_id} not found")
    return new_comment_as_json
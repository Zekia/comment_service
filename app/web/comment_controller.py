from fastapi import APIRouter, Body, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from app.di_container import DIContainer
from app.infra.comment_respository_mongo import CommentRepositoryException
from app.repository.comment_repository import CommentRepository

from app.web.dtos import CommentPost
from app.model.comment import Comment

router = APIRouter()


@router.put("/", response_description="Create a new comment", status_code=status.HTTP_201_CREATED, response_model=Comment)
def create_comment(
        request: Request,
        comment_post: CommentPost = Body(...),
        comment_repository: CommentRepository = Depends(DIContainer().get(CommentRepository))
):
    new_comment = Comment(title=comment_post.title,
                          content=comment_post.content,
                          author=comment_post.author,
                          image=comment_post.image
                          ),
    new_comment = new_comment[0]
    try:
        comment_repository.create_comment(new_comment, comment_post.thread_id, request.app)

    except CommentRepositoryException as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                      detail=str(err))

    return jsonable_encoder(new_comment)
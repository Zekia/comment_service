from fastapi import APIRouter, Body, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from app.infra.comment_mongo_repository import CommentRepositoryException
from app.web.dtos import CommentPost
from app.model.comment import Comment
from app.web.factory.comment_repository_factory import CommentRepositoryFactory

router = APIRouter()


@router.put("/", response_description="Create a new comment", status_code=status.HTTP_201_CREATED,
            response_model=Comment)
def create_comment(
        request: Request,
        comment_post: CommentPost = Body(...)
):
    comment_repository = CommentRepositoryFactory().from_request(request)

    try:
        new_comment = Comment(
            title=comment_post.title,
            content=comment_post.content,
            author=comment_post.author,
            image=comment_post.image
        )

        comment_repository.add_comment(new_comment, comment_post.thread_id)

    except CommentRepositoryException as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(err))

    return jsonable_encoder(new_comment)

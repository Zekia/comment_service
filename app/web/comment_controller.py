from fastapi import APIRouter, Body, Request, status, HTTPException, Response
from app.web.dtos import CommentPost
from app.model.comment import Comment
from app.web.factory.comment_repository_factory import CommentRepositoryFactory
from app.web.factory.thread_repository_factory import ThreadRepositoryFactory

router = APIRouter()


@router.put("/{id}", response_description="Create a new comment",
            response_model=Comment)
def put_comment(
        id: str,
        request: Request,
        response: Response,
        comment_post: CommentPost = Body(...)
) -> Comment:
    new_comment = Comment(_id=id, **comment_post.dict())
    thread_repository = ThreadRepositoryFactory().from_request(request)
    thread = thread_repository.find_with_id(comment_post.thread_id)
    if thread is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Thread with ID {comment_post.thread_id} not found")
    thread_index = None
    for i in range(len(thread.comments)):
        if thread.comments[i].id == new_comment.id:
            thread_index = i
            thread.comments.pop(thread_index)
            thread.comments.insert(thread_index, new_comment)
            thread_repository.update_thread(thread)
            response.status_code = status.HTTP_200_OK

    if thread_index is None:
        comment_repository = CommentRepositoryFactory().from_request(request)
        comment_repository.add_comment(new_comment, comment_post.thread_id)
        response.status_code = status.HTTP_201_CREATED
    return new_comment

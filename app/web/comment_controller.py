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

    index_of_comment_to_in_thread = get_index_comment_to_update(new_comment, thread)

    if index_of_comment_to_in_thread is None:
        add_comment(comment_post.thread_id, new_comment, request, response)
    else:
        update_comment(new_comment, thread, response, request)
    return new_comment


def add_comment(thread_id, new_comment, request, response):
    comment_repository = CommentRepositoryFactory().from_request(request)
    comment_repository.add_comment(new_comment, thread_id)
    response.status_code = status.HTTP_201_CREATED


def update_comment(new_comment, thread, response, request):
    comment_repository = CommentRepositoryFactory().from_request(request)
    comment_repository.update_comment(new_comment, thread.id)
    response.status_code = status.HTTP_200_OK


def get_index_comment_to_update(new_comment, thread):
    comment_index = None
    for i in range(len(thread.comments)):
        if thread.comments[i].id == new_comment.id:
            return i
    return comment_index

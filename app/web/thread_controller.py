from fastapi import APIRouter, Response, Body, Request, status, HTTPException
from typing import List
from app.web.dtos import ThreadPost, DeleteResult
from app.model.thread import Thread
from app.web.factory.thread_repository_factory import ThreadRepositoryFactory

router = APIRouter()


@router.get("/", response_description="Get all the threads", status_code=status.HTTP_200_OK,
            response_model=List[Thread])
def get_all_threads(
        request: Request,
):
    thread_repository = ThreadRepositoryFactory().from_request(request)
    return thread_repository.find_all()


@router.get("/{id}", response_description="Get a single thread by id", response_model=Thread)
def get_a_thread(
        id: str,
        request: Request
):
    thread_repository = ThreadRepositoryFactory().from_request(request)
    thread = thread_repository.find_with_id(id)
    if thread:
        return thread
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f'Unknown thread {id}')


@router.put("/{thread_id}", response_description="Create or update a thread", response_model=Thread)
def put_thread(thread_id: str, request: Request, response: Response, thread_post: ThreadPost = Body(...)) -> Thread:
    thread_repository = ThreadRepositoryFactory().from_request(request)
    existing_thread = thread_repository.find_with_id(thread_id)
    if existing_thread is None:
        updated_thread = create_thread(response, thread_id, thread_post, thread_repository)
    else:
        updated_thread = update_thread(existing_thread, thread_post, thread_repository, response)
    return updated_thread


def create_thread(response, thread_id, thread_post, thread_repository) -> Thread:
    thread = Thread(_id=thread_id, title=thread_post.title)
    thread_repository.add_thread(thread)
    response.status_code = status.HTTP_201_CREATED
    return thread


def update_thread(thread, thread_post, thread_repository, response) -> Thread:
    new_thread = thread.copy(update=thread_post.dict())  # merge the 2 versions of the thread
    thread_repository.update_thread(new_thread)
    response.status_code = status.HTTP_200_OK
    return new_thread


@router.delete("/{id}", response_description="Delete a thread", response_model=DeleteResult)
def delete_thread(id: str, request: Request, response: Response):
    delete_result = request.app.database["threads"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return DeleteResult(id=id)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Thread with ID {id} not found")

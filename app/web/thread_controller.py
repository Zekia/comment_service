from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List
from app.web.dtos import ThreadPost
from app.model.thread import Thread
from app.web.factory.thread_repository_factory import ThreadRepositoryFactory

router = APIRouter()


@router.put("/", response_description="Create a new thread", status_code=status.HTTP_201_CREATED, response_model=Thread)
def add_thread(
        request: Request,
        thread_post: ThreadPost = Body(...)
):
    thread_repository = ThreadRepositoryFactory().from_request(request)
    new_thread = Thread(title=thread_post.title)
    return jsonable_encoder(thread_repository.add_thread(new_thread))


@router.get("/", response_description="Get all the threads", status_code=status.HTTP_200_OK,
            response_model=List[Thread])
def get_all_threads(
        request: Request,
):
    thread_repository = ThreadRepositoryFactory().from_request(request)
    return thread_repository.find_all()

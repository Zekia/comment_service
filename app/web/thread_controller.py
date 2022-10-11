from fastapi import APIRouter, Body, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from typing import List

from app.di_container import DIContainer
from app.repository.thread_repository import ThreadRepository
from app.web.dtos import ThreadPost
from app.model.thread import Thread

router = APIRouter()


@router.put("/", response_description="Create a new thread", status_code=status.HTTP_201_CREATED, response_model=Thread)
def add_thread(
        request: Request,
        thread_post: ThreadPost = Body(...),
        thread_repository: ThreadRepository = Depends(DIContainer().get(ThreadRepository))
):
    new_thread = Thread(title=thread_post.title)
    return jsonable_encoder(thread_repository.add_thread(new_thread, request.app))


@router.get("/", response_description="Get all the threads", status_code=status.HTTP_200_OK,
            response_model=List[Thread])
def get_all_threads(
        request: Request,
        thread_repository: ThreadRepository = Depends(DIContainer().get(ThreadRepository))
):
    return thread_repository.find_all(request.app)

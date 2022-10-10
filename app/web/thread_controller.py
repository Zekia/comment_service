from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List

from app.dtos import ThreadPost
from app.models.thread import Thread

router = APIRouter()

@router.post("/", response_description="Create a new thread", status_code=status.HTTP_201_CREATED, response_model=Thread)
def create_thread(request: Request, thread_post: ThreadPost = Body(...)):
    new_thread = Thread(title=thread_post.title)
    new_thread = request.app.database["threads"].insert_one(jsonable_encoder(new_thread))
    created_thread = request.app.database["threads"].find_one(
        {"_id": new_thread.inserted_id}
    )
    print(thread_post)
    print(new_thread)
    print(created_thread)

    return created_thread

@router.get("/", response_description="Get all the threads", status_code=status.HTTP_201_CREATED, response_model=List[Thread])
def get_all_threads(request: Request):
    threadsList = list(request.app.database["threads"].find())
    print(threadsList)
    return threadsList
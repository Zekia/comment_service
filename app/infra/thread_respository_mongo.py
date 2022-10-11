from typing import List

from fastapi.encoders import jsonable_encoder

from app.model.thread import Thread
from app.repository.thread_repository import ThreadRepository


class ThreadRepositoryMongo(ThreadRepository):
    def add_thread(self, new_thread: Thread, app) -> Thread:
        app.database["threads"].insert_one(jsonable_encoder(new_thread))
        return new_thread

    def find_all(self, app) -> List[Thread]:
        return list(app.database["threads"].find())
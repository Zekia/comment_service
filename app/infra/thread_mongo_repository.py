from typing import List

from fastapi.encoders import jsonable_encoder

from app.infra.repository_mongo import MongoRepository
from app.model.thread import Thread
from app.repository.thread_repository import ThreadRepository


class ThreadMongoRepository(ThreadRepository, MongoRepository):
    def add_thread(self, new_thread: Thread) -> Thread:
        self.database.insert_one(jsonable_encoder(new_thread))
        return new_thread

    def find_all(self) -> List[Thread]:
        return list(self.database.find())

from typing import List, Union

from fastapi.encoders import jsonable_encoder

from app.infra.repository_mongo import MongoRepository
from app.model.thread import Thread
from app.repository.thread_repository import ThreadRepository


class ThreadMongoRepository(ThreadRepository, MongoRepository):
    def add_thread(self, new_thread: Thread) -> Thread:
        self.collection.insert_one(jsonable_encoder(new_thread))
        return new_thread

    def update_thread(self, new_thread: Thread) -> Thread:
        self.collection.update_one(
            {"_id": new_thread.id}, {"$set": jsonable_encoder(new_thread)}
        )
        print("new_thread", new_thread)
        return new_thread

    def find_all(self) -> List[Thread]:
        return list(self.collection.find())

    def find_with_id(self, id) -> Union[Thread, None]:
        if (thread := self.collection.find_one({"_id": id})) is not None:
            return Thread(**thread)
        return None

    def remove(self, id: str) -> int:
        """
        :param id: The id of the thread to delete
        :return: int The deleted count
        """
        return self.collection.delete_one({"_id": id}).deleted_count

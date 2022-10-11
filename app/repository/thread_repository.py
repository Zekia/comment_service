from abc import abstractmethod
from typing import List

from app.model.thread import Thread


class ThreadRepository:
    @abstractmethod
    def add_thread(self, thread: Thread) -> Thread:
        pass

    @abstractmethod
    def find_all(self) -> List[Thread]:
        pass

    @abstractmethod
    def find_with_id(self, id: str) -> List[Thread]:
        pass


class ThreadRepositoryException(Exception):
    pass

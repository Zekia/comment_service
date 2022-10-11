from abc import abstractmethod
from typing import List

from app.model.thread import Thread


class ThreadRepository:
    @abstractmethod
    def add_thread(self, thread: Thread, app) -> Thread:
        pass

    @abstractmethod
    def find_all(self, app) -> List[Thread]:
        pass


class ThreadRepositoryException(Exception):
    pass

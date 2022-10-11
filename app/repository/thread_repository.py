from abc import abstractmethod
from typing import List

from app.model.thread import Thread


class ThreadRepository:
    @abstractmethod
    def add_thread(self, thread: Thread) -> Thread:
        pass

    @abstractmethod
    def update_thread(self, thread: Thread) -> Thread:
        pass

    @abstractmethod
    def find_all(self) -> List[Thread]:
        pass

    @abstractmethod
    def find_with_id(self, id: str) -> Thread:
        pass

    @abstractmethod
    def remove(self, id: str) -> int:
        """
        :param id: The id of the thread to delete
        :return: int The deleted count
        """
        pass


class ThreadRepositoryException(Exception):
    pass

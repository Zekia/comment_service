from abc import abstractmethod
from fastapi import Request

from app.repository.model_repository import ModelRepository


class WebRepositoryFactory:
    """
    Interface to create the right factory from request
    """

    @abstractmethod
    def from_request(self, request: Request) -> ModelRepository:
        pass

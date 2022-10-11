from fastapi import Request
from app.infra.thread_mongo_repository import ThreadMongoRepository
from app.repository.model_repository import ModelRepository
from app.repository.thread_repository import ThreadRepository


class ThreadRepositoryFactory(ModelRepository):
    def from_request(self, request: Request) -> ThreadRepository:
        repository = ThreadMongoRepository()
        repository.setDatabase(request.app.database["threads"])
        return repository

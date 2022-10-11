from fastapi import Request
from app.infra.comment_mongo_repository import CommentMongoRepository
from app.repository.model_repository import ModelRepository
from app.repository.comment_repository import CommentRepository


class CommentRepositoryFactory(ModelRepository):
    def from_request(self, request: Request) -> CommentRepository:
        repository = CommentMongoRepository()
        repository.setCollection(request.app.database["threads"])
        return repository

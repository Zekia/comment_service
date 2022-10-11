from fastapi.encoders import jsonable_encoder

from app.infra.repository_mongo import MongoRepository
from app.model.comment import Comment
from app.repository.comment_repository import CommentRepositoryException, CommentRepository


class CommentMongoRepository(CommentRepository, MongoRepository):
    def add_comment(self, new_comment: Comment, thread_id: str) -> Comment:
        new_comment_as_json = jsonable_encoder(new_comment)
        update_result = self.collection.update_one(
            {"_id": thread_id},
            {"$push": {"comments": new_comment_as_json}}
        )
        if update_result.modified_count == 0:
            raise CommentRepositoryException(f"Thread with ID {thread_id} not found")
        return new_comment
from fastapi.encoders import jsonable_encoder

from app.model.comment import Comment
from app.repository.comment_repository import CommentRepositoryException


class CommentRepositoryMongo:
    def create_comment(self, new_comment: Comment, thread_id: str, app) -> Comment:
        new_comment_as_json = jsonable_encoder(new_comment)
        update_result = app.database["threads"].update_one(
            {"_id": thread_id},
            {"$push": {"comments": new_comment_as_json}}
        )
        if update_result.modified_count == 0:
            raise CommentRepositoryException(f"Thread with ID {thread_id} not found")
        return new_comment

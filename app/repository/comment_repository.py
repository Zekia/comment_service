from abc import abstractmethod

from app.model.comment import Comment


class CommentRepository:
    @abstractmethod
    def create_comment(self, comment: Comment, thread_id, app) -> Comment:
        pass

class CommentRepositoryException(Exception):
    pass

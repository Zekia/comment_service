from abc import abstractmethod

from app.model.comment import Comment


class CommentRepository:
    @abstractmethod
    def add_comment(self, comment: Comment, thread_id: str) -> Comment:
        pass

    @abstractmethod
    def update_comment(self, comment: Comment, thread_id: str) -> Comment:
        pass


class CommentRepositoryException(Exception):
    pass

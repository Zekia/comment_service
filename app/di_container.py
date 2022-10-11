from app.infra.comment_respository_mongo import CommentRepositoryMongo
from app.infra.thread_respository_mongo import ThreadRepositoryMongo
from app.repository.comment_repository import CommentRepository
from app.repository.thread_repository import ThreadRepository


class DIContainer:
    def get(self, instance):
        """
        Get the right types of instances for the injected objects to be injected
        :param instance:
        :return:
        """
        instance_type = instance.__name__
        return {
            CommentRepository.__name__: CommentRepositoryMongo,
            ThreadRepository.__name__: ThreadRepositoryMongo
        }[instance_type]

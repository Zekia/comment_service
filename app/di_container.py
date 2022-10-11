from app.infra.comment_respository_mongo import CommentRepositoryMongo
from app.repository.comment_repository import CommentRepository


class DIContainer:
    def get(self, instance):
        """
        Get the right types of instances for the injected objects to be injected
        :param instance:
        :return:
        """
        instance_type = instance.__name__
        return {
            CommentRepository.__name__: CommentRepositoryMongo
        }[instance_type]

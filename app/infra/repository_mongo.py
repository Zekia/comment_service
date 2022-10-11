from pymongo.collection import Collection


class MongoRepository:
    collection = None

    def setCollection(self, collection: Collection):
        self.collection = collection

from bson.objectid import ObjectId

class BaseEntity():
    def __init__(self, data=None):
        if data:
            self.__dict__ = data

    def set_id(self, id):
        self._id = ObjectId(id) 
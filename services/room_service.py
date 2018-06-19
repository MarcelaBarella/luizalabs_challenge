import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from bson.objectid import ObjectId

from domain.room import Room
from errors.room_errors import RoomNotFoundError 


class RoomService:
    def __init__(self, collection):
        self.collection = collection

    def all(self):
        return list(self.collection.find())

    #abstrair
    def find(self, id):
        room = self.collection.find_one({'_id': ObjectId(id)})
        if not room:
            raise RoomNotFoundError()

        return room

    def create(self, room):      
        self.collection.save(room.__dict__)

    def delete(self, id):
        self.find(id)
        self.collection.remove(ObjectId(id))

    def edit(self,room):
        self.find(str(room._id))
        self.collection.update_one({'_id': room._id}, 
                                    {'$set': room.__dict__}, 
                                    upsert=False)


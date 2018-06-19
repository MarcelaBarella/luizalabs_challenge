import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from bson.objectid import ObjectId

from domain.room import Room
from domain.schedule import Schedule
from errors.room_errors import RoomNotFoundError 
from errors.schedule_errors import ScheduleNotFoundError

class ScheduleService:
    def __init__(self, room_collection, room_service):
        self.room_collection = room_collection
        self.room_service = room_service

    def find(self, room_id, schedule_id):
        room = self.room_collection.find_one(
            {'_id': ObjectId(room_id), 'schedules._id': ObjectId(schedule_id)},
            {'schedules.$': 1}
        )
        schedule = room['schedules'][0]
        return schedule

    def all(self):
        pass

    def add_schedule(self, room_id, schedule):
        room = Room(self.room_service.find(str(room_id)))
        room.add_schedule(schedule)
        self.room_service.edit(room)

    def delete(self, room_id, schedule_id):
        room = Room(self.find(str(room_id)))
        room_collection.remove_schedule(schedule_id)
        self.edit(room)

    def edit(self, room, schedule, title=None, participants=[], begin=None, end=None):
        schedule = Schedule(self.find(str(room['_id']), str(schedule['_id'])))
        schedule.title = title or schedule.title
        schedule.participants = participants or schedule.participants
        if begin: schedule.set_begin(begin)
        if end: schedule.set_end(end)
        self.room_collection.update_one({'_id': schedule._id}, 
                                        {'$set': schedule.__dict__}, 
                                        upsert=False)

        

    

    
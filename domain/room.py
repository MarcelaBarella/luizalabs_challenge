import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from errors.schedule_errors import ScheduleNotFoundError
from errors.room_errors import RoomAlreadyHasScheduleInGivenPeriodError
from domain.base_entity import BaseEntity
from domain.schedule import Schedule

class Room(BaseEntity):
    def add_schedule(self, new_schedule):
        if not hasattr(self, 'schedules'):
            self.schedules = []

        for schedule in self.schedules:
            if(Schedule(schedule).colides_with_other_schedule(new_schedule)):
                raise RoomAlreadyHasScheduleInGivenPeriodError()
                
        self.schedules.append(new_schedule.__dict__)

    def remove_schedule(self, schedule_id):
        if not hasattr(self, 'schedules'):
            raise ScheduleNotFoundError()
        
        schedule = next((schedule for schedule in self.schedules if str(schedule['_id']) == schedule_id), None)
        if not schedule:
            raise ScheduleNotFoundError()

        self.schedules.remove(schedule)

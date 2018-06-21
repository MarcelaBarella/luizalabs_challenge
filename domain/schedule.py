import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from datetime import datetime

from bson.objectid import ObjectId

from domain.base_entity import BaseEntity
from utils import str_to_datetime

class Schedule(BaseEntity):
    def __init__(self, data):
        super(Schedule, self).__init__(data)
        if not hasattr(self, '_id'):
            self._id = ObjectId()

        self.begin = str_to_datetime(self.begin)
        self.end =str_to_datetime(self.end)
        self.__validate_dates()

    def set_begin(self, date):
        self.begin = str_to_datetime(date) if type(date) == str else date
        self.__validate_dates()

    def set_end(self, date):
        self.end = str_to_datetime(date) if type(date) == str else date
        self.__validate_dates()

    def colides_with_other_schedule(self, other):
        return (self.begin <= other.begin <= self.end) or (other.begin <= self.begin <= other.end)

    def __validate_dates(self):
        if self.begin and self.begin > self.end:
            raise ValueError('End cannot be before or equals begin')
        if self.end and self.begin >= self.end:
            raise ValueError('Begin cannot be after or equals end')

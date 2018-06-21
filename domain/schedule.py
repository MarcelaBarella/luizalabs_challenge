from datetime import datetime

from bson.objectid import ObjectId

from domain.base_entity import BaseEntity

class Schedule(BaseEntity):
    def __init__(self, data):
        super(Schedule, self).__init__(data)
        if not hasattr(self, '_id'):
            self._id = ObjectId()

        self.set_begin(self.begin)
        self.set_end(self.end)

        if(self.begin > self.end):
            raise ValueError('Begin cannot be after or equals end')

    def set_begin(self, date):
        if(type(date) == str):
            self.begin = datetime.strptime(date, '%d/%m/%Y %H:%M')
        else:
            self.begin = date

        if self.end and self.begin >= self.end:
            raise ValueError('Begin cannot be after or equals end')

    def set_end(self, date):
        if(type(date) == str):
            self.end = datetime.strptime(date, '%d/%m/%Y %H:%M')
        else:
            self.end = date

        if self.begin and self.begin > self.end:
            raise ValueError('End cannot be before or equals begin')

    def colides_with_other_schedule(self, other):
        return (self.begin <= other.begin <= self.end) or (other.begin <= self.begin <= other.end)



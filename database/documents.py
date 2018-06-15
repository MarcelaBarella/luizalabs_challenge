from connect import db

#esse arquivo e a pasta dele deveriam ter outro nome?

class Schedule(db.Document):
    #query_class = ScheduleQuery

    title = db.StringField()

    participants = db.ListField(db.StringField())

    beginning = db.DateTimeField()

    end = db.DateTimeField()

class Room(db.Document):
    #query_class = RoomQuery

    room_name = db.StringField()

    capacity = db.IntField()

    schedules = db.DocumentField(Schedule, required=False)

import os

from flask import (Flask, request)
from flask.json import jsonify
from flask_request_validator import (PATH, JSON, validate_params, Param)
from bson.json_util import dumps
from pymongo import MongoClient

from services.room_service import RoomService
from services.schedule_service  import ScheduleService
from domain.room import Room
from domain.schedule import Schedule
from errors.room_errors import RoomNotFoundError, RoomAlreadyHasScheduleInGivenPeriodError

app = Flask(__name__)
database = MongoClient('mongo', 27017).room_scheduler
room_service = RoomService(database.room)
schedule_service = ScheduleService(database.room, room_service)


@app.route('/room', methods=['GET'])
def get_all_rooms():
    rooms = room_service.all()
    return dumps(rooms)

@app.route('/room/<room_id>', methods=['GET'])
def get_given_room(room_id):
    room = room_service.find(room_id)
    return dumps(room)

@app.route('/room/<room_id>', methods=['DELETE'])
def delete_room(room_id):
    room = room_service.delete(room_id)
    return (dumps({'message': 'Room deleted'}), 200)

#Como tratar o erro 500
@app.route("/room", methods=['POST'])
@validate_params(
    Param('name', JSON, str),
    Param('capacity', JSON, int)
)
def create_room(name, capacity):
    room = Room(request.json)
    room_service.create(room)
    return (dumps({'message':'Room created'}), 201)

@app.route("/room/<room_id>", methods=['PUT'])
@validate_params(
    Param('room_id', PATH, str),
    Param('name', JSON, str, required=False),
    Param('capacity', JSON, int, required=False)
)
def edit_room(room_id, name, capacity):
    room = Room(request.json)
    room.set_id(room_id)
    room_service.edit(room)
    return (dumps({'message': 'Edited Room'}), 204)



@app.route("/room/<room_id>/schedule/<schedule_id>", methods=["GET"])
def get_schedule(room_id, schedule_id):
    schedule = schedule_service.find(room_id, schedule_id)
    import pdb
    pdb.set_trace()
    return dumps(schedule)

@app.route("/room/<room_id>/schedule", methods=['POST'])
@validate_params(
    Param('title', JSON, str),
    Param('participants', JSON, list),
    Param('begin', JSON, str),
    Param('end', JSON, str),
    Param('room_id', PATH, str)
)
def create_schedule(title, participants, begin, end, room_id):
    schedule = Schedule(request.json)
    schedule_service.add_schedule(room_id, schedule)
    return (dumps({'message':'Created Schedule'}), 201)

@app.route("/room/<room_id>/schedule/<schedule_id>", methods=['DELETE'])
def delete_schedule(room_id, schedule_id):
    schedule_service.delete_schedule(room_id, schedule_id)
    return (dumps({'message': 'Schedule deleted'}), 201)

@app.route("/room/<room_id>/schedule/<schedule_id>", methods=['PUT'])
@validate_params(
    Param('room_id', PATH, str),
    Param('schedule_id', PATH, str),
    Param('title', JSON, str, required=False),
    Param('participants', JSON, list, required=False),
    Param('begin', JSON, str, required=False),
    Param('end', JSON, str, required=False)
)
def edit_schedule(room_id, schedule_id, title, participants, begin, end):
    schedule_service.edit(room_id, schedule_id, title, participants, begin, end)
    return (dumps({'message': 'Schedule edited'}), 204)


@app.errorhandler(RoomNotFoundError)
def room_not_found_error_handler(errror):
    return (dumps({'message': 'Room not found'}), 404)

@app.errorhandler(RoomAlreadyHasScheduleInGivenPeriodError)
def cannot_book_error_handler(error):
    return (dumps({'message': 'This room is busy in this given period. Please, try other!'}), 406)

@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'application/json'
    return response

    
# tem que ir pra outro arquivo
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

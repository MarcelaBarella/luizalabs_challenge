import os

from flask import (Flask, request)
from flask_request_validator import (PATH, JSON, validate_params, Param)
from bson.json_util import dumps
from pymongo import MongoClient

from services.room_service import RoomService
from domain.room import Room
from errors.room_errors import RoomNotFoundError

app = Flask(__name__)
database = MongoClient('mongo', 27017).room_scheduler
room_service = RoomService(database.room)


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
    return ('', 200)

#Como tratar o erro 500
@app.route("/room", methods=['POST'])
@validate_params(
    Param('name', JSON, str),
    Param('capacity', JSON, int)
)
def create_room(name, capacity):
    room = Room(request.json)
    room_service.create(room)
    return ('Room created', 201)

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
    return ('', 204)

@app.route("/room/<room_id>/schedule", methods=['POST'])
def create_schedule(room_id):
    """ Route to book a room, return the 200 state request if is available.
    Otherwise will return the """

    pass


#deleta o agendamento de uma sala
@app.route("/room/<room_id>/schedule/<schedule_id>")
def delete_schedule(room_id, schedule_id, methods=['DELETE']):
    pass

@app.route("/room/")
def edit_reservation():
    pass

@app.errorhandler(RoomNotFoundError)
def room_not_found_error_handler(errror):
    return ('Room not found', 404)

"""room_scheduler  = { 'room_name': 'carrapato',
                        'capacity': 7,
                        'schedules' : {
                            'title': 'squad planning',
                            'participants': ['Marcela', 'Ricardo', 'Juninho']
                            'beginning': '14/06/2018-15:00PM',
                            'end': '14/06/2018-16:30PM'
                        }
}"""

    
# tem que ir pra outro arquivo
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

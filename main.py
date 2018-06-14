import os

from flask import (Flask, redirect, request)

app = Flask(__name__)


@app.route("/room/<room_id>/schedule", methods=['POST'])
def create_reservation(room_id):
    """ Route to book a room, return the 200 state request if is available.
    Otherwise will return the """
    #if request.method == 'POST':
    #    try:

    pass

'''cria uma nova sala'''
@app.route("/room", methods=['POST'])
def create_room():
    """Method to create a new room"""
    pass

#deleta o agendamento de uma sala
@app.route("/room/<room_id>/schedule/<schedule_id>")
def delete_schedule(room_id, schedule_id, methods=['DELETE']):
    pass

@app.route("/room/")
def edit_reservation():
    pass

@app.route("/ping")
def ping():
    return "It's ok, I'm alive!"

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

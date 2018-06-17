#verificar se so importar o schedule basta
from database import Schedule, ScheduleQuery

@app.route("/room/<room_id>/schedule", methods=['POST'])
def create_schedule(room_id):
    """ Route to book a room, return the 200 state request if is available.
    Otherwise will return the """
    #if request.method == 'POST':
        try:
            title = resquest.json['title']
            capacity = resquest.json['capacity']

            schedule = Schedule(title=title, capacity=capacity)
            schedule.save()


    pass

@app.route("/room/<room_id>/schedule/<schedule_id>", methods=['DELETE'])
def delete_schedule(room_id, schedule_id):
    pass

@app.route("/room/<room_id>/schedule/<schedule_id>" methodd=['PUT'])
def edit_schedule(room_id, schedule_id):
    pass
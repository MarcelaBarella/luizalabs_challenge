class Service():

    def save_room(self):
        
        room_name = 'coffe room'

        capacity = 8

        schedule = {
            'title': 'coffe break',
            'participants': 3,
            'beginning': 'date',
            'end': 'date'
            }

        room = {
            'room_name': room_name,
            'capacity': capacity,
            'schedules': {schedule}
        }

        db.save(room)


    def save_schedule(self):
        """Saves the some given schedule in a given room schedule"""

        #title = schedule_data['title']
        title = 'Test save_schedule'

        """if not len(request.json['participants']) > db.room.capacity
            participants = schedule_data['participants']"""
        participants = 'Over capacity'

        beginning = 'date'

        end = 'date'

        schedule = {
            'title': title,
            'participants': participants,
            'beginning': beginning,
            'end': end
        }

        db.save(schedule)


def main():
    Service.save_room('test')

if __name__ == '__main__':
    main()
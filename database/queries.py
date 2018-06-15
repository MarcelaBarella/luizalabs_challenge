from connect import db

#As classes desse arquivo deveriam ficar com as de documents?

class ScheduleQuery(db.BaseQuery):

    #Formato manualmente num dicionario ou uso um serialize?
    def get_all(self):
        results = self.query.all()

    def get_schedule_room(self):
        result = self.query.filter(self.data==)

    #Como achar a sala da qual esta inserido um schedule?
    def get_schedule_data(self, data):
        result = self.query.filter(self.data == data)

class RoomQuery(db.BaseQuery):

    def get_all(self):
        self.query.all()

    #sera que é melhor mudar para ListField e depois dar um append etc
    def get_room_schedules(self):
        result = self.query.filter(self.schedules)


class Appointment:
    def __init__(self, date , startTime, endTime,barberId,clientId):
        self.date = date;
        self.endTime = endTime;
        self.startTime = startTime;
        self.barberId = barberId;
        self.clientId = clientId;
        
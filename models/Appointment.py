class Appointment:
    def __init__(self, date , startTime, barberId,clientId):
        self.date = date;
        self.startTime = startTime;
        self.endTime = startTime(minutes=30);
        self.barberId = barberId;
        self.clientId = clientId;
        

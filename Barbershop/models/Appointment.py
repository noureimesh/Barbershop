#from datetime import date,timedelta,time
from datetime import time,date,datetime,timedelta

class Appointment:
    def __init__(self, appDate , startTime, barberId,clientId):
        self.date = appDate;
        self.startTime = startTime;
        self.endTime =(datetime.combine(date(1, 1, 1), startTime) + timedelta(minutes=30)).time()
        self.barberId = barberId;
        self.clientId = clientId;

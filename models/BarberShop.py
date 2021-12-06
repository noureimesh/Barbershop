from Barber import *
from Appointment import *

class Barbershop:
       def __init__(self,address= "", name= "" , barbers= [],clients =[], bio = "", appointments= []):
        self.id = address;
        self.name = name;
        self.bio = bio;
        self.barbers = barbers;
        self.clients = clients;
        self.appointments = appointments;
        
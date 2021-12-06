import datetime
from Appointment import *
from BarberShop import *
from Barber import *
from Client import *
from Shift import *
import django;


barbershop= Barbershop();

def CheckBarberShift(id, date, startTime, endTime):
 for barber in barbershop.barbers:
  if barber.id == id:
    for shift in barber.shifts:
        if shift.day == date.weekday() and shift.startTime <= startTime and shift.endTime >= endTime :
          return True;
    return False;


def CheckBookedAppointments(barberId, date, startTime, endTime):
  for appointment in barbershop.appointments:
    if appointment.date == date and appointment.barberId == barberId and not((startTime <= appointment.startTime and endTime <= appointment.startTime ) or
      (startTime >= appointment.endTime and endTime >= appointment.endTime)): 
          return False;
    return True;
    
def AddAppointment(barberId, clientName, date, startTime, endTime):
  if(CheckBarberShift(barberId,date,startTime,endTime) and CheckBookedAppointments(barberId,date,startTime,endTime)):
    isClientExist = False;
    for client in barbershop.clients :
      if client.name == clientName :
        clientId = client.id;
        isClientExist = True;
        break;
    if isClientExist == False :
       clientId = barbershop.clients[-1].id + 1;
       barbershop.clients.append(Client(clientId,clientName));
    barbershop.appointments.append(Appointment(date,startTime,endTime,barberId,clientId));
    
      

    for appointment in barbershop.appointments :
       print (appointment.clientId)
       print ("/n")
       print (appointment.barberId)
    



def Seed():
  ahmadShifts= list();
  ahmadShifts.append(Shift(1,0, datetime.time(8, 30, 00),datetime.time(13, 30, 00)))
  ahmadShifts.append(Shift(2,2, datetime.time(8, 30, 00),datetime.time(13, 30, 00)))
  ahmadShifts.append(Shift(3,3, datetime.time(8, 30, 00),datetime.time(13, 30, 00)))

  hussamShifts= list();
  hussamShifts.append(Shift(1,1, datetime.time(8, 30, 00),datetime.time(13, 30, 00)))
  hussamShifts.append(Shift(2,2, datetime.time(8, 30,00),datetime.time(13, 30, 00)))
  hussamShifts.append(Shift(3,4, datetime.time(12, 30, 00),datetime.time(17, 30, 00)))

  barbershop.barbers.append(Barber(1,"Ahmad","2 years ecperience",ahmadShifts));
  barbershop.barbers.append(Barber(2,"Hussam","5 years ecperience",hussamShifts));

  barbershop.clients.append(Client(1,"Georg"))
  barbershop.clients.append(Client(2,"Saleem"))

  barbershop.appointments.append(Appointment(datetime.date(2021,12,6),datetime.time(8,30,00),datetime.time(9,00,00),1,1))
  barbershop.appointments.append(Appointment(datetime.date(2021,12,6),datetime.time(10,00,00),datetime.time(10,30,00),1,1))

  #for client in barbershop.clients:
#    print(client.name)

 # for client in barbershop.barbers:
  # print(client.name)
  
  #for appointment in barbershop.appointments:
  # print(appointment.startTime)

     
Seed();
AddAppointment(1,"Ahmad",datetime.date(2021,12,6),datetime.time(9,00,00),datetime.time(9,30,00));
#print (CheckBookedAppointments(1,datetime.date(2021,12,6),datetime.time(9,00,00),datetime.time(9,30,00)));
#print (CheckBarberShift(1,datetime.date(2021,12,6),datetime.time(9,00,00),datetime.time(9,30,00)));
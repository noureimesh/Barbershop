from datetime import time,date,datetime,timedelta
from operator import contains

from .BarberShop import *
from .Barber import *
from .Client import *
from .Shift import *

def CheckBarberShift(id, appointmantDate, startTime, endTime, barbershop):
 for barber in barbershop.barbers:
  if barber.id == id:
    for shift in barber.shifts:
        if shift.day == appointmantDate.weekday() and shift.startTime <= startTime and shift.endTime >= endTime :
          return True;
    return False;


def CheckBookedAppointments(barberId, date, startTime, endTime,barbershop):
  for appointment in barbershop.appointments:
    if appointment.date == date and appointment.barberId == barberId and not((startTime <= appointment.startTime and endTime <= appointment.startTime ) or
      (startTime >= appointment.endTime and endTime >= appointment.endTime)): 
          return False;
  return True;
    
def AddAppointment(barberId, clientName, appointmentDate, startTime, barbershop):
  endTime = (datetime.combine(date(1, 1, 1), startTime) + timedelta(minutes=30)).time();
  if type(appointmentDate)== str :
     appointmentDate= datetime.strptime(appointmentDate, '%m/%d/%Y');
  if not CheckBarberShift(barberId,appointmentDate,startTime,endTime,barbershop):
      return "Sorry! The selected barber doesn't work at selected time"
  if not CheckBookedAppointments(barberId,appointmentDate,startTime,endTime,barbershop):
      return "Sorry! The Appointment is taken"
  #Check Client
  isClientExist = False;
  for client in barbershop.clients :
    if client.name == clientName :
      clientId = client.id;
      isClientExist = True;
      break;
  if isClientExist == False :
    clientId = barbershop.clients[-1].id + 1;
    barbershop.clients.append(Client(clientId,clientName));
  #Add appointment
  barbershop.appointments.append(Appointment(appointmentDate,startTime,barberId,clientId));
  return True;

def Seed():
  barbershop= Barbershop();
  ahmadShifts= list();
  ahmadShifts.append(Shift(1,0, time(8, 30, 00),time(13, 30, 00)));
  ahmadShifts.append(Shift(1,2, time(8, 30, 00),time(13, 30, 00)));
  ahmadShifts.append(Shift(1,3, time(8, 30, 00),time(13, 30, 00)));

  hussamShifts= list();
  hussamShifts.append(Shift(2,1, time(8, 30, 00) ,time(13, 30, 00)));
  hussamShifts.append(Shift(2,2, time(8, 30,00) , time(13, 30, 00)));
  hussamShifts.append(Shift(2,4, time(12, 30, 00) , time(17, 30, 00)));

  barbershop.barbers.append(Barber(1,"Ahmad","2 years experience",ahmadShifts));
  barbershop.barbers.append(Barber(2,"Hussam","5 years experience",hussamShifts));

  barbershop.clients.append(Client(1,"Georg"))
  barbershop.clients.append(Client(2,"Saleem"))

  barbershop.appointments.append(Appointment(date(2021,12,6),time(8,30,00),1,1))
  barbershop.appointments.append(Appointment(date(2021,12,6),time(10,00,00),1,1))

  return barbershop;


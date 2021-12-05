from Appointment import *
from BarberShop import *
import django
   
barbershop= Barbershop();



def CheckBarberShift(id, date, startTime, endTime):
 for barber in barbershop.barbers:
  if barber.id == id:
    print(barber)
    for shift in barber.shift:
        if shift.date == date & shift.startTime >= startTime & shift.endTime <= endTime:
          return True;
    return False;


  def CheckBookedAppointments(date, startTime, endTime, barberId):
    for appointment in barbershop.appointments:
      if appointment.date == date & appointment.barberId == barberId & ~((startTime <= appointment.startTime & endTime <= appointment.startTime ) or
        (startTime >= appointment.endTime & endTime >= appointment.endTime)): 
           return False;
      return True;
       
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from .models import main;

Barbershop = main.Seed()

def index(request):
    return render(request, 'appointmentForm.html',
    {
     'barbers': Barbershop.barbers,
    }
)

# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        barberId = int(request.POST.get('barberId', None))
        clientName = request.POST.get('clientName', None)  
        date = request.POST.get('date', None) 
        time =  request.POST.get('time', None) 
        if barberId and clientName and date and time: 
            time = datetime.strptime(time, '%H:%M').time();
            addAppointmentResult = main.AddAppointment(barberId,clientName,date,time,Barbershop);
            if addAppointmentResult == True:
                return JsonResponse({
                            'msg':'Your appointment has been submitted successfully'
                    },status= 200 )
            else :
                return JsonResponse({
                         'msg': addAppointmentResult
                },status= 400 )
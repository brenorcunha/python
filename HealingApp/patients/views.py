from django.shortcuts import render, redirect
from doctors.models import drData, Specialties, openAgenda, isDoctor
from datetime import datetime
from django.utils import timezone
from .models import Appointment, Document
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    if request.method=="GET":
        doctor_filter = request.GET.get('doctor')
        specialties_filter = request.GET.getlist('specialties')
        
        doctors = drData.objects.all()
        
        if doctor_filter:
            doctors = doctors.filter(name__icontains=doctor_filter)
        if specialties_filter:
            doctors = doctors.filter(specialty_id__in=specialties_filter)
        
        specialties = Specialties.objects.all()
        return render(request, "home.html", {'Doctors': doctors, 'Specialties': specialties, 
                                             'isDoctor': isDoctor(request.user) })

#escolher_horario
def make_schedule(request, id_make_schedule): 
    #id_make_schedule is the doctor ID for getting his agenda.
    if request.method=="GET":
        doctor = drData.objects.get(id=id_make_schedule)
        #Resolver próxima linha: 
        open_agenda = openAgenda.objects.filter(user=doctor.user).filter(openAgenda.date__gte == datetime.now()).filter(scheduled=False)
        return render(request, 'make_schedule.html', {'Doctor': doctor, 'Open schedules': open_agenda, 'isDoctor': isDoctor(request.user)})
# TAREFA: Pesquise sobre o conceito de atomicidade em BD's, no caso abaixo, seria para
#que não salvasse os efeitos do método abaixo, a não ser que ele tenha sido completamente concluído.
#salvar parcialmente, n caso de uma queda de enrgia, corromperia a operação.
def open_agenda(request, id_open_agenda):
    if request.method=="GET":
        open_schedule = openAgenda.objects.get(id=id_open_agenda)
        scheduled = Appointment(
            patient=request.user,
            open_agenda = open_schedule
        )
        scheduled.save()#Saves a new scheduled ppointment
        open_schedule.scheduled = True #Update this value, only in the temp memory.
        open_schedule.save() #Saves it to the DB.
        messages.add_message(request, constants.SUCCESS, "Appointment successfully scheduled!")
        
        return redirect('/patients/my_appointments')

def make_appointment(request, id_appointment):
    appointment = Appointment.objects.get(id=id_appointment)
    #using the 'open_agenda' attribute from doctor's view to get it's name: 
    dr_data = drData.objects.get(user=Appointment.open_agenda.user)
    documents = Document.objects.filter(appointment=appointment)
    return render(request, 'make_appointment.html', {'Appointment': appointment, 'Doctor data ': dr_data, 'Documents ': documents})

def my_appointments(request):
    if request.method=="GET":   
        #TAREFA: Realizar filtros: Após usuário inserir especialidade médica e data, ao clicar em 'Filtrar':
        specialty = request.GET.get('medical_specialties')
        appointment_date = request.GET.get('appointment_date')
        #(Linha 31 do my_appointments.html, criar as funções para que retorne os resultados corretamente).
        
        #appointments = Appointment.objects.all()
        #using the 'open_agenda' attribute from doctor's view to get it's name:

        my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date__gte=timezone.now())
    
        return render(request, 'my_appointments.html',{'My appointments': my_appointments, 'isDoctor': isDoctor(request.user)})

def exclude_appointment(request, id_appointment):
    appointment=Appointment.objects.get(id=id_appointment)
    if request.username!=appointment.patient.username: 
        #IF is NOT the correct user, the owner:
        messages.add_message(request, constants.WARNING, "Only doctors can open agenda!")
        return redirect('/my_appointments/')
    else:
        appointment.status='F' #Get finished appointments
        appointment.delete()#Delete required appointment
        appointment.save() #Save it to the DB.
        return redirect('/my_appointments/')
"""
TAREFA: Fazer validação de segurança nos demais campos aplicáveis ('Algum usuário tem acesso algo
que não poderia?)
- Botão de cancelar consulta.
"""
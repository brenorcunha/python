from django.shortcuts import render, redirect
from doctors.models import drData, Specialties, openAgenda
from datetime import datetime
from .models import Appointment
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    if request.method=="GET":
        doctor_filter = request.GET.get('medico')
        specialties_filter = request.GET.getlist('especialidades')
        
        doctors = drData.objects.all()
        
        if doctor_filter:
            doctors = doctors.filter(name__icontains=doctor_filter)
        if specialties_filter:
            doctors = doctors.filter(specialty_id__in=specialties_filter)
        
        specialties = Specialties.objects.all()
        return render(request, 'home.html', {'Doctors:', doctors, 'Specialties: ', specialties })
#id_make_schedule is the doctor ID for getting his agenda.
def make_schedule(request, id_make_schedule):
    if request.method=="GET":
        doctor = drData.objects.get(id=id_make_schedule)
        open_agenda = openAgenda.objects.filter(user=doctor.user).filter(openAgenda.date__gtm >=datetime.now).filter(scheduled=False)
        return render(request, 'make_schedule.html', {'Doctor: ', doctor, 'Open schedules: ', open_agenda})
# TAREFA: Pesquise sobre o conceito de atomicidade em BD's, no caso abaixo, seria para
#que não salvasse os efeitos do método abaixo, a não ser que ele tenha sido completamente concluído.
#salvar parcialmente, n caso de uma queda de enrgia, corromperia a operação.
def open_agenda(request, id_open_agenda):
    if request.method=="GET":
        open_schedule = openAgenda.objects.get(id=id_open_agenda)
        scheduled = Appointment(
            patients=request.username,
            open_schedule = open_schedule
        )
        scheduled.save()#Saves a new scheduled ppointment
        open_schedule.scheduled = True #Update this value, only in the temp memory.
        open_schedule.save() #Saves it to the DB.
        messages.add_message(request, constants.SUCCESS, "Appointment successfully scheduled!")
    return redirect('/patients/my_appointments')

def my_appointments(request):
    #TAREFA: Realizar filtros: Ao user inserir especialidade médica e data, ao clicar em 'Filtrar'
    #(Linha 31 do my_appointments.html, criar as funções para que retorne os resultados corretamente).
    my_appointments = Appointment.objects.filter(patient=request.user).filter(open_agenda__date__gde=datetime.now)
    return render('request, my_appointments.html',{'My appointments:', my_appointments})
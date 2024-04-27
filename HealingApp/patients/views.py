from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import drData, Specialties, openAgenda, isDoctor
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Appointment, Document
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def home(request):
    if request.method=="GET":
        if request.user=='Anonymous':
            messages.add_message(request, constants.WARNING, 'There is no one logged! Try again.' )
            return redirect('/users/login/')
        else:
            doctor_filter = request.GET.get('doctor')
            specialties_filter = request.GET.getlist('specialties')
            
            doctors = drData.objects.all()

            if doctor_filter:
                doctors = doctors.filter(name__icontains=doctor_filter)
                
            if specialties_filter:
                doctors = doctors.filter(specialty_id__in=specialties_filter)
                
            #LEMBRETES: Aqui obtenho as consultas deste user. Agora será iterar e põr pra exibir na barra de lembretes
            #porém SOMENTE SE user é um paciente.    
            today = datetime.now().date()
            my_appointments = Appointment.objects.filter(open_agenda__user=request.user).filter(open_agenda__date__gte=today).filter(open_agenda__date__lt=today+timedelta(days=1))

            specialties = Specialties.objects.all()
            return render(request, "home.html", {'doctors': doctors, 'specialties': specialties, 
                                                'isDoctor': isDoctor(request.user) })

#escolher_horario: 
@login_required
def make_schedule(request, id_doctor): #id_dr to get his/her agenda.
    if request.method=="GET":
        doctor = drData.objects.get(id=id_doctor)
        open_agenda = openAgenda.objects.filter(user=doctor.user).filter(date__gte= datetime.now()).filter(scheduled=False)
        return render(request, 'make_schedule.html', {'doctor': doctor, 'open_agenda': open_agenda, 'isDoctor': isDoctor(request.user)})
# TAREFA: Pesquise sobre o conceito de atomicidade em BD's, no caso abaixo, seria para
#que não salvasse os efeitos do método abaixo, a não ser que ele tenha sido completamente concluído.
#salvar parcialmente, n caso de uma queda de enrgia, corromperia a operação.

#agendar horario: 
@login_required
def open_agenda(request, id_open_agenda):
    if request.method=="GET":
        open_agenda = openAgenda.objects.get(id=id_open_agenda)
        schedule = Appointment(
            patient=request.user,
            open_agenda = open_agenda
        )
        schedule.save() #Saves a new scheduled ppointment
        open_agenda.scheduled = True #Update this value, only in the temp memory.
        open_agenda.save() #Saves it to the DB.
        messages.add_message(request, constants.SUCCESS, "Appointment successfully scheduled!")
        
        return redirect('/patients/my_appointments')

#consulta
@login_required
def make_appointment(request, id_appointment):
    if request.method=="GET":
        appointment = Appointment.objects.get(id=id_appointment)
        #using the 'open_agenda' attribute from doctor's view to get it's name: 
        dr_data = drData.objects.get(user=Appointment.open_agenda.user)
        documents = Document.objects.filter(appointment=appointment)
        return render(request, 'make_appointment.html', {'appointment': appointment, 'dr_data': dr_data, 'documents ': documents})

#minhas_consultas
@login_required
def my_appointments(request):
    #Realizar filtros: Após usuário inserir especialidade médica e data, ao clicar em 'Filtrar':
    specialty = request.GET.get('medical_specialties')
    appointment_date = request.GET.get('date')
    my_appointments = Appointment.objects.filter(patient=request.user).filter(open_agenda__date__gte=datetime.now().date())

    if appointment_date:
        my_appointments = Appointment.objects.filter(patient=request.user).filter(open_agenda__date__gte=appointment_date)
    if specialty:
        my_appointments = Appointment.objects.filter(patient=request.user).filter(open_agenda__user__drData__specialty__id=specialty)
 
    specialties = Specialties.objects.all()
    #using the 'open_agenda' attribute from doctor's view to get it's name: THIS
    return render(request, 'my_appointments.html',{'my_appointments': my_appointments, 'specialties': specialties})
    

def cancel_appointment(request, id_appointment):
    appointment=Appointment.objects.get(id=id_appointment)
    if request.user != appointment.patient: 
        #IF is NOT the correct user, the owner:
        messages.add_message(request, constants.WARNING, "Only doctors can cancel an appointment!")
        return redirect('/patients/home')
    else:
        appointment.status='F' #Get finished appointments
        #appointment.delete()Delete required appointment
        appointment.save() #Save it to the DB.
        return redirect(f'/patients/make_appointment/{id_appointment}')
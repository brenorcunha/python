from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import drData, Specialties, openAgenda, isDoctor
from datetime import date, datetime, timedelta
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
            my_appointments = Appointment.objects.filter(open_agenda__user=request.user, open_agenda__date__gte=today, open_agenda__date__lt=today+timedelta(days=7))
            
            specialties = Specialties.objects.all()
            return render(request, "home.html", {'doctors': doctors, 'specialties': specialties, 
                                                'isDoctor': isDoctor(request.user), 'my_appointments': my_appointments})

#escolher_horario: 
@login_required
def make_schedule(request, id_doctor):
    if request.method=="GET":
        doctor = drData.objects.get(id=id_doctor) #getting dr's agenda
        open_agenda = openAgenda.objects.filter(user=doctor.user, date__gte= datetime.now(), scheduled=False)
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
        schedule.save() #Saves the new scheduled appointment
        open_agenda.scheduled = True #Update this value, only in the temp memory.
        open_agenda.save() #Saves it to the DB.
        messages.add_message(request, constants.SUCCESS, "Appointment successfully scheduled!")
        
        return redirect('/patients/my_appointments')

#consulta
@login_required
def appointment(request, id_appointment):
    if request.method=="GET":
        my_appointments = Appointment.objects.get(id=id_appointment)
        #using the 'open_agenda' attribute from doctor's view to get it's name: 
        dr_data = drData.objects.get(user=my_appointments.open_agenda.user)
        documents = Document.objects.filter(appointment=my_appointments)
        return render(request, 'appointment.html', {'my_appointments': my_appointments, 'dr_data': dr_data, 'documents ': documents})

#minhas_consultas
@login_required
def my_appointments(request):
    specialty = request.GET.get('medical_specialties')
    appointment_date = request.GET.get('date')
    cancel = request.GET.get('cancel')
    
    today = datetime.now().date()
    my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date=today, status='S')
    #rem_appointments = Appointment.objects.exclude(id__in=appointments_today.values('id'), open_agenda__user=request.user) #Don't show the earlier appointments.
    
    rem_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date__gt=date.today(), status='S')

    if appointment_date:
       my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date__gte=appointment_date, status='S')
    if specialty:
        my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__user__drData__specialty__id=specialty, status='S')
    
    specialties = Specialties.objects.all()
    #using the 'open_agenda' attribute from doctor's view to get it's name: THIS
    return render(request, 'my_appointments.html',{'my_appointments': my_appointments, 'rem_appointments': rem_appointments, 'specialties': specialties})
    

def cancel_appointment(request, id_appointment):
    appointment=Appointment.objects.get(id=id_appointment)
    if request.user != appointment.patient: 
        #IF is NOT the correct user, the owner:
        messages.add_message(request, constants.WARNING, "Only the patient can cancel an appointment!")
        return redirect('/patients/home')
    else:
        appointment.status='C' #Get finished appointments
        appointment.save() #Save it to the DB.
        appointment.delete() #Delete required appointment
        appointment.save() #Save it to the DB.
        return redirect(f'/patients/my_appointments')
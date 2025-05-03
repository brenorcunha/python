from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from doctors.models import drData, Specialties, openAgenda, isDoctor
from datetime import date, datetime, timedelta
from .models import Appointment, Document
from django.contrib import messages
from django.contrib.messages import constants
from django.db import transaction #Adding atomicity

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
            
            #LEMBRETES: Getting only the appointments from the current user (patient!). Then, iter over it and shows in reminders bar.   
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

#agendar horario: 
@login_required
@transaction.atomic
def open_agenda(request, id_open_agenda):
    if request.method=="GET":
        try:
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
        except:
            messages.add_message(request, constants.ERROR, "Fail on trying to open appointment!")

#consulta
@login_required
def appointment(request, id_appointment):
    if request.method=="GET":
        my_appointments = get_object_or_404(Appointment, id=id_appointment)
        #using the 'open_agenda' attribute from doctor's view to get it's name: 
        dr_data = get_object_or_404(drData, user=my_appointments.open_agenda.user)
        documents = Document.objects.filter(appointment=my_appointments)
        return render(request, 'appointment.html', {'my_appointments': my_appointments, 'dr_data': dr_data, 'documents': documents})

#minhas_consultas
@login_required
def my_appointments(request):
    specialty = request.GET.get('medical_specialties')
    appointment_date = request.GET.get('date')
    #cancel = request.GET.get('cancel')
    
    today = datetime.now().date()
    my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date=today, status='S')
    #rem_appointments = Appointment.objects.exclude(id__in=appointments_today.values('id'), open_agenda__user=request.user) #Don't show the earlier appointments.
    
    rem_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date__gt=date.today(), status='S')

    if appointment_date:
       my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__date__gte=appointment_date, status='S')
    if specialty:
        my_appointments = Appointment.objects.filter(patient=request.user, open_agenda__user__drData__specialty__id=specialty, status='S')
    
    specialties = Specialties.objects.all()
    #using the 'open_agenda' attribute from doctor's view to get its name: THIS
    return render(request, 'my_appointments.html',{'my_appointments': my_appointments, 'rem_appointments': rem_appointments, 'specialties': specialties})
    
@transaction.atomic
@login_required
def cancel_appointment(request, id_appointment):
    try:
        appointment=get_object_or_404(Appointment, id=id_appointment)
        if request.user != appointment.patient:
            #IF is NOT the correct user, the owner:
            messages.add_message(request, constants.WARNING, "Only the patient can cancel an appointment!")
            return redirect('/patients/home')
        else:
            try:
                appointment.status='C' #Get finished appointments
                appointment.save() #Save it to the DB.
                appointment.delete() #Delete required appointment
                appointment.save() #Save it to the DB.
                return redirect(f'/patients/my_appointments')
            except:
                messages.add_message(request, constants.ERROR, "Fail on trying to alter the appointments. try again!")
    except Appointment.DoesNotExist:
        messages.add_message(request, constants.ERROR , 'The apppointment was not found!')
        return redirect('/patients/home')
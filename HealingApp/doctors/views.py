from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Specialties, drData, isDoctor,openAgenda
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta
from patients.models import Appointment

@login_required
# Create your views here.
def register_doctors(request):
    #If doctor is registered, would not allow him to access the register doctor page: 
    dataLogged = drData.objects.filter(user=request.user)
    if dataLogged.exists():
        messages.add_message(request, constants.WARNING, "You cannot access this page.")
        return redirect('doctors/open_agenda.html')
    if request.method=="GET":
        specialties = Specialties.objects.all() #Getting data from DB. In this case, all data (fields).
        return render(request, 'register_doctors.html', {'specialties': specialties})
    elif request.method=="POST":
        crm = request.POST.get('crm' )
        name = request.POST.get('name')
        cep = request.POST.get('cep')
        street =request.POST.get('street')
        neighborhood = request.POST.get('neighborhood')
        number = request.POST.get('number')
        medicalID = request.FILES.get('medicalID')
        rg = request.FILES.get('rg')
        photo = request.FILES.get('photo')
        specialty = request.POST.get('specialty')
        description = request.POST.get('description')
        appointmentValue = request.POST.get('appointmentValue')
        """
         Specialties require an instance, so if we would do that:
        Ex.: s = specialties.objects.filter(specialty=specialty).first()
        """
        dr_data = drData(
            crm=crm,
            name=name,
            cep=cep,
            street=street,
            neighborhood=neighborhood,
            number=number,
            medicalID=medicalID,
            rg=rg,
            photo=photo,
            specialty_id=specialty,
            description=description,
            appointmentValue=appointmentValue,
            user=request.user
        )
        dr_data.save()
        
        messages.add_message(request, constants.SUCCESS, "Doctor registered successfully!")
        return redirect("doctors/open_agenda")
    
@login_required
def open_agenda(request):
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, "Only doctors can open agenda!")
        return redirect('users/logout')
    
    if request.method == "GET":
        dr_data = drData.objects.get(user=request.user)
        open_agenda = openAgenda.objects.filter(user=request.user)
        
        return render(request, 'open_agenda.html', {'Doctor data: ', dr_data, 'Open agenda:', open_agenda})
    elif request.method=="POST":
        date = request.post.get('date')
        #Formating date with datetime library, another way is awful to use!
        formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
        if formatted_date <= datetime.now():
            messages.add_message(request, constants.WARNING, " The date cannot earlier than today.")
            return("doctors/open_agenda")
        
        appointment_open=openAgenda(
            date=date,
            user=request.user,
            
        ) 
        appointment_open.save()
        messages.add_message(request, constants.SUCCESS, "Appointment shceduled successfully!")
        return redirect('doctors/open_agenda')

def appointments_dr(request):
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, "Only doctors can open agenda!")
        today = datetime.now().date()
        #The line says: Today appointments = filter(doctor=logged doctor) filter (Opened appointments are from tpday or tomorrow (today+1 day)): 
        appointments_today = Appointment.objects.filter(open_agenda__user=request.user).filter(open_agenda__date__gte=today).filter(open_agenda__date__lt= today + timedelta(days=1))
        rem_appointments = Appointment.objects.exclude(id__in=appointments_today.values('id')) #Don't show the earlier appointments.
        return (request, 'appointments_dr.html', {'appointments_today:', appointments_today, 'rem_appointments: ', rem_appointments} )
from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Specialties, drData, isDoctor,openAgenda
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta
from patients.models import Appointment, Document, User
from django.db.models import Count
from django.urls import reverse

@login_required
# Create your views here.
def register_doctors(request):
    #If doctor is registered, would not allow him to access the register doctor page: 
    if isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'You are a doctor already.')
        return redirect('/doctors/open_agenda')
    if request.method=="GET":
        specialties = Specialties.objects.all() #Getting data from DB. In this case, all data (fields).
        print(specialties)
        return render(request, 'register_doctors.html', {'specialties': specialties, 'isDoctor': isDoctor(request.user)})
    elif request.method=="POST":
        crm = request.POST.get('crm' )
        name = request.POST.get('name')
        cep = request.POST.get('cep')
        street =request.POST.get('street')
        neighborhood = request.POST.get('neighborhood')
        number = request.POST.get('number')
        medicalID = request.FILES.get('medicalID') #old 'cim' field
        rg = request.FILES.get('rg')
        photo = request.FILES.get('photo')
        specialty = request.POST.get('specialty')
        description = request.POST.get('description')
        appointmentValue = request.POST.get('appointmentValue')
        '''
         Specialties require an instance, so if we would do that:
        Ex.: s = specialties.objects.filter(specialty=specialty).first()
        '''
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
            user=request.user,
            specialty_id=specialty,
            description=description,
            appointmentValue=appointmentValue
        )
        dr_data.save()
        
        messages.add_message(request, constants.SUCCESS, 'Doctor registered successfully!')
        return redirect('/doctors/open_agenda')
    
@login_required #abrir_horario
def open_agenda(request):
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'Only doctors can open agenda!')
        return redirect('/users/logout')
    elif request.method == "GET":
        dr_data = drData.objects.get(user=request.user)
        open_agenda = openAgenda.objects.filter(user=request.user)
        
        return render(request, 'open_agenda.html', {'dr_data': dr_data, 'open_agenda': open_agenda, 'isDoctor': isDoctor(request.user)})
    elif request.method=="POST":
        #Formating date with datetime library: 
        date = request.POST.get('date')
        formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
        #local_date = datetime.stftime(formatted_date, '%d/%m/%Y%H:%M')
        if formatted_date <= datetime.now():
            messages.add_message(request, constants.WARNING, ' The date cannot earlier than today.')
            return redirect('/doctors/open_agenda')
        
        new_appointment=openAgenda(
            date=date,
            user=request.user,
            scheduled = False
        )
        new_appointment.save()
        
        messages.add_message(request, constants.SUCCESS, 'Appointment scheduled successfully!')
        return redirect('/doctors/open_agenda')
    
@login_required
def appointments_dr(request):
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'Only doctors can open agenda!')
        return redirect('/users/logout')
    else:
        specialty = request.GET.get('medical_specialties')
        appointment_date = request.GET.get('date')
        today = datetime.now().date()
        
        appointments_today = Appointment.objects.filter(open_agenda__user=request.user, open_agenda__date__gte=today, status__in=['I','S'])
        if appointment_date:
            appointments_today = appointments_today.filter(open_agenda__date=appointment_date)
        if specialty:
            appointments_today = appointments_today.filter(open_agenda__user__drData__specialty__id=specialty)
        
        rem_appointments = Appointment.objects.filter(open_agenda__user=request.user). exclude(id__in=appointments_today.values('id'))
        
        specialties = Specialties.objects.all()
        return render(request, 'appointments_dr.html', {'appointments_today': appointments_today, 'rem_appointments': rem_appointments,'specialties': specialties, 'isDoctor': isDoctor(request.user)})

@login_required
def appointments_dr_area(request, id_appointment):
    try:
        if request.method=="GET":
            appointment=get_object_or_404(Appointment, id=id_appointment)
            documents = Document.objects.filter(appointment=appointment) #Getting all the doctor's document files sent.
            return render(request, 'appointments_dr_area.html', {'appointment': appointment, 'isDoctor': isDoctor, 'documents': documents})
        elif request.method=="POST":
            appointment=Appointment.objects.get(id=id_appointment)
            link=request.POST.get('link')
            if appointment.status in ['C', 'F']:
                messages.add_message(request, constants.WARNING, f'Consultation already {appointment.get_status_display()}! No operations available.')
                return redirect(reverse('appointments_dr_area', args=[id_appointment]))
            
            appointment.link =link
            appointment.status = 'S'
            appointment.save()
            messages.add_message(request, constants.SUCCESS, 'Started consultation.')
        return (request, 'appointments_dr_area.html', {
            'appointment': appointment,
            'isDoctor': isDoctor(request.user),
            'documents': documents
        })
    except Appointment.DoesNotExist:
         messages.add_message(request, constants.ERROR, 'Appointment NOT FOUND!')
         return redirect(reverse('appointments_dr'))
@login_required
def finish_appointment(request, id_appointment):
    appointment=get_object_or_404(Appointment, id=id_appointment)
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'Only doctors can open agenda!')
        return redirect('/users/logout')
    
    # DEFENSIVE CODE: Verifying if the user logged is the doctor rsponsaible for the appointment, if NOT, do not allow!
    if request.user!=appointment.open_agenda.user:
        messages.add_message(request, constants.ERROR, 'You cannot finish this appointment!')
        return redirect(reverse('open_agenda')) #Take the user back to the page.
    
    appointment.status='F' #Get finished appointments
    appointment.save() #Save it to the DB.
    messages.add_message(request, constants.SUCCESS, 'Appointment successfully canceled/ finished')
    return redirect(reverse('appointments_dr_area', args=[id_appointment])) #Take the user back to the page.

@login_required
def add_document(request, id_appointment):
    appointment=get_object_or_404(Appointment, id=id_appointment)
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'Only doctors can open agenda!')
        return redirect('/users/logout')
    
    if request.user!=appointment.open_agenda.user:
        messages.add_message(request, constants.ERROR, 'You cannot finish this appointment!')
        return redirect(reverse('open_agenda')) #Take the user back to the page.
    document = request.FILES.get('documento')
    title = request.POST.get('titulo')
    
    if not document:
        messages.add_message(request, constants.ERROR('You must fill the <document> field.'))
        return redirect(reverse('appointments_dr_area', args=[id_appointment])) 
    new_document = Document(
        appointment=appointment,
        title=title,
        document=document
    )
    new_document.save()
    messages.add_message(request, constants.SUCCESS, 'Document successfully created.')
    return redirect(reverse('appointments_dr_area', args=[id_appointment]))

@login_required
def dashboard(request):
    if not isDoctor(request.user):
        messages.add_message(request, constants.WARNING, 'Only doctors can open the dashboard!')
        return redirect('/users/logout')

    # Consulta correta com agregação
    appointments = Appointment.objects.filter(open_agenda__user=request.user, open_agenda__date__range=[datetime.now().date() - timedelta(days=7), datetime.now().date() + timedelta(days=1)]).annotate(quantity=Count('id')).values('open_agenda__date', 'quantity')

    dates = [i['open_agenda__date'].strftime("%d/%m/%Y") for i in appointments]
    quantity = [i['quantity'] for i in appointments]

    return render(request, 'dashboard.html', {'dates': dates, 'quantity': quantity})

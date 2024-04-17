from django.shortcuts import render
from doctors.models import drData, Specialties, openAgenda
from datetime import datetime
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

def make_schedule(request, id_drData):
    if request.method=="GET":
        doctor = drData.objects.get(id=id_drData)
        open_agenda = openAgenda.objects.filter(user=doctor.user).filter(openAgenda.date__gtm >=datetime.now).filter(scheduled=False)
        return render(request, 'make_schedule.html')
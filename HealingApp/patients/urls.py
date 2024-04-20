from django.urls import path
from . import views

urlpatterns = [
    path('home/',  views.home,  name='home'),
    path('make_schedule/<int:id_make_schedule>', views.make_schedule, name='make_schedule'), #Choose an hour.
    path('open_agenda/<int:id_open_agenda>', views.open_agenda, name="open_agenda"), #Schedule an hour.
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('appointment/<int:id_appointment>', views.make_appointment, name="make_appointment"),
    path('exclude_appointment/<int:id_appointment>', views.exclude_appointment, name='exclude_appointment')
]
#id_make_schedule is the doctor ID for getting his agenda.
from django.urls import path
from . import views
app_name='patients',
urlpatterns = [
    path('home/',  views.home,  name='home'),
    path('make_schedule/<int:id_make_schedule>', views.make_schedule, name='make_schedule'), #Choose an hour.
    path('open_agenda/<int:id_open_agenda>', views.open_agenda, name="open_agenda"), #Schedule an hour.
    path('my_appointments/', views.my_appointments, name='my_appointments'),
]
#id_make_schedule is the doctor ID for getting his agenda.
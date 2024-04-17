from django.urls import path
from . import views

app_name='doctors'
urlpatterns =[
    path('register_doctors/', views.register_doctors, name='register_doctors'),
    path('open_agenda/', views.open_agenda, name='open_agenda')
]
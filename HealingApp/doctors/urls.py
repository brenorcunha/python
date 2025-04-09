from django.urls import path
from . import views

urlpatterns = [
    path('register_doctors/', views.register_doctors, name="register_doctors"),
    path('open_agenda/', views.open_agenda, name="open_agenda"),
    path('appointments_dr/', views.appointments_dr, name="appointments_dr"),
    path('appointments_dr_area/<int:id_appointment>', views.appointments_dr_area, name='appointments_dr_area'),
    path('finish_appointment/<int:id_appointment>', views.finish_appointment, name="finish_appointment"),
    path('add_document/<int:id_appointment>', views.add_document, name="add_document"),
    path('dashboard', views.dashboard, name="dashboard")
]
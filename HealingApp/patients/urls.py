from django.urls import path
from . import views

urlpatterns = [
    path('home/',  views.home,  name='home'),
    path('make_schedule/', views.make_schedule, name='make_schedule')
]
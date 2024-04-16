from django.urls import path
from . import views

urlpatterns =[
    path('register_doctors/', views.register_doctors)
]
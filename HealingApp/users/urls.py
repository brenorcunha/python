# File that must contain all the URL's to be handled for this module/ miniApp.
from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
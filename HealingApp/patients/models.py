import importlib
from django.db import models
from django.contrib.auth.models import User
from doctors.models import openAgenda


class Appointment(models.Model):
    status_choices = (
        ('S', 'Scheduled'),
        ('F', 'Finished'),
        ('C', 'Cancelled'),
        ('I', 'Initialized')
    )
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    open_agenda = models.ForeignKey(openAgenda, on_delete=models.DO_NOTHING) #data_aberta: The doctor is the only one who opens the agenda.
    status = models.CharField(max_length=1, choices=status_choices, default='S')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.patient.username
    
class Document(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=30)
    document = models.FileField(upload_to='documents')
    
    def __str__(self):
        return self.title
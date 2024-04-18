from django.db import models
from django.contrib.auth.models import User
from doctors.models import openAgenda

class Appointment(models.Model):
    status_choices = (
        ('S', 'Scheduled'),
        ('F', 'Finished'),
        ('C', 'Cancelled'),
        ('1', 'Started')

    )
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    open_agenda = models.ForeignKey(openAgenda, on_delete=models.DO_NOTHING) #The doctor is the only one opens the agenda.
    status = models.CharField(max_length=1, choices=status_choices, default='S')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.patient.username
    

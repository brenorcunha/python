from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
def isDoctor(user):
    return drData.objects.filter(user=user).exists()

class Specialties(models.Model):
    specialty = models.CharField(max_length=50)
    #icon = models.ImageField(upload_to="icons", null=True, blank=True)
    
    def __str__(self):
        return self.specialty
    
"""After creating here:
1- Add to the root 'seetings.py' the name of the module: 'doctors'
2- python3 manage.py makemigrations Create migrations
3- python3 manage.py migrate Save them to the DB.

4-Creating admin user:
python3 manage.py createsuperuser
Can log @ admin-area
"""

class drData(models.Model):
    crm = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=50)
    number = models.IntegerField()
    rg = models.ImageField(upload_to='rgs')
    medicalID = models.ImageField(upload_to='mid')
    photo = models.ImageField(upload_to='photos')
    description = models.TextField(null=True, blank=True)
    appointmentValue = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    specialty = models.ForeignKey(Specialties, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.user.username
    
    """"Appointment value:
    After creating this class, with the rg (brazilian ID) we have to store an image or a PDF. Query at 'settings;py'
    the following parameters (MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  & MEDIA_URL = '/media/').
    In programming, WE DON'T INSERT IMAGES OR PDF's in the DB, we upload to a specific folder & refers to it in the table.
    """

    @property
    def next_date(self):
        next_date = openAgenda.objects.filter(user=self.user, date__gte=datetime.now(), scheduled=False).order_by('date')#Getting all the available dates of appointment but ONLY FROM THE CURRENT DR.
        #'data_gt' is an adavanced filter Greater than, we also have (lt=less than,lte=less or equal than, gte=greater or equal than)
        return next_date
    
    def next_sched_date(self):
        next_sched_date = openAgenda.objects.filter(user=self.user, date__gte=datetime.now(), date__lte=datetime.now()+timedelta(days=7), scheduled=True).order_by('date')
        return next_sched_date

class openAgenda(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) #getting Doctor ID from DB.
    scheduled = models.BooleanField(default=False) #For getting IF the 'hour' is already scheduled.
    
    def __str__(self):
        return str(self.date)
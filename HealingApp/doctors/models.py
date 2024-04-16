from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def isDoctor(user):
    return drData.objects.filter(user==user).exists()
class Specialties(models.Model):
    specialty = models.CharField(max_length=50)
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
    description = models.TextField()
    appointmentValue = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    specialty = models.ForeignKey(Specialties, on_delete=models.DO_NOTHING)
    
""""
 After creating this class, with the rg (brazilian ID) we have to store an image or a PDF. Query at 'settings;py'
 the following parameters (MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  & MEDIA_URL = '/media/').
 In programming, wWE DON'T INSERT IMAGES OR PDF's in the DB, we upload to a specific folder & refers to it in the table.
"""
def __str__(self):
    return self.user.username
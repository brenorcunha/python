from django.contrib import admin
from .models import Specialties, drData

# Register the data (DB, table) from here to the admin area.
admin.site.register(Specialties)
admin.site.register(drData)
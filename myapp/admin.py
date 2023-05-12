from django.contrib import admin
from .models import User,Doctor,Appointment
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Appointment)
from django.contrib import admin

# Register your models here.
from . models import *

class Doctor_Display(admin.ModelAdmin):
    list_display = ['Name','Specialist']


admin.site.register(Doctor,Doctor_Display)
admin.site.register(Speciality)

admin.site.register(Shift)
admin.site.register(Nurse)
admin.site.register(Gender)
admin.site.register(Room_Service)

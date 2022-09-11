from django.contrib import admin

# Register your models here.
from .models import DiseaseDoctorRelation, SymptomsforMultiselector


admin.site.register(DiseaseDoctorRelation)
admin.site.register(SymptomsforMultiselector)
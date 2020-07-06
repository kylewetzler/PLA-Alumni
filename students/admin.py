from django.contrib import admin
from .models import OfferedMajor, StudentOrganization, GraduationDate

# Register your models here.
admin.site.register(OfferedMajor)
admin.site.register(StudentOrganization)
admin.site.register(GraduationDate)
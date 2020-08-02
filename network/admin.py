from django.contrib import admin
from network.models import Alumni, Degree, InvolvementOrLeadershipPosition, JobSector, Occupation, Expectation
# Register your models here.

admin.site.register(Alumni)
admin.site.register(Degree)
admin.site.register(InvolvementOrLeadershipPosition)
admin.site.register(JobSector)
admin.site.register(Occupation)
admin.site.register(Expectation)
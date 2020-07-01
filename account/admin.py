from django.contrib import admin
from .models import Account, USStates, Country, City

admin.site.register(Account)
admin.site.register(USStates)
admin.site.register(Country)
admin.site.register(City)


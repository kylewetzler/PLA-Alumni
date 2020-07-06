from django.contrib import admin
from .models import Account, USState, Country, City, Location, ContactMethod

admin.site.register(Account)
admin.site.register(USState)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(ContactMethod)


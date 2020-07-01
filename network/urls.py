from django.urls import path

from .views import (
    all_alumni_view,
)

urlpatterns = [
    path('all/', all_alumni_view, name='all_alumni'),
]
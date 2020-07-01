from django.urls import path

from .views import (
    all_students_view,
)

urlpatterns = [
    path('all/', all_students_view, name='all_students'),
]
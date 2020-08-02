from django.shortcuts import render, redirect
from network.models import Alumni
from django.contrib.auth import get_user_model
from .forms import AlumniDataForm

User = get_user_model()

def alumni_response_view(request, alum_id):
    context = {}
    context['response'] = Alumni.objects.get(id=alum_id)

    return render(request, 'responses/response.html', context)


def add_alumni_response_view(request):
    context = {}

    new_alumni_data_form = AlumniDataForm(prefix='alumniDataForm')
    context['alumni_data_form'] = new_alumni_data_form

    return render(request, 'responses/add_response.html', context)


def all_alumni_view(request):
    context = {}
    alumni = User.objects.filter(is_alumnus=True).order_by('last_name')
    context['alumni'] = alumni
    return render(request, 'alumni/all_alumni.html', context)

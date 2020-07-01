from django.shortcuts import render, HttpResponse
from network.models import Alumni
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required()
def home_page_view(request):
    context = {}
    responses = Alumni.objects.all().order_by('full_name')
    context['responses'] = responses
    return render(request, 'home/home.html', context)

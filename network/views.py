from django.shortcuts import render, redirect
from network.models import Alumni
from django.contrib.auth import get_user_model

User = get_user_model()

def alumni_response_view(request, alum_id):
    context = {}
    context['response'] = Alumni.objects.get(id=alum_id)
    return render(request, 'responses/response.html', context)


def add_alumni_response_view(request):
    context = {}
    if request.POST:
        a = Alumni(
            email=request.POST['email'],
            full_name=request.POST['full_name'],
            hometown=request.POST['hometown'],
            residence=request.POST['residence'],
            degree=request.POST['degree'],
            changed_major=request.POST['changed_major'],
            original_major=request.POST['original_major'],
            leadership=request.POST['leadership'],
            grad_date=request.POST['grad_date'],
            current_occupation=request.POST['current_occupation'],
            career_long_term=request.POST['career_long_term'],
            expected_career=request.POST['expected_career'],
            career_path=request.POST['career_path'],
            favorites=request.POST['favorites'],
            mentorship_selections=request.POST['mentorship_selections'],
            conference_location=request.POST['conference_location'],
            conference_topics=request.POST['conference_topics'],
            contact_method=request.POST['contact_method']
        )
        a.save()
        new_response = Alumni.objects.get(full_name=request.POST['full_name'])
        return redirect('view_response', alum_id=new_response.id)
    return render(request, 'responses/add_response.html', context)


def all_alumni_view(request):
    context = {}
    alumni = User.objects.filter(is_alumnus=True).order_by('last_name')
    context['alumni'] = alumni
    return render(request, 'alumni/all_alumni.html', context)

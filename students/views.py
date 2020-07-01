from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def all_students_view(request):
    context = {}
    students = User.objects.filter(is_student=True).order_by('last_name')
    context['students'] = students
    return render(request, 'students/all_students.html', context)



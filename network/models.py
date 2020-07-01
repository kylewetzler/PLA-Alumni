from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Alumni(models.Model):
    email = models.EmailField(max_length=60)
    full_name = models.CharField(max_length=60, blank=False)
    hometown = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    changed_major = models.CharField(max_length=10)
    original_major = models.CharField(max_length=75)
    leadership = models.TextField(max_length=255)
    grad_date = models.CharField(max_length=100)
    current_occupation = models.TextField(max_length=255)
    career_long_term = models.TextField(max_length=255)
    expected_career = models.TextField(max_length=255)
    career_path = models.CharField(max_length=200)
    favorites = models.TextField(max_length=255)
    mentorship_selections = models.CharField(max_length=200)
    conference_location = models.CharField(max_length=200)
    conference_topics = models.TextField(max_length=255)
    contact_method = models.CharField(max_length=200)


class AlumniData(models.Model):
    alumni = models.ForeignKey(User, blank=False, related_name='alumni', on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth import get_user_model
from account.models import Location, ContactMethod
from students.models import OfferedMajor, StudentOrganization, GraduationDate

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


class Degree(models.Model):
    alumnus = models.ForeignKey(User, blank=False, related_name='alumnus_degree', on_delete=models.CASCADE)
    degree = models.ForeignKey(OfferedMajor, on_delete=models.DO_NOTHING)


class InvolvementOrLeadershipPosition(models.Model):
    alumnus = models.ForeignKey(User, blank=False, related_name='alumnus_position', on_delete=models.CASCADE)
    organization = models.ForeignKey(StudentOrganization, on_delete=models.DO_NOTHING)
    position = models.TextField()


class JobSector(models.Model):
    sector = models.CharField(max_length=50)


class Occupation(models.Model):
    sector = models.ForeignKey(JobSector, on_delete=models.DO_NOTHING)
    description = models.TextField()


class Expectation(models.Model):
    expected = models.BooleanField(default=True)
    description = models.TextField()


class AlumniData(models.Model):
    alumnus = models.ForeignKey(User, blank=False, related_name='alumnus_data', on_delete=models.CASCADE)
    hometown = models.ForeignKey(Location, related_name='hometown', on_delete=models.DO_NOTHING)
    current_residence = models.ForeignKey(Location, related_name='currents_residence', on_delete=models.DO_NOTHING)
    changed_major = models.BooleanField(default=False)
    original_major = models.ForeignKey(OfferedMajor, on_delete=models.DO_NOTHING)
    grad_date = models.ForeignKey(GraduationDate, on_delete=models.DO_NOTHING)
    current_occupation = models.ForeignKey(Occupation, on_delete=models.DO_NOTHING)
    expected_career = models.ForeignKey(Expectation, related_name='expected_career', on_delete=models.DO_NOTHING)
    career_long_term = models.ForeignKey(Expectation, related_name='career_long_term', on_delete=models.DO_NOTHING)
    career_path = models.CharField(max_length=200)
    favorites = models.TextField()
    mentor_resume = models.BooleanField(default=False)
    mentor_cover_letter = models.BooleanField(default=False)
    mentor_job_search = models.BooleanField(default=False)
    mentor_ugrad_opportunities = models.BooleanField(default=False)
    mentor_connections = models.BooleanField(default=False)
    mentor_moving = models.BooleanField(default=False)
    conference_location = models.ForeignKey(Location, related_name='conference_locaiton', on_delete=models.DO_NOTHING)
    conference_topics = models.TextField()
    contact_method = models.ForeignKey(ContactMethod, on_delete=models.DO_NOTHING)




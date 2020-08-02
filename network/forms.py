from django.forms import ModelForm
from .models import AlumniData
from account.models import Location

class AlumniDataForm(ModelForm):
    class Meta:
        model = AlumniData
        fields = ['hometown', 'current_residence', 'changed_major', 'original_major', 'grad_date', 'current_occupation',
                  'expected_career', 'career_long_term', 'career_path', 'favorites', 'mentor_resume',
                  'mentor_cover_letter', 'mentor_job_search', 'mentor_connections', 'mentor_moving',
                  'mentor_ugrad_opportunities', 'conference_location', 'conference_topics', 'contact_method']


class HometownForm(ModelForm):
    class Meta:
        model = Location
        fields
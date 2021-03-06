# Generated by Django 2.2.12 on 2020-07-05 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0012_account_phone_number'),
        ('students', '0004_graduationdate'),
        ('network', '0011_expectation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_major', models.BooleanField(default=False)),
                ('career_path', models.CharField(max_length=200)),
                ('favorites', models.TextField()),
                ('mentor_resume', models.BooleanField(default=False)),
                ('mentor_cover_letter', models.BooleanField(default=False)),
                ('mentor_job_search', models.BooleanField(default=False)),
                ('mentor_ugrad_opportunities', models.BooleanField(default=False)),
                ('mentor_connections', models.BooleanField(default=False)),
                ('mentor_moving', models.BooleanField(default=False)),
                ('conference_topics', models.TextField()),
                ('alumnus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_data', to=settings.AUTH_USER_MODEL)),
                ('career_long_term', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='career_long_term', to='network.Expectation')),
                ('conference_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conference_locaiton', to='account.Location')),
                ('contact_method', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.ContactMethod')),
                ('current_occupation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='network.Occupation')),
                ('current_residence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currents_residence', to='account.Location')),
                ('expected_career', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='expected_career', to='network.Expectation')),
                ('grad_date', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.GraduationDate')),
                ('hometown', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hometown', to='account.Location')),
                ('original_major', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.OfferedMajor')),
            ],
        ),
    ]

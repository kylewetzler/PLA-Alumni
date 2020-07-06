# Generated by Django 2.2.12 on 2020-07-05 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_graduationdate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0008_delete_alumnidata'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvolvementOrLeadershipPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField()),
                ('alumnus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_position', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.StudentOrganization')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumnus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_degree', to=settings.AUTH_USER_MODEL)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.OfferedMajor')),
            ],
        ),
    ]
